---
type: Playbook
id: https://w3id.org/lmodel/fix-orchestra/knowledge/playbooks/regenerate-and-test
genre: how-to
title: Regenerate and test
description: "How to change the schema: edit the words table or the XSD converter, run `just gen-schema`, `just gen-project`, `just gen-doc` and `just lokf-adapt`, then `just lint` and `just test`, and commit the output."
resource: CONTRIBUTING.md
references:
  - https://w3id.org/lmodel/fix-orchestra/knowledge/services/xsd-converter
sources:
  - id: contributing
    resource: CONTRIBUTING.md
    title: Before opening a pull request
  - resource: project.justfile
  - resource: justfile
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:53:42Z"
status: draft
---

# Regenerate and test

1. Edit `scripts/orchestra_words.yaml` or `scripts/orchestra_xsd_to_linkml.py`.
2. Run `just gen-schema`, `just gen-project`, `just gen-doc` and `just lokf-adapt`, and commit the output.[^contributing]
3. Run `just test`, which runs the schema generation, `pytest` and the examples under `tests/data/`.[^contributing]

[^contributing]: CONTRIBUTING.md, Before opening a pull request
