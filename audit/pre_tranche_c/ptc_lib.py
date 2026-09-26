# -*- coding: utf-8 -*-
"""Shared helpers for the Pre-Tranche-C maturation transactions (P1-P4).

Every Master change is an exact-value-checked cell write through scripts/projection/master_writer.MasterEditor.
A transaction script builds a staged Master plus a JSON ledger; audit/tranche_b_execution/run_stage.py then commits it
(regenerate -> rebind -> build -> literal audit -> validate -> generator --check) or rolls it back.
"""
import hashlib, json, os, sys, tempfile
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from projection.master_reader import Workbook            # noqa: E402
from projection.master_writer import MasterEditor        # noqa: E402

S03 = "03_PAGE_SECTIONS"
COL03 = {"route": 1, "section_order": 2, "section_role": 3, "heading_en": 4, "body_en": 5, "heading_ar": 6, "body_ar": 7}


class TxError(Exception):
    pass


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


class Session:
    def __init__(self, master_path, work_dir):
        self.src = master_path
        self.work = work_dir
        os.makedirs(work_dir, exist_ok=True)
        self.ed = MasterEditor(master_path)
        self.ledger = []

    # current (edited) state of a sheet
    def grid(self, sheet):
        tmp = tempfile.NamedTemporaryFile(suffix=".xlsx", delete=False, dir=self.work)
        tmp.close()
        self.ed.save(tmp.name)
        try:
            return Workbook(tmp.name).grid(sheet)
        finally:
            os.remove(tmp.name)

    def header(self, sheet, header_row):
        return [str(x) if x is not None else None for x in self.grid(sheet)[header_row - 1]]

    def set(self, finding, sheet, row, col, new, expect, field=None):
        old = self.ed.get_value(sheet, row, col)
        if old != expect:
            raise TxError(f"{finding}: {sheet}!r{row}c{col} holds {str(old)[:90]!r}, expected {str(expect)[:90]!r}")
        if old == new:
            return
        self.ed.set_cell(sheet, row, col, new, expect=expect)
        self.ledger.append(OrderedDict([("finding", finding), ("sheet", sheet), ("row", row), ("col", col), ("field", field),
                                        ("old", old), ("new", new)]))

    def replace(self, finding, sheet, row, col, old_sub, new_sub, field=None):
        cur = self.ed.get_value(sheet, row, col)
        if not isinstance(cur, str) or cur.count(old_sub) != 1:
            raise TxError(f"{finding}: {sheet}!r{row}c{col}: substring occurs {0 if not isinstance(cur, str) else cur.count(old_sub)} times: {old_sub[:70]!r}")
        self.set(finding, sheet, row, col, cur.replace(old_sub, new_sub), cur, field)

    # 03 section cells, located by (route, order, language)
    def section_row(self, route, order, lang):
        # row positions of 03 never move in a cell-write transaction; the index is read once
        if getattr(self, "_g03", None) is None:
            self._g03 = self.grid(S03)
        g = self._g03
        hits = []
        for i, r in enumerate(g, 1):
            if i <= 4 or not r or r[0] != route or r[1] in (None, ""):
                continue
            if int(float(r[1])) != int(order):
                continue
            if r[COL03["heading_" + lang] - 1] not in (None, "") or r[COL03["body_" + lang] - 1] not in (None, ""):
                hits.append(i)
        if len(hits) != 1:
            raise TxError(f"03 {route} s{order} {lang}: {len(hits)} rows")
        return hits[0]

    def set_section(self, finding, route, order, lang, field, new, expect):
        row = self.section_row(route, order, lang)
        self.set(finding, S03, row, COL03[f"{field}_{lang}"], new, expect, f"{route}#s{order}.{field}_{lang}")

    def rewrite_section(self, finding, route, order, lang, field, new, must_start):
        """Replace a whole 03 cell whose current value is guarded by its opening words (the authored first sentence)."""
        row = self.section_row(route, order, lang)
        col = COL03[f"{field}_{lang}"]
        cur = self.ed.get_value(S03, row, col)
        if not isinstance(cur, str) or not cur.startswith(must_start):
            raise TxError(f"{finding}: {route}#s{order}.{field}_{lang} does not start with {must_start[:60]!r}: {str(cur)[:80]!r}")
        self.set(finding, S03, row, col, new, cur, f"{route}#s{order}.{field}_{lang}")

    def replace_section(self, finding, route, order, lang, field, old_sub, new_sub):
        row = self.section_row(route, order, lang)
        self.replace(finding, S03, row, COL03[f"{field}_{lang}"], old_sub, new_sub, f"{route}#s{order}.{field}_{lang}")

    # EXF-002: 02 full_copy_* = title + (heading, body) of every 03 section of the route in section order
    def regenerate_full_copy(self, finding="EXF-002"):
        g02, g03 = self.grid("02_SITE_MAP"), self.grid(S03)
        changed = []
        for i, r in enumerate(g02[4:], start=5):
            if not r or not r[0]:
                continue
            rows = [x for x in g03[4:] if x and x[0] == r[0]]
            rows.sort(key=lambda x: int(float(x[1])) if x[1] not in (None, "") else 0)
            for lang, col, tcol in (("en", 7, 5), ("ar", 8, 6)):
                hi, bi = (3, 4) if lang == "en" else (5, 6)
                parts = [r[tcol - 1]] + [v for x in rows for v in (x[hi], x[bi]) if v not in (None, "")]
                new = "\n\n".join(parts)
                if r[col - 1] != new:
                    self.set(finding, "02_SITE_MAP", i, col, new, r[col - 1], f"{r[0]}.full_copy_{lang}")
                    changed.append(f"{r[0]} {lang}")
        return changed

    def save(self, out_master, ledger_path, meta):
        data = self.ed.save(out_master)
        rep = OrderedDict(meta)
        rep["input_master_sha256"] = sha(self.src)
        rep["output_master_sha256"] = hashlib.sha256(data).hexdigest()
        rep["cells_written"] = len(self.ledger)
        rep["changes"] = self.ledger
        with open(ledger_path, "w", encoding="utf-8") as fh:
            json.dump(rep, fh, ensure_ascii=False, indent=1)
        return rep
