#!/usr/bin/env python3
"""Convert an Orchestra file to records that the schema validates, and records back to XML.

An Orchestra repository or interfaces file is XML. The schema keys each attribute and
element of the XSDs as ``fixr_`` or ``fixi_`` and the XML name in snake case, and keeps
the XML name in an ``xml_attribute`` or ``xml_element`` annotation. This script reads those
annotations from the schema's modules, so it holds no table of its own:

- to records: the root element's namespace picks the edition and the class, and each
  attribute, element and text becomes the key the class's annotations name. A repeated
  choice becomes a list of one-key members, so the order of a message's fields is kept;
- to XML: the same tables, read the other way, write the file back.

A name the class does not know is an error, so nothing is dropped silently. Attributes in
the XML Schema instance namespace, such as ``xsi:schemaLocation``, are hints to a parser and
are left out; so are comments and processing instructions. Usage::

    uv run python scripts/orchestra_xml_to_yaml.py FILE.xml [-o FILE.yaml]
    uv run python scripts/orchestra_xml_to_yaml.py --to-xml FILE.yaml [-o FILE.xml]
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass, field
from functools import cache
from pathlib import Path

import yaml
from lxml import etree

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_DIR = ROOT / "src" / "fix_orchestra" / "schema"
MODULES = ("fix_orchestra_common", "fix_orchestra_v1_0", "fix_orchestra_v1_1")
XSI = "http://www.w3.org/2001/XMLSchema-instance"
XML_NS = "http://www.w3.org/XML/1998/namespace"
DC = "http://purl.org/dc/elements/1.1/"
DCTERMS = "http://purl.org/dc/terms/"

# The class a file's root element becomes, by its namespace and name.
ROOTS = {
    (
        "http://fixprotocol.io/2020/orchestra/repository",
        "repository",
    ): "OrchestraRepositoryV10",
    (
        "http://fixprotocol.io/2020/orchestra/interfaces",
        "interfaces",
    ): "OrchestraInterfacesV10",
    (
        "http://fixprotocol.io/2026/orchestra/repository",
        "repository",
    ): "OrchestraRepositoryV11",
    (
        "http://fixprotocol.io/2026/orchestra/interfaces",
        "interfaces",
    ): "OrchestraInterfacesV11",
}

# A parser that reads no network resource and expands no entity.
PARSER = etree.XMLParser(
    no_network=True,
    resolve_entities=False,
    huge_tree=True,
    remove_comments=True,
    remove_pis=True,
)


@dataclass
class Table:
    """How one class's keys meet XML: in the order the XSD gives them."""

    name: str
    namespace: str | None
    order: list[str] = field(default_factory=list)
    attributes: dict[str, str] = field(default_factory=dict)  # XML name -> key
    elements: dict[str, str] = field(default_factory=dict)  # XML name -> key
    choices: dict[str, str] = field(default_factory=dict)  # XML name -> members key
    text: str | None = None
    any: str | None = None
    other_attributes: str | None = None
    slots: dict[str, dict] = field(default_factory=dict)  # key -> slot


@cache
def _classes() -> dict[str, dict]:
    classes = {}
    for module in MODULES:
        doc = yaml.safe_load(
            (SCHEMA_DIR / f"{module}.yaml").read_text(encoding="utf-8")
        )
        classes.update(doc.get("classes") or {})
    return classes


def _slots(name: str) -> dict[str, dict]:
    """A class's keys with its parents' and mixins' first, in their XSD order."""
    cls = _classes()[name]
    out: dict[str, dict] = {}
    if cls.get("is_a"):
        out |= _slots(cls["is_a"])
    for mixin in cls.get("mixins") or []:
        out |= _slots(mixin)
    out |= cls.get("attributes") or {}
    return out


@cache
def table(name: str) -> Table:
    cls = _classes()[name]
    out = Table(
        name=name, namespace=(cls.get("annotations") or {}).get("xml_namespace")
    )
    out.slots = _slots(name)
    for key, slot in out.slots.items():
        out.order.append(key)
        notes = slot.get("annotations") or {}
        if "xml_attribute" in notes:
            out.attributes[notes["xml_attribute"]] = key
        elif "xml_element" in notes:
            out.elements[notes["xml_element"]] = key
        elif "xml_choice" in notes:
            for xml in notes["xml_choice"].split():
                out.choices[xml] = key
        elif "xml_text" in notes:
            out.text = key
        elif notes.get("xml_any") == "elements":
            out.any = key
        elif notes.get("xml_any") == "attributes":
            out.other_attributes = key
    overlap = set(out.elements) & set(out.choices)
    if overlap:
        raise ValueError(f"{name}: {overlap} is both an element and a choice")
    return out


def _value(text: str, slot: dict):
    rng = slot.get("range")
    if rng == "integer":
        return int(text)
    if rng == "boolean":
        if text.strip() in ("true", "1"):
            return True
        if text.strip() in ("false", "0"):
            return False
        raise ValueError(f"{text!r} is not a boolean")
    return text


def _lexical(value) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def _clark(qname: etree.QName) -> str:
    return qname.text


def _open_element(element) -> dict:
    """An element the XSDs leave open, kept as written."""
    out: dict = {"xml_name": _clark(etree.QName(element))}
    if element.attrib:
        out["xml_attributes"] = [
            {"xml_name": name, "xml_value": value}
            for name, value in element.attrib.items()
        ]
    if element.text is not None:
        out["xml_text"] = element.text
    children = [c for c in element if isinstance(c.tag, str)]
    if children:
        out["xml_children"] = [_open_element(c) for c in children]
    if element.tail is not None and element.getparent() is not None:
        out["xml_tail"] = element.tail
    return out


def _metadata(element) -> dict:
    out: dict = {}
    keys = {
        notes["xml_element"]: key
        for key, slot in _slots("OrchestraMetadata").items()
        for notes in [slot.get("annotations") or {}]
    }
    for child in element:
        if not isinstance(child.tag, str):
            continue
        key = keys.get(child.tag)
        if key is None:
            raise ValueError(f"metadata: no key for {child.tag}")
        if child.attrib or len(child):
            raise ValueError(f"metadata: {child.tag} holds more than text")
        out.setdefault(key, []).append(child.text or "")
    return out


def to_record(element, name: str) -> dict:
    """The record of one element, as the class ``name`` keys it."""
    if name == "OrchestraMetadata":
        return _metadata(element)
    t = table(name)
    out: dict = {}
    for attr, value in element.attrib.items():
        if attr.startswith(f"{{{XSI}}}"):
            continue
        xml = "xml:base" if attr == f"{{{XML_NS}}}base" else attr
        key = t.attributes.get(xml)
        if key is None:
            if t.other_attributes:
                out.setdefault(t.other_attributes, []).append(
                    {"xml_name": attr, "xml_value": value}
                )
                continue
            raise ValueError(f"{name}: no key for the attribute {attr}")
        out[key] = _value(value, t.slots[key])
    if t.text is not None and element.text is not None:
        out[t.text] = element.text
    for child in element:
        if not isinstance(child.tag, str):
            continue
        q = etree.QName(child)
        if q.namespace == t.namespace and q.localname in t.elements:
            key = t.elements[q.localname]
            out_value = _child(child, t.slots[key])
        elif q.namespace == t.namespace and q.localname in t.choices:
            key = t.choices[q.localname]
            member = t.slots[key]["range"]
            mt = table(member)
            inner = mt.elements[q.localname]
            out.setdefault(key, []).append({inner: _child(child, mt.slots[inner])})
            continue
        elif t.any is not None:
            out.setdefault(t.any, []).append(_open_element(child))
            continue
        else:
            raise ValueError(f"{name}: no key for the element {child.tag}")
        if t.slots[key].get("multivalued"):
            out.setdefault(key, []).append(out_value)
        elif key in out:
            raise ValueError(f"{name}: {child.tag} appears twice")
        else:
            out[key] = out_value
    return out


def _child(child, slot: dict):
    rng = slot.get("range", "string")
    if rng == "OrchestraMetadata":
        return _metadata(child)
    if rng in _classes():
        return to_record(child, rng)
    if len(child):
        raise ValueError(f"{child.tag} should hold text only")
    return _value(child.text or "", slot)


def read(path: Path) -> tuple[str, dict]:
    """The class and record of an Orchestra file."""
    root = etree.parse(str(path), PARSER).getroot()
    q = etree.QName(root)
    name = ROOTS.get((q.namespace, q.localname))
    if name is None:
        raise ValueError(f"{path}: no class for a root {root.tag}")
    return name, to_record(root, name)


# Records to XML


def _prefix(namespace: str | None) -> str:
    if namespace and namespace.endswith("/interfaces"):
        return "fixi"
    return "fixr"


def to_element(record: dict, name: str, tag: str):
    """The element ``tag`` that a record of the class ``name`` gives."""
    t = table(name)
    element = etree.Element(tag, nsmap=_nsmap(t.namespace))
    _fill(element, record, name)
    return element


def _nsmap(namespace: str | None) -> dict:
    return {_prefix(namespace): namespace, "dcterms": DCTERMS, "dc": DC}


def _fill(element, record: dict, name: str) -> None:
    t = table(name)
    by_key = {v: k for k, v in t.attributes.items()}
    elements_by_key = {v: k for k, v in t.elements.items()}
    for key in t.order:
        if key not in record:
            continue
        value = record[key]
        if key in by_key:
            xml = by_key[key]
            attr = f"{{{XML_NS}}}base" if xml == "xml:base" else xml
            element.set(attr, _lexical(value))
        elif key in elements_by_key:
            xml = elements_by_key[key]
            for item in value if isinstance(value, list) else [value]:
                _append(element, t, key, xml, item)
        elif key == t.text:
            element.text = value
        elif key == t.any:
            for item in value:
                element.append(_from_open(item))
        elif key == t.other_attributes:
            for item in value:
                element.set(item["xml_name"], item["xml_value"])
        else:
            member = t.slots[key]["range"]
            mt = table(member)
            for item in value:
                ((inner, inner_value),) = item.items()
                xml = {v: k for k, v in mt.elements.items()}[inner]
                _append(element, mt, inner, xml, inner_value)


def _append(parent, t: Table, key: str, xml: str, value) -> None:
    slot = t.slots[key]
    rng = slot.get("range", "string")
    tag = f"{{{t.namespace}}}{xml}"
    if rng == "OrchestraMetadata":
        child = etree.SubElement(parent, tag)
        for mkey, values in value.items():
            mslot = _slots("OrchestraMetadata")[mkey]
            for text in values:
                etree.SubElement(child, mslot["annotations"]["xml_element"]).text = text
    elif rng in _classes():
        child = etree.SubElement(parent, tag)
        _fill(child, value, rng)
    else:
        etree.SubElement(parent, tag).text = _lexical(value)


def _from_open(item: dict):
    element = etree.Element(item["xml_name"])
    for attr in item.get("xml_attributes") or []:
        element.set(attr["xml_name"], attr["xml_value"])
    element.text = item.get("xml_text")
    for child in item.get("xml_children") or []:
        element.append(_from_open(child))
    element.tail = item.get("xml_tail")
    return element


def write(name: str, record: dict) -> bytes:
    """The XML of a file's record, with its root class."""
    ((namespace, local),) = [k for k, v in ROOTS.items() if v == name]
    root = to_element(record, name, f"{{{namespace}}}{local}")
    return etree.tostring(root, xml_declaration=True, encoding="UTF-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("path", type=Path)
    parser.add_argument("--to-xml", action="store_true", help="Read records, write XML")
    parser.add_argument("-o", "--output", type=Path)
    args = parser.parse_args(argv)
    if args.to_xml:
        doc = yaml.safe_load(args.path.read_text(encoding="utf-8"))
        name = next(iter(doc))
        data = write(name, doc[name])
    else:
        name, record = read(args.path)
        data = yaml.safe_dump(
            {name: record}, sort_keys=False, allow_unicode=True, width=100
        ).encode("utf-8")
    if args.output:
        args.output.write_bytes(data)
    else:
        sys.stdout.buffer.write(data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
