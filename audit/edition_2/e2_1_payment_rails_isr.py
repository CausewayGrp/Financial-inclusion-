# -*- coding: utf-8 -*-
"""Edition 2 transaction E2-1: the FPS and RTGS operational state, as the World Bank's ISR sequence 2 reports it.

  python3 e2_1_payment_rails_isr.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Finding (independent review of cd7817b): VIS-PAYMENT-RAILS says "no later operational state is recorded", while the
same record cites SRC-WB-FMIIP-ISR2-2026-001. Read on 4 October 2026 (documents1.worldbank.org PDF, 8 pages):
- p. 3-4, "Development of Fast Payment Systems (FPS)": "Fast Payment System is developed and operational (Yes/No)":
  baseline No (Jan/2025), Actual (Previous) No 31-Aug-2025, Actual (Current) No 31-Aug-2025, closing Yes (Jun/2030);
  "Real Time Gross Settlement System is developed and operational (Yes/No)": the same, No at 31-Aug-2025.
- p. 2, Implementation Status and Key Decisions: "Procurement has advanced with the RTGS tender launched and the FPS
  tender expected to be published shortly."
The reviewer's wording ("ISR sequence 2 reports both still not operational at 31 August 2025; no later state is
recorded") is right on the first half; "no later state" is not, because the same report records a later procurement
state. So the text says what the report says, and keeps "no later operational state". The same stale sentence stood
in CLM-018 and in section 3 of CWR-009; they change with it, and CLM-018 gains the report as a source (it is already a
governed source record with a public locator). The drawing's rows are unchanged: none of them is an operation state.
"""
import json, os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "release_candidate"))
from rc_lib import Session, Table, TxError  # noqa: E402

F = "E2-1:R-PAYRAILS"
ISR = "SRC-WB-FMIIP-ISR2-2026-001"

SUM_EN = ("The FMIIP baseline for January 2025 records FPS and RTGS as not yet operational, with no participating "
          "institutions, and no later operational state is recorded.",
          "The FMIIP baseline for January 2025 records FPS and RTGS as not yet operational, with no participating "
          "institutions, and the project's later implementation report still records neither as operational.")
SUM_AR = ("ويسجل خط أساس مشروع FMIIP في يناير 2025 أن نظامي FPS وRTGS لم يكونا قيد التشغيل بعد ولا مؤسسات مشاركة "
          "فيهما، ولا يُسجَّل أي وضع تشغيلي لاحق.",
          "ويسجل خط أساس مشروع FMIIP في يناير 2025 أن نظامي FPS وRTGS لم يكونا قيد التشغيل بعد ولا مؤسسات مشاركة "
          "فيهما، ولا يسجل تقرير التنفيذ اللاحق للمشروع أيًّا منهما قيد التشغيل.")
LIM_EN = ("records both as not yet operational, and no later operational state is recorded.",
          "records both as not yet operational. The World Bank's implementation report of 8 April 2026 reports both "
          "still not operational at 31 August 2025 and, by its own date, the RTGS tender launched and the FPS tender "
          "still to be published; no later operational state is recorded.")
LIM_AR = ("أن كليهما لم يكن قيد التشغيل بعد، ولا يُسجَّل أي وضع تشغيلي لاحق.",
          "أن كليهما لم يكن قيد التشغيل بعد. ويفيد تقرير التنفيذ الصادر عن البنك الدولي في 8 أبريل 2026 بأن أيًّا منهما "
          "لم يكن قيد التشغيل بعد في 31 أغسطس 2025، وبأن مناقصة نظام RTGS طُرحت حتى تاريخ التقرير بينما لم تُطرح مناقصة "
          "نظام FPS بعد؛ ولا يُسجَّل أي وضع تشغيلي لاحق.")
CLM_EN = ("in January 2025, with no participating institutions; no later operational state is recorded here.",
          "in January 2025, with no participating institutions, and the World Bank's implementation report of "
          "8 April 2026 reports both still not operational at 31 August 2025; no later operational state is recorded "
          "here.")
CLM_AR = ("في يناير 2025، ولا مؤسسات مشاركة فيهما، ولا يسجل هذا الدليل أي وضع تشغيلي لاحق.",
          "في يناير 2025، ولا مؤسسات مشاركة فيهما، ويفيد تقرير التنفيذ الصادر عن البنك الدولي في 8 أبريل 2026 بأن "
          "أيًّا منهما لم يكن قيد التشغيل بعد في 31 أغسطس 2025، ولا يسجل هذا الدليل أي وضع تشغيلي لاحق.")
RDG_EN = ("as not yet operational in January 2025, with no later operational state recorded here.",
          "as not yet operational in January 2025; the project's implementation report of 8 April 2026 still reported "
          "both as not operational at 31 August 2025, with no later operational state recorded here.")
RDG_AR = ("على أنهما غير عاملين بعد في يناير 2025، من دون حالة تشغيل لاحقة مسجلة هنا.",
          "على أنهما غير عاملين بعد في يناير 2025، وظل تقرير تنفيذ المشروع الصادر في 8 أبريل 2026 يسجلهما غير عاملين "
          "في 31 أغسطس 2025، من دون حالة تشغيل لاحقة مسجلة هنا.")


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
    deps = t06.get("CLM-018", "source_dependencies")
    if ISR in deps:
        raise TxError("CLM-018 already cites the ISR")
    t06.set(F, "CLM-018", "source_dependencies", deps + "; " + ISR, deps)
    route = "/readings/from-rail-to-result-missing-middle/"
    s.replace_section(F, route, 3, "en", "body", *RDG_EN)
    s.replace_section(F, route, 3, "ar", "body", *RDG_AR)
    rep = s.save(out, ledger, OrderedDict([("transaction", "E2-1"), ("summary", "FPS and RTGS still not operational at 31 August 2025 (World Bank ISR sequence 2); no later operational state")]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
