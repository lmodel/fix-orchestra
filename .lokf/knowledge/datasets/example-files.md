---
type: Dataset
id: https://w3id.org/lmodel/fix-orchestra/knowledge/datasets/example-files
genre: reference
title: The example Orchestra files
description: "`tests/data/xml/`: four Orchestra files this project wrote, a repository and an interfaces file for each edition, with one of each kind of element the XSDs define, since no published RC3 file is valid against RC3's XSDs."
resource: tests/data/xml
sources:
  - id: data-readme
    resource: tests/data/README.md
  - id: about
    resource: docs/about.md
    title: What the real files show
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:53:42Z"
status: draft
---

# The example Orchestra files

The tests validate each file with the pinned XSD and the schema.[^data-readme]

No published RC3 file is valid against RC3's XSDs, so these are the v1.1 module's whole files.[^about]

[^data-readme]: tests/data/README.md
[^about]: docs/about.md, What the real files show
