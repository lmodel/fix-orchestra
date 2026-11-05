# Playbooks

* [Knowledge sources map](knowledge-sources.md) - The librarian's scrape map: every repository location and external source this bundle derives concepts from, how to re-check each, and the tracked paths left out with their reasons.
* [Regenerate and test](regenerate-and-test.md) - How to change the schema: edit the words table or the XSD converter, run `just gen-schema`, `just gen-project`, `just gen-doc` and `just lokf-adapt`, then `just lint` and `just test`, and commit the output.
* [Release](release.md) - How a release happens: a merge to `main` with a `feat:`, `fix:` or `security:` commit makes semantic-release promote the changelog, tag `vX.Y.Z` and publish the GitHub Release, from a `v0.0.0` baseline tag.
* [Move to another edition](update-upstream-pins.md) - What to do when the upstream watch reports a new tag, such as another release candidate or a v1.1 standard: move `upstream/`, the pins and the schema headers together, and rerun the XSD converter.
* [Validate an Orchestra file](validate-an-orchestra-file.md) - How to check an Orchestra file against the schema: convert it with `just to-records`, validate the records with `linkml-validate` as the edition's repository or interfaces class, and convert them back with `--to-xml`.
