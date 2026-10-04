# -*- coding: utf-8 -*-
"""Edition 2 transaction E2-3b: the independent bilingual and adversarial review of E2-3, folded in (same commit).

  python3 e2_3b_review_fixes.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

The reviewer re-derived the figure from the file with its own script: 0.351821646573129, the adult-weighted mean of the
19 low-income economies with a 2021-wave observation (12 surveyed in 2021, 7 in 2022, Yemen among them) to 12
decimals; Yemen weighs 6.6%; without Yemen 36.8%. Findings:
1. "the 19 economies it classes as low income" reads as if only 19 economies are low income; the file classes 25
   (six have no observation in this wave). Now "the 19 low-income economies surveyed in it".
2. "(fiscal year 2024)" has no public locator: the only basis was a column name (incomegroupwb24). Now "the income
   classification in the Global Findex Database 2025" (hard rule 5).
3. Compare prints CLM-001's method, which named "the low-income context figure" without the figure; the method now
   states it.
4. Arabic: «اقتصادات ذات ظروف متباينة جدًا» (economies do not "live" conditions).
"""
import json, os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "release_candidate"))
from rc_lib import Session, Table, TxError  # noqa: E402

F = "E2-3b:REVIEW"
CLM = [
    ("summary_en", "the World Bank's figure for the same survey wave across the 19 economies it classes as low income, "
                   "Yemen among them, is 35.2%.",
     "the World Bank's figure for the same survey wave across the 19 low-income economies surveyed in it, Yemen among "
     "them, is 35.2%."),
    ("summary_ar", "يبلغ رقم البنك الدولي لموجة المسح نفسها في 19 اقتصادًا يصنّفها منخفضة الدخل، ومنها اليمن، 35.2%.",
     "يبلغ رقم البنك الدولي لموجة المسح نفسها في الاقتصادات منخفضة الدخل الـ19 التي شملتها الموجة، ومنها اليمن، 35.2%."),
    ("limitations_en", "and uses the income classification of the World Bank's database (fiscal year 2024),",
     "and uses the income classification in the Global Findex Database 2025,"),
    ("limitations_ar", "فهو متوسط لاقتصادات تعيش ظروفًا متباينة جدًا، ويشمل اليمن نفسه، ويستند إلى تصنيف الدخل الذي تعتمده "
                       "قاعدة بيانات البنك الدولي (السنة المالية 2024)،",
     "فهو متوسط لاقتصادات ذات ظروف متباينة جدًا، ويشمل اليمن نفسه، ويستند إلى تصنيف الدخل المعتمد في قاعدة بيانات "
     "Global Findex 2025،"),
    ("method_en", "The low-income context figure is the World Bank's own aggregate for the same wave and indicator; this "
                  "resource reproduced it as the average of the 19 economies' published values weighted by their adult "
                  "populations.",
     "The low-income context figure, 35.2%, is the World Bank's own aggregate for the same wave and indicator; this "
     "resource reproduced it as the average of the published values of the 19 low-income economies surveyed in the "
     "wave, weighted by their adult populations."),
    ("method_ar", "ورقم السياق للاقتصادات منخفضة الدخل هو التجميع الذي ينشره البنك الدولي نفسه للموجة والمؤشر ذاتيهما؛ وقد "
                  "أعاد هذا المورد احتسابه متوسطًا لقيم الاقتصادات الـ19 المنشورة، مرجّحًا بعدد البالغين في كل منها.",
     "ورقم السياق للاقتصادات منخفضة الدخل، 35.2%، هو التجميع الذي ينشره البنك الدولي نفسه للموجة والمؤشر ذاتيهما؛ وقد "
     "أعاد هذا المورد احتسابه متوسطًا للقيم المنشورة للاقتصادات منخفضة الدخل الـ19 التي شملتها الموجة، مرجّحًا بعدد "
     "البالغين في كل منها."),
]
PEOPLE = [
    ("en", "the World Bank's figure for the same wave across the 19 economies it classes as low income, Yemen among them, "
           "is 35.2%;",
     "the World Bank's figure for the same wave across the 19 low-income economies surveyed in it, Yemen among them, is "
     "35.2%;"),
    ("ar", "يبلغ رقم البنك الدولي للموجة نفسها في 19 اقتصادًا يصنّفها منخفضة الدخل، ومنها اليمن، 35.2%؛",
     "يبلغ رقم البنك الدولي للموجة نفسها في الاقتصادات منخفضة الدخل الـ19 التي شملتها، ومنها اليمن، 35.2%؛"),
]


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    t06 = Table(s, "06_EVIDENCE_OBJECTS", 4)
    for field, old, new in CLM:
        s.replace(F, "06_EVIDENCE_OBJECTS", t06.rows["CLM-001"], t06.col(field), old, new, f"CLM-001.{field}")
    for lang, old, new in PEOPLE:
        s.replace_section(F, "/people/", 2, lang, "body", old, new)
    t25 = Table(s, "25_FINDEX_BASELINE", 4)
    old = t25.get("WB-FINDEX-CTX-2021-LIC", "caveat")
    t25.set(F, "WB-FINDEX-CTX-2021-LIC", "caveat",
            old.replace("the 19 economies classed Low income (fiscal year 2024)",
                        "the 19 economies the file classes Low income with a 2021-wave observation"), old)
    rep = s.save(out, ledger, OrderedDict([("transaction", "E2-3b"), ("summary", "E2-3 review fixes: 19 surveyed low-income economies; classification named by its source; the figure in the method; Arabic")]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
