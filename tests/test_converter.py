"""Checks the two scripts that stand between the XSDs, the schema and an Orchestra file."""

import pytest
from lxml import etree

from tests import conversion

V10 = "http://fixprotocol.io/2020/orchestra/repository"


def test_the_modules_are_the_converters_output():
    """An edit to the words or the XSD rules without a run of the converter fails here."""
    assert conversion.XSD_CONVERTER.main(["--check"]) == 0


def test_every_key_is_its_xml_name_in_snake_case():
    """The key of each attribute and element is the file's prefix and its XML name in
    snake case, so a reader can find one from the other."""
    for name, cls in conversion.CONVERTER._classes().items():
        for key, slot in (cls.get("attributes") or {}).items():
            notes = slot.get("annotations") or {}
            xml = notes.get("xml_attribute") or notes.get("xml_element")
            if xml is None or name == "OrchestraMetadata":
                continue
            prefix = "fixi" if cls.get("in_subset") == ["fixi"] else "fixr"
            expected = (
                "xml_base"
                if xml == "xml:base"
                else f"{prefix}_{conversion.XSD_CONVERTER.snake(xml)}"
            )
            assert key == expected, (name, key, xml)


def _repository(body: str) -> bytes:
    return f"""<fixr:repository xmlns:fixr="{V10}" xmlns:dcterms="http://purl.org/dc/terms/"
        name="R" version="1.0"><fixr:metadata/>{body}</fixr:repository>""".encode()


@pytest.mark.parametrize(
    "body, message",
    [
        ('<fixr:datatypes colour="blue"/>', "no key for the attribute colour"),
        ("<fixr:unknown/>", "no key for the element"),
    ],
)
def test_an_unknown_name_stops_the_converter(body, message):
    """Nothing in a file is dropped silently: a name the schema has no key for is an
    error."""
    with pytest.raises(ValueError, match=message):
        conversion.CONVERTER.to_record(
            etree.fromstring(_repository(body)), "OrchestraRepositoryV10"
        )


def test_a_parser_hint_is_left_out():
    """xsi:schemaLocation tells a parser where an XSD is; it is not the file's content."""
    xml = _repository("").replace(
        b'name="R"',
        b'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" '
        b'xsi:schemaLocation="x y" name="R"',
    )
    record = conversion.CONVERTER.to_record(
        etree.fromstring(xml), "OrchestraRepositoryV10"
    )
    assert set(record) == {"fixr_name", "fixr_version", "fixr_metadata"}


def test_an_entity_is_not_expanded():
    """The parser expands no entity and reads no network resource."""
    xml = b'<!DOCTYPE r [<!ENTITY e SYSTEM "file:///etc/passwd">]>' + _repository(
        "<fixr:annotation><fixr:documentation>&e;</fixr:documentation></fixr:annotation>"
    )
    root = etree.fromstring(xml, conversion.CONVERTER.PARSER)
    assert "root:" not in etree.tostring(root).decode()
