# -*- coding: utf-8 -*-
"""Edition 2 transaction E2-1b: the bilingual and adversarial review of E2-1, folded in (same commit as E2-1).

  python3 e2_1b_review_fixes.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Findings of the independent reviewer (4 October 2026), read against the ISR again:
- F1: the text alternative's "later implementation report still records neither as operational" gives no as-of point,
  so it reads as the state in April 2026. Gate RC-A1 keeps day-precise dates of undrawn steps out of a chain figure's
  text alternative, so the as-of point is said without one: "measured the day before the project became effective".
- F2: the ISR says the FPS tender is "expected to be published shortly"; "still to be published" sounded like a delay.
- F3: 31 August 2025 is the day before effectiveness (1 September 2025, ISR p. 2); saying so removes a "stalled
  project" reading. "Still" is dropped in English.
- F4: the Arabic "الصادر … في 8 أبريل 2026" becomes "المؤرخ 8 أبريل 2026" (the ISR is dated, archived 08-Apr-2026).
- F5: "لم يكن أيٌّ منهما" in place of "أيًّا منهما لم يكن".
- F6: the Arabic of CWR-009 section 3 names the fast payment system «نظام الدفع السريع», as every other cell does.
"""
import json, os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "release_candidate"))
from rc_lib import Session, Table, TxError  # noqa: E402

F = "E2-1b:REVIEW"

SUM_EN = ("and the project's later implementation report still records neither as operational.",
          "and the status the project last reported, measured the day before it became effective, records neither as "
          "operational.")
SUM_AR = ("ولا يسجل تقرير التنفيذ اللاحق للمشروع أيًّا منهما قيد التشغيل.",
          "ولا تسجل آخر حالة أبلغ عنها المشروع، وقد قيست قبل يوم من نفاذه، أيًّا منهما قيد التشغيل.")
LIM_EN = ("reports both still not operational at 31 August 2025 and, by its own date, the RTGS tender launched and the "
          "FPS tender still to be published;",
          "reports both as not operational at 31 August 2025, the day before the project became effective, and, by its "
          "own date, the RTGS tender launched and the FPS tender expected to be published shortly;")
LIM_AR = ("ويفيد تقرير التنفيذ الصادر عن البنك الدولي في 8 أبريل 2026 بأن أيًّا منهما لم يكن قيد التشغيل بعد في "
          "31 أغسطس 2025، وبأن مناقصة نظام RTGS طُرحت حتى تاريخ التقرير بينما لم تُطرح مناقصة نظام FPS بعد؛",
          "ويفيد تقرير التنفيذ الصادر عن البنك الدولي والمؤرخ 8 أبريل 2026 بأنه لم يكن أيٌّ منهما قيد التشغيل في "
          "31 أغسطس 2025، أي قبل يوم من نفاذ المشروع، وبأن مناقصة نظام RTGS طُرحت حتى تاريخ التقرير وأن طرح مناقصة "
          "نظام FPS متوقع قريبًا؛")
CLM_EN = ("reports both still not operational at 31 August 2025;",
          "reports both as not operational at 31 August 2025, the day before the project became effective;")
CLM_AR = ("ويفيد تقرير التنفيذ الصادر عن البنك الدولي في 8 أبريل 2026 بأن أيًّا منهما لم يكن قيد التشغيل بعد في "
          "31 أغسطس 2025،",
          "ويفيد تقرير التنفيذ الصادر عن البنك الدولي والمؤرخ 8 أبريل 2026 بأنه لم يكن أيٌّ منهما قيد التشغيل في "
          "31 أغسطس 2025، أي قبل يوم من نفاذ المشروع،")
RDG_EN = ("still reported both as not operational at 31 August 2025,",
          "reported both as not operational at 31 August 2025, the day before the project became effective,")
RDG_AR = ("وظل تقرير تنفيذ المشروع الصادر في 8 أبريل 2026 يسجلهما غير عاملين في 31 أغسطس 2025،",
          "وسجلهما تقرير تنفيذ المشروع المؤرخ 8 أبريل 2026 غير عاملين في 31 أغسطس 2025، أي قبل يوم من نفاذ المشروع،")
RDG_AR_TERM = ("نظامَ الدفع الفوري", "نظامَ الدفع السريع")


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    t06 = Table(s, "06_EVIDENCE_OBJECTS", 4)
    t11 = Table(s, "11_VISUAL_LIBRARY", 4)
    for tab, key, field, (old, new) in (
            (t06, "VIS-PAYMENT-RAILS", "summary_en", SUM_EN), (t06, "VIS-PAYMENT-RAILS", "summary_ar", SUM_AR),
            (t06, "VIS-PAYMENT-RAILS", "limitations_en", LIM_EN), (t06, "VIS-PAYMENT-RAILS", "limitations_ar", LIM_AR),
            (t11, "VIS-PAYMENT-RAILS", "accessible_summary_en", SUM_EN),
            (t11, "VIS-PAYMENT-RAILS", "accessible_summary_ar", SUM_AR),
            (t11, "VIS-PAYMENT-RAILS", "prohibited_inference_en", LIM_EN),
            (t11, "VIS-PAYMENT-RAILS", "prohibited_inference_ar", LIM_AR),
            (t06, "CLM-018", "limitations_en", CLM_EN), (t06, "CLM-018", "limitations_ar", CLM_AR)):
        s.replace(F, tab.sheet, tab.rows[key], tab.col(field), old, new, f"{key}.{field}")
    route = "/readings/from-rail-to-result-missing-middle/"
    s.replace_section(F, route, 3, "en", "body", *RDG_EN)
    s.replace_section(F, route, 3, "ar", "body", *RDG_AR)
    s.replace_section(F, route, 3, "ar", "body", *RDG_AR_TERM)
    rep = s.save(out, ledger, OrderedDict([("transaction", "E2-1b"), ("summary", "E2-1 review fixes: as-of point, 'expected shortly', the day before effectiveness, Arabic wording")]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
