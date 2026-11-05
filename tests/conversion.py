"""The documents, the converters and the schemas, for the tests that read them.

The scripts are not a package, so each is loaded by its path. FIX Latest takes about a
second to convert and an XSD a moment to compile, so each test module shares one copy of
each and must not change it.
"""

import importlib.util
import json
import sys
from functools import cache
from pathlib import Path

import jsonschema
from lxml import etree

ROOT = Path(__file__).parent.parent
SCRIPTS = ROOT / "scripts"
SCHEMA_DIR = ROOT / "src" / "fix_orchestra" / "schema"
SCHEMA = SCHEMA_DIR / "fix_orchestra.yaml"
UPSTREAM = ROOT / "upstream"
EXAMPLES = ROOT / "tests" / "data" / "xml"
JSON_SCHEMA = ROOT / "project" / "jsonschema" / "fix_orchestra.schema.json"

# Each edition's folder under upstream/, by the class suffix the schema gives it.
EDITION_FOLDERS = {"V10": "v1.0", "V11": "v1.1-rc3"}

# The real documents the tests read, pinned under upstream/documents/, and the examples
# this project wrote. Every one is valid against its edition's XSD.
DOCUMENTS = sorted((UPSTREAM / "documents").glob("*.xml")) + sorted(
    EXAMPLES.glob("*.xml")
)
FIX_LATEST = UPSTREAM / "documents" / "OrchestraFIXLatest.xml"


def _load(name):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    # The dataclasses in a script read their module from this table.
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


CONVERTER = _load("orchestra_xml_to_yaml")
XSD_CONVERTER = _load("orchestra_xsd_to_linkml")


@cache
def record(path: Path) -> tuple[str, dict]:
    """The class and record of one document, converted once."""
    return CONVERTER.read(path)


class _XmlXsd(etree.Resolver):
    """Serve the v1.0 XSDs' import of xml.xsd from the copy beside them, so that no
    schema is fetched from the network."""

    def __init__(self, folder: Path):
        self.folder = folder

    def resolve(self, url, pubid, context):
        if url and url.endswith("/xml.xsd"):
            return self.resolve_filename(str(self.folder / "xml.xsd"), context)
        return None


def xsd_path(suffix: str, kind: str) -> Path:
    return UPSTREAM / EDITION_FOLDERS[suffix] / kind / f"{kind}.xsd"


def xsd_tree(suffix: str, kind: str):
    """An edition's XSD as a tree, parsed with no network access."""
    path = xsd_path(suffix, kind)
    parser = etree.XMLParser(no_network=True, resolve_entities=False)
    parser.resolvers.add(_XmlXsd(path.parent))
    return etree.parse(str(path), parser)


@cache
def xsd(suffix: str, kind: str):
    """An edition's compiled XSD, for 'repository' or 'interfaces'."""
    return etree.XMLSchema(xsd_tree(suffix, kind))


def edition_of(path: Path) -> tuple[str, str]:
    """The edition suffix and file kind of a document, by its root's namespace."""
    root = etree.parse(str(path), CONVERTER.PARSER).getroot()
    name = CONVERTER.roots()[(etree.QName(root).namespace, etree.QName(root).localname)]
    kind = "repository" if "Repository" in name else "interfaces"
    return name[-3:], kind


@cache
def json_schema() -> dict:
    return json.loads(JSON_SCHEMA.read_text(encoding="utf-8"))


@cache
def _validator(class_name: str):
    schema = {"$ref": f"#/$defs/{class_name}", "$defs": json_schema()["$defs"]}
    return jsonschema.validators.validator_for(schema)(schema)


def schema_errors(instance, class_name: str) -> list:
    """What the committed JSON Schema finds wrong with a record of a class."""
    return list(_validator(class_name).iter_errors(instance))


def pointer(error) -> str:
    return "/" + "/".join(str(part) for part in error.absolute_path)


def places(error) -> set[str]:
    """Where an error points: its own place, or, for an anyOf or oneOf that no branch
    met, the places inside the branch that could have been meant. An optional value's
    branches are the value and null, so its error points inside the value; the null
    branch is left aside. A choice whose branches are alternatives stays at its own
    place."""
    if error.validator not in ("anyOf", "oneOf") or not error.context:
        return {pointer(error)}
    branches = {}
    for sub in error.context:
        branches.setdefault(sub.relative_schema_path[0], []).append(sub)
    real = [
        subs
        for subs in branches.values()
        if not any(s.validator == "type" and s.validator_value == "null" for s in subs)
    ]
    if len(real) != 1:
        return {pointer(error)}
    found = set()
    for sub in real[0]:
        found |= places(sub)
    return found or {pointer(error)}
