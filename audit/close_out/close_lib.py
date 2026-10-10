# -*- coding: utf-8 -*-
"""Shared helpers for the close-out transactions (CLOSE-1 … CLOSE-5, AR-1; brief audit/close_out/BRIEF.md).

Builds on audit/release_candidate/rc_lib.py: every write is an exact-value-checked cell write, recorded in the ledger;
audit/tranche_b_execution/run_stage.py commits the staged Master or rolls it back.

refresh_self_counts (OWN-10): the Master describes itself twice — 00_MASTER rows 14–26 ("Actual" is a formula cache or a
constant, "Expected" a constant) and 37_READINESS_CHECKLIST rows 5–21 ("Expected" a constant, "Actual" a formula cache or
a constant). Both had drifted (143 pages, 10 Readings, 165 sources). Every close-out transaction calls this last, so the
counts are recomputed from the sheets themselves in the same staged Master; formulas are kept and only their cached
result moves. The validator gate CO-G01 fails if any of them diverges again.
"""
import os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "release_candidate"))
from rc_lib import Session, Table, TxError, insert_ui_rows, set_ui, formula_of, set_formula_cache  # noqa: E402,F401

S03 = "03_PAGE_SECTIONS"
COL03 = {"heading_en": 4, "body_en": 5, "heading_ar": 6, "body_ar": 7}


def _counta(g, sheet_first=5):
    return sum(1 for r in g[sheet_first - 1:] if r and r[0] not in (None, ""))


def bilingual_sections(g03):
    """Distinct (route, section_order) of 03_PAGE_SECTIONS that carry both English and Arabic text. The rows are split per
    language (one row each, or one row with both), so a section is counted once whatever its row layout."""
    pairs = {}
    for r in g03:
        if not r or not isinstance(r[0], str) or not r[0].startswith("/") or r[1] in (None, ""):
            continue
        k = (r[0], int(float(r[1])))
        en, ar = pairs.get(k, (False, False))
        pairs[k] = (en or bool(r[3] or r[4]), ar or bool(r[5] or r[6]))
    return sum(1 for en, ar in pairs.values() if en and ar)


def true_counts(s):
    """label -> count, from the staged Master's own sheets."""
    chron = [r for r in s.grid("14_SYSTEM_CHRONOLOGY")[4:] if r and r[0] not in (None, "")]
    ci = [str(x) for x in s.grid("14_SYSTEM_CHRONOLOGY")[3]].index("event_class")
    return OrderedDict([
        ("site_pages", _counta(s.grid("02_SITE_MAP"))),
        ("bilingual_sections", bilingual_sections(s.grid(S03))),
        ("questions", _counta(s.grid("05_QUESTIONS"))),
        ("evidence_objects", _counta(s.grid("06_EVIDENCE_OBJECTS"))),
        ("public_claims", _counta(s.grid("07_PUBLIC_CLAIMS"))),
        ("readings", _counta(s.grid("08_READINGS"))),
        ("measurement", _counta(s.grid("10_MEASUREMENT_AGENDA"))),
        ("visuals", _counta(s.grid("11_VISUAL_LIBRARY"))),
        ("relationships", _counta(s.grid("13_SYSTEM_RELATIONSHIPS"))),
        ("dated_events", sum(1 for r in chron if r[ci] != "SYSTEM_INTERPRETATION")),
        ("sources", _counta(s.grid("15_SOURCE_LIBRARY"))),
        ("datasets", _counta(s.grid("16_DATASET_CATALOG"))),
        ("indicators", _counta(s.grid("17_INDICATOR_LIBRARY"))),
        ("cby_monetary", _counta(s.grid("18_CBY_MONETARY"))),
        ("payments", _counta(s.grid("19_PAYMENTS_DATA"))),
        ("firm_finance", _counta(s.grid("20_FIRM_FINANCE"))),
        ("remittances", _counta(s.grid("23_REMITTANCES"))),
    ])


# (sheet, row, label in column A or B, count key, columns: actual, expected)
SELF_COUNT_CELLS = [
    ("00_MASTER", 14, "Site pages", "site_pages", 2, 3),
    ("00_MASTER", 15, "Bilingual page sections", "bilingual_sections", 2, 3),
    ("00_MASTER", 16, "Questions", "questions", 2, 3),
    ("00_MASTER", 17, "Evidence objects", "evidence_objects", 2, 3),
    ("00_MASTER", 18, "Public claims", "public_claims", 2, 3),
    ("00_MASTER", 19, "Readings", "readings", 2, 3),
    ("00_MASTER", 20, "Measurement priorities", "measurement", 2, 3),
    ("00_MASTER", 21, "Visual objects", "visuals", 2, 3),
    ("00_MASTER", 22, "System relationships", "relationships", 2, 3),
    ("00_MASTER", 23, "Chronology events", "dated_events", 2, 3),
    ("00_MASTER", 24, "Sources", "sources", 2, 3),
    ("00_MASTER", 25, "Datasets", "datasets", 2, 3),
    ("00_MASTER", 26, "Indicators", "indicators", 2, 3),
    ("37_READINESS_CHECKLIST", 5, "All site pages", "site_pages", 4, 3),
    ("37_READINESS_CHECKLIST", 6, "Bilingual page sections", "bilingual_sections", 4, 3),
    ("37_READINESS_CHECKLIST", 7, "Question entry system", "questions", 4, 3),
    ("37_READINESS_CHECKLIST", 8, "Public evidence objects", "evidence_objects", 4, 3),
    ("37_READINESS_CHECKLIST", 9, "Public claims", "public_claims", 4, 3),
    ("37_READINESS_CHECKLIST", 10, "Readings", "readings", 4, 3),
    ("37_READINESS_CHECKLIST", 11, "Measurement agenda", "measurement", 4, 3),
    ("37_READINESS_CHECKLIST", 12, "Visualization objects", "visuals", 4, 3),
    ("37_READINESS_CHECKLIST", 13, "System relationships", "relationships", 4, 3),
    ("37_READINESS_CHECKLIST", 14, "Chronology events", "dated_events", 4, 3),
    ("37_READINESS_CHECKLIST", 15, "Source records", "sources", 4, 3),
    ("37_READINESS_CHECKLIST", 16, "Dataset catalogue", "datasets", 4, 3),
    ("37_READINESS_CHECKLIST", 17, "Indicator library", "indicators", 4, 3),
    ("37_READINESS_CHECKLIST", 18, "CBY monetary observations", "cby_monetary", 4, 3),
    ("37_READINESS_CHECKLIST", 19, "Payment observations", "payments", 4, 3),
    ("37_READINESS_CHECKLIST", 20, "Firm finance observations", "firm_finance", 4, 3),
    ("37_READINESS_CHECKLIST", 21, "Remittance observations", "remittances", 4, 3),
]


def _set_count(s, finding, sheet, row, col, new):
    f = formula_of(s, sheet, row, col)
    cur = s.ed.get_value(sheet, row, col)            # the editor returns cell text ("144"), the new count is an int
    if str(cur) == str(new):
        return
    if f is not None:
        set_formula_cache(s, finding, sheet, row, col, new, cur if not isinstance(cur, float) or cur != int(cur) else int(cur),
                          f, f"{sheet}!r{row}c{col}")
    else:
        s.set(finding, sheet, row, col, new, cur, f"{sheet}!r{row}c{col}")


def refresh_self_counts(s, finding):
    """Set every self-count of 00_MASTER and 37_READINESS_CHECKLIST to the value counted from the staged sheets."""
    counts = true_counts(s)
    for sheet, row, label, key, c_act, c_exp in SELF_COUNT_CELLS:
        g = s.grid(sheet)
        r = g[row - 1]
        if label not in (r[0], r[1]):
            raise TxError(f"{finding}: {sheet}!r{row} is not '{label}': {r[:2]!r}")
        for col in (c_act, c_exp):
            _set_count(s, finding, sheet, row, col, counts[key])
    return counts


# ------------------------------------------------------------------------------------------------
# The adjudicated Arabic register (audit/arabic_review/YFIE_ARABIC_ACCEPTED_EDIT_REGISTER_2026-10-10.csv, D11)
# ------------------------------------------------------------------------------------------------
import csv, hashlib, re  # noqa: E402

REGISTER = os.path.join(HERE, "..", "arabic_review", "YFIE_ARABIC_ACCEPTED_EDIT_REGISTER_2026-10-10.csv")


def register_rows():
    with open(REGISTER, encoding="utf-8-sig", newline="") as fh:
        return {r["review_id"].split(":")[-1]: r for r in csv.DictReader(fh)}


def _h(t):
    return hashlib.sha256(t.encode("utf-8")).hexdigest()


def register_cell(row):
    m = re.match(r"(\w+)!R(\d+)C(\d+)", row["master_cell"])
    if not m:
        raise TxError(f"{row['review_id']}: master_cell {row['master_cell']!r} is not one cell")
    return m.group(1), int(m.group(2)), int(m.group(3))


def apply_register_ar(s, finding, row, new_ar=None, expect_old=None):
    """Write a register row's Arabic: the cell must hold exact_old_ar (or `expect_old`, when an earlier transaction of this
    brief changed the same cell; the merge is recorded by the caller), and exact_old_ar must hash to original_sha256. The
    new text is the register's new_ar unless `new_ar` is given (a conditional row's final form); the register's own text
    must hash to new_ar_sha256. No fuzzy or regex replacement: whole-cell, exact-value writes only."""
    rid = row["review_id"]
    if _h(row["exact_old_ar"]) != row["original_sha256"]:
        raise TxError(f"{finding} {rid}: exact_old_ar does not hash to original_sha256")
    if row["new_ar"] and row.get("new_ar_sha256") and _h(row["new_ar"]) != row["new_ar_sha256"]:
        raise TxError(f"{finding} {rid}: new_ar does not hash to new_ar_sha256")
    sheet, r, c = register_cell(row)
    cur = s.ed.get_value(sheet, r, c)
    want = row["exact_old_ar"] if expect_old is None else expect_old
    if cur != want:
        raise TxError(f"{finding} {rid}: MISMATCH at {sheet}!R{r}C{c}: holds {str(cur)[:80]!r}")
    s.set(f"{finding}:{rid}", sheet, r, c, new_ar if new_ar is not None else row["new_ar"], cur, f"{sheet}!R{r}C{c}")
    return sheet, r, c


def en_cell_of(s, row):
    """The English cell paired with a register row's Arabic cell."""
    sheet, r, c = register_cell(row)
    if sheet == S03:
        sel = dict(kv.strip().split("=", 1) for kv in row["selector"].split(";") if "=" in kv)
        field = row["field"].replace("_ar", "")
        rr = s.section_row(sel["route"], int(sel["section_order"]), "en")
        return S03, rr, COL03[field + "_en"]
    if sheet == "04_NAV_UX":
        return sheet, r, c - 1                       # label_en is the column before label_ar
    if sheet == "06_EVIDENCE_OBJECTS":
        return sheet, r, c - 1                       # every *_ar column follows its *_en column
    raise TxError(f"{row['review_id']}: no English pairing rule for {sheet}")


def apply_register_en(s, finding, row, new_en, must_start=None):
    sheet, r, c = en_cell_of(s, row)
    cur = s.ed.get_value(sheet, r, c)
    if must_start is not None and not str(cur).startswith(must_start):
        raise TxError(f"{finding} {row['review_id']}: EN cell {sheet}!R{r}C{c} does not start with {must_start[:50]!r}")
    s.set(f"{finding}:{row['review_id']}", sheet, r, c, new_en, cur, f"{sheet}!R{r}C{c}")
