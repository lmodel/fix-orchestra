---
type: GlossaryTerm
id: https://w3id.org/lmodel/fix-orchestra/knowledge/glossary/member
title: Member
description: "A member: one item of a repeated XSD choice, such as a field, component or group in a message's structure, held as an object with exactly one key so the list keeps the elements' order."
relatedTo:
  - https://w3id.org/lmodel/fix-orchestra/knowledge/explanations/how-the-schema-reads-an-xsd
sources:
  - id: test_generated_json_schema.py
    resource: tests/test_generated_json_schema.py
    title: test_a_member_holds_exactly_one_element
generated:
  by: process:ktl-librarian
  at: "2026-11-05T20:05:31Z"
status: draft
---

# Member

The generated JSON Schema writes a member as a `oneOf`, one branch per element it may hold.[^test_generated_json_schema.py]

[^test_generated_json_schema.py]: tests/test_generated_json_schema.py, test_a_member_holds_exactly_one_element
