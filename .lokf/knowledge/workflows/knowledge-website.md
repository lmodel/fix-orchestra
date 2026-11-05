---
type: Service
id: https://w3id.org/lmodel/fix-orchestra/knowledge/workflows/knowledge-website
genre: reference
title: Knowledge website (knowledge-website.yaml)
description: The workflow that builds the documentation site and deploys it to GitHub Pages from `main`, once `KNOWLEDGE_WEBSITE_ENABLED` is `true`.
resource: .github/workflows/knowledge-website.yaml
references:
  - https://w3id.org/lmodel/fix-orchestra/knowledge/services/documentation-site
sources:
  - id: security
    resource: SECURITY.md
    title: What executes here
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:53:42Z"
status: draft
---

# Knowledge website (knowledge-website.yaml)

The build holds no write token, and only the deploy job holds `pages: write` and `id-token: write`.[^security]

[^security]: SECURITY.md, What executes here
