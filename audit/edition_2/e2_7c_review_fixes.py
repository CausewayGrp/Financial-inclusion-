# -*- coding: utf-8 -*-
"""Edition 2 transaction E2-7c: the independent bilingual and adversarial review of E2-7 folded in (same batch).

  python3 e2_7c_review_fixes.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Nothing blocking; every new number confirmed in its original. Findings folded in (review numbering):
1. CLM-059: "independent account" reads as a bank account: "no independent source confirms it".
2. VIS-REMITTANCE-COST: the one outlier quote also lifts the US$500 average (20.24%; the others 2.26–3.12%); each count
   named with its corridor.
3. "reproduced exactly": the Saudi US$200 mean is 2.695, equal to the published 2.70 at the two decimals published.
4. Arabic labels: «لم يُتحقق» ("not verified") says more than "not re-read"; the site's term is «هذا الإصدار».
   The label becomes «فلم تُعَد في هذا الإصدار قراءةُ … في الأصل» everywhere (CLM-049, /reforms/, CLM-020, MF-ORIG,
   YSC-023).
5. CLM-020, MF-ORIG-001+002: SFD's 1997 inception is read in its Q4 2012 newsletter (p. 1); only the dating of
   microfinance's start to 1997 rests on the unreachable terms of reference. Value states split; the newsletter bound to
   MF-ORIG-001+002.
6. CLM-032 currentness names the 2021 and 2022 vintages. 7. CLM-032 summary: the reference year leads, "editions", not a
   series; limitations: the source notes differ by edition (2022: CBY and IMF staff estimates).
8.–10., 12. Arabic and English wording nits (POS, CLM-059, CLM-032, RPW method dated).
Not built: 11. (tokenizer fragments stated as TRIVIAL get a state class of their own): recorded in the edition-2 log.
"""
import json, os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "release_candidate"))
from rc_lib import Session, Table, TxError  # noqa: E402

F = "E2-7c:REVIEW"
NL = "SRC-SFD-Q4-2012-001"
R06 = [
    ("CLM-059", "limitations_en", "it is not shown by an independent account.", "no independent source confirms it."),
    ("CLM-059", "limitations_ar", "ولا يثبته حساب مستقل.", "ولا يؤكده مصدر مستقل."),
    ("CLM-059", "summary_ar", "وبإجمالي برامجي قدره 54.7 مليون دولار تفيد بأنه مصروف.",
     "وبأنها صرفت إجماليًا برامجيًا قدره 54.7 مليون دولار."),
    ("VIS-REMITTANCE-COST", "limitations_en",
     "each rests on few quotes (8 and 6), and one of the six United Arab Emirates quotes for US$200, at 22.71%, lifts that "
     "average well above the other five (2.97% to 5.25%).",
     "each rests on few quotes (8 for Saudi Arabia–Yemen, 6 for United Arab Emirates–Yemen), and a single United Arab "
     "Emirates quote, at 22.71% for US$200 and 20.24% for US$500, lifts both United Arab Emirates averages well above the "
     "other five quotes (2.97% to 5.25% for US$200; 2.26% to 3.12% for US$500)."),
    ("VIS-REMITTANCE-COST", "limitations_ar",
     "ويستند كل متوسط إلى عروض قليلة (8 و6)، ويرفع عرضٌ واحد من عروض الإمارات الستة لمبلغ 200 دولار، قدره 22.71%، ذلك "
     "المتوسط كثيرًا فوق العروض الخمسة الأخرى (من 2.97% إلى 5.25%).",
     "ويستند كل متوسط إلى عدد قليل من عروض الأسعار (8 لممر السعودية–اليمن، و6 لممر الإمارات–اليمن)، ويرفع عرضٌ واحد من "
     "عروض الإمارات، قدره 22.71% لمبلغ 200 دولار و20.24% لمبلغ 500 دولار، متوسطَي الإمارات كليهما بفارق كبير فوق العروض "
     "الخمسة الأخرى (من 2.97% إلى 5.25% لمبلغ 200 دولار، ومن 2.26% إلى 3.12% لمبلغ 500 دولار)."),
    ("VIS-REMITTANCE-COST", "method_en",
     "The corridor pages refuse automated requests; on 4 October 2026 each of the four averages was reproduced exactly as",
     "The corridor pages refuse automated requests (on 4 October 2026); that day each of the four averages was reproduced, "
     "to the two decimals published, as"),
    ("VIS-REMITTANCE-COST", "method_ar",
     "وترفض صفحتا الممرين الطلبات الآلية؛ وفي 4 أكتوبر 2026 أُعيد حساب كلٍّ من المتوسطات الأربعة فطابق المنشور، بوصفه "
     "المتوسط البسيط لعروض أسعار الربع الثالث من 2025 في مجموعة بيانات عروض الأسعار التفصيلية لقاعدة Remittance Prices "
     "Worldwide التابعة للبنك الدولي (8 عروض لممر السعودية–اليمن، و6 لممر الإمارات–اليمن).",
     "وترفض صفحتا الممرين الطلبات الآلية (في 4 أكتوبر 2026)؛ وفي ذلك اليوم أُعيد حساب كلٍّ من المتوسطات الأربعة بوصفه "
     "المتوسط البسيط لعروض أسعار الربع الثالث من 2025 في مجموعة بيانات عروض الأسعار التفصيلية لقاعدة Remittance Prices "
     "Worldwide التابعة للبنك الدولي (8 عروض لممر السعودية–اليمن، و6 لممر الإمارات–اليمن)، فطابق القيمة المنشورة حتى "
     "منزلتين عشريتين."),
    ("CLM-049", "summary_ar", "فلم يُتحقق من التاريخ ومدة 18 شهرًا والوضع المذكور أعلاه في الأصل في هذه الطبعة.",
     "فلم تُعَد في هذا الإصدار قراءةُ التاريخ ومدة الـ18 شهرًا ووضعِ الاتفاق المذكورة أعلاه في الأصل."),
    ("CLM-032", "currentness_en", "the restatement concerns 2024, first published in the 2024 annual report and restated in "
     "the 2025 annual report.",
     "the headline restatement concerns 2024, first published in the 2024 annual report and restated in the 2025 annual "
     "report; the values for 2021 and 2022 differ across the 2022, 2023, 2024 and 2025 reports."),
    ("CLM-032", "currentness_ar", "وتخص إعادة العرض عام 2024، الذي نُشر أولًا في التقرير السنوي 2024 ثم أُعيد عرضه في "
     "التقرير السنوي 2025.",
     "وتخص إعادة العرض الرئيسية عام 2024، الذي نُشر أولًا في التقرير السنوي 2024 ثم أُعيد عرضه في التقرير السنوي 2025؛ "
     "وتختلف قيمتا عامي 2021 و2022 بين تقارير 2022 و2023 و2024 و2025."),
    ("CLM-032", "summary_en",
     "The same holds further back: for 2021, the annual reports of 2022, 2023, 2024 and 2025 print USD 4,043, 5,400.0, "
     "5,625 and 2,900.22 million; for 2022, USD 4,454, 6,000, 6,000 and 3,066.58 million.",
     "The same holds further back. For reference year 2021, the 2022, 2023, 2024 and 2025 editions of the annual report "
     "give USD 4,043, 5,400.0, 5,625 and 2,900.22 million; for reference year 2022, they give USD 4,454, 6,000, 6,000 and "
     "3,066.58 million. These are successive editions' values for one year, not a series over time."),
    ("CLM-032", "summary_ar",
     "ويصح ذلك على سنوات أسبق أيضًا: فلعام 2021 تطبع التقارير السنوية لأعوام 2022 و2023 و2024 و2025 القيم 4,043 و5,400.0 "
     "و5,625 و2,900.22 مليون دولار، ولعام 2022 القيم 4,454 و6,000 و6,000 و3,066.58 مليون دولار.",
     "ويصح ذلك على سنوات أسبق أيضًا: فلسنة 2021 المرجعية تورد إصدارات التقرير السنوي لأعوام 2022 و2023 و2024 و2025 القيم "
     "4,043 و5,400.0 و5,625 و2,900.22 مليون دولار، ولسنة 2022 المرجعية القيم 4,454 و6,000 و6,000 و3,066.58 مليون دولار. "
     "وهذه قيم إصدارات متعاقبة لسنة واحدة، لا سلسلة زمنية."),
    ("CLM-032", "limitations_en", "this record uses Table 4-1 (p. 37).",
     "this record uses Table 4-1 (p. 37). The source notes also differ: the 2022 report cites the CBY and IMF staff "
     "estimates (October 2022), the 2023 and 2024 reports the CBY and the IMF, and the 2025 report the CBY, the Yemen "
     "Customs Authority, two ministries and international trade and banking sources."),
    ("CLM-032", "limitations_ar", "تنزاح تسميات الصفوف سطرًا واحدًا، فيطبع الصف المسمى «حوالات العاملين» ميزان التحويلات؛ "
     "ويعتمد هذا السجل على الجدول 4-1 (ص 37).",
     "تنزاح تسميات الصفوف بمقدار سطر واحد، فيحمل الصف المسمى «حوالات العاملين» قيمة ميزان التحويلات؛ ويعتمد هذا السجل على "
     "الجدول 4-1 (ص 37). وتختلف ملاحظات المصدر أيضًا: فتقرير 2022 يستند إلى البنك المركزي وتقديرات خبراء صندوق النقد "
     "الدولي (أكتوبر 2022)، وتقريرا 2023 و2024 إلى البنك المركزي وصندوق النقد الدولي، وتقرير 2025 إلى البنك المركزي ومصلحة "
     "الجمارك اليمنية ووزارتين ومصادر دولية للتجارة والمصارف."),
]
for _v in ("VIS-POS-TERMINALS", "VIS-POS-TRANSACTIONS", "VIS-POS-VALUE"):
    R06 += [(_v, "limitations_en", "and its design changes in January and again in February 2026;",
             "and its design changed in January 2026 and again in February 2026;"),
            (_v, "limitations_ar", "وكل إصدار شهري منذ مارس 2025 إنفوغرافيك من صفحة واحدة، ويتغير تصميمه في يناير ثم في فبراير 2026؛",
             "وكل إصدار شهري منذ مارس 2025 إنفوغرافيك من صفحة واحدة، وقد تغيّر تصميمه في يناير 2026 ثم في فبراير 2026؛")]
SFD_EN_OLD = (" The 2012 SFD document that dates the start of microfinance to 1997 could not be re-opened on 4 October 2026 "
              "(its archived copy is not reachable from this resource), so that date has not been re-read in the original "
              "for this edition.")
SFD_EN_NEW = (" SFD's 1997 inception is re-read in its fourth-quarter 2012 newsletter (p. 1), but the SFD terms of reference "
              "that date the start of microfinance to 1997 could not be re-opened on 4 October 2026 (their archived copy is "
              "not reachable from this resource), so that dating has not been re-read in the original for this edition.")
SFD_AR_OLD = (" وتعذّرت في 4 أكتوبر 2026 إعادة فتح وثيقة الصندوق لعام 2012 التي تؤرخ بداية التمويل الأصغر بعام 1997 (لا يمكن "
              "الوصول إلى نسختها المؤرشفة من هذا المورد)، فلم يُتحقق من هذا التاريخ في الأصل في هذه الطبعة.")
SFD_AR_NEW = (" وأُعيدت قراءة نشأة الصندوق عام 1997 في نشرته للربع الرابع من 2012 (ص 1)، أما الشروط المرجعية للصندوق التي "
              "تؤرخ بداية التمويل الأصغر بعام 1997 فتعذّرت إعادة فتحها في 4 أكتوبر 2026 (لا يمكن الوصول إلى نسختها المؤرشفة "
              "من هذا المورد)، فلم تُعَد في هذا الإصدار قراءةُ هذا التأريخ في الأصل.")
SEC = [("en", None, None),
       ("ar", "فلم يُتحقق من هذه التفاصيل في الأصل في هذه الطبعة.", "فلم تُعَد في هذا الإصدار قراءةُ هذه التفاصيل في الأصل.")]
YSC = ("فلم يُتحقق من هذا المدخل في الأصل في هذه الطبعة.", "فلم تُعَد في هذا الإصدار قراءةُ هذا المدخل في الأصل.")
RPW_STATES = [("20.24%", "cc2 total cost % of the same outlier quote"), ("2.26%", "lowest cc2 total cost % of the other five"),
              ("3.12%", "highest cc2 total cost % of the other five")]


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    t06 = Table(s, "06_EVIDENCE_OBJECTS", 4)
    for oid, field, old, new in R06:
        s.replace(F, "06_EVIDENCE_OBJECTS", t06.rows[oid], t06.col(field), old, new, f"{oid}.{field}")
    for oid in ("CLM-020", "MF-ORIG-001+002"):
        s.replace(F, "06_EVIDENCE_OBJECTS", t06.rows[oid], t06.col("summary_en"), SFD_EN_OLD, SFD_EN_NEW, f"{oid}.summary_en")
        s.replace(F, "06_EVIDENCE_OBJECTS", t06.rows[oid], t06.col("summary_ar"), SFD_AR_OLD, SFD_AR_NEW, f"{oid}.summary_ar")
        cur = t06.get(oid, "value_states")
        vs = json.loads(cur)
        vs.append({"t": "1997", "k": "d", "s": "READ", "src": NL,
                   "loc": "SFD Newsletter No. 60 (Oct–Dec 2012), p. 1: 'Since its inception in 1997, the Social Fund for Development' (SFD's inception, not the start of microfinance)"})
        t06.set(F, oid, "value_states", json.dumps(vs, ensure_ascii=False, separators=(",", ":")), cur)
    deps = t06.get("MF-ORIG-001+002", "source_dependencies")
    if NL not in deps:
        t06.set(F, "MF-ORIG-001+002", "source_dependencies", deps + "; " + NL, deps)
    cur = t06.get("VIS-REMITTANCE-COST", "value_states")
    vs = json.loads(cur)
    vs += [{"t": t, "k": "v", "s": "READ", "src": "SRC-WB-RPW-UAE-YEM-2025Q3-001",
            "loc": f"RPW quote-level dataset, sheet 'Dataset (from Q2 2016)', 2025_3Q, United Arab Emirates to Yemen, {w}"} for t, w in RPW_STATES]
    t06.set(F, "VIS-REMITTANCE-COST", "value_states", json.dumps(vs, ensure_ascii=False, separators=(",", ":")), cur)
    cur = t06.get("CLM-032", "value_states")
    vs = json.loads(cur) + [{"t": "October 2022", "k": "d", "s": "READ", "src": "SRC-CBY-AR2022-001",
                             "loc": "Annual Report 2022 (Arabic), Table 4-1, p. 37, source line: CBY and IMF staff estimates, October 2022"}]
    t06.set(F, "CLM-032", "value_states", json.dumps(vs, ensure_ascii=False, separators=(",", ":")), cur)
    s.replace_section(F, "/reforms/", 7, "ar", "body", SEC[1][1], SEC[1][2])
    t14 = Table(s, "14_SYSTEM_CHRONOLOGY", 4)
    s.replace(F, "14_SYSTEM_CHRONOLOGY", t14.rows["YSC-023"], t14.col("verification_note_ar"), *YSC, "YSC-023.verification_note_ar")
    rep = s.save(out, ledger, OrderedDict([("transaction", "E2-7c"), ("summary", "E2-7 independent review folded in: wording, the RPW outlier at both amounts, Arabic labels, SFD 1997 split, CLM-032 vintages")]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
