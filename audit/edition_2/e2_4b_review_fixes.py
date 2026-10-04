# -*- coding: utf-8 -*-
"""Edition 2 transaction E2-4b: the independent bilingual and adversarial review of E2-4, folded in (same commit).

  python3 e2_4b_review_fixes.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Findings (4 October 2026):
1. BLOCKING (hard rule 5). E2-4 wrote each pair's counterpart number into the other record's limitations, so the
   public-literal closure traced, for example, CBY-Aden's 2,102,484 on /reforms/ to the World Bank project record, and
   CLM-016's citation printed 2026 counts under a 2025 source. A record must carry only the numbers its own sources
   give. Fix: in a record, the sentence names the counterpart by its record ID and its measure, never by its number; the
   pages where a pair meets print both numbers with the counterpart's record ID, and each counterpart record is bound to
   that page (CLM-010 to /reforms/, FMIIP-BASELINE-2025-01 to /payments/), so each number traces to the record that
   governs it.
2. Pair A: "the two count different things" is not governed (the records say only that the measures are not the same
   unless a definition shows it, and are not reconciled): now "carry different labels … not reconciled".
3. Pair B, Arabic: «لم يُطابَق» (not «لم يُوفَّق», which reads as "failed"); «يورده».
4. Pair C: the 2026 decisions explain why a roster is not a count of operating providers, not why higher entries are not
   new providers. Now: entries by class rather than unique firms; this evidence base has not compared the two rosters
   entry by entry (a statement about this evidence base, which is true); the 2026 roster states no issue date. The
   class labels are given as each roster's record gives them, without asserting that the classes are identical.
5. Arabic date placement in pair A («خط أساس يناير 2025 لمشروع FMIIP»).
Presentation (looked at in the browser): the treatment opens its own paragraph in each section, so the lead "Why the
numbers differ" is seen, not buried at the end of a long paragraph.
"""
import json, os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "release_candidate"))
sys.path.insert(0, HERE)
from rc_lib import Session, Table, TxError  # noqa: E402
import e2_4_why_numbers_differ as E4  # noqa: E402  (the exact text E2-4 wrote, so every replacement is guarded)

F = "E2-4b:REVIEW"
WHY = {"en": "Why the numbers differ: ", "ar": "لماذا تختلف الأرقام: "}
LBL_EN = ("carry different labels under definitions the evidence base does not document and that have not been "
          "reconciled, so the gap cannot be read as growth, as inactivity or as an error, and neither is a count of people.")
LBL_AR = ("ويحمل الرقمان تسميتين مختلفتين وفق تعريفين لا توثقهما قاعدة الأدلة ولم يُطابَق بينهما؛ لذلك لا يُقرأ الفرق "
          "بينهما نموًا ولا خمولًا ولا خطأً، ولا يمثل أيٌّ منهما عددًا من الأشخاص.")
ROSTER_EN = ("The higher 2026 entries cannot be read as new providers entering the market: both rosters count entries by "
             "class rather than unique firms, this evidence base has not compared the two rosters entry by entry, and the "
             "2026 roster states no issue date.")
ROSTER_AR = ("ولا تُقرأ الأعداد الأعلى في قائمة 2026 دخولًا لمقدمي خدمات جدد إلى السوق: فالقائمتان تحصيان القيود بحسب الفئة "
             "لا الشركات الفريدة، ولم تقارن قاعدة الأدلة هذه بين القائمتين قيدًا قيدًا، ولا تذكر قائمة 2026 تاريخ صدورها.")

# --- record sentences: the counterpart by record ID and measure, never by its number --------------------------------
REC = {
    "CLM-010": (
        "Why the numbers differ: the January 2025 baseline of active e-wallet accounts of the World Bank-financed FMIIP "
        "project (record FMIIP-BASELINE-2025-01) is far lower than the 2025 subscriber count here. The two " + LBL_EN +
        " Nor can the 2024 subscriber counts here be read as a fall from the e-money accounts counted in December 2019 "
        "(record CLM-050): that study covered five providers and counted accounts, under a definition never reconciled "
        "with CBY-Aden's.",
        "لماذا تختلف الأرقام: خط أساس يناير 2025 لحسابات المحافظ الإلكترونية النشطة في مشروع FMIIP الممول من البنك الدولي "
        "(السجل FMIIP-BASELINE-2025-01) أقل بكثير من عدد المشتركين لعام 2025 هنا. " + LBL_AR +
        " كذلك لا تُقرأ أعداد المشتركين لعام 2024 هنا تراجعًا عن حسابات النقود الإلكترونية المحصاة في ديسمبر 2019 "
        "(السجل CLM-050): فتلك الدراسة شملت خمسة مقدمي خدمات وأحصت حسابات، وفق تعريف لم يُطابَق قط مع تعريف البنك المركزي "
        "اليمني – عدن."),
    "FMIIP-BASELINE-2025-01": (
        "Why the numbers differ: CBY-Aden reports a far higher count of e-wallet subscribers for the first half of 2025 "
        "(record CLM-010) than the active e-wallet accounts here. The two " + LBL_EN,
        "لماذا تختلف الأرقام: يُبلغ البنك المركزي اليمني – عدن عن عدد أعلى بكثير من مشتركي المحافظ الإلكترونية للنصف "
        "الأول من 2025 (السجل CLM-010) مقارنةً بحسابات المحافظ النشطة هنا. " + LBL_AR),
    "CLM-050": (
        "Why the numbers differ: CBY-Aden's lower e-wallet subscriber counts for 2024 (record CLM-010) cannot be read as a "
        "fall from this total. This study covered five providers and counted accounts; CBY-Aden counts subscribers under "
        "its own definition and reporting scope. The two have not been reconciled, and neither counts people.",
        "لماذا تختلف الأرقام: لا تُقرأ أعداد مشتركي المحافظ الإلكترونية الأدنى التي يوردها البنك المركزي اليمني – عدن "
        "لعام 2024 (السجل CLM-010) تراجعًا عن هذا الإجمالي. فهذه الدراسة شملت خمسة مقدمي خدمات وأحصت حسابات، أما البنك "
        "المركزي فيحصي مشتركين وفق تعريفه ونطاق إبلاغه. ولم يُطابَق بين الرقمين، ولا يحصي أيٌّ منهما أشخاصًا."),
    "CLM-016": (
        "Why the numbers differ: the 2026 roster (record CLM-009) lists more entries in each of its three classes. "
        + ROSTER_EN,
        "لماذا تختلف الأرقام: تُدرج قائمة 2026 (السجل CLM-009) قيودًا أكثر في كل فئة من فئاتها الثلاث. " + ROSTER_AR),
    "CLM-009": (
        "Why the numbers differ: the 2025 roster (record CLM-016) listed fewer entries in each of its three classes. "
        + ROSTER_EN,
        "لماذا تختلف الأرقام: أدرجت قائمة 2025 (السجل CLM-016) قيودًا أقل في كل فئة من فئاتها الثلاث. " + ROSTER_AR),
}
OLD_REC = {"CLM-010": ([E4.A_EN, E4.B_EN], [E4.A_AR, E4.B_AR]), "FMIIP-BASELINE-2025-01": ([E4.A2_EN], [E4.A2_AR]),
           "CLM-050": ([E4.B_EN], [E4.B_AR]), "CLM-016": ([E4.C2_EN], [E4.C2_AR]), "CLM-009": ([E4.C_EN], [E4.C_AR])}

# --- section paragraphs: both numbers, the counterpart's record ID, a paragraph of their own --------------------------
SEC = {
    ("/payments/", 5): (E4.A_EN, E4.A_AR,
        "Why the numbers differ: the January 2025 baseline of the World Bank-financed FMIIP project counts 375,252 active "
        "e-wallet accounts (record FMIIP-BASELINE-2025-01), far fewer than the 2,102,484 subscribers CBY-Aden reports for "
        "the first half of 2025. The two " + LBL_EN,
        "لماذا تختلف الأرقام: يحصي خط أساس يناير 2025 لمشروع FMIIP الممول من البنك الدولي 375,252 حساب محفظة إلكترونية "
        "نشطًا (السجل FMIIP-BASELINE-2025-01)، وهو أقل بكثير من 2,102,484 مشتركًا يُبلغ عنهم البنك المركزي اليمني – عدن "
        "للنصف الأول من 2025. " + LBL_AR),
    ("/payments/", 6): (E4.B_EN, E4.B_AR,
        "Why the numbers differ: the 807,919 e-money accounts of December 2019 and CBY-Aden's 414,631 to 581,075 e-wallet "
        "subscribers in the first three quarters of 2024 (record CLM-010) cannot be read as a fall. The first counts "
        "accounts at the five providers one study of the Institute of Banking Studies (IBS) covered; the second counts "
        "subscribers under CBY-Aden's own definition and reporting scope. The two have not been reconciled, and neither "
        "counts people.",
        "لماذا تختلف الأرقام: لا يُقرأ الفرق بين 807,919 حساب نقود إلكترونية في ديسمبر 2019 وما بين 414,631 و581,075 "
        "مشتركًا في المحافظ الإلكترونية يورده البنك المركزي اليمني – عدن للأرباع الثلاثة الأولى من 2024 (السجل CLM-010) "
        "تراجعًا. فالأول يحصي حسابات لدى خمسة مقدمي خدمات شملتهم دراسة واحدة لمعهد الدراسات المصرفية، والثاني يحصي مشتركين "
        "وفق تعريف البنك المركزي ونطاق إبلاغه. ولم يُطابَق بين الرقمين، ولا يحصي أيٌّ منهما أشخاصًا."),
    ("/reforms/", 6): (E4.A2_EN, E4.A2_AR,
        "Why the numbers differ: CBY-Aden reports 2,102,484 e-wallet subscribers for the first half of 2025 (record "
        "CLM-010), far more than the project's 375,252 active e-wallet accounts in January 2025. The two " + LBL_EN,
        "لماذا تختلف الأرقام: يُبلغ البنك المركزي اليمني – عدن عن 2,102,484 مشتركًا في المحافظ الإلكترونية للنصف الأول "
        "من 2025 (السجل CLM-010)، وهو أكثر بكثير من 375,252 حساب محفظة إلكترونية نشطًا يحصيها المشروع في يناير 2025. "
        + LBL_AR),
    ("/providers/", 4): (E4.C_EN, E4.C_AR,
        "Why the numbers differ: the official 2025 roster (record CLM-016) listed 79 exchange companies, 195 exchange "
        "establishments and 108 remittance agents in its three classes. " + ROSTER_EN,
        "لماذا تختلف الأرقام: أدرجت القائمة الرسمية لعام 2025 (السجل CLM-016) في فئاتها الثلاث 79 شركة صرافة و195 منشأة "
        "صرافة و108 وكلاء للحوالات. " + ROSTER_AR),
}


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    t06 = Table(s, "06_EVIDENCE_OBJECTS", 4)
    for oid, (new_en, new_ar) in REC.items():
        olds = OLD_REC[oid]
        for field, old_parts, new in (("limitations_en", olds[0], new_en), ("limitations_ar", olds[1], new_ar)):
            s.replace(F, "06_EVIDENCE_OBJECTS", t06.rows[oid], t06.col(field), " " + " ".join(old_parts), " " + new,
                      f"{oid}.{field}")
    for (route, order), (old_en, old_ar, new_en, new_ar) in SEC.items():
        s.replace_section(F, route, order, "en", "body", " " + old_en, "\n" + new_en)
        s.replace_section(F, route, order, "ar", "body", " " + old_ar, "\n" + new_ar)
    # each counterpart record is bound to the page where its number now appears, so the number traces to it
    t06.set(F, "CLM-010", "public_routes", "/evidence/compare/ | /payments/ | /providers/ | /reforms/",
            "/evidence/compare/ | /payments/ | /providers/")
    t06.set(F, "FMIIP-BASELINE-2025-01", "public_routes", "/reforms/ | /evidence/compare/ | /payments/",
            "/reforms/ | /evidence/compare/")
    t07 = Table(s, "07_PUBLIC_CLAIMS", 4)
    t07.set(F, "CLM-010", "public_routes", '["/evidence/compare","/payments","/providers","/reforms"]',
            '["/evidence/compare","/payments","/providers"]')
    rep = s.save(out, ledger, OrderedDict([("transaction", "E2-4b"), ("summary", "E2-4 review fixes: each number traces to the record that governs it; governed wording for pairs A and C; Arabic; a paragraph of its own")]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
