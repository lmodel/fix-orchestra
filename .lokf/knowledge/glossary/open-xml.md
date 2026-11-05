---
type: GlossaryTerm
id: https://w3id.org/lmodel/fix-orchestra/knowledge/glossary/open-xml
title: Open XML
description: "Open XML: an element or attribute in a place where the XSDs accept any content, such as an application hint's FIXML flags, which the schema keeps as written in `OrchestraXmlElement` and `OrchestraXmlAttribute`."
relatedTo:
  - https://w3id.org/lmodel/fix-orchestra/knowledge/datasets/common-module
sources:
  - id: common-module
    resource: src/fix_orchestra/schema/fix_orchestra_common.yaml
    title: OrchestraXmlElement
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:53:42Z"
status: draft
---

# Open XML

An open element keeps its name with its namespace in braces, its attributes, its text, its children in order and the text after it.[^common-module]

[^common-module]: src/fix_orchestra/schema/fix_orchestra_common.yaml, OrchestraXmlElement
