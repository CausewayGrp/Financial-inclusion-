# -*- coding: utf-8 -*-
"""Final content pass, transaction FC-3b: the /people/ section the reader sees, and the three published observations.

  python3 fc_3b_people_section.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Finding FC-3:FC-A-01, completing it. FC-3 corrected the five records and the vintage ladder, but two of its steps were
lost when the script was restructured mid-session and did not run: the /people/ section a reader actually reads, and
the three published 2022 observations in 25_FINDEX_BASELINE. Without them /people/ still headed the section "Saving and
borrowing tell a different - older - story" and printed only the 2014 values, which is the misleading framing the
finding is about. The ledger of FC-3 shows the gap; this transaction closes it. Nothing in FC-3 is undone.

The three observations are the World Bank's own published values for Yemen in 2022, each reproduced exactly from the
respondent file (see the FC-1 docstring for the reconciliation). The section states each with the interval this
resource derives, and says who derived it.
"""
import json, os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "release_candidate"))
from rc_lib import Session, Table, TxError  # noqa: E402

F = "FC-3b:FC-A-01"
S25 = "25_FINDEX_BASELINE"
API = "https://data.worldbank.org/indicator/FX.OWN.TOTL.ZS?locations=YE"

OBS = [("WB-FINDEX-OBS-2022-010", "save.any.t.d", "Saved any money in the past year", 21.6,
        "Weighted World Bank value for the 2021 Findex wave; the same series also carries a 2014 value (20.6%). "
        "A 95% interval of 18.4% to 24.9% is derived from the respondent file (CW-FINDEX-MOE-2022-015)."),
       ("WB-FINDEX-OBS-2022-011", "borrow.any.t.d", "Borrowed any money in the past year", 51.3,
        "Weighted World Bank value for the 2021 Findex wave; the same series also carries a 2014 value (66.0%), "
        "which is not the 65.9% printed on the World Bank's own 2014 country page - see finding FC-A-04. "
        "A 95% interval of 47.1% to 55.5% is derived from the respondent file (CW-FINDEX-MOE-2022-016)."),
       ("WB-FINDEX-OBS-2022-012", "g20.any", "Made or received a digital payment", 9.3,
        "Weighted World Bank value for the 2021 Findex wave; the same series also carries a 2014 value (4.4%). "
        "A 95% interval of 7.4% to 11.3% is derived from the respondent file (CW-FINDEX-MOE-2022-017).")]

OLD_H_EN = "Saving and borrowing tell a different — older — story"
OLD_H_AR = ("الاقتراض والادخار "
            "يقدمان صورة أخرى — "
            "لكنها أقدم")
NEW_H_EN = "Saving, borrowing and digital payments in the same wave"
NEW_H_AR = ("الادخار والاقتراض "
            "والمدفوعات الرقمية "
            "في الموجة نفسها")

# The 2014 figures stay on the page, with their own year named, because they are the only values this resource holds
# for borrowing by source and saving by method. What changes is that they are no longer the latest thing said.
NEW_B_EN = (
    "The same 2021 wave measures more than account ownership. In it, 21.6% of adults reported saving any money in the "
    "past year (95% interval 18.4% to 24.9%), 51.3% reported borrowing any money (47.1% to 55.5%) and 9.3% reported "
    "making or receiving a digital payment (7.4% to 11.3%). Borrowing is far more common than saving, and both are "
    "far more common than having an account — borrowing here includes borrowing from family or friends, which "
    "needs no provider at all. The intervals are derived by this resource from the survey's own weights; the World "
    "Bank publishes none. For the sources people borrowed from and the methods they saved by, the latest values this "
    "resource holds are older, from the World Bank's 2014 country profile: 51.7% of adults borrowed from family or "
    "friends, 15.0% from a private informal lender and 0.4% from a financial institution, while 0.9% saved at a "
    "financial institution and 4.5% through a savings club or a person outside the family. Those categories are not "
    "additive, each percentage applies to the all-adult base used by its question, and they are not subtracted from "
    "the 2022 figures above.")
NEW_B_AR = (
    "تقيس موجة 2021 نفسها أكثر "
    "من امتلاك الحساب. ففيها "
    "أفاد 21.6% من البالغين بأنهم "
    "ادخروا أي مبلغ خلال "
    "السنة الماضية (فترة ثقة "
    "95% من 18.4% إلى 24.9%)، وأفاد 51.3% بأنهم "
    "اقترضوا أي مبلغ (من 47.1% إلى "
    "55.5%)، و9.3% بأنهم أجروا مدفوعة "
    "رقمية أو تلقوها (من 7.4% إلى "
    "11.3%). والاقتراض أشيع بكثير "
    "من الادخار، وكلاهما "
    "أشيع بكثير من امتلاك "
    "حساب — فالاقتراض هنا "
    "يشمل الاقتراض من الأسرة "
    "أو الأصدقاء وهو لا يحتاج "
    "مقدم خدمة أبدًا. "
    "والفترات يستخرجها هذا "
    "المورد من أوزان المسح "
    "نفسها؛ ولا ينشر البنك "
    "الدولي أي منها. أما جهات "
    "الاقتراض وأساليب "
    "الادخار فأحدث ما يحمله "
    "هذا المورد عنها أقدم، "
    "من الملف القطري للبنك "
    "الدولي لعام 2014: فقد اقترض "
    "51.7% من البالغين من الأسرة "
    "أو الأصدقاء، و15.0% من مقرض "
    "خاص غير رسمي، و0.4% من مؤسسة "
    "مالية، بينما ادخر 0.9% لدى "
    "مؤسسة مالية و4.5% عبر جمعية "
    "ادخار أو شخص من خارج "
    "الأسرة. وهذه الفئات غير "
    "قابلة للجمع، وكل نسبة "
    "تنطبق على قاعدة جميع "
    "البالغين المستخدمة في "
    "سؤالها، ولا تُطرح من "
    "أرقام 2022 أعلاه.")


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)

    # 1. the three published 2022 observations
    t25 = Table(s, S25, 4)
    rows = []
    for oid, code, label, value, caveat in OBS:
        if oid in t25.rows:
            raise TxError("25 already holds " + oid)
        rows.append({1: oid, 2: code, 3: label, 4: "total", 5: "2022", 6: value,
                     7: "percent of population ages 15+", 8: "World Bank Global Findex", 9: API,
                     10: "PUBLIC_PRIMARY_AGGREGATE", 11: caveat})
    at = t25.rows["WB-FINDEX-CURRENTNESS-2025-001"]
    s.ed.insert_rows(S25, at, rows)
    for oid, _c, label, value, _cav in OBS:
        s.ledger.append(OrderedDict([("finding", F), ("sheet", S25), ("row", None), ("col", None), ("field", oid),
                                     ("old", None), ("new", "%s = %s%% (World Bank, 2022)" % (label, value))]))

    # 2. the section a reader reads
    s.set_section(F, "/people/", 6, "en", "heading", NEW_H_EN, OLD_H_EN)
    s.set_section(F, "/people/", 6, "ar", "heading", NEW_H_AR, OLD_H_AR)
    row_en = s.section_row("/people/", 6, "en")
    row_ar = s.section_row("/people/", 6, "ar")
    s.set(F, "03_PAGE_SECTIONS", row_en, 5, NEW_B_EN, s.ed.get_value("03_PAGE_SECTIONS", row_en, 5),
          "/people/#s6.body_en")
    s.set(F, "03_PAGE_SECTIONS", row_ar, 7, NEW_B_AR, s.ed.get_value("03_PAGE_SECTIONS", row_ar, 7),
          "/people/#s6.body_ar")

    rep = s.save(out, ledger, OrderedDict([
        ("transaction", "FC-3b"),
        ("summary", "The /people/ section now leads with the 2021 wave's own saving, borrowing and digital-payment "
                    "values and their derived intervals, keeping the 2014 source and method detail below them and "
                    "explicitly not subtracted from them; the three published observations recorded")]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
