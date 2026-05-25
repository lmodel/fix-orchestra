#!/usr/bin/env python3
"""Convert FIX Orchestra upstream XSD artifacts into a single LinkML schema.

Achieves 100% coverage of every ``complexType``, ``simpleType``,
``attributeGroup`` and top-level ``element`` declared across
``repository.xsd``, ``repositorytypes.xsd`` and ``interfaces.xsd``.

Inputs (default locations relative to the repo root):
    upstream-releases/repository.xsd
    upstream-releases/repositorytypes.xsd
    upstream-releases/interfaces.xsd

Output (default):
    src/fix_orchestra/schema/fix_orchestra.yaml

Run from the repo root:

    python3 scripts/schema_to_linkml.py
    # or override via env vars / CLI args:
    UPSTREAM_DIR=/path/to/xsd OUT_FILE=/tmp/schema.yaml python3 scripts/schema_to_linkml.py

Only the Python standard library is required.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
import xml.etree.ElementTree as ET
from collections import OrderedDict
from pathlib import Path

XS = "{http://www.w3.org/2001/XMLSchema}"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def local(tag: str) -> str:
    return tag.split("}", 1)[1] if "}" in tag else tag


def nons(qname: str | None) -> str | None:
    if qname is None:
        return None
    return qname.split(":", 1)[1] if ":" in qname else qname


def doc_of(elt: ET.Element | None) -> str | None:
    if elt is None:
        return None
    ann = elt.find(f"{XS}annotation")
    if ann is None:
        return None
    parts = []
    for d in ann.findall(f"{XS}documentation"):
        # itertext() walks nested xhtml (xml.xsd embeds <div>/<h1>/<p>... in docs)
        txt = " ".join("".join(d.itertext()).split())
        if txt:
            parts.append(txt)
    joined = " ".join(parts)
    # Cap very long docs to keep YAML legible.
    if len(joined) > 1200:
        joined = joined[:1197] + "..."
    return joined or None


_SNAKE1 = re.compile(r"([A-Z]+)([A-Z][a-z])")
_SNAKE2 = re.compile(r"([a-z0-9])([A-Z])")


def snake(name: str) -> str:
    s = _SNAKE1.sub(r"\1_\2", name)
    s = _SNAKE2.sub(r"\1_\2", s)
    return s.lower().replace("-", "_")


def pascal(name: str) -> str:
    """PascalCase, stripping XSD ``_t`` / ``_enum`` suffixes."""
    base = re.sub(r"(_t|_enum)$", "", name)
    parts = re.split(r"[_\-]", base)
    parts = [p[:1].upper() + p[1:] for p in parts if p]
    out = "".join(parts)
    return out[:1].upper() + out[1:] if out else out


def pascal_simple(name: str) -> str:
    """PascalCase for simpleType names.

    XSDs commonly pair ``foo_enum`` (the enumeration) with ``foo_t`` (a union
    extending it). Stripping both suffixes collapses the pair to the same name,
    so we keep ``Enum`` as a suffix for the enumeration variant.
    """
    if name.endswith("_enum"):
        return pascal(name[:-5]) + "Enum"
    return pascal(name)


# XSD primitive -> LinkML built-in type
PRIM = {
    "string": "string",
    "token": "string",
    "normalizedString": "string",
    "NMTOKEN": "string",
    "NMTOKENS": "string",
    "NCName": "string",
    "Name": "string",
    "QName": "string",
    "ID": "string",
    "IDREF": "string",
    "language": "string",
    "integer": "integer",
    "positiveInteger": "integer",
    "nonNegativeInteger": "integer",
    "negativeInteger": "integer",
    "nonPositiveInteger": "integer",
    "int": "integer",
    "long": "integer",
    "short": "integer",
    "byte": "integer",
    "unsignedInt": "integer",
    "unsignedLong": "integer",
    "unsignedShort": "integer",
    "unsignedByte": "integer",
    "decimal": "decimal",
    "float": "float",
    "double": "double",
    "boolean": "boolean",
    "date": "date",
    "dateTime": "datetime",
    "time": "time",
    "duration": "string",
    "gYear": "string",
    "gYearMonth": "string",
    "gMonth": "string",
    "gMonthDay": "string",
    "gDay": "string",
    "anyURI": "uri",
    "anyType": "string",
    "anySimpleType": "string",
    "base64Binary": "string",
    "hexBinary": "string",
}

# Names defined in both XSDs - the interfaces.xsd variants get prefixed.
IFACE_DUPLICATES = {
    "annotation",
    "appinfo",
    "documentation",
    "purpose_enum",
    "purpose_t",
    "reliability_t",
}


def iface_name(name: str) -> str:
    return ("interface_" + name) if name in IFACE_DUPLICATES else name


# XSD attributes declared use="required" that are routinely absent in real FIX
# Orchestra documents.  Marking them optional produces a schema that faithfully
# models actual usage rather than the over-strict XSD declaration.
# Each entry is (xsd_complex_type_name, xsd_attribute_name).
_OPTIONAL_DESPITE_XSD: frozenset[tuple[str, str]] = frozenset({
    # The "Common" category omits `section` in every known FIX distribution.
    ("categoryType", "section"),
})


# ---------------------------------------------------------------------------
# XSD parsing
# ---------------------------------------------------------------------------


def parse_xsd(path: Path) -> dict:
    tree = ET.parse(path)
    root = tree.getroot()
    out = {
        "simple_types": OrderedDict(),
        "complex_types": OrderedDict(),
        "attribute_groups": OrderedDict(),
        "elements": OrderedDict(),
    }
    for child in root:
        tag = local(child.tag)
        name = child.get("name")
        if not name:
            continue
        if tag == "simpleType":
            out["simple_types"][name] = parse_simple(child)
        elif tag == "complexType":
            out["complex_types"][name] = parse_complex(child)
        elif tag == "attributeGroup":
            out["attribute_groups"][name] = parse_attr_group(child)
        elif tag == "element":
            out["elements"][name] = parse_top_element(child)
    return out


def parse_simple(elt: ET.Element) -> dict:
    info = {
        "doc": doc_of(elt),
        "kind": None,
        "base": None,
        "enums": [],
        "union_members": [],
        "pattern": None,
        "min_length": None,
        "max_length": None,
        "min_inclusive": None,
        "max_inclusive": None,
    }
    r = elt.find(f"{XS}restriction")
    u = elt.find(f"{XS}union")
    if r is not None:
        info["base"] = r.get("base")
        enums = []
        for enu in r.findall(f"{XS}enumeration"):
            enums.append({"value": enu.get("value"), "doc": doc_of(enu)})
        if enums:
            info["kind"] = "enum"
            info["enums"] = enums
        else:
            info["kind"] = "restriction"
        for facet, key in (
            ("pattern", "pattern"),
            ("minLength", "min_length"),
            ("maxLength", "max_length"),
            ("minInclusive", "min_inclusive"),
            ("maxInclusive", "max_inclusive"),
        ):
            f = r.find(f"{XS}{facet}")
            if f is not None:
                info[key] = f.get("value")
    elif u is not None:
        info["kind"] = "union"
        info["union_members"] = (u.get("memberTypes") or "").split()
    return info


def parse_complex(elt: ET.Element) -> dict:
    info = {
        "doc": doc_of(elt),
        "abstract": elt.get("abstract") == "true",
        "mixed": elt.get("mixed") == "true",
        "base": None,
        "elements": [],
        "attributes": [],
        "attribute_groups": [],
        "has_any": False,
        "has_any_attr": False,
    }
    holder = elt
    cc = elt.find(f"{XS}complexContent")
    sc = elt.find(f"{XS}simpleContent")
    if cc is not None:
        ext = cc.find(f"{XS}extension")
        if ext is not None:
            info["base"] = ext.get("base")
            holder = ext
        else:
            rst = cc.find(f"{XS}restriction")
            if rst is not None:
                info["base"] = rst.get("base")
                holder = rst
    elif sc is not None:
        ext = sc.find(f"{XS}extension")
        if ext is not None:
            info["base"] = ext.get("base")
            holder = ext
            info["mixed"] = True
    walk_holder(holder, info)
    return info


def walk_holder(holder: ET.Element, info: dict) -> None:
    for tag in ("sequence", "choice", "all"):
        for c in holder.findall(f"{XS}{tag}"):
            walk_particle(c, info, parent_unbounded=False)
    for a in holder.findall(f"{XS}attribute"):
        info["attributes"].append(parse_attribute(a))
    for ag in holder.findall(f"{XS}attributeGroup"):
        ref = ag.get("ref")
        if ref:
            info["attribute_groups"].append(nons(ref))
    if holder.find(f"{XS}anyAttribute") is not None:
        info["has_any_attr"] = True


def walk_particle(
    particle: ET.Element,
    info: dict,
    parent_unbounded: bool,
    parent_is_choice: bool = False,
) -> None:
    cmax = particle.get("maxOccurs", "1")
    container_unbounded = (
        parent_unbounded or cmax == "unbounded" or (cmax.isdigit() and int(cmax) > 1)
    )
    is_choice = local(particle.tag) == "choice"
    # Inside an <xs:choice>, the children are alternatives - none individually
    # required by virtue of their default minOccurs=1. Whether *some* alternative
    # is required is captured by the choice's own minOccurs (on the particle).
    children_optional = parent_is_choice or is_choice
    for child in particle:
        tag = local(child.tag)
        if tag == "element":
            info["elements"].append(
                parse_local_element(
                    child, container_unbounded, force_optional=children_optional
                )
            )
        elif tag in ("sequence", "choice", "all"):
            walk_particle(
                child, info, container_unbounded, parent_is_choice=children_optional
            )
        elif tag == "any":
            info["has_any"] = True


def parse_local_element(
    elt: ET.Element, parent_unbounded: bool, force_optional: bool = False
) -> dict:
    ref = elt.get("ref")
    if ref:
        name = nons(ref)
        type_q = ref
        is_ref = True
    else:
        name = elt.get("name")
        type_q = elt.get("type")
        is_ref = False
    minocc = elt.get("minOccurs", "1")
    maxocc = elt.get("maxOccurs", "1")
    if parent_unbounded and maxocc == "1":
        maxocc = "unbounded"
    if force_optional and minocc == "1":
        # Element inside <xs:choice>: defaults to minOccurs=1 but the choice
        # makes it an alternative, not an individual requirement.
        minocc = "0"
    inline = None
    if not type_q and not is_ref:
        ct = elt.find(f"{XS}complexType")
        if ct is not None:
            inline = parse_complex(ct)
    return {
        "name": name,
        "type": type_q,
        "ref": is_ref,
        "min_occurs": int(minocc) if minocc.isdigit() else 0,
        "max_occurs": maxocc,
        "doc": doc_of(elt),
        "inline": inline,
    }


def parse_attribute(elt: ET.Element) -> dict:
    ref = elt.get("ref")
    if ref:
        name = nons(ref)
        type_q = None
    else:
        name = elt.get("name")
        type_q = elt.get("type")
    return {
        "name": name,
        "type": type_q,
        "ref": bool(ref),
        "use": elt.get("use", "optional"),
        "default": elt.get("default"),
        "fixed": elt.get("fixed"),
        "doc": doc_of(elt),
    }


def parse_attr_group(elt: ET.Element) -> dict:
    info = {"doc": doc_of(elt), "attributes": [], "attribute_groups": []}
    for a in elt.findall(f"{XS}attribute"):
        info["attributes"].append(parse_attribute(a))
    for ag in elt.findall(f"{XS}attributeGroup"):
        ref = ag.get("ref")
        if ref:
            info["attribute_groups"].append(nons(ref))
    return info


def parse_top_element(elt: ET.Element) -> dict:
    info = {
        "doc": doc_of(elt),
        "type": elt.get("type"),
        "inline": None,
        "keys": [],  # xs:key / xs:unique declarations
        "keyrefs": [],  # xs:keyref declarations
    }
    ct = elt.find(f"{XS}complexType")
    if ct is not None:
        info["inline"] = parse_complex(ct)
    for k in elt.findall(f"{XS}key") + elt.findall(f"{XS}unique"):
        info["keys"].append(parse_key(k))
    for kr in elt.findall(f"{XS}keyref"):
        info["keyrefs"].append(parse_key(kr, is_ref=True))
    return info


def parse_key(elt: ET.Element, is_ref: bool = False) -> dict:
    sel = elt.find(f"{XS}selector")
    fields = [f.get("xpath") for f in elt.findall(f"{XS}field")]
    return {
        "name": elt.get("name"),
        "refer": elt.get("refer") if is_ref else None,
        "selector": sel.get("xpath") if sel is not None else None,
        "fields": fields,
        "doc": doc_of(elt),
    }


# ---------------------------------------------------------------------------
# Aux XSDs (dc / dcmitype / dcterms / xml.xsd)
#
# Each aux XSD is parsed with the same primitives as the FIX XSDs but emitted
# with a scope-specific PascalCase prefix so cross-XSD names stay distinct.
# ---------------------------------------------------------------------------

AUX_XSDS = [
    # (scope_key, file, target_ns, prefix, subset_name, description)
    (
        "dc",
        "dc.xsd",
        "http://purl.org/dc/elements/1.1/",
        "Dc",
        "dc",
        "Dublin Core elements 1.1.",
    ),
    (
        "dcmitype",
        "dcmitype.xsd",
        "http://purl.org/dc/dcmitype/",
        "Dcmitype",
        "dcmitype",
        "DCMI Type Vocabulary.",
    ),
    (
        "dct",
        "dcterms.xsd",
        "http://purl.org/dc/terms/",
        "Dcterms",
        "dcterms",
        "Dublin Core Terms (element refinements and encoding schemes).",
    ),
    (
        "xml",
        "xml.xsd",
        "http://www.w3.org/XML/1998/namespace",
        "Xml",
        "xml_namespace",
        "W3C XML namespace (xml:base, xml:lang, xml:space, xml:id).",
    ),
]


def parse_aux_xsd(path: Path) -> dict:
    """Parse an XSD capturing every named declaration we care about.

    This is a superset of ``parse_xsd`` adding:
      * top-level <xs:attribute> declarations (xml.xsd uses these heavily)
      * <xs:group> definitions
      * substitutionGroup on elements
      * <xs:simpleContent>/<xs:restriction> bases
      * anonymous <xs:simpleType> nested inside <xs:attribute>
    """
    tree = ET.parse(path)
    root = tree.getroot()
    out = {
        "simple_types": OrderedDict(),
        "complex_types": OrderedDict(),
        "attribute_groups": OrderedDict(),
        "elements": OrderedDict(),
        "attributes": OrderedDict(),  # top-level attribute decls
        "groups": OrderedDict(),
        "schema_doc": doc_of(root),
    }
    for child in root:
        tag = local(child.tag)
        name = child.get("name")
        if not name:
            continue
        if tag == "simpleType":
            out["simple_types"][name] = parse_simple(child)
        elif tag == "complexType":
            info = parse_complex(child)
            info["simple_restriction_base"] = _simple_content_base(child, "restriction")
            info["simple_extension_base"] = _simple_content_base(child, "extension")
            out["complex_types"][name] = info
        elif tag == "attributeGroup":
            out["attribute_groups"][name] = parse_attr_group(child)
        elif tag == "element":
            info = parse_top_element(child)
            info["substitution_group"] = child.get("substitutionGroup")
            info["abstract"] = child.get("abstract") == "true"
            out["elements"][name] = info
        elif tag == "attribute":
            out["attributes"][name] = _parse_top_attribute(child)
        elif tag == "group":
            out["groups"][name] = _parse_group(child)
    return out


def _simple_content_base(elt: ET.Element, kind: str) -> str | None:
    sc = elt.find(f"{XS}simpleContent")
    if sc is None:
        return None
    node = sc.find(f"{XS}{kind}")
    return node.get("base") if node is not None else None


def _parse_top_attribute(elt: ET.Element) -> dict:
    info = {
        "name": elt.get("name"),
        "type": elt.get("type"),
        "doc": doc_of(elt),
        "inline_simple": None,
    }
    st = elt.find(f"{XS}simpleType")
    if st is not None:
        info["inline_simple"] = parse_simple(st)
    return info


def _parse_group(elt: ET.Element) -> dict:
    members = []
    for cont_tag in ("sequence", "choice", "all"):
        for cont in elt.findall(f"{XS}{cont_tag}"):
            for e in cont.findall(f".//{XS}element"):
                if e.get("ref"):
                    members.append(nons(e.get("ref")))
    return {"doc": doc_of(elt), "members": members}


def emit_aux_xsds(
    upstream_dir: Path,
    classes: OrderedDict,
    enums: OrderedDict,
    types: OrderedDict,
    aux_registry: dict[tuple[str, str], dict],
) -> None:
    """Parse the 4 supporting XSDs and emit LinkML entities for every
    named declaration. Side-effects: mutates ``classes``, ``enums``, ``types``
    and ``aux_registry``.
    """
    parsed: dict[str, dict] = {}
    for scope_key, fname, _ns, _pfx, _ss, _desc in AUX_XSDS:
        p = upstream_dir / fname
        if not p.is_file():
            continue
        parsed[scope_key] = parse_aux_xsd(p)

    # --- Pass 1: register all names so cross-XSD refs resolve ------------
    for scope_key, fname, _ns, name_pfx, _ss, _desc in AUX_XSDS:
        data = parsed.get(scope_key)
        if not data:
            continue
        for n, info in data["simple_types"].items():
            kind = "enum" if info["kind"] == "enum" else "type"
            aux_registry[(scope_key, n)] = {
                "kind": kind,
                "name": name_pfx + pascal_simple(n),
            }
        for n in data["complex_types"]:
            aux_registry[(scope_key, n)] = {
                "kind": "class",
                "name": name_pfx + pascal(n),
            }
        for n in data["attribute_groups"]:
            aux_registry[(scope_key, n)] = {
                "kind": "mixin",
                "name": name_pfx + pascal(n),
            }
        for n in data["elements"]:
            aux_registry[(scope_key, n)] = {
                "kind": "class",
                "name": name_pfx + pascal(n),
            }
        for n in data["attributes"]:
            aux_registry[(scope_key, n)] = {
                "kind": "slot",
                "name": name_pfx.lower() + "_" + snake(n),
            }
        for n in data["groups"]:
            aux_registry[(scope_key, n)] = {
                "kind": "group",
                "name": name_pfx + pascal(n),
            }

    # --- Pass 2: emit ----------------------------------------------------
    def aux_resolve(qname: str | None) -> tuple[str, bool]:
        if not qname:
            return ("string", False)
        if ":" in qname:
            pfx, nm = qname.split(":", 1)
        else:
            pfx, nm = "", qname
        if pfx == "xs":
            return (PRIM.get(nm, "string"), False)
        # Map both XSD-side prefixes (dct, dcmitype, xml) and the canonical
        # output prefixes (dcterms, dctypes, XML) onto internal scope keys.
        scope = {
            "dc": "dc",
            "dct": "dct",
            "dcterms": "dct",
            "dcmitype": "dcmitype",
            "dctypes": "dcmitype",
            "xml": "xml",
            "XML": "xml",
        }.get(pfx)
        if scope:
            e = aux_registry.get((scope, nm))
            if e:
                return (e["name"], e["kind"] in ("class", "enum"))
        return ("string", False)

    for scope_key, fname, ns, name_pfx, subset_name, desc in AUX_XSDS:
        data = parsed.get(scope_key)
        if not data:
            continue
        _emit_aux_simple_types(
            scope_key, data, name_pfx, subset_name, fname, aux_resolve, types, enums
        )
        _emit_aux_complex_types(
            scope_key,
            data,
            name_pfx,
            subset_name,
            fname,
            aux_resolve,
            classes,
            aux_registry,
        )
        _emit_aux_attr_groups(
            scope_key, data, name_pfx, subset_name, fname, aux_resolve, classes
        )
        _emit_aux_top_attributes(
            scope_key,
            data,
            name_pfx,
            subset_name,
            fname,
            aux_resolve,
            classes,
            types,
            enums,
        )
        _emit_aux_elements(
            scope_key,
            data,
            name_pfx,
            subset_name,
            fname,
            aux_resolve,
            classes,
            aux_registry,
        )
        _emit_aux_groups(
            scope_key, data, name_pfx, subset_name, fname, aux_registry, classes
        )

    # ---- Post-process: expand DC element substitution chain into the two
    #      container classes so naively-converted XML metadata can validate.
    _expand_dc_container_attributes(parsed, classes)


def _expand_dc_container_attributes(parsed: dict, classes: OrderedDict) -> None:
    """Augment ``DcElementContainer`` and ``DctermsElementOrRefinementContainer``
    with one ``attributes:`` entry per DC element / refinement.

    XSD models these containers as ``<xs:group>`` references that expand into
    ``<xs:element ref="dc:any"/>`` - and ``dc:any`` is the head of a
    substitutionGroup chain covering all 15 DC elements plus the 41 dcterms
    refinements. Without expansion the LinkML containers expose no slots and
    any XML metadata children get rejected by ``linkml-validate`` as
    "additional properties not allowed".

    Each emitted slot is ``range: string, multivalued: true`` - matching what
    the companion XML converter will produce after collapsing mixed-content
    ``<dc:title>X</dc:title>`` to a bare string.
    """
    # Collect element local-names whose XSD <element name="..."> is reachable
    # from dc:any via the substitutionGroup chain.
    dc = parsed.get("dc", {})
    dct = parsed.get("dct", {})
    # In dc.xsd: dc:any is the abstract head. All other dc elements
    # substitutionGroup="any". In dcterms.xsd: dcterms elements have
    # substitutionGroup pointing at dc:* or at other dcterms elements.
    members: list[str] = []
    for n, info in dc.get("elements", {}).items():
        if n == "any":
            continue
        members.append(n)
    for n, info in dct.get("elements", {}).items():
        members.append(n)
    # De-dupe preserving order.
    seen: set[str] = set()
    ordered = []
    for n in members:
        if n not in seen:
            seen.add(n)
            ordered.append(n)
    for container_class in (
        "DcElementContainer",
        "DctermsElementOrRefinementContainer",
    ):
        cls = classes.get(container_class)
        if cls is None:
            continue
        attrs = cls.setdefault("attributes", OrderedDict())
        for n in ordered:
            slot = snake(n)
            if slot in attrs:
                continue
            body: OrderedDict = OrderedDict()
            body["range"] = "string"
            # Single-valued by design: FIX Orchestra documents carry each
            # Dublin Core element at most once in the metadata block. The
            # converter (scripts/fix_xml_to_linkml.py) takes the first XML
            # occurrence when more are present, mirroring this constraint.
            body["description"] = (
                f"Free-text value of the Dublin Core element/refinement "
                f"`{n}`. Expanded from the XSD substitutionGroup chain "
                f"rooted at dc:any."
            )
            body["slot_uri"] = "dcterms:" + n if n in dct.get("elements", {}) else "dc:" + n
            if slot != n:
                body["aliases"] = [n]
            attrs[slot] = body


def _xsd_prefix_for_scope(scope_key: str) -> str:
    """Map an internal aux-scope key to the canonical CURIE prefix emitted
    into LinkML output (``slot_uri``, ``class_uri``, ``enum_uri``, type
    ``uri``).

    Canonical names follow linkml-lint's ``canonical_prefixes`` rule:
    ``http://purl.org/dc/terms/`` -> ``dcterms`` (not ``dct``),
    ``http://purl.org/dc/dcmitype/`` -> ``dctypes`` (not ``dcmitype``),
    ``http://www.w3.org/XML/1998/namespace`` -> ``XML`` (not ``xml``).
    """
    return {"dc": "dc", "dct": "dcterms", "dcmitype": "dctypes", "xml": "XML"}[scope_key]


def _qualify(qname: str | None, scope_key: str) -> str | None:
    """Qualify an unprefixed QName with the current XSD's default namespace.

    Each aux XSD declares its own default namespace via the schema-level
    ``xmlns="..."``. References like ``substitutionGroup="title"`` or
    ``type="SimpleLiteral"`` are unprefixed in dc.xsd / dcterms.xsd because
    they target their own targetNamespace. To resolve them through the
    aux_registry (which is keyed by xsd-prefix) we have to qualify them first.
    """
    if not qname or ":" in qname:
        return qname
    return f"{_xsd_prefix_for_scope(scope_key)}:{qname}"


def _emit_aux_simple_types(
    scope_key, data, name_pfx, subset, src_xsd, resolve, types, enums
):
    xsd_pfx = _xsd_prefix_for_scope(scope_key)
    for n, info in data["simple_types"].items():
        ln = name_pfx + pascal_simple(n)
        if info["kind"] == "enum":
            perm: OrderedDict = OrderedDict()
            for e in info["enums"]:
                body: OrderedDict = OrderedDict()
                if e["doc"]:
                    body["description"] = e["doc"]
                perm[e["value"]] = body if body else None
            out: OrderedDict = OrderedDict()
            if info["doc"]:
                out["description"] = info["doc"]
            out["enum_uri"] = f"{xsd_pfx}:{n}"
            out["aliases"] = [n] if n != ln else []
            if not out["aliases"]:
                del out["aliases"]
            out["in_subset"] = [subset]
            out["permissible_values"] = perm
            enums[ln] = out
        else:
            base_q = info["base"]
            if info["kind"] == "union":
                base_range = "string"
                desc_extra = "Union of: " + ", ".join(info["union_members"])
            else:
                base_range, _ = resolve(base_q)
                desc_extra = None
            primitives = {
                "string",
                "integer",
                "decimal",
                "float",
                "double",
                "boolean",
                "date",
                "datetime",
                "time",
                "uri",
            }
            if base_range not in primitives:
                base_range = "string"
            out = OrderedDict()
            descs = []
            if info["doc"]:
                descs.append(info["doc"])
            if desc_extra:
                descs.append(desc_extra)
            if descs:
                out["description"] = " | ".join(descs)
            out["typeof"] = base_range
            out["uri"] = f"{xsd_pfx}:{n}"
            if n != ln:
                out["aliases"] = [n]
            out["in_subset"] = [subset]
            if info["pattern"]:
                out["pattern"] = info["pattern"]
            types[ln] = out


def _emit_aux_complex_types(
    scope_key, data, name_pfx, subset, src_xsd, resolve, classes, aux_registry
):
    xsd_pfx = _xsd_prefix_for_scope(scope_key)
    for n, info in data["complex_types"].items():
        ln = name_pfx + pascal(n)
        out: OrderedDict = OrderedDict()
        if info["doc"]:
            out["description"] = info["doc"]
        if info["abstract"]:
            out["abstract"] = True
        # Inheritance: prefer complexContent extension base; else simpleContent
        # extension/restriction base; emit as is_a when it resolves to a class.
        parent_q = _qualify(
            info["base"]
            or info.get("simple_extension_base")
            or info.get("simple_restriction_base"),
            scope_key,
        )
        if parent_q:
            rng, is_cls = resolve(parent_q)
            if is_cls:
                out["is_a"] = rng
            else:
                out.setdefault("annotations", OrderedDict())["xsd_base"] = parent_q
        out["class_uri"] = f"{xsd_pfx}:{n}"
        if n != ln:
            out["aliases"] = [n]
        out["in_subset"] = [subset]
        attrs: OrderedDict = OrderedDict()
        for a in info.get("attributes", []) or []:
            if not a.get("name"):
                continue
            slot = snake(a["name"])
            rng, _ = resolve(_qualify(a["type"], scope_key))
            body = OrderedDict([("range", rng)])
            if a.get("doc"):
                body["description"] = a["doc"]
            if a.get("use") == "required" and (n, a["name"]) not in _OPTIONAL_DESPITE_XSD:
                body["required"] = True
            if a.get("use") == "prohibited":
                body.setdefault("annotations", OrderedDict())["xsd_prohibited"] = True
            attrs[slot] = body
        if info.get("mixed"):
            attrs.setdefault(
                "value",
                OrderedDict(
                    [
                        ("range", "string"),
                        ("description", "Mixed text content of the element."),
                    ]
                ),
            )
        if info.get("has_any"):
            attrs.setdefault(
                "content",
                OrderedDict(
                    [
                        ("range", "string"),
                        ("multivalued", True),
                        ("description", "Pass-through xs:any content as raw strings."),
                    ]
                ),
            )
        if attrs:
            out["attributes"] = attrs
        out.setdefault("annotations", OrderedDict())["xsd_source"] = src_xsd
        if info.get("simple_restriction_base"):
            out["annotations"]["xsd_simple_restriction"] = info[
                "simple_restriction_base"
            ]
        if info.get("simple_extension_base"):
            out["annotations"]["xsd_simple_extension"] = info["simple_extension_base"]
        classes[ln] = out


def _emit_aux_attr_groups(scope_key, data, name_pfx, subset, src_xsd, resolve, classes):
    xsd_pfx = _xsd_prefix_for_scope(scope_key)
    for n, info in data["attribute_groups"].items():
        ln = name_pfx + pascal(n)
        out: OrderedDict = OrderedDict()
        if info["doc"]:
            out["description"] = info["doc"]
        out["mixin"] = True
        out["class_uri"] = f"{xsd_pfx}:{n}"
        if n != ln:
            out["aliases"] = [n]
        out["in_subset"] = [subset]
        attrs: OrderedDict = OrderedDict()
        for a in info["attributes"]:
            if not a.get("name"):
                continue
            slot = snake(a["name"])
            rng, _ = resolve(a["type"])
            body = OrderedDict([("range", rng)])
            if a.get("doc"):
                body["description"] = a["doc"]
            attrs[slot] = body
        if attrs:
            out["attributes"] = attrs
        classes[ln] = out


def _emit_aux_top_attributes(
    scope_key, data, name_pfx, subset, src_xsd, resolve, classes, types, enums
):
    """Top-level <xs:attribute> declarations (xml.xsd has 4 of these).

    LinkML has no global slot concept that maps cleanly to an XSD global
    attribute, so we synthesise a container class ``XmlGlobalAttributes`` (or
    equivalent per scope) whose attributes are the global attribute set, plus
    emit any inline simpleType as a separate enum/type.
    """
    xsd_pfx = _xsd_prefix_for_scope(scope_key)
    if not data["attributes"]:
        return
    container_name = name_pfx + "GlobalAttributes"
    out: OrderedDict = OrderedDict()
    out["description"] = (
        f"Container for the global <xs:attribute> declarations defined in "
        f"{src_xsd}. Each attribute here is referenceable from other XSDs "
        f'via ``ref="{xsd_pfx}:<name>"``.'
    )
    out["class_uri"] = f"{xsd_pfx}:GlobalAttributes"
    out["in_subset"] = [subset]
    out["annotations"] = OrderedDict([("xsd_source", src_xsd)])
    attrs: OrderedDict = OrderedDict()
    for n, info in data["attributes"].items():
        slot = snake(n)
        rng = "string"
        # Resolve type
        if info.get("type"):
            rng, _ = resolve(info["type"])
        elif info.get("inline_simple"):
            inline = info["inline_simple"]
            inline_ln = name_pfx + pascal(n) + "Type"
            if inline["kind"] == "enum":
                perm: OrderedDict = OrderedDict()
                for e in inline["enums"]:
                    body: OrderedDict = OrderedDict()
                    if e["doc"]:
                        body["description"] = e["doc"]
                    perm[e["value"]] = body if body else None
                enums[inline_ln] = OrderedDict(
                    [
                        (
                            "description",
                            f"Anonymous simpleType for {xsd_pfx}:{n} (from {src_xsd}).",
                        ),
                        ("enum_uri", f"{xsd_pfx}:{n}_t"),
                        ("in_subset", [subset]),
                        ("permissible_values", perm),
                    ]
                )
                rng = inline_ln
            else:
                base_r = "string"
                if inline["kind"] == "union":
                    base_r = "string"
                else:
                    base_r, _ = resolve(inline.get("base"))
                    if base_r not in {
                        "string",
                        "integer",
                        "decimal",
                        "float",
                        "double",
                        "boolean",
                        "date",
                        "datetime",
                        "time",
                        "uri",
                    }:
                        base_r = "string"
                types[inline_ln] = OrderedDict(
                    [
                        (
                            "description",
                            f"Anonymous simpleType for {xsd_pfx}:{n} (from {src_xsd}).",
                        ),
                        ("typeof", base_r),
                        ("uri", f"{xsd_pfx}:{n}_t"),
                        ("in_subset", [subset]),
                    ]
                )
                rng = inline_ln
        body = OrderedDict([("range", rng)])
        if info.get("doc"):
            body["description"] = info["doc"]
        body["slot_uri"] = f"{xsd_pfx}:{n}"
        if n != slot:
            body["aliases"] = [n]
        attrs[slot] = body
    out["attributes"] = attrs
    classes[container_name] = out


def _emit_aux_elements(
    scope_key, data, name_pfx, subset, src_xsd, resolve, classes, aux_registry
):
    xsd_pfx = _xsd_prefix_for_scope(scope_key)
    for n, info in data["elements"].items():
        ln = name_pfx + pascal(n)
        out: OrderedDict = OrderedDict()
        if info.get("doc"):
            out["description"] = info["doc"]
        if info.get("abstract"):
            out["abstract"] = True
        # substitutionGroup -> is_a (LinkML element-inheritance)
        sg = _qualify(info.get("substitution_group"), scope_key)
        if sg:
            srng, scls = resolve(sg)
            if scls:
                out["is_a"] = srng
            else:
                out.setdefault("annotations", OrderedDict())[
                    "xsd_substitution_group"
                ] = sg
        # Element with a named type -> is_a that type (when no substitution group)
        type_q = _qualify(info.get("type"), scope_key)
        if type_q:
            trng, tcls = resolve(type_q)
            if tcls and "is_a" not in out:
                out["is_a"] = trng
            elif tcls:
                out.setdefault("annotations", OrderedDict())["xsd_type"] = type_q
        out["class_uri"] = f"{xsd_pfx}:{n}"
        if n != ln:
            out["aliases"] = [n]
        out["in_subset"] = [subset]
        # Inline anonymous complexType
        if info.get("inline"):
            inline = info["inline"]
            attrs: OrderedDict = OrderedDict()
            for el in inline.get("elements", []) or []:
                if not el.get("name"):
                    continue
                slot = snake(el["name"])
                rng_e, is_cls = resolve(el.get("type"))
                if not is_cls and el.get("ref"):
                    rng_e, is_cls = resolve(el.get("ref"))
                body = OrderedDict([("range", rng_e)])
                if el.get("doc"):
                    body["description"] = el["doc"]
                if el.get("max_occurs") == "unbounded":
                    body["multivalued"] = True
                    if is_cls:
                        body["inlined"] = True
                        body["inlined_as_list"] = True
                attrs[slot] = body
            for a in inline.get("attributes", []) or []:
                if not a.get("name"):
                    continue
                slot = snake(a["name"])
                rng_a, _ = resolve(a.get("type"))
                body_a = OrderedDict([("range", rng_a)])
                if a.get("doc"):
                    body_a["description"] = a["doc"]
                attrs[slot] = body_a
            if inline.get("mixed") and "value" not in attrs:
                attrs["value"] = OrderedDict(
                    [
                        ("range", "string"),
                        ("description", "Mixed text content of the element."),
                    ]
                )
            if attrs:
                out["attributes"] = attrs
        out.setdefault("annotations", OrderedDict())["xsd_source"] = src_xsd
        classes[ln] = out


def _emit_aux_groups(scope_key, data, name_pfx, subset, src_xsd, aux_registry, classes):
    """xs:group definitions become placeholder mixin classes whose annotation
    records the member element names; full expansion only happens inside the
    types that <xs:group ref=.../> them, but emitting the group itself ensures
    100% coverage of named declarations.
    """
    xsd_pfx = _xsd_prefix_for_scope(scope_key)
    for n, info in data["groups"].items():
        ln = name_pfx + pascal(n)
        out: OrderedDict = OrderedDict()
        if info["doc"]:
            out["description"] = info["doc"]
        out["mixin"] = True
        out["class_uri"] = f"{xsd_pfx}:{n}"
        if n != ln:
            out["aliases"] = [n]
        out["in_subset"] = [subset]
        out["annotations"] = OrderedDict(
            [
                ("xsd_source", src_xsd),
                (
                    "xsd_group_members",
                    ", ".join(info["members"]) if info["members"] else "",
                ),
            ]
        )
        classes[ln] = out


# ---------------------------------------------------------------------------
# DC metadata slots — hand-crafted augmentation for DctermsElementOrRefinementContainer
#
# The XSD uses xs:any / xs:group references that the parser cannot resolve to
# typed attributes.  We inject explicit string slots for the common DC
# properties so that Repository.metadata can carry title, description, etc.
# ---------------------------------------------------------------------------

_DC_SLOT_DEFS: "OrderedDict[str, OrderedDict]" = OrderedDict(
    [
        (
            "title",
            OrderedDict(
                [
                    ("range", "string"),
                    ("description", "A name given to the resource."),
                    ("slot_uri", "dcterms:title"),
                ]
            ),
        ),
        (
            "description",
            OrderedDict(
                [
                    ("range", "string"),
                    ("description", "An account of the resource."),
                    ("slot_uri", "dcterms:description"),
                ]
            ),
        ),
        (
            "creator",
            OrderedDict(
                [
                    ("range", "string"),
                    ("description", "An entity responsible for making the resource."),
                    ("slot_uri", "dcterms:creator"),
                ]
            ),
        ),
        (
            "rights",
            OrderedDict(
                [
                    ("range", "string"),
                    (
                        "description",
                        "Information about rights held in and over the resource.",
                    ),
                    ("slot_uri", "dcterms:rights"),
                ]
            ),
        ),
        (
            "date",
            OrderedDict(
                [
                    ("range", "string"),
                    (
                        "description",
                        "A point or period of time associated with the resource.",
                    ),
                    ("slot_uri", "dcterms:date"),
                ]
            ),
        ),
        (
            "publisher",
            OrderedDict(
                [
                    ("range", "string"),
                    (
                        "description",
                        "An entity responsible for making the resource available.",
                    ),
                    ("slot_uri", "dcterms:publisher"),
                ]
            ),
        ),
    ]
)

_DC_CONTAINER = "DctermsElementOrRefinementContainer"


def _inject_dc_slots(classes: "OrderedDict[str, OrderedDict]") -> None:
    """Add DC property slots to DctermsElementOrRefinementContainer.

    This is an explicit augmentation: the XSD xs:any group makes it impossible
    to derive these typed slots automatically.
    """
    cls_def = classes.get(_DC_CONTAINER)
    if cls_def is None:
        return
    existing = list(cls_def.get("slots") or [])
    for name in reversed(list(_DC_SLOT_DEFS)):
        if name not in existing:
            existing.insert(0, name)
    cls_def["slots"] = existing


def _inject_fixml_appinfo(
    upstream_dir: Path,
    classes: "OrderedDict[str, OrderedDict]",
) -> bool:
    """Inject the FIXML appinfo content model from ``FIXMLappinfo.xsd``.

    The canonical FIX Orchestra XML corpus carries 500+ instances of
    ``<fixr:appinfo purpose="FIXML"><fixml:FIXMLencodingType notReqXML inlined/>
    </fixr:appinfo>`` payloads. Without this hook the converter drops the
    ``notReqXML`` / ``inlined`` flags. Reading the small ``FIXMLappinfo.xsd``
    bundled by the FIX Trading Community lets us add a ``FIXMLencodingType``
    class to the schema and wire it onto ``Appinfo`` via ``fixml_encoding``.

    Returns ``True`` when the class was emitted, ``False`` if the XSD is
    missing (the function is opt-in: callers degrade gracefully).
    """
    appinfo_xsd = upstream_dir / "FIXMLappinfo.xsd"
    if not appinfo_xsd.is_file():
        return False
    root = ET.parse(appinfo_xsd).getroot()
    cls_name = "FIXMLencodingType"
    ct = next(
        (
            c
            for c in root
            if local(c.tag) == "complexType" and c.get("name") == cls_name
        ),
        None,
    )
    if ct is None:
        return False
    attrs: "OrderedDict[str, OrderedDict]" = OrderedDict()
    for a in ct.findall(f"{XS}attribute"):
        name = a.get("name")
        if not name:
            continue
        body: "OrderedDict" = OrderedDict()
        body["range"] = "boolean"
        doc = doc_of(a)
        if doc:
            body["description"] = doc
        default = a.get("default")
        if default is not None:
            truth = default.strip().lower() in ("1", "true")
            body["ifabsent"] = f"boolean({'true' if truth else 'false'})"
        slot = snake(name)
        body["slot_uri"] = f"fix_orchestra:{slot}"
        body["exact_mappings"] = [f"fixml:{name}"]
        if slot != name:
            body["aliases"] = [name]
        attrs[slot] = body
    cls_out: "OrderedDict" = OrderedDict()
    cls_out["description"] = (
        doc_of(ct)
        or 'FIXML generator hints carried inside <fixr:appinfo purpose="FIXML">. '
        "Captures whether a component is inlined in its containing message and "
        "whether an element is ignored by the FIXML generator."
    )
    cls_out["class_uri"] = f"fix_orchestra:{cls_name}"
    cls_out["exact_mappings"] = [f"fixml:{cls_name}"]
    cls_out["aliases"] = ["FIXMLencoding"]
    cls_out["in_subset"] = ["repository_types"]
    cls_out["attributes"] = attrs
    cls_out["annotations"] = OrderedDict([("xsd_source", "FIXMLappinfo.xsd")])
    classes[cls_name] = cls_out
    appinfo_cls = classes.get("Appinfo")
    if appinfo_cls is not None:
        appinfo_attrs = appinfo_cls.setdefault("attributes", OrderedDict())
        if "fixml_encoding" not in appinfo_attrs:
            appinfo_attrs["fixml_encoding"] = OrderedDict(
                [
                    ("range", cls_name),
                    (
                        "description",
                        "FIXML generator hints. Surfaces "
                        "<fixml:FIXMLencoding> / <fixml:FIXMLencodingType> "
                        'payloads embedded in <fixr:appinfo purpose="FIXML">.',
                    ),
                    ("inlined", True),
                    ("slot_uri", "fix_orchestra:fixml_encoding"),
                    ("aliases", ["FIXMLencoding", "FIXMLencodingType"]),
                ]
            )
    return True


def _slot_diff(canonical: dict, other: dict) -> "OrderedDict":
    """Return keys where *other* differs from *canonical* (skip range/multivalued)."""
    skip = {"range", "multivalued"}
    result: "OrderedDict" = OrderedDict()
    for k, v in other.items():
        if k in skip:
            continue
        if canonical.get(k) != v:
            result[k] = v
    # Keys present in canonical but absent in other require an explicit null
    # override in slot_usage so the class can "un-set" the inherited value.
    for k, v in canonical.items():
        if k in skip:
            continue
        if k not in other and v is not None:
            result[k] = None
    return result


def _promote_to_schema_slots(
    classes: "OrderedDict[str, OrderedDict]",
) -> "OrderedDict[str, OrderedDict]":
    """Promote shared class attributes to schema-level slots.

    Attributes whose (range, multivalued) is identical across ALL classes that
    define that attribute are lifted to the schema-level ``slots:`` section.
    Divergent attributes (different range or multivalued across classes) are
    kept as per-class ``attributes:``.

    For ``required``: if ANY class that uses an attribute does NOT mark it
    required, the canonical slot definition omits ``required`` entirely.
    Classes that DO need ``required: true`` get it via ``slot_usage``.  This
    prevents incorrectly forcing the constraint on classes that didn't ask for
    it, since LinkML's ``slot_usage: required: null`` does not reliably
    downgrade an inherited ``required: true``.

    Returns the ordered slots dict (first-use traversal order across classes).
    """
    import copy
    from collections import defaultdict

    def _canonical_key(d: dict) -> tuple:
        return (str(d.get("range", "")), str(d.get("multivalued", "")))

    # Collect usage: attr_name -> [(cls_name, attr_def_copy)]
    attr_usage: dict[str, list] = defaultdict(list)
    for cls_name, cls_def in classes.items():
        if not cls_def:
            continue
        for attr_name, attr_def in (cls_def.get("attributes") or {}).items():
            attr_usage[attr_name].append((cls_name, dict(attr_def) if attr_def else {}))

    # Decide promotable vs keep-local
    promotable: dict[str, dict] = {}
    keep_local: set[str] = set()
    for attr_name, uses in attr_usage.items():
        keys = {_canonical_key(d) for _, d in uses}
        if len(keys) == 1:
            canonical = copy.deepcopy(uses[0][1])
            # Use "minimal required": drop required from canonical when not
            # ALL classes want it, so that non-requiring classes need no
            # slot_usage override.
            if canonical.get("required"):
                if not all(d.get("required") for _, d in uses):
                    del canonical["required"]
            # Use best description: prefer first non-empty description across
            # all uses so that a later XSD annotation is not silently dropped
            # when the first-encountered definition has no doc.
            if not canonical.get("description"):
                for _, other in uses[1:]:
                    if other.get("description"):
                        canonical["description"] = other["description"]
                        break
            promotable[attr_name] = canonical
        else:
            keep_local.add(attr_name)

    # Build ordered slots section (first-use order across class traversal)
    seen: set[str] = set()
    ordered_slots: "OrderedDict[str, OrderedDict]" = OrderedDict()
    for cls_def in classes.values():
        if not cls_def:
            continue
        for attr_name in list((cls_def.get("attributes") or {}).keys()):
            if attr_name in promotable and attr_name not in seen:
                ordered_slots[attr_name] = promotable[attr_name]
                seen.add(attr_name)

    # Update each class: replace promotable attributes with slots: list
    for cls_name, cls_def in classes.items():
        if not cls_def or not cls_def.get("attributes"):
            continue
        attrs: dict = cls_def["attributes"]
        promote_here = [n for n in attrs if n in promotable]
        keep_here = [n for n in attrs if n in keep_local]

        slot_usage_additions: "OrderedDict[str, OrderedDict]" = OrderedDict()
        for attr_name in promote_here:
            diff = _slot_diff(promotable[attr_name], attrs[attr_name] or {})
            if diff:
                slot_usage_additions[attr_name] = diff

        if promote_here:
            cls_def["slots"] = promote_here
        if keep_here:
            cls_def["attributes"] = OrderedDict((n, attrs[n]) for n in keep_here)
        else:
            del cls_def["attributes"]
        if slot_usage_additions:
            existing_su = cls_def.get("slot_usage") or {}
            cls_def["slot_usage"] = OrderedDict(
                [*slot_usage_additions.items(), *existing_su.items()]
            )

    return ordered_slots


# ---------------------------------------------------------------------------
# FIX Orchestra XML enrichment helpers
# ---------------------------------------------------------------------------

# Maps xs:* base type names (from <fixr:mappedDatatype standard="XML" base="xs:...">) to
# their closest LinkML primitive type name.
_XSD_BASE_TO_LINKML: dict[str, str] = {
    "xs:integer":            "integer",
    "xs:nonNegativeInteger": "integer",
    "xs:positiveInteger":    "integer",
    "xs:long":               "integer",
    "xs:int":                "integer",
    "xs:short":              "integer",
    "xs:decimal":            "float",
    "xs:float":              "float",
    "xs:double":             "float",
    "xs:boolean":            "boolean",
    "xs:string":             "string",
    "xs:normalizedString":   "string",
    "xs:token":              "string",
    "xs:language":           "string",
    "xs:Name":               "string",
    "xs:NCName":             "string",
    "xs:anyURI":             "uri",
    "xs:base64Binary":       "string",
    "xs:date":               "date",
    "xs:dateTime":           "datetime",
    "xs:time":               "string",
}

# Maps FIX datatype name -> protobuf scalar type.
# Canonical copy lives in scripts/fix_xml_to_proto.py; kept in sync manually.
_FIX_DATATYPE_TO_PROTO: dict[str, str] = {
    "int":                "fixed32",
    "Length":             "fixed32",
    "TagNum":             "fixed32",
    "SeqNum":             "fixed32",
    "DayOfMonth":         "fixed32",
    "NumInGroup":         "fixed32",
    "float":              "double",
    "Qty":                "Decimal64",
    "Price":              "Decimal64",
    "PriceOffset":        "Decimal64",
    "Amt":                "Decimal64",
    "Percentage":         "double",
    "char":               "string",
    "Boolean":            "bool",
    "String":             "string",
    "MultipleCharValue":  "string",
    "MultipleStringValue":"string",
    "Country":            "string",
    "Currency":           "string",
    "Exchange":           "string",
    "MonthYear":          "string",
    "UTCTimestamp":       "Timestamp",
    "UTCTimeOnly":        "TimeOnly",
    "UTCDateOnly":        "string",
    "LocalMktDate":       "string",
    "TZTimeOnly":         "TimeOnly",
    "TZTimestamp":        "Timestamp",
    "data":               "bytes",
    "Pattern":            "string",
    "Tenor":              "Tenor",
    "Reserved100Plus":    "fixed32",
    "Reserved1000Plus":   "fixed32",
    "Reserved4000Plus":   "fixed32",
    "XMLData":            "string",
    "Language":           "string",
    "LocalMktTime":       "TimeOnly",
    "XID":                "string",
    "XIDREF":             "string",
}

_FIXR_NS = "http://fixprotocol.io/2020/orchestra/repository"
_FIXR = "{" + _FIXR_NS + "}"


def _enrich_fix_datatypes(
    orchestra_xml: Path,
    types: "OrderedDict[str, OrderedDict]",
    subsets: "OrderedDict[str, OrderedDict]",
) -> int:
    """Parse ``<fixr:datatypes>`` from *orchestra_xml* and append LinkML type
    entries with ``proto_scalar`` annotations to *types*.

    Also registers a ``fix_base_types`` subset.  Returns the count of entries
    added.
    """
    tree = ET.parse(orchestra_xml)
    root = tree.getroot()

    subsets["fix_base_types"] = OrderedDict(
        [
            (
                "description",
                "FIX base datatypes derived from the FIX Orchestra XML repository. "
                "Each type carries a proto_scalar annotation giving the recommended "
                "Protocol Buffers scalar type when encoding FIX wire-format messages.",
            )
        ]
    )

    datatypes_el = root.find(f"{_FIXR}datatypes")
    if datatypes_el is None:
        return 0

    count = 0
    for dt in datatypes_el.findall(f"{_FIXR}datatype"):
        name = dt.attrib.get("name")
        if not name:
            continue

        # Determine the closest LinkML primitive from the XSD mapping.
        xsd_base: str | None = None
        for mapped in dt.findall(f"{_FIXR}mappedDatatype"):
            if mapped.attrib.get("standard") == "XML":
                xsd_base = mapped.attrib.get("base")
                break
        linkml_typeof = _XSD_BASE_TO_LINKML.get(xsd_base or "", "string")

        # Collect description from annotation/documentation.
        desc_parts: list[str] = []
        base_type = dt.attrib.get("baseType")
        if base_type:
            desc_parts.append(f"FIX {name} datatype (extends {base_type}).")
        else:
            desc_parts.append(f"FIX {name} base datatype.")
        ann = dt.find(f"{_FIXR}annotation")
        if ann is not None:
            for doc_el in ann.findall(f"{_FIXR}documentation"):
                text = " ".join((doc_el.text or "").split())
                if text:
                    desc_parts.append(text)
                    break

        # LinkML type name: "FIX" + capitalised original name avoids clashing
        # with built-in LinkML primitives (e.g. FIX "int" -> "FIXInt").
        linkml_name = "FIX" + name[0].upper() + name[1:]

        out: OrderedDict = OrderedDict()
        out["description"] = " ".join(desc_parts)
        out["typeof"] = linkml_typeof
        out["uri"] = f"fix_orchestra:{linkml_name}"
        out["exact_mappings"] = [f"fixr:{name}"]
        out["in_subset"] = ["fix_base_types"]
        proto_scalar = _FIX_DATATYPE_TO_PROTO.get(name)
        if proto_scalar:
            out["annotations"] = OrderedDict([("proto_scalar", proto_scalar)])

        types[linkml_name] = out
        count += 1

    return count


# ---------------------------------------------------------------------------
# Conversion
# ---------------------------------------------------------------------------


def convert(
    upstream_dir: Path,
    out_file: Path,
    orchestra_xml: "Path | None" = None,
    dc_out_file: "Path | None" = None,
) -> None:
    repo_types = parse_xsd(upstream_dir / "repositorytypes.xsd")
    repo_root = parse_xsd(upstream_dir / "repository.xsd")
    iface = parse_xsd(upstream_dir / "interfaces.xsd")

    # Global name registry: src-name -> {kind, name}
    registry: dict[str, dict] = {}

    def register(src_name: str, kind: str, linkml_name: str) -> None:
        registry[src_name] = {"kind": kind, "name": linkml_name}

    for n, info in repo_types["simple_types"].items():
        register(n, "enum" if info["kind"] == "enum" else "type", pascal_simple(n))
    for n in repo_types["complex_types"]:
        register(n, "class", pascal(n))
    for n in repo_types["attribute_groups"]:
        register(n, "mixin", pascal(n))
    for n in repo_types["elements"]:
        register(n, "class", pascal(n))
    for n in repo_root["elements"]:
        register(n, "class", pascal(n))

    iface_local_to_linkml: dict[str, str] = {}
    for n, info in iface["simple_types"].items():
        ln = pascal_simple(iface_name(n))
        iface_local_to_linkml[n] = ln
        register("iface:" + n, "enum" if info["kind"] == "enum" else "type", ln)
    for n in iface["complex_types"]:
        ln = pascal(iface_name(n))
        iface_local_to_linkml[n] = ln
        register("iface:" + n, "class", ln)
    for n in iface["elements"]:
        ln = pascal(iface_name(n))
        iface_local_to_linkml[n] = ln
        register("iface:" + n, "class", ln)

    # XSD-prefix -> aux-scope key used in aux_registry below.
    AUX_PREFIX_TO_SCOPE = {
        "dc": "dc",
        "dct": "dct",
        "dcterms": "dct",
        "dcmitype": "dcmitype",
        "xml": "xml",
    }
    aux_registry: dict[tuple[str, str], dict] = {}

    def resolve_range(
        qname: str | None, in_interfaces: bool = False
    ) -> tuple[str, bool]:
        if not qname:
            return ("string", False)
        if ":" in qname:
            prefix, name = qname.split(":", 1)
        else:
            prefix, name = "", qname
        if prefix == "xs":
            return (PRIM.get(name, "string"), False)
        if prefix in AUX_PREFIX_TO_SCOPE:
            scope = AUX_PREFIX_TO_SCOPE[prefix]
            entry = aux_registry.get((scope, name))
            if entry:
                return (entry["name"], entry["kind"] in ("class", "enum", "mixin"))
            return ("string", False)
        if in_interfaces and name in iface_local_to_linkml:
            kind = registry["iface:" + name]["kind"]
            return (iface_local_to_linkml[name], kind in ("class", "enum", "mixin"))
        if name in registry:
            kind = registry[name]["kind"]
            return (registry[name]["name"], kind in ("class", "enum", "mixin"))
        if ("iface:" + name) in registry:
            entry = registry["iface:" + name]
            return (entry["name"], entry["kind"] in ("class", "enum", "mixin"))
        return ("string", False)

    classes: "OrderedDict[str, OrderedDict]" = OrderedDict()
    enums: "OrderedDict[str, OrderedDict]" = OrderedDict()
    types: "OrderedDict[str, OrderedDict]" = OrderedDict()
    subsets: "OrderedDict[str, OrderedDict]" = OrderedDict(
        [
            (
                "repository_types",
                OrderedDict(
                    [
                        (
                            "description",
                            "Types and elements defined in repositorytypes.xsd. Forms the "
                            "shared vocabulary used by repository.xsd.",
                        )
                    ]
                ),
            ),
            (
                "repository",
                OrderedDict(
                    [
                        (
                            "description",
                            "Top-level container elements defined in repository.xsd.",
                        )
                    ]
                ),
            ),
            (
                "interfaces",
                OrderedDict(
                    [
                        (
                            "description",
                            "Types and elements defined in interfaces.xsd, describing FIX "
                            "service / session / encoding / protocol / transport bindings.",
                        )
                    ]
                ),
            ),
            (
                "dc",
                OrderedDict(
                    [
                        (
                            "description",
                            "Dublin Core elements 1.1 (dc.xsd, namespace "
                            "http://purl.org/dc/elements/1.1/).",
                        )
                    ]
                ),
            ),
            (
                "dcterms",
                OrderedDict(
                    [
                        (
                            "description",
                            "Dublin Core Terms (dcterms.xsd, namespace "
                            "http://purl.org/dc/terms/). Includes element refinements and "
                            "value encoding schemes (LCSH, MESH, W3CDTF, ISO639, ...).",
                        )
                    ]
                ),
            ),
            (
                "dcmitype",
                OrderedDict(
                    [
                        (
                            "description",
                            "DCMI Type Vocabulary (dcmitype.xsd, namespace "
                            "http://purl.org/dc/dcmitype/). Controlled list of resource "
                            "type values (Collection, Dataset, Image, ...).",
                        )
                    ]
                ),
            ),
            (
                "xml_namespace",
                OrderedDict(
                    [
                        (
                            "description",
                            "W3C XML namespace declarations (xml.xsd, namespace "
                            "http://www.w3.org/XML/1998/namespace). Defines the well-known "
                            "xml:base, xml:lang, xml:space, xml:id attributes.",
                        )
                    ]
                ),
            ),
        ]
    )

    SUBSET_FOR_XSD = {
        "repositorytypes.xsd": "repository_types",
        "repository.xsd": "repository",
        "interfaces.xsd": "interfaces",
    }

    def src_prefix(src_xsd: str | None, in_interfaces: bool) -> str:
        if in_interfaces:
            return "fixi"
        return "fixr"

    def class_uri_for(src_name: str, in_interfaces: bool) -> str:
        # Use the project's own w3id namespace so the URI rendered by gen-doc
        # resolves through https://w3id.org/lmodel/fix-orchestra/ (which
        # redirects to the published doc site) instead of the upstream FIX
        # targetNamespace (fixprotocol.io -> 404). The upstream identity is
        # preserved via ``exact_mappings`` on each entity.
        ln = pascal(iface_name(src_name)) if in_interfaces else pascal(src_name)
        return f"fix_orchestra:{ln}"

    def slot_uri_for(src_name: str, in_interfaces: bool) -> str:
        return f"fix_orchestra:{snake(src_name)}"

    def fix_upstream_curie(src_name: str, in_interfaces: bool) -> str:
        """Upstream FIX CURIE (``fixr:`` / ``fixi:``) preserved as exact_mapping."""
        return f"{src_prefix(None, in_interfaces)}:{src_name}"

    def unique_slot_name(existing: dict, name: str) -> str:
        if name not in existing:
            return name
        i = 2
        while f"{name}_{i}" in existing:
            i += 1
        return f"{name}_{i}"

    def collect_attrs(
        info: dict,
        in_interfaces: bool = False,
        mixed: bool = False,
        has_any: bool = False,
        has_any_attr: bool = False,
        xsd_type_name: str = "",
    ) -> OrderedDict:
        attrs: OrderedDict = OrderedDict()
        for el in info.get("elements", []) or []:
            xsd_name = el["name"]
            slot_name = snake(xsd_name)
            body: OrderedDict = OrderedDict()
            rng = "string"
            is_class_like = False
            if el.get("ref"):
                refname = xsd_name
                if refname in registry:
                    rng = registry[refname]["name"]
                    is_class_like = True
                elif ("iface:" + refname) in registry:
                    rng = registry["iface:" + refname]["name"]
                    is_class_like = True
            elif el.get("inline"):
                synth_name = pascal(xsd_name) + "Inline"
                emit_synthetic_class(
                    synth_name,
                    el["inline"],
                    in_interfaces=in_interfaces,
                    parent_xsd_prefix=src_prefix(None, in_interfaces),
                )
                rng = synth_name
                is_class_like = True
            else:
                rng, is_class_like = resolve_range(
                    el["type"], in_interfaces=in_interfaces
                )
            body["range"] = rng
            if el.get("doc"):
                body["description"] = el["doc"]
            unbounded = el["max_occurs"] == "unbounded" or (
                isinstance(el["max_occurs"], str)
                and el["max_occurs"].isdigit()
                and int(el["max_occurs"]) > 1
            )
            if unbounded:
                body["multivalued"] = True
                if is_class_like:
                    body["inlined"] = True
                    body["inlined_as_list"] = True
            if el["min_occurs"] >= 1:
                body["required"] = True
            body["slot_uri"] = slot_uri_for(xsd_name, in_interfaces)
            body["exact_mappings"] = [fix_upstream_curie(xsd_name, in_interfaces)]
            if slot_name != xsd_name:
                body["aliases"] = [xsd_name]
            attrs[unique_slot_name(attrs, slot_name)] = body
        for a in info.get("attributes", []) or []:
            xsd_name = a.get("name")
            if not xsd_name:
                continue
            slot_name = snake(xsd_name)
            rng, _ = resolve_range(a["type"], in_interfaces=in_interfaces)
            body = OrderedDict()
            body["range"] = rng
            if a.get("doc"):
                body["description"] = a["doc"]
            if a.get("use") == "required" and (xsd_type_name, xsd_name) not in _OPTIONAL_DESPITE_XSD:
                body["required"] = True
            if a.get("fixed") is not None:
                # XSD fixed value: enforce + provide as default.
                body["equals_string"] = a["fixed"]
                body["ifabsent"] = f"string({a['fixed']})"
            elif a.get("default") is not None:
                body["ifabsent"] = f"string({a['default']})"
            body["slot_uri"] = slot_uri_for(xsd_name, in_interfaces)
            body["exact_mappings"] = [fix_upstream_curie(xsd_name, in_interfaces)]
            if slot_name != xsd_name:
                body["aliases"] = [xsd_name]
            attrs[unique_slot_name(attrs, slot_name)] = body
        if mixed:
            attrs[unique_slot_name(attrs, "value")] = OrderedDict(
                [
                    ("range", "string"),
                    ("description", "Mixed text content of the element."),
                ]
            )
        if has_any:
            attrs[unique_slot_name(attrs, "content")] = OrderedDict(
                [
                    ("range", "string"),
                    ("multivalued", True),
                    ("description", "Pass-through xs:any content as raw strings."),
                ]
            )
        if has_any_attr:
            attrs[unique_slot_name(attrs, "extra_attributes")] = OrderedDict(
                [
                    ("range", "string"),
                    ("multivalued", True),
                    (
                        "description",
                        "Pass-through xs:anyAttribute values keyed by their XML "
                        "attribute name (open extension point).",
                    ),
                ]
            )
        return attrs

    def emit_attr_group(src_name: str, info: dict) -> None:
        ln = pascal(src_name)
        out: OrderedDict = OrderedDict()
        if info["doc"]:
            out["description"] = info["doc"]
        out["mixin"] = True
        out["class_uri"] = class_uri_for(src_name, in_interfaces=False)
        out["exact_mappings"] = [fix_upstream_curie(src_name, in_interfaces=False)]
        if src_name != ln:
            out["aliases"] = [src_name]
        out["in_subset"] = ["repository_types"]
        attrs = collect_attrs(info, xsd_type_name=src_name)
        if attrs:
            out["attributes"] = attrs
        classes[ln] = out

    def emit_enum(src_name: str, info: dict, in_interfaces: bool = False) -> None:
        ln = (
            pascal_simple(iface_name(src_name))
            if in_interfaces
            else pascal_simple(src_name)
        )
        perm: OrderedDict = OrderedDict()
        for e in info["enums"]:
            body: OrderedDict = OrderedDict()
            if e["doc"]:
                body["description"] = e["doc"]
            perm[e["value"]] = body if body else None
        out: OrderedDict = OrderedDict()
        if info["doc"]:
            out["description"] = info["doc"]
        out["enum_uri"] = f"fix_orchestra:{ln}"
        out["exact_mappings"] = [fix_upstream_curie(src_name, in_interfaces)]
        if src_name != ln:
            out["aliases"] = [src_name]
        out["in_subset"] = ["interfaces" if in_interfaces else "repository_types"]
        out["permissible_values"] = perm
        enums[ln] = out

    def emit_type(src_name: str, info: dict, in_interfaces: bool = False) -> None:
        ln = (
            pascal_simple(iface_name(src_name))
            if in_interfaces
            else pascal_simple(src_name)
        )
        primitives = {
            "string",
            "integer",
            "decimal",
            "float",
            "double",
            "boolean",
            "date",
            "datetime",
            "time",
            "uri",
        }
        if info["kind"] == "union":
            base_range = "string"
            union_note = "Union of: " + ", ".join(info["union_members"])
        else:
            base_range, _ = resolve_range(info["base"], in_interfaces=in_interfaces)
            union_note = None
        if base_range not in primitives:
            base_range = "string"
        out: OrderedDict = OrderedDict()
        descs = []
        if info["doc"]:
            descs.append(info["doc"])
        if union_note:
            descs.append(union_note)
        if descs:
            out["description"] = " | ".join(descs)
        out["typeof"] = base_range
        out["uri"] = f"fix_orchestra:{ln}"
        out["exact_mappings"] = [fix_upstream_curie(src_name, in_interfaces)]
        if src_name != ln:
            out["aliases"] = [src_name]
        out["in_subset"] = ["interfaces" if in_interfaces else "repository_types"]
        if info["pattern"]:
            out["pattern"] = info["pattern"]
        anno: OrderedDict = OrderedDict()
        if info["min_length"]:
            anno["xsd_min_length"] = int(info["min_length"])
        if info["max_length"]:
            anno["xsd_max_length"] = int(info["max_length"])
        if anno:
            out["annotations"] = anno
        if info["min_inclusive"]:
            try:
                out["minimum_value"] = int(info["min_inclusive"])
            except ValueError:
                pass
        if info["max_inclusive"]:
            try:
                out["maximum_value"] = int(info["max_inclusive"])
            except ValueError:
                pass
        types[ln] = out

    def emit_synthetic_class(
        name: str,
        complex_info: dict,
        in_interfaces: bool = False,
        parent_xsd_prefix: str = "fixr",
    ) -> None:
        if name in classes:
            return
        out: OrderedDict = OrderedDict()
        if complex_info["doc"]:
            out["description"] = complex_info["doc"]
        mixins = []
        for ag in complex_info.get("attribute_groups", []) or []:
            if ag in registry:
                mixins.append(registry[ag]["name"])
            elif ("iface:" + ag) in registry:
                mixins.append(registry["iface:" + ag]["name"])
        if mixins:
            out["mixins"] = mixins
        out["in_subset"] = ["interfaces" if in_interfaces else "repository_types"]
        out.setdefault("annotations", OrderedDict())["xsd_anonymous_inline"] = True
        attrs = collect_attrs(
            complex_info,
            in_interfaces=in_interfaces,
            mixed=complex_info.get("mixed", False),
            has_any=complex_info.get("has_any", False),
            has_any_attr=complex_info.get("has_any_attr", False),
            xsd_type_name=name,
        )
        if attrs:
            out["attributes"] = attrs
        classes[name] = out

    def emit_complex(
        src_name: str,
        info: dict,
        in_interfaces: bool = False,
        tree_root: bool = False,
        src_xsd: str | None = None,
        keys: list | None = None,
        keyrefs: list | None = None,
    ) -> None:
        ln = pascal(iface_name(src_name)) if in_interfaces else pascal(src_name)
        out: OrderedDict = OrderedDict()
        if info["doc"]:
            out["description"] = info["doc"]
        if info["abstract"]:
            out["abstract"] = True
        if info["base"]:
            bname = nons(info["base"])
            base_range, _ = resolve_range(info["base"], in_interfaces=in_interfaces)
            base_kind = None
            if in_interfaces and ("iface:" + bname) in registry:
                base_kind = registry["iface:" + bname]["kind"]
            elif bname in registry:
                base_kind = registry[bname]["kind"]
            elif ("iface:" + bname) in registry:
                base_kind = registry["iface:" + bname]["kind"]
            if base_kind == "class":
                out["is_a"] = base_range
            elif base_kind == "type":
                out.setdefault("annotations", OrderedDict())["xsd_simple_base"] = (
                    base_range
                )
        if tree_root:
            out["tree_root"] = True
        mixins = []
        for ag in info.get("attribute_groups", []) or []:
            if ag in registry:
                mixins.append(registry[ag]["name"])
            elif ("iface:" + ag) in registry:
                mixins.append(registry["iface:" + ag]["name"])
        if mixins:
            out["mixins"] = mixins
        out["class_uri"] = class_uri_for(src_name, in_interfaces=in_interfaces)
        out["exact_mappings"] = [fix_upstream_curie(src_name, in_interfaces)]
        if src_name != ln:
            out["aliases"] = [src_name]
        out["in_subset"] = [
            SUBSET_FOR_XSD.get(
                src_xsd or "", "interfaces" if in_interfaces else "repository_types"
            )
        ]
        attrs = collect_attrs(
            info,
            in_interfaces=in_interfaces,
            mixed=info.get("mixed", False),
            has_any=info.get("has_any", False),
            has_any_attr=info.get("has_any_attr", False),
            xsd_type_name=src_name,
        )
        if attrs:
            out["attributes"] = attrs
        # unique_keys derived from xs:key declarations on the wrapping element.
        ukeys = build_unique_keys(keys or [])
        if ukeys:
            out["unique_keys"] = ukeys
        # Annotations: source XSD, xs:anyAttribute marker, xs:keyref refs.
        if src_xsd:
            out.setdefault("annotations", OrderedDict())["xsd_source"] = src_xsd
        if info.get("has_any_attr"):
            out.setdefault("annotations", OrderedDict())["xsd_any_attribute"] = True
        if keyrefs:
            # Flatten to a single string - LinkML lint rejects nested
            # list-of-dicts at the annotation level.
            out.setdefault("annotations", OrderedDict())["xsd_keyrefs"] = "; ".join(
                f"{k['name']}(refer={k['refer']}, selector={k['selector']}, "
                f"fields=[{','.join(k['fields'] or [])}])"
                for k in keyrefs
            )
        classes[ln] = out

    def build_unique_keys(keys: list) -> OrderedDict:
        out: OrderedDict = OrderedDict()
        for k in keys:
            if not k.get("fields"):
                continue
            # XSD field xpaths look like '@name' or 'fixr:something'. We only
            # convert simple '@attr' fields to LinkML unique_key_slots.
            slot_fields = []
            for xp in k["fields"]:
                if xp and xp.startswith("@"):
                    slot_fields.append(snake(xp[1:]))
            if not slot_fields:
                continue
            key_name = snake(k["name"] or "unique_key")
            body = OrderedDict()
            if k.get("selector"):
                body["description"] = (
                    f'From XSD <xs:key name="{k["name"]}"> with '
                    f'selector "{k["selector"]}".'
                )
            body["unique_key_slots"] = slot_fields
            out[key_name] = body
        return out

    def emit_top_element_wrapper(
        src_name: str,
        info: dict,
        in_interfaces: bool = False,
        tree_root: bool = False,
        src_xsd: str | None = None,
    ) -> None:
        ln = pascal(iface_name(src_name)) if in_interfaces else pascal(src_name)
        if info.get("inline"):
            emit_complex(
                src_name,
                info["inline"],
                in_interfaces=in_interfaces,
                tree_root=tree_root,
                src_xsd=src_xsd,
                keys=info.get("keys"),
                keyrefs=info.get("keyrefs"),
            )
            if info.get("doc"):
                classes[ln].setdefault("description", info["doc"])
        elif info.get("type"):
            rng, _ = resolve_range(info["type"], in_interfaces=in_interfaces)
            out: OrderedDict = OrderedDict()
            if info.get("doc"):
                out["description"] = info["doc"]
            out["is_a"] = rng
            if tree_root:
                out["tree_root"] = True
            out["class_uri"] = class_uri_for(src_name, in_interfaces=in_interfaces)
            out["exact_mappings"] = [fix_upstream_curie(src_name, in_interfaces)]
            if src_name != ln:
                out["aliases"] = [src_name]
            out["in_subset"] = [
                SUBSET_FOR_XSD.get(
                    src_xsd or "", "interfaces" if in_interfaces else "repository_types"
                )
            ]
            if src_xsd:
                out.setdefault("annotations", OrderedDict())["xsd_source"] = src_xsd
            classes[ln] = out

    # ---- Aux XSDs (dc, dcmitype, dcterms, xml.xsd) -------------------------
    # Each contributes a subset of LinkML entities under a scope-specific
    # name prefix so cross-XSD types stay disambiguated.
    emit_aux_xsds(upstream_dir, classes, enums, types, aux_registry)

    # ---- Emission order: mixins -> types/enums -> complex types -> wrappers --
    for n, info in repo_types["attribute_groups"].items():
        emit_attr_group(n, info)

    for n, info in repo_types["simple_types"].items():
        (emit_enum if info["kind"] == "enum" else emit_type)(n, info)
    for n, info in iface["simple_types"].items():
        (emit_enum if info["kind"] == "enum" else emit_type)(
            n, info, in_interfaces=True
        )

    for n, info in repo_types["complex_types"].items():
        emit_complex(n, info, src_xsd="repositorytypes.xsd")
    for n, info in iface["complex_types"].items():
        emit_complex(n, info, in_interfaces=True, src_xsd="interfaces.xsd")

    for n, info in repo_types["elements"].items():
        emit_top_element_wrapper(n, info, src_xsd="repositorytypes.xsd")
    for n, info in repo_root["elements"].items():
        emit_top_element_wrapper(
            n, info, tree_root=(n == "repository"), src_xsd="repository.xsd"
        )
    for n, info in iface["elements"].items():
        emit_top_element_wrapper(
            n,
            info,
            in_interfaces=True,
            tree_root=(n == "interfaces"),
            src_xsd="interfaces.xsd",
        )

    # ---- Inject FIXML appinfo content model (FIXMLappinfo.xsd) ---------------
    _inject_fixml_appinfo(upstream_dir, classes)

    # ---- Inject DC property slots and promote shared attributes to schema slots --
    _inject_dc_slots(classes)
    promoted_slots = _promote_to_schema_slots(classes)

    # Build the slots section: place DC slot definitions immediately after any
    # promoted slots that precede them in class traversal order (value, content),
    # then the rest of the promoted slots.  We insert the DC entries after the
    # first two promoted slots (value, content) to match the conventional order.
    slots_section: "OrderedDict[str, OrderedDict]" = OrderedDict()
    # Emit value + content first (they'll be in promoted_slots if present),
    # then the explicit DC slot defs, then everything else.
    pre_dc = [k for k in ("value", "content") if k in promoted_slots]
    post_dc = [k for k in promoted_slots if k not in pre_dc]
    for k in pre_dc:
        slots_section[k] = promoted_slots[k]
    for name, defn in _DC_SLOT_DEFS.items():
        if name not in slots_section:
            slots_section[name] = defn
    for k in post_dc:
        slots_section[k] = promoted_slots[k]

    # ---- Optional FIX Orchestra XML enrichment --------------------------------
    if orchestra_xml is not None:
        n_enriched = _enrich_fix_datatypes(orchestra_xml, types, subsets)
        print(
            f"  FIX Orchestra XML   : added {n_enriched} FIX base datatype types",
            file=sys.stderr,
        )

    # ---- DC schema split ----------------------------------------------------
    # Entities whose in_subset belongs to one of the four DC-originated XSDs
    # are emitted to a companion fix_orchestra_dc.yaml schema.  The main
    # fix_orchestra.yaml schema imports it so non-DC classes that happen to
    # share slots (value, content, source) can still resolve them.
    _DC_SUBSETS = frozenset({"dc", "dcterms", "dcmitype", "xml_namespace"})

    def _is_dc(entity: dict) -> bool:
        return bool(set(entity.get("in_subset") or []) & _DC_SUBSETS)

    # Collect slots that DC classes reference in their `slots:` list.
    # Those slots MUST live in the DC schema so DC classes can resolve them
    # without a back-reference to the FIX schema.
    _dc_class_names: set[str] = {k for k, v in classes.items() if _is_dc(v)}
    _dc_slot_names: set[str] = set()
    for _cname in _dc_class_names:
        for _sname in (classes[_cname].get("slots") or []):
            _dc_slot_names.add(_sname)

    dc_types = OrderedDict((k, v) for k, v in types.items() if _is_dc(v))
    dc_enums = OrderedDict((k, v) for k, v in enums.items() if _is_dc(v))
    dc_subsets_d = OrderedDict((k, v) for k, v in subsets.items() if k in _DC_SUBSETS)
    dc_classes = OrderedDict((k, v) for k, v in classes.items() if _is_dc(v))
    dc_slots = OrderedDict(
        (k, v) for k, v in slots_section.items() if k in _dc_slot_names
    )

    fix_types = OrderedDict((k, v) for k, v in types.items() if not _is_dc(v))
    fix_enums = OrderedDict((k, v) for k, v in enums.items() if not _is_dc(v))
    fix_subsets_d = OrderedDict(
        (k, v) for k, v in subsets.items() if k not in _DC_SUBSETS
    )
    fix_classes = OrderedDict((k, v) for k, v in classes.items() if not _is_dc(v))
    fix_slots = OrderedDict(
        (k, v) for k, v in slots_section.items() if k not in _dc_slot_names
    )

    if dc_out_file is None:
        dc_out_file = out_file.with_name(out_file.stem + "_dc" + out_file.suffix)

    dc_hdr: OrderedDict = OrderedDict()
    dc_hdr["id"] = "https://w3id.org/lmodel/fix-orchestra/dc"
    dc_hdr["name"] = "fix_orchestra_dc"
    dc_hdr["title"] = "FIX Orchestra - Dublin Core vocabularies"
    dc_hdr["description"] = (
        "Dublin Core Elements 1.1, Dublin Core Terms, DCMI Type Vocabulary, "
        "and W3C xml.xsd namespace declarations. "
        "Auto-generated from dc.xsd, dcterms.xsd, dcmitype.xsd, xml.xsd."
    )
    dc_hdr["license"] = "Apache-2.0"
    dc_hdr["prefixes"] = OrderedDict(
        [
            ("fix_orchestra", "https://w3id.org/lmodel/fix-orchestra/"),
            ("linkml", "https://w3id.org/linkml/"),
            ("rdf", "http://www.w3.org/1999/02/22-rdf-syntax-ns#"),
            ("rdfs", "http://www.w3.org/2000/01/rdf-schema#"),
            ("xsd", "http://www.w3.org/2001/XMLSchema#"),
            ("dc", "http://purl.org/dc/elements/1.1/"),
            ("dcterms", "http://purl.org/dc/terms/"),
            ("dctypes", "http://purl.org/dc/dcmitype/"),
            ("XML", "http://www.w3.org/XML/1998/namespace#"),
        ]
    )
    dc_hdr["default_prefix"] = "fix_orchestra"
    dc_hdr["default_range"] = "string"
    dc_hdr["imports"] = ["linkml:types"]

    dc_doc: OrderedDict = OrderedDict(dc_hdr)
    if dc_types:
        dc_doc["types"] = dc_types
    if dc_subsets_d:
        dc_doc["subsets"] = dc_subsets_d
    if dc_enums:
        dc_doc["enums"] = dc_enums
    if dc_classes:
        dc_doc["classes"] = dc_classes
    if dc_slots:
        dc_doc["slots"] = dc_slots

    dc_lines = [
        "---",
        "# Auto-generated by scripts/schema_to_linkml.py",
        "# Source: upstream-releases/{dc,dcterms,dcmitype,xml}.xsd",
        "# DO NOT EDIT BY HAND - re-run the script to regenerate.",
        "",
    ]
    dc_lines.extend(dump_yaml(dc_doc, separate=False))
    dc_lines.append("")
    dc_out_file.parent.mkdir(parents=True, exist_ok=True)
    dc_out_file.write_text("\n".join(dc_lines), encoding="utf-8")
    print(f"  Wrote: {dc_out_file}", file=sys.stderr)

    # Rebuild entity dicts with only FIX-schema entities so the document
    # assembly below produces the lean main schema.
    types = fix_types
    enums = fix_enums
    subsets = fix_subsets_d
    classes = fix_classes
    slots_section = fix_slots

    # ---- Document assembly --------------------------------------------------
    header: OrderedDict = OrderedDict()
    header["id"] = "https://w3id.org/lmodel/fix-orchestra"
    header["name"] = "fix_orchestra"
    header["title"] = "FIX Orchestra"
    header["description"] = (
        "LinkML schema generated from the FIX Orchestra "
        "v1.1-RC2 XSD artifacts (repository.xsd, "
        "repositorytypes.xsd, interfaces.xsd)."
    )
    header["license"] = "Apache-2.0"
    header["see_also"] = [
        "https://www.fixtrading.org/standards/fix-orchestra-standard/",
        "https://github.com/FIXTradingCommunity/fix-orchestra",
        "https://github.com/FIXTradingCommunity/fix-orchestra-spec",
        "https://lmodel.github.io/fix-orchestra",
    ]
    header["source"] = "https://www.fixtrading.org/standards/fix-orchestra-standard/"
    header["version"] = "1.1-rc2"
    header["notes"] = [
        "(c) Copyright 2016-2024 FIX Protocol Limited. "
        "Creative Commons Attribution-NoDerivatives 4.0 International Public "
        "License (CC BY-ND 4.0) applies to the upstream XSD specification.",
        "This LinkML schema is auto-generated by scripts/schema_to_linkml.py - "
        "edit the script (or the upstream XSDs) and re-run, do not edit this "
        "file by hand.",
    ]
    header["annotations"] = OrderedDict(
        [
            ("xsd_sources", "repository.xsd, repositorytypes.xsd, interfaces.xsd"),
            (
                "xsd_target_namespace_fixr",
                "http://fixprotocol.io/2024/orchestra/repository",
            ),
            (
                "xsd_target_namespace_fixi",
                "http://fixprotocol.io/2024/orchestra/interfaces",
            ),
        ]
    )

    header["prefixes"] = OrderedDict(
        [
            ("fix_orchestra", "https://w3id.org/lmodel/fix-orchestra/"),
            ("linkml", "https://w3id.org/linkml/"),
            ("rdf", "http://www.w3.org/1999/02/22-rdf-syntax-ns#"),
            ("rdfs", "http://www.w3.org/2000/01/rdf-schema#"),
            ("xsd", "http://www.w3.org/2001/XMLSchema#"),
            ("skos", "http://www.w3.org/2004/02/skos/core#"),
            ("schema", "http://schema.org/"),
            ("dc", "http://purl.org/dc/elements/1.1/"),
            ("dcterms", "http://purl.org/dc/terms/"),
            ("dctypes", "http://purl.org/dc/dcmitype/"),
            ("XML", "http://www.w3.org/XML/1998/namespace#"),
            ("fixr", "http://fixprotocol.io/2024/orchestra/repository/"),
            ("fixi", "http://fixprotocol.io/2024/orchestra/interfaces/"),
            ("fixml", "http://fixprotocol.io/2022/orchestra/appinfo/fixml#"),
        ]
    )
    header["default_prefix"] = "fix_orchestra"
    header["default_range"] = "string"
    header["imports"] = ["linkml:types", dc_out_file.stem]

    doc: OrderedDict = OrderedDict(header)
    if types:
        doc["types"] = types
    if subsets:
        doc["subsets"] = subsets
    if enums:
        doc["enums"] = enums
    doc["classes"] = classes
    if slots_section:
        doc["slots"] = slots_section

    out_lines = [
        "---",
        "# Auto-generated by scripts/schema_to_linkml.py",
        "# Source: upstream-releases/{repository,repositorytypes,interfaces}.xsd",
        "# DO NOT EDIT BY HAND - re-run the script to regenerate.",
        "",
    ]
    out_lines.extend(dump_yaml(doc, separate=False))
    out_lines.append("")
    out_file.parent.mkdir(parents=True, exist_ok=True)
    out_file.write_text("\n".join(out_lines), encoding="utf-8")

    # ---- Coverage report ----------------------------------------------------
    r_st = len(repo_types["simple_types"])
    r_ct = len(repo_types["complex_types"])
    r_ag = len(repo_types["attribute_groups"])
    r_el = len(repo_types["elements"])
    rr_el = len(repo_root["elements"])
    i_st = len(iface["simple_types"])
    i_ct = len(iface["complex_types"])
    i_el = len(iface["elements"])

    expected_classes = r_ct + r_ag + r_el + rr_el + i_ct + i_el
    expected_enums = sum(
        1 for v in repo_types["simple_types"].values() if v["kind"] == "enum"
    )
    expected_enums += sum(
        1 for v in iface["simple_types"].values() if v["kind"] == "enum"
    )
    expected_types = (r_st + i_st) - expected_enums

    # Aux XSD coverage counts (parsed again for reporting; cheap).
    aux_counts: dict[str, dict] = {}
    for scope_key, fname, *_ in AUX_XSDS:
        p = upstream_dir / fname
        if not p.is_file():
            continue
        d = parse_aux_xsd(p)
        aux_counts[fname] = {
            "simpleTypes": len(d["simple_types"]),
            "complexTypes": len(d["complex_types"]),
            "attributeGroups": len(d["attribute_groups"]),
            "elements": len(d["elements"]),
            "attributes": len(d["attributes"]),
            "groups": len(d["groups"]),
        }

    print("=== FIX Orchestra XSD -> LinkML coverage ===", file=sys.stderr)
    print(
        f"  repositorytypes.xsd : simpleTypes={r_st} complexTypes={r_ct} "
        f"attributeGroups={r_ag} elements={r_el}",
        file=sys.stderr,
    )
    print(f"  repository.xsd      : elements={rr_el}", file=sys.stderr)
    print(
        f"  interfaces.xsd      : simpleTypes={i_st} complexTypes={i_ct} "
        f"elements={i_el}",
        file=sys.stderr,
    )
    for fname, c in aux_counts.items():
        print(
            f"  {fname:<19} : simpleTypes={c['simpleTypes']} "
            f"complexTypes={c['complexTypes']} "
            f"attributeGroups={c['attributeGroups']} "
            f"elements={c['elements']} attributes={c['attributes']} "
            f"groups={c['groups']}",
            file=sys.stderr,
        )
    aux_expected = sum(
        c["simpleTypes"]
        + c["complexTypes"]
        + c["attributeGroups"]
        + c["elements"]
        + (1 if c["attributes"] else 0)
        + c["groups"]
        for c in aux_counts.values()
    )
    print(
        f"  Expected (FIX)      : classes={expected_classes} "
        f"enums={expected_enums} types={expected_types}",
        file=sys.stderr,
    )
    print(f"  Aux entities        : ~{aux_expected} additional", file=sys.stderr)
    print(
        f"  Emitted (all)       : classes={len(classes)} "
        f"enums={len(enums)} types={len(types)}",
        file=sys.stderr,
    )
    if len(classes) < expected_classes:
        print(
            f"  WARN: emitted {len(classes)} classes; expected >= {expected_classes}",
            file=sys.stderr,
        )
    print(f"  Wrote: {out_file}", file=sys.stderr)


# ---------------------------------------------------------------------------
# Hand-rolled YAML emitter - preserves insertion order, no external deps.
# ---------------------------------------------------------------------------


def yaml_quote(s: str) -> str:
    """Return *s* as a YAML plain scalar if safe, otherwise single- or double-quoted.

    Plain scalars in YAML block context only require quoting when:
    - The string is empty, a boolean/null keyword, or looks like a number.
    - The first character is a YAML indicator (``'``, ``"``, ``|``, ``>``,
      ``!``, ``@``, `` ` ``, ``[``, ``{``, ``&``, ``*``, ``%``).
    - The first character is ``#`` (comment) or ``:`` (mapping value indicator).
    - ``-`` or ``?`` followed immediately by a space/tab (block sequence /
      mapping key indicator).
    - The string contains ``": "`` (would be parsed as mapping) or ``" #"``
      (inline comment), or ends with ``:``.
    - Leading or trailing whitespace.

    NOTE: bare ``:`` inside a string (e.g. ``https://...``, ``fixr:name``) is
    fine and does NOT require quoting in block context.
    """
    s = str(s)
    # Normalise embedded newlines to a single space - a literal '\n' inside a
    # YAML flow scalar breaks the parser (the continuation is mis-interpreted
    # as a new mapping key).
    if "\n" in s:
        s = " ".join(s.split())
    if s == "":
        return "''"
    if re.fullmatch(r"-?\d+(\.\d+)?([eE][+-]?\d+)?", s):
        return f"'{s}'"
    if s.lower() in ("true", "false", "null", "yes", "no", "on", "off", "~"):
        return f"'{s}'"
    first = s[0]
    needs_quote = (
        first in "'\"|>!@`[{&*%"
        or first == "#"
        or first == ":"
        or (first == "-" and len(s) > 1 and s[1] in " \t")
        or (first == "?" and len(s) > 1 and s[1] in " \t")
        or ": " in s
        or s.endswith(":")
        or " #" in s
        or s[0].isspace()
        or s[-1].isspace()
    )
    if needs_quote:
        if "'" not in s:
            return f"'{s}'"
        esc = s.replace("\\", "\\\\").replace('"', '\\"')
        return f'"{esc}"'
    return s


def yaml_key(k) -> str:
    return (
        yaml_quote(k) if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", str(k)) else str(k)
    )


def scalar(v) -> str:
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return str(v)
    if v is None:
        return "null"
    return yaml_quote(v)


# Keys whose dict values should be emitted with a blank line between each
# child entry. Applies anywhere these keys appear in the schema document.
SEPARATED_DICT_KEYS = {
    "types",
    "enums",
    "classes",
    "slots",
    "subsets",
    "attributes",
    "unique_keys",
}


def dump_yaml(value, indent: int = 0, separate: bool = False) -> list[str]:
    """Serialise a Python dict / list / scalar to indented YAML lines.

    When ``separate`` is True, a blank line is inserted between immediate
    dict children when at least one of the adjacent values is complex
    (dict or non-empty list). This keeps scalar header fields packed
    together while visually separating structured sections / elements.

    List items are emitted at the same indentation level as their parent key
    (``{pad}-`` style), matching the block-sequence compact notation used by
    standard YAML formatters.
    """
    pad = "  " * indent
    lines: list[str] = []
    if isinstance(value, dict):
        if not value:
            return ["{}"]
        items = list(value.items())
        prev_complex = False
        for idx, (k, v) in enumerate(items):
            this_complex = (isinstance(v, dict) and v) or (isinstance(v, list) and v)
            if idx > 0 and separate and (this_complex or prev_complex):
                lines.append("")
            key = yaml_key(k)
            child_separate = isinstance(v, dict) and k in SEPARATED_DICT_KEYS
            if isinstance(v, dict):
                if not v:
                    lines.append(f"{pad}{key}: {{}}")
                else:
                    lines.append(f"{pad}{key}:")
                    lines.extend(dump_yaml(v, indent + 1, separate=child_separate))
            elif isinstance(v, list):
                if not v:
                    lines.append(f"{pad}{key}: []")
                else:
                    lines.append(f"{pad}{key}:")
                    for item in v:
                        if isinstance(item, (dict, list)):
                            sub = dump_yaml(item, indent + 1)
                            first = sub[0].lstrip()
                            lines.append(f"{pad}- {first}")
                            for s in sub[1:]:
                                lines.append(s)
                        else:
                            lines.append(f"{pad}- {scalar(item)}")
            elif v is None:
                lines.append(f"{pad}{key}:")
            else:
                lines.append(f"{pad}{key}: {scalar(v)}")
            prev_complex = this_complex
    return lines


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    here = Path(__file__).resolve().parent
    project_dir = here.parent
    default_upstream = Path(
        os.environ.get("UPSTREAM_DIR", project_dir / "upstream-releases")
    )
    default_out = Path(
        os.environ.get(
            "OUT_FILE",
            project_dir / "src" / "fix_orchestra" / "schema" / "fix_orchestra.yaml",
        )
    )
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument(
        "--upstream-dir",
        type=Path,
        default=default_upstream,
        help="directory containing the FIX Orchestra XSD files",
    )
    p.add_argument(
        "--out-file",
        type=Path,
        default=default_out,
        help="destination LinkML YAML schema path",
    )
    p.add_argument(
        "--orchestra-xml",
        type=Path,
        default=None,
        metavar="XML",
        help=(
            "FIX Orchestra XML repository file (e.g. OrchestraFIXLatest.xml). "
            "When supplied, appends 38 FIX base datatype entries to the schema "
            "types section, each annotated with proto_scalar."
        ),
    )
    args = p.parse_args(argv)
    for f in ("repository.xsd", "repositorytypes.xsd", "interfaces.xsd"):
        if not (args.upstream_dir / f).is_file():
            print(f"ERROR: missing {args.upstream_dir / f}", file=sys.stderr)
            return 1
    if args.orchestra_xml is not None and not args.orchestra_xml.is_file():
        print(f"ERROR: missing --orchestra-xml {args.orchestra_xml}", file=sys.stderr)
        return 1
    convert(
        args.upstream_dir,
        args.out_file,
        orchestra_xml=args.orchestra_xml,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
