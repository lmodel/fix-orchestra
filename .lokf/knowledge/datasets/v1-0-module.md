---
type: Dataset
id: https://w3id.org/lmodel/fix-orchestra/knowledge/datasets/v1-0-module
genre: reference
title: The v1.0 module
description: "`src/fix_orchestra/schema/fix_orchestra_v1_0.yaml`: 77 classes for Orchestra v1.0's repository and interfaces XSDs, among them 5 mixins and 9 member classes, each name ending in `V10`, which the XSD converter writes."
resource: src/fix_orchestra/schema/fix_orchestra_v1_0.yaml
isPartOf:
  - https://w3id.org/lmodel/fix-orchestra/knowledge/datasets/fix-orchestra-linkml-schema
derivedFrom:
  - https://w3id.org/lmodel/fix-orchestra/knowledge/references/orchestra-v1-0
sources:
  - id: v10-module
    resource: src/fix_orchestra/schema/fix_orchestra_v1_0.yaml
  - id: test_coverage.py
    resource: tests/test_coverage.py
    title: test_each_attribute_and_element_of_the_xsd_has_its_key
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:53:42Z"
status: draft
---

# The v1.0 module

The module imports `linkml:types` and `fix_orchestra_common`, and its annotations name the tag `v1.0`, its commit, and the namespaces `http://fixprotocol.io/2020/orchestra/repository` and `http://fixprotocol.io/2020/orchestra/interfaces`.[^v10-module]

Each class has a key for each attribute and child element of the XSD type it renders, under the same XML name, required exactly when the XSD requires it.[^test_coverage.py]

[^v10-module]: src/fix_orchestra/schema/fix_orchestra_v1_0.yaml
[^test_coverage.py]: tests/test_coverage.py, test_each_attribute_and_element_of_the_xsd_has_its_key
