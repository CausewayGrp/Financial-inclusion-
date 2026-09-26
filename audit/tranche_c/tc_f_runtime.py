# -*- coding: utf-8 -*-
"""Tranche C transaction TC-F — governed copy for the generator and runtime fixes (Master part).

  python3 tc_f_runtime.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

The code changes of TC-F (scripts/build.py, site-src/app.js, site-src/styles.css, scripts/projection/derived.py and
families.py, the projection manifest and the presentation contract) render only governed text; the text they need is
added here to 04 first:
  * interface copy (04 'Governed interface copy'): product name and content version for citations (TOOL-14, VER-07),
    answer-page question crumb (JRN-07), bound-record disclosures (JRN-03), related questions (JRN-12), the financial-
    system chronology (JRN-09), measurement links and fields (JRN-10), block headings and the hub index (JRN-16/17),
    the Reading's return path (JRN-02) and the no-script note (TOOL-17);
  * search aliases (04 SEARCH-ALIAS block): women and gender, humanitarian and cash transfers, licences and
    suspensions (JRN-06).
"""
import json, os, sys
from collections import OrderedDict
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from tc_lib import Session, TxError, insert_ui_rows  # noqa: E402

UI = [
    ("UI-PRODUCT-NAME", "Yemen Financial Inclusion Evidence", "أدلة الشمول المالي في اليمن", "Tranche C TC-F. Resource name in citations."),
    ("UI-CONTENT-VERSION", "Content version of 26 September 2026", "إصدار المحتوى بتاريخ 26 سبتمبر 2026",
     "Tranche C TC-F (VER-07/TOOL-14). Content version cited with every record; changes only with a governed release."),
    ("UI-NOSCRIPT-NOTE", "Search, Compare and the copy buttons need JavaScript. Every page of evidence remains readable without it.",
     "يحتاج البحث والمقارنة وأزرار النسخ إلى JavaScript، وتبقى كل صفحات الأدلة قابلة للقراءة من دونه.", "Tranche C TC-F (TOOL-17)."),
    ("UI-ANSWER-CRUMB-LABEL", "The question this page answers", "السؤال الذي تجيب عنه هذه الصفحة", "Tranche C TC-F (JRN-07). Accessible name of the answer-page crumb."),
    ("UI-ANSWER-ALL-RECORDS", "All evidence records on this question", "كل سجلات الأدلة المتعلقة بهذا السؤال", "Tranche C TC-F (JRN-03)."),
    ("UI-HOME-FIGURES-EVIDENCE", "Evidence records behind these figures", "سجلات الأدلة وراء هذه الأرقام", "Tranche C TC-F (JRN-03). Home."),
    ("UI-RELATED-QUESTIONS", "Related questions", "أسئلة ذات صلة", "Tranche C TC-F (JRN-12)."),
    ("UI-RELATED-QUESTIONS-NOTE", "These pages answer connected questions. A link between two pages is not evidence that a change in one causes a change in the other.",
     "تجيب هذه الصفحات عن أسئلة مترابطة. ولا يُعد الرابط بين صفحتين دليلًا على أن التغير في إحداهما يسبب تغيرًا في الأخرى.", "Tranche C TC-F (JRN-12)."),
    ("UI-CHRONOLOGY-H", "Dated events in Yemen's financial system", "أحداث مؤرخة في النظام المالي في اليمن", "Tranche C TC-F (JRN-09)."),
    ("UI-CHRONOLOGY-INTRO", "Each event keeps its date, its source and what it does not establish. The order of events does not show that one caused another.",
     "يحتفظ كل حدث بتاريخه ومصدره وما لا يثبته. ولا يبيّن ترتيب الأحداث أن أحدها تسبب في غيره.", "Tranche C TC-F (JRN-09)."),
    ("UI-CHRONOLOGY-RELEVANCE", "Relevance to financial inclusion:", "الصلة بالشمول المالي:", "Tranche C TC-F (JRN-09)."),
    ("UI-CHRONOLOGY-SOURCES", "Sources:", "المصادر:", "Tranche C TC-F (JRN-09)."),
    ("UI-MA-OPEN", "Open this measurement priority", "افتح أولوية القياس هذه", "Tranche C TC-F (JRN-10)."),
    ("UI-MA-MORE", "More about this priority", "المزيد عن هذه الأولوية", "Tranche C TC-F (JRN-10)."),
    ("UI-MA-GUARDRAIL", "Measurement guardrail", "ضابط القياس", "Tranche C TC-F (JRN-10)."),
    ("UI-MA-FEASIBILITY", "Feasibility", "إمكانية التنفيذ", "Tranche C TC-F (JRN-10)."),
    ("UI-MA-BASIS", "Why this is a priority", "سبب الأولوية", "Tranche C TC-F (JRN-10)."),
    ("UI-MA-CHANGES", "What the measurement would change", "ما الذي سيغيّره القياس", "Tranche C TC-F (JRN-10)."),
    ("UI-MEASURE-REVEALING-RECORDS", "Evidence records that revealed these gaps", "سجلات الأدلة التي كشفت هذه الفجوات", "Tranche C TC-F (JRN-16)."),
    ("UI-HUB-START-HERE", "Start here: selected evidence records", "ابدأ من هنا: سجلات أدلة مختارة", "Tranche C TC-F (JRN-16/17)."),
    ("UI-RELATED-RECORDS", "Related evidence records", "سجلات أدلة ذات صلة", "Tranche C TC-F (JRN-16)."),
    ("UI-EXPLORE-CANNOT-ANSWER", "What the evidence cannot yet answer", "ما لا تستطيع الأدلة الإجابة عنه بعد", "Tranche C TC-F (JRN-16)."),
    ("UI-RELATED-MEASUREMENT", "Related measurement priorities", "أولويات قياس ذات صلة", "Tranche C TC-F (JRN-16)."),
    ("UI-HUB-ALL-RECORDS", "All evidence records, by question", "كل سجلات الأدلة، بحسب السؤال", "Tranche C TC-F (JRN-17)."),
    ("UI-HUB-OTHER", "Method, context and other records", "سجلات المنهج والسياق وغيرها", "Tranche C TC-F (JRN-17)."),
    ("UI-READING-RETURN", "Return to the question", "عد إلى السؤال", "Tranche C TC-F (JRN-02)."),
]
ALIASES = [
    ("SEARCH-ALIAS-025", "women; woman; female; gender; gender gap",
     "المرأة; امرأة; النساء; نساء; الإناث; النوع الاجتماعي; فجوة النوع الاجتماعي; الفجوة بين الجنسين", "route:/people/",
     "Discovery aid only: the measured gap comes from one survey wave (the 2021 Findex wave; Yemen fieldwork 2022–23); it is not a 2026 figure and does not establish causes.",
     "أداة اكتشاف فقط: الفجوة المقاسة مأخوذة من موجة مسحية واحدة (موجة Findex لعام 2021؛ العمل الميداني في اليمن 2022–2023)، وليست رقمًا لعام 2026 ولا تثبت الأسباب."),
    ("SEARCH-ALIAS-026", "humanitarian; cash transfer; cash transfers; social protection; G2P",
     "إنساني; المساعدات الإنسانية; التحويلات النقدية; الحماية الاجتماعية; مدفوعات الحكومة للأفراد",
     "route:/readings/after-transfer-persistence/ | route:/payments/", None, None),
    ("SEARCH-ALIAS-027", "licence; license; licensing; suspension; closure",
     "ترخيص; تراخيص; إيقاف; تعليق; إغلاق", "route:/providers/ | document_type:decision/enforcement", None, None),
]


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    insert_ui_rows(s, "TC-F", UI)
    g = s.grid("04_NAV_UX")
    rows = [i for i, r in enumerate(g, 1) if r and r[0] == "SEARCH-ALIAS-024"]
    if len(rows) != 1 or any(r and r[0] in [a[0] for a in ALIASES] for r in g):
        raise TxError("04 alias block not as expected")
    s.ed.insert_rows("04_NAV_UX", rows[0] + 1, [{i + 1: v for i, v in enumerate(a) if v is not None} for a in ALIASES])
    for a in ALIASES:
        s.ledger.append(OrderedDict([("finding", "TC-F:JRN-06"), ("sheet", "04_NAV_UX"), ("row", None), ("col", None), ("field", a[0]),
                                     ("old", None), ("new", a[1] + " || " + a[2] + " -> " + a[3])]))
    g = s.grid("04_NAV_UX")
    r11 = [i for i, r in enumerate(g, 1) if r and r[0] == "SEARCH-ALIAS-011"][0]
    s.set("TC-F:JRN-06", "04_NAV_UX", r11, 2, "measurement; measurement agenda; measurement priorities", "measurement agenda", "SEARCH-ALIAS-011.terms_en")
    from tc_lib import Table
    t10 = Table(s, "10_MEASUREMENT_AGENDA")
    t10.set("TC-F:EN-27", "MA-003", "what_changes_en",
            "Keeps apart what needs different evidence: whether a disparity is measured, what is associated with it, and what design could test a causal mechanism or intervention.",
            "Separates three questions that require different evidence: whether a disparity is measured, what is associated with it, and what design could test a causal mechanism or intervention.")
    t10.set("TC-F:EN-27", "MA-003", "what_changes_ar",
            "يفصل بين ما يحتاج أدلة مختلفة: هل يوجد تفاوت مقاس، وما العوامل المرتبطة به، وما التصميم القادر على اختبار آلية سببية أو تدخل.",
            "يفصل بين ثلاثة أسئلة تحتاج أدلة مختلفة: هل يوجد تفاوت مقاس، وما العوامل المرتبطة به، وما التصميم القادر على اختبار آلية سببية أو تدخل.")
    rep = s.save(out, ledger, {"transaction": "TC-F", "summary": "04 interface copy for generator/runtime fixes; 3 search aliases"})
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
