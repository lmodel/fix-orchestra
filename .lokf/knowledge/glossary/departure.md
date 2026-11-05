---
type: GlossaryTerm
id: https://w3id.org/lmodel/fix-orchestra/knowledge/glossary/departure
title: Departure
description: "A departure: a place where a real FIX file breaks one of this project's rules, listed by file and JSON pointer in `tests/document_departures.yaml` so a test expects it."
relatedTo:
  - https://w3id.org/lmodel/fix-orchestra/knowledge/datasets/document-departures
sources:
  - id: departures
    resource: tests/document_departures.yaml
    title: the header
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:53:42Z"
status: draft
---

# Departure

A change in either the document or the rules fails the test that expects each departure.[^departures]

[^departures]: tests/document_departures.yaml, the header
