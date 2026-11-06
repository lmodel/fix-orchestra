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

# ============ Knowledge bundle: the adapted domain schema ============

# `.lokf/schema/fix-orchestra.yaml` is the copy `lokf adapt` writes from the schema so that
# it can sit beside `.lokf/schema/lokf.yaml` (`lokf adapt --help` lists the moves). The roots
# are the classes a concept may name as its `type`, in each edition: a repository or
# interfaces file, and the named elements a host documents, such as a message, a field
# or a session. Every class under a root, such as OrchestraServiceV10 under
# OrchestraProtocolV10, is a concept type too. Each --keep names a Dublin Core key whose
# IRI one of LOKF's slots also takes, for a concept, where this one takes text. The
# recipes run the `lokf` the sidecar's floor pins (0.9.0 or later); LOKF_CMD runs
# another, such as a checkout: LOKF_CMD="uv run --project ../lokf lokf" just lokf-adapt
lokf_cmd := env_var_or_default("LOKF_CMD", "uv run --project .lokf lokf")
lokf_roots_each := "Repository Interfaces Actor Flow StateMachine Category Section Datatype CodeSet Field Component Group Message Concept BaseInterface Protocol"
lokf_roots_v11 := "Scenario EncodingStandard"
lokf_keep := "source relation is_replaced_by requires is_part_of references"
lokf_adapt_args := shell('for e in V10 V11; do for c in $1; do printf -- "--root Orchestra%s%s " "$c" "$e"; done; done; for c in $2; do printf -- "--root Orchestra%sV11 " "$c"; done; for k in $3; do printf -- "--keep OrchestraMetadata.dcterms_%s " "$k"; done; printf -- "--prefix fix_orchestra"', lokf_roots_each, lokf_roots_v11, lokf_keep)

# Rewrite .lokf/schema/fix-orchestra.yaml from the schema (run after every schema change)
[group('knowledge bundle')]
lokf-adapt:
  {{lokf_cmd}} adapt {{source_schema_path}} {{lokf_adapt_args}} --lokf .lokf/schema/lokf.yaml -o .lokf/schema/fix-orchestra.yaml

# Fail when .lokf/schema/fix-orchestra.yaml is stale against the schema or .lokf/schema/lokf.yaml
[group('knowledge bundle')]
lokf-adapt-check:
  {{lokf_cmd}} adapt {{source_schema_path}} {{lokf_adapt_args}} --lokf .lokf/schema/lokf.yaml -o .lokf/schema/fix-orchestra.yaml --check
