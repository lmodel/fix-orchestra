---
type: Dataset
id: https://w3id.org/lmodel/fix-orchestra/knowledge/datasets/common-module
genre: reference
title: The common module
description: "`src/fix_orchestra/schema/fix_orchestra_common.yaml`: the 13 value lists both editions share, `OrchestraMetadata` for the Dublin Core block that heads a file, and `OrchestraXmlElement` and `OrchestraXmlAttribute` for XML the XSDs leave open."
resource: src/fix_orchestra/schema/fix_orchestra_common.yaml
isPartOf:
  - https://w3id.org/lmodel/fix-orchestra/knowledge/datasets/fix-orchestra-linkml-schema
about:
  - https://w3id.org/lmodel/fix-orchestra/knowledge/glossary/open-xml
sources:
  - id: common-module
    resource: src/fix_orchestra/schema/fix_orchestra_common.yaml
  - id: xsd-converter
    resource: scripts/orchestra_xsd_to_linkml.py
    title: build and common_classes
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:53:42Z"
status: draft
---

# The common module

`OrchestraMetadata` holds a multivalued key for each of the 15 Dublin Core elements, as `dc_`, and each of the 55 DCMI terms, as `dcterms_`, each under the term's own IRI.[^common-module]

A value list both editions give with the same values is shared and keeps its plain name, such as `OrchestraPresence`. A list only one edition gives takes that edition's suffix, such as `OrchestraPurposeV11`.[^xsd-converter]

[^common-module]: src/fix_orchestra/schema/fix_orchestra_common.yaml
[^xsd-converter]: scripts/orchestra_xsd_to_linkml.py, build and common_classes
