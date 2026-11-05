# About fix-orchestra

This page says how the schema reads the Orchestra XSDs, where it departs from them, and what the real files show. It is for someone who will use the records or change the converters.

## Two editions

Orchestra v1.0 became a Technical Standard in February 2021, and FIX Latest is published in it. Version 1.1 is in its third release candidate, of June 2026, whose XSDs sit in FIX's code repository under the tag `v1.1-rc3`. Neither is a superset of the other: RC3 adds scenarios, encoding standards and encoding blocks, drops v1.0's FIXML file names and category kinds, requires a category's section and caps a name at 64 characters.

So each edition is a module of its own, `fix_orchestra_v1_0` and `fix_orchestra_v1_1`, and each class carries its edition's suffix: `OrchestraMessageV10`, `OrchestraMessageV11`. `fix_orchestra_common` holds the value lists both editions share, the Dublin Core block that heads a file, and two classes for XML the XSDs leave open.

## How the schema reads an XSD

`scripts/orchestra_xsd_to_linkml.py` writes the edition modules from `upstream/`, and the descriptions from `scripts/orchestra_words.yaml`.

| In the XSD | In the schema |
| --- | --- |
| A complex type, or an element's anonymous type | A class, `Orchestra<Name><Edition>` |
| An attribute group | A mixin, such as `OrchestraPedigreeV10Mixin` for the added, changed and deprecated versions |
| An attribute or a child element | A key: `fixr_` for a repository, `fixi_` for an interfaces file, then the XML name in snake case, which an `xml_attribute` or `xml_element` annotation keeps |
| A choice that repeats, such as a message's fields and components | A list of members, each holding one element, so the order survives |
| A value list | An enum, with the XSD's values as written |
| A value list joined with any string | Any text, with the enum as the values Orchestra recommends |
| `xs:any`, `xs:anyAttribute` | `OrchestraXmlElement` and `OrchestraXmlAttribute`, kept as written |
| A pattern, a length or a bound | A pattern or a minimum and maximum on the key |

`scripts/orchestra_xml_to_yaml.py` reads those annotations, and nothing else, to convert a file both ways. It stops on a name the schema has no key for. It leaves out `xsi:schemaLocation`, which tells a parser where an XSD is, and comments.

## What the records leave out

- The order of the children of a repository and of a metadata block, which the XSDs leave free.
- A language tag on a Dublin Core value, which no real file uses.
- Whitespace around a name: RC3's names are XML Schema tokens, which a validator collapses before checking. The schema checks the collapsed form, so write a name with single spaces.

## Where the schema departs from the XSDs

- **RC3's `fieldTypeOrCodeSetKey`.** It is a key on a field's type or code set, so it refuses a second field of the same datatype, which every real repository has. The rules keep what it asks of one field, a type or a code set but not both, and leave out the uniqueness.
- **Keys and references.** JSON Schema cannot state that two elements share no key, or that a reference names an element that exists. `tests/orchestra_rules.py` checks both: the XSDs' `xs:key` and `xs:keyref` constraints, and the references the specification describes, such as a field used by number and scenario or a trigger's transition.

## What the real files show

The tests read FIX Latest as of Extension Pack 312, the FIXT and FIX 4.4 session files, the Trading Digital Assets practices and a sample interfaces file, each unchanged under `upstream/documents/`. Each is valid against the v1.0 XSD and converts to records that the schema accepts and that convert back unchanged.

- FIX Latest leaves the section out of three categories, Common, Fields and ImplFields. That is valid in v1.0, which FIX Latest conforms to, and RC3 is the edition that requires a section.
- The two session files put groups in a category named Common, which neither file defines. `tests/document_departures.yaml` lists them.
- RC3 cannot hold FIX Latest as it is: one group name, `UnderlyingPaymentStreamNonDeliverableFixingDatesBusinessCenterGrp`, has 65 characters. `tests/test_documents.py` moves FIX Latest to RC3's shape, and the XSD and the schema then refuse that name alone.
- No published RC3 file is valid against RC3's XSDs, so `tests/data/xml/` holds two this project wrote, one per kind of file.
- At its `v1.1-rc3` tag, the specification repository's `v1-1` folder still holds the v1.0 XSDs byte for byte.

## The licence position

FIX licenses the XSDs and the specification under CC BY-ND 4.0, which allows a whole copy and no adapted text. So `upstream/` holds the XSDs unchanged, the schema takes their names, structure and value lists, and every description is this project's own. [NOTICE](https://github.com/lmodel/fix-orchestra/blob/main/NOTICE) states the position.
