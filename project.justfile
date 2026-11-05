## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# Rewrite the schema's modules from the XSDs under upstream/ and the words in
# scripts/orchestra_words.yaml.
[group('model development')]
gen-schema:
  uv run python scripts/orchestra_xsd_to_linkml.py

# Convert an Orchestra file to records the schema validates, written to stdout.
[group('model development')]
to-records file:
  uv run python scripts/orchestra_xml_to_yaml.py {{file}}
