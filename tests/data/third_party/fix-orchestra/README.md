# Third-party FIX Orchestra test data

Sample XML instances pulled from the FIX Trading Community
[fix-orchestra](https://github.com/FIXTradingCommunity/fix-orchestra) reference implementation. Useful for exercising the generated LinkML schema against representative real-world Orchestra documents.

## Inventory

| File | Size | Schema root | Target namespace | Upstream path |
|---|---|---|---|---|
| `SampleInterfaces.xml` | 14 KB | `<fixi:interfaces>` | `fixprotocol.io/2022/orchestra/interfaces` | `interfaces/src/test/resources/examples/SampleInterfaces.xml` |
| `mit_2016.xml` | 8.9 MB | `<fixr:repository>` | `fixprotocol.io/2024/orchestra/repository` | [src/test/resources/mit_2016.xml](https://raw.githubusercontent.com/FIXTradingCommunity/fix-orchestra/refs/heads/master/repository/src/test/resources/examples/mit_2016.xml) |
| `OrchestraFIXLatest.xml` | 9.4 MB | `<fixr:repository>` | `fixprotocol.io/2024/orchestra/repository` | `repository-util/src/test/resources/OrchestraFIXLatest.xml` |


## Selection rationale

- **`mit_2016.xml`**: three near-identical revisions exist upstream (`repository/`, `repository-util/`, `orchestra2doc/`). All three describe the same FIX edition (`FIX.5.0SP2_EP216`) and differ by a few hundred bytes in annotation/documentation prose. The `orchestra2doc` copy is kept because it uses the **2024** target namespace, matching the XSDs in `upstream-releases/`. The other two use the 2022 namespace and would require a namespace rewrite to validate against the current schema.

- **`OrchestraFIXLatest.xml`**: also uses the 2024 namespace, the largest single instance available, and exercises the full FIX latest dictionary.

- **`SampleInterfaces.xml`** and **`interfaceswitherrors.xml`**: only one copy exists upstream for each. Namespaces are older (2022 and 2020) but the schema structure is identical to the 2024 `interfaces.xsd`; downstream tooling can normalise the namespace if strict prefix matching is required.

## Skipped from upstream

- `repository-util/.../FixRepositoryUnifiedEP247.xml` and
  `FIX.5.0SP2_EP247_en_phrases.xml` use the legacy **2010** schema family (`<fixRepository>` root, `<phrases>` root). They do not validate against the current Orchestra `repository.xsd` and would require a separate LinkML schema derived from `repository2010/.../FixRepository.xsd` to be useful.

- The two near-duplicate `mit_2016.xml` copies (see above).

## Usage

The project ships a schema-aware XML -> YAML converter and a pytest module that wires conversion + validation together:

```bash
# One-shot: convert + validate all third-party files (prints record counts)
just test-third-party

# Or run the converter standalone to inspect the YAML output:
uv run python scripts/fix_xml_to_linkml.py \
    --in  tests/data/third_party/fix-orchestra/mit_2016.xml \
    --out /tmp/mit_2016.yaml
uv run linkml-validate -s src/fix_orchestra/schema/fix_orchestra.yaml \
    --target-class Repository /tmp/mit_2016.yaml
```

The pytest module ([`tests/test_third_party.py`](../../../test_third_party.py)) runs two gates per file - XML well-formedness and LinkML-schema validation - and prints the number of records processed per FIX container (`fields`, `messages`, `code_sets`, `groups`, ...). Representative output:

```
[wellformed] mit_2016.xml: 7189 records (fields=5644, codeSets=614, ...)
[validate]   mit_2016.xml (Repository): 1/1 errors | 7189 records (...)
```

### Maximum allowed validation errors

Each entry in `tests/test_third_party.py::CASES` lists the **maximum number of validation errors the test will tolerate** (third field). The test asserts `actual_errors <= max_allowed`, so a non-zero number documents a *known* upstream data issue that we accept rather than "fix" by patching the schema:

| File | Max allowed errors | Reason |
|---|---|---|
| `SampleInterfaces.xml` | 0 | Validates cleanly. |
| `mit_2016.xml` | 1 | FIX `Common` category lacks the XSD-required `section` attribute (real upstream data quirk). |
| `OrchestraFIXLatest.xml` | 1 | Same upstream data quirk. |

If a test starts failing because the actual error count exceeds the allowed number, **investigate the new errors before raising the limit**  they may indicate a regression in the schema generator (`scripts/schema_to_linkml.py`) or the XML -> YAML converter (`scripts/fix_xml_to_linkml.py`), not another quirk of the source data.

### Alternative: XSD validation

If you only need XSD-conformance (not LinkML conformance), `xmllint` remains the lossless path:

```bash
xmllint --schema upstream-releases/repository.xsd --noout \
        tests/data/third_party/fix-orchestra/mit_2016.xml
```

## Provenance and license

All files copied verbatim (byte-identical) from the FIX Trading Community GitHub repository at [`FIXTradingCommunity/fix-orchestra`](https://github.com/FIXTradingCommunity/fix-orchestra).

Content is © Copyright 2016-2024 FIX Protocol Limited under
[Creative Commons Attribution-NoDerivatives 4.0 International
(CC BY-ND 4.0)](https://creativecommons.org/licenses/by-nd/4.0/). These files are unmodified.
