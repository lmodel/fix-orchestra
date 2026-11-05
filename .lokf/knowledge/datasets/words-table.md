---
type: Dataset
id: https://w3id.org/lmodel/fix-orchestra/knowledge/datasets/words-table
genre: reference
title: The words table
description: "`scripts/orchestra_words.yaml`: this project's own title and description for every class, key and value list the schema renders, written from what each element does and not from FIX's text."
resource: scripts/orchestra_words.yaml
about:
  - https://w3id.org/lmodel/fix-orchestra/knowledge/policies/license-and-attribution
sources:
  - id: words
    resource: scripts/orchestra_words.yaml
    title: the header
  - id: test_own_words.py
    resource: tests/test_own_words.py
    title: the module's description
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:53:42Z"
status: draft
---

# The words table

A key's words come from the first entry that exists, from an override for one edition or one class down to the entry for its XML name.[^words]

A test holds that no run of four words in the schema, the words table, the README or the docs is a run of the XSDs' documentation.[^test_own_words.py]

[^words]: scripts/orchestra_words.yaml, the header
[^test_own_words.py]: tests/test_own_words.py, the module's description
