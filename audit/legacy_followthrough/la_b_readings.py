# -*- coding: utf-8 -*-
"""Legacy-audit follow-through, transaction LA-B: strengthen four existing Readings. No new objects. EN and AR together.

  python3 la_b_readings.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Owner brief "Legacy-audit follow-through" of 10 October 2026, transaction B, with the owner's corrections of the same day.
Every number below was read in the original by this session on 10 October 2026, and each is bound to a record the
Reading already cites (or that this transaction binds to it), with its locator in value_states:

CWR-003  a target inherits every property of its baseline; the five declarations (unit, universe, date, instrument,
         definition of "active"); the results-framework baseline of 10,761 *matches* the 10,761 wallets of PAD ¶14 (an
         inference from the same number in the same document, not a stated link): PAD (Report No. PADHI00396, 22 May
         2025) results framework, printed p. 23 (PDF p. 33), and ¶14, printed p. 4 (PDF p. 14); the alternative: the
         sub-component 3-1 GIS database includes money exchangers (¶30, printed p. 10, PDF p. 20). Bound through
         FMIIP-BASELINE-2025-01, now also bound to CWR-003.
CWR-002  across the 2022 revaluation, CBY-Aden "Monetary and Financial Developments", Issue No. 54 (May 2026), Table 4
         (printed p. 15): private-sector credit 338.0 -> 1,301.6, foreign assets 904.5 -> 2,669.0, loans to government
         1,926.8 -> 1,913.2 (YER billion; December 2022 at the old rate and "Based on market exchange rates"); consistent
         with valuing foreign-currency items, not new lending; still no headline restatement percentage. Bound through
         CLM-033 (SRC-CBY-001 added to its sources).
CWR-007  concordance: Findex 2022 women 5.4% (weighted; CLM-002); Findex 2014 women 1.7% (Little Data Book on Financial
         Inclusion 2015, Yemen page, printed p. 160, PDF p. 170 — the brief's p. 159 is West Bank and Gaza); the PAD's
         undated, unsourced "two percent holding a bank account" (¶9, printed p. 2) is bound as a record of what the PAD
         says and is not used as a measurement. No cause added. Bound through CLM-027, now also bound to CWR-007.
CWR-010  PAD ¶14 (printed p. 4): 10,761 wallets opened, with cash transfers paid into them, by the end of payment cycle 18
         (16 September – 17 October 2024); take-up 40% to 70% across pilot districts; no ratio against 45,460 —
         different documents, dates and units, and the PAD does not say it is the same pilot. Bound through CLM-045 (the PAD source added).
"""
import json, os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "tranche_c"))
from tc_lib import Session, Table, TxError  # noqa: E402

S03 = "03_PAGE_SECTIONS"
PAD = "SRC-WB-FMIIP-P180708"
CBY = "SRC-CBY-001"
LDB = "SRC-WB-FINDEX-LDB-2015-001"
PADLOC = "PAD (Report No. PADHI00396, 22 May 2025)"
CBYLOC = "CBY-Aden, Monetary and Financial Developments, Issue No. 54 (May 2026), Table 4 \"Consolidated Balance Sheet of Commercial & Islamic Banks - Assets\", printed p. 15 (PDF p. 16), YER billion"


def tset(t, finding, key, field, old_sub, new_sub):
    cur = t.get(key, field)
    if not isinstance(cur, str) or cur.count(old_sub) != 1:
        raise TxError(f"{finding}: {t.sheet} {key}.{field}: {old_sub[:60]!r} occurs {0 if not isinstance(cur, str) else cur.count(old_sub)} times")
    t.set(finding, key, field, cur.replace(old_sub, new_sub), cur)


def append(t, finding, key, field, must_end, add):
    cur = t.get(key, field)
    if not isinstance(cur, str) or not cur.rstrip().endswith(must_end):
        raise TxError(f"{finding}: {t.sheet} {key}.{field} does not end with {must_end[-40:]!r}")
    t.set(finding, key, field, cur.rstrip() + add, cur)


def add_values(t, finding, key, entries):
    cur = t.get(key, "value_states")
    vs = json.loads(cur or "[]")
    have = {v.get("t") for v in vs}
    for e in entries:
        if e["t"] in have:
            raise TxError(f"{finding}: {key} already carries {e['t']!r}")
        vs.append(e)
    t.set(finding, key, "value_states", json.dumps(vs, ensure_ascii=False, separators=(",", ":")), cur)


def bind_reading(t08, finding, rid, oid):
    for field in ("claim_bindings", "evidence_bindings"):
        cur = t08.get(rid, field)
        ids = json.loads(cur)
        if oid in ids:
            raise TxError(f"{finding}: {rid}.{field} already binds {oid}")
        t08.set(finding, rid, field, json.dumps(ids + [oid], separators=(",", ":")), cur)
    cur = t08.get(rid, "verification_bindings")
    vb = json.loads(cur, object_pairs_hook=OrderedDict)
    vb["claim_ids"] = vb["claim_ids"] + [oid]
    t08.set(finding, rid, "verification_bindings", json.dumps(vb, ensure_ascii=False), cur)


def sect(s, finding, route, order, lang, old_sub, new_sub):
    s.replace_section(finding, route, order, lang, "body", old_sub, new_sub)


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    t06, t08 = Table(s, "06_EVIDENCE_OBJECTS"), Table(s, "08_READINGS")
    D14 = [{"t": "October 2024", "k": "d", "s": "READ", "src": PAD, "loc": PADLOC + ", paragraph 14"},
           {"t": "September 2024", "k": "d", "s": "READ", "src": PAD, "loc": PADLOC + ", paragraph 14"},
           {"t": "16 September 2024", "k": "d", "s": "READ", "src": PAD, "loc": PADLOC + ", paragraph 14: from September 16 to October 17, 2024"},
           {"t": "17 October 2024", "k": "d", "s": "READ", "src": PAD, "loc": PADLOC + ", paragraph 14: from September 16 to October 17, 2024"}]

    # ------------------------------------------------------------------------------------------------- CWR-003
    F = "LA-B:CWR-003"
    tset(t08, F, "CWR-003", "thesis_en", "and a target or a trend is only as sound as the unit it keeps.",
         "and a target inherits every property of its baseline: its unit, its universe, its date, its instrument and its definition of “active”.")
    tset(t08, F, "CWR-003", "thesis_ar", "ولا يكون المستهدف أو الاتجاه سليمًا إلا بقدر ثبات الوحدة التي يقيسها.",
         "والمستهدف يرث كل خصائص خط أساسه: وحدته، والمجتمع الذي ينطبق عليه، وتاريخه، وأداة قياسه، وتعريفه لما هو «نشط».")
    url = "/readings/define-what-you-count/"
    sect(s, F, url, 5, "en", "A bounded measure is not weak because its universe is narrow; it becomes misleading when that universe disappears from view.",
         "A bounded measure is not weak because its universe is narrow; it becomes misleading when that universe disappears from view.\n"
         "The same results framework shows how a baseline can carry a unit from elsewhere. Its January 2025 baseline of 10,761 "
         "beneficiaries who received or made payments through electronic channels matches the 10,761 wallets that the appraisal document "
         "reports were opened, with cash transfers paid into them, in a pilot, by the end of payment cycle 18 (16 September–17 October 2024). "
         "That the two are one count is an inference from the same number in the same document, which does not state the link. If it "
         "holds, the baseline counts e-wallets in one pilot, while the indicator names beneficiaries.\n"
         "The project’s own design points to a broader measure of access: the geographic database planned under its access-and-use "
         "component is to map bank branches, ATMs, POS terminals, merchants that accept QR-code payments and money exchangers, a category "
         "the access-point definition does not name.")
    sect(s, F, url, 5, "ar", "ضيق نطاق المقياس لا يجعله ضعيفًا؛ ما يجعله مضللًا أن يغيب هذا النطاق عن العرض.",
         "ضيق نطاق المقياس لا يجعله ضعيفًا؛ ما يجعله مضللًا أن يغيب هذا النطاق عن العرض.\n"
         "ويبيّن إطار النتائج نفسه كيف يمكن أن يحمل خط الأساس وحدةً من مصدر آخر: فخط أساسه في يناير 2025 البالغ 10,761 مستفيدًا "
         "تلقوا مدفوعات أو أجروها عبر قنوات إلكترونية يطابق 10,761 محفظة إلكترونية تذكر وثيقة التقييم أنها فُتحت وأُودعت فيها تحويلات "
         "نقدية، في إطار تجربة، بنهاية دورة الدفع 18 (16 سبتمبر–17 أكتوبر 2024). والقول إنهما عدّ واحد استنتاجٌ من تطابق الرقم في "
         "الوثيقة نفسها، إذ لا تذكر الوثيقة صلةً بينهما. فإن صحّ ذلك، فإن خط الأساس يعدّ محافظَ إلكترونية في تجربة واحدة، في حين "
         "يسمّي المؤشر مستفيدين.\n"
         "ويشير تصميم المشروع نفسه إلى مقياس أوسع للوصول: فقاعدة البيانات الجغرافية المزمعة ضمن مكوّن الوصول والاستخدام سترصد مواقع "
         "فروع البنوك وأجهزة الصراف الآلي وأجهزة نقاط البيع والتجار الذين يقبلون الدفع برمز الاستجابة السريعة وشركات ومنشآت الصرافة، "
         "وهي فئة لا يذكرها تعريف نقاط الوصول المالي.")
    sect(s, F, url, 6, "en",
         "Before accepting any baseline, target or claim of progress, ask:\n- What exactly is being counted?\n- Among whom does the number apply?\n"
         "- What makes the unit active, or included?\n- Are the baseline and the result measured under the same definition?\n"
         "- What does the measure still not tell us?",
         "A target inherits every property of its baseline. Before relying on any target, declare five things:\n"
         "- Unit: what exactly is counted — people, accounts, wallets, terminals or transactions?\n"
         "- Universe: among whom, and where, does the number apply?\n"
         "- Date: when was the baseline observed, when was the target set, and for when?\n"
         "- Instrument: a survey, an administrative report or project monitoring?\n"
         "- Activity: what makes the unit “active”, and over what period?\n"
         "If any of the five differs between the baseline and the result, the result does not measure progress against the target.")
    sect(s, F, url, 6, "ar",
         "وقبل قبول أي خط أساس أو مستهدف أو ادعاء بالتقدم، اسأل:\n- ما الذي يُعدّ بالضبط؟\n- على من ينطبق الرقم؟\n"
         "- ما الذي يجعل الوحدة نشطة أو مشمولة؟\n- هل قيس خط الأساس والنتيجة بالتعريف نفسه؟\n- ما الذي لا يخبرنا به المقياس بعد؟",
         "المستهدف يرث كل خصائص خط أساسه. وقبل الاعتماد على أي مستهدف، صرّح بخمسة أمور:\n"
         "- الوحدة: ما الذي يُعدّ بالضبط — أشخاص أم حسابات أم محافظ إلكترونية أم أجهزة أم معاملات؟\n"
         "- المجتمع: على من ينطبق الرقم، وأين؟\n"
         "- التاريخ: متى رُصد خط الأساس ومتى حُدّد المستهدف، ولأي تاريخ؟\n"
         "- الأداة: مسح أم تقرير إداري أم متابعة مشروع؟\n"
         "- النشاط: ما الذي يجعل الوحدة «نشطة»، وخلال أي فترة؟\n"
         "فإذا اختلف أيٌّ من هذه الخمسة بين خط الأساس والنتيجة، فالنتيجة لا تقيس التقدم نحو المستهدف.")
    append(t06, F, "FMIIP-BASELINE-2025-01", "definition_en", "not an independent measurement of the financial system.",
           " The framework also sets a January 2025 baseline of 10,761 for its development-objective indicator, beneficiaries who received "
           "or made payments through electronic channels; the same document reports 10,761 wallets opened, with cash transfers paid into "
           "them, in a pilot, by the end of payment cycle 18 (16 September–17 October 2024), and does not state whether the two are the same count.")
    cur_ar = t06.get("FMIIP-BASELINE-2025-01", "definition_ar")
    t06.set(F, "FMIIP-BASELINE-2025-01", "definition_ar", cur_ar.rstrip() +
            " ويحدد الإطار كذلك خط أساس في يناير 2025 قدره 10,761 لمؤشر الهدف الإنمائي للمشروع، أي المستفيدين الذين تلقوا مدفوعات أو "
            "أجروها عبر قنوات إلكترونية؛ وتذكر الوثيقة نفسها أن 10,761 محفظة إلكترونية فُتحت وأُودعت فيها تحويلات نقدية، في إطار تجربة، "
            "بنهاية دورة الدفع 18 (16 سبتمبر–17 أكتوبر 2024)، ولا تذكر ما إذا كان الرقمان عدًّا واحدًا.", cur_ar)
    add_values(t06, F, "FMIIP-BASELINE-2025-01", [
        {"t": "10,761", "k": "v", "s": "READ", "src": PAD,
         "loc": PADLOC + ", Annex 1 results framework, printed p. 23 (PDF p. 33): PDO indicator baseline Jan/2025 10,761; and paragraph 14, printed p. 4 (PDF p. 14): \"10,761 wallets had been opened with cash transfers rendered into them\"; read 10 October 2026"},
        {"t": "18", "k": "v", "s": "READ", "src": PAD, "loc": PADLOC + ", paragraph 14, printed p. 4: \"By the end of the payment cycle 18\""}] + D14)
    bind_reading(t08, F, "CWR-003", "FMIIP-BASELINE-2025-01")

    # ------------------------------------------------------------------------------------------------- CWR-002
    F = "LA-B:CWR-002"
    url = "/readings/banking-jump-measurement-basis/"
    sect(s, F, url, 3, "en", "so that decomposition remains open.",
         "so that decomposition remains open.\n"
         "The central bank’s own monthly bulletin shows the shape of the break. The consolidated balance sheet of commercial and Islamic "
         "banks in the bulletin prints December 2022 twice, on the earlier basis and at market exchange rates: private-sector credit 338.0 "
         "and 1,301.6 billion rials and foreign assets 904.5 and 2,669.0 billion, while loans and advances to government — treasury bills, "
         "bonds and sukuk, in the bulletin’s definition — stayed almost unchanged at 1,926.8 and 1,913.2 billion. That pattern is "
         "consistent with revaluing foreign-currency items, not with new lending; the bulletin does not split any line between valuation "
         "and other effects.")
    sect(s, F, url, 3, "ar", "ولذلك يبقى هذا التفكيك مفتوحًا.",
         "ولذلك يبقى هذا التفكيك مفتوحًا.\n"
         "وتُظهر النشرة الشهرية للبنك المركزي نفسه شكل الانقطاع: فالميزانية المجمعة للبنوك التجارية والإسلامية في النشرة تعرض ديسمبر "
         "2022 مرتين، على الأساس السابق وبسعر الصرف السوقي: الائتمان الممنوح للقطاع الخاص 338.0 و1,301.6 مليار ريال، والأصول الخارجية "
         "904.5 و2,669.0 مليار، أما القروض والسلفيات للحكومة — وهي وفق تعريف النشرة أذون الخزانة والسندات والصكوك — فبقيت شبه ثابتة: "
         "1,926.8 و1,913.2 مليار. وهذا النمط يتسق مع إعادة تقييم البنود المقوّمة بالعملات الأجنبية، لا مع إقراض جديد؛ ولا تفصل النشرة "
         "أي بند بين أثر التقييم والآثار الأخرى.")
    append(t06, F, "CLM-033", "method_en", "at the market exchange rate.",
           " The monthly bulletin Monetary and Financial Developments (Issue No. 54, May 2026, Table 4) prints December 2022 twice for "
           "commercial and Islamic banks, on the earlier basis and at market exchange rates: private-sector credit 338.0 and 1,301.6, foreign "
           "assets 904.5 and 2,669.0, and loans and advances to government 1,926.8 and 1,913.2 (billion rials).")
    append(t06, F, "CLM-033", "method_ar", "بسعر الصرف السوقي.",
           " وتعرض النشرة الشهرية «التطورات النقدية والمالية» (العدد رقم 54، مايو 2026، الجدول 4) ديسمبر 2022 مرتين للبنوك التجارية "
           "والإسلامية، على الأساس السابق وبسعر الصرف السوقي: الائتمان الممنوح للقطاع الخاص 338.0 و1,301.6، والأصول الخارجية 904.5 "
           "و2,669.0، والقروض والسلفيات للحكومة 1,926.8 و1,913.2 (مليار ريال).")
    tset(t06, F, "CLM-033", "source_dependencies", "SRC-CBY-AR2023-001; ", "SRC-CBY-AR2023-001; " + CBY + "; ")
    add_values(t06, F, "CLM-033", [
        {"t": v, "k": "v", "s": "READ", "src": CBY, "loc": CBYLOC + f", {lab}; read 10 October 2026"}
        for v, lab in (("338.0", "Loans & Advances: Private Sector, Dec 2022"), ("1,301.6", "Loans & Advances: Private Sector, Dec *2022 (*Based on market exchange rates)"),
                       ("904.5", "Foreign Assets, Dec 2022"), ("2,669.0", "Foreign Assets, Dec *2022 (*Based on market exchange rates)"),
                       ("1,926.8", "Loans & Advances: Government, Dec 2022"), ("1,913.2", "Loans & Advances: Government, Dec *2022 (*Based on market exchange rates)"))] + [
        {"t": "4", "k": "v", "s": "TRIVIAL"},
        {"t": "54", "k": "v", "s": "TRIVIAL"},
        {"t": "May 2026", "k": "d", "s": "READ", "src": CBY, "loc": CBYLOC},
        {"t": "December 2022", "k": "d", "s": "READ", "src": CBY, "loc": CBYLOC}])

    # ------------------------------------------------------------------------------------------------- CWR-007
    F = "LA-B:CWR-007"
    url = "/readings/gender-gap-measured-causes-open/"
    sect(s, F, url, 2, "en", "towards the conditions under which access is produced.",
         "towards the conditions under which access is produced.\n"
         "Three figures for women’s account ownership circulate, and only two of them are measurements. The 2021 Findex wave (Yemen "
         "fieldwork 2022–23) measured 5.4% of women aged 15 and over with an account, a weighted survey estimate for the areas surveyed; "
         "the 2014 wave measured 1.7% (World Bank, Little Data Book on Financial Inclusion 2015). The appraisal document of the World "
         "Bank-financed FMIIP project says that “two percent” of women hold a bank account, with no date and no source, so it is not used "
         "here as a measurement. The two measurements come from different waves and are not joined into a trend here, and neither "
         "explains the gap.")
    sect(s, F, url, 2, "ar", "إلى الظروف التي يتشكل فيها الوصول.",
         "إلى الظروف التي يتشكل فيها الوصول.\n"
         "تُتداوَل ثلاثة أرقام لنسبة النساء اللواتي يملكن حسابًا، اثنان منها فقط قياسان. فقد قدّرت موجة 2021 من المؤشر العالمي للشمول "
         "المالي (Findex)، التي نُفذ عملها الميداني في اليمن خلال 2022–2023، أن 5.4% من النساء بعمر 15 سنة فأكثر يملكن حسابًا، وهو تقدير "
         "مسحي مرجّح للمناطق التي شملها المسح؛ وقدّرت موجة 2014 النسبة بـ1.7% (البنك الدولي، Little Data Book on Financial Inclusion 2015). "
         "أما وثيقة تقييم مشروع FMIIP الممول من البنك الدولي فتذكر أن «اثنين في المئة» من النساء يملكن حسابًا مصرفيًا، من دون تاريخ ولا "
         "مصدر، ولذلك لا يُستخدم هنا قياسًا. والقياسان من موجتين مختلفتين، ولا يُربط بينهما هنا لاستخلاص اتجاه، ولا يفسر أيٌّ منهما الفجوة.")
    tset(t06, F, "CLM-027", "limitations_en", "that excluded areas holding about 23% of the population.",
         "that excluded areas holding about 23% of the population. For women, the 2014 wave records 1.7%; the waves are not joined into a "
         "trend. The FMIIP appraisal document (May 2025) says that “two percent” of women hold a bank account, with no date and no source; "
         "that is a statement, not a measurement.")
    tset(t06, F, "CLM-027", "limitations_ar", "واستبعد مناطق يقطنها نحو 23% من السكان.",
         "واستبعد مناطق يقطنها نحو 23% من السكان. وتسجل موجة 2014 للنساء نسبة 1.7%، ولا يُربط بين الموجتين في اتجاه. وتذكر وثيقة تقييم "
         "مشروع FMIIP (مايو 2025) أن «اثنين في المئة» من النساء يملكن حسابًا مصرفيًا، من دون تاريخ ولا مصدر؛ وهذا تصريح لا قياس.")
    tset(t06, F, "CLM-027", "source_dependencies", "SRC-WB-FINDEX-001", "SRC-WB-FINDEX-001; " + PAD)
    add_values(t06, F, "CLM-027", [
        {"t": "1.7%", "k": "v", "s": "READ", "src": LDB,
         "loc": "Little Data Book on Financial Inclusion 2015, Yemen, Rep. country page, printed p. 160 (PDF p. 170), Account (% age 15+), Women = 1.7; read 10 October 2026"},
        {"t": "two percent", "k": "v", "s": "READ", "src": PAD,
         "loc": PADLOC + ", paragraph 9, printed p. 2 (PDF p. 12): \"with just two percent holding a bank account\" — no year, no footnote; read 10 October 2026"},
        {"t": "May 2025", "k": "d", "s": "READ", "src": PAD, "loc": PADLOC + ", date of the appraisal document"}])
    bind_reading(t08, F, "CWR-007", "CLM-027")

    # ------------------------------------------------------------------------------------------------- CWR-010
    F = "LA-B:CWR-010"
    url = "/readings/after-transfer-persistence/"
    sect(s, F, url, 6, "en", "The 45,460 figure counts recipients reported by the programme, not people who kept using an account.",
         "The 45,460 figure counts recipients reported by the programme, not people who kept using an account.\n"
         "The appraisal document of the World Bank-financed FMIIP project (May 2025) reports a separate count from a pilot, without saying "
         "whether it is the pilot described above: by the end of payment cycle 18 (16 September–17 October 2024), 10,761 wallets had been "
         "opened with cash transfers paid into them, and take-up ranged from 40% to 70% across pilot districts. The two documents differ in "
         "date and unit, and may not describe the same pilot — recipients reported in May 2024, wallets opened by October 2024 — so no "
         "ratio between 10,761 and 45,460 is published or implied.")
    sect(s, F, url, 6, "ar", "لا الأشخاص الذين واصلوا استخدام حساب.",
         "لا الأشخاص الذين واصلوا استخدام حساب.\n"
         "وتورد وثيقة تقييم مشروع FMIIP الممول من البنك الدولي (مايو 2025) عدًّا منفصلًا من تجربة، من دون أن تذكر ما إذا كانت هي "
         "التجربة المذكورة أعلاه: فبنهاية دورة الدفع 18 (16 سبتمبر–17 أكتوبر 2024) كانت 10,761 محفظة إلكترونية قد فُتحت وأُودعت فيها "
         "تحويلات نقدية، وتراوحت نسبة الإقبال بين 40% و70% في مديريات التجربة. ويختلف المصدران في التاريخ والوحدة، وقد لا يتناولان "
         "التجربة نفسها — مستفيدون أُبلغ عنهم في مايو 2024، ومحافظ إلكترونية فُتحت بحلول أكتوبر 2024 — لذلك لا تُنشر أي نسبة بين 10,761 "
         "و45,460، صراحةً أو ضمنًا.")
    tset(t06, F, "CLM-045", "limitations_en", "not a count of people who kept using an account.",
         "not a count of people who kept using an account. The FMIIP appraisal document (May 2025) reports, for a pilot it does not identify "
         "with this one, that by the end of payment cycle 18 (16 September–17 October 2024) 10,761 wallets had been opened with cash "
         "transfers paid into them, with take-up of 40% to 70% across pilot districts; it differs in document, date and unit, and no ratio "
         "to 45,460 is drawn.")
    tset(t06, F, "CLM-045", "limitations_ar", "وليس عددًا لمن واصلوا استخدام حساب.",
         "وليس عددًا لمن واصلوا استخدام حساب. وتذكر وثيقة تقييم مشروع FMIIP (مايو 2025)، عن تجربة لا تحدد ما إذا كانت هي هذه التجربة نفسها، أن "
         "10,761 محفظة إلكترونية فُتحت وأُودعت فيها تحويلات نقدية بنهاية دورة الدفع 18 (16 سبتمبر–17 أكتوبر 2024)، وأن نسبة الإقبال "
         "تراوحت بين 40% و70% في مديريات التجربة؛ وهي تختلف عنه في الوثيقة والتاريخ والوحدة، ولا تُحسب منها نسبة إلى 45,460.")
    tset(t06, F, "CLM-045", "source_dependencies", "SRC-WB-G2PX-YEM-UCT-2024-001; ", "SRC-WB-G2PX-YEM-UCT-2024-001; " + PAD + "; ")
    add_values(t06, F, "CLM-045", [
        {"t": "10,761", "k": "v", "s": "READ", "src": PAD, "loc": PADLOC + ", paragraph 14, printed p. 4 (PDF p. 14): \"10,761 wallets had been opened with cash transfers rendered into them\"; read 10 October 2026"},
        {"t": "18", "k": "v", "s": "READ", "src": PAD, "loc": PADLOC + ", paragraph 14: \"payment cycle 18\""},
        {"t": "40%", "k": "v", "s": "READ", "src": PAD, "loc": PADLOC + ", paragraph 14: \"take-up rates ranged from 40 to 70 percent\""},
        {"t": "70%", "k": "v", "s": "READ", "src": PAD, "loc": PADLOC + ", paragraph 14: \"take-up rates ranged from 40 to 70 percent\""},
        {"t": "May 2025", "k": "d", "s": "READ", "src": PAD, "loc": PADLOC + ", date of the appraisal document"}] + D14)

    r = s.save(out, ledger, OrderedDict([("transaction", "LA-B"),
                                         ("summary", "Legacy-audit follow-through B: CWR-003, CWR-002, CWR-007 and CWR-010 strengthened; every new number bound")]))
    print(json.dumps({k: r[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
