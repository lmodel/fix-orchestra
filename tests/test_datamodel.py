"""Checks what the generated models do with real data.

The Pydantic models and the dataclasses load the examples and the whole of FIX Latest
EP312, so a user of either reads an Orchestra file's records without LinkML's validator.
"""

import json
from pathlib import Path

import pytest
import yaml
from linkml_runtime.loaders import json_loader

from fix_orchestra.datamodel import fix_orchestra as dataclasses_module
from fix_orchestra.datamodel import fix_orchestra_pydantic
from tests import conversion

VALID = sorted((Path(__file__).parent / "data" / "valid").glob("*.yaml"))


@pytest.mark.parametrize("path", VALID, ids=lambda p: p.stem)
def test_each_example_loads_into_the_pydantic_models(path):
    model = getattr(fix_orchestra_pydantic, path.stem.split("-")[0])
    model(**yaml.safe_load(path.read_text(encoding="utf-8")))


@pytest.mark.parametrize("path", VALID, ids=lambda p: p.stem)
def test_each_example_loads_into_the_dataclasses(path):
    cls = getattr(dataclasses_module, path.stem.split("-")[0])
    json_loader.loads(
        json.dumps(yaml.safe_load(path.read_text(encoding="utf-8"))), target_class=cls
    )


def test_fix_latest_loads_into_the_pydantic_models():
    name, record = conversion.record(conversion.FIX_LATEST)
    model = getattr(fix_orchestra_pydantic, name)(**record)
    assert len(model.fixr_messages.fixr_message) == 181
    assert len(model.fixr_fields.fixr_field) == 6203


def test_a_value_with_capitals_survives_the_python_enums():
    """A value such as bestEffort or TAG_VALUE keeps its text, whatever name Python gives
    it."""
    assert (
        fix_orchestra_pydantic.OrchestraReliability("bestEffort").value == "bestEffort"
    )
    assert (
        fix_orchestra_pydantic.OrchestraDatatypeStandardV10("TAG_VALUE").value
        == "TAG_VALUE"
    )
