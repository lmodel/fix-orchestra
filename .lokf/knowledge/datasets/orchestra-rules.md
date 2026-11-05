---
type: Dataset
id: https://w3id.org/lmodel/fix-orchestra/knowledge/datasets/orchestra-rules
genre: reference
title: The rules a validator cannot state
description: "`tests/orchestra_rules.py`: the XSDs' `xs:key` and `xs:keyref` constraints and the references the specification describes, checked over a whole file, which JSON Schema cannot state."
resource: tests/orchestra_rules.py
sources:
  - id: rules
    resource: tests/orchestra_rules.py
    title: the module's description
generated:
  by: process:ktl-librarian
  at: "2026-11-05T20:05:31Z"
status: draft
---

# The rules a validator cannot state

`rule_errors` returns each error as a JSON pointer and a sentence.[^rules]

RC3's `fieldTypeOrCodeSetKey` refuses two fields that share a datatype, so the rule keeps what it asks of one field, a datatype or else a code set, never both, and leaves out the uniqueness.[^rules]

[^rules]: tests/orchestra_rules.py, the module's description
