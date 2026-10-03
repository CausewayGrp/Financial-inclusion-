# -*- coding: utf-8 -*-
"""Release-candidate transaction RC-13: Part B item B14 e — the signed-scan dates of the other 2026 enforcement
decisions (register item of 3 October 2026, from the adversarial review of RC-8).

  python3 rc_13_decision_dates.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Each of CBY-Aden's twelve other Governor's decisions of 2026 held in the Master (Nos. 1–6, 9, 11, 13–15, 17) was opened
on 3 October 2026. Each news page (cby-ye.com/news/<n>) links a one-page signed scan (cby-ye.com/files/<id>.pdf), and the
date printed on each instrument was read in Gregorian and Hijri. Ten match the date the Master holds. Two do not; the
scans of both were read again for this transaction:
    - Decision No. 13 of 2026: "Ref:474/CBY/2026 · Date: 5/8/2026"; «بتاريخ 22 صفر 1448هـ الموافق 5 أغسطس 2026م».
      The news page (No. 964) is dated 6 August 2026, the day the scan was published.
    - Decision No. 14 of 2026: "Ref:498/CBY/2026 · Date:19/8/2026"; «بتاريخ 6 ربيع الأول 1448هـ الموافق 19 أغسطس 2026م».
      The news page (No. 968) is dated 20 August 2026.
Both sources and their status events (PSE-003, PSE-004) now carry the instrument's date, as Decision No. 10's did in
RC-8. Every one of the twelve records its signed scan as an additional locator and the check date, so each date can be
verified against the instrument. No record's text prints either date, and the order of events is unchanged. The scans of
Decisions 3 and 4 misprint the year beside the signature («8 يناير 2025م»); the header date and the Hijri date
(19 Rajab 1447) both give 8 January 2026, the date held (audit/release_candidate/ORIGINAL_SOURCE_VERIFICATION.md §7).
"""
import json, os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from rc_lib import Session, Table, TxError  # noqa: E402

F = "RC-13:B14e"
CHECKED = "2026-10-03"
SCANS = OrderedDict([   # source: the signed scan the news page links (each opened and read on 3 October 2026)
    ("SRC-CBY-ENF-01-2026", "69566356f386a"), ("SRC-CBY-ENF-02-2026", "69566423792f1"),
    ("SRC-CBY-ENF-03-2026", "695fdd05de273"), ("SRC-CBY-ENF-04-2026", "695fddc70da3b"),
    ("SRC-CBY-ENF-05-2026", "69666b96b0089"), ("SRC-CBY-ENF-06-2026", "69666bc45faf0"),
    ("SRC-CBY-ENF-09-2026", "6a0f1baad6f36"), ("SRC-CBY-ENF-11-2026", "6a296e96cf10f"),
    ("SRC-CBY-ENF-13-2026", "6a749e284951b"), ("SRC-CBY-ENF-14-2026", "6a870ae11a5d5"),
    ("SRC-CBY-ENF-15-2026", "6a9055206c613"), ("SRC-CBY-ENF-17-2026", "6aabe46e975f1"),
])
DATES = [  # (source, PSE, old date, new date, (old EN title, new EN title), (old AR title, new AR title))
    ("SRC-CBY-ENF-13-2026", "PSE-003", "2026-08-06", "2026-08-05",
     ("Governor's Decision No. 13 of 2026 on licence suspensions and closures (6 August 2026)",
      "Governor's Decision No. 13 of 2026 on licence suspensions and closures (5 August 2026)"),
     ("قرار المحافظ رقم (13) لسنة 2026 بشأن إيقاف تراخيص وإغلاق مقرات (6 أغسطس 2026)",
      "قرار المحافظ رقم (13) لسنة 2026 بشأن إيقاف تراخيص وإغلاق مقرات (5 أغسطس 2026)")),
    ("SRC-CBY-ENF-14-2026", "PSE-004", "2026-08-20", "2026-08-19",
     ("Governor's Decision No. 14 of 2026 on licence suspensions and closures (20 August 2026)",
      "Governor's Decision No. 14 of 2026 on licence suspensions and closures (19 August 2026)"),
     ("قرار المحافظ رقم (14) لسنة 2026 بشأن إيقاف تراخيص وإغلاق مقرات (20 أغسطس 2026)",
      "قرار المحافظ رقم (14) لسنة 2026 بشأن إيقاف تراخيص وإغلاق مقرات (19 أغسطس 2026)")),
]


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    t15 = Table(s, "15_SOURCE_LIBRARY", 4)
    for sid, en, ar in [(d[0], d[4], d[5]) for d in DATES]:
        t15.set(F, sid, "display_title", en[1], en[0])
        t15.set(F, sid, "display_title_ar", ar[1], ar[0])
    # the status-event block is found by its header (rows inserted above it since RC-8 moved it from row 72)
    hdr = [i for i, r in enumerate(s.grid("22_PROVIDERS_DATA"), 1) if r and r[0] == "status_event_id"]
    if len(hdr) != 1:
        raise TxError(f"{F}: 22_PROVIDERS_DATA has {len(hdr)} status-event headers")
    t22 = Table(s, "22_PROVIDERS_DATA", hdr[0])
    for sid, pse, old, new, _, _ in DATES:
        t15.set(F, sid, "document_date", new, old)
        t22.set(F, pse, "event_date", new, old)
    for sid, fid in SCANS.items():
        t15.set(F, sid, "additional_urls", json.dumps([f"https://www.cby-ye.com/files/{fid}.pdf"]), None)
        t15.set(F, sid, "retrieval_date", CHECKED, None)
    rep = s.save(out, ledger, OrderedDict([("transaction", "RC-13"), ("summary", "B14 e: signed-scan dates of the other 2026 decisions"),
                                           ("items", OrderedDict([("dates_corrected", len(DATES)), ("scans_recorded", len(SCANS))]))]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
