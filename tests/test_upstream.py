"""Checks that upstream/ holds the editions the schema renders.

upstream/ holds each edition's XSDs and licence, and the real documents the tests read,
as the FIX Trading Community publishes them. scripts/check_upstream_release.py compares
them with GitHub each week; these tests make the same comparison offline.
"""

import hashlib
import importlib.util
from functools import cache

import pytest
import yaml

from tests.conversion import SCHEMA_DIR, UPSTREAM, ROOT

WATCH = ROOT / "scripts" / "check_upstream_release.py"


@cache
def _watch():
    spec = importlib.util.spec_from_file_location("watch_pins", WATCH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _blob(data: bytes) -> str:
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def test_upstream_holds_only_the_pinned_files():
    found = {
        str(path.relative_to(UPSTREAM))
        for path in UPSTREAM.rglob("*")
        if path.is_file()
    }
    assert found == {pin["local"] for pin in _watch().pins()}
    assert len(found) == 30


def test_copies_match_the_pinned_blobs():
    """Each file has the git object hash the watch pins."""
    wrong = [
        pin["local"]
        for pin in _watch().pins()
        if _blob((UPSTREAM / pin["local"]).read_bytes()) != pin["sha"]
    ]
    assert not wrong


def test_each_pin_names_an_edition_or_a_document_tag():
    """Every pinned commit is one the watch checks a tag against."""
    watch = _watch()
    commits = {e["commit"] for e in watch.EDITIONS.values()}
    commits |= set(watch.DOCUMENT_TAGS.values())
    commits.add("cd24169a2abd8daba7c360987c7a46ca11873a12")
    assert {pin["commit"] for pin in watch.pins()} <= commits


@pytest.mark.parametrize("suffix", ["V10", "V11"])
def test_each_edition_module_names_its_pins(suffix):
    """A module's header names the edition, tag and commit the watch pins."""
    module = {"V10": "fix_orchestra_v1_0", "V11": "fix_orchestra_v1_1"}[suffix]
    header = yaml.safe_load((SCHEMA_DIR / f"{module}.yaml").read_text(encoding="utf-8"))
    edition = _watch().EDITIONS[header["version"]]
    assert header["annotations"]["upstream_tag"] == edition["tag"]
    assert header["annotations"]["upstream_commit"] == edition["commit"]
    assert header["annotations"]["upstream_repository"].endswith(edition["repository"])
    assert header["license"] == "Apache-2.0"


def test_the_umbrella_names_both_editions():
    header = yaml.safe_load(
        (SCHEMA_DIR / "fix_orchestra.yaml").read_text(encoding="utf-8")
    )
    assert header["version"] == ", ".join(_watch().EDITIONS)


def test_the_specification_repository_holds_v10_xsds_at_its_rc3_tag():
    """At v1.1-rc3, fix-orchestra-spec's v1-1 folder holds the v1.0 XSDs, byte for byte,
    so the RC3 XSDs come from the fix-orchestra code repository. The pins of the v1.0 files are the evidence: the watch lists the same hashes."""
    pins = {pin["local"]: pin["sha"] for pin in _watch().pins()}
    assert pins["v1.0/repository/repositorytypes.xsd"] == (
        "e1595434020673042675031c7575fda59afa0203"
    )
    assert (
        pins["v1.1-rc3/repository/repositorytypes.xsd"]
        != (pins["v1.0/repository/repositorytypes.xsd"])
    )
