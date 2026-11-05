#!/usr/bin/env python3
"""Write the schema's modules from the Orchestra XSDs under upstream/.

Each edition of Orchestra is two XSDs: the repository (``repository.xsd``, which includes
``repositorytypes.xsd``) and the interfaces (``interfaces.xsd``). This script reads both
editions and writes four modules into ``src/fix_orchestra/schema/``:

- ``fix_orchestra_v1_0.yaml`` and ``fix_orchestra_v1_1.yaml``, one class per complex type
  of an edition, with the edition's suffix;
- ``fix_orchestra_common.yaml``, the value lists both editions share, the Dublin Core
  metadata class and the classes that hold XML the XSDs leave open;
- ``fix_orchestra.yaml``, the umbrella that imports them.

A key is the XML name in snake case after ``fixr_`` for the repository and ``fixi_`` for
the interfaces, and an ``xml_attribute`` or ``xml_element`` annotation keeps the XML name,
so ``scripts/orchestra_xml_to_yaml.py`` can convert a document both ways. An attribute group
becomes a mixin, an element with an anonymous type a class, and a repeated choice a list of
one-key members, so the order of a message's fields survives. Every description comes from
``scripts/orchestra_words.yaml``, which is the project's own wording; no XSD documentation
is copied. The script stops on any XSD construct or name it has no rule or words for, so a
new edition cannot lose an element silently. Usage::

    uv run python scripts/orchestra_xsd_to_linkml.py [--check]
"""

from __future__ import annotations

import argparse
import re
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
UPSTREAM = ROOT / "upstream"
SCHEMA_DIR = ROOT / "src" / "fix_orchestra" / "schema"
WORDS = ROOT / "scripts" / "orchestra_words.yaml"

XS = "{http://www.w3.org/2001/XMLSchema}"
XML_NS = "http://www.w3.org/XML/1998/namespace"
W3ID = "https://w3id.org/lmodel/fix-orchestra"

# The two editions: where their XSDs sit, their namespaces and how upstream names them.
EDITIONS = {
    "V10": {
        "module": "fix_orchestra_v1_0",
        "folder": "v1.0",
        "version": "1.0",
        "title": "FIX Orchestra v1.0 Technical Standard",
        "source": "https://github.com/FIXTradingCommunity/fix-orchestra-spec/tree/v1.0/"
        "v1-0-STANDARD/resources",
        "repository": "fix-orchestra-spec",
        "tag": "v1.0",
        "commit": "e2b65db8505244f2708c468fe7cad60855fa9834",
        "fixr": "http://fixprotocol.io/2020/orchestra/repository",
        "fixi": "http://fixprotocol.io/2020/orchestra/interfaces",
    },
    "V11": {
        "module": "fix_orchestra_v1_1",
        "folder": "v1.1-rc3",
        "version": "1.1-rc3",
        "title": "FIX Orchestra v1.1 Release Candidate 3",
        "source": "https://github.com/FIXTradingCommunity/fix-orchestra/tree/v1.1-rc3/"
        "repository/src/main/resources/xsd",
        "repository": "fix-orchestra",
        "tag": "v1.1-rc3",
        "commit": "eb4bb9de3bd8802c6e5e0aba06182407b22acc9b",
        "fixr": "http://fixprotocol.io/2026/orchestra/repository",
        "fixi": "http://fixprotocol.io/2026/orchestra/interfaces",
    },
}

# Each XSD's key prefix and the files that make it up.
DOCUMENTS = {
    "fixr": ("repository", ("repository.xsd", "repositorytypes.xsd")),
    "fixi": ("interfaces", ("interfaces.xsd",)),
}

# The class each complex type, global element or anonymous type becomes, without the
# Orchestra prefix and the edition suffix. An anonymous type is named by its path.
CLASS_NAMES = {
    "fixr": {
        "repository": "Repository",
        "actors": "Actors",
        "categories": "Categories",
        "codeSets": "CodeSets",
        "components": "Components",
        "concepts": "Concepts",
        "datatypes": "Datatypes",
        "fields": "Fields",
        "groups": "Groups",
        "messages": "Messages",
        "sections": "Sections",
        "scenarios": "Scenarios",
        "encodingStandards": "EncodingStandards",
        "encodingStandard": "EncodingStandard",
        "encodings": "Encodings",
        "datatype": "Datatype",
        "actionType": "Action",
        "actorType": "Actor",
        "annotation": "Annotation",
        "appinfo": "Appinfo",
        "blockAssignmentType": "BlockAssignment",
        "categoryType": "Category",
        "codeSetType": "CodeSet",
        "codeType": "Code",
        "componentRefType": "ComponentRef",
        "componentRuleType": "ComponentRule",
        "componentType": "Component",
        "conceptType": "Concept",
        "documentation": "Documentation",
        "fieldRefType": "FieldRef",
        "fieldRuleType": "FieldRule",
        "fieldType": "Field",
        "flowType": "Flow",
        "groupRefType": "GroupRef",
        "groupType": "Group",
        "identifiersType": "Identifiers",
        "identifierType": "Identifier",
        "mappedDatatype": "MappedDatatype",
        "messageRefType": "MessageRef",
        "messageType": "Message",
        "responseType": "Response",
        "scenarioType": "Scenario",
        "sectionType": "Section",
        "stateMachineType": "StateMachine",
        "stateType": "State",
        "timerSchedule": "TimerSchedule",
        "timerType": "Timer",
        "transitionType": "Transition",
        "triggerType": "Trigger",
        "baseEncoding": "BaseEncoding",
        "namedEncoding": "NamedEncoding",
        "unnamedEncoding": "UnnamedEncoding",
        "messageType/structure": "MessageStructure",
        "messageType/responses": "Responses",
        "fieldRuleType/unique": "Unique",
        "mappedDatatype/extension": "DatatypeExtension",
    },
    "fixi": {
        "interfaces": "Interfaces",
        "annotation": "InterfaceAnnotation",
        "appinfo": "InterfaceAppinfo",
        "documentation": "InterfaceDocumentation",
        "baseInterfaceType": "BaseInterface",
        "encodingType": "Encoding",
        "identifierType": "SessionIdentifier",
        "interfaceType": "Interface",
        "interfaceType/sessions": "Sessions",
        "protocolType": "Protocol",
        "serviceType": "Service",
        "sessionProtocolType": "SessionProtocol",
        "sessionType": "Session",
        "transportProtocolType": "Transport",
        "userIntefaceType": "UserInterface",
        "userInterfaceType": "UserInterface",
    },
}

# The mixin each attribute group becomes. A group no type uses is left out.
MIXIN_NAMES = {
    "entityAttribGrp": "Pedigree",
    "oidGrp": "Identity",
    "refidGrp": "Reference",
    "fieldAttribGrp": "FieldConstraints",
    "containerAttribGrp": "Container",
    "scenarioRefGrp": "ScenarioReference",
}

# The class a repeated choice's members become, by the elements the choice offers. Each
# member holds one of them, so a list of members keeps the elements' order.
MEMBER_NAMES = {
    frozenset({"componentRef", "groupRef", "fieldRef"}): "StructureMember",
    frozenset({"componentRef", "groupRef", "fieldRef", "messageRef"}): "ConceptMember",
    frozenset(
        {"field", "fieldRef", "component", "componentRef", "group", "groupRef"}
    ): "ActionParameter",
    frozenset({"messageRef", "assign", "trigger", "timerSchedule"}): "ActionStep",
    frozenset(
        {
            "field",
            "fieldRef",
            "component",
            "componentRef",
            "group",
            "groupRef",
            "states",
            "timer",
        }
    ): "ActorMember",
    frozenset({"actor", "flow"}): "ActorsMember",
    frozenset({"documentation", "appinfo"}): "AnnotationMember",
    frozenset({"correlate", "assign"}): "IdentifiersMember",
}

# The key of a repeated choice's list, by the choice's id where it has one.
CHOICE_KEYS = {None: "members", "parameters": "parameters", "actions": "actions"}

# The value lists both editions share, by XSD name and values, and the name each takes.
# A list whose values differ between the editions takes the edition's suffix instead.
ENUM_NAMES = {
    "presence_t": "Presence",
    "supportType": "Support",
    "changeType_t": "ChangeKind",
    "memberType": "MemberSelection",
    "reliability_t": "Reliability",
    "synchronization": "Synchronization",
    "timerOperation": "TimerOperation",
    "purpose_enum": "Purpose",
    "CatComponentType_t": "CategoryContent",
    "CatIncludeFile_t": "CategoryIncludeFile",
    "datatypeStandard_enum": "DatatypeStandard",
    "UnionDataType_t": "UnionDatatype",
    "layer_t": "Layer",
    "messageCast_t": "MessageCast",
    "role_t": "Role",
    "protocolEnum_t": "ProtocolName",
    "transportUse_enum": "TransportUse",
}

# Simple types the XSDs declare and never use; listed so a new one stops the script.
UNUSED_TYPES = {
    "CompID_t",
    "Edition_t",
    "GroupName_t",
    "IncludeFile_t",
    "CategoryComponentType_t",
    "Term_t",
    "Usage_t",
    "Sort_t",
}
UNUSED_GROUPS = {"messageAttribGrp"}

# Patterns for XSD built-in types that LinkML has no type for. Each is anchored, since an
# XSD pattern matches the whole value and a LinkML pattern any part of it.
TOKEN = r"\S+( \S+)*"
BUILTIN = {
    "string": ("string", None, None, None),
    "normalizedString": ("string", None, None, None),
    "token": ("string", f"^({TOKEN})?$", None, None),
    "anyURI": ("uri", None, None, None),
    "boolean": ("boolean", None, None, None),
    "integer": ("integer", None, None, None),
    "int": ("integer", None, -2147483648, 2147483647),
    "short": ("integer", None, -32768, 32767),
    "nonNegativeInteger": ("integer", None, 0, None),
    "positiveInteger": ("integer", None, 1, None),
    "language": ("string", r"^[A-Za-z]{1,8}(-[A-Za-z0-9]{1,8})*$", None, None),
    "duration": (
        "string",
        r"^-?P(?=\d|T\d)(\d+Y)?(\d+M)?(\d+D)?(T(?=\d)(\d+H)?(\d+M)?(\d+(\.\d+)?S)?)?$",
        None,
        None,
    ),
    "dateTime": (
        "string",
        r"^-?\d{4,}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?(Z|[+-]\d{2}:\d{2})?$",
        None,
        None,
    ),
}

# The Dublin Core terms and elements a metadata block may hold, in the order DCMI lists
# them. Each becomes a multivalued key of OrchestraMetadata under its own IRI.
DC_ELEMENTS = (
    "title",
    "creator",
    "subject",
    "description",
    "publisher",
    "contributor",
    "date",
    "type",
    "format",
    "identifier",
    "source",
    "language",
    "relation",
    "coverage",
    "rights",
)


def snake(name: str) -> str:
    """An XML name in snake case: FIXMLFileName gives fixml_file_name, addedEP added_ep."""
    name = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", name)
    name = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", name)
    return name.replace(":", "_").replace("-", "_").lower()


def local(qname: str) -> str:
    return qname.split(":", 1)[-1]


@dataclass
class Attr:
    """One key of a class: an XML attribute, an element, text, or a list of members."""

    key: str
    kind: str  # attribute, element, text, members, any, any_attribute
    xml: str | None = None
    range: str = "string"
    required: bool = False
    multivalued: bool = False
    inlined: bool = False
    pattern: str | None = None
    minimum: int | None = None
    maximum: int | None = None
    default: str | None = None
    any_of: list[str] | None = None
    choice: list[str] | None = None
    words_key: str | None = None


@dataclass
class Cls:
    name: str
    xsd: str
    doc: str
    attrs: list[Attr] = field(default_factory=list)
    mixins: list[str] = field(default_factory=list)
    is_a: str | None = None
    abstract: bool = False
    mixin: bool = False
    tree_root: bool = False
    member: bool = False


class Words:
    """The project's own wording, read from scripts/orchestra_words.yaml."""

    def __init__(self, path: Path):
        self.data = yaml.safe_load(path.read_text(encoding="utf-8"))
        self.missing: list[str] = []

    def _get(self, section: str, key: str):
        found = (self.data.get(section) or {}).get(key)
        if found is None:
            self.missing.append(f"{section}: {key}")
            return {"title": "MISSING", "description": "MISSING"}
        return found if isinstance(found, dict) else {"description": found}

    def cls(self, base: str) -> dict:
        return self._get("classes", base)

    def slot(self, suffix: str, doc: str, base: str, xml: str) -> str:
        overrides = self.data.get("overrides") or {}
        keys = (
            f"{suffix}:{base}.{xml}",
            f"{doc}:{base}.{xml}",
            f"{base}.{xml}",
            f"{doc}:{xml}",
        )
        for key in keys:
            if key in overrides:
                return overrides[key]
        return self._get("slots", xml)["description"]

    def enum(self, name: str) -> dict:
        return self._get("enums", name)


class Edition:
    """The complex types, simple types, groups and elements of one edition's XSDs."""

    def __init__(self, suffix: str, words: Words):
        self.suffix = suffix
        self.info = EDITIONS[suffix]
        self.words = words
        self.classes: dict[str, Cls] = {}
        self.enums: dict[str, tuple[str, tuple[str, ...]]] = {}
        self.used_types: set[str] = set()

    def run(self) -> None:
        for doc, (folder, files) in DOCUMENTS.items():
            self.doc = doc
            self.complex, self.simple, self.groups, self.elements = {}, {}, {}, {}
            for name in files:
                path = UPSTREAM / self.info["folder"] / folder / name
                root = ET.parse(path).getroot()
                for child in root:
                    if not isinstance(child.tag, str):
                        continue
                    tag, name_ = child.tag.removeprefix(XS), child.get("name")
                    target = {
                        "complexType": self.complex,
                        "simpleType": self.simple,
                        "attributeGroup": self.groups,
                        "element": self.elements,
                    }.get(tag)
                    if target is not None:
                        target[name_] = child
                    elif tag not in ("annotation", "import", "include"):
                        raise SystemExit(f"{path.name}: no rule for top-level {tag}")
            for group in set(self.groups) - set(MIXIN_NAMES) - UNUSED_GROUPS:
                raise SystemExit(f"{self.suffix} {doc}: no mixin name for {group}")
            for name, node in self.complex.items():
                self.add_class(name, node)
            for name, node in self.elements.items():
                anon = node.find(f"{XS}complexType")
                if anon is not None:
                    self.add_class(name, anon, element=node)
            unused = set(self.simple) - self.used_types - UNUSED_TYPES
            if unused:
                raise SystemExit(f"{self.suffix} {doc}: no rule for unused {unused}")
            self.used_types = set()
            root_name = "repository" if doc == "fixr" else "interfaces"
            self.classes[self.cname(root_name)].tree_root = True

    # Names

    def base(self, xsd: str) -> str:
        try:
            return CLASS_NAMES[self.doc][xsd]
        except KeyError:
            raise SystemExit(f"{self.suffix} {self.doc}: no class name for {xsd}")

    def cname(self, xsd: str) -> str:
        return f"Orchestra{self.base(xsd)}{self.suffix}"

    def key(self, xml: str) -> str:
        if xml == "xml:base":
            return "xml_base"
        return f"{self.doc}_{snake(xml)}"

    # Simple types

    def simple_type(self, qname: str | None) -> dict:
        """The range and constraints of a simple type, by its QName."""
        if qname is None:
            return {"range": "string"}
        prefix, _, name = qname.rpartition(":")
        if prefix == "xs":
            rng, pattern, lo, hi = BUILTIN[name]
            return {"range": rng, "pattern": pattern, "minimum": lo, "maximum": hi}
        node = self.simple.get(name)
        if node is None:
            raise SystemExit(f"{self.suffix} {self.doc}: unknown simple type {qname}")
        self.used_types.add(name)
        return self._simple_node(name, node)

    def _simple_node(self, name: str | None, node) -> dict:
        restriction = node.find(f"{XS}restriction")
        union = node.find(f"{XS}union")
        if union is not None:
            members = union.get("memberTypes").split()
            if name == "unboundedIntType":
                self.used_types.add("unbounded")
                return {"range": "string", "pattern": r"^(\d+|unbounded)$"}
            parts = [self.simple_type(m) for m in members]
            enums = [p for p in parts if p.get("enum")]
            others = [p for p in parts if not p.get("enum")]
            if (
                len(enums) == 1
                and others
                and all(p["range"] == "string" for p in others)
            ):
                return {"range": "string", "any_of": [enums[0]["range"], "string"]}
            raise SystemExit(f"{self.suffix}: no rule for the union {name}")
        if restriction is None:
            raise SystemExit(f"{self.suffix}: no rule for the simple type {name}")
        values = [e.get("value") for e in restriction.findall(f"{XS}enumeration")]
        if values:
            return {"range": self.enum_name(name, tuple(values)), "enum": True}
        out = self.simple_type(restriction.get("base"))
        out = {k: v for k, v in out.items() if v is not None}
        facets = {
            child.tag.removeprefix(XS): child.get("value")
            for child in restriction
            if isinstance(child.tag, str) and child.tag != f"{XS}annotation"
        }
        lo_len = int(facets.pop("minLength", 0))
        hi_len = facets.pop("maxLength", None)
        xsd_pattern = facets.pop("pattern", None)
        if "minInclusive" in facets:
            out["minimum"] = int(facets.pop("minInclusive"))
        if "maxInclusive" in facets:
            out["maximum"] = int(facets.pop("maxInclusive"))
        if facets:
            raise SystemExit(f"{self.suffix}: no rule for facets {facets} on {name}")
        body = None
        if xsd_pattern is not None:
            body = f"({xsd_pattern})"
        elif out.get("pattern") == f"^({TOKEN})?$":
            body = f"({TOKEN})"
        if (lo_len or hi_len is not None) and body is None:
            out["pattern"] = f"^[\\s\\S]{{{lo_len},{hi_len or ''}}}$"
        elif lo_len or hi_len is not None:
            length = f"(?=[\\s\\S]{{{lo_len},{hi_len or ''}}}$)"
            out["pattern"] = f"^{length}{body}$"
        elif body is not None:
            out["pattern"] = f"^{body}$"
        return out

    def enum_name(self, xsd: str, values: tuple[str, ...]) -> str:
        if xsd is None or xsd not in ENUM_NAMES:
            raise SystemExit(f"{self.suffix}: no enum name for {xsd} {values}")
        name = f"Orchestra{ENUM_NAMES[xsd]}"
        self.enums[f"{self.doc}:{xsd}"] = (name, values)
        return name

    # Complex types

    def add_class(self, xsd: str, node, element=None, path: str | None = None) -> str:
        name = self.cname(path or xsd)
        if name in self.classes:
            return name
        base = self.base(path or xsd)
        cls = Cls(name=name, xsd=path or xsd, doc=self.doc)
        self.classes[name] = cls
        cls.abstract = node.get("abstract") == "true"
        if node.get("mixed") == "true":
            cls.attrs.append(
                Attr(key=f"{self.doc}_text", kind="text", words_key="#text")
            )
        content = node
        complex_content = node.find(f"{XS}complexContent")
        if complex_content is not None:
            extension = complex_content.find(f"{XS}extension")
            if extension is None:
                raise SystemExit(
                    f"{name}: no rule for complexContent without extension"
                )
            parent = local(extension.get("base"))
            cls.is_a = self.add_class(parent, self.complex[parent])
            content = extension
        self.particles(cls, base, content, xsd)
        for child in content:
            if not isinstance(child.tag, str):
                continue
            tag = child.tag.removeprefix(XS)
            if tag == "attribute":
                self.attribute(cls, base, child)
            elif tag == "attributeGroup":
                cls.mixins.append(self.mixin(local(child.get("ref"))))
            elif tag == "anyAttribute":
                cls.attrs.append(
                    Attr(
                        key=f"{self.doc}_other_attributes",
                        kind="any_attribute",
                        range="OrchestraXmlAttribute",
                        multivalued=True,
                        inlined=True,
                        words_key="#other_attributes",
                    )
                )
        return name

    def mixin(self, group: str) -> str:
        name = f"Orchestra{MIXIN_NAMES[group]}{self.suffix}Mixin"
        if name in self.classes:
            return name
        cls = Cls(name=name, xsd=group, doc=self.doc, mixin=True)
        self.classes[name] = cls
        for child in self.groups[group]:
            if not isinstance(child.tag, str):
                continue
            tag = child.tag.removeprefix(XS)
            if tag == "attribute":
                self.attribute(cls, MIXIN_NAMES[group], child)
            elif tag != "annotation":
                raise SystemExit(f"{group}: no rule for {tag}")
        return name

    def attribute(self, cls: Cls, base: str, node) -> None:
        if node.get("use") == "prohibited":
            return
        if node.get("ref"):
            if node.get("ref") != "xml:base":
                raise SystemExit(f"{cls.name}: no rule for attribute {node.get('ref')}")
            xml, spec = "xml:base", {"range": "uri"}
        else:
            xml = node.get("name")
            inline = node.find(f"{XS}simpleType")
            spec = (
                self._simple_node(None, inline)
                if inline is not None
                else self.simple_type(node.get("type"))
            )
        cls.attrs.append(
            Attr(
                key=self.key(xml),
                kind="attribute",
                xml=xml,
                required=node.get("use") == "required",
                default=node.get("default"),
                words_key=f"{base}.{xml}",
                **{k: v for k, v in spec.items() if k != "enum"},
            )
        )

    def particles(self, cls: Cls, base: str, node, xsd: str) -> None:
        for child in node:
            if not isinstance(child.tag, str):
                continue
            tag = child.tag.removeprefix(XS)
            if tag in ("sequence", "all"):
                if child.get("maxOccurs") not in (None, "1"):
                    if tag == "sequence" and len(child) == 1:
                        self.repeated_any(cls, base, child)
                        continue
                    raise SystemExit(f"{cls.name}: no rule for a repeated {tag}")
                self.particles(cls, base, child, xsd)
            elif tag == "choice":
                self.choice(cls, base, child, xsd)
            elif tag == "element":
                self.element(cls, base, child, xsd)
            elif tag == "any":
                self.any_element(cls, base)
            elif tag not in (
                "attribute",
                "attributeGroup",
                "anyAttribute",
                "annotation",
                "complexContent",
            ):
                raise SystemExit(f"{cls.name}: no rule for {tag}")

    def repeated_any(self, cls: Cls, base: str, node) -> None:
        inner = [c for c in node if isinstance(c.tag, str) and c.tag == f"{XS}any"]
        if len(inner) != 1:
            raise SystemExit(f"{cls.name}: no rule for this repeated sequence")
        self.any_element(cls, base)

    def any_element(self, cls: Cls, base: str) -> None:
        cls.attrs.append(
            Attr(
                key=f"{self.doc}_any",
                kind="any",
                range="OrchestraXmlElement",
                multivalued=True,
                inlined=True,
                words_key="#any",
            )
        )

    def choice(self, cls: Cls, base: str, node, xsd: str) -> None:
        elements = [
            c for c in node if isinstance(c.tag, str) and c.tag == f"{XS}element"
        ]
        names = [e.get("name") or local(e.get("ref")) for e in elements]
        repeated = node.get("maxOccurs") not in (None, "1")
        if not repeated:
            if len(elements) == 1 or node.get("minOccurs") == "0":
                for element in elements:
                    self.element(cls, base, element, xsd, optional=True)
                return
            # A single choice of elements: each is optional, and a rule says one.
            for element in elements:
                self.element(cls, base, element, xsd, optional=True)
            return
        if len(names) != len(node):
            others = [c.tag for c in node if c.tag != f"{XS}element"]
            if set(others) - {f"{XS}annotation", f"{XS}group"}:
                raise SystemExit(f"{cls.name}: no rule for a choice of {others}")
            groups = [c for c in node if c.tag == f"{XS}group"]
            if groups:
                raise SystemExit(f"{cls.name}: no rule for a group in a choice")
        member_name = MEMBER_NAMES.get(frozenset(names))
        if member_name is None:
            raise SystemExit(f"{cls.name}: no member name for the choice {names}")
        member_name = ("Interface" if self.doc == "fixi" else "") + member_name
        member = f"Orchestra{member_name}{self.suffix}"
        if member not in self.classes:
            mcls = Cls(name=member, xsd=f"choice of {', '.join(names)}", doc=self.doc)
            mcls.member = True
            self.classes[member] = mcls
            for element in elements:
                self.element(mcls, member_name, element, xsd, optional=True)
        cls.attrs.append(
            Attr(
                key=f"{self.doc}_{CHOICE_KEYS[node.get('id')]}",
                kind="members",
                range=member,
                multivalued=True,
                inlined=True,
                required=node.get("minOccurs") != "0",
                choice=names,
                words_key=f"#{CHOICE_KEYS[node.get('id')]}",
            )
        )

    def element(self, cls: Cls, base: str, node, xsd: str, optional=False) -> None:
        ref = node.get("ref")
        if ref is not None:
            name = local(ref)
            decl = self.elements[name]
            type_ = decl.get("type")
            anon = decl.find(f"{XS}complexType")
            if anon is not None:
                rng = self.add_class(name, anon)
                spec = {"range": rng, "inlined": True}
            else:
                spec = self._type_spec(cls, type_, name, xsd)
        else:
            name = node.get("name")
            type_ = node.get("type")
            anon = node.find(f"{XS}complexType")
            if anon is not None:
                path = f"{xsd}/{name}"
                rng = self.add_class(name, anon, path=path)
                spec = {"range": rng, "inlined": True}
            elif type_ is None and name == "metadata":
                spec = {"range": "OrchestraMetadata", "inlined": True}
            else:
                spec = self._type_spec(cls, type_, name, xsd)
        lo = int(node.get("minOccurs", "1"))
        hi = node.get("maxOccurs", "1")
        multivalued = hi != "1"
        if (
            name == "metadata"
            and type_
            and type_.endswith("elementOrRefinementContainer")
        ):
            spec = {"range": "OrchestraMetadata", "inlined": True}
        cls.attrs.append(
            Attr(
                key=self.key(name),
                kind="element",
                xml=name,
                required=lo >= 1 and not optional,
                multivalued=multivalued,
                words_key=f"{base}.{name}",
                **spec,
            )
        )

    def _type_spec(self, cls: Cls, type_: str | None, name: str, xsd: str) -> dict:
        if type_ is None:
            raise SystemExit(f"{cls.name}: element {name} has no type")
        prefix, _, tname = type_.rpartition(":")
        if prefix in ("fixr", "fixi") and tname in self.complex:
            return {
                "range": self.add_class(tname, self.complex[tname]),
                "inlined": True,
            }
        if prefix == "dcterms":
            return {"range": "OrchestraMetadata", "inlined": True}
        spec = self.simple_type(type_)
        return {k: v for k, v in spec.items() if k != "enum" and v is not None}


# YAML output


class _Dumper(yaml.SafeDumper):
    """Indents a list under its key, as yamllint's default asks."""

    def increase_indent(self, flow=False, indentless=False):
        return super().increase_indent(flow, False)


def _str(dumper, data):
    """Long prose folds under its key; a pattern or a short value stays on one line."""
    if "\n" in data:
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")
    if len(data) > 60 and " " in data and not data.startswith("^"):
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style=">")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


_Dumper.add_representer(str, _str)

# Top-level keys that open a block, which a blank line sets apart.
_BLOCKS = ("prefixes", "imports", "subsets", "enums", "classes")


def dump(doc: dict) -> str:
    """The module as YAML, with a blank line before each block and each element."""
    text = yaml.dump(doc, Dumper=_Dumper, sort_keys=False, width=80, allow_unicode=True)
    out = []
    for line in text.splitlines():
        top = re.match(r"^([a-z_]+):", line)
        element = re.match(r"^  [A-Za-z][A-Za-z0-9_]*:$", line)
        if out and ((top and top.group(1) in _BLOCKS) or element):
            out.append("")
        out.append(line)
    result = "---\n" + "\n".join(out) + "\n"
    if yaml.safe_load(result) != doc:
        raise SystemExit("the YAML written does not read back as the module")
    return result


def slot_dict(attr: Attr, words: Words, suffix: str, doc: str, base: str) -> dict:
    out: dict = {}
    xml = attr.words_key if attr.kind not in ("attribute", "element") else attr.xml
    out["description"] = words.slot(suffix, doc, base, xml)
    if attr.any_of:
        out["any_of"] = [{"range": r} for r in attr.any_of]
    else:
        out["range"] = attr.range
    if attr.required:
        out["required"] = True
    if attr.multivalued:
        out["multivalued"] = True
        if attr.inlined or attr.range.startswith("Orchestra"):
            out["inlined_as_list"] = True
        if attr.required:
            out["minimum_cardinality"] = 1
    elif attr.inlined:
        out["inlined"] = True
    if attr.pattern:
        out["pattern"] = attr.pattern
    if attr.minimum is not None:
        out["minimum_value"] = attr.minimum
    if attr.maximum is not None:
        out["maximum_value"] = attr.maximum
    if attr.default is not None:
        if attr.range.startswith("Orchestra"):
            out["ifabsent"] = f"{attr.range}({attr.default})"
        elif attr.range == "integer":
            out["ifabsent"] = f"int({attr.default})"
        else:
            out["ifabsent"] = f"string({attr.default})"
    annotations = {}
    if attr.kind == "attribute":
        annotations["xml_attribute"] = attr.xml
    elif attr.kind == "element":
        annotations["xml_element"] = attr.xml
    elif attr.kind == "members":
        annotations["xml_choice"] = " ".join(attr.choice)
    elif attr.kind == "text":
        annotations["xml_text"] = "true"
    elif attr.kind == "any":
        annotations["xml_any"] = "elements"
    elif attr.kind == "any_attribute":
        annotations["xml_any"] = "attributes"
    out["annotations"] = annotations
    return out


def class_dict(cls: Cls, edition: Edition, words: Words) -> dict:
    base = cls.name.removeprefix("Orchestra").removesuffix("Mixin")
    base = base.removesuffix(edition.suffix)
    text = words.cls(base)
    out: dict = {}
    out["title"] = f"{text['title']} ({edition.info['version']})"
    out["description"] = text["description"]
    if cls.is_a:
        out["is_a"] = cls.is_a
    if cls.abstract:
        out["abstract"] = True
    if cls.mixin:
        out["mixin"] = True
    if cls.mixins:
        out["mixins"] = cls.mixins
    if cls.tree_root:
        out["tree_root"] = True
    out["annotations"] = {"xsd_type": cls.xsd, "xml_namespace": edition.info[cls.doc]}
    out["in_subset"] = [cls.doc]
    if cls.member:
        out["exactly_one_of"] = [
            {"slot_conditions": {a.key: {"required": True}}} for a in cls.attrs
        ]
    attrs = {}
    for attr in cls.attrs:
        if attr.key in attrs:
            raise SystemExit(f"{cls.name}: two keys {attr.key}")
        attrs[attr.key] = slot_dict(attr, words, edition.suffix, cls.doc, base)
    if attrs:
        out["attributes"] = attrs
    return out


def header(
    module: str, title: str, description: str, version: str, source: str
) -> dict:
    return {
        "id": f"{W3ID}/{module}",
        "name": module,
        "title": title,
        "description": description,
        "version": version,
        "source": source,
        "license": "Apache-2.0",
        "see_also": [
            "https://lmodel.github.io/fix-orchestra",
            "https://github.com/FIXTradingCommunity/fix-orchestra-spec",
        ],
    }


PREFIXES = {
    "fix_orchestra": f"{W3ID}/",
    "linkml": "https://w3id.org/linkml/",
    "dc": "http://purl.org/dc/elements/1.1/",
    "dcterms": "http://purl.org/dc/terms/",
}


def build(words: Words) -> dict[str, str]:
    editions = {s: Edition(s, words) for s in EDITIONS}
    for edition in editions.values():
        edition.run()
    # Value lists: a list both editions give with the same values is shared and keeps its
    # plain name; a list only one edition gives takes that edition's suffix.
    occurrences: dict[str, dict[tuple[str, ...], set[str]]] = {}
    where: dict[tuple[str, str, str], tuple[str, ...]] = {}
    for suffix, edition in editions.items():
        for key, (name, values) in edition.enums.items():
            doc = key.split(":", 1)[0]
            occurrences.setdefault(name, {}).setdefault(values, set()).add(suffix)
            where[(suffix, doc, name)] = values
    shared: dict[str, tuple[str, ...]] = {}
    per_edition: dict[str, dict[str, tuple[str, ...]]] = {}
    for name, by_values in occurrences.items():
        for values, suffixes in by_values.items():
            if suffixes == set(editions):
                if name in shared:
                    raise SystemExit(f"{name}: two shared value lists")
                shared[name] = values
            elif len(suffixes) == 1:
                suffix = next(iter(suffixes))
                if f"{name}{suffix}" in per_edition.get(suffix, {}):
                    raise SystemExit(f"{name}{suffix}: two value lists")
                per_edition.setdefault(suffix, {})[f"{name}{suffix}"] = values
    final = {
        key: name if shared.get(name) == values else f"{name}{key[0]}"
        for key, values in where.items()
        for name in [key[2]]
    }

    def enum_doc(name: str, values: tuple[str, ...], version: str | None) -> dict:
        stem = re.sub(r"V1[01]$", "", name).removeprefix("Orchestra")
        text = words.enum(stem)
        out = {}
        out["title"] = text["title"] + (f" ({version})" if version else "")
        out["description"] = text["description"]
        vals = text.get("values") or {}
        pvs = {}
        for value in values:
            if value not in vals:
                words.missing.append(f"enums: {stem}.{value}")
            pvs[value] = {"description": vals.get(value, "MISSING")}
        out["permissible_values"] = pvs
        return out

    files = {}
    common = header(
        "fix_orchestra_common",
        "FIX Orchestra shared value lists and XML holders",
        words.data["modules"]["common"],
        ", ".join(e["version"] for e in EDITIONS.values()),
        "https://github.com/FIXTradingCommunity/fix-orchestra-spec",
    )
    common["prefixes"] = PREFIXES
    common["default_prefix"] = "fix_orchestra"
    common["default_range"] = "string"
    common["imports"] = ["linkml:types"]
    common["subsets"] = {
        name: {"description": words.data["subsets"][name]} for name in ("fixr", "fixi")
    }
    common["enums"] = {
        name: enum_doc(name, values, None) for name, values in sorted(shared.items())
    }
    common["classes"] = common_classes(words)
    files["fix_orchestra_common"] = dump(common)

    for suffix, edition in editions.items():
        info = edition.info
        doc = header(
            info["module"],
            info["title"],
            words.data["modules"][suffix],
            info["version"],
            info["source"],
        )
        doc["annotations"] = {
            "upstream_repository": f"https://github.com/FIXTradingCommunity/{info['repository']}",
            "upstream_tag": info["tag"],
            "upstream_commit": info["commit"],
            "xml_namespace_repository": info["fixr"],
            "xml_namespace_interfaces": info["fixi"],
        }
        doc["prefixes"] = PREFIXES
        doc["default_prefix"] = "fix_orchestra"
        doc["default_range"] = "string"
        doc["imports"] = ["linkml:types", "./fix_orchestra_common"]
        enums = per_edition.get(suffix, {})
        if enums:
            doc["enums"] = {
                name: enum_doc(name, values, info["version"])
                for name, values in sorted(enums.items())
            }
        classes = {}
        for name in sorted(edition.classes):
            cls = edition.classes[name]
            classes[name] = class_dict(cls, edition, words)
            renames = {
                key[2]: value
                for key, value in final.items()
                if key[0] == suffix and key[1] == cls.doc
            }
            _rename_ranges({name: classes[name]}, renames)
        doc["classes"] = classes
        files[info["module"]] = dump(doc)

    umbrella = header(
        "fix_orchestra",
        "FIX Orchestra",
        words.data["modules"]["umbrella"],
        ", ".join(e["version"] for e in EDITIONS.values()),
        "https://github.com/FIXTradingCommunity/fix-orchestra-spec",
    )
    umbrella["id"] = W3ID
    umbrella["annotations"] = {
        f"edition_{e['version']}": f"{e['repository']} {e['tag']} {e['commit']}"
        for e in EDITIONS.values()
    }
    umbrella["prefixes"] = PREFIXES
    umbrella["default_prefix"] = "fix_orchestra"
    umbrella["default_range"] = "string"
    umbrella["imports"] = [
        "linkml:types",
        "./fix_orchestra_common",
        "./fix_orchestra_v1_0",
        "./fix_orchestra_v1_1",
    ]
    files["fix_orchestra"] = dump(umbrella)
    return files


def _rename_ranges(classes: dict, renames: dict[str, str]) -> None:
    for cls in classes.values():
        for slot in (cls.get("attributes") or {}).values():
            if slot.get("range") in renames:
                slot["range"] = renames[slot["range"]]
            for part in slot.get("any_of") or []:
                if part.get("range") in renames:
                    part["range"] = renames[part["range"]]


def common_classes(words: Words) -> dict:
    """The metadata class and the two classes that hold XML the XSDs leave open."""
    meta_words = words.data["metadata"]
    attributes = {}
    for name in DC_ELEMENTS:
        attributes[f"dc_{name}"] = {
            "description": meta_words["dc"].format(term=name),
            "slot_uri": f"dc:{name}",
            "multivalued": True,
            "range": "string",
            "annotations": {
                "xml_element": f"{{http://purl.org/dc/elements/1.1/}}{name}"
            },
        }
    for name in dc_terms():
        attributes[f"dcterms_{snake(name)}"] = {
            "description": meta_words["dcterms"].format(term=name),
            "slot_uri": f"dcterms:{name}",
            "multivalued": True,
            "range": "string",
            "annotations": {"xml_element": f"{{http://purl.org/dc/terms/}}{name}"},
        }
    xml_words = words.data["xml"]
    return {
        "OrchestraMetadata": {
            "title": meta_words["title"],
            "description": meta_words["description"],
            "annotations": {
                "xsd_type": "dcterms:elementOrRefinementContainer",
            },
            "attributes": attributes,
        },
        "OrchestraXmlElement": {
            "title": xml_words["element_title"],
            "description": xml_words["element"],
            "attributes": {
                "xml_name": {
                    "description": xml_words["name"],
                    "required": True,
                    "pattern": r"^\{[^}]*\}[^\s{}]+$",
                },
                "xml_attributes": {
                    "description": xml_words["attributes"],
                    "range": "OrchestraXmlAttribute",
                    "multivalued": True,
                    "inlined_as_list": True,
                },
                "xml_text": {"description": xml_words["text"]},
                "xml_children": {
                    "description": xml_words["children"],
                    "range": "OrchestraXmlElement",
                    "multivalued": True,
                    "inlined_as_list": True,
                },
                "xml_tail": {"description": xml_words["tail"]},
            },
        },
        "OrchestraXmlAttribute": {
            "title": xml_words["attribute_title"],
            "description": xml_words["attribute"],
            "attributes": {
                "xml_name": {
                    "description": xml_words["name"],
                    "required": True,
                    "pattern": r"^(\{[^}]*\})?[^\s{}]+$",
                },
                "xml_value": {
                    "description": xml_words["value"],
                    "required": True,
                },
            },
        },
    }


def dc_terms() -> list[str]:
    """The DCMI terms the pinned dcterms.xsd declares, in its order."""
    path = UPSTREAM / "v1.0" / "repository" / "dcterms.xsd"
    root = ET.parse(path).getroot()
    names = [
        e.get("name")
        for e in root.findall(f"{XS}element")
        if e.get("substitutionGroup") is not None
    ]
    other = UPSTREAM / "v1.1-rc3" / "repository" / "dcterms.xsd"
    names_rc = [
        e.get("name")
        for e in ET.parse(other).getroot().findall(f"{XS}element")
        if e.get("substitutionGroup") is not None
    ]
    if names != names_rc:
        raise SystemExit("the two editions' dcterms.xsd declare different terms")
    return names


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--check", action="store_true", help="Fail if a module differs from its output"
    )
    args = parser.parse_args(argv)
    words = Words(WORDS)
    files = build(words)
    if words.missing:
        print("No words for:", file=sys.stderr)
        for item in sorted(set(words.missing)):
            print(f"  {item}", file=sys.stderr)
        return 2
    stale = []
    for module, text in files.items():
        path = SCHEMA_DIR / f"{module}.yaml"
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != text:
                stale.append(path.name)
        else:
            path.write_text(text, encoding="utf-8")
    if stale:
        print(f"Stale: {', '.join(stale)}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
