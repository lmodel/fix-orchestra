# Third-party orchestrations test data

XML instances copied from the FIX Trading Community
[orchestrations](https://github.com/FIXTradingCommunity/orchestrations) repository, whose purpose is to collect machine-readable rules of engagement (asset-class and session definitions) conformant to FIX Orchestra standard.

**License:** Apache 2.0 (© Copyright 2017–2026 FIX Protocol Limited).

## Inventory

| File | Size | Schema root | Target namespace | Description |
|---|---|---|---|---|
| `Debt.xml` | 215 KB | `<fixr:repository>` | 2020 | Debt-instrument rules of engagement |
| `Equity.xml` | 30 KB | `<fixr:repository>` | 2020 | Equity trading rules of engagement |
| `FIX44Session.xml` | 112 KB | `<fixr:repository>` | 2020 | FIX 4.4 session protocol definition |
| `FIXReferenceData.xml` | 469 KB | `<fixr:repository>` | 2020 | FIX reference-data definitions |
| `FIXTSession.xml` | 141 KB | `<fixr:repository>` | 2020 | FIXT session protocol definition |
| `Future.xml` | 96 KB | `<fixr:repository>` | 2020 | Futures trading rules of engagement |
| `Option.xml` | 121 KB | `<fixr:repository>` | 2020 | Options trading rules of engagement |
| `OrchestraExamples-v11-RC1.xml` | 6.3 MB | `<fixr:repository>` | **2022** | Orchestra v1.1-RC1 combined examples |
| `OrchestraFIX42.xml` | 660 KB | `<fixr:repository>` | 2020 | Full FIX 4.2 Orchestra dictionary |
| `OrchestraFIX44.xml` | 1.5 MB | `<fixr:repository>` | 2020 | Full FIX 4.4 Orchestra dictionary |
| `OrchestraFIXLatest.xml` | 7.2 MB | `<fixr:repository>` | 2020 | Full FIX latest dictionary (2020 ns) |
| `OrchestraFIXLatestNonOTC_EP273.xml` | 5.5 MB | `<fixr:repository>` | 2020 | FIX latest non-OTC subset (EP273) |
| `TradingDigitalAssets.xml` | 93 KB | `<fixr:repository>` | 2020 | Digital-assets trading rules of engagement |
| `Warrant.xml` | 36 KB | `<fixr:repository>` | 2020 | Warrant trading rules of engagement |

> **Note on namespaces:** the current LinkML schema and upstream XSDs use the
> 2024 namespace (`http://fixprotocol.io/2024/orchestra/repository`).  The 2020
> and 2022 namespaces are structurally equivalent; `scripts/fix_xml_to_linkml.py`
> normalises the namespace during conversion so all files validate against the same schema.

## Skipped from upstream

**`Examples/NYSE Pillar/NYSEPillarBinaryPhase2.xml`** — uses the legacy FIX
Repository 2016 namespace (`http://fixprotocol.io/2016/fixrepository`), which
predates the Orchestra standard and has a different root element structure
(`<fixr:repository>` with a distinct attribute set).  It does not validate
against the current `repository.xsd` and would require a separate schema
derived from the 2016 XSD to be useful.

### Maximum allowed validation errors

All files carry an error budget of `0` in `test_third_party.py::CASES`, confirmed by the `scripts/fix_xml_to_linkml.py` converter.  If future upstream updates introduce a known quirk, increment the budget and add a comment explaining the issue.  A non-zero budget should reflect an upstream data issue, not a converter or schema defect.

## Usage

```bash
# Well-formedness gate only (fast, no converter needed)
uv run pytest tests/test_third_party.py -m "not slow" -k orchestrations

# Full gate including LinkML validation (requires fix_xml_to_linkml.py)
uv run pytest tests/test_third_party.py -k orchestrations
```
