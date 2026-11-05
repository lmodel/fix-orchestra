# Explanations

* [Where the schema departs from the XSDs](departures-from-the-xsds.md) - The two places the schema and its rules differ from the XSDs: RC3's `fieldTypeOrCodeSetKey`, whose uniqueness the rules leave out, and the keys and references that only the rules check.
* [How the schema reads an XSD](how-the-schema-reads-an-xsd.md) - What each XSD construct becomes here: a complex type a class, an attribute group a mixin, an attribute or child element a `fixr_` or `fixi_` key, a repeated choice a list of members, and `xs:any` an open XML element.
* [Why the schema has two editions](two-editions.md) - Why v1.0 and v1.1 RC3 are separate modules with suffixed class names: neither edition is a superset of the other, and FIX Latest is published in v1.0.
* [What the real files show](what-the-real-files-show.md) - What FIX's own Orchestra files show when the schema reads them: FIX Latest's three categories without a section, the session files' undefined category, the 65-character group name RC3 refuses, and the v1.0 XSDs in the RC3 tag.
