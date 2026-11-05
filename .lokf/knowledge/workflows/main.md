---
type: Service
id: https://w3id.org/lmodel/fix-orchestra/knowledge/workflows/main
genre: reference
title: Build and test (main.yaml)
description: The workflow that runs `just lint` and `just test` on Python 3.10 to 3.14 on every pull request and push to `main`, and checks that the adapt copy is current.
resource: .github/workflows/main.yaml
sources:
  - id: main
    resource: .github/workflows/main.yaml
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:53:42Z"
status: draft
---

# Build and test (main.yaml)

The job installs the project with `uv sync --locked`, and on Python 3.13 it also runs `just lint` and `just lokf-adapt-check`.[^main]

[^main]: .github/workflows/main.yaml
