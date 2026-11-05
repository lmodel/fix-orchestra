"""Checks the two scripts that stand between the XSDs, the schema and an Orchestra file."""

import subprocess
import sys
from pathlib import Path

import pytest
import yaml
from lxml import etree

from tests import conversion
from tests.test_documents import _canonical

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


def _run(*args, cwd=conversion.ROOT):
    """A command as docs/index.md gives it, run from the repository with this Python."""
    exe = Path(sys.executable).with_name(args[0])
    return subprocess.run(
        [str(exe), *args[1:]], cwd=cwd, capture_output=True, text=True, check=False
    )


def test_the_documented_commands_validate_and_round_trip_a_pinned_file(tmp_path):
    """The three commands docs/index.md shows: the converter writes a file's records
    bare, linkml-validate accepts them as the file's class, and --to-xml writes the file
    back with no class named, since the record's keys name it."""
    script = str(conversion.SCRIPTS / "orchestra_xml_to_yaml.py")
    source = str(conversion.UPSTREAM / "documents" / "FIXTSession.xml")
    records, back = tmp_path / "fixt.yaml", tmp_path / "fixt.xml"
    assert _run("python", script, source, "-o", str(records)).returncode == 0
    assert records.read_text(encoding="utf-8").startswith("fixr_name: FIXT\n")
    checked = _run(
        "linkml-validate",
        "-s",
        str(conversion.SCHEMA),
        "-C",
        "OrchestraRepositoryV10",
        str(records),
    )
    assert checked.returncode == 0, checked.stdout + checked.stderr
    assert (
        _run("python", script, "--to-xml", str(records), "-o", str(back)).returncode
        == 0
    )
    original = etree.parse(source, conversion.CONVERTER.PARSER).getroot()
    original.tail = None
    assert _canonical(etree.parse(str(back)).getroot()) == _canonical(original)


def test_a_record_that_fits_both_editions_needs_its_class_named(tmp_path):
    """A record with no edition-specific key fits both editions, so --to-xml asks for
    --class and takes it."""
    _, record = conversion.record(
        conversion.UPSTREAM / "documents" / "SampleInterfaces.xml"
    )
    with pytest.raises(
        ValueError, match="OrchestraInterfacesV10, OrchestraInterfacesV11"
    ):
        conversion.CONVERTER.class_of(record)
    name = conversion.CONVERTER.class_of(conversion.record(conversion.FIX_LATEST)[1])
    assert name == "OrchestraRepositoryV10"
    assert (
        conversion.CONVERTER.main(
            [
                "--to-xml",
                "--class",
                "OrchestraInterfacesV10",
                "-o",
                str(tmp_path / "i.xml"),
                str(_write(tmp_path, record)),
            ]
        )
        == 0
    )


def _write(folder, record):
    path = folder / "record.yaml"
    path.write_text(yaml.safe_dump(record, sort_keys=False), encoding="utf-8")
    return path
