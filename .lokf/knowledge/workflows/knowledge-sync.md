---
type: Service
id: https://w3id.org/lmodel/fix-orchestra/knowledge/workflows/knowledge-sync
genre: reference
title: Knowledge sync (knowledge-sync.yaml)
description: The workflow that copies the KTL sidecar's scripts and workflows from a newer KTL release into this repository, as a pull request.
resource: .github/workflows/knowledge-sync.yaml
sources:
  - id: contributing
    resource: CONTRIBUTING.md
    title: Before opening a pull request
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:53:42Z"
status: draft
---

# Knowledge sync (knowledge-sync.yaml)

When the skills pin moves, the other knowledge workflows and `.lokf/scripts/` and `.lokf/m365/` move with it from that release's templates.[^contributing]

[^contributing]: CONTRIBUTING.md, Before opening a pull request
