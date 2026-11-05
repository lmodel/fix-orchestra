"""Data tests: every example against the committed JSON Schema, and the rules that no
generator carries against their counter-examples."""

from pathlib import Path

import pytest
import yaml
from linkml.validator import validate
from linkml_runtime import SchemaView

from tests import conversion
from tests.orchestra_rules import rule_errors

DATA = Path(__file__).parent / "data"
VALID = sorted((DATA / "valid").glob("*.yaml"))
INVALID = sorted((DATA / "invalid").glob("*.yaml"))
PROBLEM_INVALID = sorted((DATA / "problem" / "invalid").glob("*.yaml"))


def class_of(path):
    return path.stem.split("-")[0]


def fails_at(path):
    first = path.read_text(encoding="utf-8").splitlines()[0]
    assert first.startswith("# Fails at: "), (
        f"{path.name}: the first line names where it fails"
    )
    return first.removeprefix("# Fails at: ").strip()


def _load(path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def test_the_example_folders_hold_examples():
    """The parametrized tests below pass on an empty folder, so this one does not."""
    assert len(VALID) >= 150, len(VALID)
    assert len(INVALID) >= 45, len(INVALID)
    assert len(PROBLEM_INVALID) >= 25, len(PROBLEM_INVALID)


@pytest.mark.parametrize("path", VALID, ids=lambda p: p.stem)
def test_valid_examples_validate(path):
    """Every valid example passes the JSON Schema."""
    found = conversion.schema_errors(_load(path), class_of(path))
    assert not found, [f"{conversion.pointer(e)}: {e.message[:200]}" for e in found]


@pytest.mark.parametrize(
    "path",
    [
        p
        for p in VALID
        if class_of(p)
        in (
            "OrchestraRepositoryV10",
            "OrchestraRepositoryV11",
            "OrchestraInterfacesV10",
            "OrchestraInterfacesV11",
        )
    ],
    ids=lambda p: p.stem,
)
def test_valid_files_keep_the_rules(path):
    """A valid whole file breaks none of the rules on a whole file."""
    assert not rule_errors(class_of(path), _load(path))


@pytest.mark.parametrize("path", INVALID, ids=lambda p: p.stem)
def test_counter_examples_fail_where_they_say(path):
    """Every counter-example fails at the place its first line names, as
    `# Fails at: <JSON pointer>`, and nowhere else but on the way to it, so a file that
    starts failing for another reason fails this test."""
    where = fails_at(path)
    found = conversion.schema_errors(_load(path), class_of(path))
    assert found, "it validates"
    reached = set().union(*(conversion.places(e) for e in found))
    report = [f"{conversion.pointer(e)}: {e.message[:200]}" for e in found]
    assert where in reached, (sorted(reached), report)
    on_the_way = {
        p for p in reached if where == p or where.startswith(p.rstrip("/") + "/")
    }
    assert reached == on_the_way, (sorted(reached - on_the_way), report)


@pytest.mark.parametrize("path", PROBLEM_INVALID, ids=lambda p: p.stem)
def test_rule_counter_examples_fail_where_they_say(path):
    """A counter-example under problem/invalid/ passes the JSON Schema, which cannot
    state its rule, and fails only the rule its first line points to."""
    where = fails_at(path)
    instance = _load(path)
    found = conversion.schema_errors(instance, class_of(path))
    assert not found, [f"{conversion.pointer(e)}: {e.message[:200]}" for e in found]
    assert [p for p, _ in rule_errors(class_of(path), instance)] == [where]


def test_validator_agrees():
    """linkml-validate, which the README tells a user to run, accepts a valid example and
    rejects a counter-example at the same place."""
    good = DATA / "valid" / "OrchestraRepositoryV10-small.yaml"
    report = validate(_load(good), str(conversion.SCHEMA), "OrchestraRepositoryV10")
    assert not report.results, [r.message for r in report.results]
    bad = DATA / "invalid" / "OrchestraFieldV11-name-too-long.yaml"
    report = validate(_load(bad), str(conversion.SCHEMA), "OrchestraFieldV11")
    assert any("fixr_name" in r.message for r in report.results), [
        r.message for r in report.results
    ]


def test_every_concrete_class_has_an_example():
    """Each class a file can hold has a valid example."""
    view = SchemaView(str(conversion.SCHEMA))
    concrete = {
        name
        for name, cls in view.all_classes().items()
        if not cls.abstract and not cls.mixin
    }
    examples = {class_of(path) for path in VALID}
    assert concrete == examples, sorted(concrete ^ examples)
