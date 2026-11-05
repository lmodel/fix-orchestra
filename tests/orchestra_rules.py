"""The rules on a whole Orchestra file that JSON Schema cannot state.

JSON Schema sees one value at a time, so it cannot tell whether two elements share a
key, or whether a name or number points at an element that exists. The XSDs state the
first kind in their xs:key and xs:keyref constraints, which ``KEY_RULES`` follows one by
one for each edition. The second kind is what the specification says a reference means:
a use of a field, component, group or message names one that the file defines, by its
number and scenario, and a name of a category, section, flow, actor, state machine,
transition, state or timer names one the file holds. ``REFERENCE_RULES`` checks those.

RC3's fieldTypeOrCodeSetKey is a key on a field's type or code set, so it refuses two
fields that share a datatype; no real repository can meet it. The rule here keeps what
the key asks of one field, a type or a code set but not both, and leaves out the
uniqueness. issues/93 reports the fault.

``rule_errors(class_name, record)`` returns each error as a JSON pointer and a sentence.
tests/test_documents.py runs the rules over every pinned and example file, and
tests/test_data.py holds them to the counter-examples under tests/data/problem/invalid/.
"""

from __future__ import annotations

from collections.abc import Iterator

BASE = "base"


def _items(record, *keys) -> Iterator[tuple[str, dict]]:
    """The items of a list under a chain of keys, with their pointers."""
    value, place = record, ""
    for key in keys[:-1]:
        value = (value or {}).get(key)
        place += f"/{key}"
    for index, item in enumerate((value or {}).get(keys[-1]) or []):
        yield f"{place}/{keys[-1]}/{index}", item


def _unique(items, fields, label) -> Iterator[tuple[str, str]]:
    seen = {}
    for place, item in items:
        key = tuple(
            item.get(f, BASE if f.endswith("scenario") else None) for f in fields
        )
        if None in key:
            continue
        if key in seen:
            shown = ", ".join(str(k) for k in key)
            yield f"{place}/{fields[0]}", f"another {label} already has the key {shown}"
        seen.setdefault(key, place)


# Keys


def _repository_keys(record) -> Iterator[tuple[str, str]]:
    r = record
    actors = [
        (p + "/fixr_actor", m["fixr_actor"])
        for p, m in _items(r, "fixr_actors", "fixr_members")
        if "fixr_actor" in m
    ]
    yield from _unique(actors, ("fixr_name",), "actor")
    names = {a["fixr_name"] for _, a in actors}
    for place, member in _items(r, "fixr_actors", "fixr_members"):
        flow = member.get("fixr_flow")
        for end in ("fixr_source", "fixr_destination"):
            if flow is not None and flow[end] not in names:
                yield f"{place}/fixr_flow/{end}", f"no actor is named {flow[end]}"
    code_sets = list(_items(r, "fixr_code_sets", "fixr_code_set"))
    yield from _unique(code_sets, ("fixr_name", "fixr_scenario"), "code set")
    yield from _unique(code_sets, ("fixr_id", "fixr_scenario"), "code set")
    for place, code_set in code_sets:
        codes = [
            (f"{place}/fixr_code/{i}", c)
            for i, c in enumerate(code_set.get("fixr_code") or [])
        ]
        yield from _unique(codes, ("fixr_name",), "code of this set")
    for container, item, label in (
        ("fixr_components", "fixr_component", "component"),
        ("fixr_groups", "fixr_group", "group"),
        ("fixr_messages", "fixr_message", "message"),
        ("fixr_fields", "fixr_field", "field"),
    ):
        found = list(_items(r, container, item))
        yield from _unique(found, ("fixr_name", "fixr_scenario"), label)
        yield from _unique(found, ("fixr_id", "fixr_scenario"), label)
    yield from _unique(
        list(_items(r, "fixr_concepts", "fixr_concept")), ("fixr_name",), "concept"
    )


def _v10_keys(record) -> Iterator[tuple[str, str]]:
    yield from _repository_keys(record)
    types = list(_items(record, "fixr_code_sets", "fixr_code_set")) + list(
        _items(record, "fixr_datatypes", "fixr_datatype")
    )
    yield from _unique(types, ("fixr_name",), "code set or datatype")
    names = {t["fixr_name"] for _, t in types}
    for place, field in _items(record, "fixr_fields", "fixr_field"):
        if field["fixr_type"] not in names:
            yield (
                f"{place}/fixr_type",
                f"no code set or datatype is named {field['fixr_type']}",
            )


def _v11_keys(record) -> Iterator[tuple[str, str]]:
    yield from _repository_keys(record)
    datatypes = list(_items(record, "fixr_datatypes", "fixr_datatype"))
    yield from _unique(datatypes, ("fixr_name",), "datatype")
    names = {d["fixr_name"] for _, d in datatypes}
    code_sets = list(_items(record, "fixr_code_sets", "fixr_code_set"))
    for place, code_set in code_sets:
        codes = [
            (f"{place}/fixr_code/{i}", c)
            for i, c in enumerate(code_set.get("fixr_code") or [])
        ]
        yield from _unique(codes, ("fixr_id",), "code of this set")
        if code_set["fixr_type"] not in names:
            yield f"{place}/fixr_type", f"no datatype is named {code_set['fixr_type']}"
    sets = {(c["fixr_name"], c.get("fixr_scenario", BASE)) for _, c in code_sets}
    for place, field in _items(record, "fixr_fields", "fixr_field"):
        has_type, has_set = "fixr_type" in field, "fixr_code_set" in field
        if has_type == has_set:
            yield place, "a field names a datatype or a code set, and not both"
        if has_type and field["fixr_type"] not in names:
            yield f"{place}/fixr_type", f"no datatype is named {field['fixr_type']}"
        key = (field.get("fixr_code_set"), field.get("fixr_scenario", BASE))
        if has_set and key not in sets:
            yield f"{place}/fixr_code_set", f"no code set is named {key[0]} in {key[1]}"
    scenarios = list(_items(record, "fixr_scenarios", "fixr_scenario"))
    yield from _unique(scenarios, ("fixr_name",), "scenario")
    standards = list(
        _items(record, "fixr_encoding_standards", "fixr_encoding_standard")
    )
    yield from _unique(standards, ("fixr_name",), "encoding standard")


def _interfaces_keys(record) -> Iterator[tuple[str, str]]:
    interfaces = list(_items(record, "fixi_interface"))
    yield from _unique(interfaces, ("fixi_name",), "interface")
    sessions = [
        (f"{place}/fixi_sessions/fixi_session/{i}", s)
        for place, interface in interfaces
        for i, s in enumerate(
            (interface.get("fixi_sessions") or {}).get("fixi_session") or []
        )
    ]
    yield from _unique(sessions, ("fixi_name",), "session")


# References


def _walk(value, place="") -> Iterator[tuple[str, str, dict]]:
    """Every object in a record, with its pointer and the key that holds it."""
    if isinstance(value, dict):
        for key, inner in value.items():
            for item_place, item in (
                [(f"{place}/{key}/{i}", v) for i, v in enumerate(inner)]
                if isinstance(inner, list)
                else [(f"{place}/{key}", inner)]
            ):
                if isinstance(item, dict):
                    yield item_place, key, item
                    yield from _walk(item, item_place)


def _defined(record, container, item) -> set[tuple[int, str]]:
    return {
        (e["fixr_id"], e.get("fixr_scenario", BASE))
        for _, e in _items(record, container, item)
    }


def _reference_errors(record) -> Iterator[tuple[str, str]]:
    targets = {
        "fixr_field_ref": ("field", _defined(record, "fixr_fields", "fixr_field")),
        "fixr_num_in_group": ("field", _defined(record, "fixr_fields", "fixr_field")),
        "fixr_component_ref": (
            "component",
            _defined(record, "fixr_components", "fixr_component"),
        ),
        "fixr_group_ref": ("group", _defined(record, "fixr_groups", "fixr_group")),
        "fixr_message_ref": (
            "message",
            _defined(record, "fixr_messages", "fixr_message"),
        ),
    }
    categories = {
        c["fixr_name"] for _, c in _items(record, "fixr_categories", "fixr_category")
    }
    sections = {
        s["fixr_name"] for _, s in _items(record, "fixr_sections", "fixr_section")
    }
    actors = {}
    flows = set()
    for _, member in _items(record, "fixr_actors", "fixr_members"):
        if "fixr_flow" in member:
            flows.add(member["fixr_flow"]["fixr_name"])
        if "fixr_actor" in member:
            actor = member["fixr_actor"]
            machines, timers = {}, set()
            for item in actor.get("fixr_members") or []:
                if "fixr_states" in item:
                    machine = item["fixr_states"]
                    states = [machine["fixr_initial"], *machine["fixr_state"]]
                    machines[machine["fixr_name"]] = {
                        "states": {s["fixr_name"] for s in states},
                        "transitions": {
                            t["fixr_name"]
                            for s in states
                            for t in s.get("fixr_transition") or []
                        },
                    }
                if "fixr_timer" in item:
                    timers.add(item["fixr_timer"]["fixr_name"])
            actors[actor["fixr_name"]] = (machines, timers)
    for place, key, item in _walk(record):
        if key in targets:
            label, defined = targets[key]
            ref = (item["fixr_id"], item.get("fixr_scenario", BASE))
            if ref not in defined:
                yield (
                    f"{place}/fixr_id",
                    f"no {label} has the number {ref[0]} in {ref[1]}",
                )
        if key in ("fixr_message", "fixr_component", "fixr_group") and categories:
            if "fixr_category" in item and item["fixr_category"] not in categories:
                yield (
                    f"{place}/fixr_category",
                    f"no category is named {item['fixr_category']}",
                )
        if key == "fixr_category" and sections and "fixr_section" in item:
            if item["fixr_section"] not in sections:
                yield (
                    f"{place}/fixr_section",
                    f"no section is named {item['fixr_section']}",
                )
        if (
            key == "fixr_message"
            and "fixr_flow" in item
            and item["fixr_flow"] not in flows
        ):
            yield f"{place}/fixr_flow", f"no flow is named {item['fixr_flow']}"
        if key == "fixr_trigger":
            machines, _ = actors.get(item["fixr_actor"], ({}, set()))
            machine = machines.get(item["fixr_state_machine"])
            if item["fixr_actor"] not in actors:
                yield f"{place}/fixr_actor", f"no actor is named {item['fixr_actor']}"
            elif machine is None:
                yield (
                    f"{place}/fixr_state_machine",
                    f"{item['fixr_actor']} has no state machine {item['fixr_state_machine']}",
                )
            elif item["fixr_name"] not in machine["transitions"]:
                yield (
                    f"{place}/fixr_name",
                    f"no transition is named {item['fixr_name']}",
                )
        if key == "fixr_timer_schedule":
            if item["fixr_actor"] not in actors:
                yield f"{place}/fixr_actor", f"no actor is named {item['fixr_actor']}"
            elif item["fixr_name"] not in actors[item["fixr_actor"]][1]:
                yield (
                    f"{place}/fixr_name",
                    f"{item['fixr_actor']} has no timer {item['fixr_name']}",
                )
        if key == "fixr_states":
            states = {
                s["fixr_name"] for s in [item["fixr_initial"], *item["fixr_state"]]
            }
            for i, state in enumerate([item["fixr_initial"], *item["fixr_state"]]):
                state_place = (
                    f"{place}/fixr_initial" if i == 0 else f"{place}/fixr_state/{i - 1}"
                )
                for j, transition in enumerate(state.get("fixr_transition") or []):
                    if transition["fixr_target"] not in states:
                        yield (
                            f"{state_place}/fixr_transition/{j}/fixr_target",
                            f"no state of this machine is named {transition['fixr_target']}",
                        )


KEY_RULES = {
    "OrchestraRepositoryV10": _v10_keys,
    "OrchestraRepositoryV11": _v11_keys,
    "OrchestraInterfacesV10": _interfaces_keys,
    "OrchestraInterfacesV11": _interfaces_keys,
}


def rule_errors(class_name: str, record: dict) -> list[tuple[str, str]]:
    """Each rule a whole file breaks, as a JSON pointer and a sentence."""
    found = list(KEY_RULES[class_name](record))
    if class_name.startswith("OrchestraRepository"):
        found += list(_reference_errors(record))
    return found
