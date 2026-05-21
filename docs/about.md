# About fix-orchestra

FIX Orchestra - LinkML Schema and wire-format toolchain.

This project converts the FIX Orchestra XSD specification into a [LinkML](https://linkml.io/)
schema and generates a wire-format Protocol Buffers definition directly from the FIX Orchestra
XML repository.

## What is here

| Artefact | Path | Description |
|---|---|---|
| LinkML schema (FIX) | `src/fix_orchestra/schema/fix_orchestra.yaml` | 69 classes, 53 types (38 FIX base), 20 enums, 117 slots — generated from the upstream XSDs; imports the DC companion |
| LinkML schema (DC) | `src/fix_orchestra/schema/fix_orchestra_dc.yaml` | 97 Dublin Core / DCterms / DCMIType / XML namespace classes, 2 types, 1 enum, 55 slots — split out from the main schema |
| XSD -> schema converter | `scripts/schema_to_linkml.py` | Reads `repository.xsd`, `repositorytypes.xsd`, `interfaces.xsd`; opt-in `--orchestra-xml` flag enriches the 38 FIX base datatypes with `proto_scalar` annotations; emits both schema files |
| Wire-format proto generator | `scripts/fix_xml_to_proto.py` | Reads a FIX Orchestra XML repository file; emits a proto3 definition with one `message` per FIX message/component/group and one `enum` per code set |
| Wire-format proto | `project/protobuf/fix_orchestra.wire.proto` | Generated from `OrchestraFIXLatest.xml` — 932 messages, 691 enums, 1.1 MB |
| Known issues | `upstream-releases/ISSUE.md` | Documents upstream XSD bugs and downstream tool bugs (including the broken `gen-proto` output from LinkML) |

## Justfile recipes

| Recipe | Purpose |
|---|---|
| `just gen-linkml` | Regenerate the LinkML schema enriched with FIX base datatype `proto_scalar` annotations |
| `just gen-project` | Run all LinkML generators against the schema |
| `just gen-proto-wire` | Generate `project/protobuf/fix_orchestra.wire.proto` from `OrchestraFIXLatest.xml` |
| `just test-third-party` | Validate the FIX Orchestra XML corpus against the LinkML schema |
| `just test` | Run the full test suite |

## Test suite

103 tests across three modules:

- `tests/test_data.py` — unit tests for the schema converter
- `tests/test_third_party.py` — validates 14 FIX Orchestra XML orchestration files against the LinkML schema (7,882 records validated for `OrchestraFIXLatest.xml` alone)
- `tests/test_proto.py` — 15 tests for the wire-format proto generator (syntax, field numbering, enum sentinels, custom options, committed file integrity)

## Schema enrichment

Running `just gen-linkml` (or `python3 scripts/schema_to_linkml.py --orchestra-xml <path>`) does two things and emits **two schema files**:

1. **FIX base datatypes** — adds 38 FIX base datatype entries to the schema `types:` section under
   the `fix_base_types` subset.  Each entry carries a `proto_scalar` annotation:

   ```yaml
     FIXPrice:
       typeof: float
       uri: fixr:Price
       in_subset: [fix_base_types]
       annotations:
         proto_scalar: Decimal64
   ```

2. **Description enrichment** — every `xs:annotation/xs:documentation` element in the upstream
   XSDs is imported into the corresponding LinkML entity's `description:` field.  Coverage after
   enrichment (descriptions / total):

   | Section | With description |
   |---|---|
   | `slots` (global) | 42 / 117 |
   | `types` | 47 / 53 |
   | `classes` | 15 / 69 |
   | `enums` | 6 / 20 |
   | class `attributes` (inline) | 35 / 129 |

   (DC-vocabulary entities now live in `fix_orchestra_dc.yaml` and are excluded from the counts above.)

   The remaining gaps reflect XSD entities that the upstream authors left undocumented (no
   `xs:documentation` present).  The extractor is complete — when the upstream XSDs are updated
   with new documentation nodes, `just gen-linkml` will pick them up automatically.

   Two extraction improvements were made to the generator:

   - **Best-description selection in slot promotion** — `_promote_to_schema_slots()` used to take
     the first-encountered class's attribute definition as the canonical global slot, losing
     descriptions from later uses.  It now scans all uses and applies the first non-empty
     description, recovering descriptions for `when`, `field_ref`, `presence`, `which`,
     `impl_min_occurs`, and `impl_max_occurs`.

   - **Inline element/attribute docs in auxiliary XSDs** — `_emit_aux_elements()` now propagates
     `xs:documentation` from inline anonymous `xs:complexType` children.

3. **Dublin Core schema split** — The 97 Dublin Core / DCterms / DCMIType / XML namespace classes
   (and their 55 slots, 2 types, 1 enum, 4 subsets) were separated into a companion schema
   `fix_orchestra_dc.yaml`.  The main schema imports it via `imports: [linkml:types, fix_orchestra_dc]`.
   The XML-to-YAML converter (`fix_xml_to_linkml.py`) was updated to merge locally-resolvable
   imports before indexing the schema, so it sees DC classes when structuring the `metadata` field.

## Known issues

See [`upstream-releases/ISSUE.md`](../upstream-releases/ISSUE.md) for documented bugs:

1. **`categoryType/@section` declared `use="required"` in the XSD but omitted in canonical FIX data.**
   Workaround applied in `schema_to_linkml.py` via `_OPTIONAL_DESPITE_XSD`.
   Upstream target: [fix-orchestra-spec](https://github.com/FIXTradingCommunity/fix-orchestra-spec).

2. **LinkML `gen-proto` produces invalid proto3** — all 1,018 fields numbered `= 0`, blank `package`
   line, fails `protoc`.  The file `project/protobuf/fix_orchestra.proto` is retained as-is.
   `project/protobuf/fix_orchestra.wire.proto` is the replacement.
   Upstream target: [linkml/linkml](https://github.com/linkml/linkml).

# References

- [Fix Orchestra](https://github.com/FIXTradingCommunity/fix-orchestra)
- [fix-orchestra-spec](https://github.com/FIXTradingCommunity/fix-orchestra-spec)
- [LinkML](https://linkml.io/)
- [Protocol Buffers](https://protobuf.dev/)