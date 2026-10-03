# -*- coding: utf-8 -*-
"""Release-candidate transaction RC-18: the owner's note of 3 October 2026, about 11:15 Cairo, sections 4.1 and 4.2
(audit/OWNER_DECISIONS_2026-10-02.md). English and Arabic change together. The code half (the figure set in its
sentence, the record head's FOR WHOM, the dimensions on /measurement/, the drawn chain beside Home's section 6) ships in
the same commit.

  python3 rc_18_figure_first.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

4.1, figure first, inside the accepted D7 design. D7's Design Intent Lock forbids lifted figures and stat tiles ("a
number is never typeset outside its governed sentence or its bounded object") and keeps Home's product statement first
(DL-D3-002: cold readers reached the third screen before learning what the product is). So the figure comes first
where D7 allows it:
- Home's product statement (section 1) is two sentences instead of five. What it drops is said elsewhere: that the
  resource makes no decisions for users is on /about/; that the evidence spans many dates and definitions is Home's
  headline and section 5; the closing instruction is the action that follows.
- The first figure group (section 3) opens with its figure: "11.9% of adults aged 15 and over …", then whose survey,
  when, and the coverage sentence that follows unchanged. Same numbers, same order of the other two groups.
4.2:
- /corrections/ invites source institutions, in the owner's words, with "the same route" named: write to
  office@causewaygrp.com with the record or source reference (the address /about/ already gives).
- Three search aliases for the words citizens type that landed wrong or nowhere (checked with the validator's mirror
  of the runtime search): «قرض / قروض» landed on firm-finance records before /finance/; «تحويل للخارج» missed
  /remittances/; «كاش» found nothing.
- One governed label, UI-MA-DIMENSIONS, so that /measurement/ can print each priority's governed dimensions.
"""
import json, os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from rc_lib import Session, Table, TxError, insert_ui_rows  # noqa: E402

HOME_S1 = [
    ("en", "Yemen Financial Inclusion Evidence is a bilingual public evidence resource that helps users understand",
     "Yemen Financial Inclusion Evidence is a bilingual public resource on financial inclusion in Yemen. For each figure, "
     "it shows what the evidence establishes and what it does not, when and for whom the figure applies, and where it "
     "comes from."),
    ("ar", "«أدلة الشمول المالي في اليمن» مورد عام ثنائي اللغة يساعد المستخدمين",
     "«أدلة الشمول المالي في اليمن» مورد عام ثنائي اللغة عن الشمول المالي في اليمن. ويبيّن لكل رقم ما الذي تثبته الأدلة "
     "وما الذي لا تثبته، ومتى ولمن ينطبق، ومن أين جاء."),
]
HOME_S3 = [
    ("en", "The latest representative population measure is the World Bank’s Global Findex 2021 survey of Yemen (fieldwork 7 November 2022 to 9 January 2023; World Bank data year 2022): 11.9% of adults aged 15 and over in the areas surveyed had an account at a financial institution or with a mobile-money provider.",
     "11.9% of adults aged 15 and over in the areas surveyed had an account at a financial institution or with a mobile-money provider, according to the latest representative population measure: the World Bank’s Global Findex 2021 survey of Yemen (fieldwork 7 November 2022 to 9 January 2023; World Bank data year 2022)."),
    ("ar", "أحدث قياس ممثل للسكان هو مسح المؤشر العالمي للشمول المالي (Global Findex) لعام 2021 في اليمن، الصادر عن البنك الدولي (نُفذ العمل الميداني من 7 نوفمبر 2022 إلى 9 يناير 2023؛ وسنة البيانات لدى البنك الدولي 2022): كان لدى 11.9% من البالغين بعمر 15 سنة فأكثر في المناطق التي شملها المسح حساب لدى مؤسسة مالية أو لدى مقدم خدمة أموال عبر الهاتف المحمول.",
     "كان لدى 11.9% من البالغين بعمر 15 سنة فأكثر في المناطق التي شملها المسح حساب لدى مؤسسة مالية أو لدى مقدم خدمة أموال عبر الهاتف المحمول، وفق أحدث قياس ممثل للسكان: مسح المؤشر العالمي للشمول المالي (Global Findex) لعام 2021 في اليمن، الصادر عن البنك الدولي (نُفذ العمل الميداني من 7 نوفمبر 2022 إلى 9 يناير 2023؛ وسنة البيانات لدى البنك الدولي 2022)."),
]
CORRECTIONS_S1 = [
    ("en", "Material corrections to published evidence and superseded records, and how they are recorded.",
     "Material corrections to published evidence and superseded records, and how they are recorded. Institutions whose "
     "documents or data are used in this resource can request a correction to any record through the same route as any "
     "reader: write to office@causewaygrp.com with the record or source reference."),
    ("ar", "التصحيحات الجوهرية للأدلة المنشورة والسجلات المستبدلة، وكيف تُسجَّل.",
     "التصحيحات الجوهرية للأدلة المنشورة والسجلات المستبدلة، وكيف تُسجَّل. ويمكن للمؤسسات التي تُستخدم وثائقها أو بياناتها "
     "في هذا المورد أن تطلب تصحيح أي سجل عبر المسار نفسه المتاح لأي قارئ: بالكتابة إلى office@causewaygrp.com مع مرجع "
     "السجل أو المصدر."),
]
# alias id, terms_en, terms_ar, targets, boundary_note_en, boundary_note_ar (04_NAV_UX alias block, columns 1-6)
# «كاش» is ordinary vocabulary ("cash"). RC-NAMES matches a circular name that contains it only beside its other words
# («وي كاش», «سبا كاش», «محفظة كاش»), so the bare word is safe as a search term; never pair «محفظة» and «كاش» in one
# alias term.
NEW_ALIASES = [
    ("SEARCH-ALIAS-031", "loan; loans; borrowing; borrow", "قرض; قروض; اقتراض; الاقتراض; سلفة", "route:/finance/ | route:/people/",
     None, None),
    ("SEARCH-ALIAS-032", "transfer abroad; send money abroad; international transfer",
     "تحويل للخارج; تحويل إلى الخارج; تحويل خارجي; تحويلات خارجية; حوالة خارجية; حوالات خارجية; حوالة من الخارج; "
     "تحويل من الخارج; حوالات المغتربين; تحويلات المغتربين; تحويل دولي; حوالة دولية", "route:/remittances/",
     "Discovery aid only: the remittance evidence here is about money sent to Yemen and transfers within Yemen. It does "
     "not cover money sent from Yemen to other countries.",
     "أداة اكتشاف فقط: تتناول أدلة التحويلات هنا الأموال المرسلة إلى اليمن والحوالات داخل اليمن، ولا تتناول الأموال "
     "المرسلة من اليمن إلى الخارج."),
    ("SEARCH-ALIAS-033", "cash-out; cash out; cashout; cash withdrawal", "كاش; كاش آوت; سحب كاش; سحب نقدي", "route:/payments/",
     None, None),
]
ALIAS_HEADER = ["alias_id", "terms_en", "terms_ar", "targets", "boundary_note_en", "boundary_note_ar"]
UI_ROWS = [("UI-MA-DIMENSIONS", "Dimensions it would cover:", "الأبعاد التي سيغطيها القياس:",
            "RC-18 (owner note of 3 October 2026, 11:15, 4.2). /measurement/: the label before a priority's governed dimensions_en/dimensions_ar.")]


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    insert_ui_rows(s, "RC-18:4.2", UI_ROWS)
    for lang, must, new in HOME_S1:
        row = s.section_row("/", 1, lang)
        col = {"en": 5, "ar": 7}[lang]
        cur = s.ed.get_value("03_PAGE_SECTIONS", row, col)
        if not isinstance(cur, str) or not cur.startswith(must):
            raise TxError(f"RC-18:4.1: Home section 1 ({lang}) does not open as expected")
        s.set("RC-18:4.1", "03_PAGE_SECTIONS", row, col, new, cur, f"/#s1.body_{lang}")
    for lang, old, new in HOME_S3:
        s.replace_section("RC-18:4.1", "/", 3, lang, "body", old, new)
    for lang, old, new in CORRECTIONS_S1:
        s.set_section("RC-18:4.2", "/corrections/", 1, lang, "body", new, old)
    g = s.grid("04_NAV_UX")
    hdr = [i for i, r in enumerate(g, 1) if r and r[0] == "alias_id"]
    if len(hdr) != 1:
        raise TxError("RC-18:4.2: alias header not found once")
    if [str(x or "").strip() for x in g[hdr[0] - 1][:6]] != ALIAS_HEADER:
        raise TxError(f"RC-18:4.2: alias header is not {ALIAS_HEADER}")
    ta = Table(s, "04_NAV_UX", hdr[0])
    if list(ta.rows)[-1] != "SEARCH-ALIAS-030":
        raise TxError("RC-18:4.2: the alias block does not end at SEARCH-ALIAS-030")
    s.ed.insert_rows("04_NAV_UX", max(ta.rows.values()) + 1,
                     [{k: v for k, v in zip(range(1, 7), row) if v is not None} for row in NEW_ALIASES])
    for a, b, c, d, e, f in NEW_ALIASES:
        s.ledger.append(OrderedDict([("finding", "RC-18:4.2"), ("sheet", "04_NAV_UX"), ("row", None), ("col", None), ("field", a),
                                     ("old", None), ("new", " || ".join(str(x) for x in (b, c, d, e, f) if x))]))
    rep = s.save(out, ledger, OrderedDict([("transaction", "RC-18"), ("summary", "Owner note 11:15, 4.1 and 4.2: figure first inside D7; corrections invitation; citizen aliases; dimensions label")]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
