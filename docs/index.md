# fix-orchestra

This project is a LinkML model of FIX Orchestra, the FIX Trading Community's standard for rules of engagement that a machine can read. It renders two editions from their XSDs, the v1.0 Technical Standard and the v1.1 third release candidate, and converts an Orchestra file to records and back.

- [Schema documentation](elements/index.md), generated from the schema
- [About](about.md): how the schema reads the XSDs, where it departs from them and what the real files show
- [`fix_orchestra.yaml`](schema/fix_orchestra.yaml): the schema, with its modules merged

## Validating an Orchestra file

The converter reads the file's namespace to pick the edition, and writes its records:

```bash
just to-records upstream/documents/FIXTSession.xml > fixt.yaml
uv run linkml-validate -s src/fix_orchestra/schema/fix_orchestra.yaml -C OrchestraRepositoryV10 fixt.yaml
```

A repository is `OrchestraRepositoryV10` or `OrchestraRepositoryV11`, and an interfaces file `OrchestraInterfacesV10` or `OrchestraInterfacesV11`. `project/jsonschema/fix_orchestra.schema.json` is the same schema for anyone without LinkML. `tests/orchestra_rules.py` adds what a validator cannot state, such as that a field's number is unique and that a message uses fields the file defines.

`uv run python scripts/orchestra_xml_to_yaml.py --to-xml fixt.yaml` writes the file back.
