# Glossary

* [Adapt copy](adapt-copy.md) - The adapt copy: the copy of a schema that `lokf adapt` writes so that it can sit beside LOKF's schema in a knowledge bundle, here `.lokf/fix-orchestra.yaml`.
* [Departure](departure.md) - A departure: a place where a real FIX file breaks one of this project's rules, listed by file and JSON pointer in `tests/document_departures.yaml` so a test expects it.
* [Edition](edition.md) - An edition: one published version of FIX Orchestra that the schema renders, v1.0 or v1.1 RC3, each a module of its own whose class names end in `V10` or `V11`.
* [Member](member.md) - A member: one item of a repeated XSD choice, such as a field, component or group in a message's structure, held as an object with exactly one key so the list keeps the elements' order.
* [Open XML](open-xml.md) - Open XML: an element or attribute in a place where the XSDs accept any content, such as an application hint's FIXML flags, which the schema keeps as written in `OrchestraXmlElement` and `OrchestraXmlAttribute`.
