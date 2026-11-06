---
type: Dataset
id: https://w3id.org/lmodel/fix-orchestra/knowledge/datasets/adapt-copy
genre: reference
title: The adapt copy
description: "`.lokf/schema/fix-orchestra.yaml`, which `just lokf-adapt` writes from the schema so that it can sit beside LOKF's: the file this bundle validates against, and the file a release attaches as `schema-<tag>-fix-orchestra.yaml`."
resource: .lokf/schema/fix-orchestra.yaml
derivedFrom:
  - https://w3id.org/lmodel/fix-orchestra/knowledge/datasets/fix-orchestra-linkml-schema
about:
  - https://w3id.org/lmodel/fix-orchestra/knowledge/glossary/adapt-copy
sources:
  - id: readme
    resource: README.md
    title: Knowledge Trust Ladder (KTL)
  - id: justfile
    resource: project.justfile
    title: lokf_adapt_args
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
    title: test_the_copy_keeps_every_class_and_key
generated:
  by: process:ktl-librarian
  at: "2026-11-06T21:19:55Z"
status: draft
---

# The adapt copy

The copy roots each edition's file classes and named elements on `Concept`, and keeps six Dublin Core keys, such as `dcterms_source`, whose IRIs LOKF's relations also use.[^justfile]

The copy renames nothing, because every key starts with `fixr_`, `fixi_`, `xml_`, `dc_` or `dcterms_`.[^readme]

The copy keeps each class of the source with all its keys.[^test_schema_rules.py]

[^readme]: README.md, Knowledge Trust Ladder (KTL)
[^justfile]: project.justfile, lokf_adapt_args
[^test_schema_rules.py]: tests/test_schema_rules.py, test_the_copy_keeps_every_class_and_key
