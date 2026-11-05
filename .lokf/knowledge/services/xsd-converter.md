---
type: Service
id: https://w3id.org/lmodel/fix-orchestra/knowledge/services/xsd-converter
genre: reference
title: The XSD converter
description: "`scripts/orchestra_xsd_to_linkml.py`: reads both editions' XSDs under `upstream/` and the words table, and writes the schema's four modules. `just gen-schema` runs it, and it stops on any XSD construct or name it has no rule or words for."
resource: scripts/orchestra_xsd_to_linkml.py
references:
  - https://w3id.org/lmodel/fix-orchestra/knowledge/datasets/v1-0-module
  - https://w3id.org/lmodel/fix-orchestra/knowledge/datasets/v1-1-module
  - https://w3id.org/lmodel/fix-orchestra/knowledge/datasets/common-module
  - https://w3id.org/lmodel/fix-orchestra/knowledge/datasets/words-table
sources:
  - id: xsd-converter
    resource: scripts/orchestra_xsd_to_linkml.py
    title: the module's description
  - id: test_converter.py
    resource: tests/test_converter.py
    title: test_the_modules_are_the_converters_output
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:53:42Z"
status: draft
---

# The XSD converter

An attribute group becomes a mixin, an element with an anonymous type a class, and a repeated choice a list of one-key members, so the order of a message's fields survives.[^xsd-converter]

Every description comes from the words table, and no XSD documentation is copied.[^xsd-converter]

A test fails when the committed modules differ from what the converter writes.[^test_converter.py]

[^xsd-converter]: scripts/orchestra_xsd_to_linkml.py, the module's description
[^test_converter.py]: tests/test_converter.py, test_the_modules_are_the_converters_output
