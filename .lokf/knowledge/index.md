---
lokf_version: "0.2"
okf_version: "0.2"
base_iri: https://w3id.org/lmodel/fix-orchestra/knowledge/
context: https://w3id.org/lokf/context.jsonld
title: fix-orchestra Knowledge Bundle
description: FIX Orchestra v1.0 Technical Standard and v1.1 RC3 (LinkML)
license: https://creativecommons.org/licenses/by/4.0/
publisher:
  type: Person
  id: https://w3id.org/lmodel/fix-orchestra/knowledge/person/noel-mcloughlin
  name: Noel McLoughlin
---

# fix-orchestra Knowledge Bundle

A [LOKF](https://lokf.nolan-nichols.com) knowledge base for fix-orchestra. Every Markdown file under `knowledge/` is one concept; together they form a queryable knowledge graph, derived from this repository's code and docs.

# Services

* [Documentation site](services/documentation-site.md) - The knowledge website in `website/`, an Astro Starlight site that the Knowledge website workflow publishes to GitHub Pages at `https://lmodel.github.io/fix-orchestra`, built from the README, `docs/`, the schema's pages and this bundle.
* [The XML converter](services/xml-converter.md) - `scripts/orchestra_xml_to_yaml.py`: converts an Orchestra repository or interfaces file to records the schema validates, picking the edition by the root's namespace, and writes records back to XML. `just to-records FILE` runs it.
* [The XSD converter](services/xsd-converter.md) - `scripts/orchestra_xsd_to_linkml.py`: reads both editions' XSDs under `upstream/` and the words table, and writes the schema's four modules. `just gen-schema` runs it, and it stops on any XSD construct or name it has no rule or words for.

# Datasets

* [The adapt copy](datasets/adapt-copy.md) - `.lokf/fix-orchestra.yaml`, which `just lokf-adapt` writes from the schema so that it can sit beside LOKF's: the file this bundle validates against, and the file a release attaches as `schema-<tag>-fix-orchestra.yaml`.
* [The common module](datasets/common-module.md) - `src/fix_orchestra/schema/fix_orchestra_common.yaml`: the 13 value lists both editions share, `OrchestraMetadata` for the Dublin Core block that heads a file, and `OrchestraXmlElement` and `OrchestraXmlAttribute` for XML the XSDs leave open.
* [Where FIX's files break a rule](datasets/document-departures.md) - `tests/document_departures.yaml`: each rule a real FIX file breaks, by file and JSON pointer. FIX's two session files put groups in a category named Common, which neither defines.
* [The example data](datasets/example-data.md) - `tests/data/`: a valid example of each class, taken from the example files, three small whole files for the rule tests, a counter-example per kind of constraint, and a counter-example per rule the JSON Schema cannot state.
* [The example Orchestra files](datasets/example-files.md) - `tests/data/xml/`: four Orchestra files this project wrote, a repository and an interfaces file for each edition, with one of each kind of element the XSDs define, since no published RC3 file is valid against RC3's XSDs.
* [The example venue's order flow](datasets/example-flow.md) - A v1.0 flow from the example repository, `OrderFlow`, which carries orders from the actor Trader to the actor Venue with recoverable delivery.
* [FIX Latest EP312](datasets/fix-latest.md) - `upstream/documents/OrchestraFIXLatest.xml`: FIX Latest as of Extension Pack 312, a v1.0 Orchestra repository of 181 messages and 6,203 fields that the tests validate with the XSD and the schema and convert back unchanged.
* [The fix-orchestra LinkML schema](datasets/fix-orchestra-linkml-schema.md) - `src/fix_orchestra/schema/`: the umbrella `fix_orchestra.yaml` over `fix_orchestra_common`, `fix_orchestra_v1_0` and `fix_orchestra_v1_1`, a LinkML model of FIX Orchestra's repository and interfaces files in two editions, with four tree roots.
* [The generated artefacts](datasets/generated-artefacts.md) - `project/`, `src/fix_orchestra/datamodel/` and `docs/schema/`: what `just gen-project` and `just gen-doc` write from the schema, such as the JSON Schema, the Pydantic models and the OWL, never edited by hand.
* [The neighbours' copies](datasets/neighbour-copies.md) - `tests/neighbours/`: the schema assets of 30 released lmodel repositories, each checked against its release's `.sha256` and attestation, against which the adapt copy is held to share no class or key.
* [The rules a validator cannot state](datasets/orchestra-rules.md) - `tests/orchestra_rules.py`: the XSDs' `xs:key` and `xs:keyref` constraints and the references the specification describes, checked over a whole file, which JSON Schema cannot state.
* [The copy of FIX's files](datasets/upstream-copy.md) - `upstream/`: both editions' XSDs and licences and five of FIX's own Orchestra files, 30 files in all, each unchanged and pinned by git object hash in `scripts/upstream_pins.tsv`.
* [The v1.0 module](datasets/v1-0-module.md) - `src/fix_orchestra/schema/fix_orchestra_v1_0.yaml`: 77 classes for Orchestra v1.0's repository and interfaces XSDs, among them 5 mixins and 9 member classes, each name ending in `V10`, which the XSD converter writes.
* [The v1.1 RC3 module](datasets/v1-1-module.md) - `src/fix_orchestra/schema/fix_orchestra_v1_1.yaml`: 84 classes for Orchestra v1.1 RC3's repository and interfaces XSDs, among them 5 mixins and 9 member classes, each name ending in `V11`, which the XSD converter writes.
* [The words table](datasets/words-table.md) - `scripts/orchestra_words.yaml`: this project's own title and description for every class, key and value list the schema renders, written from what each element does and not from FIX's text.

# Explanations

* [Where the schema departs from the XSDs](explanations/departures-from-the-xsds.md) - The two places the schema and its rules differ from the XSDs: RC3's `fieldTypeOrCodeSetKey`, whose uniqueness the rules leave out, and the keys and references that only the rules check.
* [How the schema reads an XSD](explanations/how-the-schema-reads-an-xsd.md) - What each XSD construct becomes in the schema: a complex type a class, an attribute group a mixin, an attribute or child element a `fixr_` or `fixi_` key, a repeated choice a list of members, and `xs:any` an open XML element.
* [Why the schema has two editions](explanations/two-editions.md) - Why v1.0 and v1.1 RC3 are separate modules with suffixed class names: neither edition is a superset of the other, and FIX Latest is published in v1.0.
* [What the real files show](explanations/what-the-real-files-show.md) - What FIX's own Orchestra files show when the schema reads them: FIX Latest's three categories without a section, the session files' undefined category, the 65-character group name RC3 refuses, and the v1.0 XSDs in the RC3 tag.

# Glossary

* [Adapt copy](glossary/adapt-copy.md) - The adapt copy: the copy of a schema that `lokf adapt` writes so that it can sit beside LOKF's schema in a knowledge bundle, here `.lokf/fix-orchestra.yaml`.
* [Departure](glossary/departure.md) - A departure: a place where a real FIX file breaks one of this project's rules, listed by file and JSON pointer in `tests/document_departures.yaml` so a test expects it.
* [Edition](glossary/edition.md) - An edition: one published version of FIX Orchestra that the schema renders, v1.0 or v1.1 RC3, each a module of its own whose class names end in `V10` or `V11`.
* [Member](glossary/member.md) - A member: one item of a repeated XSD choice, such as a field, component or group in a message's structure, held as an object with exactly one key so the list keeps the elements' order.
* [Open XML](glossary/open-xml.md) - Open XML: an element or attribute in a place where the XSDs accept any content, such as an application hint's FIXML flags, which the schema keeps as written in `OrchestraXmlElement` and `OrchestraXmlAttribute`.

# Playbooks

* [Knowledge sources map](playbooks/knowledge-sources.md) - The librarian's scrape map: every repository location and external source this bundle derives concepts from, how to re-check each, and the tracked paths left out with their reasons.
* [Regenerate and test](playbooks/regenerate-and-test.md) - How to change the schema: edit the words table or the XSD converter, run `just gen-schema`, `just gen-project`, `just gen-doc` and `just lokf-adapt`, then `just lint` and `just test`, and commit the output.
* [Release](playbooks/release.md) - How a release happens: a merge to `main` with a `feat:`, `fix:` or `security:` commit makes semantic-release promote the changelog, tag `vX.Y.Z` and publish the GitHub Release, from a `v0.0.0` baseline tag.
* [Move to another edition](playbooks/update-upstream-pins.md) - What to do when the upstream watch reports a new tag, such as another release candidate or a v1.1 standard: move `upstream/`, the pins and the schema headers together, and rerun the XSD converter.
* [Validate an Orchestra file](playbooks/validate-an-orchestra-file.md) - How to check an Orchestra file against the schema: convert it with `just to-records`, validate the records with `linkml-validate` as the edition's repository or interfaces class, and convert them back with `--to-xml`.

# Policies

* [AI covenant](policies/ai-covenant.md) - AI_COVENANT.md: the rules for AI-assisted work here. A contributor owns what they submit, an element says what the XSD says, a rule states only what Orchestra states, and the words are this project's own.
* [Licence and attribution](policies/license-and-attribution.md) - The code and schema are under the Apache License 2.0 and the bundle under CC BY 4.0. FIX's XSDs, under CC BY-ND 4.0, and its Orchestra files, under the Apache License 2.0, are copied unchanged, and every description is this project's own words.
* [Security policy](policies/security-policy.md) - SECURITY.md: how to report a vulnerability, through GitHub's private vulnerability reporting, what this repository releases, and what holds each surface that executes here.

# References

* [FIX Orchestra v1.0, the Technical Standard](references/orchestra-v1-0.md) - The upstream authority for the v1.0 module: FIX Orchestra v1.0, promoted to Technical Standard in February 2021, whose XSDs sit in FIXTradingCommunity/fix-orchestra-spec under the tag `v1.0`, commit `e2b65db`. FIX Latest is published in this edition.
* [FIX Orchestra v1.1 Release Candidate 3](references/orchestra-v1-1-rc3.md) - The upstream authority for the v1.1 module: FIX Orchestra v1.1 RC3 of June 2026, whose XSDs sit in FIX's code repository, FIXTradingCommunity/fix-orchestra, under the tag `v1.1-rc3`, commit `eb4bb9d`.
* [FIX's orchestrations repository](references/orchestrations-repository.md) - FIXTradingCommunity/orchestrations, under the Apache License 2.0: the source of FIX Latest as of Extension Pack 312 and of three more Orchestra files the tests read, pinned at commit `cd24169`.

# Workflows

* [Knowledge librarian (knowledge-librarian.yaml)](workflows/knowledge-librarian.md) - The scheduled workflow that runs the ktl-librarian skill as an agent and opens a pull request with its patch, inert until `KNOWLEDGE_LIBRARIAN_ENABLED` is `true`.
* [Knowledge registrar (knowledge-registrar.yaml)](workflows/knowledge-registrar.md) - The gate that checks the bundle's form on every pull request that touches `.lokf/`: `lokf validate --check-refs` and the conventions script.
* [Knowledge release (knowledge-release.yaml)](workflows/knowledge-release.md) - The workflow that attaches the schema's adapt copy, the bundle zip and a Microsoft 365 Copilot skill zip to a release, each with its `.sha256` and a build-provenance attestation.
* [Knowledge sync (knowledge-sync.yaml)](workflows/knowledge-sync.md) - The workflow that copies the KTL sidecar's scripts and workflows from a newer KTL release into this repository, as a pull request.
* [Knowledge website (knowledge-website.yaml)](workflows/knowledge-website.md) - The workflow that builds the documentation site and deploys it to GitHub Pages from `main`, once `KNOWLEDGE_WEBSITE_ENABLED` is `true`.
* [Lint and docs (lint-and-docs.yaml)](workflows/lint-and-docs.md) - The workflow of static checks: ShellCheck, actionlint, markdownlint, lychee, codespell, and the word budgets that hold CONTRIBUTING.md to 1,000 words and SECURITY.md to 900.
* [Build and test (main.yaml)](workflows/main.md) - The workflow that runs `just lint` and `just test` on Python 3.10 to 3.14 on every pull request and push to `main`, and checks that the adapt copy is current.
* [Semantic release (semantic-release.yml)](workflows/semantic-release.md) - The workflow that, on a push to `main`, promotes the changelog's `[Unreleased]` section, tags `vX.Y.Z`, publishes the GitHub Release and dispatches the knowledge release.
* [Upstream watch (upstream-watch.yaml)](workflows/upstream-watch.md) - The weekly check that `scripts/check_upstream_release.py` runs: a new tag in FIX's repositories, a moved tag, a changed or missing pinned file, or a changed licence opens or updates an issue.
