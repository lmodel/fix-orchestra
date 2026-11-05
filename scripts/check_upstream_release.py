#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Check the FIX Trading Community's repositories against the editions the schema renders.

The schema renders two editions of FIX Orchestra: the v1.0 Technical Standard, whose XSDs
sit in fix-orchestra-spec at the tag v1.0, and the v1.1 third release candidate, whose
XSDs sit in fix-orchestra at the tag v1.1-rc3. The tests read real documents from
orchestrations and fix-orchestra. upstream/ holds each file unchanged, and
scripts/upstream_pins.tsv names its repository, commit, path and git object hash. These
can change without any change in this repository:

- a repository gains a tag, such as another release candidate or a v1.1 standard;
- a pinned tag moves, or a pinned file changes or goes;
- a licence file on a default branch changes.

Each of these fails the check. Two more are reported for information only: the XSDs on
fix-orchestra's default branch differ from the release candidate's, and the FIX Latest
file on orchestrations' default branch differs from the copy the tests read, which happens
with each extension pack.

The script reads only GitHub's API and compares git object hashes, so it downloads no
file. It prints a Markdown report and exits 1 on any failing check, or when a check could
not finish. Text a server chose is quoted as code on one line in the report, so the issue
the workflow opens from it cannot mention anyone. A redirect is followed only to an https
address on api.github.com. Set ``GITHUB_TOKEN`` to raise the API's rate limit. Usage::

    python scripts/check_upstream_release.py [--report FILE]
"""

from __future__ import annotations

import argparse
import http.client
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parent.parent
PINS = ROOT / "scripts" / "upstream_pins.tsv"
USER_AGENT = "lmodel-fix-orchestra-upstream-check"
OWNER = "FIXTradingCommunity"
HOST = "api.github.com"
API = f"https://{HOST}/repos/{OWNER}"

# The most the script reads of one answer. A directory listing is a few kilobytes and the
# longest tag list about ten.
MAX_BYTES = 5_000_000

# The editions the schema renders. tests/test_upstream.py holds the schema headers and
# these pins equal. Move them together, with upstream/ and scripts/upstream_pins.tsv, for
# another edition.
EDITIONS = {
    "1.0": {
        "label": "the v1.0 Technical Standard",
        "repository": "fix-orchestra-spec",
        "tag": "v1.0",
        "commit": "e2b65db8505244f2708c468fe7cad60855fa9834",
    },
    "1.1-rc3": {
        "label": "the v1.1 third release candidate",
        "repository": "fix-orchestra",
        "tag": "v1.1-rc3",
        "commit": "eb4bb9de3bd8802c6e5e0aba06182407b22acc9b",
    },
}

# The other tags the documents are read at.
DOCUMENT_TAGS = {("fix-orchestra", "v1.6"): "68ce876068aae1352b483ed8a41f1da3e3f9ea17"}

# Every tag each repository held when the pins were set. A tag outside this list is news.
KNOWN_TAGS = {
    "fix-orchestra-spec": {
        "v1-0-DRAFT",
        "v1-0-RC1",
        "v1-0-RC2",
        "v1-0-RC3",
        "v1-0-RC4",
        "v1-0-RC5",
        "v1.0",
        "v1.1-rc1",
        "v1.1-rc2",
        "v1.1-rc3",
    },
    "fix-orchestra": {
        "v1-0-RC1",
        "v1-0-RC2",
        "v1-0-RC3",
        "v1-0-RC4",
        "v1-0-RC5",
        "v1.1-rc1",
        "v1.1-rc2",
        "v1.1-rc3",
        "v1.5",
        "v1.6",
    },
    "orchestrations": {"v1.5"},
}

# The licence file at each repository's root. The default branch is read from the API.
LICENCE = "LICENSE"


class _ApiRedirect(urllib.request.HTTPRedirectHandler):
    """Follow a redirect only to an https address on the API's host."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        parts = urllib.parse.urlsplit(newurl)
        if parts.scheme != "https" or parts.hostname != HOST:
            raise ValueError(f"a redirect leads off {HOST}, to {newurl}")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


# An opener in place of urlopen's, whose redirect handler follows any address.
_open = urllib.request.build_opener(_ApiRedirect).open


def _get(path: str):
    """The JSON answer to one API path under the owner's repositories, read up to the cap."""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(f"{API}{path}", headers=headers)
    with _open(req, timeout=60) as resp:
        body = resp.read(MAX_BYTES + 1)
    if len(body) > MAX_BYTES:
        raise ValueError(f"the answer to {path} is larger than {MAX_BYTES} bytes")
    return json.loads(body)


def _code(text: object) -> str:
    """Text a server chose, as a code span on one line, so it cannot mention a person or
    add a link in the issue. A blank line would end the span, so every run of spaces and
    line breaks is one space."""
    return "`" + " ".join(str(text).replace("`", "'").split()) + "`"


def pins() -> list[dict[str, str]]:
    """Each pinned file: its path under upstream/, git object hash, repository, commit and
    path in that repository."""
    keys = ("local", "sha", "repository", "commit", "path")
    rows = PINS.read_text(encoding="utf-8").splitlines()
    return [dict(zip(keys, row.split("\t"), strict=True)) for row in rows]


def _quote(path: str) -> str:
    return urllib.parse.quote(path, safe="/")


def _listing(repository: str, folder: str, ref: str) -> dict[str, str]:
    """The git object hash of each file in one folder of a repository at a ref."""
    answer = _get(f"/{repository}/contents/{_quote(folder)}?ref={_quote(ref)}")
    if not isinstance(answer, list):
        raise ValueError(f"{folder} in {repository} at {ref} is not a folder")
    return {entry["path"]: entry["sha"] for entry in answer if entry["type"] == "file"}


def _files(repository: str, paths: set[str], ref: str) -> dict[str, str]:
    """The git object hash of each named file at a ref, read folder by folder."""
    folders = {str(PurePosixPath(path).parent) for path in paths}
    found = {}
    for folder in sorted(folders):
        found |= _listing(repository, "" if folder == "." else folder, ref)
    return {path: found[path] for path in paths if path in found}


def _commit_of(repository: str, tag: str) -> str:
    """The commit a tag names, through any annotated tag objects on the way."""
    target = _get(f"/{repository}/git/ref/tags/{_quote(tag)}")["object"]
    while target["type"] == "tag":
        target = _get(f"/{repository}/git/tags/{target['sha']}")["object"]
    return target["sha"]


_default_branches: dict[str, str] = {}


def _default_branch(repository: str) -> str:
    """The repository's default branch, read once."""
    if repository not in _default_branches:
        _default_branches[repository] = _get(f"/{repository}")["default_branch"]
    return _default_branches[repository]


def check_tags() -> tuple[list[str], bool]:
    """Report any tag a repository has gained since the pins were set."""
    lines = []
    attention = False
    for repository, known in KNOWN_TAGS.items():
        entries = _get(f"/{repository}/tags?per_page=100")
        if len(entries) >= 100:
            raise ValueError(
                f"{repository} has 100 tags or more, past what one page holds"
            )
        tags = {entry["name"] for entry in entries}
        new = sorted(tags - known)
        if new:
            attention = True
            shown = ", ".join(_code(tag) for tag in new[:10])
            lines.append(
                f"- **{repository} has {len(new)} new tags:** {shown}. Read what changed, "
                "decide whether the schema moves to it, and move upstream/, the pins and "
                "the schema headers together."
            )
        else:
            lines.append(f"- {repository} has no new tag.")
    return lines, attention


def check_pinned_tags() -> tuple[list[str], bool]:
    """Report whether each pinned tag still names its commit."""
    tags = {(e["repository"], e["tag"]): e["commit"] for e in EDITIONS.values()}
    tags |= DOCUMENT_TAGS
    lines = []
    attention = False
    for (repository, tag), commit in sorted(tags.items()):
        found = _commit_of(repository, tag)
        if found != commit:
            attention = True
            lines.append(
                f"- **The tag {tag} of {repository} moved to {_code(found)}.** Find out "
                "why a published tag moved before trusting the copy in upstream/."
            )
    if not attention:
        lines.append(f"- All {len(tags)} pinned tags name their pinned commits.")
    return lines, attention


def check_pinned_files() -> tuple[list[str], bool]:
    """Report whether each pinned file still has its hash at its pinned commit."""
    by_source: dict[tuple[str, str], dict[str, str]] = {}
    for pin in pins():
        by_source.setdefault((pin["repository"], pin["commit"]), {})[pin["path"]] = pin[
            "sha"
        ]
    gone, changed = [], []
    for (repository, commit), wanted in sorted(by_source.items()):
        found = _files(repository, set(wanted), commit)
        for path, sha in sorted(wanted.items()):
            if path not in found:
                gone.append(f"{repository}/{path}")
            elif found[path] != sha:
                changed.append(f"{repository}/{path}")
    lines = []
    for label, paths in (("gone", gone), ("changed", changed)):
        if paths:
            shown = ", ".join(_code(path) for path in paths[:10])
            lines.append(f"- **{len(paths)} pinned files {label}:** {shown}.")
    if gone or changed:
        return lines, True
    return [f"- All {len(pins())} pinned files are unchanged."], False


def check_licences() -> tuple[list[str], bool]:
    """Report whether the licence on each default branch is the pinned file."""
    pinned = {pin["repository"]: pin["sha"] for pin in pins() if pin["path"] == LICENCE}
    lines = []
    attention = False
    for repository, sha in sorted(pinned.items()):
        found = _files(repository, {LICENCE}, _default_branch(repository)).get(LICENCE)
        if found != sha:
            attention = True
            lines.append(
                f"- **{LICENCE} on {repository}'s default branch changed.** Read what "
                "changed, and update NOTICE if the licence moved."
            )
    if not attention:
        lines.append(f"- The licences of all {len(pinned)} repositories are unchanged.")
    return lines, attention


def check_default_branches() -> tuple[list[str], bool]:
    """Report, for information, the pinned files that differ on a default branch."""
    lines = []
    edition = EDITIONS["1.1-rc3"]
    rc_pins = {
        pin["path"]: pin["sha"]
        for pin in pins()
        if pin["commit"] == edition["commit"] and pin["path"].endswith(".xsd")
    }
    found = _files(
        edition["repository"], set(rc_pins), _default_branch(edition["repository"])
    )
    moved = sorted(path for path, sha in rc_pins.items() if found.get(path) != sha)
    if moved:
        shown = ", ".join(_code(path) for path in moved)
        lines.append(
            f"- For information, fix-orchestra's default branch has XSDs that differ "
            f"from {edition['tag']}'s: {shown}."
        )
    else:
        lines.append(
            f"- fix-orchestra's default branch holds {edition['tag']}'s XSDs unchanged."
        )
    documents = {
        pin["path"]: pin["sha"]
        for pin in pins()
        if pin["repository"] == "orchestrations" and pin["path"].endswith(".xml")
    }
    found = _files("orchestrations", set(documents), _default_branch("orchestrations"))
    moved = sorted(path for path, sha in documents.items() if found.get(path) != sha)
    if moved:
        shown = ", ".join(_code(path) for path in moved)
        lines.append(
            "- For information, orchestrations' default branch has newer documents than "
            f"the tests read: {shown}. They are test data, so moving them is optional."
        )
    else:
        lines.append(
            "- orchestrations' default branch holds the documents the tests read."
        )
    return lines, False


# Each check, by the name the report gives it when it cannot finish.
CHECKS = (
    ("tags", check_tags),
    ("pinned tags", check_pinned_tags),
    ("pinned files", check_pinned_files),
    ("licence", check_licences),
    ("default branch", check_default_branches),
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--report", type=Path, help="Also write the Markdown report to this file"
    )
    args = parser.parse_args(argv)
    lines = [
        f"- Pinned edition: {e['label']}, {e['repository']} at {e['tag']}."
        for e in EDITIONS.values()
    ]
    attention = False
    for label, check in CHECKS:
        try:
            found, needs = check()
        # OSError covers a refused or failed request and a timeout, HTTPException and
        # EOFError a connection cut off mid-answer, LookupError and ValueError an answer
        # of another shape or too large.
        except (
            OSError,
            http.client.HTTPException,
            EOFError,
            LookupError,
            ValueError,
        ) as err:
            found = [f"- **The {label} check could not finish: {_code(err)}.**"]
            needs = True
        lines += found
        attention = attention or needs
    text = "\n".join(lines) + "\n"
    print(text, end="")
    if args.report:
        args.report.write_text(text, encoding="utf-8")
    return 1 if attention else 0


if __name__ == "__main__":
    sys.exit(main())
