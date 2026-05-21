"""Tests for scripts/fix_xml_to_proto.py — wire-format proto3 generator.

Exercises the ProtoGenerator class directly (import via sys.path) and also
verifies the generated project/protobuf/fix_orchestra.wire.proto that is committed to
the repository.  Both paths parse OrchestraFIXLatest.xml.

Structural invariants checked
------------------------------
* Package declaration is present and non-empty.
* No proto field number 0 outside of enum zero-value sentinels.
* ``NewOrderSingle`` message is present with ``msg_type_value = "D"`` option.
* ``AdvSideCodeSet`` enum is present with the expected Buy/Sell values.
* Custom ``(tag)`` options appear on field declarations.
* Supporting messages (Decimal64, Timestamp, Tenor) are declared.
* No duplicate message or enum names.
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

import pytest

PROJECT = Path(__file__).parent.parent
SCRIPT = PROJECT / "scripts" / "fix_xml_to_proto.py"
XML_LATEST = (
    PROJECT
    / "tests"
    / "data"
    / "third_party"
    / "orchestrations"
    / "OrchestraFIXLatest.xml"
)
COMMITTED_PROTO = PROJECT / "project" / "protobuf" / "fix_orchestra.wire.proto"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _run_generator(xml_path: Path, extra_args: list[str] | None = None) -> str:
    """Run fix_xml_to_proto.py as a subprocess; return stdout."""
    cmd = [sys.executable, str(SCRIPT), "--input", str(xml_path)]
    if extra_args:
        cmd.extend(extra_args)
    result = subprocess.run(cmd, capture_output=True, text=True)
    assert result.returncode == 0, f"Script failed:\n{result.stderr}"
    return result.stdout


def _field_zero_lines(proto_text: str) -> list[str]:
    """Return lines that have a field declaration with field number 0.

    Proto3 forbids field number 0 except as the mandatory enum zero value
    (``ENUM_NAME_UNSPECIFIED = 0;``), which is intentional here.
    """
    bad = []
    for line in proto_text.splitlines():
        stripped = line.strip()
        # Skip enum zero-value sentinels (_UNSPECIFIED = 0;)
        if re.search(r"_UNSPECIFIED\s*=\s*0\s*;", stripped):
            continue
        # Flag any other field declaration ending with = 0
        if re.search(r"\s=\s0\s*[;\[]", stripped):
            bad.append(line)
    return bad


# ---------------------------------------------------------------------------
# Tests against the generated output (running the script live)
# ---------------------------------------------------------------------------


@pytest.fixture(scope="module")
def proto_text() -> str:
    """Generate proto once per test module from OrchestraFIXLatest.xml."""
    pytest.importorskip("xml.etree.ElementTree")  # always present; docs guard
    return _run_generator(XML_LATEST)


def test_syntax_line(proto_text: str) -> None:
    assert 'syntax = "proto3";' in proto_text


def test_package_declaration(proto_text: str) -> None:
    """Package line must have an identifier — not just a bare `package;`."""
    match = re.search(r"^package\s+(\w+)\s*;", proto_text, re.MULTILINE)
    assert match is not None, "No valid package declaration found"
    assert match.group(1), "Package identifier is empty"


def test_no_field_number_zero(proto_text: str) -> None:
    """No non-enum field may have field number 0 (proto3 forbids it)."""
    bad = _field_zero_lines(proto_text)
    assert bad == [], (
        f"Found {len(bad)} field(s) with illegal field number 0:\n"
        + "\n".join(bad[:10])
    )


def test_new_order_single_present(proto_text: str) -> None:
    assert "message NewOrderSingle {" in proto_text


def test_new_order_single_msg_type(proto_text: str) -> None:
    """NewOrderSingle must carry option (msg_type_value) = \"D\"."""
    assert '(msg_type_value) = "D"' in proto_text


def test_adv_side_code_set_enum(proto_text: str) -> None:
    assert "enum AdvSideCodeSet {" in proto_text
    assert "ADV_SIDE_UNSPECIFIED = 0;" in proto_text
    assert '(enum_value) = "B"' in proto_text  # Buy
    assert '(enum_value) = "S"' in proto_text  # Sell


def test_tag_options_present(proto_text: str) -> None:
    """At least one field must carry a (tag) custom option."""
    assert "(tag) =" in proto_text


def test_supporting_messages_present(proto_text: str) -> None:
    for name in ("Decimal64", "Timestamp", "TimeOnly", "Tenor"):
        assert f"message {name} " in proto_text, f"Supporting message {name!r} missing"


def test_cl_ord_id_tag_11(proto_text: str) -> None:
    """ClOrdID is FIX tag 11; it must appear in NewOrderSingle with (tag) = 11."""
    # Find the NewOrderSingle block (between the opening brace and the next
    # top-level '}' that closes it).
    m = re.search(
        r"message NewOrderSingle \{(.+?)^\}",
        proto_text,
        re.MULTILINE | re.DOTALL,
    )
    assert m is not None, "NewOrderSingle block not found"
    body = m.group(1)
    assert "(tag) = 11" in body, "ClOrdID (tag 11) missing from NewOrderSingle"


def test_no_duplicate_message_names(proto_text: str) -> None:
    names = re.findall(r"^message (\w+) \{", proto_text, re.MULTILINE)
    seen: set[str] = set()
    duplicates = [n for n in names if n in seen or seen.add(n)]  # type: ignore[func-returns-value]
    assert duplicates == [], f"Duplicate message names: {duplicates}"


def test_no_duplicate_enum_names(proto_text: str) -> None:
    names = re.findall(r"^enum (\w+) \{", proto_text, re.MULTILINE)
    seen: set[str] = set()
    duplicates = [n for n in names if n in seen or seen.add(n)]  # type: ignore[func-returns-value]
    assert duplicates == [], f"Duplicate enum names: {duplicates}"


def test_component_message_present(proto_text: str) -> None:
    """CommissionData is a well-known FIX component; it must appear."""
    assert "message CommissionData {" in proto_text


def test_group_becomes_repeated(proto_text: str) -> None:
    """Groups referenced in a message must use `repeated` label."""
    assert "repeated " in proto_text


# ---------------------------------------------------------------------------
# Tests against the committed project/protobuf/fix_orchestra.wire.proto
# ---------------------------------------------------------------------------


@pytest.mark.skipif(
    not COMMITTED_PROTO.exists(),
    reason="project/protobuf/fix_orchestra.wire.proto not yet generated (run just gen-proto-wire)",
)
def test_committed_proto_is_valid() -> None:
    """The committed fix_orchestra.wire.proto must pass the same structural checks."""
    text = COMMITTED_PROTO.read_text(encoding="utf-8")
    assert 'syntax = "proto3";' in text
    assert "package fix;" in text
    bad = _field_zero_lines(text)
    assert bad == [], f"Committed proto has {len(bad)} field(s) with field number 0"
    assert "message NewOrderSingle {" in text
    assert '(msg_type_value) = "D"' in text


def test_custom_package_flag() -> None:
    """--package flag must appear in the emitted package declaration."""
    text = _run_generator(XML_LATEST, ["--package", "fix_latest_ep302"])
    assert "package fix_latest_ep302;" in text
