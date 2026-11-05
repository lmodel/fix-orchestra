---
type: Playbook
id: https://w3id.org/lmodel/fix-orchestra/knowledge/playbooks/validate-an-orchestra-file
genre: how-to
title: Validate an Orchestra file
description: "How to check an Orchestra file against the schema: convert it with `just to-records`, validate the records with `linkml-validate` as the edition's repository or interfaces class, and convert them back with `--to-xml`."
resource: docs/index.md
references:
  - https://w3id.org/lmodel/fix-orchestra/knowledge/services/xml-converter
sources:
  - id: index
    resource: docs/index.md
    title: Validating an Orchestra file
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:53:42Z"
status: draft
---

# Validate an Orchestra file

1. Convert the file: `just to-records upstream/documents/FIXTSession.xml > fixt.yaml`.[^index]
2. Validate the records: `uv run linkml-validate -s src/fix_orchestra/schema/fix_orchestra.yaml -C OrchestraRepositoryV10 fixt.yaml`.[^index]
3. Write the file back with `uv run python scripts/orchestra_xml_to_yaml.py --to-xml fixt.yaml`.[^index]

[^index]: docs/index.md, Validating an Orchestra file
