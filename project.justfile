## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

_default_xml := justfile_directory() / "upstream-releases/OrchestraFIXLatest.xml"

# Regenerate LinkML Schema from upstream XSDs + FIX base datatype proto_scalar annotations
# Chains into overlay-sssom-mappings so the freshly-generated schema picks up
# any *.sssom.tsv edits in src/fix_orchestra/mappings/.
[group('model development')]
gen-linkml: && overlay-sssom-mappings
  uv run python3 scripts/schema_to_linkml.py \
    --orchestra-xml {{_default_xml}}

# Apply SSSOM mappings (src/fix_orchestra/mappings/*.sssom.tsv) onto the
# generated LinkML schema YAMLs. Idempotent.
[group('model development')]
overlay-sssom-mappings:
  uv run python3 scripts/apply_sssom_overlay.py \
    --schema-dir src/fix_orchestra/schema \
    --mappings-dir src/fix_orchestra/mappings

# Generate wire-format proto3 from FIX Orchestra XML (output: project/protobuf/fix_orchestra.wire.proto)
[group('model development')]
gen-proto-wire:
  @if [ ! -d "{{dest}}/protobuf" ]; then mkdir -p {{dest}}/protobuf ; fi
  uv run python3 scripts/fix_xml_to_proto.py \
    --input {{_default_xml}} \
    --output {{dest}}/protobuf/fix_orchestra.wire.proto

# Validate FIX Community supplied XML corpus against the LinkML schema (with per-file record counts)
[group('model development')]
test-third-party:
  uv run python -m pytest -v -s tests/test_third_party.py

