---
type: Service
id: https://w3id.org/lmodel/fix-orchestra/knowledge/services/xml-converter
genre: reference
title: The XML converter
description: "`scripts/orchestra_xml_to_yaml.py`: converts an Orchestra repository or interfaces file to records the schema validates, picking the edition by the root's namespace, and writes records back to XML. `just to-records FILE` runs it."
resource: scripts/orchestra_xml_to_yaml.py
dependsOn:
  - https://w3id.org/lmodel/fix-orchestra/knowledge/datasets/fix-orchestra-linkml-schema
sources:
  - id: xml-converter
    resource: scripts/orchestra_xml_to_yaml.py
    title: the module's description and PARSER
  - id: test_documents.py
    resource: tests/test_documents.py
    title: test_each_document_converts_back_unchanged
generated:
  by: process:ktl-librarian
  at: "2026-11-05T20:05:31Z"
status: draft
---

# The XML converter

The converter reads the schema's `xml_attribute`, `xml_element` and `xml_choice` annotations and holds no table of its own. A name the class does not know is an error.[^xml-converter]

It leaves out the attributes that tell a parser where an XSD is, such as `xsi:schemaLocation`, and comments and processing instructions. Its parser reads no network resource and expands no entity.[^xml-converter]

Records converted back give each pinned and example file again, with every attribute, element, text and order of elements.[^test_documents.py]

[^xml-converter]: scripts/orchestra_xml_to_yaml.py, the module's description and PARSER
[^test_documents.py]: tests/test_documents.py, test_each_document_converts_back_unchanged
