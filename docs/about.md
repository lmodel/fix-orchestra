# About fix-orchestra

FIX Orchestra - LinkML Schema and wire-format toolchain.

This project converts the FIX Orchestra XSD specification into a [LinkML](https://linkml.io/) schema and generates a wire-format Protocol Buffers definition directly from the FIX Orchestra XML repository.

## What is here

| Artefact | Path | Description |
|---|---|---|
| LinkML schema (FIX) | `src/fix_orchestra/schema/fix_orchestra.yaml` | 70 classes, 53 types (38 FIX base), 20 enums, 120 slots — generated from the upstream XSDs; imports the DC companion |
| LinkML schema (DC) | `src/fix_orchestra/schema/fix_orchestra_dc.yaml` | 97 Dublin Core / DCterms / DCMIType / XML namespace classes, 2 types, 1 enum, 55 slots — split out from the main schema |
| XSD -> schema converter | `scripts/schema_to_linkml.py` | Reads `repository.xsd`, `repositorytypes.xsd`, `interfaces.xsd`, and `FIXMLappinfo.xsd`; opt-in `--orchestra-xml` flag enriches the 38 FIX base datatypes with `proto_scalar` annotations; emits both schema files |
| Wire-format proto generator | `scripts/fix_xml_to_proto.py` | Reads a FIX Orchestra XML repository file; emits a proto3 definition with one `message` per FIX message/component/group and one `enum` per code set |
| Wire-format proto | `project/protobuf/fix_orchestra.wire.proto` | Generated from `OrchestraFIXLatest.xml` — 932 messages, 691 enums, 1.1 MB |
| SSSOM mappings (Orchestra → SBE) | `src/fix_orchestra/mappings/fix-orchestra-to-fix-sbe.sssom.tsv` | 28 manually-curated cross-schema mappings from FIX Orchestra entities to FIX Simple Binary Encoding (SBE) entities, using SKOS predicates (`exactMatch`, `closeMatch`, `broadMatch`, `narrowMatch`) |
| SSSOM overlay | `scripts/apply_sssom_overlay.py` | Project-agnostic overlay: reads `*.sssom.tsv` files in a mappings dir, merges the predicate-mapped CURIEs into matching `exact_mappings` / `close_mappings` / `broad_mappings` / `narrow_mappings` / `related_mappings` slots on classes / enums / types. Idempotent; subject prefix autodetected from each schema's `default_prefix:` |
| Known issues | `upstream-releases/ISSUE.md` | Documents upstream XSD bugs and downstream tool bugs (including the broken `gen-proto` output from LinkML) |

## Justfile recipes

| Recipe | Purpose |
|---|---|
| `just gen-linkml` | Regenerate the LinkML schema enriched with FIX base datatype `proto_scalar` annotations, then chain into `overlay-sssom-mappings` |
| `just overlay-sssom-mappings` | Apply `*.sssom.tsv` files in `src/fix_orchestra/mappings/` onto the generated schema YAMLs (callable standalone after editing a TSV without re-running `gen-linkml`) |
| `just gen-project` | Run all LinkML generators against the schema |
| `just gen-proto-wire` | Generate `project/protobuf/fix_orchestra.wire.proto` from `OrchestraFIXLatest.xml` |
| `just test-third-party` | Validate the FIX Orchestra XML corpus against the LinkML schema |
| `just test` | Run the full test suite |

## Test suite

103 tests across three modules:

- `tests/test_data.py` — unit tests for the schema converter
- `tests/test_third_party.py` — validates 17 FIX Orchestra XML files across two upstream corpora (`tests/data/third_party/fix-orchestra/` and `tests/data/third_party/orchestrations/`) against the LinkML schema; 36,986 FIX records validated cleanly in total
- `tests/test_proto.py` — 15 tests for the wire-format proto generator (syntax, field numbering, enum sentinels, custom options, committed file integrity)

## Schema enrichment

Running `just gen-linkml` (or `python3 scripts/schema_to_linkml.py --orchestra-xml <path>`) does two things and emits **two schema files**:

1. **FIX base datatypes** — adds 38 FIX base datatype entries to the schema `types:` section under the `fix_base_types` subset.  Each entry carries a `proto_scalar` annotation:

   ```yaml
     FIXPrice:
       typeof: float
       uri: fix_orchestra:FIXPrice
       exact_mappings: [fixr:Price]
       in_subset: [fix_base_types]
       annotations:
         proto_scalar: Decimal64
   ```

2. **Description enrichment** — every `xs:annotation/xs:documentation` element in the upstream XSDs is imported into the corresponding LinkML entity's `description:` field.  Coverage after enrichment (descriptions / total):

   | Section | With description |
   |---|---|
   | `slots` (global) | 42 / 117 |
   | `types` | 47 / 53 |
   | `classes` | 15 / 69 |
   | `enums` | 6 / 20 |
   | class `attributes` (inline) | 35 / 129 |

   (DC-vocabulary entities now live in `fix_orchestra_dc.yaml` and are excluded from the counts above.)

   The remaining gaps reflect XSD entities that the upstream authors left undocumented (no `xs:documentation` present).  The extractor is complete — when the upstream XSDs are updated with new documentation nodes, `just gen-linkml` will pick them up automatically.

   Two extraction improvements were made to the generator:

   - **Best-description selection in slot promotion** — `_promote_to_schema_slots()` used to take the first-encountered class's attribute definition as the canonical global slot, losing descriptions from later uses.  It now scans all uses and applies the first non-empty description, recovering descriptions for `when` `field_ref`, `presence`, `which`,
     `impl_min_occurs`, and `impl_max_occurs`.

   - **Inline element/attribute docs in auxiliary XSDs** — `_emit_aux_elements()` now propagates
     `xs:documentation` from inline anonymous `xs:complexType` children.

3. **Dublin Core schema split** — The 97 Dublin Core / DCterms / DCMIType / XML namespace classes
   (and their 55 slots, 2 types, 1 enum, 4 subsets) were separated into a companion schema `fix_orchestra_dc.yaml`.  The main schema imports it via `imports: [linkml:types, fix_orchestra_dc]`. The XML-to-YAML converter (`fix_xml_to_linkml.py`) was updated to merge locally-resolvable imports before indexing the schema, so it sees DC classes when structuring the `metadata` field.

4. **Resolvable element URIs** — `class_uri`, `slot_uri`, `enum_uri`, and type `uri` on FIX-originated entities now use the project-owned `fix_orchestra:` prefix
   (`https://w3id.org/lmodel/fix-orchestra/`) so URIs rendered by `gen-doc` resolve through the w3id redirect to the published documentation site. The upstream FIX target namespace is preserved as `exact_mappings: [fixr:<original>]` (or `[fixi:<original>]` for `interfaces.xsd`), keeping semantic identity intact for RDF/OWL generation. Dublin Core / DCterms / DCMIType / xml.xsd entities keep their canonical resolvable URIs using linkml-lint's canonical prefix names: `dc:`, `dcterms:`, `dctypes:`, `XML:` (formerly emitted as `dct:`, `dcmitype:`, `xml:` — renamed to clear the `canonical_prefixes` lint warnings).

5. **FIXML appinfo content model** — the canonical Orchestra XML corpus carries 500+ `<fixr:appinfo purpose="FIXML"><fixml:FIXMLencodingType notReqXML inlined/></fixr:appinfo>` payloads that previous versions of the converter silently dropped. The generator now reads `upstream-releases/FIXMLappinfo.xsd` (vendored from [orchestra-transposer](https://github.com/FIXTradingCommunity/orchestra-transposer)) and emits a `FIXMLencodingType` class with `inlined` and `not_req_xml` boolean attributes, wired onto `Appinfo` via a `fixml_encoding` slot (aliased to `FIXMLencoding`, `FIXMLencodingType` so the XML→YAML converter resolves the child element correctly):

   ```yaml
     Appinfo:
       slots: [..., fixml_encoding]
     FIXMLencodingType:
       class_uri: fix_orchestra:FIXMLencodingType
       exact_mappings: [fixml:FIXMLencodingType]
       slots: [inlined, not_req_xml]
   ```

   After this change, running `python3 scripts/fix_xml_to_linkml.py` against `OrchestraFIXLatest.xml` produces 1,142 `fixml_encoding` / `not_req_xml` lines in the YAML output, where previously there were zero. `scripts/fix_xml_to_linkml.py` was updated alongside: `SchemaIndex.slot_for_xml_name()` now consults each slot's `aliases:` list, so element local-names whose snake-casing diverges from the schema slot name (`FIXMLencodingType` → `fixml_encoding`) still resolve.

6. **Cross-schema mappings via SSSOM overlay** — manually-curated mappings from Orchestra entities to sister-format entities (currently FIX Simple Binary Encoding) are stored as [SSSOM](https://mapping-commons.github.io/sssom/) TSV files under `src/fix_orchestra/mappings/`. After `schema_to_linkml.py` regenerates the schema, `scripts/apply_sssom_overlay.py` reads each `*.sssom.tsv`, picks out rows whose subject CURIE matches the schema's `default_prefix:` (autodetected — `fix_orchestra:` for this project), and merges the predicate-mapped object CURIEs into the matching mapping slot. SKOS predicate → LinkML slot:

   | SSSOM predicate | LinkML slot |
   |---|---|
   | `skos:exactMatch` | `exact_mappings` |
   | `skos:closeMatch` | `close_mappings` |
   | `skos:broadMatch` | `broad_mappings` |
   | `skos:narrowMatch` | `narrow_mappings` |
   | `skos:relatedMatch` | `related_mappings` |

   The current Orchestra → SBE TSV adds 28 cross-schema mapping CURIEs to 12 Orchestra entities. Example result on `FieldType`:

   ```yaml
     FieldType:
       class_uri: fix_orchestra:FieldType
       exact_mappings:
         - fixr:fieldType        # XSD source (added by schema_to_linkml.py)
         - fix_sbe:FieldTypeV1   # added by apply_sssom_overlay.py
         - fix_sbe:FieldTypeV2   # added by apply_sssom_overlay.py
   ```

   The overlay script is **project-agnostic** (autodetects subject side from the schema's `default_prefix:`) and **idempotent** (running twice produces no further changes). `just gen-linkml` chains into `just overlay-sssom-mappings` via just's `&&` post-dependency syntax, so editing a TSV and re-running `just gen-linkml` re-applies the overlay automatically. The overlay can also be invoked standalone (`just overlay-sssom-mappings`) when only TSV edits need pushing into the schema. Bidirectional mapping files can coexist in `src/fix_orchestra/mappings/` without cross-pollution: rows whose subject CURIE doesn't match the local schema's prefix are silently skipped.

## Known issues

See [`upstream-releases/ISSUE.md`](../upstream-releases/ISSUE.md) for documented bugs:

1. **`categoryType/@section` declared `use="required"` in the XSD but omitted in canonical FIX data.**
   Workaround applied in `schema_to_linkml.py` via `_OPTIONAL_DESPITE_XSD`.
   Upstream target: [fix-orchestra-spec](https://github.com/FIXTradingCommunity/fix-orchestra-spec).

2. **LinkML `gen-proto` produces invalid proto3** — all 1,018 fields numbered `= 0`, blank `package` line, fails `protoc`.  The file `project/protobuf/fix_orchestra.proto` is retained as-is `project/protobuf/fix_orchestra.wire.proto` is the replacement. Upstream target: [linkml/linkml](https://github.com/linkml/linkml).

## References

- [Fix Orchestra](https://github.com/FIXTradingCommunity/fix-orchestra)
- [fix-orchestra-spec](https://github.com/FIXTradingCommunity/fix-orchestra-spec)
- [orchestra-transposer](https://github.com/FIXTradingCommunity/orchestra-transposer)
- [LinkML](https://linkml.io/)
- [Protocol Buffers](https://protobuf.dev/)
