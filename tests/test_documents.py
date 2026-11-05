"""Checks the schema against whole Orchestra files, each read two independent ways.

Each document is a real file pinned under upstream/documents/, or an example this project
wrote under tests/data/xml/ so that every class has an instance. Each is valid against its
edition's XSD, which lxml checks. The converter then turns it into records that the
committed JSON Schema must accept, the rules in tests/orchestra_rules.py must accept but
for the departures listed, and the converter must turn back into the same XML.
"""

from pathlib import Path

import pytest
import yaml
from lxml import etree

from tests import conversion
from tests.orchestra_rules import rule_errors

XSI = "http://www.w3.org/2001/XMLSchema-instance"
DEPARTURES = yaml.safe_load(
    (Path(__file__).parent / "document_departures.yaml").read_text(encoding="utf-8")
)
IDS = [path.name for path in conversion.DOCUMENTS]


@pytest.mark.parametrize("path", conversion.DOCUMENTS, ids=IDS)
def test_each_document_is_valid_against_its_xsd(path):
    """The pinned XSD accepts the document, so the tests below start from valid files."""
    schema = conversion.xsd(*conversion.edition_of(path))
    document = etree.parse(str(path), conversion.CONVERTER.PARSER)
    assert schema.validate(document), [e.message for e in schema.error_log][:5]


@pytest.mark.parametrize("path", conversion.DOCUMENTS, ids=IDS)
def test_each_document_converts_to_valid_records(path):
    """The records of a valid document pass the committed JSON Schema."""
    name, record = conversion.record(path)
    found = conversion.schema_errors(record, name)
    assert not found, [f"{conversion.pointer(e)}: {e.message[:200]}" for e in found][:5]


@pytest.mark.parametrize("path", conversion.DOCUMENTS, ids=IDS)
def test_each_document_keeps_the_rules(path):
    """A document breaks no rule but the departures tests/document_departures.yaml
    lists, each a fault in the upstream's own file."""
    name, record = conversion.record(path)
    found = sorted(p for p, _ in rule_errors(name, record))
    assert found == sorted(DEPARTURES.get(path.name) or [])


def _canonical(element, ordered=True):
    """An element's name, attributes, text and children, with the whitespace between
    elements and the hints for a parser left out. The repository's children may come in
    any order, and so may a metadata block's, so those are sorted."""
    q = etree.QName(element)
    attributes = sorted(
        (k, v) for k, v in element.attrib.items() if not k.startswith(f"{{{XSI}}}")
    )
    children = [_canonical(c) for c in element if isinstance(c.tag, str)]
    if q.localname in ("repository", "metadata"):
        children.sort(key=lambda c: c[0])
    text = (element.text or "").strip()
    tail = (element.tail or "").strip()
    return (element.tag, attributes, text, tail, children)


@pytest.mark.parametrize("path", conversion.DOCUMENTS, ids=IDS)
def test_each_document_converts_back_unchanged(path):
    """Records to XML gives the document back: every attribute, element, text and
    order of elements survives the trip, which proves the keys map one to one."""
    name, record = conversion.record(path)
    original = etree.parse(str(path), conversion.CONVERTER.PARSER).getroot()
    original.tail = None
    back = etree.fromstring(conversion.CONVERTER.write(name, record))
    assert _canonical(back) == _canonical(original)


def test_the_records_are_the_xml_text():
    """FIX Latest's records hold the attribute values as the XML gives them: a message's
    type code, a field's tag number and an extension pack, spot-checked."""
    _, record = conversion.record(conversion.FIX_LATEST)
    messages = record["fixr_messages"]["fixr_message"]
    order = next(m for m in messages if m["fixr_name"] == "NewOrderSingle")
    assert order["fixr_msg_type"] == "D"
    fields = record["fixr_fields"]["fixr_field"]
    side = next(f for f in fields if f["fixr_id"] == 54)
    assert side["fixr_name"] == "Side"
    assert record["fixr_version"] == "FIX.Latest_EP312"


def test_a_v10_category_may_have_no_section():
    """FIX Latest is a v1.0 file, and v1.0 makes a category's section optional. Three of
    its categories have none, and both the XSD and the schema accept that; RC3 makes the
    section required."""
    _, record = conversion.record(conversion.FIX_LATEST)
    without = [
        c["fixr_name"]
        for c in record["fixr_categories"]["fixr_category"]
        if "fixr_section" not in c
    ]
    assert without == ["Common", "Fields", "ImplFields"]


def _rc3_repository(fields: str) -> bytes:
    return f"""<fixr:repository xmlns:fixr="http://fixprotocol.io/2026/orchestra/repository"
        xmlns:dcterms="http://purl.org/dc/terms/" name="Two" version="1">
      <fixr:metadata><dcterms:title>Two</dcterms:title></fixr:metadata>
      <fixr:datatypes><fixr:datatype name="String"/></fixr:datatypes>
      <fixr:fields>{fields}</fixr:fields>
    </fixr:repository>""".encode()


def test_rc3_refuses_two_fields_of_one_datatype_and_the_schema_does_not():
    """RC3's fieldTypeOrCodeSetKey is a key, so the XSD refuses a second field of the
    same datatype, which every real repository has. The schema and the rules keep what
    the key asks of one field and accept the pair. issues/93 reports the fault."""
    one = '<fixr:field id="1" name="A" type="String"/>'
    two = one + '<fixr:field id="2" name="B" type="String"/>'
    schema = conversion.xsd("V11", "repository")
    assert schema.validate(etree.fromstring(_rc3_repository(one)))
    assert not schema.validate(etree.fromstring(_rc3_repository(two)))
    assert "fieldTypeOrCodeSetKey" in str(schema.error_log)
    record = conversion.CONVERTER.to_record(
        etree.fromstring(_rc3_repository(two)), "OrchestraRepositoryV11"
    )
    assert not conversion.schema_errors(record, "OrchestraRepositoryV11")
    assert not rule_errors("OrchestraRepositoryV11", record)


def _rc3_from_fix_latest():
    """FIX Latest moved to RC3's shape by what RC3 changed: its namespace, the v1.0
    attributes RC3 drops, and a code set named in `codeSet` rather than `type`. The
    three categories that name no section, which RC3 requires, are left out."""
    v10 = "http://fixprotocol.io/2020/orchestra/repository"
    v11 = "http://fixprotocol.io/2026/orchestra/repository"
    root = etree.parse(
        str(conversion.FIX_LATEST), conversion.CONVERTER.PARSER
    ).getroot()
    code_sets = {c.get("name") for c in root.iter(f"{{{v10}}}codeSet")}
    for category in list(root.iter(f"{{{v10}}}category")):
        if category.get("section") is None:
            category.getparent().remove(category)
    dropped = {
        "category": ("FIXMLFileName", "componentType", "includeFile"),
        "section": ("FIXMLFileName",),
        "repository": ("latestEP", "applVerId"),
    }
    for element in root.iter():
        if not isinstance(element.tag, str):
            continue
        q = etree.QName(element)
        for attribute in dropped.get(q.localname, ()):
            element.attrib.pop(attribute, None)
        if q.localname.endswith("s") and q.namespace == v10:
            element.attrib.pop("latestEP", None)
        if q.localname == "field" and element.get("type") in code_sets:
            element.set("codeSet", element.attrib.pop("type"))
        if q.namespace == v10:
            element.tag = f"{{{v11}}}{q.localname}"
    etree.cleanup_namespaces(root, top_nsmap={"fixr": v11})
    return etree.fromstring(etree.tostring(root))


def test_rc3_and_the_schema_agree_on_fix_latest_moved_to_rc3():
    """With the faulty key left out, RC3's XSD and the schema's v1.1 module judge FIX
    Latest in RC3's shape alike: both refuse only the one group name longer than RC3's
    64 characters, which issues/93 reports."""
    tree = conversion.xsd_tree("V11", "repository")
    for key in tree.getroot().iter("{http://www.w3.org/2001/XMLSchema}key"):
        if key.get("name") == "fieldTypeOrCodeSetKey":
            key.getparent().remove(key)
    schema = etree.XMLSchema(tree)
    document = _rc3_from_fix_latest()
    schema.validate(document)
    lengths = [e for e in schema.error_log if "maximum length" in e.message]
    others = [
        e.message
        for e in schema.error_log
        if "maximum length" not in e.message
        and "precomputed" not in e.message
        and "evaluate to a node" not in e.message
    ]
    assert len(lengths) == 1 and not others, others[:5]
    long_name = "UnderlyingPaymentStreamNonDeliverableFixingDatesBusinessCenterGrp"
    assert long_name in lengths[0].message
    record = conversion.CONVERTER.to_record(document, "OrchestraRepositoryV11")
    found = conversion.schema_errors(record, "OrchestraRepositoryV11")
    reached = set().union(*(conversion.places(e) for e in found))
    index = _group_index(record, long_name)
    assert reached == {f"/fixr_groups/fixr_group/{index}/fixr_name"}


def _group_index(record, name):
    groups = record["fixr_groups"]["fixr_group"]
    return next(i for i, g in enumerate(groups) if g["fixr_name"] == name)
