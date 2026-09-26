# -*- coding: utf-8 -*-
"""Stage 4 follow-up (PB-0492/PB-0494): three governed discovery aliases found necessary by the post-execution search probe.

  python3 stage4b_search_aliases.py <in_master.xlsx> <out_master.xlsx> <ledger.json>

The 28-term probe showed 'licensed banks' (EN), «تكلفة التحويل» and «عدن» (AR) outside the top 10 for their answer pages.
Aliases are discovery aids only; they never assert that two things mean the same (PB-0492). Rows are appended to the
04 'Search aliases' block (the last block of the sheet); every existing cell is untouched.
"""
import hashlib, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "scripts"))
from projection.master_reader import Workbook               # noqa: E402
from projection.master_writer import MasterEditor           # noqa: E402

ROWS = [
    ("SEARCH-ALIAS-015", "licensed banks; licensed bank; bank list", "البنوك المرخصة; بنوك مرخصة; قائمة البنوك", "route:/providers/", None, None),
    ("SEARCH-ALIAS-016", "remittance cost; remittance prices; transfer cost", "تكلفة التحويل; تكلفة الحوالات; رسوم التحويل", "route:/remittances/", None, None),
    ("SEARCH-ALIAS-017", "Aden; CBY Aden; CBY-Aden", "عدن; البنك المركزي في عدن", "route:/providers/ | route:/data/",
     "Discovery aid only: CBY-Aden lists, decisions and statistics carry the scope of that authority; they do not describe all of Yemen.",
     "وسيلة للعثور على المحتوى فقط: قوائم البنك المركزي اليمني في عدن وقراراته وإحصاءاته تحمل نطاق تلك السلطة، ولا تصف اليمن كله."),
]


def main():
    src, out, ledger = sys.argv[1:4]
    wb = Workbook(src)
    g = wb.grid("04_NAV_UX")
    last = max(i for i, r in enumerate(g, 1) if any(c not in (None, "") for c in r))
    if not str(g[last - 1][0]).startswith("SEARCH-ALIAS-014"):
        sys.exit(f"04 last row is {g[last - 1][0]!r}, expected SEARCH-ALIAS-014")
    ed = MasterEditor(src)
    for k, row in enumerate(ROWS, 1):
        for j, v in enumerate(row, 1):
            if v not in (None, ""):
                ed.set_cell("04_NAV_UX", last + k, j, v, expect=None)
    data = ed.save(out)
    rep = {"root_context": "PB-0492 / PB-0494 (Stage 4 follow-up)", "rows_appended": [r[0] for r in ROWS], "first_row": last + 1,
           "input_master_sha256": hashlib.sha256(open(src, "rb").read()).hexdigest(), "output_master_sha256": hashlib.sha256(data).hexdigest()}
    json.dump(rep, open(ledger, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(json.dumps(rep, ensure_ascii=False))


if __name__ == "__main__":
    main()
