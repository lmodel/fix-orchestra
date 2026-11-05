---
type: Service
id: https://w3id.org/lmodel/fix-orchestra/knowledge/workflows/knowledge-release
genre: reference
title: Knowledge release (knowledge-release.yaml)
description: The workflow that attaches the schema's adapt copy, the bundle zip and a Microsoft 365 Copilot skill zip to a release, each with its `.sha256` and a build-provenance attestation.
resource: .github/workflows/knowledge-release.yaml
sources:
  - id: security
    resource: SECURITY.md
    title: What this repository releases
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:53:42Z"
status: draft
---

# Knowledge release (knowledge-release.yaml)

The workflow attaches the assets when the bundle or the schema has changed.[^security]

[^security]: SECURITY.md, What this repository releases
