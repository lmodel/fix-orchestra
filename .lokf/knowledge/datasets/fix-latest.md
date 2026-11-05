---
type: Dataset
id: https://w3id.org/lmodel/fix-orchestra/knowledge/datasets/fix-latest
genre: reference
title: FIX Latest EP312
description: "`upstream/documents/OrchestraFIXLatest.xml`: FIX Latest as of Extension Pack 312, a v1.0 Orchestra repository of 181 messages and 6,203 fields that the tests validate with the XSD and the schema and convert back unchanged."
resource: upstream/documents/OrchestraFIXLatest.xml
isPartOf:
  - https://w3id.org/lmodel/fix-orchestra/knowledge/datasets/upstream-copy
derivedFrom:
  - https://w3id.org/lmodel/fix-orchestra/knowledge/references/orchestrations-repository
sources:
  - id: test_documents.py
    resource: tests/test_documents.py
    title: test_the_records_are_the_xml_text and test_rc3_and_the_schema_agree_on_fix_latest_moved_to_rc3
  - id: test_datamodel.py
    resource: tests/test_datamodel.py
    title: test_fix_latest_loads_into_the_pydantic_models
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:53:42Z"
status: draft
---

# FIX Latest EP312

The file's version is `FIX.Latest_EP312`, and its records load into the Pydantic models with 181 messages and 6,203 fields.[^test_datamodel.py]

RC3 cannot hold the file as it is: one group name, `UnderlyingPaymentStreamNonDeliverableFixingDatesBusinessCenterGrp`, has 65 characters, more than RC3's 64.[^test_documents.py]

[^test_documents.py]: tests/test_documents.py, test_the_records_are_the_xml_text and test_rc3_and_the_schema_agree_on_fix_latest_moved_to_rc3
[^test_datamodel.py]: tests/test_datamodel.py, test_fix_latest_loads_into_the_pydantic_models
