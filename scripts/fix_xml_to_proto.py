#!/usr/bin/env python3
"""Generate a wire-format proto3 file from a FIX Orchestra XML repository.

Reads a FIX Orchestra XML file (e.g. OrchestraFIXLatest.xml) and emits
proto3 representing the actual FIX trading objects:

* One proto ``enum``    per FIX code set (AdvSideCodeSet, …)
* One proto ``message`` per FIX component (CommissionData, Instrument, …)
* One proto ``message`` per FIX group     (NoAllocs, NoLegs, …)
* One proto ``message`` per FIX message   (NewOrderSingle, Heartbeat, …)

This is categorically different from the *metamodel* proto that LinkML's
``gen-proto`` emits: that tool models the schema types (FieldType, MessageType)
as proto messages and is currently broken (all fields = 0, blank package).
This script models the FIX trading *instances* — the artefact useful for
financial systems exchanging FIX messages over a protobuf wire.

Reference implementation:
  upstream-releases/fix-orchestra-protobuf/src/main/java/
  io/fixprotocol/orchestra2proto/ProtobufModelFactory.java
  (commit a2e9edd, io.fixprotocol:orchestra2proto:0.0.1-SNAPSHOT)

Key design decisions (all match the Java reference):

* Proto field numbers are sequential (1..N) within each message; the FIX
  tag number travels as a ``(tag)`` custom option on each field.
* ``<numInGroup>`` elements are elided; the group itself becomes ``repeated``
  when referenced from a parent message/component.
* Enum field numbers are sequential (1..N) after sorting by ``code/@sort``;
  a synthetic ``<PREFIX>_UNSPECIFIED = 0`` zero-value is prepended (required
  by proto3).
* FIX datatypes are mapped to proto scalars or to supporting messages
  (Decimal64, Timestamp, TimeOnly, Tenor) via ``_FIX_TO_PROTO``.

Usage::

    python3 scripts/fix_xml_to_proto.py \\
        --input  tests/data/third_party/orchestrations/OrchestraFIXLatest.xml \\
        --output project/protobuf/fix_orchestra.wire.proto

Only the Python standard library is required.
"""
from __future__ import annotations

import argparse
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

# ---------------------------------------------------------------------------
# XML namespace
# ---------------------------------------------------------------------------

_REPO_NS = "http://fixprotocol.io/2020/orchestra/repository"
_R = "{" + _REPO_NS + "}"

# ---------------------------------------------------------------------------
# FIX base datatype -> proto scalar (or supporting message name)
# Derived from ProtobufModelFactory.java#buildField (FieldRefType).
# ---------------------------------------------------------------------------

_FIX_TO_PROTO: dict[str, str] = {
    "int":                 "fixed32",
    "Length":              "fixed32",
    "TagNum":              "fixed32",
    "SeqNum":              "fixed32",
    "DayOfMonth":          "fixed32",
    "NumInGroup":          "fixed32",   # elided as group header, mapped if used directly
    "float":               "double",
    "Qty":                 "Decimal64",
    "Price":               "Decimal64",
    "PriceOffset":         "Decimal64",
    "Amt":                 "Decimal64",
    "Percentage":          "double",
    "char":                "string",
    "Boolean":             "bool",
    "String":              "string",
    "MultipleCharValue":   "string",
    "MultipleStringValue": "string",
    "Country":             "string",
    "Currency":            "string",
    "Exchange":            "string",
    "MonthYear":           "string",
    "UTCTimestamp":        "Timestamp",
    "UTCTimeOnly":         "TimeOnly",
    "UTCDateOnly":         "string",
    "LocalMktDate":        "string",
    "TZTimeOnly":          "TimeOnly",
    "TZTimestamp":         "Timestamp",
    "data":                "bytes",
    "Pattern":             "string",
    "Tenor":               "Tenor",
    "Reserved100Plus":     "fixed32",
    "Reserved1000Plus":    "fixed32",
    "Reserved4000Plus":    "fixed32",
    "XMLData":             "string",
    "Language":            "string",
    "LocalMktTime":        "TimeOnly",
    "XID":                 "string",
    "XIDREF":              "string",
}

# Supporting message names emitted verbatim at the top of the proto file.
_SUPPORTING_MSG_NAMES: frozenset[str] = frozenset({
    "Decimal32", "Decimal64",
    "Timestamp", "TimeOnly", "LocalTimestamp", "LocalTimeOnly",
    "Tenor",
})

_SUPPORTING_MESSAGES = """\
// ---------------------------------------------------------------------------
// Supporting messages (equivalent to the Java reference tool's supporting types)
// ---------------------------------------------------------------------------

message Decimal32 {
  sint32 mantissa = 1;
  sint32 exponent = 2;
}

message Decimal64 {
  sint64 mantissa = 1;
  sint32 exponent = 2;
}

message Timestamp {
  uint64 time_ns   = 1;
  uint32 time_unit = 2;
}

message TimeOnly {
  uint64 time_ns   = 1;
  uint32 time_unit = 2;
}

message LocalTimestamp {
  uint64 time_ns   = 1;
  uint32 time_unit = 2;
}

message LocalTimeOnly {
  uint64 time_ns   = 1;
  uint32 time_unit = 2;
}

message Tenor {
  string value = 1;
}"""

# ---------------------------------------------------------------------------
# Name helpers
# ---------------------------------------------------------------------------


def _camel_to_snake(name: str) -> str:
    """Convert a PascalCase / camelCase identifier to snake_case."""
    s = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", name)
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s)
    return s.lower()


def _to_enum_prefix(codeset_name: str) -> str:
    """``'AdvSideCodeSet'`` -> ``'ADV_SIDE'`` (UPPER_SNAKE without CodeSet suffix)."""
    base = (
        codeset_name[: -len("CodeSet")]
        if codeset_name.endswith("CodeSet")
        else codeset_name
    )
    return _camel_to_snake(base).upper()


def _to_enum_value_name(codeset_name: str, code_name: str) -> str:
    """``('AdvSideCodeSet', 'Buy')`` -> ``'ADV_SIDE_BUY'``."""
    prefix = _to_enum_prefix(codeset_name)
    sanitized = re.sub(r"[^A-Za-z0-9]+", "_", code_name).strip("_").upper()
    return f"{prefix}_{sanitized}"


def _field_name(name: str) -> str:
    """Convert a FIX entity name to a proto field name (snake_case)."""
    return _camel_to_snake(name)


# ---------------------------------------------------------------------------
# Generator
# ---------------------------------------------------------------------------


class ProtoGenerator:
    """Converts a FIX Orchestra XML repository into a wire-format proto3 file."""

    def __init__(self, xml_path: Path, package: str) -> None:
        self._path = xml_path
        self._package = package
        self._lines: list[str] = []

    # -- output --

    def _emit(self, line: str = "") -> None:
        self._lines.append(line)

    def _result(self) -> str:
        return "\n".join(self._lines) + "\n"

    # -- type resolution --

    def _resolve_type(self, fix_type: str) -> str:
        """Return the proto type string for a FIX datatype name."""
        if fix_type in self._codeset_names:
            return fix_type  # inline enum type
        return _FIX_TO_PROTO.get(fix_type, "string")

    # -- public entry point --

    def generate(self) -> str:
        tree = ET.parse(self._path)
        root = tree.getroot()

        # Build lookup tables used during message emission.
        self._fields: dict[str, dict[str, str]] = {}
        for f in root.findall(f"{_R}fields/{_R}field"):
            self._fields[f.attrib["id"]] = {
                "name": f.attrib["name"],
                "type": f.attrib.get("type", "String"),
            }

        self._components: dict[str, str] = {}  # id -> name
        for c in root.findall(f"{_R}components/{_R}component"):
            self._components[c.attrib["id"]] = c.attrib["name"]

        self._groups: dict[str, dict[str, str | None]] = {}  # id -> {name, ni_id}
        for g in root.findall(f"{_R}groups/{_R}group"):
            ni = g.find(f"{_R}numInGroup")
            self._groups[g.attrib["id"]] = {
                "name": g.attrib["name"],
                "ni_id": ni.attrib.get("id") if ni is not None else None,
            }

        self._codeset_names: set[str] = {
            cs.attrib["name"]
            for cs in root.findall(f"{_R}codeSets/{_R}codeSet")
        }

        # Emit in logical order.
        self._emit_header()
        self._emit(self._SUPPORTING_MESSAGES)
        self._emit()
        for cs in root.findall(f"{_R}codeSets/{_R}codeSet"):
            self._emit_enum(cs)
        for comp in root.findall(f"{_R}components/{_R}component"):
            self._emit_message(comp.attrib["name"], comp)
        for grp in root.findall(f"{_R}groups/{_R}group"):
            self._emit_message(grp.attrib["name"], grp)
        for msg in root.findall(f"{_R}messages/{_R}message"):
            structure = msg.find(f"{_R}structure")
            self._emit_message(
                msg.attrib["name"],
                structure,
                msg_type=msg.attrib.get("msgType"),
            )

        return self._result()

    # -- section emitters --

    def _emit_header(self) -> None:
        self._emit('syntax = "proto3";')
        self._emit()
        self._emit(f"package {self._package};")
        self._emit()
        self._emit('import "google/protobuf/descriptor.proto";')
        self._emit()
        self._emit("// FIX custom option extensions")
        self._emit("// Field option: carries the FIX tag number.")
        self._emit("extend google.protobuf.FieldOptions {")
        self._emit("  fixed32 tag = 50001;")
        self._emit("}")
        self._emit()
        self._emit("// Message option: carries the FIX MsgType value (e.g. 'D' for NewOrderSingle).")
        self._emit("extend google.protobuf.MessageOptions {")
        self._emit("  string msg_type_value = 52001;")
        self._emit("}")
        self._emit()
        self._emit("// Enum value option: carries the FIX wire-value string (e.g. 'B' for Buy).")
        self._emit("extend google.protobuf.EnumValueOptions {")
        self._emit("  string enum_value = 51004;")
        self._emit("}")
        self._emit()

    def _emit_enum(self, cs_elem: ET.Element) -> None:
        cs_name = cs_elem.attrib["name"]
        prefix = _to_enum_prefix(cs_name)

        self._emit(f"enum {cs_name} {{")

        # Collect all code entries and sort by @sort.
        codes: list[tuple[int, dict[str, str]]] = []
        for code in cs_elem.findall(f"{_R}code"):
            raw = code.attrib.get("sort", "").strip()
            try:
                sort = int(raw)
            except (ValueError, TypeError):
                sort = 0
            codes.append((sort, dict(code.attrib)))
        codes.sort(key=lambda x: x[0])

        # Proto3 mandates a zero-valued first entry.
        self._emit(f"  {prefix}_UNSPECIFIED = 0;")

        for i, (_sort, attrs) in enumerate(codes, 1):
            val_name = _to_enum_value_name(cs_name, attrs["name"])
            # Guard against collision with the UNSPECIFIED sentinel.
            if "_UNSPECIFIED" in val_name:
                val_name += "_VALUE"
            code_value = attrs.get("value", "")
            self._emit(f'  {val_name} = {i} [(enum_value) = "{code_value}"];')

        self._emit("}")
        self._emit()

    def _emit_message(
        self,
        name: str,
        struct_elem: ET.Element | None,
        *,
        msg_type: str | None = None,
    ) -> None:
        self._emit(f"message {name} {{")
        if msg_type:
            self._emit(f'  option (msg_type_value) = "{msg_type}";')

        field_num = 1
        for child in (list(struct_elem) if struct_elem is not None else []):
            local = child.tag.split("}", 1)[1] if "}" in child.tag else child.tag

            if local in ("annotation", "numInGroup"):
                # numInGroup is elided: the group becomes `repeated` on the parent.
                continue

            if local == "fieldRef":
                fid = child.attrib.get("id", "")
                fi = self._fields.get(fid)
                if fi is None:
                    continue
                fname = _field_name(fi["name"])
                ptype = self._resolve_type(fi["type"])
                self._emit(f"  {ptype} {fname} = {field_num} [(tag) = {fid}];")
                field_num += 1

            elif local == "componentRef":
                cid = child.attrib.get("id", "")
                cname = self._components.get(cid)
                if cname is None:
                    continue
                fname = _field_name(cname)
                self._emit(f"  {cname} {fname} = {field_num};")
                field_num += 1

            elif local == "groupRef":
                gid = child.attrib.get("id", "")
                ginfo = self._groups.get(gid)
                if ginfo is None:
                    continue
                gname = ginfo["name"]
                fname = _field_name(gname)
                ni_id = ginfo["ni_id"]
                if ni_id:
                    self._emit(
                        f"  repeated {gname} {fname} = {field_num} [(tag) = {ni_id}];"
                    )
                else:
                    self._emit(f"  repeated {gname} {fname} = {field_num};")
                field_num += 1

        self._emit("}")
        self._emit()

    # Module-level constant referenced via class scope.
    _SUPPORTING_MESSAGES = _SUPPORTING_MESSAGES


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Generate wire-format proto3 from a FIX Orchestra XML repository.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 scripts/fix_xml_to_proto.py \\
      --input  tests/data/third_party/orchestrations/OrchestraFIXLatest.xml \\
      --output project/protobuf/fix_orchestra.wire.proto

  python3 scripts/fix_xml_to_proto.py \\
      --input  tests/data/third_party/orchestrations/OrchestraFIXLatest.xml \\
      --package fix_latest > /tmp/fix_latest.proto
""",
    )
    ap.add_argument(
        "--input", "-i", required=True, type=Path, metavar="XML",
        help="FIX Orchestra XML repository file",
    )
    ap.add_argument(
        "--output", "-o", type=Path, metavar="PROTO",
        help="Output .proto file path (default: stdout)",
    )
    ap.add_argument(
        "--package", default="fix", metavar="NAME",
        help="Proto package name (default: fix)",
    )
    args = ap.parse_args()

    if not args.input.exists():
        print(f"error: input file not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    proto = ProtoGenerator(args.input, args.package).generate()

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(proto, encoding="utf-8")
        size = args.output.stat().st_size
        print(f"Written {size:,} bytes -> {args.output}", file=sys.stderr)
    else:
        sys.stdout.write(proto)


if __name__ == "__main__":
    main()
