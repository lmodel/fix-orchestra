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

Automated LinkML-schema validation of the published FIX Orchestra XML files in this repository (`lmodel/finos/fix-orchestra`) flagged
`'section' is a required property` for every `<category>` element that lacks the attribute.  The LinkML schema was originally generated faithfully from `repositorytypes.xsd`; it was corrected to treat `section` as optional (`_OPTIONAL_DESPITE_XSD` override in `scripts/schema_to_linkml.py`) precisely because the XSD constraint contradicts the published data.
