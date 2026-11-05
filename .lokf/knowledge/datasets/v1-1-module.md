---
type: Dataset
id: https://w3id.org/lmodel/fix-orchestra/knowledge/datasets/v1-1-module
genre: reference
title: The v1.1 RC3 module
description: "`src/fix_orchestra/schema/fix_orchestra_v1_1.yaml`: 84 classes for Orchestra v1.1 RC3's repository and interfaces XSDs, among them 5 mixins and 9 member classes, each name ending in `V11`, which the XSD converter writes."
resource: src/fix_orchestra/schema/fix_orchestra_v1_1.yaml
isPartOf:
  - https://w3id.org/lmodel/fix-orchestra/knowledge/datasets/fix-orchestra-linkml-schema
derivedFrom:
  - https://w3id.org/lmodel/fix-orchestra/knowledge/references/orchestra-v1-1-rc3
sources:
  - id: v11-module
    resource: src/fix_orchestra/schema/fix_orchestra_v1_1.yaml
  - id: about
    resource: docs/about.md
    title: Two editions
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:53:42Z"
status: draft
---

# The v1.1 RC3 module

The module imports `linkml:types` and `fix_orchestra_common`, and its annotations name the tag `v1.1-rc3`, its commit, and the namespaces `http://fixprotocol.io/2026/orchestra/repository` and `http://fixprotocol.io/2026/orchestra/interfaces`.[^v11-module]

Its classes for scenarios, encoding standards and encoding blocks have no counterpart in v1.0.[^about]

[^v11-module]: src/fix_orchestra/schema/fix_orchestra_v1_1.yaml
[^about]: docs/about.md, Two editions
