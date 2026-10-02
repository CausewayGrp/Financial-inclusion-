# -*- coding: utf-8 -*-
"""Shared helpers for the release-candidate transactions (RC-1 … RC-3).

audit/tranche_c/tc_lib.py locates the end of the 04 governed interface-copy block with a row bound (< 300) that held
at Tranche C; the block has since grown to row 489. These helpers find the block by its own structure instead — the
last UI-* row before the "Trust navigation" block title — and are otherwise identical. tc_lib.py is a historical
record and is not edited. set_formula_cache (RC-2) updates the cached result of a formula cell and keeps its formula.
"""
import os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "tranche_c"))
from tc_lib import Session, Table, TxError  # noqa: E402,F401

S04 = "04_NAV_UX"


def ui_block_end(s):
    g04 = s.grid(S04)
    titles = [i for i, x in enumerate(g04, 1) if x and x[0] == "Trust navigation"]
    if len(titles) != 1:
        raise TxError(f"04: 'Trust navigation' title found {len(titles)} times")
    title = titles[0]
    ui = {x[0]: i for i, x in enumerate(g04, 1) if x and isinstance(x[0], str) and x[0].startswith("UI-") and i < title}
    last = max(ui.values())
    if any(c not in (None, "") for c in g04[last]):   # the row after the last UI row is blank, then the title
        raise TxError("04: interface-copy block is not followed by a blank row")
    return last, ui


def insert_ui_rows(s, finding, rows):
    """rows: [(ui_id, label_en, label_ar, use_rule)] appended to the end of the 04 interface-copy block."""
    last, ui = ui_block_end(s)
    for r in rows:
        if r[0] in ui:
            raise TxError(f"{finding}: 04 already has {r[0]}")
    s.ed.insert_rows(S04, last + 1, [{1: a, 2: b, 3: c, 4: d} for a, b, c, d in rows])
    for a, b, c, _ in rows:
        s.ledger.append(OrderedDict([("finding", finding), ("sheet", S04), ("row", None), ("col", None), ("field", a),
                                     ("old", None), ("new", b + " || " + c)]))


def set_ui(s, finding, ui_id, label_en, label_ar, old_en, old_ar):
    _, ui = ui_block_end(s)
    if ui_id not in ui:
        raise TxError(f"{finding}: 04 has no {ui_id}")
    row = ui[ui_id]
    if label_en is not None:
        s.set(finding, S04, row, 2, label_en, old_en, f"{ui_id}.label_en")
    if label_ar is not None:
        s.set(finding, S04, row, 3, label_ar, old_ar, f"{ui_id}.label_ar")


_FCELL = r'<x:c r="{ref}"([^>]*)><x:f>(.*?)</x:f><x:v>(.*?)</x:v></x:c>'


def formula_of(s, sheet, row, col):
    """The formula a cell holds (without '='), or None for a value cell."""
    import re   # noqa: PLC0415
    from projection.master_reader import col_letters   # noqa: PLC0415
    m = re.search(_FCELL.format(ref=f"{col_letters(col)}{row}"), s.ed._get(sheet), re.S)
    return m.group(2) if m else None


def set_formula_cache(s, finding, sheet, row, col, new, expect_cached, expect_formula, field=None):
    """Update only the cached result of a formula cell, keeping the formula: the generator reads cached values, and a
    workbook that recalculates gets the same number from the formula. Both the formula and the cached value are guarded."""
    import re   # noqa: PLC0415
    from projection.master_reader import col_letters   # noqa: PLC0415
    ref = f"{col_letters(col)}{row}"
    text = s.ed._get(sheet)
    hits = list(re.finditer(_FCELL.format(ref=ref), text, re.S))
    if len(hits) != 1:
        raise TxError(f"{finding}: {sheet}!{ref} is not a single formula cell")
    m = hits[0]
    if m.group(2) != expect_formula or m.group(3) != str(expect_cached):
        raise TxError(f"{finding}: {sheet}!{ref} holds ={m.group(2)} cached {m.group(3)!r}, expected ={expect_formula} cached {expect_cached!r}")
    if m.group(3) == str(new):
        return
    cell = f'<x:c r="{ref}"{m.group(1)}><x:f>{m.group(2)}</x:f><x:v>{new}</x:v></x:c>'
    s.ed._put(sheet, text[:m.start()] + cell + text[m.end():])
    s.ledger.append(OrderedDict([("finding", finding), ("sheet", sheet), ("row", row), ("col", col), ("field", field),
                                 ("old", m.group(3)), ("new", new), ("formula_kept", "=" + m.group(2)),
                                 ("note", "cached result of the formula updated; the formula is unchanged and computes the same value")]))
