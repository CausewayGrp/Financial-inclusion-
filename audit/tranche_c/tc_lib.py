# -*- coding: utf-8 -*-
"""Shared helpers for Tranche C Master transactions.

Builds on audit/pre_tranche_c/ptc_lib.Session: every write is an exact-value-checked cell write, recorded in the ledger.
The transaction scripts stage a Master; audit/tranche_b_execution/run_stage.py commits it or rolls it back.
"""
import os, sys
from collections import OrderedDict
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "pre_tranche_c"))
from ptc_lib import Session, TxError  # noqa: E402,F401


def norm(v):
    if v is None:
        return ""
    return str(v).strip() if isinstance(v, str) else str(v)


class Table:
    """A keyed table in a Master sheet: header on `header_row`, key in column 1."""

    def __init__(self, s, sheet, header_row=4):
        self.s, self.sheet, self.hr = s, sheet, header_row
        g = s.grid(sheet)
        self.head = [str(x) if x is not None else None for x in g[header_row - 1]]
        self.rows = OrderedDict()
        for i, r in enumerate(g[header_row:], start=header_row + 1):
            if r and r[0] not in (None, ""):
                if r[0] in self.rows:
                    raise TxError(f"{sheet}: duplicate key {r[0]}")
                self.rows[r[0]] = i

    def col(self, field):
        if self.head.count(field) != 1:
            raise TxError(f"{self.sheet}: header {field!r} occurs {self.head.count(field)} times")
        return self.head.index(field) + 1

    def get(self, key, field):
        return self.s.ed.get_value(self.sheet, self.rows[key], self.col(field))

    def set(self, finding, key, field, new, old):
        """Write `new` if the cell still holds `old` (compared after whitespace normalisation)."""
        if key not in self.rows:
            raise TxError(f"{finding}: {self.sheet} has no row {key}")
        cur = self.get(key, field)
        if norm(cur) != norm(old):
            raise TxError(f"{finding}: {self.sheet} {key}.{field} holds {norm(cur)[:100]!r}; expected {norm(old)[:100]!r}")
        if norm(cur) == norm(new):
            return False
        self.s.set(finding, self.sheet, self.rows[key], self.col(field), new, cur, f"{key}.{field}")
        return True


def ui_block_end(s):
    """1-based row of the last row of the 04 governed interface-copy block (the block ends before 'Trust navigation')."""
    g04 = s.grid("04_NAV_UX")
    ui = {x[0]: i for i, x in enumerate(g04, 1) if x and isinstance(x[0], str) and x[0].startswith("UI-")}
    last = max(i for i in ui.values() if i < 300)
    if any(c not in (None, "") for c in g04[last]) or g04[last + 1][0] != "Trust navigation":
        raise TxError("04: interface-copy block end not where expected")
    return last, ui


def insert_ui_rows(s, finding, rows):
    """rows: [(ui_id, label_en, label_ar, use_rule)] appended to the end of the 04 interface-copy block."""
    last, ui = ui_block_end(s)
    for r in rows:
        if r[0] in ui:
            raise TxError(f"{finding}: 04 already has {r[0]}")
    s.ed.insert_rows("04_NAV_UX", last + 1, [{1: a, 2: b, 3: c, 4: d} for a, b, c, d in rows])
    for a, b, c, _ in rows:
        s.ledger.append(OrderedDict([("finding", finding), ("sheet", "04_NAV_UX"), ("row", None), ("col", None), ("field", a),
                                     ("old", None), ("new", b + " || " + c)]))


def set_ui(s, finding, ui_id, label_en, label_ar, old_en, old_ar):
    _, ui = ui_block_end(s)
    if ui_id not in ui:
        raise TxError(f"{finding}: 04 has no {ui_id}")
    row = ui[ui_id]
    if label_en is not None:
        s.set(finding, "04_NAV_UX", row, 2, label_en, old_en, f"{ui_id}.label_en")
    if label_ar is not None:
        s.set(finding, "04_NAV_UX", row, 3, label_ar, old_ar, f"{ui_id}.label_ar")
