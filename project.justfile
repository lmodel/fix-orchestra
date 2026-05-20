## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# Regenerate src/fix_orchestra/schema/fix_orchestra.yaml from upstream-releases/*.xsd
[group('model development')]
gen-linkml:
  uv run python scripts/schema_to_linkml.py

# Validate FIX Community supplied XML corpus against the LinkML schema (with per-file record counts)
[group('model development')]
test-third-party:
  uv run python -m pytest -v -s tests/test_third_party.py

