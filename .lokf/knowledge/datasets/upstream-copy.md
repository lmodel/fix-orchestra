---
type: Dataset
id: https://w3id.org/lmodel/fix-orchestra/knowledge/datasets/upstream-copy
genre: reference
title: The copy of FIX's files
description: "`upstream/`: both editions' XSDs and licences and five of FIX's own Orchestra files, 30 files in all, each unchanged and pinned by git object hash in `scripts/upstream_pins.tsv`."
resource: upstream
derivedFrom:
  - https://w3id.org/lmodel/fix-orchestra/knowledge/references/orchestra-v1-0
  - https://w3id.org/lmodel/fix-orchestra/knowledge/references/orchestra-v1-1-rc3
  - https://w3id.org/lmodel/fix-orchestra/knowledge/references/orchestrations-repository
sources:
  - id: pins
    resource: scripts/upstream_pins.tsv
  - id: test_upstream.py
    resource: tests/test_upstream.py
    title: test_upstream_holds_only_the_pinned_files
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:53:42Z"
status: draft
---

# The copy of FIX's files

Each row of the pin table names a file's path under `upstream/`, its git object hash, its repository, the commit and its path there.[^pins]

`upstream/` holds only the pinned files, 30 of them, and each has the hash the table names.[^test_upstream.py]

[^pins]: scripts/upstream_pins.tsv
[^test_upstream.py]: tests/test_upstream.py, test_upstream_holds_only_the_pinned_files
