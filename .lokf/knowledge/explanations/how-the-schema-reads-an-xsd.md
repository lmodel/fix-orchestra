---
type: Explanation
id: https://w3id.org/lmodel/fix-orchestra/knowledge/explanations/how-the-schema-reads-an-xsd
genre: explanation
title: How the schema reads an XSD
description: "What each XSD construct becomes here: a complex type a class, an attribute group a mixin, an attribute or child element a `fixr_` or `fixi_` key, a repeated choice a list of members, and `xs:any` an open XML element."
resource: docs/about.md
about:
  - https://w3id.org/lmodel/fix-orchestra/knowledge/glossary/member
  - https://w3id.org/lmodel/fix-orchestra/knowledge/glossary/open-xml
sources:
  - id: about
    resource: docs/about.md
    title: How the schema reads an XSD
generated:
  by: process:ktl-librarian
  at: "2026-11-05T20:05:31Z"
status: draft
---

# How the schema reads an XSD

A key is `fixr_` for a repository or `fixi_` for an interfaces file, then the XML name in snake case, and an `xml_attribute` or `xml_element` annotation keeps the XML name.[^about]

A value list joined with any string takes any text, and its enum lists the values Orchestra recommends.[^about]

[^about]: docs/about.md, How the schema reads an XSD
