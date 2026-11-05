# Services

* [Documentation site](documentation-site.md) - The knowledge website in `website/`, an Astro Starlight site that the Knowledge website workflow publishes to GitHub Pages at `https://lmodel.github.io/fix-orchestra`, built from the README, `docs/`, the schema's pages and this bundle.
* [The XML converter](xml-converter.md) - `scripts/orchestra_xml_to_yaml.py`: converts an Orchestra repository or interfaces file to records the schema validates, picking the edition by the root's namespace, and writes records back to XML. `just to-records FILE` runs it.
* [The XSD converter](xsd-converter.md) - `scripts/orchestra_xsd_to_linkml.py`: reads both editions' XSDs under `upstream/` and the words table, and writes the schema's four modules. `just gen-schema` runs it, and it stops on any XSD construct or name it has no rule or words for.
