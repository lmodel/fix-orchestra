---
type: Service
id: https://w3id.org/lmodel/fix-orchestra/knowledge/workflows/knowledge-librarian
genre: reference
title: Knowledge librarian (knowledge-librarian.yaml)
description: The scheduled workflow that runs the ktl-librarian skill as an agent and opens a pull request with its patch, inert until `KNOWLEDGE_LIBRARIAN_ENABLED` is `true`.
resource: .github/workflows/knowledge-librarian.yaml
sources:
  - id: security
    resource: SECURITY.md
    title: What executes here
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:53:42Z"
status: draft
---

# Knowledge librarian (knowledge-librarian.yaml)

The agent's job holds no write token, and the `publish` job runs no agent, confines the patch to the bundle and refuses a `human:` claim.[^security]

[^security]: SECURITY.md, What executes here
