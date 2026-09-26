# -*- coding: utf-8 -*-
"""Master-first patch execution engine (Tranche B, Stages 2–5).

Executes the governed patch specification (audit/MASTER_FIRST_PATCH_SPEC.csv) against the Production Master:
  * a patch root (PB-nnnn, before the first '.') is one transaction: all of its rows apply, or none;
  * every SUBSTR row is applied to the exact cell named by its Excel row and field, only if the exact current
    substring occurs exactly the stated number of times (no fuzzy matching, no silent skip);
  * structural roots (new sections, new columns, row removals) run through named handlers that check the exact
    current cell values before writing.
The engine never writes a projection; the stage runner regenerates everything from the saved Master.
"""
import csv
import json
import os
import re
import sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from projection.master_reader import Workbook                      # noqa: E402
from projection.master_writer import MasterEditor, MasterWriteError  # noqa: E402

LOC_SUBSTR = re.compile(r"Excel row (\d+); exact-substring replace(?: in this cell only)? \((\d+)(?:×| occurrence)")
DELETE_PREFIX = "(DELETE"


class RootFailure(Exception):
    pass


def load_spec(path):
    roots = OrderedDict()
    with open(path, encoding="utf-8-sig", newline="") as fh:
        for r in csv.DictReader(fh):
            roots.setdefault(r["patch_id"].split(".")[0], []).append(r)
    return roots


def export_labels(grid):
    """Field names exactly as the spec builder saw them: labels of the sheet's main header row, colN when blank."""
    h = next(i for i, r in enumerate(grid[:6]) if sum(1 for c in r if c not in (None, "")) >= 3)
    return h + 1, [str(c) if c not in (None, "") else f"col{j}" for j, c in enumerate(grid[h])]


def parse_sections(text):
    """'EN heading: … || EN body: … || AR heading: … || AR body: …' -> dict."""
    out = {}
    for part in text.split(" || "):
        m = re.match(r"(EN|AR) (heading|body): (.*)$", part.strip(), re.S)
        if not m:
            raise RootFailure(f"unparseable section text part: {part[:80]!r}")
        out[f"{m.group(2)}_{m.group(1).lower()}"] = m.group(3).strip()
    if set(out) != {"heading_en", "body_en", "heading_ar", "body_ar"}:
        raise RootFailure(f"section text lacks fields: {sorted(out)}")
    return out


class Engine:
    def __init__(self, master_path, spec_path):
        self.master_path = master_path
        self.wb = Workbook(master_path)
        self.ed = MasterEditor(master_path)
        self.spec = load_spec(spec_path)
        self.labels = {}
        self.results = OrderedDict()
        self.presentation_edits = []            # (route, new_order, tier) for the controlled presentation contract
        self.section_shifts = []                # (route, from_order, delta)
        self._appended = {}                     # sheet -> next free row for appended rows

    # ------------------------------------------------------------------ helpers
    def col(self, sheet, field):
        if sheet not in self.labels:
            self.labels[sheet] = export_labels(self.wb.grid(sheet))[1]
        labs = self.labels[sheet]
        if field not in labs:
            raise RootFailure(f"{sheet}: field {field!r} not in main header")
        return labs.index(field) + 1

    def value(self, sheet, row, col):
        return self.ed.get_value(sheet, row, col)

    def next_free_row(self, sheet):
        if sheet not in self._appended:
            g = self.wb.grid(sheet)
            self._appended[sheet] = max(i for i, r in enumerate(g, 1) if any(c not in (None, "") for c in r)) + 1
        r = self._appended[sheet]
        self._appended[sheet] += 1
        return r

    # ------------------------------------------------------------------ transactions
    def run_root(self, root, fn, stage):
        snap_xml, snap_log = dict(self.ed._xml), len(self.ed.log)
        snap_app, snap_pres, snap_shift = dict(self._appended), list(self.presentation_edits), list(self.section_shifts)
        try:
            detail = fn(root)
            self.results[root] = OrderedDict([("disposition", "APPLIED"), ("stage", stage), ("detail", detail)])
        except (RootFailure, MasterWriteError) as exc:
            self.ed._xml = snap_xml
            del self.ed.log[snap_log:]
            self._appended, self.presentation_edits, self.section_shifts = snap_app, snap_pres, snap_shift
            self.results[root] = OrderedDict([("disposition", "FAILED"), ("stage", stage), ("detail", str(exc))])

    def hold(self, root, disposition, stage, reason):
        self.results[root] = OrderedDict([("disposition", disposition), ("stage", stage), ("detail", reason)])

    # ------------------------------------------------------------------ SUBSTR rows
    def apply_substr_rows(self, root):
        rows = self.spec[root]
        done = []
        for r in rows:
            m = LOC_SUBSTR.match(r["row_locator_if_needed"])
            if not m:
                raise RootFailure(f"{r['patch_id']}: not an exact-substring row ({r['row_locator_if_needed'][:60]!r})")
            row, n = int(m.group(1)), int(m.group(2))
            old = r["current_value"]
            new = "" if r["proposed_value"].startswith(DELETE_PREFIX) else r["proposed_value"]
            c = self.col(r["sheet"], r["field"])
            self.ed.replace_in_cell(r["sheet"], row, c, old, new, count=n)
            done.append(f"{r['patch_id']}: {r['sheet']}!r{row}.{r['field']} ×{n}")
        return done

    # ------------------------------------------------------------------ 03 sections
    def section_rows(self, route):
        g = self.wb.grid("03_PAGE_SECTIONS")
        return [(i, r) for i, r in enumerate(g, 1) if i > 4 and r and r[0] == route]

    def add_section(self, route, new_order, texts, role_en=None, role_ar=None):
        """Insert a bilingual section at new_order: later sections of the route move +1 (exact-value checked);
        the two new rows (EN, AR) are appended to the end of the sheet (row numbers of other rows never change)."""
        S = "03_PAGE_SECTIONS"
        rows = self.section_rows(route)
        if not rows:
            raise RootFailure(f"03: route {route} has no sections")
        prev = [r for _, r in rows if r[1] == new_order - 1]
        follows_role = (prev[0][2] if prev else None, prev[1][2] if len(prev) > 1 else None)
        for i, r in rows:
            cur = self.value(S, i, 2)
            cur_n = int(float(cur)) if cur not in (None, "") else None
            if cur_n is not None and cur_n >= new_order:
                self.ed.set_cell(S, i, 2, cur_n + 1, expect=cur)
        self.section_shifts.append((route, new_order, 1))
        ren = role_en if role_en is not None else follows_role[0]
        rar = role_ar if role_ar is not None else follows_role[1]
        r_en, r_ar = self.next_free_row(S), self.next_free_row(S)
        for j, v in enumerate([route, new_order, ren, texts["heading_en"], texts["body_en"], None, None], 1):
            if v not in (None, ""):
                self.ed.set_cell(S, r_en, j, v, expect=None)
        for j, v in enumerate([route, new_order, rar, None, None, texts["heading_ar"], texts["body_ar"]], 1):
            if v not in (None, ""):
                self.ed.set_cell(S, r_ar, j, v, expect=None)
        return r_en, r_ar, (prev[0][1] if prev else None)

    def new_section_root(self, root, tier_rule="follow", role=None):
        rows = self.spec[root]
        if len(rows) != 1:
            raise RootFailure(f"{root}: expected one NEW row")
        r = rows[0]
        m = re.match(r"(/[^ ]*/) NEW section \((?:insert as )?section_order (\d+)", r["stable_object_id"])
        after = re.match(r"(/[^ ]*/) NEW section \(insert after (PB-\d+)\)", r["stable_object_id"])
        if m:
            route, order = m.group(1), int(m.group(2))
        elif after:
            route = after.group(1)
            prev_root = after.group(2)
            prev = self.results.get(prev_root)
            if not prev or prev["disposition"] != "APPLIED":
                raise RootFailure(f"{root}: depends on {prev_root}, which is not applied")
            order = prev["detail"]["section_order"] + 1
        else:
            raise RootFailure(f"{root}: cannot read target route/order from {r['stable_object_id'][:80]!r}")
        texts = parse_sections(r["proposed_value"])
        r_en, r_ar, follows = self.add_section(route, order, texts, *(role or (None, None)))
        self.presentation_edits.append((route, order, tier_rule))
        return OrderedDict([("route", route), ("section_order", order), ("rows_appended", [r_en, r_ar]), ("follows_section", order - 1)])


# ---------------------------------------------------------------------- controlled presentation contract
def apply_presentation_edits(pp, shifts, edits):
    """Shift section references for inserted sections and place each new section in the tier of the section it follows
    (primary if that section is primary, otherwise progressive). Returns the edited contract and a change log."""
    log = []
    routes = {r["route"]: r for r in pp.get("routes", [])}
    for (route, new_order, delta), (_, _, tier_rule) in zip(shifts, edits):
        r = routes.get(route)
        if r is None:
            log.append(f"{route}: not a presentation-contract route (rendered in order by the generic section renderer)")
            continue
        for tier, items_ in r.items():                        # every tier list that references sections
            if not isinstance(items_, list):
                continue
            for item in items_:
                if isinstance(item, dict) and item.get("kind") == "section" and isinstance(item.get("section_order"), int) and item["section_order"] >= new_order:
                    item["section_order"] += delta
        follows = new_order - 1
        prim = [i for i in r.get("primary", []) if i.get("kind") == "section"]
        in_primary = any(i["section_order"] == follows for i in prim) or follows <= 1
        tier = tier_rule if tier_rule in ("primary", "progressive") else ("primary" if in_primary else "progressive")
        items = r.setdefault(tier, [])
        pos = next((k for k, i in enumerate(items) if i.get("kind") == "section" and i["section_order"] > new_order), None)
        if pos is None:
            pos = next((k for k, i in enumerate(items) if i.get("kind") != "section"), len(items))
        items.insert(pos, OrderedDict([("kind", "section"), ("section_order", new_order)]))
        if tier == "progressive":                              # progressive sections are excluded from first load
            ex = r.setdefault("first_load_exclusions", [])
            ex.append(OrderedDict([("kind", "section"), ("section_order", new_order)]))
            ex.sort(key=lambda i: i.get("section_order", 0))
        log.append(f"{route}: section {new_order} added to {tier}; later section references shifted +{delta}")
    return pp, log
