---
type: Dataset
id: https://w3id.org/lmodel/fix-orchestra/knowledge/datasets/generated-artefacts
genre: reference
title: The generated artefacts
description: "`project/`, `src/fix_orchestra/datamodel/` and `docs/schema/`: what `just gen-project` and `just gen-doc` write from the schema, such as the JSON Schema, the Pydantic models and the OWL, never edited by hand."
resource: project
derivedFrom:
  - https://w3id.org/lmodel/fix-orchestra/knowledge/datasets/fix-orchestra-linkml-schema
sources:
  - id: generators
    resource: .linkml/generators.yaml
    title: excludes
  - id: test_generated_json_schema.py
    resource: tests/test_generated_json_schema.py
    title: test_the_committed_file_is_the_generators_output
  - resource: src/fix_orchestra/datamodel
  - resource: docs/schema
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:53:42Z"
status: draft
---

# The generated artefacts

The SQL table generator is off, because it writes a join table per multivalued slot per class.[^generators]

A schema edit without `just gen-project` fails a test, which compares the committed JSON Schema with the generator's output.[^test_generated_json_schema.py]

[^generators]: .linkml/generators.yaml, excludes
[^test_generated_json_schema.py]: tests/test_generated_json_schema.py, test_the_committed_file_is_the_generators_output
