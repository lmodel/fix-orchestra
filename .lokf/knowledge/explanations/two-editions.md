---
type: Explanation
id: https://w3id.org/lmodel/fix-orchestra/knowledge/explanations/two-editions
genre: explanation
title: Why the schema has two editions
description: "Why v1.0 and v1.1 RC3 are separate modules with suffixed class names: neither edition is a superset of the other, and FIX Latest is published in v1.0."
resource: docs/about.md
about:
  - https://w3id.org/lmodel/fix-orchestra/knowledge/glossary/edition
sources:
  - id: about
    resource: docs/about.md
    title: Two editions
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:53:42Z"
status: draft
---

# Why the schema has two editions

RC3 adds scenarios, encoding standards and encoding blocks, drops v1.0's FIXML file names and category kinds, requires a category's section and caps a name at 64 characters.[^about]

So each edition is a module of its own, and each class carries its edition's suffix, as in `OrchestraMessageV10` and `OrchestraMessageV11`.[^about]

[^about]: docs/about.md, Two editions
