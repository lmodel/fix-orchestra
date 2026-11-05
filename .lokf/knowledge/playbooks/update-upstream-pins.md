---
type: Playbook
id: https://w3id.org/lmodel/fix-orchestra/knowledge/playbooks/update-upstream-pins
genre: how-to
title: Move to another edition
description: "What to do when the upstream watch reports a new tag, such as another release candidate or a v1.1 standard: move `upstream/`, the pins and the schema headers together, and rerun the XSD converter."
resource: scripts/check_upstream_release.py
references:
  - https://w3id.org/lmodel/fix-orchestra/knowledge/workflows/upstream-watch
  - https://w3id.org/lmodel/fix-orchestra/knowledge/datasets/upstream-copy
sources:
  - id: watch
    resource: scripts/check_upstream_release.py
    title: check_tags and EDITIONS
  - id: test_upstream.py
    resource: tests/test_upstream.py
    title: test_each_edition_module_names_its_pins
generated:
  by: process:ktl-librarian
  at: "2026-11-05T20:05:31Z"
status: draft
---

# Move to another edition

1. Read what changed, and decide whether the schema moves to the new tag.[^watch]
2. Move `upstream/`, `scripts/upstream_pins.tsv`, the watch's `EDITIONS` and the converter's `EDITIONS` together.[^watch]
3. Run `just gen-schema` and the other regeneration recipes. A module's header must name the edition, tag and commit the watch pins.[^test_upstream.py]

[^watch]: scripts/check_upstream_release.py, check_tags and EDITIONS
[^test_upstream.py]: tests/test_upstream.py, test_each_edition_module_names_its_pins
