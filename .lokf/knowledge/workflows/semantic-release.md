---
type: Service
id: https://w3id.org/lmodel/fix-orchestra/knowledge/workflows/semantic-release
genre: reference
title: Semantic release (semantic-release.yml)
description: The workflow that, on a push to `main`, promotes the changelog's `[Unreleased]` section, tags `vX.Y.Z`, publishes the GitHub Release and dispatches the knowledge release.
resource: .github/workflows/semantic-release.yml
sources:
  - id: contributing
    resource: CONTRIBUTING.md
    title: Releasing (maintainers)
  - resource: .github/workflows/semantic-release.yml
  - resource: .github/scripts/changelog-release.mjs
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:53:42Z"
status: draft
---

# Semantic release (semantic-release.yml)

The step runs behind the `release` GitHub Environment, and only `feat:`, `fix:`, `security:` and a breaking `!` start a release.[^contributing]

[^contributing]: CONTRIBUTING.md, Releasing (maintainers)
