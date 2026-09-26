# -*- coding: utf-8 -*-
"""Transaction R85-B — R8.5 public-copy corrections and known duplicates/debt (directive D7 §F4; D6 §18).

  python3 r85b_subtraction.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

  C1  interface copy (04) rewritten where it spoke the product's control language (404, corrections, domain disclosure,
      source-trace, data directory, compare) — the controls themselves are unchanged
  C2  XW-FMIIP-005 title said "compared with" for a record whose finding is that the measures cannot be compared
  D1  duplicate reform events merged: REF-PAY-010 = REF-PAY-006 (17 June 2026, CBY news 946) and REF-PAY-007 =
      REF-PAY-013 (4 August 2026, CBY news 962); the kept IDs are the ones the visual contract draws; CLM-018 lists
      its inputs by ID instead of the range "REF-PAY-010..013"
  D2  Resource Library: sixteen near-duplicate categories on 28 curated cards become six
  D3  P3-D02: two derived-analytics labels in 33 said "change" for a difference between observed survey waves
  D4  Unicode NFC for every text cell (one Arabic boilerplate existed in two diacritic orders; search and parity
      compare exact strings)
"""
import json, os, sys, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from fi_lib import Session, Table, TxError, set_ui  # noqa: E402

UI = {  # id: (new_en, new_ar) — None keeps a language unchanged
    "UI-DOM-ADDITIONAL-CONTROLLED-DETAIL-FROM-THIS": ("More detail on this question, each item with its own period and limits.",
                                                      "مزيد من التفاصيل حول هذا السؤال، ولكل منها فترته وحدوده."),
    "UI-EVID-OPEN-THE-SOURCE-RECORD-HERE": ("Open the source record here, or go to the original document where a public link exists.",
                                            "افتح سجل المصدر هنا، أو انتقل إلى الوثيقة الأصلية حيث يتوافر رابط عام."),
    "UI-EVID-NO-STANDALONE-PUBLIC-LOCATOR-IS": ("No public link to the original document is available for this source.",
                                                "لا يتوافر رابط عام إلى الوثيقة الأصلية لهذا المصدر."),
    "UI-EVID-THIS-RECORD-CURRENTLY-HAS-NO": ("No original source for this record can be opened from here; use the method and verification detail below.",
                                             "لا يمكن فتح مصدر أصلي لهذا السجل من هنا؛ استخدم المنهج وطريقة التحقق أدناه."),
    "UI-EVID-ADDITIONAL-DETAIL-FOR-REPRODUCING-OR": ("Detail for reproducing or challenging this record without changing what it means.",
                                                     "تفاصيل تساعد على إعادة إنتاج هذا السجل أو مراجعته نقديًا من دون تغيير معناه."),
    "UI-EVID-THE-STABLE-RECORD-ID-STAYS": ("This record’s reference stays linked to the original sources that can be shown publicly. Missing bibliographic details are left blank rather than guessed.",
                                           "يبقى مرجع هذا السجل مرتبطًا بالمصادر الأصلية التي يمكن عرضها علنًا، وتُترك البيانات الببليوغرافية الناقصة فارغة بدل تخمينها."),
    "UI-QUESTIONS-EVERY-ROUTE-KEEPS-PERIOD-POPULATION": ("Every answer keeps its period, population or calculation base, limits and source in view.",
                                                         "تبقي كل إجابة فترتها ومجتمعها أو قاعدة احتسابها وحدودها ومصدرها ظاهرة."),
    "UI-HOME-CROSS-SOURCE-ANALYSIS-THAT-STAYS": ("Evidence-led essays, each traceable to the records behind it.",
                                                 "قراءات تحليلية تنطلق من الأدلة، ويمكن تتبّع كل منها إلى السجلات التي قامت عليها."),
    "UI-DATA-ONLY-SOURCE-INFORMATION-PERMITTED-BY": ("Sources that support current public evidence are listed separately from references kept for verification or context, so that a link is never mistaken for analytical use or an observed result.",
                                                     "تُعرض المصادر التي تسند الأدلة العامة الحالية منفصلة عن المراجع المتاحة للتحقق أو السياق، حتى لا يُفهم مجرد وجود رابط على أنه استخدام تحليلي أو دليل على نتيجة."),
    "UI-DATA-THESE-SOURCES-ARE-LINKED-DIRECTLY": ("These sources are linked directly to at least one current public Evidence Record. Open the records that use them to see exactly where and how.",
                                                  "هذه المصادر مرتبطة مباشرة بسجل دليل عام واحد على الأقل. افتح السجلات التي تستخدمها لمعرفة موضع استخدامها وكيفيته بدقة."),
    "UI-DATA-THESE-REFERENCES-ARE-AVAILABLE-FOR": ("These references are available for verification, method or context but do not currently support a public Evidence Record. Being listed here does not make them evidence for any finding or claim.",
                                                   "هذه المراجع متاحة للتحقق أو المنهج أو السياق، لكنها لا تسند حاليًا سجل دليل عام. وإدراجها هنا لا يجعلها دليلًا على أي نتيجة أو خلاصة."),
    "UI-DATA-EVERY-SOURCE-HERE-CAN-BE": ("Every source here can be cited and opened where it was originally published. Each card says whether the source’s reuse terms have been assessed; where they have not, this resource offers no copy of the source for download or republication, so check the source’s own terms before redistributing its material.",
                                         "يمكن الاستشهاد بكل مصدر هنا وفتحه حيث نُشر أصلًا. وتبيّن كل بطاقة ما إذا كانت شروط إعادة استخدام المصدر قد قُيّمت؛ وحيث لم تُقيَّم، لا يقدم هذا المورد نسخة من المصدر للتنزيل أو إعادة النشر، فتحقّق من شروط المصدر نفسه قبل إعادة توزيع مادته."),
    "UI-CORR-THIS-RESOURCE-DOES-NOT-MANUFACTURE": ("A correction appears here only when a material correction has been made to a public record. A record’s reference always leads to its current version.",
                                                   "لا يظهر التصحيح هنا إلا عند إجراء تصحيح جوهري على سجل عام. ويقود مرجع السجل دائمًا إلى نسخته الحالية."),
    "UI-CORR-THIS-PAGE-CURRENTLY-HAS-NO": ("No material corrections have been recorded yet.",
                                           "لم تُسجَّل أي تصحيحات جوهرية حتى الآن."),
    "UI-FOOTER-PUBLISHED-EVIDENCE-REMAINS-ATTRIBUTED-TO": (None, "تبقى الأدلة المنشورة منسوبة إلى مصادرها الأصلية."),
    "UI-COMPARE-START-WITH-COMPARISON-LEGITIMACY-NOT": ("First ask whether the records can be compared at all; then look at the numbers.",
                                                        "اسأل أولًا هل يمكن مقارنة السجلات أصلًا، ثم انظر إلى الأرقام."),
    "UI-COMPARE-NO-AUTO-AVERAGE-NO-PREFERRED": ("No automatic averages · no preferred number · no invented conversion factor",
                                                "لا متوسطات تلقائية · لا رقم مفضل · لا معامل تحويل مفترض"),
    "UI-JS-COMPARE-SAME": ("Same in the recorded fields", "متطابق في الحقول المسجلة"),
    "UI-JS-COMPARE-ALIGNED-COPY": ("The recorded definition, population and method match. This does not establish equivalence beyond the fields shown here.",
                                   "يتطابق التعريف والمجتمع والطريقة المسجلة. ولا يثبت ذلك تكافؤ المعنى خارج الحقول المعروضة هنا."),
    "UI-JS-COMPARE-NO-MERGE": ("Do not merge values, invent a midpoint, average the disagreement or derive a conversion factor from this comparison.", None),
    "UI-404-HEADING": ("We could not find this page", "تعذر العثور على هذه الصفحة"),
    "UI-404-BODY": ("The page may have moved, or the link may be out of date. Start from Home, explore the questions, or search the published evidence.",
                    "ربما نُقلت الصفحة أو أصبح الرابط قديمًا. ابدأ من الصفحة الرئيسية، أو استكشف الأسئلة، أو ابحث في الأدلة المنشورة."),
    "UI-SOURCE-NO-PUBLIC-LOCATOR": ("Also draws on material that has no public link to its original document; that material is not listed or linked.", None),
    "UI-EVID-SOURCES-WITHOUT-LOCATOR": ("This record also draws on material that has no public link to its original document. That material is held in the evidence base but is not listed or linked here, so the sources shown above are not the record’s only basis.", None),
    "UI-VERIFY-UNLISTED": ("The material behind this record has no public link to its original document, so no source is listed or linked here and no figure from that material is shown. Read the record as an explanation of method, not as a verifiable figure.", None),
    "UI-READING-PATH-COMPLETE-UNLISTED": ("Every figure in this Reading traces through the records below to a named source. Where a record also rests on material with no public link to its original document, that material is not listed and no figure from it is shown.", None),
}
XW = ("The FMIIP access-point target is not comparable with ATM, POS or agent counts",
      "مستهدف نقاط الوصول في مشروع FMIIP غير قابل للمقارنة بأعداد أجهزة الصراف الآلي ونقاط البيع والوكلاء")
CATS = {
    "OFFICIAL": ("Official Yemen documents and statistics", "الوثائق والإحصاءات الرسمية في اليمن",
                 ["SRC-CBY-AR2022-001", "SRC-CBY-AR2023-001", "SRC-CBY-AR2024-BOP", "SRC-CBY-AR2025-BOP", "SRC-CBY-DEC-23-2024-001"]),
    "RESEARCH": ("Research and analysis on Yemen’s financial sector", "البحوث والتحليلات حول القطاع المالي في اليمن",
                 ["SRC-WB-FSD-2024-001", "SRC-OECD-YEM-RESILIENCE-001", "SRC-SANAA-EMONEY-2022", "SRC-SANAA-MFB-2024", "SRC-AMB-MFB-SUPERVISION-2026"]),
    "CONTEXT": ("Yemen’s economy and policy context", "السياق الاقتصادي والسياساتي في اليمن",
                ["SRC-IMF-YEM-AIV-2025-2026", "SRC-IMF-YEM-SMP-2026", "SRC-WB-YEM-ECON-MONITOR-2026-SPRING-001", "SRC-WB-YEM-CPF-2026-2030-001"]),
    "PROGRAMMES": ("Programmes and projects in Yemen", "البرامج والمشروعات في اليمن",
                   ["SRC-WB-FMIIP-ISR2-2026-001", "SRC-UNDP-FMIIP-001", "SRC-WB-FMIIP-P180708", "SRC-KFW-YEM-MSME-FIN-III-47229", "SRC-WB-YEM-CNL-2026-001", "SRC-WB-G2PX-YEM-UCT-2024-001"]),
    "METHODS": ("Measurement standards and methods", "معايير القياس ومناهجه",
                ["SRC-OECD-INFE-2023", "SRC-WB-FINDEX-2025-EDITION", "SRC-CGAP-ARAB-MEAS-2017-001", "SRC-OECD-YOUTH-DFI-2020-001"]),
    "PAYMENTS": ("Payment-system design and digital payments", "تصميم أنظمة الدفع والمدفوعات الرقمية",
                 ["SRC-BIS-CPMI-FPS-RTGS-2021-001", "SRC-WB-FASTT-FPS-2021-001", "SRC-WB-G2PX-001", "SRC-BIS-CPMI-PAFI-FINTECH-2020-001"]),
}
DA = {"DA-023": ("Women's account ownership observed-wave change", "Women's account ownership: difference between observed waves"),
      "DA-024": ("Poorest-40 account ownership observed-wave change", "Poorest-40 account ownership: difference between observed waves")}


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    # C1
    from fi_lib import ui_rows
    ui, _ = ui_rows(s)
    old_labels = {uid: (s.ed.get_value("04_NAV_UX", ui[uid], 2), s.ed.get_value("04_NAV_UX", ui[uid], 3)) for uid in UI}
    for uid, (en, ar) in UI.items():
        set_ui(s, "R85-B:C1", uid, en, ar)
    # closure rule v2: a record's 06 verification text equals the governed template of its lineage state, so a
    # template label changed above is mirrored into every 06 verification cell that carries it
    t06v = Table(s, "06_EVIDENCE_OBJECTS")
    for uid, (en, ar) in UI.items():
        for lang, new_txt, old_txt in (("en", en, old_labels[uid][0]), ("ar", ar, old_labels[uid][1])):
            if new_txt is None:
                continue
            for oid in t06v.rows:
                if t06v.get(oid, f"verification_{lang}") == old_txt:
                    t06v.set("R85-B:C1", oid, f"verification_{lang}", new_txt, old_txt)
    # C2
    t06 = Table(s, "06_EVIDENCE_OBJECTS")
    for lang, txt in zip(("en", "ar"), XW):
        t06.set("R85-B:C2", "XW-FMIIP-005", f"title_{lang}", txt, t06.get("XW-FMIIP-005", f"title_{lang}"))
    # D1 (claim first; row deletions last)
    t07 = Table(s, "07_PUBLIC_CLAIMS")
    t07.set("R85-B:D1", "CLM-018", "evidence_inputs",
            '["73_PAYMENT_CURRENTNESS","REF-PAY-006","REF-PAY-011","REF-PAY-012","REF-PAY-013","EP-CBY-PAY-INSTITUTIONAL-2026"]',
            '["73_PAYMENT_CURRENTNESS","REF-PAY-010..013","EP-CBY-PAY-INSTITUTIONAL-2026"]')
    # D2
    t15 = Table(s, "15_SOURCE_LIBRARY")
    cards = [k for k in t15.rows if t15.get(k, "public_card_state") == "FULL_PUBLIC_CARD"]
    mapped = [x for _, _, ids in CATS.values() for x in ids]
    if sorted(cards) != sorted(mapped):
        raise TxError(f"curated cards differ from the category map: {sorted(set(cards) ^ set(mapped))}")
    for key, (en, ar, ids) in CATS.items():
        for sid in ids:
            t15.set("R85-B:D2", sid, "resource_category", en, t15.get(sid, "resource_category"))
            t15.set("R85-B:D2", sid, "resource_category_ar", ar, t15.get(sid, "resource_category_ar"))
    # D3
    g33 = s.grid("33_ANALYTICS_MASTER")
    for i, r in enumerate(g33, 1):
        if r and r[0] in DA:
            old, new = DA[r[0]]
            s.set("R85-B:D3", "33_ANALYTICS_MASTER", i, 3, new, old, f"{r[0]}.label")
    # D4 Unicode NFC, every text cell of every sheet
    from projection.master_reader import Workbook  # noqa: E402
    n = 0
    for sheet in list(s.ed.sheet_part):
        g = s.grid(sheet)
        for i, r in enumerate(g, 1):
            for j, v in enumerate(r or [], 1):
                if isinstance(v, str) and unicodedata.normalize("NFC", v) != v:
                    s.set("R85-B:D4", sheet, i, j, unicodedata.normalize("NFC", v), s.ed.get_value(sheet, i, j), f"{sheet}!r{i}c{j} NFC")
                    n += 1
    # D1 deletions
    g31 = s.grid("31_REFORMS_REGULATION")
    rows = [i for i, r in enumerate(g31, 1) if r and r[0] in ("REF-PAY-007", "REF-PAY-010")]
    if len(rows) != 2:
        raise TxError("31 duplicate rows not found")
    keep = {r[0]: r for r in g31 if r and r[0] in ("REF-PAY-006", "REF-PAY-013")}
    dup = {r[0]: r for r in g31 if r and r[0] in ("REF-PAY-007", "REF-PAY-010")}
    for a, b in (("REF-PAY-010", "REF-PAY-006"), ("REF-PAY-007", "REF-PAY-013")):
        if dup[a][1] != keep[b][1] or dup[a][7] != keep[b][7]:
            raise TxError(f"{a} is not a same-date, same-source duplicate of {b}")
    for row in sorted(rows, reverse=True):
        s.ed.delete_rows("31_REFORMS_REGULATION", row, row)
        s.ledger.append({"finding": "R85-B:D1", "sheet": "31_REFORMS_REGULATION", "row": row, "col": None, "field": "row deleted (duplicate event)", "old": None, "new": None})
    rep = s.save(out, ledger, {"transaction": "R85-B", "summary": f"R8.5 public-copy corrections; duplicate events merged; six resource categories; P3-D02 labels; NFC ({n} cells)"})
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}), "NFC cells", n)


if __name__ == "__main__":
    sys.path.insert(0, os.path.join(HERE, "..", "..", "scripts"))
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
