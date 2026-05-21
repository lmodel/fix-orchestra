# Upstream Issue: `categoryType/@section` declared `use="required"` but omitted in canonical FIX data

**Target repository:** https://github.com/FIXTradingCommunity/fix-orchestra-spec  
**Affected file:** `repositorytypes.xsd` (v1.1-rc2, namespace `http://fixprotocol.io/2024/orchestra/repository`)  
**Affected line:** 116

---

## Summary

`repositorytypes.xsd` declares the `section` attribute on `categoryType` as `use="required"`, yet the canonical FIX Orchestra XML distributions published by the FIX Trading Community itself consistently omit this attribute for three special cross-section categories: **`Common`**, **`Fields`**, and **`ImplFields`**.  The XSD constraint is stricter than the data it is meant to describe — this is a bug in the specification.

---

## XSD declaration (the constraint)

```xml
<!-- repositorytypes.xsd, line 116 -->
<xs:complexType name="categoryType">
    ...
    <xs:attribute name="name"    type="fixr:Name_t" use="required"/>
    <xs:attribute name="section" type="fixr:Name_t" use="required"/>  <!-- ← bug -->
    ...
</xs:complexType>
```

---

## Observed data (canonical FIX distributions)

The five sections defined in every full FIX repository are `Session`,
`PreTrade`, `Trade`, `PostTrade`, and `Infrastructure`.  Three categories (`Common`, `Fields`, `ImplFields`) are genuinely cross-section — their content is shared across all sections — so they carry no `section` attribute:

```xml
<!-- OrchestraFIXLatest (FIX.Latest_EP302), orchestrations repo -->
<fixr:category name="Common"     componentType="Message" FIXMLFileName="components" includeFile="fields"/>
<fixr:category name="Fields"     componentType="Field"   FIXMLFileName="fields"/>
<fixr:category name="ImplFields" componentType="Field"   FIXMLFileName="fields"/>
```

---

## Affected files

All files distributed by the FIX Trading Community that include a full category table are affected:

| File | Repository | Version | Categories missing `section` |
|------|-----------|---------|------------------------------|
| `OrchestraFIXLatest.xml` | fix-orchestra | FIX.Latest_EP269 | `Common`, `Fields`, `ImplFields` |
| `mit_2016.xml` | fix-orchestra | FIX.5.0SP2_EP216 | `Common`, `Fields`, `ImplFields` |
| `OrchestraFIXLatest.xml` | orchestrations | FIX.Latest_EP302 | `Common`, `Fields`, `ImplFields` |
| `OrchestraExamples-v11-RC1.xml` | orchestrations | FIX.5.0SP2_EP216 | `Common`, `Fields`, `ImplFields` |
| `OrchestraFIX44.xml` | orchestrations | EP294 | `Common` |

Files that contain **no** `<category>` elements at all (e.g. the rules-of-engagement overlays such as `Equity.xml`, `Future.xml`, `OrchestraFIXLatestNonOTC_EP273.xml`) are unaffected because they do not include a category table.

---

## Is this a data bug or a specification bug?

**It is a specification bug.**

The three affected categories have no meaningful section membership:

* **`Common`** — messages and components used by every FIX section equally.
* **`Fields`** — field definitions shared across all sections.
* **`ImplFields`** — implementation-specific fields shared across all sections.

No single value from `{Session, PreTrade, Trade, PostTrade, Infrastructure}` correctly describes these categories.  The canonical data produced by the FIX Trading Community itself has never included `section` for these entries, across every version from FIX 4.4 (EP294) through FIX.Latest (EP302).  Requiring the attribute is therefore an over-constraint in the schema.

An XSD validator rejects each of these files due to this constraint:

```
cvc-complex-type.4: Attribute 'section' must appear on element 'fixr:category'.
```

---

## Proposed fix

Change `use="required"` to `use="optional"` (or simply omit the `use` attribute, which defaults to optional) on the `section` attribute of `categoryType`:

```xml
<!-- before -->
<xs:attribute name="section" type="fixr:Name_t" use="required"/>

<!-- after -->
<xs:attribute name="section" type="fixr:Name_t"/>
```

This aligns the schema with every published FIX Orchestra document and has no impact on files that already supply a `section` value.

---

## How this was detected

Automated LinkML-schema validation of the published FIX Orchestra XML files in this repository (`lmodel/finos/fix-orchestra`) flagged `'section' is a required property` for every `<category>` element that lacks the attribute.  The LinkML schema was originally generated faithfully from `repositorytypes.xsd`; it was corrected to treat `section` as optional (`_OPTIONAL_DESPITE_XSD` override in `scripts/schema_to_linkml.py`) precisely because the XSD constraint contradicts the published data.

---

# Downstream tool issue: `gen-proto` produces invalid proto3

**Target:** https://github.com/linkml/linkml (`gen-proto` generator)  
**Affected command:** `uv run gen-proto <schema.yaml>`  
**Affected output:** `project/protobuf/fix_orchestra.proto`

---

## Summary

LinkML's `gen-proto` generator emits a proto3 file where every field is numbered `= 0` and the `package` line has no identifier.  Both are fatal errors for `protoc`: field number 0 is reserved and a bare `package;` is a syntax error. The generated file cannot be compiled or used.

---

## Reproducer

```bash
# From the fix-orchestra repo root:
uv run gen-proto src/fix_orchestra/schema/fix_orchestra.yaml > /tmp/check.proto

# Field number 0 occurrences (should be 0 in valid proto3):
grep -c ' = 0$' /tmp/check.proto
# 1018

# First four lines — the blank `package` line is line 2:
head -4 /tmp/check.proto
#  syntax="proto3";
#  package
#  // metamodel_version: 1.11.0
#  // version: 1.1-rc2

# protoc rejects it:
protoc --proto_path=/tmp /tmp/check.proto
# /tmp/check.proto:2:8: Expected ";".
```

The same broken file is committed to this repository as `project/protobuf/fix_orchestra.proto` and is regenerated on every `just gen-project` run.

---

## Root cause

`gen-proto` was written for an earlier LinkML metamodel and has two known defects:

1. **Field numbers** — the generator emits `= 0` for every field instead of assigning stable sequential integers.  Proto3 forbids field number 0.
2. **Package declaration** — the `package` value is derived from the schema's `id` URI; the current schema URI maps to an empty string after stripping.

These bugs affect any LinkML schema, not just FIX Orchestra.

---

## Scope of the broken output

The current `project/protobuf/fix_orchestra.proto` is a **metamodel proto** — it represents the FIX Orchestra *specification schema* types (`FieldType`,
`MessageType`, `CodeSetType`, …) as proto messages.  This is categorically different from a **wire-format proto** that represents actual FIX trading messages (`NewOrderSingle`, `Instrument`, …).

The wire-format proto — the artefact useful for FIX trading systems — is generated by `scripts/fix_xml_to_proto.py` in this repository (see
`project/protobuf/fix_orchestra.wire.proto`).

---

## Proposed fix (upstream)

1. `gen-proto` should assign sequential field numbers starting from 1 within
   each generated message, preserving slot-definition order in the schema.
2. The `package` value should fall back to a sanitised form of the schema
   `name` when the `id` URI cannot be converted to a valid proto identifier.
