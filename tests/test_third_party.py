"""Validate FIX-Trading-Community sample XML files against the LinkML schema.

Two third-party corpora are covered:

* ``tests/data/third_party/fix-orchestra/`` — reference-implementation samples
  from the `fix-orchestra <https://github.com/FIXTradingCommunity/fix-orchestra>`_
  repository (interfaces and full FIX dictionaries).
* ``tests/data/third_party/orchestrations/`` — asset-class and session rules of
  engagement from the
  `orchestrations <https://github.com/FIXTradingCommunity/orchestrations>`_
  repository (FIX Standard subset).

Both corpora exercise two gates:

1. **XML well-formedness** - every ``.xml`` parses without error.
2. **LinkML-schema validation** - each XML is converted via
   ``scripts/fix_xml_to_linkml.py`` and then validated by ``linkml-validate``
   against the generated schema. The number of errors must be ``<= max_errors``
   for the file, where ``max_errors > 0`` flags a *known* upstream data quirk
   (e.g. the FIX ``Common`` category is missing the XSD-required ``section``
   attribute). Investigate before incrementing the budget.

The LinkML-level gate proves the auto-generated schema is faithful enough to
round-trip representative real-world Orchestra documents.
"""
from __future__ import annotations

import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

import pytest
import yaml

PROJECT = Path(__file__).parent.parent
SCHEMA = PROJECT / "src" / "fix_orchestra" / "schema" / "fix_orchestra.yaml"
CONV = PROJECT / "scripts" / "fix_xml_to_linkml.py"

_FIX_ORCH = PROJECT / "tests" / "data" / "third_party" / "fix-orchestra"
_ORCH = PROJECT / "tests" / "data" / "third_party" / "orchestrations"

_LARGE_THRESHOLD = 1_000_000  # 1 MB

# (corpus-dir, filename, target-class, max-allowed-validation-errors, note)
# A non-zero allowance flags a *known* data quirk in the upstream FIX corpus,
# not a converter or schema bug. Investigate before incrementing the budget.
CASES = [
    # fix-orchestra – reference implementation corpus
    (_FIX_ORCH, "SampleInterfaces.xml",           "Interfaces", 0,
     "FIX-supplied sample – validates cleanly."),
    (_FIX_ORCH, "mit_2016.xml",                   "Repository", 0,
     "FIX `Common` category `section` attribute is optional in real Orchestra files."),
    (_FIX_ORCH, "OrchestraFIXLatest.xml",         "Repository", 0,
     "FIX `Common` category `section` attribute is optional in real Orchestra files."),

    # orchestrations – FIX Standard asset-class and session rules of engagement
    # All files use the 2020 (or 2022) Orchestra namespace and validate cleanly.
    (_ORCH, "Equity.xml",                         "Repository", 0,
     "FIX equity trading rules of engagement."),
    (_ORCH, "Warrant.xml",                        "Repository", 0,
     "FIX warrant trading rules of engagement."),
    (_ORCH, "Future.xml",                         "Repository", 0,
     "FIX futures trading rules of engagement."),
    (_ORCH, "Option.xml",                         "Repository", 0,
     "FIX options trading rules of engagement."),
    (_ORCH, "TradingDigitalAssets.xml",           "Repository", 0,
     "FIX digital-assets trading rules of engagement."),
    (_ORCH, "FIX44Session.xml",                   "Repository", 0,
     "FIX 4.4 session protocol definition."),
    (_ORCH, "FIXTSession.xml",                    "Repository", 0,
     "FIXT session protocol definition."),
    (_ORCH, "Debt.xml",                           "Repository", 0,
     "FIX debt-instrument rules of engagement."),
    (_ORCH, "FIXReferenceData.xml",               "Repository", 0,
     "FIX reference-data definitions."),
    (_ORCH, "OrchestraFIX42.xml",                 "Repository", 0,
     "Full FIX 4.2 Orchestra dictionary."),
    (_ORCH, "OrchestraFIX44.xml",                 "Repository", 0,
     "Full FIX 4.4 Orchestra dictionary (>1 MB, marked slow)."),
    (_ORCH, "OrchestraExamples-v11-RC1.xml",      "Repository", 0,
     "Orchestra v1.1-RC1 examples; uses 2022 namespace."),
    (_ORCH, "OrchestraFIXLatest.xml",             "Repository", 0,
     "FIX latest dictionary (2020 ns); counterpart to fix-orchestra copy."),
    (_ORCH, "OrchestraFIXLatestNonOTC_EP273.xml", "Repository", 0,
     "FIX latest non-OTC subset (EP273)."),
]


def _have(cmd: str) -> bool:
    return shutil.which(cmd) is not None


def _params():
    out = []
    for corpus, name, target, max_err, note in CASES:
        path = corpus / name
        marks: list = []
        if path.is_file() and path.stat().st_size > _LARGE_THRESHOLD:
            marks.append(pytest.mark.slow)
        out.append(pytest.param(corpus, name, target, max_err, note,
                                id=f"{corpus.name}/{name}", marks=marks))
    return out


# ---------------------------------------------------------------------------
# Well-formedness gate
# ---------------------------------------------------------------------------

# could be dropped - we should assume upstream FIX XML is well-formed, and if not,
# the converter will error out anyway. But leave for now.

@pytest.mark.parametrize("corpus,filename,target,max_errors,note", _params())
def test_third_party_xml_wellformed(corpus, filename, target, max_errors, note,
                                    capsys):
    """The XML must parse without error."""
    src = corpus / filename
    if not src.is_file():
        pytest.skip(f"missing upstream file {src}")
    tree = ET.parse(str(src))
    counts = _count_xml_records(tree.getroot())
    with capsys.disabled():
        print(f"\n  [wellformed] {corpus.name}/{filename}: "
              f"parsed OK -- {_fmt_counts(counts, verb='counted')}")


# ---------------------------------------------------------------------------
# LinkML-schema validation gate
# ---------------------------------------------------------------------------

@pytest.mark.skipif(not _have("linkml-validate"),
                    reason="linkml-validate not on PATH (run `uv sync`).")
@pytest.mark.skipif(not CONV.exists(),
                    reason="scripts/fix_xml_to_linkml.py not yet implemented.")
@pytest.mark.parametrize("corpus,filename,target,max_errors,note", _params())
def test_third_party_xml_validates_against_linkml(
        tmp_path, corpus, filename, target, max_errors, note, capsys,
        fix_record_tally):
    """Convert the XML to YAML and assert LinkML validation stays within the
    per-file error budget."""
    src = corpus / filename
    if not src.is_file():
        pytest.skip(f"missing upstream file {src}")
    yaml_out = tmp_path / (Path(filename).stem + ".yaml")

    conv = subprocess.run(
        [sys.executable, str(CONV), "--schema", str(SCHEMA),
         "--target-class", target, "--in", str(src), "--out", str(yaml_out)],
        capture_output=True, text=True, check=False,
    )
    assert conv.returncode == 0, (
        f"converter failed for {filename}:\nstdout={conv.stdout}\n"
        f"stderr={conv.stderr}")
    assert yaml_out.exists()

    val = subprocess.run(
        ["linkml-validate", "-s", str(SCHEMA),
         "--target-class", target, str(yaml_out)],
        capture_output=True, text=True, check=False,
    )
    error_lines = [ln for ln in val.stdout.splitlines()
                   if ln.startswith("[ERROR]")]
    actual = len(error_lines)

    yaml_obj = yaml.safe_load(yaml_out.read_text())
    counts = _count_yaml_records(yaml_obj)
    fix_record_tally["total"] += sum(counts.values())
    budget_msg = (f"{actual}/{max_errors} errors (within budget)"
                  if max_errors > 0 else "no errors")
    with capsys.disabled():
        print(f"\n  [validate]   {corpus.name}/{filename} ({target}): "
              f"{_fmt_counts(counts, verb='linkml schema validated')}; {budget_msg}")

    assert actual <= max_errors, (
        f"{filename}: {actual} validation errors, expected <= "
        f"{max_errors}. Note: {note}\n"
        f"First 5 errors:\n  " + "\n  ".join(error_lines[:5]))


# ---------------------------------------------------------------------------
# Record-count helpers (used to surface processing volume per file)
# ---------------------------------------------------------------------------

# XML local tag names whose direct children we want to count as "records" in
# a FIX Orchestra document. Ordered roughly by domain weight.
_XML_CONTAINERS = [
    'datatypes', 'fields', 'codeSets', 'messages', 'components', 'groups',
    'actors', 'concepts', 'scenarios', 'sections', 'categories',
    'interface', 'sessions',
]


def _count_xml_records(root: ET.Element) -> dict[str, int]:
    """Count the children of each top-level FIX container element."""
    out: dict[str, int] = {}
    # ET tags can be namespaced - compare on local name
    def local(tag: str) -> str:
        return tag.split('}', 1)[1] if '}' in tag else tag

    for elt in root.iter():
        lname = local(elt.tag)
        if lname in _XML_CONTAINERS:
            n = sum(1 for c in elt if local(c.tag) != 'annotation')
            out[lname] = out.get(lname, 0) + n
    return out


# YAML slot names whose multivalued contents we count after conversion.
# Mirrors the XML containers but uses snake_case where applicable.
_YAML_RECORD_PATHS = [
    ('datatypes', 'datatype'),
    ('fields', 'field'),
    ('code_sets', 'code_set'),
    ('messages', 'message'),
    ('components', 'component'),
    ('groups', 'group'),
    ('actors', 'actor'),
    ('actors', 'flow'),
    ('concepts', 'concept'),
    ('scenarios', 'scenario'),
    ('sections', 'section'),
    ('categories', 'category'),
]


def _count_yaml_records(doc: Any) -> dict[str, int]:
    """Count entries inside the well-known FIX containers in a converted YAML."""
    out: dict[str, int] = {}
    if not isinstance(doc, dict):
        return out
    for container, child in _YAML_RECORD_PATHS:
        node = doc.get(container)
        if isinstance(node, dict):
            items = node.get(child)
            if isinstance(items, list):
                out[child] = len(items)
    # Special-case Interfaces: top-level `interface` list
    if isinstance(doc.get('interface'), list):
        out['interface'] = len(doc['interface'])
    return out


_GREEN = "\033[32m"
_RESET = "\033[0m"


def _green(s: str) -> str:
    """Wrap ``s`` in ANSI green codes when stdout is a TTY (no-op otherwise)."""
    return f"{_GREEN}{s}{_RESET}" if sys.stdout.isatty() else s


def _fmt_counts(counts: dict[str, int], verb: str = "counted") -> str:
    """Format a record-count summary as ``<verb> N records (k1=v1, k2=v2, ...)``.

    The verb makes the relationship between the test outcome and the count
    explicit: e.g. ``parsed OK -- counted 7189 records`` confirms all 7189
    were parsed, and ``validated 7189 records; 1/1 errors (within budget)``
    confirms all 7189 went through the validator.

    The ``<verb> N records`` prefix is rendered in green on TTYs so the
    "successfully processed" headline stands out from the breakdown.
    """
    if not counts:
        return _green(f"{verb} 0 records")
    total = sum(counts.values())
    parts = [f"{k}={v}" for k, v in sorted(counts.items(),
                                            key=lambda kv: -kv[1])]
    return f"{_green(f'{verb} {total} records')} ({', '.join(parts)})"
