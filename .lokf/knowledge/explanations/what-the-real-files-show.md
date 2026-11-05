---
type: Explanation
id: https://w3id.org/lmodel/fix-orchestra/knowledge/explanations/what-the-real-files-show
genre: explanation
title: What the real files show
description: "What FIX's own Orchestra files show when the schema reads them: FIX Latest's three categories without a section, the session files' undefined category, the 65-character group name RC3 refuses, and the v1.0 XSDs in the RC3 tag."
resource: docs/about.md
references:
  - https://w3id.org/lmodel/fix-orchestra/knowledge/datasets/fix-latest
  - https://w3id.org/lmodel/fix-orchestra/knowledge/datasets/document-departures
sources:
  - id: about
    resource: docs/about.md
    title: What the real files show
  - id: test_documents.py
    resource: tests/test_documents.py
    title: test_a_v10_category_may_have_no_section
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:53:42Z"
status: draft
---

# What the real files show

FIX Latest leaves the section out of three categories, Common, Fields and ImplFields. That is valid in v1.0, and RC3 is the edition that requires a section.[^test_documents.py]

No published RC3 file is valid against RC3's XSDs.[^about]

[^about]: docs/about.md, What the real files show
[^test_documents.py]: tests/test_documents.py, test_a_v10_category_may_have_no_section
