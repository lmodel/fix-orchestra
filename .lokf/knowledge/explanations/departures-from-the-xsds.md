---
type: Explanation
id: https://w3id.org/lmodel/fix-orchestra/knowledge/explanations/departures-from-the-xsds
genre: explanation
title: Where the schema departs from the XSDs
description: "The two places the schema and its rules differ from the XSDs: RC3's `fieldTypeOrCodeSetKey`, whose uniqueness the rules leave out, and the keys and references that only the rules check."
resource: docs/about.md
references:
  - https://w3id.org/lmodel/fix-orchestra/knowledge/datasets/orchestra-rules
sources:
  - id: about
    resource: docs/about.md
    title: Where the schema departs from the XSDs
  - id: test_documents.py
    resource: tests/test_documents.py
    title: test_rc3_refuses_two_fields_of_one_datatype_and_the_schema_does_not
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:53:42Z"
status: draft
---

# Where the schema departs from the XSDs

RC3's `fieldTypeOrCodeSetKey` is a key on a field's type or code set, so it refuses a second field of the same datatype, which every real repository has.[^about]

The XSD refuses a repository with two fields of one datatype, and the schema and the rules accept it.[^test_documents.py]

[^about]: docs/about.md, Where the schema departs from the XSDs
[^test_documents.py]: tests/test_documents.py, test_rc3_refuses_two_fields_of_one_datatype_and_the_schema_does_not
