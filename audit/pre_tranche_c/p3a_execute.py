# -*- coding: utf-8 -*-
"""P3-A — visual-contract truth corrections found while writing the P3 data contracts (Master-first).

  python3 p3a_execute.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Every new value is derived from other governed Master fields (named per finding); no fact, number or source is added.
Findings are recorded as P3-F01..F12 in audit/pre_tranche_c/FINDINGS_LEDGER.csv.
"""
import datetime, sys
from ptc_lib import Session, TxError

S = None


def hdr_row(sheet, name):
    g = S.grid(sheet)
    for i in range(1, 8):
        if name in [str(x) for x in g[i - 1] if x is not None]:
            return i, [str(x) if x is not None else None for x in g[i - 1]]
    raise TxError(f"{sheet}: no header {name!r}")


def row_of(sheet, key, keycol_name):
    hr, h = hdr_row(sheet, keycol_name)
    kc = h.index(keycol_name)
    g = S.grid(sheet)
    hits = [i for i, r in enumerate(g, 1) if i > hr and r and len(r) > kc and r[kc] == key]
    if len(hits) != 1:
        raise TxError(f"{sheet}: key {key!r} found {len(hits)} times")
    return hits[0], h


def cell(finding, sheet, key, keycol, col, new, expect):
    r, h = row_of(sheet, key, keycol)
    S.set(finding, sheet, r, h.index(col) + 1, new, expect, f"{key}.{col}")


def sub(finding, sheet, key, keycol, col, old, new):
    r, h = row_of(sheet, key, keycol)
    S.replace(finding, sheet, r, h.index(col) + 1, old, new, f"{key}.{col}")


def main():
    global S
    src, out, ledger, work = sys.argv[1:5]
    S = Session(src, work)
    V, E, C = "11_VISUAL_LIBRARY", "06_EVIDENCE_OBJECTS", "07_PUBLIC_CLAIMS"

    # P3-F01 Metadata copied from another visual's row (evidence_strength / freshness_profile). New values come from the
    # row's own period/source_period and from the governed class of its data (35 fi_relevance_class; 34 EP-FIRM-2022).
    cell("P3-F01", V, "VIS-CAPITAL-CONTEXT", "visual_id", "evidence_strength", "HUMANITARIAN_CONTEXT_ONLY", "HIGH_MACRO")
    cell("P3-F01", V, "VIS-CAPITAL-CONTEXT", "visual_id", "freshness_profile", "Event-level flows; 2026 context",
         "2018–2030: reported history (staff report) / estimate and projections (supplement)")
    cell("P3-F01", V, "VIS-FIRM-CONSTRAINTS", "visual_id", "evidence_strength", "PRIMARY_SURVEY", "HIGH_QUOTE_BOUNDED")
    cell("P3-F01", V, "VIS-FIRM-CONSTRAINTS", "visual_id", "freshness_profile", "2022 custom survey", "2025-Q3")
    cell("P3-F01", V, "VIS-FIRM-FINANCE-SEVERITY", "visual_id", "evidence_strength", "PRIMARY_SURVEY", "HIGH_BUT_COVERAGE_LIMITED")
    cell("P3-F01", V, "VIS-FIRM-FINANCE-SEVERITY", "visual_id", "freshness_profile", "2022 custom survey; report-specific filtered tabulation",
         "2022 observation; wave/fieldwork caveats explicit")
    cell("P3-F01", V, "VIS-FCP-REDRESS-PATH", "visual_id", "freshness_profile", "2023–2024 framework; outcome evidence open", "2021→2024/current gaps")

    # P3-F02 VIS-FINDEX-GAPS: "2022 observation" collapses reporting year, study wave and fieldwork. Align to CLM-001's
    # governed period/universe/currentness. Title: present-tense "left behind" and Arabic «الوصول» (access) replaced.
    clm_period_en = "World Bank reporting year 2022; Global Findex 2021 study; Yemen fieldwork 2022-11-07 to 2023-01-09"
    clm_period_ar = "سنة الإبلاغ في بيانات البنك الدولي: 2022؛ دراسة Global Findex 2021؛ العمل الميداني في اليمن من 2022-11-07 إلى 2023-01-09"
    t_en, t_ar = "Account ownership and measured gaps in the latest Yemen survey", "امتلاك الحساب والفجوات المقاسة في أحدث مسح لليمن"
    for sh, ten, tar in ((V, "title_en", "title_ar"), (E, "title_en", "title_ar")):
        key = "visual_id" if sh == V else "object_id"
        cell("P3-F02", sh, "VIS-FINDEX-GAPS", key, ten, t_en, "Account Ownership — Who is being left behind?")
        cell("P3-F02", sh, "VIS-FINDEX-GAPS", key, tar, t_ar, "امتلاك الحساب: من تبقى خارج الوصول؟")
    cell("P3-F02", V, "VIS-FINDEX-GAPS", "visual_id", "period", clm_period_en, "2022 observation")
    cell("P3-F02", V, "VIS-FINDEX-GAPS", "visual_id", "source_period",
         "Global Findex 2021 study (Yemen fieldwork 2022-11-07 to 2023-01-09): total/female/male/poorest40/richest60/primary-or-less",
         "2022 total/female/male/poorest40/richest60/primary-or-less")
    cell("P3-F02", V, "VIS-FINDEX-GAPS", "visual_id", "freshness_profile",
         "World Bank reporting year 2022; Findex 2021 study; no newer Yemen observation in the Findex 2025 edition",
         "2022 observation; wave/fieldwork caveats explicit")
    cell("P3-F02", V, "VIS-FINDEX-GAPS", "visual_id", "denominator_universe",
         "Adults 15+ in survey coverage; same-wave subgroup definitions", "2022 Findex Yemen observation universe and subgroup definitions")
    cell("P3-F02", E, "VIS-FINDEX-GAPS", "object_id", "period_en", clm_period_en, "2022 observation")
    cell("P3-F02", E, "VIS-FINDEX-GAPS", "object_id", "period_ar", clm_period_ar, "مشاهدة 2022")
    cell("P3-F02", E, "VIS-FINDEX-GAPS", "object_id", "universe_en", "Adults 15+ in survey coverage; same-wave subgroup definitions",
         "2022 Findex Yemen observation universe and subgroup definitions")
    cell("P3-F02", E, "VIS-FINDEX-GAPS", "object_id", "universe_ar",
         "الأشخاص بعمر 15 سنة فأكثر ضمن التغطية التي شملها المسح، وفق تعريفات المجموعات الفرعية داخل الموجة نفسها.",
         "مجتمع ملاحظة Findex اليمنية المضبوطة لعام 2022 وتعريفات المجموعات الفرعية المتوافقة داخل الموجة.")
    cell("P3-F02", E, "VIS-FINDEX-GAPS", "object_id", "currentness_en",
         "As of the Global Findex 2025 edition, Yemen’s latest available account-ownership observation remains the 2022 World Bank value derived from the Yemen Findex 2021 study. Do not relabel it as a 2024, 2025 or 2026 population rate.",
         "Currentness is bounded to 2022 observation. Do not carry the value, status or interpretation beyond the latest comparable evidence available from a comparable source without a newer comparable observation.")
    cell("P3-F02", E, "VIS-FINDEX-GAPS", "object_id", "currentness_ar",
         "حتى نسخة Global Findex 2025، تظل أحدث مشاهدة متاحة لامتلاك الحساب في اليمن هي قيمة البنك الدولي لسنة 2022 المستمدة من دراسة اليمن ضمن موجة Findex 2021. ولا يجوز إعادة وصفها باعتبارها معدلًا سكانيًا لعام 2024 أو 2025 أو 2026.",
         "تقتصر حداثة هذا الدليل على مشاهدة 2022. ولا يجوز ترحيل القيمة أو الحالة أو التفسير إلى فترة لاحقة على أحدث دليل قابل للمقارنة من دون مشاهدة أحدث قابلة للمقارنة.")

    # P3-F03 IMF remittance series: scope is the IMF analytical scope for IRG areas (CLM-036/CLM-042 governed universes);
    # 2018-2024 are reported history from staff calculations, not "observed" (Tranche B REFINE of this visual);
    # projections are not current evidence.
    uni_en = "IMF external-sector remittance series on the IMF’s analytical scope for areas under the internationally recognized government; evidence state and source document by year"
    uni_ar = "سلسلة صندوق النقد للتحويلات في القطاع الخارجي ضمن النطاق التحليلي للصندوق الخاص بمناطق الحكومة المعترف بها دوليًا، مع حالة كل سنة ووثيقة مصدرها."
    old_uni = "IMF external-sector remittance series; evidence state and source document by year"
    cell("P3-F03", V, "VIS-REMITTANCE-MACRO", "visual_id", "denominator_universe", uni_en, old_uni)
    cell("P3-F03", E, "VIS-REMITTANCE-MACRO", "object_id", "universe_en", uni_en, old_uni)
    cell("P3-F03", E, "VIS-REMITTANCE-MACRO", "object_id", "universe_ar", uni_ar, "سلسلة صندوق النقد للتحويلات في القطاع الخارجي، مع حالة كل سنة ووثيقة مصدرها.")
    cell("P3-F03", E, "VIS-REMITTANCE-MACRO", "object_id", "currentness_en",
         "Reported history runs to 2024 (IMF staff report, staff calculations); 2025 is an estimate and 2026–2030 are projections from a later supplement. Estimates and projections are not observations: do not treat 2025–2030 values as current evidence.",
         "Currentness is bounded to 2018–2030. Do not carry the value, status or interpretation beyond the latest comparable evidence available from a comparable source without a newer comparable observation.")
    cell("P3-F03", E, "VIS-REMITTANCE-MACRO", "object_id", "currentness_ar",
         "يمتد التاريخ المبلغ عنه حتى 2024 (تقرير خبراء صندوق النقد، وفق حسابات الخبراء)؛ أما 2025 فتقدير، و2026–2030 توقعات من ملحق لاحق. والتقديرات والتوقعات ليست مشاهدات، فلا تُعامل قيم 2025–2030 بوصفها أدلة حالية.",
         "تقتصر حداثة هذا الدليل على 2018–2030. ولا يجوز ترحيل القيمة أو الحالة أو التفسير إلى فترة لاحقة على أحدث دليل قابل للمقارنة من دون مشاهدة أحدث قابلة للمقارنة.")
    cell("P3-F03", E, "CLM-007", "object_id", "period_en", "Reported history 2018–2024 (staff calculations); estimate 2025; projection 2026–2030",
         "Observed 2018–2024; estimate 2025; projection 2026–2030")
    cell("P3-F03", E, "CLM-007", "object_id", "period_ar", "تاريخ مبلغ عنه 2018–2024 (حسابات الخبراء)؛ تقدير 2025؛ توقعات 2026–2030",
         "مرصود 2018–2024؛ تقدير 2025؛ توقعات 2026–2030")
    sub("P3-F03", E, "CLM-007", "object_id", "currentness_en", "Currentness is bounded to Observed 2018–2024;",
        "Currentness is bounded to reported history 2018–2024 (staff calculations);")
    sub("P3-F03", E, "CLM-007", "object_id", "currentness_ar", "تقتصر حداثة هذا الدليل على مرصود 2018–2024؛",
        "تقتصر حداثة هذا الدليل على تاريخ مبلغ عنه 2018–2024 (حسابات الخبراء)؛")
    P = "34_EVIDENCE_PASSPORTS"
    cell("P3-F03", P, "EP-REMITTANCE-MACRO", "passport_id", "reference_period",
         "Reported history 2018–2024 (staff calculations); estimate 2025; projection 2026–2030", "Observed 2018–2024; estimate 2025; projection 2026–2030")
    cell("P3-F03", P, "EP-REMITTANCE-MACRO", "passport_id", "universe",
         "External-sector macro concept; IMF analytical scope for areas under the internationally recognized government", "External-sector macro concept")
    cell("P3-F03", P, "EP-REMITTANCE-MACRO", "passport_id", "display_requirements",
         "Reported-history, estimate and projection states must be visually separate, and the line breaks where the source document changes.",
         "Observed and forecast states must be visually separate.")

    # P3-F04 POS titles are the in-frame text of a detached chart: "Footprint" implies reach, "Usage" implies people;
    # the value series must say "nominal". Transactions summary: endpoint framing hid the July 2025 high (19 OBS-00064).
    titles = {"VIS-POS-TERMINALS": (("POS Footprint Pulse", "تطور نقاط البيع"), ("Reported POS terminals, monthly", "أجهزة نقاط البيع المبلغ عنها شهريًا")),
              "VIS-POS-TRANSACTIONS": (("POS Usage Pulse", "تطور استخدام نقاط البيع"), ("Reported POS transactions, monthly", "معاملات نقاط البيع المبلغ عنها شهريًا")),
              "VIS-POS-VALUE": (("POS Transaction Value", "قيمة معاملات نقاط البيع"),
                                ("Nominal value of reported POS transactions, monthly", "القيمة الاسمية لمعاملات نقاط البيع المبلغ عنها شهريًا"))}
    for vid, ((oen, oar), (nen, nar)) in titles.items():
        for sh, key in ((V, "visual_id"), (E, "object_id")):
            cell("P3-F04", sh, vid, key, "title_en", nen, oen)
            cell("P3-F04", sh, vid, key, "title_ar", nar, oar)
    peak_en = ("Reported POS transactions rose from 8,015 in March 2025 to 24,026 in January 2026.",
               "Reported POS transactions rose from 8,015 in March 2025 to 24,026 in January 2026, but not steadily: the monthly high was 27,187 in July 2025.")
    peak_ar = ("ارتفع عدد معاملات نقاط البيع المبلغ عنها من 8,015 معاملة في مارس 2025 إلى 24,026 معاملة في يناير 2026.",
               "ارتفع عدد معاملات نقاط البيع المبلغ عنها من 8,015 معاملة في مارس 2025 إلى 24,026 معاملة في يناير 2026، ولكن ليس بصورة مطردة: فقد بلغ أعلى مستوى شهري 27,187 معاملة في يوليو 2025.")
    sub("P3-F04", V, "VIS-POS-TRANSACTIONS", "visual_id", "accessible_summary_en", *peak_en)
    sub("P3-F04", V, "VIS-POS-TRANSACTIONS", "visual_id", "accessible_summary_ar", *peak_ar)
    sub("P3-F04", E, "VIS-POS-TRANSACTIONS", "object_id", "summary_en", *peak_en)
    sub("P3-F04", E, "VIS-POS-TRANSACTIONS", "object_id", "summary_ar", *peak_ar)

    # P3-F05 Arrows between numbers in Arabic text: U+2192 is not mirrored in RTL, so "a→b" displays pointing against the
    # reading order. Written out in words instead.
    sub("P3-F05", V, "VIS-POS-TERMINALS", "visual_id", "what_it_shows_ar", "الذي تعطيه الأرقام 1,357→1,473؛",
        "الذي تعطيه زيادة الأرقام من 1,357 إلى 1,473؛")
    sub("P3-F05", E, "CLM-010", "object_id", "limitations_ar", "التسلسل 7→9→8", "التسلسل 7 ثم 9 ثم 8")
    sub("P3-F05", C, "CLM-010", "claim_id", "does_not_prove_ar", "التسلسل 7→9→8", "التسلسل 7 ثم 9 ثم 8")
    A = "33_ANALYTICS_MASTER"
    for r in (17, 18):
        S.replace("P3-F05", A, r, 9, "بين الإمارات→اليمن والسعودية→اليمن", "بين ممري الإمارات–اليمن والسعودية–اليمن", "DA corridor note_ar")

    # P3-F06 Research-tool artefacts in 20 governed source locators ("web ref turn…"); the month is already carried by source_id.
    g19 = S.grid("19_PAYMENTS_DATA")
    n = 0
    for i, r in enumerate(g19, 1):
        v = r[10] if len(r) > 10 else None
        if isinstance(v, str) and v.startswith("one-page monthly POS infographic; web ref turn"):
            S.set("P3-F06", "19_PAYMENTS_DATA", i, 11, "one-page monthly POS infographic", v, f"{r[0]}.source_locator")
            n += 1
    if n != 20:
        raise TxError(f"P3-F06 expected 20 artefact locators, found {n}")

    # P3-F07 Home system map promised an evidence state on each link; 13_SYSTEM_RELATIONSHIPS governs none (21 of 26 links
    # carry no reference). The contract now describes what the data support: documented relationship statements, text-first.
    it = "VIS-INCLUSION-TRANSMISSION"
    new_t_en, new_t_ar = "Financial inclusion is a connected system, not a sector score", "الشمول المالي منظومة مترابطة، لا درجة واحدة"
    for sh, key in ((V, "visual_id"), (E, "object_id")):
        cell("P3-F07", sh, it, key, "title_en", new_t_en, "Financial inclusion is a transmission system, not a sector score")
        cell("P3-F07", sh, it, key, "title_ar", new_t_ar, "الشمول المالي منظومة انتقال، لا درجة واحدة")
    cell("P3-F07", V, it, "visual_id", "visual_form", "TEXT_FIRST_SYSTEM_RELATIONSHIP_LIST",
         "LAYERED_SYSTEM_MAP__PEOPLE_FIRMS_PROVIDERS_RAILS_FLOWS_RULES_CONTEXT")
    cell("P3-F07", V, it, "visual_id", "what_it_shows_en",
         "The documented relationships between people and capability, firms and income, providers, payment rails, remittance and capital flows, regulation and protection, and enabling constraints. Each relationship states what the evidence supports and what it does not establish; no link carries an evidence-strength rating, and there is no composite score.",
         "A layered map of the financial-inclusion system linking people and capability, firms and income, providers, payment rails, remittance and capital flows, regulation and protection, and enabling constraints, with the evidence state marked on each link and no composite score.")
    cell("P3-F07", V, it, "visual_id", "what_it_shows_ar",
         "يعرض العلاقات الموثقة بين الناس والقدرات، والمنشآت والدخل، ومقدمي الخدمات، وبنية المدفوعات، وتدفقات الحوالات ورأس المال، والتنظيم والحماية، والقيود المُمكِّنة أو المعطلة. وتذكر كل علاقة ما تسنده الأدلة وما لا تثبته؛ ولا تحمل أي علاقة تقديرًا لقوة الدليل، ولا توجد درجة مركبة.",
         "يستخدم خريطة هادئة متعددة الطبقات تربط الناس والقدرات، والمنشآت والدخل، ومقدمي الخدمات، وسكك الدفع، والتحويلات وتدفقات رأس المال، والتنظيم والحماية، والقيود الممكّنة، مع إظهار نوع الدليل عند كل رابط.")
    cell("P3-F07", V, it, "visual_id", "evidence_strength", "SYNTHESIS__RELATIONSHIP_STATEMENTS_ONLY", "SYNTHESIS__EVIDENCE_BOUND")
    enc_en = "Ordered list of documented relationships grouped by system layer; each item names its relationship type and what it does not establish. Adjacency is not causality: no arrows and no evidence-strength marker, because none is governed per link."
    enc_ar = "قائمة مرتبة بالعلاقات الموثقة مجمعة بحسب طبقات المنظومة؛ يذكر كل بند نوع العلاقة وما لا تثبته. والتجاور لا يعني السببية: فلا أسهم ولا علامة لقوة الدليل، لأن قوة الدليل غير محددة لكل علاقة."
    cell("P3-F07", V, it, "visual_id", "encoding_contract", enc_en, "6–7 calm layers with evidence-state markers; adjacency not causality.")
    cell("P3-F07", E, it, "object_id", "method_en", enc_en, "6–7 calm layers with evidence-state markers; adjacency not causality.")
    cell("P3-F07", E, it, "object_id", "method_ar", enc_ar,
         "يعرض الشكل ستًا إلى سبع طبقات هادئة مع علامات لحالة الدليل؛ ويشير التجاور إلى صلة في النظام لا إلى علاقة سببية.")
    pi_ar = "لا أسهم سببية ما لم يدعمها دليل مستقل، ولا مؤشر مركب، ولا إيحاء بأن مجالًا يسبب آخر بصورة آلية."
    cell("P3-F07", V, it, "visual_id", "prohibited_inference_ar", pi_ar, "لا مؤشر مركب ولا أسهم سببية ما لم يدعمها دليل مستقل.")
    cell("P3-F07", E, it, "object_id", "limitations_ar", pi_ar, "لا مؤشر مركب ولا أسهم سببية ما لم يدعمها دليل مستقل.")
    # relationship references: registered chronology dataset (16 DS-V4R3-SYSTEM-CHRONOLOGY) and the SMEPS KPI claim (CLM-060)
    R = "13_SYSTEM_RELATIONSHIPS"
    for sl in ("SL-022", "SL-023", "SL-024", "SL-025", "SL-026"):
        cell("P3-F07", R, sl, "link_id", "from", "DS-V4R3-SYSTEM-CHRONOLOGY", "DS-SYSTEM-CHRONOLOGY")
        cell("P3-F07", R, sl, "link_id", "evidence_refs", '["DS-V4R3-SYSTEM-CHRONOLOGY"]', '["DS-SYSTEM-CHRONOLOGY"]')
    cell("P3-F07", R, "SL-019", "link_id", "from", "CLM-060", "SMEPS-FINACC-2024")

    # P3-F08 RV-CWR-006 title asserted divergence; its own decision value and the CWR-006 thesis say anchors, not a trend.
    cell("P3-F08", V, "RV-CWR-006", "visual_id", "title_en", "Borrowers, savers and portfolio: separate anchors, not one trend",
         "Borrowers, savers and portfolio are moving differently")
    cell("P3-F08", V, "RV-CWR-006", "visual_id", "title_ar", "المقترضون والمدخرون والمحفظة: نقاط مرجعية منفصلة، لا اتجاه واحد",
         "المقترضون والمدخرون والمحفظة لا يتحركون بالطريقة نفسها")

    # P3-F09 Boundary copy named "manipulation" as a possibility about a named official source; the method-scrutiny boundary
    # (smoothing, interpolation, real-world volatility) is kept without introducing an allegation of intent.
    sub("P3-F09", E, "CLM-034", "object_id", "summary_en", "smoothing, interpolation, manipulation or low", "smoothing, interpolation or low")
    sub("P3-F09", E, "CLM-034", "object_id", "summary_ar", "تسوية أو استيفاء أو تلاعب أو انخفاض", "تسوية أو استيفاء أو انخفاض")
    sub("P3-F09", E, "CLM-034", "object_id", "method_en", "proof of smoothing or manipulation", "proof of smoothing or interpolation")
    sub("P3-F09", E, "CLM-034", "object_id", "method_ar", "التنعيم أو الاستيفاء أو التلاعب", "التنعيم أو الاستيفاء")
    sub("P3-F09", E, "CLM-034", "object_id", "limitations_en", "smoothing, interpolation, manipulation or low", "smoothing, interpolation or low")
    sub("P3-F09", E, "CLM-034", "object_id", "limitations_ar", "تنعيم أو استيفاء أو تلاعب أو تقلب", "تنعيم أو استيفاء أو تقلب")
    sub("P3-F09", C, "CLM-034", "claim_id", "copy_en", "smoothing, interpolation, manipulation or low", "smoothing, interpolation or low")
    sub("P3-F09", C, "CLM-034", "claim_id", "copy_ar", "تسوية أو استيفاء أو تلاعب أو انخفاض", "تسوية أو استيفاء أو انخفاض")
    sub("P3-F09", C, "CLM-034", "claim_id", "does_not_prove_en", "smoothing, interpolation, manipulation or low", "smoothing, interpolation or low")
    sub("P3-F09", C, "CLM-034", "claim_id", "does_not_prove_ar", "تنعيم أو استيفاء أو تلاعب أو تقلب", "تنعيم أو استيفاء أو تقلب")
    S.replace("P3-F09", A, 82, 7, "smoothing, manipulation or real-world stability", "smoothing or real-world stability", "DA method boundary")
    S.replace_section("P3-F09", "/evidence/CLM-034/", 1, "en", "body", "smoothing, interpolation, manipulation or low", "smoothing, interpolation or low")
    S.replace_section("P3-F09", "/evidence/CLM-034/", 1, "ar", "body", "تسوية أو استيفاء أو تلاعب أو انخفاض", "تسوية أو استيفاء أو انخفاض")
    S.replace_section("P3-F09", "/remittances/", 3, "en", "body", "smoothing, interpolation or manipulation.", "smoothing or interpolation.")
    S.replace_section("P3-F09", "/remittances/", 3, "ar", "body", "التسوية أو الاستيفاء أو التلاعب.", "التسوية أو الاستيفاء.")

    # P3-F10 Provider entity dates stored as untyped Excel serials (General format) — written as the ISO dates they encode
    # (the same dates are governed as text in the provider-universe block: PUC-BANK-2026-01 reference_state 2026-09-07).
    g22 = S.grid("22_PROVIDERS_DATA")
    base = datetime.date(1899, 12, 30)
    m = 0
    for i, r in enumerate(g22, 1):
        if 5 <= i <= 60 and len(r) > 7 and isinstance(r[7], (int, float)) and not isinstance(r[7], bool) and r[0] and str(r[0]).startswith("PRV-"):
            iso = (base + datetime.timedelta(days=int(r[7]))).isoformat()
            if iso not in ("2026-09-07", "2026-09-17"):
                raise TxError(f"P3-F10 unexpected serial {r[7]} at r{i}")
            S.set("P3-F10", "22_PROVIDERS_DATA", i, 8, iso, S.ed.get_value("22_PROVIDERS_DATA", i, 8), f"{r[0]}.current_state_as_of")
            m += 1
    if m == 0:
        raise TxError("P3-F10 no serial dates found")

    changed = S.regenerate_full_copy()
    rep = S.save(out, ledger, [("transaction", "P3-A"), ("scope", "P3 visual-contract truth corrections (Master-first)"),
                               ("full_copy_regenerated", changed), ("provider_dates_fixed", m)])
    print(f"P3-A staged: {rep['cells_written']} cells; full copy {len(changed)}; provider dates {m}; Master {rep['output_master_sha256']}")


if __name__ == "__main__":
    main()
