# -*- coding: utf-8 -*-
"""Projection families: every governed JSON output is built here from the Production Master.

This module contains transformation rules only. Public copy, facts and controlled boilerplate are
read from the Master or from the declared controlled inputs in ./controlled_inputs (never from code).
"""
import json
import re
from collections import OrderedDict

from .structure import StructureError, blocks, keyed_records

NUM_TEXT = re.compile(r"-?\d+(\.\d+)?")


# ------------------------------------------------------------------------------------------------
# Generic helpers
# ------------------------------------------------------------------------------------------------
def slash(route):
    return route if route.endswith("/") else route + "/"


def pipe_list(v):
    return [x.strip() for x in v.split("|") if x.strip()] if isinstance(v, str) else []


def json_or_keep(v):
    """Decode a JSON array/object held as text; any other value is kept unchanged."""
    if isinstance(v, str):
        try:
            x = json.loads(v)
        except ValueError:
            return v
        if isinstance(x, (list, dict)):
            return x
    return v


def json_list_or_empty(v):
    """Decode a JSON array held as text; anything that is not a JSON array becomes []."""
    if isinstance(v, str):
        try:
            x = json.loads(v)
        except ValueError:
            return []
        if isinstance(x, list):
            return x
    return []


def numeric_text(v):
    """Declared numeric-text normalisation: '2017' -> 2017, '38.003' -> 38.003, '1262.0' -> 1262."""
    if isinstance(v, str) and NUM_TEXT.fullmatch(v):
        f = float(v)
        if "." not in v:
            return int(v)
        return int(f) if f.is_integer() else f
    return v


TRANSFORMS = {
    "json": json_or_keep,
    "json_list_or_empty": json_list_or_empty,
    "slash": lambda v: slash(v) if isinstance(v, str) and v.startswith("/") else v,
    "numeric_text": numeric_text,
    "first_pipe": lambda v: pipe_list(v)[0] if pipe_list(v) else v,
    "semicolon_list": lambda v: [x.strip() for x in v.split(";") if x.strip()] if isinstance(v, str) else [],
    # Tranche C (JRN-02): 06 public_routes is authored as a ' | ' list of routes; it was read as JSON and projected empty.
    "pipe_route_list": lambda v: [slash(x) for x in pipe_list(v)],
}


# ------------------------------------------------------------------------------------------------
# Structure contract
# ------------------------------------------------------------------------------------------------
def validate_structure(wb, contract):
    """Assert that every sheet's block layout equals the declared contract. Fail loudly otherwise."""
    problems = []
    declared = contract["sheets"]
    if list(declared) != wb.sheet_names:
        problems.append(f"sheet list differs from contract: {wb.sheet_names} vs {list(declared)}")
    for name in wb.sheet_names:
        if name not in declared:
            continue
        spec = declared[name]
        grid = wb.grid(name)
        found = blocks(grid, name)
        # declared titled blocks that have no blank separator are recognised explicitly
        titles_found = [b["title"] for b in found[1:]]
        for extra in spec.get("unseparated_block_titles", []):
            rows = [i for i, r in enumerate(grid) if r and r[0] == extra and not any(c not in (None, "") for c in r[1:])]
            if len(rows) != 1:
                problems.append(f"{name}: declared unseparated block {extra!r} found {len(rows)} times")
            else:
                titles_found.append(extra)
        if found[0]["header_row"] != spec["main_header_row"]:
            problems.append(f"{name}: main header row {found[0]['header_row']} != declared {spec['main_header_row']}")
        if [x for x in titles_found] != [b["title"] for b in spec["blocks"]] and sorted(titles_found) != sorted(b["title"] for b in spec["blocks"]):
            problems.append(f"{name}: titled blocks {titles_found} != declared {[b['title'] for b in spec['blocks']]}")
        if spec.get("main_labels") and found[0]["labels"][: len(spec["main_labels"])] != spec["main_labels"]:
            problems.append(f"{name}: main header labels changed: {found[0]['labels']} vs declared {spec['main_labels']}")
    if problems:
        raise StructureError("Production Master structure does not match the declared contract:\n  " + "\n  ".join(problems))


def block_ranges(wb, name, contract):
    """Return [(block_key, first_row, last_row)] with 1-based rows; block_key '__pre__' | '__main__' | title."""
    grid = wb.grid(name)
    spec = contract["sheets"][name]
    titles = [b["title"] for b in spec["blocks"]]
    starts = []
    for i, r in enumerate(grid, 1):
        if r and r[0] in titles and not any(c not in (None, "") for c in r[1:]):
            starts.append((i, r[0]))
    out = [("__pre__", 1, spec["main_header_row"])]
    first_main = spec["main_header_row"] + 1
    bounds = [first_main] + [s for s, _ in starts] + [len(grid) + 1]
    keys = ["__main__"] + [t for _, t in starts]
    for k, a, b in zip(keys, bounds[:-1], bounds[1:]):
        out.append((k, a, b - 1))
    return out


# ------------------------------------------------------------------------------------------------
# Raw sheet snapshots (whole grid)
# ------------------------------------------------------------------------------------------------
def snapshot(wb, name, contract):
    grid = wb.grid(name)
    numcols = contract["sheets"][name].get("numeric_text_columns", {})
    rows = [list(r) for r in grid]
    if numcols:
        for key, a, b in block_ranges(wb, name, contract):
            cols = numcols.get(key, [])
            for r in range(a, b + 1):
                for j in cols:
                    if j < len(rows[r - 1]):
                        rows[r - 1][j] = numeric_text(rows[r - 1][j])
    return OrderedDict([("sheet", name), ("rows", rows)])


# ------------------------------------------------------------------------------------------------
# Keyed record families
# ------------------------------------------------------------------------------------------------
def keyed(wb, name, contract, fields=None):
    """Main-block keyed records in sheet order with declared per-field transforms."""
    spec = contract["sheets"][name]
    if spec["blocks"]:
        raise StructureError(f"{name}: keyed family expects a single-block sheet")
    recs = keyed_records(wb.grid(name), name)
    expected = spec.get("main_labels")
    out = []
    for _, rec in recs:
        if expected and list(rec.keys()) != [x for x in expected if not x.startswith("col")]:
            raise StructureError(f"{name}: record keys differ from declared labels")
        o = OrderedDict()
        for k, v in rec.items():
            t = (fields or {}).get(k)
            o[k] = TRANSFORMS[t](v) if t else v
        out.append(o)
    return out


def block_projection(ctx, e):
    """Keyed records of one titled block (Stage 1: 04 'Governed interface copy'), keys in header order."""
    out = []
    for _, rec in keyed_records(ctx.wb.grid(e["sheet"]), e["sheet"], block=e["block"]):
        out.append(OrderedDict((k, v) for k, v in rec.items()))
    key = e.get("stable_key")
    if key:
        seen = set()
        for r in out:
            if r.get(key) in (None, "") or r[key] in seen:
                raise StructureError(f"{e['path']}: missing or duplicate stable key {key}={r.get(key)!r}")
            seen.add(r[key])
    return out
