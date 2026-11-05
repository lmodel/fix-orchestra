"""Checks that the schema's words are the project's own.

FIX licenses its XSDs and the Orchestra specification under CC BY-ND 4.0, which allows
whole copies but no adapted text. So upstream/ holds the XSDs unchanged, and every title,
description and comment the schema gives is written from what the element does. This test
holds that no run of four words in the schema, the words table or the docs is a run of the
XSDs' documentation. NOTICE states the position.
"""

import re
import xml.etree.ElementTree as ET
from functools import cache

import pytest
import yaml

from tests.conversion import ROOT, SCHEMA_DIR, UPSTREAM

XS = "{http://www.w3.org/2001/XMLSchema}"
RUN = 4
# Keys whose values are names, addresses or patterns rather than prose.
NOT_PROSE = {
    "id",
    "source",
    "see_also",
    "prefixes",
    "imports",
    "pattern",
    "annotations",
}


def _words(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+(?:'[a-z]+)?", text.lower())


def _runs(text: str) -> set[tuple[str, ...]]:
    words = _words(text)
    return {tuple(words[i : i + RUN]) for i in range(len(words) - RUN + 1)}


@cache
def upstream_runs() -> set[tuple[str, ...]]:
    """Every run of four words in the documentation of every pinned XSD."""
    runs = set()
    for path in sorted(UPSTREAM.rglob("*.xsd")):
        for doc in ET.parse(path).getroot().iter(f"{XS}documentation"):
            runs |= _runs("".join(doc.itertext()))
    return runs


def _prose(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for key, inner in value.items():
            if key not in NOT_PROSE:
                yield from _prose(inner)
    elif isinstance(value, list):
        for inner in value:
            yield from _prose(inner)


SOURCES = [
    *sorted(SCHEMA_DIR.glob("*.yaml")),
    ROOT / "scripts" / "orchestra_words.yaml",
]
DOCS = [ROOT / "README.md", ROOT / "docs" / "about.md", ROOT / "docs" / "index.md"]


def test_the_upstream_text_is_read():
    """The comparison has something to compare with."""
    assert len(upstream_runs()) > 2000


@pytest.mark.parametrize("path", SOURCES, ids=lambda p: p.name)
def test_no_schema_text_shares_a_run_with_the_xsds(path):
    shared = set()
    for text in _prose(yaml.safe_load(path.read_text(encoding="utf-8"))):
        shared |= _runs(text) & upstream_runs()
    assert not shared, sorted(" ".join(run) for run in shared)


@pytest.mark.parametrize("path", [p for p in DOCS if p.exists()], ids=lambda p: p.name)
def test_no_page_shares_a_run_with_the_xsds(path):
    shared = _runs(path.read_text(encoding="utf-8")) & upstream_runs()
    assert not shared, sorted(" ".join(run) for run in shared)


def test_no_xsd_documentation_reaches_a_generated_file():
    """The generated JSON Schema carries the schema's descriptions alone."""
    generated = (
        ROOT / "project" / "jsonschema" / "fix_orchestra.schema.json"
    ).read_text()
    shared = _runs(generated) & upstream_runs()
    assert not shared, sorted(" ".join(run) for run in shared)[:10]
