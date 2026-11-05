---
type: Dataset
id: https://w3id.org/lmodel/fix-orchestra/knowledge/datasets/example-data
genre: reference
title: The example data
description: "`tests/data/`: a valid example of each class, taken from the example files, three small whole files for the rule tests, a counter-example per kind of constraint, and a counter-example per rule the JSON Schema cannot state."
resource: tests/data
hasPart:
  - https://w3id.org/lmodel/fix-orchestra/knowledge/datasets/example-files
sources:
  - id: data-readme
    resource: tests/data/README.md
  - id: test_data.py
    resource: tests/test_data.py
    title: test_counter_examples_fail_where_they_say
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:53:42Z"
status: draft
---

# The example data

A file name is `ClassName-anything.yaml`, and the class is the part before the first hyphen.[^data-readme]

Every counter-example fails at the place its first line names, as `# Fails at: <JSON pointer>`, and at no other place except along the path to it.[^test_data.py]

[^data-readme]: tests/data/README.md
[^test_data.py]: tests/test_data.py, test_counter_examples_fail_where_they_say
