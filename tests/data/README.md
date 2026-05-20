# Example data for fix_orchestra

This folder contains example data for testing and demonstrating the
datamodel, sorted into subfolders:

- `valid/` - data conforming to the datamodel. Used to verify the datamodel
  (`test_data.py::test_valid_data_files`).
- `invalid/` - data intentionally violating the datamodel. Used to verify
  validation surfaces the breach
  (`test_data.py::test_invalid_data_files`).
- `problem/` - data not yet handled correctly in the current schema version,
  separated into `valid/` and `invalid/` again. Excluded from the test
  suite until the underlying issue is resolved.
- `third_party/fix-orchestra/` - real-world XML samples from the FIX Trading
  Community reference implementation. Exercised by
  `test_third_party.py` (XML -> YAML conversion via
  `scripts/fix_xml_to_linkml.py`, then `linkml-validate`). See its
  [README](third_party/fix-orchestra/README.md) for provenance and the
  per-file error budget.

## Filename convention

Files in `valid/` and `invalid/` must be named `<ClassName>-<desc>.yaml`.
The class name is derived by splitting on the first `-` and taking the
part before it; it must match a class in the LinkML schema. `<desc>` can
be any filename-safe identifier (e.g. `Repository-minimal.yaml`,
`FieldType-missing-id.yaml`).
