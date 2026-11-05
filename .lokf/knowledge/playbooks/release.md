---
type: Playbook
id: https://w3id.org/lmodel/fix-orchestra/knowledge/playbooks/release
genre: how-to
title: Release
description: "How a release happens: a merge to `main` with a `feat:`, `fix:` or `security:` commit makes semantic-release promote the changelog, tag `vX.Y.Z` and publish the GitHub Release, from a `v0.0.0` baseline tag."
resource: CONTRIBUTING.md
references:
  - https://w3id.org/lmodel/fix-orchestra/knowledge/workflows/semantic-release
  - https://w3id.org/lmodel/fix-orchestra/knowledge/workflows/knowledge-release
sources:
  - id: contributing
    resource: CONTRIBUTING.md
    title: Releasing (maintainers)
  - resource: .releaserc.json
  - resource: CHANGELOG.md
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:53:42Z"
status: draft
---

# Release

1. Write `## [Unreleased]` in `CHANGELOG.md` as you go, since the release job refuses an empty one.[^contributing]
2. Push the `v0.0.0` baseline tag on `main` before the first releasing merge, which then releases 0.1.0.[^contributing]
3. Merge. `semantic-release.yml` retitles the section, tags `vX.Y.Z` and publishes the release, and then dispatches the knowledge release when `KNOWLEDGE_RELEASE_ENABLED` is `true`.[^contributing]

[^contributing]: CONTRIBUTING.md, Releasing (maintainers)
