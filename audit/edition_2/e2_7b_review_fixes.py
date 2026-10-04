# -*- coding: utf-8 -*-
"""Edition 2 transaction E2-7b: the independent bilingual and adversarial review of E2-7 and E2-8, and the gaps the new
gates E2-READ and E2-DATES found, folded in (same batch).

  python3 e2_7b_review_fixes.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Gate findings:
1. QUAL-001 (E2-6, after the ledger was compiled): 31 March 2026 and April 2026 read in IMF CR 26/80 (cover; PDF p. 4);
   the report number and page numbers are locators.
2. CLM-032 and CLM-062: page and table numbers of the originals are locators, not values.
3. VIS-POS-*: "February 2026" (the second design change) read in the February 2026 release.
4. CLM-049: the Arabic label states its phrase as the other labels do.
Reading finding (finance batch): 5. CLM-054: the paper's 3.3 million "active savers" are microfinance banks' savers.
Review findings: listed in REVIEW below.
"""
import json, os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "release_candidate"))
from rc_lib import Session, Table, TxError  # noqa: E402

F = "E2-7b:REVIEW"
IMF = "SRC-IMF-YEM-AIV-2025-2026"
LOC = lambda *ts: [{"t": t, "k": "v", "s": "LOCATOR"} for t in ts]  # noqa: E731
ADD = OrderedDict([
    ("QUAL-001", [{"t": "31 March 2026", "k": "d", "s": "READ", "src": IMF,
                   "loc": "IMF CR 26/80, PDF p. 4, press release: 'Washington, DC – March 31, 2026: The Executive Board ... concluded the 2025 Article IV consultation'"},
                  {"t": "April 2026", "k": "d", "s": "READ", "src": IMF, "loc": "IMF CR 26/80, cover: 'April 2026'"}]
     + LOC("26/80", "4", "90")),
    ("CLM-032", LOC("4-1", "37", "45", "46", "48", "52", "54")),
    ("CLM-062", LOC("139", "141")),
] + [(v, [{"t": "February 2026", "k": "d", "s": "READ", "src": "SRC-CBY-POS-2026-02",
           "loc": "CBY-Aden POS release, February 2026: one-page infographic in a design that differs from the January 2026 release"}])
     for v in ("VIS-POS-TERMINALS", "VIS-POS-TRANSACTIONS", "VIS-POS-VALUE")])
REPL = [
    ("CLM-049", "summary_ar", "فلم يُتحقق في هذه الطبعة من التاريخ ومدة 18 شهرًا والوضع المذكور أعلاه في الأصل.",
     "فلم يُتحقق من التاريخ ومدة 18 شهرًا والوضع المذكور أعلاه في الأصل في هذه الطبعة."),
    ("CLM-054", "summary_en", "what it calls 3.3 million “active savers” in 2023",
     "what it calls 3.3 million “active savers” at microfinance banks in 2023"),
    ("CLM-054", "summary_ar", "ما تسميه 3.3 مليون «مدخر نشط» في 2023",
     "ما تسميه 3.3 مليون «مدخر نشط» لدى بنوك التمويل الأصغر في 2023"),
]
REVIEW = []   # (sheet, key, field, old, new) from the independent review


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    t06 = Table(s, "06_EVIDENCE_OBJECTS", 4)
    for oid, extra in ADD.items():
        cur = t06.get(oid, "value_states")
        vs = json.loads(cur) if cur else []
        have = {(e["t"], e["s"]) for e in vs}
        vs += [e for e in extra if (e["t"], e["s"]) not in have]
        t06.set(F, oid, "value_states", json.dumps(vs, ensure_ascii=False, separators=(",", ":")), cur)
    for oid, field, old, new in REPL:
        s.replace(F, "06_EVIDENCE_OBJECTS", t06.rows[oid], t06.col(field), old, new, f"{oid}.{field}")
    for sheet, key, field, old, new in REVIEW:
        if sheet == "03":
            route, order, lang = key
            s.replace_section(F, route, order, lang, "body", old, new)
            continue
        t = Table(s, sheet, 4)
        s.replace(F, sheet, t.rows[key], t.col(field), old, new, f"{key}.{field}")
    rep = s.save(out, ledger, OrderedDict([("transaction", "E2-7b"), ("summary", "E2-7/E2-8 review and new-gate findings folded in")]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
