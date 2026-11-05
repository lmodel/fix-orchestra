---
type: Dataset
id: https://w3id.org/lmodel/fix-orchestra/knowledge/datasets/document-departures
genre: reference
title: Where FIX's files break a rule
description: "`tests/document_departures.yaml`: each rule a real FIX file breaks, by file and JSON pointer. FIX's two session files put groups in a category named Common, which neither defines."
resource: tests/document_departures.yaml
about:
  - https://w3id.org/lmodel/fix-orchestra/knowledge/glossary/departure
sources:
  - id: departures
    resource: tests/document_departures.yaml
  - id: test_documents.py
    resource: tests/test_documents.py
    title: test_each_document_keeps_the_rules
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:53:42Z"
status: draft
---

# Where FIX's files break a rule

`FIX44Session.xml` puts one group in the category Common, and `FIXTSession.xml` puts three there, and neither file defines that category.[^departures]

A document breaks no rule except the ones this file lists.[^test_documents.py]

[^departures]: tests/document_departures.yaml
[^test_documents.py]: tests/test_documents.py, test_each_document_keeps_the_rules
