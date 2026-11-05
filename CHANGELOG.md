# Changelog

All notable changes to this project are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

The `v0.0.0` tag is a baseline, not a release: it marks where versioning starts so the first real release is `0.1.0` rather than `1.0.0`. The schema stays below 1.0.0 until its shape settles, so a breaking change is a minor release.

## [Unreleased]

### Added

- **Orchestra v1.0, the Technical Standard**, beside v1.1 RC3, each a module of its own, since FIX Latest is published in v1.0 and RC3 changes several of its attributes.
- **`upstream/`**, holding each edition's XSDs and licence and five of FIX's own Orchestra files, pinned by git object hash, with a weekly watch on FIX's tags, files and licences.
- **`scripts/orchestra_xml_to_yaml.py`**, which converts an Orchestra repository or interfaces file to records and back, keeping the order of a message's fields. It writes the records bare, as `linkml-validate` reads them, and the record's keys name its class on the way back.
- **Rules a validator cannot state** in `tests/orchestra_rules.py`: the XSDs' keys and references, and the references the specification describes.
- **Tests** that validate FIX Latest EP312 and the other files with the XSD and the schema, and convert them back unchanged. They also read the XSDs and the XML separately from the converters, and hold an example per class and a counter-example per constraint.
- **`.lokf/fix-orchestra.yaml`, the schema's `lokf adapt` copy.** The knowledge release attaches it as `schema-<tag>-fix-orchestra.yaml`.
- **The repository's Knowledge Trust Ladder (KTL) knowledge bundle and its sidecar automation**, from the KTL v0.61.0 templates with the lokf floor at 0.9.0, and a knowledge website that replaces the mkdocs site.
- **The governance files**: SECURITY.md, AI_COVENANT.md, NOTICE and the CONTRIBUTING checklist.

### Changed

- **v1.1 moves from RC2 to RC3**, read from the XSDs the fix-orchestra code repository tags `v1.1-rc3`.
- **Every class carries the `Orchestra` prefix and its edition**, such as `OrchestraMessageV10`, and every key is `fixr_` or `fixi_` and the XML name in snake case.
- **Every description is this project's own words.** The XSDs' documentation, which FIX licenses under CC BY-ND 4.0, is no longer copied.
- **The Dublin Core block is one class**, `OrchestraMetadata`, in place of 97.
- **The template settings** turn PyPI publishing and the docs preview off, linkml and linkml-runtime are locked at 1.12.1, and the Python project is named `fix-orchestra-linkml`.

### Removed

- **The SSSOM set of mappings to fix-sbe**, with the script that overlaid it on the schema.
- **The wire-format protocol buffers generator**, its output and the vendored fix-orchestra-protobuf sources.
- **The test corpus copied from FIX's repositories**, in favour of the pinned files under `upstream/documents/`.
