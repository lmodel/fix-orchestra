---
type: Service
id: https://w3id.org/lmodel/fix-orchestra/knowledge/workflows/knowledge-registrar
genre: reference
title: Knowledge registrar (knowledge-registrar.yaml)
description: "The gate that checks the bundle's form on every pull request that touches `.lokf/`: `lokf validate --check-refs` and the conventions script."
resource: .github/workflows/knowledge-registrar.yaml
sources:
  - id: security
    resource: SECURITY.md
    title: What executes here
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:53:42Z"
status: draft
---

# Knowledge registrar (knowledge-registrar.yaml)

The job is read-only and runs on any pull request that touches `.lokf/`.[^security]

[^security]: SECURITY.md, What executes here
