# -*- coding: utf-8 -*-
"""P3-C — two grammar labels the data contracts need, and the RV-CWR-001 title (Master-first).

  python3 p3c_execute.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

UI-VIS-STATE-REPORTED: official statistics reported by a source that are neither a survey measure nor an administrative
count (IMF reported history, SFD provider tables). UI-VIS-WITHHELD: a governed value whose caveat requires a methodology
note before public use (19 OBS-00036/00037). RV-CWR-001: "baselines" wrongly implies starting references; the two figures
are published values for one year (CLM-032).
"""
import sys
from collections import OrderedDict
from ptc_lib import Session, TxError
from projection.master_reader import Workbook

S04 = "04_NAV_UX"
NEW = [
    ("UI-VIS-STATE-REPORTED", "Reported by the source (official statistics)", "مبلغ عنه في المصدر (إحصاءات رسمية)",
     "Pre-Tranche-C P3 visual grammar. Official statistics reported by a source that are neither a survey measure nor an administrative count."),
    ("UI-VIS-WITHHELD", "Figure held back until its definition is documented", "يُحجب الرقم إلى أن يُوثَّق تعريفه",
     "Pre-Tranche-C P3 visual grammar. A governed value whose caveat requires a methodology note before public use."),
]


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    g04 = Workbook(src).grid(S04)
    last = max(i for i, r in enumerate(g04, 1) if r and isinstance(r[0], str) and r[0].startswith("UI-") and i < 140)
    if g04[last - 1][0] != "UI-VIS-FULL-RECORD" or any(c not in (None, "") for c in g04[last]):
        raise TxError(f"04: interface-copy block ends at {g04[last - 1][0]!r}")
    s.ed.insert_rows(S04, last + 1, [{1: a, 2: b, 3: c, 4: d} for a, b, c, d in NEW])
    for a, b, c, _ in NEW:
        s.ledger.append(OrderedDict([("finding", "P3-G01"), ("sheet", S04), ("row", None), ("col", None), ("field", a), ("old", None), ("new", b + " || " + c)]))
    g11 = Workbook(src).grid("11_VISUAL_LIBRARY")
    r = next(i for i, x in enumerate(g11, 1) if x and x[0] == "RV-CWR-001")
    s.set("P3-F08", "11_VISUAL_LIBRARY", r, 2, "Same year, two published values", "Same year, two published baselines", "RV-CWR-001.title_en")
    s.set("P3-F08", "11_VISUAL_LIBRARY", r, 3, "السنة نفسها وقيمتان منشورتان", "السنة نفسها وخطا أساس منشوران", "RV-CWR-001.title_ar")
    # P3-F12 credit lines for the RV-CWR-009 signature chain: the six CBY news sources its events cite carry no publisher.
    # The Master already attributes documents on cby-ye.com to "Central Bank of Yemen — Aden" (15 SRC-CBY-AR2024-BOP and
    # SRC-CBY-AR2025-BOP; 34 EP-CBY-POS-MONTHLY; 22 authority of every status event with a cby-ye.com URL). The same
    # attribution is applied to these six; no title or other bibliography is added. The remaining CBY-hosted sources
    # without a publisher stay with the corpus-metadata work (P2-F10).
    g15 = Workbook(src).grid("15_SOURCE_LIBRARY")
    hdr = [str(x) for x in g15[3]]
    pc, uc = hdr.index("publisher") + 1, hdr.index("primary_url") + 1
    for sid in ("SRC-CBY-BANK-NETWORK-MTG-2026-001", "SRC-CBY-PAY-BOARD-2026-001", "SRC-CBY-DIGITAL-EXPO-2026-001",
                "SRC-CBY-UNIFIED-NET-2026-001", "SRC-CBY-YPCC-FOUND-2026-001", "SRC-CBY-YPCC-BOARD-2026-001"):
        r = next(i for i, x in enumerate(g15, 1) if x and x[0] == sid)
        if "cby-ye.com" not in str(g15[r - 1][uc - 1]):
            raise TxError(f"{sid}: locator is not on cby-ye.com")
        s.set("P3-F12", "15_SOURCE_LIBRARY", r, pc, "Central Bank of Yemen — Aden", None, f"{sid}.publisher")
    rep = s.save(out, ledger, [("transaction", "P3-C"), ("scope", "P3 grammar labels REPORTED/WITHHELD; RV-CWR-001 title; six publishers for RV-CWR-009 credit")])
    print(f"P3-C staged: {rep['cells_written']} changes; Master {rep['output_master_sha256']}")


if __name__ == "__main__":
    main()
