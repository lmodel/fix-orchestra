"""Checks the schema against the XSDs, and the converter against the XML, each through a
walk that shares no code with the scripts under test.

The first walk reads each edition's XSDs with the standard library and holds every
attribute and child element of every complex type to a key of the class that renders
it, with the same XML name, the same required-ness, the same repetition and the same
value list. The second
walk counts every element name and attribute value in a document, and then counts what
the records hold through the schema's annotations alone; the two counts must be equal.
"""

import xml.etree.ElementTree as ET
from collections import Counter
from functools import cache

import pytest
import yaml

from tests import conversion

XS = "{http://www.w3.org/2001/XMLSchema}"
XSI = "{http://www.w3.org/2001/XMLSchema-instance}"
XML_BASE = "{http://www.w3.org/XML/1998/namespace}base"
KINDS = {
    "repository": ("repository.xsd", "repositorytypes.xsd"),
    "interfaces": ("interfaces.xsd",),
}


@cache
def classes() -> dict:
    found = {}
    for path in sorted(conversion.SCHEMA_DIR.glob("fix_orchestra_*.yaml")):
        found |= yaml.safe_load(path.read_text(encoding="utf-8")).get("classes") or {}
    return found


@cache
def enums() -> dict:
    found = {}
    for path in sorted(conversion.SCHEMA_DIR.glob("fix_orchestra_*.yaml")):
        found |= yaml.safe_load(path.read_text(encoding="utf-8")).get("enums") or {}
    return found


def keys_of(name: str) -> dict:
    """A class's keys with its parents' and mixins'."""
    cls = classes()[name]
    out = {}
    for parent in ([cls["is_a"]] if cls.get("is_a") else []) + (
        cls.get("mixins") or []
    ):
        out |= keys_of(parent)
    return out | (cls.get("attributes") or {})


def _xml_name(slot: dict, kind: str):
    return (slot.get("annotations") or {}).get(kind)


@cache
def xsd_types(suffix: str, kind: str) -> dict:
    """Each complex type, global element's anonymous type and attribute group of one
    edition's XSD, by the name the schema's xsd_type annotation uses."""
    out = {}
    for file in KINDS[kind]:
        root = ET.parse(
            conversion.UPSTREAM / conversion.EDITION_FOLDERS[suffix] / kind / file
        ).getroot()
        for node in root:
            tag, name = node.tag.removeprefix(XS), node.get("name")
            if tag in ("complexType", "attributeGroup"):
                out[name] = node
            elif tag == "element" and node.find(f"{XS}complexType") is not None:
                out[name] = node.find(f"{XS}complexType")
            elif tag == "simpleType":
                out[f"simple:{name}"] = node
        for owner in root.iter():
            for element in owner.findall(f"{XS}element"):
                anon = element.find(f"{XS}complexType")
                if anon is not None and owner is not root:
                    parent = _named_ancestor(root, element)
                    if parent is not None:
                        out[f"{parent}/{element.get('name')}"] = anon
    return out


def _named_ancestor(root, target):
    for node in root:
        if node.get("name") and target in list(node.iter()):
            return node.get("name")
    return None


def _occurrence(node, element) -> tuple[bool, bool]:
    """Whether a child element of a type is required and whether it may repeat. A member
    of a choice is never required on its own, and repeats when the choice does."""
    for choice in node.iter(f"{XS}choice"):
        if element in list(choice):
            return False, choice.get("maxOccurs") not in (None, "1")
    return element.get("minOccurs", "1") != "0", element.get("maxOccurs", "1") != "1"


def _xsd_parts(suffix: str, kind: str, node) -> tuple[dict, dict]:
    """The attributes (name to required and type) and child elements (name to required
    and repeating) of one type, with its attribute groups and its extension's base."""
    types = xsd_types(suffix, kind)
    attributes, elements = {}, {}
    for child in node.iter():
        tag = child.tag.removeprefix(XS) if isinstance(child.tag, str) else ""
        if child is not node and tag == "complexType":
            continue
        if tag == "attribute" and _owned(node, child):
            if child.get("use") == "prohibited":
                continue
            name = child.get("name") or child.get("ref")
            attributes[name] = (child.get("use") == "required", child.get("type"))
        elif tag == "attributeGroup" and child.get("ref") and _owned(node, child):
            sub, _ = _xsd_parts(suffix, kind, types[child.get("ref").split(":")[1]])
            attributes |= sub
        elif tag == "extension":
            sub_a, sub_e = _xsd_parts(
                suffix, kind, types[child.get("base").split(":")[1]]
            )
            attributes |= sub_a
            elements |= sub_e
        elif tag == "element" and _owned(node, child):
            name = child.get("name") or child.get("ref").split(":")[1]
            elements[name] = _occurrence(node, child)
    return attributes, elements


def _owned(node, child) -> bool:
    """Whether a declaration belongs to this type and not to an anonymous type inside it."""
    for inner in node.iter(f"{XS}complexType"):
        if inner is not node and child in list(inner.iter()):
            return False
    return True


CASES = [
    (name, cls)
    for name, cls in sorted(classes().items())
    if (cls.get("annotations") or {}).get("xml_namespace")
    and not name.startswith(("OrchestraXml", "OrchestraMetadata"))
    and not (cls.get("annotations") or {})["xsd_type"].startswith("choice of")
]


def _edition(name: str) -> tuple[str, str]:
    cls = classes()[name]
    kind = "interfaces" if cls["in_subset"] == ["fixi"] else "repository"
    return name.removesuffix("Mixin")[-3:], kind


@pytest.mark.parametrize("name", [n for n, _ in CASES])
def test_each_attribute_and_element_of_the_xsd_has_its_key(name):
    """A class has a key for each attribute and child element of the XSD type it
    renders, under the same XML name, required exactly when the XSD requires it."""
    suffix, kind = _edition(name)
    cls = classes()[name]
    node = xsd_types(suffix, kind)[cls["annotations"]["xsd_type"]]
    xsd_attributes, xsd_elements = _xsd_parts(suffix, kind, node)
    keys = keys_of(name) if not cls.get("mixin") else cls.get("attributes") or {}
    attributes = {
        _xml_name(s, "xml_attribute"): s
        for s in keys.values()
        if _xml_name(s, "xml_attribute")
    }
    elements = {
        _xml_name(s, "xml_element")
        for s in keys.values()
        if _xml_name(s, "xml_element")
    }
    members = {}
    for slot in keys.values():
        choice = _xml_name(slot, "xml_choice")
        for xml in choice.split() if choice else ():
            elements.add(xml)
            members[xml] = slot
    assert set(attributes) == set(xsd_attributes) - {None}
    for xml, (required, _) in xsd_attributes.items():
        assert bool(attributes[xml].get("required")) == required, xml
    if cls.get("mixin"):
        return
    assert elements == set(xsd_elements)
    by_element = {_xml_name(s, "xml_element"): s for s in keys.values()}
    for xml, (required, repeats) in xsd_elements.items():
        if xml in members:
            # The list of members carries the choice's occurrence; each member class
            # holds one element, optional and single.
            assert repeats and not required, xml
            inner = keys_of(members[xml]["range"])
            held = next(s for s in inner.values() if _xml_name(s, "xml_element") == xml)
            assert not held.get("required") and not held.get("multivalued"), xml
            continue
        slot = by_element[xml]
        assert bool(slot.get("required")) == required, xml
        assert bool(slot.get("multivalued")) == repeats, xml


def _enumeration(suffix, kind, type_name):
    node = xsd_types(suffix, kind).get(f"simple:{type_name.split(':')[-1]}")
    if node is None:
        return None
    union = node.find(f"{XS}union")
    if union is not None:
        # A list joined with any string is open, so its enum is a recommendation; a list
        # joined with numbers, such as unbounded, is a pattern instead.
        types = union.get("memberTypes").split()
        if {t for t in types if t.startswith("xs:")} - {"xs:string", "xs:token"}:
            return None
        members = [m for m in types if not m.startswith("xs:")]
        return _enumeration(suffix, kind, members[0]) if len(members) == 1 else None
    values = [e.get("value") for e in node.iter(f"{XS}enumeration")]
    return values or None


@pytest.mark.parametrize("name", [n for n, _ in CASES])
def test_each_value_list_is_the_xsds(name):
    """An attribute whose XSD type lists its values ranges over an enum with the same
    values, in the same order."""
    suffix, kind = _edition(name)
    cls = classes()[name]
    node = xsd_types(suffix, kind)[cls["annotations"]["xsd_type"]]
    xsd_attributes, _ = _xsd_parts(suffix, kind, node)
    keys = keys_of(name) if not cls.get("mixin") else cls.get("attributes") or {}
    for slot in keys.values():
        xml = _xml_name(slot, "xml_attribute")
        if xml not in xsd_attributes or xsd_attributes[xml][1] is None:
            continue
        values = _enumeration(suffix, kind, xsd_attributes[xml][1])
        if values is None:
            continue
        ranges = [slot.get("range")] + [p["range"] for p in slot.get("any_of") or []]
        enum = next(r for r in ranges if r in enums())
        assert list(enums()[enum]["permissible_values"]) == values, (xml, enum)


def test_every_complex_type_has_a_class():
    """No complex type, attribute group in use or anonymous element type of either
    edition is without a class."""
    rendered = {
        (_edition(n), cls["annotations"]["xsd_type"])
        for n, cls in classes().items()
        if (cls.get("annotations") or {}).get("xml_namespace")
    }
    for suffix in conversion.EDITION_FOLDERS:
        for kind in KINDS:
            for name, node in xsd_types(suffix, kind).items():
                if name.startswith("simple:") or name in ("messageAttribGrp",):
                    continue
                if node.tag == f"{XS}complexType" or node.tag == f"{XS}attributeGroup":
                    assert ((suffix, kind), name) in rendered, (suffix, kind, name)


# The XML walk


def _count_xml(element, elements: Counter, attributes: Counter) -> None:
    elements[element.tag.split("}")[-1]] += 1
    for name, value in element.attrib.items():
        if not name.startswith(XSI):
            attributes[(name.split("}")[-1], value)] += 1
    for child in element:
        _count_xml(child, elements, attributes)


def _count_record(record, name, elements: Counter, attributes: Counter) -> None:
    """Counts what a record holds, through the schema's annotations alone."""
    if name == "OrchestraXmlElement":
        elements[record["xml_name"].split("}")[-1]] += 1
        for attribute in record.get("xml_attributes") or []:
            attributes[
                (attribute["xml_name"].split("}")[-1], attribute["xml_value"])
            ] += 1
        for child in record.get("xml_children") or []:
            _count_record(child, "OrchestraXmlElement", elements, attributes)
        return
    keys = keys_of(name)
    for key, value in record.items():
        slot = keys[key]
        notes = slot.get("annotations") or {}
        items = value if isinstance(value, list) else [value]
        if "xml_attribute" in notes:
            attributes[(notes["xml_attribute"].split(":")[-1], _lexical(value))] += 1
        elif "xml_element" in notes:
            for item in items:
                elements[notes["xml_element"].split("}")[-1]] += 1
                if slot.get("range") in classes():
                    _count_record(item, slot["range"], elements, attributes)
        elif "xml_choice" in notes or notes.get("xml_any") == "elements":
            for item in items:
                _count_record(item, slot["range"], elements, attributes)
        elif notes.get("xml_any") == "attributes":
            for item in items:
                attributes[(item["xml_name"].split("}")[-1], item["xml_value"])] += 1
        elif not notes:
            # A member's one key: the element it holds.
            for item in items:
                elements[_member_element(name, key)] += 1
                if slot.get("range") in classes():
                    _count_record(item, slot["range"], elements, attributes)


def _member_element(name, key):
    return _xml_name(keys_of(name)[key], "xml_element")


def _lexical(value) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


@pytest.mark.parametrize("path", conversion.DOCUMENTS, ids=lambda p: p.name)
def test_the_records_hold_every_element_and_attribute(path):
    """The records hold each element and each attribute value of the document, as
    many times as the document does: the converter drops and invents nothing."""
    root = ET.parse(path).getroot()
    xml_elements, xml_attributes = Counter(), Counter()
    _count_xml(root, xml_elements, xml_attributes)
    name, record = conversion.record(path)
    record_elements, record_attributes = Counter(), Counter()
    record_elements[root.tag.split("}")[-1]] += 1
    _count_record(record, name, record_elements, record_attributes)
    assert record_elements == xml_elements
    assert record_attributes == xml_attributes
