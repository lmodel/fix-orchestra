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

### Reference implementation: FIX Orchestra -> Protobuf/Cap'n Proto

Source: <https://github.com/FIXTradingCommunity/fix-orchestra-protobuf>  
Copied to `fix-orchestra-protobuf/` (commit `a2e9edd`).  
Maven artifact: `io.fixprotocol:orchestra2proto:0.0.1-SNAPSHOT`, orchestra binding `1.6.1`, Java 8, Apache 2.0.

Read as a **reference for domain semantics** — FIX datatype->proto scalar mapping, custom option field numbers (`tag=50001`, `msg_type_value=52001`, …), NumInGroup elision, `oneof` for `UnionDataType`, supporting messages (`Decimal64`, `Timestamp`, …), and sort-order-based enum numbering. No Java code is compiled or executed.

Key files: `ProtobufModelFactory.java` (1015 lines, primary reference), `CapnpModelFactory.java` (762 lines, Cap'n Proto variant for cross-checking), `ProtoGen.java` (199 lines, CLI entry point), plus value-object packages `protobuf/` and `capnp/` (11 and 10 files respectively).

## Regenerating the LinkML schema

The LinkML schema at `src/fix_orchestra/schema/fix_orchestra.yaml` is derived from these XSDs. Re-run after any update:

```bash
python3 scripts/schema_to_linkml.py
```

## Test data

Sample XML instances pulled from the upstream [FixTradingCommunity](https://github.com/FIXTradingCommunity/) live under `tests/data/third_party/` with their own READMEs.

## License

The upstream XSDs and PDF are © Copyright 2016-2024 FIX Protocol Limited and distributed under [Creative Commons Attribution-NoDerivatives 4.0 International (CC BY-ND 4.0)](https://creativecommons.org/licenses/by-nd/4.0/). Dublin Core and W3C XML namespace schemas carry their own permissive terms; see file headers.
