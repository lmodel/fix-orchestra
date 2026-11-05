---
type: Dataset
id: https://w3id.org/lmodel/fix-orchestra/knowledge/datasets/neighbour-copies
genre: reference
title: The neighbours' copies
description: "`tests/neighbours/`: the schema assets of 30 released lmodel repositories, each checked against its release's `.sha256` and attestation, against which the adapt copy is held to share no class or key."
resource: tests/neighbours
sources:
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
    title: NEIGHBOURS and test_names_apart_from_neighbours
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:53:42Z"
status: draft
---

# The neighbours' copies

Each copy is pinned by its SHA-256. The adapt copy shares no class, enum, type or subset name with any of them, and no key under another IRI.[^test_schema_rules.py]

[^test_schema_rules.py]: tests/test_schema_rules.py, NEIGHBOURS and test_names_apart_from_neighbours
