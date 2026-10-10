# -*- coding: utf-8 -*-
"""Public naming and terminology, transaction NB-2: the fixes from the independent review of NB-1.

  python3 nb_2_review_fixes.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

An independent reviewer who did not build NB-1 read every changed cell, the built pages in both languages and the
/rights/ text (10 October 2026). No blocker; these are its should-fix items and the nits accepted by the lead. Labels
and governed wording only; no figure, unit, period, universe, source, route or identifier changes.
"""
import json, os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "release_candidate"))
from rc_lib import Session, TxError, set_ui, ui_block_end  # noqa: E402

F = "NB-2:REVIEW"
S04 = "04_NAV_UX"

UI = [
    # R1: the Arabic footer licence line — CauseWay is feminine (as in the strapline and on /rights/), and the
    # possessives attach to CauseWay, not to «نص»
    ("UI-FOOTER-LICENCE", None, None,
     "يُتاح نص CauseWay الخاص وتحليلاته وتصاميمه المرئية بموجب رخصة {licence} ما لم يُذكر خلاف ذلك، وتبقى مواد الجهات الأخرى خاضعة لشروط أصحابها.",
     "تُتاح نصوص CauseWay وتحليلاتها وتصاميمها المرئية بموجب رخصة {licence} ما لم يُذكر خلاف ذلك، وتبقى مواد الجهات الأخرى خاضعة لشروط أصحابها."),
    # R11: «لا يُستنتج» reads as "cannot be inferred"; the English is an instruction
    ("UI-DOM-DO-NOT-INFER", None, None, "لا يُستنتج:", "لا تستنتج:"),
]

# (sheet, row, column, old substring, new substring) — each old substring must occur exactly once in its cell
SUBS = [
    # R2: grammar after NB-1 made the subject plural
    ("03_PAGE_SECTIONS", 136, 5, "It does not rank national priorities", "They do not rank national priorities"),
    # R3: the /measurement/ section rubric and the priority rationale still said "agenda"
    ("03_PAGE_SECTIONS", 153, 3, "Measurement agenda", "Measurement priorities"),
    ("03_PAGE_SECTIONS", 137, 5, "this resource’s evidence agenda", "this resource’s measurement priorities"),
    # R4: /ar/terms/ names the rights page by its new name
    ("03_PAGE_SECTIONS", 337, 7, "«الحقوق وإعادة الاستخدام»", "«حقوق إعادة الاستخدام»"),
    # R5: CLM-035 keeps the bank's own label «التحويلات» (NB-1 ruling); its meta description follows the record
    ("02_SITE_MAP", 45, 8, "نسبة الحوالات إلى تمويل المانحين", "نسبة التحويلات إلى تمويل المانحين"),
    # R7: the Findex citation in the form the source record's attribution requirement gives
    ("03_PAGE_SECTIONS", 363, 5,
     "Demirgüç-Kunt, Klapper, Singer and Ansar, The Global Findex Database 2021: Financial Inclusion, Digital Payments, and Resilience in the Age of COVID-19, World Bank.",
     "Demirgüç-Kunt, Klapper, Singer and Ansar (2022), The Global Findex Database 2021: Financial Inclusion, Digital Payments, and Resilience in the Age of COVID-19, Washington, DC: World Bank."),
    ("03_PAGE_SECTIONS", 363, 7,
     "Demirgüç-Kunt وKlapper وSinger وAnsar، The Global Findex Database 2021: Financial Inclusion, Digital Payments, and Resilience in the Age of COVID-19، البنك الدولي.",
     "Demirgüç-Kunt وKlapper وSinger وAnsar (2022)، The Global Findex Database 2021: Financial Inclusion, Digital Payments, and Resilience in the Age of COVID-19، واشنطن العاصمة: البنك الدولي."),
    # R9: now that «الحوالات» means remittances, the informal hawala system is named as a system
    ("03_PAGE_SECTIONS", 315, 7, "سلسلة التحويلات الكلية لا تقيس حجم الحوالة غير الرسمية",
     "سلسلة الحوالات الكلية لا تقيس حجم التحويلات عبر نظام الحوالة غير الرسمي"),
    ("03_PAGE_SECTIONS", 327, 7, "حجمَ الحوالة غير الرسمية", "حجمَ التحويلات عبر نظام الحوالة غير الرسمي"),
    ("06_EVIDENCE_OBJECTS", 29, 17, "لا يقيس هذا الدليل حجم الحوالة غير الرسمية",
     "لا يقيس هذا الدليل حجم التحويلات عبر نظام الحوالة غير الرسمي"),
    ("06_EVIDENCE_OBJECTS", 29, 17, "ولا قياسًا مباشرًا لحجم الحوالة غير الرسمية",
     "ولا قياسًا مباشرًا لحجم التحويلات عبر نظام الحوالة غير الرسمي"),
    # R10: two substitutions whose English does not say "remittance"
    (S04, None, 6, "والحوالات داخل اليمن", "والأموال المحوَّلة داخل اليمن"),          # SEARCH-ALIAS-032 boundary note
    ("06_EVIDENCE_OBJECTS", 104, 13, "أو حوالات الأسر المستلمة", "أو ما تتسلمه الأسر من حوالات"),
    # R12: missing ≠ zero in body text (TERM-021)
    ("06_EVIDENCE_OBJECTS", 54, 7, "فهي غير متاحة وليست صفرًا.", "فهي غير متاحة، وهذا لا يعني صفرًا."),
    ("06_EVIDENCE_OBJECTS", 77, 7, "ليس صفرًا وليس دليلًا على عدم الوجود", "لا يعني صفرًا ولا يدل على عدم الوجود"),
    ("06_EVIDENCE_OBJECTS", 77, 17, "الفجوة ليست صفرًا وليست دليلًا على الغياب أو الفشل", "الفجوة لا تعني صفرًا، ولا تدل على الغياب أو الفشل"),
    ("11_VISUAL_LIBRARY", 8, 22, "ليس صفرًا وليس دليلًا على عدم الوجود", "لا يعني صفرًا ولا يدل على عدم الوجود"),
    ("11_VISUAL_LIBRARY", 8, 20, "الفجوة ليست صفرًا وليست دليلًا على الغياب أو الفشل", "الفجوة لا تعني صفرًا، ولا تدل على الغياب أو الفشل"),
    ("11_VISUAL_LIBRARY", 29, 22, "غير معروفة وليست صفرًا،", "غير معروفة، وهذا لا يعني صفرًا،"),
    # R13: the new Arabic h1 prefixes no longer repeat the domain name
    ("02_SITE_MAP", 6, 6, "نعرف أجزاءً من شبكة الوصول إلى الخدمات المالية", "نعرف أجزاءً من شبكة الخدمات المالية"),
    ("02_SITE_MAP", 129, 6, "قائمة مقدمي الخدمات تثبت وضعًا رسميًا", "تثبت القوائم الرسمية وضعًا رسميًا"),
    # R16: the rights page is called by the name its link carries
    ("02_SITE_MAP", 143, 5, "Source and data rights", "Rights and reuse"),
    ("02_SITE_MAP", 143, 6, "حقوق المصادر والبيانات", "حقوق إعادة الاستخدام"),
]

# R3 (nit): the priority rationale of each measurement priority (10, column V) said "within this evidence agenda"
AGENDA_ROWS = range(5, 15)

# R6: the register's remittance rule, narrowed to what was applied
TERM_001_RULE = (
    "When naming a source's own balance-of-payments line or indicator, quote its label (for example CBY-Aden «التحويلات»; "
    "World Bank 'Personal remittances, received', «التحويلات الشخصية الواردة»); in running text, remittances = الحوالات.",
    "عند تسمية بند ميزان المدفوعات أو المؤشر كما يسمّيه المصدر يُنقل اسمه كما ورد (مثل «التحويلات» لدى البنك المركزي اليمني – عدن، "
    "و«التحويلات الشخصية الواردة» لدى البنك الدولي)؛ وفي النص الجاري: الحوالات.")
TERM_001_OLD = (
    "In balance-of-payments text keep the source's own concept (personal remittances, workers' remittances) and present it as the source's label.",
    "في نصوص ميزان المدفوعات يُحتفظ بمفهوم المصدر نفسه (التحويلات الشخصية، تحويلات العاملين، تحويلات المغتربين) ويُقدَّم بوصفه تسمية المصدر.")


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    for ui_id, oe, ne, oa, na in UI:
        set_ui(s, F, ui_id, ne, na, oe, oa)
    g04 = s.grid(S04)
    alias = {x[0]: i for i, x in enumerate(g04, 1) if x and isinstance(x[0], str) and x[0].startswith("SEARCH-ALIAS-")}
    term = {x[0]: i for i, x in enumerate(g04, 1) if x and isinstance(x[0], str) and x[0].startswith("TERM-")}
    for sheet, row, c, old, new in SUBS:
        row = row or alias["SEARCH-ALIAS-032"]
        s.replace(F, sheet, row, c, old, new, f"{sheet}!r{row}c{c}")
    for r in AGENDA_ROWS:
        s.replace(F, "10_MEASUREMENT_AGENDA", r, 22, " within this evidence agenda ", " among these measurement priorities ",
                  f"10!r{r}.priority_rationale")
    # R14: the alias row pairs its terms across the languages
    r44 = alias["SEARCH-ALIAS-044"]
    s.replace(F, S04, r44, 2, "migrant remittances", "migrant remittances; remittance fees", "SEARCH-ALIAS-044.terms_en")
    s.set(F, S04, term["TERM-001"], 7, TERM_001_RULE[0], TERM_001_OLD[0], "TERM-001.rule_en")
    s.set(F, S04, term["TERM-001"], 8, TERM_001_RULE[1], TERM_001_OLD[1], "TERM-001.rule_ar")
    rep = s.save(out, ledger, OrderedDict([
        ("transaction", "NB-2"),
        ("summary", "Fixes from the independent review of NB-1: Arabic licence line, three missed labels, CLM-035 description, the "
                    "Findex citation, hawala wording, missing-is-not-zero wording, h1 prefixes, the rights title, the register rule"),
    ]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
