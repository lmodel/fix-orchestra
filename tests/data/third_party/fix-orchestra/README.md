# Third-party FIX Orchestra test data

Sample XML instances pulled from the FIX Trading Community
[fix-orchestra](https://github.com/FIXTradingCommunity/fix-orchestra)
reference implementation. Useful for exercising the generated LinkML schema
against representative real-world Orchestra documents.

## Inventory

### `valid/` - documents that conform to the upstream XSDs

| File | Size | Schema root | Target namespace | Upstream path |
|---|---|---|---|---|
| `SampleInterfaces.xml` | 14 KB | `<fixi:interfaces>` | `fixprotocol.io/2022/orchestra/interfaces` | `interfaces/src/test/resources/examples/SampleInterfaces.xml` |
| `mit_2016.xml` | 8.9 MB | `<fixr:repository>` | `fixprotocol.io/2024/orchestra/repository` | `orchestra2doc/src/test/resources/mit_2016.xml` |
| `OrchestraFIXLatest.xml` | 9.4 MB | `<fixr:repository>` | `fixprotocol.io/2024/orchestra/repository` | `repository-util/src/test/resources/OrchestraFIXLatest.xml` |

### `invalid/` - intentionally malformed (negative tests)

| File | Size | Schema root | Target namespace | Upstream path |
|---|---|---|---|---|
| `interfaceswitherrors.xml` | 14 KB | `<fixi:interfaces>` | `fixprotocol.io/2020/orchestra/interfaces` | `interfaces-util/src/test/resources/interfaceswitherrors.xml` |
| `repositorywitherrors.xml` | 6 KB | `<fixr:repository>` | `fixprotocol.io/2022/orchestra/repository` | `repository-util/src/test/resources/repositorywitherrors.xml` |

## Selection rationale

- **`mit_2016.xml`**: three near-identical revisions exist upstream
  (`repository/`, `repository-util/`, `orchestra2doc/`). All three describe
  the same FIX edition (`FIX.5.0SP2_EP216`) and differ by a few hundred bytes
  in annotation/documentation prose. The `orchestra2doc` copy is kept because
  it uses the **2024** target namespace, matching the XSDs in
  `upstream-releases/`. The other two use the 2022 namespace and would
  require a namespace rewrite to validate against the current schema.
- **`OrchestraFIXLatest.xml`**: also uses the 2024 namespace, the largest
  single instance available, and exercises the full FIX latest dictionary.
- **`SampleInterfaces.xml`** and **`interfaceswitherrors.xml`**: only one
  copy exists upstream for each. Namespaces are older (2022 and 2020) but
  the schema structure is identical to the 2024 `interfaces.xsd`; downstream
  tooling can normalise the namespace if strict prefix matching is required.

## Skipped from upstream

- `repository-util/.../FixRepositoryUnifiedEP247.xml` and
  `FIX.5.0SP2_EP247_en_phrases.xml` use the legacy **2010** schema family
  (`<fixRepository>` root, `<phrases>` root). They do not validate against
  the current Orchestra `repository.xsd` and would require a separate LinkML
  schema derived from `repository2010/.../FixRepository.xsd` to be useful.
- The two near-duplicate `mit_2016.xml` copies (see above).

## Usage

These files are excluded from `linkml-validate` runs by default - they
target the FIX XSDs, not the generated LinkML schema. To validate them
against the LinkML schema you must either:

1. Generate a JSON Schema and transform the XML to JSON (e.g. via
   `xq` / `xmltodict`), then `linkml-validate --target-class Repository
   instance.json`; or
2. Use the XSDs directly via `xmllint`:

   ```bash
   xmllint --schema upstream-releases/repository.xsd \
           --noout tests/data/third_party/fix-orchestra/valid/mit_2016.xml
   ```

## Provenance and license

All files copied verbatim (byte-identical) from the FIX Trading Community
GitHub repository at
[`FIXTradingCommunity/fix-orchestra`](https://github.com/FIXTradingCommunity/fix-orchestra).
Upstream commits and SHAs are tracked in `upstream-releases/github-fix-orchestra/`.

Content is © Copyright 2016-2024 FIX Protocol Limited under
[Creative Commons Attribution-NoDerivatives 4.0 International
(CC BY-ND 4.0)](https://creativecommons.org/licenses/by-nd/4.0/). These
files are unmodified.
