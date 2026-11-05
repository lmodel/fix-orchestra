---
type: Dataset
id: https://w3id.org/lmodel/fix-orchestra/knowledge/datasets/fix-orchestra-linkml-schema
genre: reference
title: The fix-orchestra LinkML schema
description: "`src/fix_orchestra/schema/`: the umbrella `fix_orchestra.yaml` over `fix_orchestra_common`, `fix_orchestra_v1_0` and `fix_orchestra_v1_1`, a LinkML model of FIX Orchestra's repository and interfaces files in two editions, with four tree roots."
resource: src/fix_orchestra/schema/fix_orchestra.yaml
hasPart:
  - https://w3id.org/lmodel/fix-orchestra/knowledge/datasets/common-module
  - https://w3id.org/lmodel/fix-orchestra/knowledge/datasets/v1-0-module
  - https://w3id.org/lmodel/fix-orchestra/knowledge/datasets/v1-1-module
derivedFrom:
  - https://w3id.org/lmodel/fix-orchestra/knowledge/references/orchestra-v1-0
  - https://w3id.org/lmodel/fix-orchestra/knowledge/references/orchestra-v1-1-rc3
sources:
  - id: umbrella
    resource: src/fix_orchestra/schema/fix_orchestra.yaml
    title: the header
  - id: generators
    resource: .linkml/generators.yaml
    title: jsonschema
  - id: index
    resource: docs/index.md
    title: Validating an Orchestra file
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:53:42Z"
status: draft
---

# The fix-orchestra LinkML schema

The umbrella's `version` is `1.0, 1.1-rc3`, and its annotations name each edition's repository, tag and commit.[^umbrella]

The four tree roots are `OrchestraRepositoryV10`, `OrchestraRepositoryV11`, `OrchestraInterfacesV10` and `OrchestraInterfacesV11`. The generated JSON Schema's root takes a v1.0 repository, and its `$defs` hold the other three.[^generators]

A repository is validated as `OrchestraRepositoryV10` or `OrchestraRepositoryV11`, and an interfaces file as `OrchestraInterfacesV10` or `OrchestraInterfacesV11`.[^index]

[^umbrella]: src/fix_orchestra/schema/fix_orchestra.yaml, the header
[^generators]: .linkml/generators.yaml, jsonschema
[^index]: docs/index.md, Validating an Orchestra file
