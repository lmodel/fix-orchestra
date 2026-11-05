"""Checks the upstream watch's decisions against stubbed answers.

scripts/check_upstream_release.py reads GitHub's API. These tests replace its one network
call, `_get`, with a table of answers, so they run offline. They show what the report says
in each case the watch knows.
"""

import http.client
import importlib.util
import urllib.error
import urllib.parse
from pathlib import Path, PurePosixPath

import pytest

ROOT = Path(__file__).parent.parent
SCRIPT = ROOT / "scripts" / "check_upstream_release.py"


@pytest.fixture
def watch():
    """A fresh copy of the script, so no test sees another's stub."""
    spec = importlib.util.spec_from_file_location("watch_under_test", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _q(path):
    return urllib.parse.quote(path, safe="/")


def _answers(watch):
    """The answers of an unchanged upstream, built from the pins."""
    answers = {}
    for repository, tags in watch.KNOWN_TAGS.items():
        answers[f"/{repository}"] = {"default_branch": "master"}
        answers[f"/{repository}/tags?per_page=100"] = [
            {"name": t} for t in sorted(tags)
        ]
    tags = {(e["repository"], e["tag"]): e["commit"] for e in watch.EDITIONS.values()}
    tags |= watch.DOCUMENT_TAGS
    for (repository, tag), commit in tags.items():
        answers[f"/{repository}/git/ref/tags/{_q(tag)}"] = {
            "object": {"type": "commit", "sha": commit}
        }
    folders: dict = {}
    for pin in watch.pins():
        folder = str(PurePosixPath(pin["path"]).parent)
        folder = "" if folder == "." else folder
        for ref in (pin["commit"], "master"):
            folders.setdefault((pin["repository"], folder, ref), []).append(
                {"path": pin["path"], "sha": pin["sha"], "type": "file"}
            )
    for (repository, folder, ref), entries in folders.items():
        answers[f"/{repository}/contents/{_q(folder)}?ref={_q(ref)}"] = entries
    return answers


def _run(watch, answers, capsys, argv=()):
    def fake_get(path):
        answer = answers[path]
        if isinstance(answer, Exception):
            raise answer
        return answer

    watch._get = fake_get
    code = watch.main(list(argv))
    return code, capsys.readouterr().out


def test_an_unchanged_upstream_reports_nothing(watch, capsys):
    code, report = _run(watch, _answers(watch), capsys)
    assert code == 0, report
    assert "**" not in report


def test_a_new_tag_is_reported_and_quoted(watch, capsys):
    answers = _answers(watch)
    answers["/fix-orchestra-spec/tags?per_page=100"].append({"name": "v1.1-rc4 `@x`"})
    code, report = _run(watch, answers, capsys)
    assert code == 1
    assert "fix-orchestra-spec has 1 new tags:** `v1.1-rc4 '@x'`" in report


def test_a_moved_tag_is_reported(watch, capsys):
    answers = _answers(watch)
    answers["/fix-orchestra/git/ref/tags/v1.1-rc3"] = {
        "object": {"type": "commit", "sha": "abc123"}
    }
    code, report = _run(watch, answers, capsys)
    assert code == 1
    assert "The tag v1.1-rc3 of fix-orchestra moved to `abc123`" in report


def test_an_annotated_tag_is_followed_to_its_commit(watch, capsys):
    answers = _answers(watch)
    commit = watch.EDITIONS["1.1-rc3"]["commit"]
    answers["/fix-orchestra/git/ref/tags/v1.1-rc3"] = {
        "object": {"type": "tag", "sha": "tagobject"}
    }
    answers["/fix-orchestra/git/tags/tagobject"] = {
        "object": {"type": "commit", "sha": commit}
    }
    code, report = _run(watch, answers, capsys)
    assert code == 0, report


def test_a_tag_behind_two_tag_objects_is_followed(watch, capsys):
    answers = _answers(watch)
    commit = watch.EDITIONS["1.1-rc3"]["commit"]
    answers["/fix-orchestra/git/ref/tags/v1.1-rc3"] = {
        "object": {"type": "tag", "sha": "outer"}
    }
    answers["/fix-orchestra/git/tags/outer"] = {
        "object": {"type": "tag", "sha": "inner"}
    }
    answers["/fix-orchestra/git/tags/inner"] = {
        "object": {"type": "commit", "sha": commit}
    }
    code, report = _run(watch, answers, capsys)
    assert code == 0, report


def test_a_hundred_tags_stop_the_tags_check(watch, capsys):
    answers = _answers(watch)
    answers["/fix-orchestra/tags?per_page=100"] = [
        {"name": f"t{i}"} for i in range(100)
    ]
    code, report = _run(watch, answers, capsys)
    assert code == 1
    assert "The tags check could not finish" in report
    assert "100 tags or more" in report


def test_a_renamed_default_branch_is_read_from_the_api(watch, capsys):
    """The licence check reads the branch the API names, not a fixed one."""
    answers = _answers(watch)
    answers["/orchestrations"] = {"default_branch": "main"}
    for key in [k for k in answers if k.startswith("/orchestrations/contents/")]:
        if key.endswith("?ref=master"):
            answers[key.replace("?ref=master", "?ref=main")] = answers.pop(key)
    code, report = _run(watch, answers, capsys)
    assert code == 0, report


def test_a_changed_pinned_file_is_reported(watch, capsys):
    answers = _answers(watch)
    pin = next(
        p for p in watch.pins() if p["local"] == "v1.0/repository/repository.xsd"
    )
    folder = "v1-0-STANDARD/resources/repository"
    entries = answers[f"/fix-orchestra-spec/contents/{folder}?ref={pin['commit']}"]
    for entry in entries:
        if entry["path"] == pin["path"]:
            entry["sha"] = "0" * 40
    code, report = _run(watch, answers, capsys)
    assert code == 1
    assert "1 pinned files changed:** `fix-orchestra-spec/" in report


def test_a_gone_pinned_file_is_reported(watch, capsys):
    answers = _answers(watch)
    commit = "cd24169a2abd8daba7c360987c7a46ca11873a12"
    key = f"/orchestrations/contents/{_q('FIX Standard')}?ref={commit}"
    answers[key] = [
        e for e in answers[key] if not e["path"].endswith("FIXTSession.xml")
    ]
    code, report = _run(watch, answers, capsys)
    assert code == 1
    assert (
        "1 pinned files gone:** `orchestrations/FIX Standard/FIXTSession.xml`" in report
    )


def test_a_changed_licence_is_reported(watch, capsys):
    answers = _answers(watch)
    for entry in answers["/orchestrations/contents/?ref=master"]:
        entry["sha"] = "1" * 40
    code, report = _run(watch, answers, capsys)
    assert code == 1
    assert "LICENSE on orchestrations's default branch changed" in report


def test_newer_fix_latest_is_for_information_only(watch, capsys):
    answers = _answers(watch)
    for entry in answers[f"/orchestrations/contents/{_q('FIX Standard')}?ref=master"]:
        if entry["path"].endswith("OrchestraFIXLatest.xml"):
            entry["sha"] = "2" * 40
    code, report = _run(watch, answers, capsys)
    assert code == 0, report
    assert (
        "For information, orchestrations' default branch has newer documents" in report
    )


def test_work_after_rc3_is_for_information_only(watch, capsys):
    answers = _answers(watch)
    folder = "repository/src/main/resources/xsd"
    for entry in answers[f"/fix-orchestra/contents/{folder}?ref=master"]:
        entry["sha"] = "3" * 40
    code, report = _run(watch, answers, capsys)
    assert code == 0, report
    assert "For information, fix-orchestra's default branch has XSDs" in report


@pytest.mark.parametrize(
    "error",
    [
        urllib.error.URLError("refused"),
        http.client.IncompleteRead(b""),
        ValueError("a redirect leads off api.github.com"),
    ],
)
def test_a_failed_check_is_reported(watch, capsys, error):
    answers = _answers(watch)
    answers["/fix-orchestra-spec/tags?per_page=100"] = error
    code, report = _run(watch, answers, capsys)
    assert code == 1
    assert "The tags check could not finish" in report


def test_a_redirect_off_the_api_is_refused(watch):
    handler = watch._ApiRedirect()
    with pytest.raises(ValueError, match="leads off"):
        handler.redirect_request(None, None, 302, "Found", {}, "https://example.org/x")
    with pytest.raises(ValueError, match="leads off"):
        handler.redirect_request(
            None, None, 302, "Found", {}, "http://api.github.com/x"
        )


def test_the_report_is_written_to_a_file(watch, capsys, tmp_path):
    out = tmp_path / "report.md"
    code, report = _run(watch, _answers(watch), capsys, ["--report", str(out)])
    assert code == 0
    assert out.read_text(encoding="utf-8") == report
