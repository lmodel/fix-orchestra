# FIX Orchestra upstream specification

## File inventory

### FIX Orchestra v1.1-RC2 schemas (authoritative)

Source: <https://www.fixtrading.org/standards/fix-orchestra-standard/>

```bash
unzip ~/Downloads/Orchestra-Schema-v1.1-RC2-108835.zip
```

| File | Size | Description |
|---|---|---|
| `repository.xsd` | 11 KB | Top-level container schema (`<repository>`, `<actors>`, `<fields>`, `<messages>`, ...). |
| `repositorytypes.xsd` | 47 KB | All complex/simple types referenced by `repository.xsd` (`fieldType`, `messageType`, `codeSetType`, ...). |
| `interfaces.xsd` | 12 KB | Service / session / encoding / protocol / transport bindings (`<interfaces>`). |

Target namespaces:

- `http://fixprotocol.io/2024/orchestra/repository` (`fixr:`)
- `http://fixprotocol.io/2024/orchestra/interfaces` (`fixi:`)

#### Supporting imports (W3C / Dublin Core)

These files complete the `<xs:import>` graph so the three XSDs above can be validated offline (e.g. `xmllint --schema repository.xsd …`). Sourced from the FIX Trading Community [fix-orchestra](https://github.com/FIXTradingCommunity/fix-orchestra) GitHub repository - byte-identical to upstream.

| File | Size | Origin |
|---|---|---|
| `dc.xsd` | 4 KB | Dublin Core elements 1.1 (<http://purl.org/dc/elements/1.1/>) |
| `dcmitype.xsd` | 2 KB | DCMI type vocabulary (<http://purl.org/dc/dcmitype/>) |
| `dcterms.xsd` | 13 KB | Dublin Core Terms (<http://purl.org/dc/terms/>) - imported by `repository.xsd` and `interfaces.xsd` via `<xs:import namespace="http://purl.org/dc/terms/" schemaLocation="dcterms.xsd"/>`. |
| `xml.xsd` | 9 KB | W3C XML namespace declarations (e.g. `xml:base`) - imported by `repository.xsd` and `interfaces.xsd`. |

#### FIXML appinfo content model

| File | Size | Origin |
|---|---|---|
| `FIXMLappinfo.xsd` | 1 KB | FIXML generator hints (`<fixml:FIXMLencoding>` with `notReqXML`, `inlined` attributes), namespace `http://fixprotocol.io/2022/orchestra/appinfo/fixml`. Copied byte-identical from [orchestra-transposer](https://github.com/FIXTradingCommunity/orchestra-transposer) (`orchestratransposer/orchestra/schemas/appinfo/FIXMLappinfo.xsd`). The canonical Orchestra XML corpus carries 500+ instances of this payload embedded in `<fixr:appinfo purpose="FIXML">` blocks; without this XSD the converter dropped the flags. |

### Reference: FIX Orchestra transposer (Python)

Vendored at `orchestra-transposer/` from <https://github.com/FIXTradingCommunity/orchestra-transposer> (Apache 2.0, FIX Trading Community). Pairwise converters between **Orchestra 1.0 ↔ SBE 1.0 ↔ FIX Unified Repository 2010** plus pythonic accessors for each schema. Not invoked at build time. Used as a source for:

- `FIXMLappinfo.xsd` (above) — the only file currently lifted into LinkML generation.
- Older Orchestra v1.0 XSDs (2020 namespace) — kept for historical comparison; superseded by the v1.1-RC2 XSDs already at the top of this directory.
- Reference implementations for SBE and Unified Repository conversion — out of scope for the current LinkML pipeline but available if we expand into those formats.

### Reference implementation: FIX Orchestra -> Protobuf/Cap'n Proto

Source: <https://github.com/FIXTradingCommunity/fix-orchestra-protobuf>  
Copied to `fix-orchestra-protobuf/` (commit `a2e9edd`).  
Maven artifact: `io.fixprotocol:orchestra2proto:0.0.1-SNAPSHOT`, orchestra binding `1.6.1`, Java 8, Apache 2.0.

Read as a **reference for domain semantics** — FIX datatype->proto scalar mapping, custom option field numbers (`tag=50001`, `msg_type_value=52001`, …), NumInGroup elision, `oneof` for `UnionDataType`, supporting messages (`Decimal64`, `Timestamp`, …), and sort-order-based enum numbering. No Java code is compiled or executed.

Key files: `ProtobufModelFactory.java` (1015 lines, primary reference), `CapnpModelFactory.java` (762 lines, Cap'n Proto variant for cross-checking), `ProtoGen.java` (199 lines, CLI entry point), plus value-object packages `protobuf/` and `capnp/` (11 and 10 files respectively).

## Regenerating the LinkML schema

The LinkML schema at `src/fix_orchestra/schema/fix_orchestra.yaml` is derived from these XSDs. Re-run after any update:

```bash
just gen-linkml      # XSD -> schema, then SSSOM overlay
```

`just gen-linkml` chains two steps:

1. `python3 scripts/schema_to_linkml.py --orchestra-xml upstream-releases/OrchestraFIXLatest.xml` — parses the XSDs above (plus `FIXMLappinfo.xsd`) and writes `src/fix_orchestra/schema/fix_orchestra{,_dc}.yaml`. Pure XSD-driven content lives here.
2. `python3 scripts/apply_sssom_overlay.py` — reads any `*.sssom.tsv` in `src/fix_orchestra/mappings/` and merges the cross-schema mapping CURIEs (currently Orchestra ↔ SBE) into the schema's `exact_mappings` / `close_mappings` / `broad_mappings` / `narrow_mappings` / `related_mappings` slots. Idempotent; rerunning produces no further changes.

If only the SSSOM TSVs were edited (no XSD changes), `just overlay-sssom-mappings` runs step 2 alone.

The mapping TSVs live under `src/fix_orchestra/mappings/`, not here — `upstream-releases/` is reserved for byte-identical copies of upstream vendor artefacts.

## Test data

Sample XML instances pulled from the upstream [FixTradingCommunity](https://github.com/FIXTradingCommunity/) live under `tests/data/third_party/` with their own READMEs.

## License

The upstream XSDs and PDF are © Copyright 2016-2024 FIX Protocol Limited and distributed under [Creative Commons Attribution-NoDerivatives 4.0 International (CC BY-ND 4.0)](https://creativecommons.org/licenses/by-nd/4.0/). Dublin Core and W3C XML namespace schemas carry their own permissive terms; see file headers.
