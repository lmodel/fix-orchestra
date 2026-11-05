---
type: Reference
id: https://w3id.org/lmodel/fix-orchestra/knowledge/references/orchestra-v1-0
genre: reference
title: FIX Orchestra v1.0, the Technical Standard
description: "The upstream authority for the v1.0 module: FIX Orchestra v1.0, promoted to Technical Standard in February 2021, whose XSDs sit in FIXTradingCommunity/fix-orchestra-spec under the tag `v1.0`, commit `e2b65db`. FIX Latest is published in this edition."
resource: https://github.com/FIXTradingCommunity/fix-orchestra-spec/tree/v1.0/v1-0-STANDARD/resources
references:
  - https://w3id.org/lmodel/fix-orchestra/knowledge/datasets/upstream-copy
sources:
  - id: watch
    resource: scripts/check_upstream_release.py
    title: EDITIONS
  - id: about
    resource: docs/about.md
    title: Two editions
  - id: notice
    resource: NOTICE
    title: FIX Orchestra XSDs
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:53:42Z"
status: draft
---

# FIX Orchestra v1.0, the Technical Standard

The watch pins the edition to the tag `v1.0` of `fix-orchestra-spec`, which names commit `e2b65db8505244f2708c468fe7cad60855fa9834`.[^watch]

Version 1.0 became a Technical Standard in February 2021, and FIX Latest is published in it.[^about]

Each XSD names the CC BY-ND 4.0 licence, so the repository copies the XSDs unchanged and writes its descriptions in its own words.[^notice]

[^watch]: scripts/check_upstream_release.py, EDITIONS
[^about]: docs/about.md, Two editions
[^notice]: NOTICE, FIX Orchestra XSDs
