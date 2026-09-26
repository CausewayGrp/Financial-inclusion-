# -*- coding: utf-8 -*-
"""P4-A — one Reading truth (P4.2) and a bilingual boundary structure (P4.3), Master-first.

  python3 p4a_execute.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

P4.2 Reading canonical ownership. 03_PAGE_SECTIONS (sections 2-9, rendered) and 08_READINGS thesis (section 1) own
Reading copy. 09_READING_SECTIONS becomes the section index (reading_id, order, section_id, title) with its copy guarded
equal to the owners; the generator derives reading_sections.json from 08/03 and stops if 09 drifts. Adjudication of the
four places where 09 and the owners differed:
  CWR-006 s5  09 wording adopted into 03 (no repeated clause; adds 'welfare change'; smoother Arabic).
  CWR-008 s2  03 kept (aligned with the governed CLM-060 headline); 09 synchronised.
  CWR-004 s1, CWR-007 s1  08 thesis kept (the rendered, stronger text); 09 synchronised.
P4.3 Limitations architecture. 06 limitations_* holds (A) what the evidence does not establish and, when recorded, (B) the
limit of the measure, separated by the authored delimiter ' | '. English carried the delimiter on 38 records; Arabic
carried the same two ideas as two sentences with no delimiter. The delimiter is inserted in the 38 Arabic cells after the
first sentence, which in every case is the prohibition (guarded: it begins «لا يجوز»). No clause is rewritten or moved.
Also: an English word ('corpus') in public Arabic copy of CLM-047 is replaced; two governed labels for the two parts.
"""
import re
import sys
from collections import OrderedDict
from ptc_lib import Session, TxError
from projection.master_reader import Workbook

S04, S06, S07, S08, S09 = "04_NAV_UX", "06_EVIDENCE_OBJECTS", "07_PUBLIC_CLAIMS", "08_READINGS", "09_READING_SECTIONS"


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    wb = Workbook(src)

    # ---- P4.2 Reading ownership -------------------------------------------------------------------------
    g08, g09 = wb.grid(S08), wb.grid(S09)
    h08, h09 = [str(x) for x in g08[3]], [str(x) for x in g09[3]]
    route = {r[0]: r[h08.index("route")] for r in g08[4:] if r and r[0]}
    thesis = {r[0]: (r[h08.index("thesis_en")], r[h08.index("thesis_ar")]) for r in g08[4:] if r and r[0]}
    row09 = {(r[0], int(float(r[1]))): i for i, r in enumerate(g09, 1) if i > 4 and r and r[0]}
    c_en, c_ar = h09.index("copy_en") + 1, h09.index("copy_ar") + 1

    # CWR-006 s5: adopt the 09 wording into the owner (03), both languages
    r09 = row09[("CWR-006", 5)]
    rt = route["CWR-006"].rstrip("/") + "/"
    for lang, col in (("en", c_en), ("ar", c_ar)):
        s.set_section("P4-R01", rt, 5, lang, "body", g09[r09 - 1][col - 1], s.ed.get_value("03_PAGE_SECTIONS", s.section_row(rt, 5, lang), 5 if lang == "en" else 7))
    # CWR-008 s2: synchronise 09 to the owner (03)
    r09 = row09[("CWR-008", 2)]
    rt = route["CWR-008"].rstrip("/") + "/"
    for lang, col in (("en", c_en), ("ar", c_ar)):
        own = s.ed.get_value("03_PAGE_SECTIONS", s.section_row(rt, 2, lang), 5 if lang == "en" else 7)
        s.set("P4-R01", S09, r09, col, own, g09[r09 - 1][col - 1], f"CWR-008.s2.copy_{lang}")
    # CWR-004 s1, CWR-007 s1: synchronise 09 to the thesis (08)
    for rid in ("CWR-004", "CWR-007"):
        r09 = row09[(rid, 1)]
        for k, col in ((0, c_en), (1, c_ar)):
            s.set("P4-R01", S09, r09, col, thesis[rid][k], g09[r09 - 1][col - 1], f"{rid}.s1.copy_{'en' if k == 0 else 'ar'}")
    s.set("P4-R01", S09, 2, 1,
          "Section index of the Readings. Copy is owned by 08_READINGS (section 1 = thesis) and 03_PAGE_SECTIONS (sections 2-9); "
          "the generator derives reading_sections.json from them and stops if this sheet differs. Edit the owners, not this sheet.",
          g09[1][0], "09.description")

    # ---- P4.3 Limitations structure ---------------------------------------------------------------------
    g06 = wb.grid(S06)
    h06 = [str(x) for x in g06[3]]
    le, la = h06.index("limitations_en") + 1, h06.index("limitations_ar") + 1
    n = 0
    for i, r in enumerate(g06, 1):
        if i <= 4 or not r or not r[0]:
            continue
        en, ar = r[le - 1] or "", r[la - 1] or ""
        if " | " not in en:
            continue
        if " | " in ar:
            continue
        parts = re.split(r"(?<=[.؟!])\s+", ar.strip(), maxsplit=1)
        if len(parts) != 2 or not parts[0].startswith("لا يجوز"):
            raise TxError(f"P4-L01 {r[0]}: Arabic limitation does not open with a prohibition sentence followed by the limit")
        s.set("P4-L01", S06, i, la, parts[0] + " | " + parts[1], ar, f"{r[0]}.limitations_ar")
        n += 1
    if n != 38:
        raise TxError(f"P4-L01 expected 38 Arabic cells, found {n}")

    # CLM-047: an English word in public Arabic copy (06 limitations_ar; 07 does_not_prove_ar)
    s.replace("P4-E01", S06, next(i for i, r in enumerate(g06, 1) if r and r[0] == "CLM-047"), la,
              "في corpus العام المعتمد", "في قاعدة الأدلة العامة المعتمدة", "CLM-047.limitations_ar")
    g07 = wb.grid(S07)
    h07 = [str(x) for x in g07[3]]
    s.replace("P4-E01", S07, next(i for i, r in enumerate(g07, 1) if r and r[0] == "CLM-047"), h07.index("does_not_prove_ar") + 1,
              "في corpus العام المعتمد", "في قاعدة الأدلة العامة المعتمدة", "CLM-047.does_not_prove_ar")

    # governed labels for the two parts of the boundary
    g04 = wb.grid(S04)
    last = max(i for i, r in enumerate(g04, 1) if r and isinstance(r[0], str) and r[0].startswith("UI-") and i < 160)
    if g04[last - 1][0] != "UI-VIS-WITHHELD":
        raise TxError(f"04: interface copy ends at {g04[last - 1][0]!r}")
    new = [("UI-EVID-DOES-NOT-ESTABLISH", "What this evidence does not establish", "ما لا يثبته هذا الدليل",
            "Pre-Tranche-C P4.3. Label for part A of 06 limitations (the prohibited inference)."),
           ("UI-EVID-MEASUREMENT-LIMITS", "Limits of the measure", "حدود القياس",
            "Pre-Tranche-C P4.3. Label for part B of 06 limitations (what the measure cannot capture), shown when recorded.")]
    s.ed.insert_rows(S04, last + 1, [{1: a, 2: b, 3: c, 4: d} for a, b, c, d in new])
    for a, b, c, _ in new:
        s.ledger.append(OrderedDict([("finding", "P4-L02"), ("sheet", S04), ("row", None), ("col", None), ("field", a), ("old", None), ("new", b + " || " + c)]))

    changed = s.regenerate_full_copy()
    rep = s.save(out, ledger, [("transaction", "P4-A"), ("scope", "P4.2 Reading ownership; P4.3 bilingual boundary delimiter; CLM-047 Arabic"),
                               ("full_copy_regenerated", changed), ("arabic_delimiters_inserted", n)])
    print(f"P4-A staged: {rep['cells_written']} changes; full copy {changed}; Master {rep['output_master_sha256']}")


if __name__ == "__main__":
    main()
