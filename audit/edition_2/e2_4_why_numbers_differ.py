# -*- coding: utf-8 -*-
"""Edition 2 transaction E2-4: "Why the numbers differ" where two governed numbers that look contradictory meet a
reader (candidate d).

  python3 e2_4_why_numbers_differ.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

The site already does this well in three places: /remittances/ (a revision of the same year, not a fall), the
22% vs 91.84% Reading, and the POS series (raw totals vs the source's own growth figure, both shown). A sweep of every
record that prints a number on the eight domain pages (audit/PUBLIC_LITERAL_CLOSURE.json, 4 October 2026) found three
more pairs a reader meets without that treatment; every number below is already governed in its own record:

A. 2,102,484 e-wallet subscribers (CBY-Aden infographic, first half of 2025; CLM-010, /payments/) and 375,252 active
   e-wallet accounts (the World Bank-financed FMIIP project's baseline, January 2025; FMIIP-BASELINE-2025-01,
   /reforms/). Six months apart, a factor of more than five: a reader can take the gap as growth, inactivity or error.
   Different things counted, under definitions the evidence base does not document (both records say so).
B. 807,919 e-money accounts (IBS study of five providers, December 2019; CLM-050) and 414,631 to 581,075 e-wallet
   subscribers (CBY-Aden payments report, 2024 Q1-Q3; CLM-010), on the same page (/payments/ sections 5 and 6): it reads
   as a fall. Different coverage, unit and publisher, never reconciled.
C. The 2025 roster (79 exchange companies, 195 exchange establishments, 108 remittance agents; CLM-016) and the 2026
   roster (100, 231, 111; CLM-009): it reads as new providers. Entries by class, not unique firms; the 2026 roster has
   no issue date; the 2026 decisions have not been matched with it (all stated in CLM-009).

The same treatment each time, built from what the two records already govern: one sentence that opens "Why the
numbers differ:" / «لماذا تختلف الأرقام:», names both numbers with their publisher and date, says what each counts,
and says what the gap cannot be read as. It goes into the "what not to conclude" part of both records' limitations
(always visible on a record page) and into the existing section where the pair meets. No new section: a section on a
domain page would need the steward's presentation contract (recorded as the next form, a typed difference relation).
"""
import json, os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "release_candidate"))
from rc_lib import Session, Table, TxError  # noqa: E402

F = "E2-4:WHY-DIFFER"

A_EN = ("Why the numbers differ: the World Bank-financed FMIIP project's baseline for January 2025 counts 375,252 active "
        "e-wallet accounts, far fewer than the 2,102,484 e-wallet subscribers CBY-Aden reports for the first half of 2025. "
        "The two count different things, accounts the project defines as active and subscribers as CBY-Aden reports them, "
        "under definitions the evidence base does not document, so the gap cannot be read as growth, as inactivity or as "
        "an error, and neither is a count of people.")
A_AR = ("لماذا تختلف الأرقام: يحصي خط الأساس لمشروع FMIIP، الممول من البنك الدولي، في يناير 2025 ما عدده 375,252 حساب "
        "محفظة إلكترونية نشطًا، وهو أقل بكثير من 2,102,484 مشتركًا في المحافظ الإلكترونية يُبلغ عنهم البنك المركزي "
        "اليمني – عدن للنصف الأول من 2025. فهما يحصيان شيئين مختلفين، حساباتٍ يعرّفها المشروع بأنها نشطة ومشتركين كما "
        "يُبلغ عنهم البنك المركزي، وفق تعريفين لا توثقهما قاعدة الأدلة؛ لذلك لا يُقرأ الفرق بينهما نموًا ولا خمولًا ولا "
        "خطأً، ولا يمثل أيٌّ منهما عددًا من الأشخاص.")
B_EN = ("Why the numbers differ: the 807,919 e-money accounts of December 2019 and CBY-Aden's 414,631 to 581,075 e-wallet "
        "subscribers in the first three quarters of 2024 cannot be read as a fall. The first counts accounts at the five "
        "providers one study of the Institute of Banking Studies (IBS) covered; the second counts subscribers under "
        "CBY-Aden's own definition and reporting scope. The two have not been reconciled, and neither counts people.")
B_AR = ("لماذا تختلف الأرقام: لا يُقرأ الفرق بين 807,919 حساب نقود إلكترونية في ديسمبر 2019 وما بين 414,631 و581,075 "
        "مشتركًا في المحافظ الإلكترونية أورده البنك المركزي اليمني – عدن للأرباع الثلاثة الأولى من 2024 تراجعًا. فالأول "
        "يحصي حسابات لدى خمسة مقدمي خدمات شملتهم دراسة واحدة لمعهد الدراسات المصرفية، والثاني يحصي مشتركين وفق تعريف "
        "البنك المركزي ونطاق إبلاغه. ولم يُوفَّق بين الرقمين، ولا يحصي أيٌّ منهما أشخاصًا.")
C_EN = ("Why the numbers differ: the official 2025 roster listed 79 exchange companies, 195 exchange establishments and "
        "108 remittance agents. The higher 2026 entries are not a count of new providers: both rosters count entries by "
        "class rather than unique firms, the 2026 roster states no issue date, and the 2026 suspension and withdrawal "
        "decisions have not been matched with it entity by entity.")
C_AR = ("لماذا تختلف الأرقام: أدرجت القائمة الرسمية لعام 2025 عدد 79 شركة صرافة و195 منشأة صرافة و108 وكلاء للحوالات. "
        "ولا تمثل الأعداد الأعلى في قائمة 2026 عددًا لمقدمي خدمات جدد: فالقائمتان تحصيان القيود بحسب الفئة لا الشركات "
        "الفريدة، ولا تذكر قائمة 2026 تاريخ صدورها، ولم تُطابَق قرارات التعليق وسحب الترخيص الصادرة في 2026 معها جهةً جهة.")
C2_EN = ("Why the numbers differ: the official 2026 roster lists 100 exchange companies, 231 individual exchange "
         "establishments and 111 remittance agents, more than the 79, 195 and 108 of the 2025 roster. The higher 2026 "
         "entries are not a count of new providers: both rosters count entries by class rather than unique firms, the 2026 "
         "roster states no issue date, and the 2026 suspension and withdrawal decisions have not been matched with it "
         "entity by entity.")
C2_AR = ("لماذا تختلف الأرقام: تُدرج القائمة الرسمية لعام 2026 عدد 100 شركة صرافة و231 منشأة صرافة فردية و111 وكيلًا "
         "للحوالات، وهي أكثر من 79 و195 و108 في قائمة 2025. ولا تمثل الأعداد الأعلى في قائمة 2026 عددًا لمقدمي خدمات جدد: "
         "فالقائمتان تحصيان القيود بحسب الفئة لا الشركات الفريدة، ولا تذكر قائمة 2026 تاريخ صدورها، ولم تُطابَق قرارات "
         "التعليق وسحب الترخيص الصادرة في 2026 معها جهةً جهة.")
# A on /reforms/ names the CBY-Aden figure first, since the page is about the project's baselines
A2_EN = ("Why the numbers differ: CBY-Aden reports 2,102,484 e-wallet subscribers for the first half of 2025, far more "
         "than the project's 375,252 active e-wallet accounts in January 2025. The two count different things under "
         "definitions the evidence base does not document, so the gap cannot be read as growth, as inactivity or as an "
         "error, and neither is a count of people.")
A2_AR = ("لماذا تختلف الأرقام: يُبلغ البنك المركزي اليمني – عدن عن 2,102,484 مشتركًا في المحافظ الإلكترونية للنصف الأول "
         "من 2025، وهو أكثر بكثير من 375,252 حساب محفظة إلكترونية نشطًا يحصيها المشروع في يناير 2025. فهما يحصيان شيئين "
         "مختلفين وفق تعريفين لا توثقهما قاعدة الأدلة؛ لذلك لا يُقرأ الفرق بينهما نموًا ولا خمولًا ولا خطأً، ولا يمثل أيٌّ "
         "منهما عددًا من الأشخاص.")

# (record, extra EN, extra AR) appended to the first part of limitations (before " | " when the field has two parts)
RECORDS = [("CLM-010", [A_EN, B_EN], [A_AR, B_AR]), ("FMIIP-BASELINE-2025-01", [A2_EN], [A2_AR]),
           ("CLM-050", [B_EN], [B_AR]), ("CLM-016", [C2_EN], [C2_AR]), ("CLM-009", [C_EN], [C_AR])]
SECTIONS = [("/payments/", 5, A_EN, A_AR), ("/payments/", 6, B_EN, B_AR), ("/reforms/", 6, A2_EN, A2_AR),
            ("/providers/", 4, C_EN, C_AR)]


def append_first_part(cur, extra):
    head, sep, tail = cur.partition(" | ")
    return head.rstrip() + " " + " ".join(extra) + (sep + tail if sep else "")


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    t06 = Table(s, "06_EVIDENCE_OBJECTS", 4)
    for oid, en, ar in RECORDS:
        for field, extra in (("limitations_en", en), ("limitations_ar", ar)):
            cur = t06.get(oid, field)
            if "Why the numbers differ" in cur or "لماذا تختلف الأرقام" in cur:
                raise TxError(f"{oid}.{field} already carries the treatment")
            t06.set(F, oid, field, append_first_part(cur, extra), cur)
    for route, order, en, ar in SECTIONS:
        for lang, extra in (("en", en), ("ar", ar)):
            row = s.section_row(route, order, lang)
            col = 5 if lang == "en" else 7
            cur = s.ed.get_value("03_PAGE_SECTIONS", row, col)
            s.set(F, "03_PAGE_SECTIONS", row, col, cur.rstrip() + " " + extra, cur, f"{route}#s{order}.body_{lang}")
    rep = s.save(out, ledger, OrderedDict([("transaction", "E2-4"), ("summary", "Why the numbers differ: three pairs that look contradictory (e-wallet subscribers vs active accounts; 2019 accounts vs 2024 subscribers; 2025 vs 2026 roster), in both records and where they meet")]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
