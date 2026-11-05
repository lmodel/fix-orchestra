<a href="https://github.com/linkml/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# fix-orchestra

FIX Orchestra v1.0 Technical Standard and v1.1 RC3 (LinkML)

> **Only want to ask?** Install `ktl-docent` into any agent you use, by a route from [the install page](https://w3id.org/ktl/docs/install/), and ask it about this project. It answers from the bundle and says how far each answer has been checked.
>
> **Agents:** if `.lokf/knowledge/index.md` exists, read it first. `llms.txt` says how to weigh it.

## Documentation Website

[https://lmodel.github.io/fix-orchestra](https://lmodel.github.io/fix-orchestra)

## What it models

The schema renders FIX Orchestra, the FIX Trading Community's standard for rules of engagement that a machine can read, in two editions: the v1.0 Technical Standard of February 2021, in which FIX Latest is published, and the v1.1 third release candidate of June 2026. Each edition is a module written from its XSDs, and `scripts/orchestra_xml_to_yaml.py` converts an Orchestra repository or interfaces file to records and back.

`upstream/` holds both editions' XSDs and five of FIX's own files, pinned by hash. [docs/about.md](docs/about.md) says how the schema reads the XSDs and where it departs from them.

## Mappings

None. The schema renders a file format and borrows no other vocabulary's terms. lmodel/fix-protocol and lmodel/fix-sbe map their classes to this one's.

The SSSOM set of mappings to fix-sbe is gone: its rows were written by hand, and fix-sbe now states the pairs from its side.

## Repository Structure

* [docs/](docs/): the website's own pages
* [project/](project/): generated project files (do not edit them)
* [scripts/](scripts/): the converter from the XSDs and its words, the converter between a file and its records, and the upstream watch
* [src/fix_orchestra/schema/](src/fix_orchestra/schema): the LinkML schema, which `just gen-schema` writes
* [src/fix_orchestra/datamodel/](src/fix_orchestra/datamodel): the generated Python datamodel
* [tests/](tests/): Python tests, with example files and data in [data/](tests/data) and the neighbours' adapt copies in [neighbours/](tests/neighbours)
* [upstream/](upstream/): each edition's XSDs and licence, and FIX's own files, unchanged
* [website/](website/): the Astro Starlight site built from the README, `docs/`, the schema's pages and the knowledge bundle

## Developer Tools

Run `just` to list the project's [just](https://github.com/casey/just/) recipes.

## Knowledge Trust Ladder (KTL)

`.lokf/` holds this project's [KTL](https://w3id.org/ktl/) knowledge bundle. Its domain schema, `.lokf/fix-orchestra.yaml`, is the copy `just lokf-adapt` writes from `src/fix_orchestra/schema/fix_orchestra.yaml`, and `just lokf-adapt-check` says when it is stale. Edit the source, never the copy. A release carries the copy as `schema-<tag>-fix-orchestra.yaml`.

The copy roots each edition's file classes and named elements on `Concept`, such as `OrchestraMessageV10` and `OrchestraSessionV11`. An element of one of these types nested in another, such as a field an actor defines in place, is a concept with keys of its own. In Obsidian, add these to the *Known LOKF types* setting of the KTL Registrar and KTL Curator plugins:

```text
OrchestraActorV10, OrchestraActorV11, OrchestraCategoryV10, OrchestraCategoryV11, OrchestraCodeSetV10, OrchestraCodeSetV11, OrchestraComponentV10, OrchestraComponentV11, OrchestraConceptV10, OrchestraConceptV11, OrchestraDatatypeV10, OrchestraDatatypeV11, OrchestraEncodingStandardV11, OrchestraEncodingV10, OrchestraEncodingV11, OrchestraFieldV10, OrchestraFieldV11, OrchestraFlowV10, OrchestraFlowV11, OrchestraGroupV10, OrchestraGroupV11, OrchestraInterfaceV10, OrchestraInterfaceV11, OrchestraInterfacesV10, OrchestraInterfacesV11, OrchestraMessageV10, OrchestraMessageV11, OrchestraProtocolV10, OrchestraProtocolV11, OrchestraRepositoryV10, OrchestraRepositoryV11, OrchestraScenarioV11, OrchestraSectionV10, OrchestraSectionV11, OrchestraServiceV10, OrchestraServiceV11, OrchestraSessionProtocolV10, OrchestraSessionProtocolV11, OrchestraSessionV10, OrchestraSessionV11, OrchestraStateMachineV10, OrchestraStateMachineV11, OrchestraTransportV10, OrchestraTransportV11, OrchestraUserInterfaceV10, OrchestraUserInterfaceV11
```

The copy renames nothing. Every key starts with `fixr_`, `fixi_`, `xml_`, `dc_` or `dcterms_`, so no key is LOKF's or another released copy's under another IRI; it keeps six Dublin Core keys, such as `dcterms_source`, whose IRIs LOKF's relations also use. `tests/test_schema_rules.py` holds both.

## License

The schema and the code are under the Apache License 2.0 ([LICENSE](LICENSE)), and the knowledge bundle in [.lokf/knowledge/](.lokf/knowledge) is under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

FIX's XSDs are under CC BY-ND 4.0 and its Orchestra files under the Apache License 2.0, each copied unchanged; the schema's descriptions are this project's own words. [NOTICE](NOTICE) states the position. This project is not endorsed by FIX Protocol Limited.

## Contributing and security

[CONTRIBUTING.md](CONTRIBUTING.md) is the checklist for pull requests and
releases, [AI_COVENANT.md](AI_COVENANT.md) sets the rules for AI-assisted work,
[SECURITY.md](SECURITY.md) says how to report a vulnerability, and
[CHANGELOG.md](CHANGELOG.md) records the changes.

## Credits

Built from the [linkml-project-copier](https://github.com/linkml/linkml-project-copier) template ([doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584)).
