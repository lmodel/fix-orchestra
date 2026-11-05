"""Checks the JSON Schema this project commits, as a user of it would read it.

project/jsonschema/fix_orchestra.schema.json is what a consumer without LinkML validates
with. It is read here under the draft it declares, and held to the generator's settings in
.linkml/generators.yaml.
"""

import json

import jsonschema
import yaml
from linkml.generators.jsonschemagen import JsonSchemaGenerator

from tests.conversion import JSON_SCHEMA, ROOT, SCHEMA, json_schema


def test_the_schema_is_valid_under_the_draft_it_declares():
    jsonschema.validators.validator_for(json_schema()).check_schema(json_schema())


def test_the_committed_file_is_the_generators_output():
    """A schema edit without `just gen-project` fails here."""
    settings = yaml.safe_load((ROOT / ".linkml" / "generators.yaml").read_text())
    args = settings["generator_args"]["jsonschema"]
    generated = JsonSchemaGenerator(str(SCHEMA), **args).serialize()
    assert json.loads(generated) == json.loads(JSON_SCHEMA.read_text(encoding="utf-8"))


def test_the_top_of_the_schema_is_a_v10_repository():
    """The file's root takes a v1.0 repository, and $defs holds the other three roots."""
    assert json_schema()["title"] == "fix_orchestra"
    assert json_schema()["version"] == "1.0, 1.1-rc3"
    assert set(json_schema()["required"]) == {
        "fixr_name",
        "fixr_version",
        "fixr_metadata",
        "fixr_datatypes",
        "fixr_code_sets",
        "fixr_fields",
        "fixr_messages",
    }
    for root in (
        "OrchestraRepositoryV11",
        "OrchestraInterfacesV10",
        "OrchestraInterfacesV11",
    ):
        assert root in json_schema()["$defs"]


def test_a_member_holds_exactly_one_element():
    """A member of a repeated choice is a oneOf, one branch per element it may hold."""
    member = json_schema()["$defs"]["OrchestraStructureMemberV10"]
    assert [b["required"] for b in member["oneOf"]] == [
        ["fixr_component_ref"],
        ["fixr_group_ref"],
        ["fixr_field_ref"],
    ]


def test_an_open_value_list_takes_any_text():
    """Where the XSD joins a value list with any string, the list recommends values and
    any text passes."""
    purpose = json_schema()["$defs"]["OrchestraDocumentationV10"]["properties"][
        "fixr_purpose"
    ]
    assert {"$ref": "#/$defs/OrchestraPurpose"} in purpose["anyOf"]
    assert {"type": "string"} in purpose["anyOf"]
