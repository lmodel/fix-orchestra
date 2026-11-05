# Workflows

* [Knowledge librarian (knowledge-librarian.yaml)](knowledge-librarian.md) - The scheduled workflow that runs the ktl-librarian skill as an agent and opens a pull request with its patch, inert until `KNOWLEDGE_LIBRARIAN_ENABLED` is `true`.
* [Knowledge registrar (knowledge-registrar.yaml)](knowledge-registrar.md) - The gate that checks the bundle's form on every pull request that touches `.lokf/`: `lokf validate --check-refs` and the conventions script.
* [Knowledge release (knowledge-release.yaml)](knowledge-release.md) - The workflow that attaches the schema's adapt copy, the bundle zip and a Microsoft 365 Copilot skill zip to a release, each with its `.sha256` and a build-provenance attestation.
* [Knowledge sync (knowledge-sync.yaml)](knowledge-sync.md) - The workflow that copies the KTL sidecar's scripts and workflows from a newer KTL release into this repository, as a pull request.
* [Knowledge website (knowledge-website.yaml)](knowledge-website.md) - The workflow that builds the documentation site and deploys it to GitHub Pages from `main`, once `KNOWLEDGE_WEBSITE_ENABLED` is `true`.
* [Lint and docs (lint-and-docs.yaml)](lint-and-docs.md) - The workflow of static checks: ShellCheck, actionlint, markdownlint, lychee, codespell, and the word budgets that hold CONTRIBUTING.md to 1,000 words and SECURITY.md to 900.
* [Build and test (main.yaml)](main.md) - The workflow that runs `just lint` and `just test` on Python 3.10 to 3.14 on every pull request and push to `main`, and checks that the adapt copy is current.
* [Semantic release (semantic-release.yml)](semantic-release.md) - The workflow that, on a push to `main`, promotes the changelog's `[Unreleased]` section, tags `vX.Y.Z`, publishes the GitHub Release and dispatches the knowledge release.
* [Upstream watch (upstream-watch.yaml)](upstream-watch.md) - The weekly check that `scripts/check_upstream_release.py` runs: a new tag in FIX's repositories, a moved tag, a changed or missing pinned file, or a changed licence opens or updates an issue.
