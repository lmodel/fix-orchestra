# Example data for fix-orchestra

- `xml/` holds four Orchestra files this project wrote for its tests, a repository and an interfaces file for each edition, with one of each kind of element the XSDs define. `tests/test_documents.py` validates each with the pinned XSD and the schema.
- `valid/` holds an example of each class, taken from those files, and three small whole files for the rule tests. `linkml-run-examples` and `tests/test_data.py` read this folder.
- `invalid/` holds a counter-example for each kind of constraint the validator can state. Each file's first line, `# Fails at: <JSON pointer>`, names its one failing place, and `tests/test_data.py` checks that it fails there.
- `problem/invalid/` holds a counter-example for each rule the generated JSON Schema cannot state, which `tests/orchestra_rules.py` checks over a whole file.

A file name is `ClassName-anything.yaml`, and the class is the part before the first hyphen. The real files the tests read are under `upstream/documents/`.
