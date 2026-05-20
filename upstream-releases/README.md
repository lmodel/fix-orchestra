# FIX Orchestra upstream specification

Source: <https://www.fixtrading.org/standards/fix-orchestra-standard/>

The downloadable ZIP was unpacked here:

```bash
unzip ~/Downloads/Orchestra-Schema-v1.1-RC2-108835.zip
```

## File inventory

### FIX Orchestra v1.1-RC2 schemas (authoritative)

| File | Size | Description |
|---|---|---|
| `repository.xsd` | 11 KB | Top-level container schema (`<repository>`, `<actors>`, `<fields>`, `<messages>`, ...). |
| `repositorytypes.xsd` | 47 KB | All complex/simple types referenced by `repository.xsd` (`fieldType`, `messageType`, `codeSetType`, ...). |
| `interfaces.xsd` | 12 KB | Service / session / encoding / protocol / transport bindings (`<interfaces>`). |

Target namespaces:

- `http://fixprotocol.io/2024/orchestra/repository` (`fixr:`)
- `http://fixprotocol.io/2024/orchestra/interfaces` (`fixi:`)

### Supporting imports (W3C / Dublin Core)

These files complete the `<xs:import>` graph so the three XSDs above can be validated offline (e.g. `xmllint --schema repository.xsd …`). Sourced from the FIX Trading Community [fix-orchestra](https://github.com/FIXTradingCommunity/fix-orchestra) GitHub repository - byte-identical to upstream.

| File | Size | Origin |
|---|---|---|
| `dc.xsd` | 4 KB | Dublin Core elements 1.1 (<http://purl.org/dc/elements/1.1/>) |
| `dcmitype.xsd` | 2 KB | DCMI type vocabulary (<http://purl.org/dc/dcmitype/>) |
| `dcterms.xsd` | 13 KB | Dublin Core Terms (<http://purl.org/dc/terms/>) - imported by `repository.xsd` and `interfaces.xsd` via `<xs:import namespace="http://purl.org/dc/terms/" schemaLocation="dcterms.xsd"/>`. |
| `xml.xsd` | 9 KB | W3C XML namespace declarations (e.g. `xml:base`) - imported by `repository.xsd` and `interfaces.xsd`. |

### Other artefacts

| File | Description |
|---|---|
| `Orchestra-V1.1-RC2-Technical-Proposal-v0.2.pdf` | Vendor technical proposal narrative (reference reading). |

## Regenerating the LinkML schema

The LinkML schema at `src/fix_orchestra/schema/fix_orchestra.yaml` is
derived from these XSDs. Re-run after any update:

```bash
python3 scripts/schema_to_linkml.py
```

## Test data

Sample XML instances pulled from the upstream [Fix-Orchestra](https://github.com/FIXTradingCommunity/fix-orchestra) repository live under `tests/data/third_party/fix-orchestra/` with their own [README](../tests/data/third_party/fix-orchestra/README.md).

## License

The upstream XSDs and PDF are © Copyright 2016-2024 FIX Protocol Limited and distributed under [Creative Commons Attribution-NoDerivatives 4.0 International (CC BY-ND 4.0)](https://creativecommons.org/licenses/by-nd/4.0/). Dublin Core and W3C XML namespace schemas carry their own permissive terms; see file headers.
