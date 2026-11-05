---
type: Service
id: https://w3id.org/lmodel/fix-orchestra/knowledge/workflows/upstream-watch
genre: reference
title: Upstream watch (upstream-watch.yaml)
description: "The weekly check that `scripts/check_upstream_release.py` runs: a new tag in FIX's repositories, a moved tag, a changed or missing pinned file, or a changed licence opens or updates an issue."
resource: .github/workflows/upstream-watch.yaml
references:
  - https://w3id.org/lmodel/fix-orchestra/knowledge/playbooks/update-upstream-pins
  - https://w3id.org/lmodel/fix-orchestra/knowledge/datasets/upstream-copy
sources:
  - id: check
    resource: scripts/check_upstream_release.py
    title: the module's description
  - id: watch-workflow
    resource: .github/workflows/upstream-watch.yaml
    title: the header
  - resource: .github/scripts/report-issue.sh
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:53:42Z"
status: draft
---

# Upstream watch (upstream-watch.yaml)

The script reads only GitHub's API, compares git object hashes and downloads no file.[^check]

A failing check fails the run and opens an issue, or comments on the one already open.[^watch-workflow]

[^check]: scripts/check_upstream_release.py, the module's description
[^watch-workflow]: .github/workflows/upstream-watch.yaml, the header
