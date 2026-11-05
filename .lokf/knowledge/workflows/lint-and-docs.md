---
type: Service
id: https://w3id.org/lmodel/fix-orchestra/knowledge/workflows/lint-and-docs
genre: reference
title: Lint and docs (lint-and-docs.yaml)
description: "The workflow of static checks: ShellCheck, actionlint, markdownlint, lychee, codespell, and the word budgets that hold CONTRIBUTING.md to 1,000 words and SECURITY.md to 900."
resource: .github/workflows/lint-and-docs.yaml
sources:
  - id: lint
    resource: .github/workflows/lint-and-docs.yaml
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:53:42Z"
status: draft
---

# Lint and docs (lint-and-docs.yaml)

The checks touch neither the schema nor the Python tests. The workflow also runs every Monday, to find links that no longer work.[^lint]

[^lint]: .github/workflows/lint-and-docs.yaml
