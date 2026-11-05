---
type: Reference
id: https://w3id.org/lmodel/fix-orchestra/knowledge/references/orchestrations-repository
genre: reference
title: FIX's orchestrations repository
description: "FIXTradingCommunity/orchestrations, under the Apache License 2.0: the source of FIX Latest at Extension Pack 312 and of three more Orchestra files the tests read, pinned at commit `cd24169`."
resource: https://github.com/FIXTradingCommunity/orchestrations
references:
  - https://w3id.org/lmodel/fix-orchestra/knowledge/datasets/fix-latest
sources:
  - id: pins
    resource: scripts/upstream_pins.tsv
  - id: notice
    resource: NOTICE
    title: FIX's Orchestra files
  - id: watch
    resource: scripts/check_upstream_release.py
    title: check_default_branches
generated:
  by: process:ktl-librarian
  at: "2026-11-05T20:05:31Z"
status: draft
---

# FIX's orchestrations repository

The repository gives four of the files under `upstream/documents/`: `OrchestraFIXLatest.xml`, `FIXTSession.xml`, `FIX44Session.xml` and `TradingDigitalAssets.xml`, each pinned at commit `cd24169a2abd8daba7c360987c7a46ca11873a12`.[^pins]

The files are under the Apache License 2.0, though the metadata of `OrchestraFIXLatest.xml` says "All Rights Reserved". The repository copies them whole and unchanged.[^notice]

The watch reports a newer file on the default branch for information only, because the files are test data.[^watch]

[^pins]: scripts/upstream_pins.tsv
[^notice]: NOTICE, FIX's Orchestra files
[^watch]: scripts/check_upstream_release.py, check_default_branches
