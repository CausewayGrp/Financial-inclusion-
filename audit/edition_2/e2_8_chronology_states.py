# -*- coding: utf-8 -*-
"""Edition 2 transaction E2-8: every dated event of the system chronology carries a state; its discrepancies fixed.

  python3 e2_8_chronology_states.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

The 24 events of 14_SYSTEM_CHRONOLOGY were re-read in their cited originals on 4 October 2026 (85 items: 75 read, 1
derived, 5 not found, 4 unreachable, 0 mismatched). Writes:
1. 14 gains value_states (JSON, input audit/edition_2/inputs/E2-8_chronology_states.json), as 06 did in E2-7.
2. YSC-003: the cited PAD (PDF p. 12, para. 8) dates the relocation decision to 2016, not to a month: period "2016".
3. YSC-005: the cited Saudi Press Agency items date the signing (March 2018), not the directive: period "March 2018".
4. YSC-007: "the 2018 deposit" is dated by the SPA item, now bound to the event.
5. YSC-021: the four operations and US$285 million are in the World Bank's press release of 4 June 2026, which says the
   Board "approved" the framework; the release joins the CPF source as an additional locator, and "endorsed" becomes
   "approved".
6. YSC-023: the IMF release (HTTP 403, no archive copy) is named as not re-read, in the event's verification note.
7. 15: retrieval and document dates of the sources opened that day; the Sana'a Center microfinance-bank brief dated
   exactly (23 September 2024, the DeepRoot brief No. 29, lead 4).
"""
import json, os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "release_candidate"))
from rc_lib import Session, Table, TxError  # noqa: E402

F = "E2-8:CHRONOLOGY"
DAY = "2026-10-04"
PR = ("https://www.worldbank.org/en/news/press-release/2026/06/04/yemen-world-bank-group-launches-new-country-partnership-"
      "framework-and-projects-to-support-better-livelihoods-and-more-jo")
EV = [
    ("YSC-003", "period_en", "September 2016", "2016"),
    ("YSC-003", "period_ar", "سبتمبر 2016", "2016"),
    ("YSC-005", "period_en", "January–March 2018", "March 2018"),
    ("YSC-005", "period_ar", "يناير–مارس 2018", "مارس 2018"),
]
RE = [
    ("YSC-021", "fact_en", "The World Bank Group endorsed a Country Partnership Framework",
     "The World Bank Group's Board of Executive Directors approved a Country Partnership Framework"),
    ("YSC-021", "fact_ar", "أقرت مجموعة البنك الدولي إطار شراكة قطرية",
     "وافق مجلس المديرين التنفيذيين لمجموعة البنك الدولي على إطار شراكة قطرية"),
]
NOTE = ("The IMF press release could not be re-opened on 4 October 2026 (the IMF website refuses automated requests); this "
        "entry has not been re-read in the original for this edition.",
        "تعذّرت إعادة فتح البيان الصحفي لصندوق النقد الدولي في 4 أكتوبر 2026 (يرفض موقع الصندوق الطلبات الآلية)، فلم يُتحقق من "
        "هذا المدخل في الأصل في هذه الطبعة.")


def main():
    src, out, ledger, work = sys.argv[1:5]
    states = json.load(open(os.path.join(HERE, "inputs", "E2-8_chronology_states.json"), encoding="utf-8"))
    sources = json.load(open(os.path.join(HERE, "inputs", "E2-8_sources.json"), encoding="utf-8"))
    s = Session(src, work)
    t14 = Table(s, "14_SYSTEM_CHRONOLOGY", 4)
    if t14.head[18] != "verification_note_ar" or "value_states" in t14.head:
        raise TxError("14 header not at expected state")
    s.set(F, "14_SYSTEM_CHRONOLOGY", 4, 20, "value_states", None, "header.value_states")
    t14 = Table(s, "14_SYSTEM_CHRONOLOGY", 4)
    for eid, st in states.items():
        t14.set(F, eid, "value_states", json.dumps(st, ensure_ascii=False, separators=(",", ":")), None)
    for eid, field, old, new in EV:
        t14.set(F, eid, field, new, old)
    for eid, field, old, new in RE:
        s.replace(F, "14_SYSTEM_CHRONOLOGY", t14.rows[eid], t14.col(field), old, new, f"{eid}.{field}")
    ids = t14.get("YSC-007", "source_ids")
    t14.set(F, "YSC-007", "source_ids", ids + " | SRC-SPA-SAU-CBY-DEPOSIT-2018-001", ids)
    t14.set(F, "YSC-023", "verification_note_en", NOTE[0], None)
    t14.set(F, "YSC-023", "verification_note_ar", NOTE[1], None)
    t15 = Table(s, "15_SOURCE_LIBRARY", 4)
    cur = t15.get("SRC-WB-YEM-CPF-2026-2030-001", "additional_urls")
    t15.set(F, "SRC-WB-YEM-CPF-2026-2030-001", "additional_urls", json.dumps(json.loads(cur) + [PR]), cur)
    for sid in sources["retrieved"]:
        if sid in t15.rows:
            t15.set(F, sid, "retrieval_date", DAY, t15.get(sid, "retrieval_date"))
    for sid, d in sources["document_dates"].items():
        t15.set(F, sid, "document_date", d, None)
    t15.set(F, "SRC-SANAA-MFB-2024", "document_date", "2024-09-23", "2024")
    rep = s.save(out, ledger, OrderedDict([("transaction", "E2-8"), ("summary", "A state for every dated chronology event; three event dates and one verb corrected to their sources; the IMF release named as not re-read; source dates")]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
