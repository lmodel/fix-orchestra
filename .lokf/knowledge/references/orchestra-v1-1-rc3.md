---
type: Reference
id: https://w3id.org/lmodel/fix-orchestra/knowledge/references/orchestra-v1-1-rc3
genre: reference
title: FIX Orchestra v1.1 Release Candidate 3
description: "The upstream authority for the v1.1 module: FIX Orchestra v1.1 RC3 of June 2026, whose XSDs sit in FIX's code repository, FIXTradingCommunity/fix-orchestra, under the tag `v1.1-rc3`, commit `eb4bb9d`."
resource: https://github.com/FIXTradingCommunity/fix-orchestra/tree/v1.1-rc3/repository/src/main/resources/xsd
references:
  - https://w3id.org/lmodel/fix-orchestra/knowledge/datasets/upstream-copy
sources:
  - id: watch
    resource: scripts/check_upstream_release.py
    title: EDITIONS
  - id: about
    resource: docs/about.md
    title: Two editions
  - id: test_upstream.py
    resource: tests/test_upstream.py
    title: test_the_specification_repository_holds_v10_xsds_at_its_rc3_tag
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:53:42Z"
status: draft
---

# FIX Orchestra v1.1 Release Candidate 3

The watch pins the edition to the tag `v1.1-rc3` of the `fix-orchestra` code repository, which names commit `eb4bb9de3bd8802c6e5e0aba06182407b22acc9b`.[^watch]

RC3 adds scenarios, encoding standards and encoding blocks, drops v1.0's FIXML file names and category kinds, requires a category's section and caps a name at 64 characters.[^about]

The XSDs come from the code repository because, at its `v1.1-rc3` tag, the specification repository's `v1-1` folder still holds the v1.0 XSDs byte for byte.[^test_upstream.py]

[^watch]: scripts/check_upstream_release.py, EDITIONS
[^about]: docs/about.md, Two editions
[^test_upstream.py]: tests/test_upstream.py, test_the_specification_repository_holds_v10_xsds_at_its_rc3_tag
