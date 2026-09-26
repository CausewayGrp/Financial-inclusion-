# -*- coding: utf-8 -*-
"""Tranche C transaction TC-I — residual bilingual defects outside the Reading prose.

  python3 tc_i_bilingual_residual.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Found by the bilingual-invariance test after TC-H (field-level and page-level):
  * BIL-02 (BLOCKER-class): the chronology period label had one language only, so every Arabic page that shows the
    financial-system chronology (/finance/, /data/) printed English dates ("February 2016", "By 30 May 2024",
    "Current analytical rule"). 14 gains period_en/period_ar; the Arabic facts that repeated the date drop it.
  * BIL-03: /payments/ Arabic title lacked the answer the English title gives (POS 561 -> 1,473).
  * BIL-04: evidence fields where one edition lacks a figure or date (ISO months printed to English readers,
    'that year' for 2014, number words that hid a figure) and five 11 fields whose Arabic was a generic paraphrase.
Out of scope by Lead decision (26 Sep 2026): Reading prose (08 thesis/question, RV-CWR visuals) is held for the
independent Reading package; see audit/TRANCHE_C_FINAL_ACCEPTANCE.md.
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from tc_lib import Session, Table, TxError  # noqa: E402

PERIOD_AR = {
    "YSC-001": "2014–2015", "YSC-002": "فبراير 2016", "YSC-003": "سبتمبر 2016", "YSC-004": "2017–2018",
    "YSC-005": "يناير–مارس 2018", "YSC-006": "ديسمبر 2019", "YSC-007": "أوائل 2020", "YSC-008": "أكتوبر 2022–يناير 2023",
    "YSC-009": "21 فبراير 2023", "YSC-010": "2023–2024", "YSC-011": "2022–2024", "YSC-012": "مارس–يونيو 2024",
    "YSC-024": "حتى 30 مايو 2024", "YSC-013": "قيمة 2024 كما رُوجعت بين إصدارات التقرير السنوي للبنك المركزي اليمني – عدن",
    "YSC-014": "2022–أبريل 2025", "YSC-015": "من يوليو 2025 فصاعدًا", "YSC-016": "منتصف يوليو–أوائل أغسطس 2025",
    "YSC-017": "سبتمبر 2025", "YSC-018": "فترة المشروع من 17 يونيو 2025 حتى 2030", "YSC-019": "1 مارس 2026",
    "YSC-021": "4 يونيو 2026", "YSC-022": "30 يونيو 2026", "YSC-023": "16 يوليو 2026", "YSC-020": "قاعدة التحليل المعمول بها",
}
DATE_IN_FACT = {"YSC-019": " في 1 مارس 2026", "YSC-021": " في 4 يونيو 2026", "YSC-022": " في 30 يونيو 2026", "YSC-023": " في 16 يوليو 2026"}


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    # ---- BIL-02: 14 period in both languages
    S14 = "14_SYSTEM_CHRONOLOGY"
    head = s.header(S14, 4)
    if head[1] != "period" or len(head) != 16:
        raise TxError(f"14 header not as expected: {head}")
    s.set("TC-I:BIL-02", S14, 4, 2, "period_en", "period", "14 header")
    s.set("TC-I:BIL-02", S14, 4, 17, "period_ar", None, "14 header")
    t14 = Table(s, S14)
    if set(t14.rows) != set(PERIOD_AR):
        raise TxError(f"14 events differ: {sorted(set(t14.rows) ^ set(PERIOD_AR))}")
    for eid, row in t14.rows.items():
        s.set("TC-I:BIL-02", S14, row, 17, PERIOD_AR[eid], None, f"{eid}.period_ar")
    for eid, frag in DATE_IN_FACT.items():
        s.replace("TC-I:BIL-02", S14, t14.rows[eid], t14.col("fact_ar"), frag, "", f"{eid}.fact_ar (date is the period label)")
    t14.set("TC-I:BIL-04", "YSC-009", "does_not_establish_ar",
            "مبلغ 0.775 مليار دولار الذي أتيح لاحقًا واستخدامه في مزادات النقد الأجنبي جزء من مبلغ المليار دولار نفسه، وليسا دعمًا إضافيًا.",
            "لا يجوز احتساب المليار دولار مرة أخرى عند عرض مبلغ 0.775 مليار دولار الذي أتيح لاحقًا أو استخدامات مزادات النقد الأجنبي.")
    t14.set("TC-I:BIL-04", "YSC-024", "does_not_establish_ar",
            "لا يثبت وجود 45,460 مستفيدًا وجودَ 45,460 مستخدمًا نشطًا مستمرًا، ولا معدلًا وطنيًا للشمول، ولا استمرار الاستخدام الرقمي بعد التحويل.",
            "لا يمثل 45,460 مستفيدًا عددًا مثبتًا لمستخدمين نشطين مستمرين، ولا معدلًا وطنيًا للشمول، ولا دليلًا على استمرار الاستخدام الرقمي بعد التحويل.")
    # ---- BIL-03: /payments/ title
    t02 = Table(s, "02_SITE_MAP")
    t02.set("TC-I:BIL-03", "/payments/", "title_ar",
            "المدفوعات: ارتفع عدد أجهزة نقاط البيع التي يُبلغ عنها البنك المركزي اليمني – عدن من 561 إلى 1,473 بين مارس 2025 ويناير 2026؛ أما عدد من يستخدمونها فغير مقيس",
            "تتوسع البنية التحتية للمدفوعات، لكن توسعها لا يخبرنا كم شخصًا يستخدمها.")
    # ---- BIL-04: Compare instruction
    s.replace_section("TC-I:BIL-04", "/evidence/compare/", 1, "ar", "body", "اختر من سجلين إلى أربعة.", "اختر من 2 إلى 4 سجلات.")
    # ---- BIL-04: 06 evidence fields
    t06 = Table(s, "06_EVIDENCE_OBJECTS")
    for oid in ("CLM-005", "CLM-006"):
        t06.set("TC-I:BIL-04", oid, "period_en", "September 2022", "2022-09")
    t06.set("TC-I:BIL-04", "CLM-013", "period_en", "OECD/INFE 2023 survey; CBY-Aden programme activity, March 2023 to March 2025",
            "OECD/INFE 2023 survey; CBY programme activity 2023-03 to 2025-03")
    for oid in ("CLM-028", "CLM-029", "CLM-030", "VIS-BORROWING-SOURCES-2014", "VIS-DOMESTIC-REMITTANCE-PATH-2014"):
        cur = t06.get(oid, "currentness_ar")
        frag = "وهي مأخوذة من الملف القطري لليمن الذي نشره البنك الدولي لذلك العام."
        if cur.count(frag) != 1:
            raise TxError(f"{oid} currentness_ar")
        t06.set("TC-I:BIL-04", oid, "currentness_ar", cur.replace(frag, "وهي مأخوذة من الملف القطري لليمن الذي نشره البنك الدولي لعام 2014."), cur)
    cur = t06.get("DS-FINDEX-HISTORY-CROSSWALK", "universe_ar")
    t06.set("TC-I:BIL-04", "DS-FINDEX-HISTORY-CROSSWALK", "universe_ar",
            cur.replace("المقاييس التاريخية الستة والثلاثون من مسح Findex", "مقاييس Findex التاريخية الـ36"), cur)
    FIRM_OLD = ("ولا تثبت قاعدة الأدلة ما إذا كانت هذه الاستجابات الثماني عشرة صادرة عن المنشآت الإحدى والثلاثين التي أفادت بخط ائتمان. "
                "وتصف هذه الأعداد الاستجابات الثماني عشرة وحدها،")
    FIRM_NEW = ("ولا تثبت قاعدة الأدلة ما إذا كانت هذه الاستجابات الـ18 صادرة عن المنشآت الـ31 التي أفادت بخط ائتمان. "
                "وتصف هذه الأعداد الاستجابات الـ18 وحدها،")
    cur = t06.get("VIS-FIRM-FINANCE-PATH", "summary_ar")
    if cur.count(FIRM_OLD) != 1:
        raise TxError("VIS-FIRM-FINANCE-PATH summary_ar")
    t06.set("TC-I:BIL-04", "VIS-FIRM-FINANCE-PATH", "summary_ar", cur.replace(FIRM_OLD, FIRM_NEW), cur)
    # ---- BIL-04: 11 visual-library fields
    t11 = Table(s, "11_VISUAL_LIBRARY")
    cur = t11.get("VIS-FIRM-FINANCE-PATH", "accessible_summary_ar")
    if cur.count(FIRM_OLD) != 1:
        raise TxError("VIS-FIRM-FINANCE-PATH accessible_summary_ar")
    t11.set("TC-I:BIL-04", "VIS-FIRM-FINANCE-PATH", "accessible_summary_ar", cur.replace(FIRM_OLD, FIRM_NEW), cur)
    V11 = [
        ("VIS-POS-VALUE", "decision_value_ar", "يعرض القيمة الاسمية بالريال اليمني لمعاملات نقاط البيع المبلغ عنها، ويُبقي قيمة سبتمبر 2025 المفقودة مفقودةً بدل استكمالها بالاستيفاء.",
         "يوضح تغير قيمة المعاملات الاسمية مع احترام الفجوة في البيانات وعدم تحويلها إلى نقطة مصطنعة."),
        ("VIS-FIRM-CONSTRAINTS", "decision_value_ar", "يضع الوصول إلى التمويل بجانب القيود الأخرى التي أفادت بها المنشآت في مسح المحافظات السبع لعام 2022، ويحافظ على إطار المسح بدل تقديم ترتيب وطني.",
         "يضع التمويل داخل منظومة القيود التي تواجه المنشآت ويحافظ على إطار المسح ذي السبع محافظات بدل تقديم ترتيب وطني."),
        ("VIS-FIRM-FINANCE-SEVERITY", "what_it_shows_ar", "يعرض نسبتي العائق الكبير (68.71%) والمتوسط (23.13%) داخل قاعدة الاحتساب المصفاة التي يستخدمها التقرير فقط، مع إظهار هذه القاعدة بوضوح.",
         "يعرض نسبة العائق الكبير ونسبة العائق المتوسط فقط داخل قاعدة الاحتساب المصفاة التي يستخدمها التقرير، مع إظهار هذه القاعدة بوضوح."),
        ("VIS-REMITTANCE-COST", "decision_value_ar", "يقارن التكاليف المعلنة في الربع الثالث من 2025 لممري السعودية–اليمن والإمارات–اليمن عند أحجام الإرسال نفسها، فيُظهر أثر حجم المبلغ من دون تقديمها متوسطًا وطنيًا.",
         "يوضح اختلاف التكلفة بين الممرات وأحجام الإرسال من دون تقديم الأسعار المعلنة باعتبارها متوسطًا وطنيًا لجميع الحوالات."),
        ("VIS-REMITTANCE-MACRO", "decision_value_ar", "يفصل القيم التي يوردها صندوق النقد الدولي للفترة 2018–2024 عن تقدير 2025 وتوقعات 2026–2030، ويُبقي وثيقتي الصندوق منفصلتين، حتى لا تُقرأ تغيرات التوقع تغيرًا اقتصاديًا.",
         "يمنع قراءة تغيرات التقدير أو التوقع باعتبارها تغيرات اقتصادية فعلية، ويُبقي وثيقتي الصندوق منفصلتين مع نسخة كل منهما وفترتها."),
    ]
    for vid, fld, new, old in V11:
        t11.set("TC-I:BIL-04", vid, fld, new, old)
    rep = s.save(out, ledger, {"transaction": "TC-I", "summary": "Chronology period in both languages; /payments/ AR title; residual evidence/visual bilingual parity (Reading prose excluded)"})
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
