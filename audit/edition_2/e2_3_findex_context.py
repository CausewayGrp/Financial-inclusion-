# -*- coding: utf-8 -*-
"""Edition 2 transaction E2-3: one same-source context row beside Yemen's account-ownership figure (candidate c).

  python3 e2_3_findex_context.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

REOPEN-INTL was recorded as "missing input: the Master holds no Findex regional or income-group aggregates; the owner
should supply them". That input is public and readable here. Read on 4 October 2026: the Global Findex Database 2025
file (GlobalFindexDatabase2025.csv, linked from the download page that SRC-WB-FINDEX-2025-EDITION already cites), row
"Low income" (LIC), year 2021, group "all", account_t_d = 0.351821646573129. Checked by reproduction: the
adult-population-weighted mean (pop_adult) of the 19 economies the file classes "Low income" (incomegroupwb24) with a
2021-wave observation, Yemen's 2022 observation among them, is 0.351822 — the same number to six decimals; without
the seven economies surveyed in 2022 it would be 0.399. So the figure is the same source, the same indicator and
definition (account_t_d), the same wave, and it contains Yemen.

Why the income group, not the region: one context row only (the brief's rule). The region "Middle East & North
Africa (excluding high income)" (45.4%, 10 economies, Yemen included, on the fiscal-year-2024 regions, without
Afghanistan and Pakistan) is an average dominated by two large economies far from Yemen's conditions; the income
group is the World Bank's own peer grouping for economies at a similar income. The World Bank printed both beside
Yemen in its own country table (The Little Data Book on Financial Inclusion 2015, p. 159).

Guarding the firewall and the "never a ranking" rule: the figure is stated as context, with what it averages, that
it includes Yemen, the classification year, and that Yemen's own figure covers only the areas surveyed. It is not
printed on Home or in a drawing, is not a target and implies no position. One decimal place (E2-2 rule).
"""
import json, os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "release_candidate"))
from rc_lib import Session, Table, TxError  # noqa: E402

F = "E2-3:REOPEN-INTL"
CSV = ("https://thedocs.worldbank.org/en/doc/be6615202d1f08a25855c8ac2d615122-0050012025/related/"
       "GlobalFindexDatabase2025.csv")
ROW = {1: "WB-FINDEX-CTX-2021-LIC", 2: "account_t_d", 3: "Account ownership (same definition as FX.OWN.TOTL.ZS)",
       4: "low-income economies (19 economies with a 2021-wave observation, Yemen included)", 5: "2021 wave", 6: 35.2,
       7: "percent of population ages 15+", 8: "World Bank Global Findex", 9: CSV,
       10: "PUBLIC_PRIMARY_AGGREGATE_CONTEXT",
       11: "World Bank aggregate 0.351821646573129 (Global Findex Database 2025, row Low income, 2021, all); reproduced as "
           "the adult-population-weighted mean of the 19 economies classed Low income (fiscal year 2024), Yemen's 2022 "
           "observation included. Context only: not a benchmark, target or ranking."}

SUM_EN = ("The Global Findex 2025 edition adds 2024 observations for many economies, but no newer Yemen observation.",
          "The Global Findex 2025 edition adds 2024 observations for many economies, but no newer Yemen observation. For "
          "context, the World Bank's figure for the same survey wave across the 19 economies it classes as low income, "
          "Yemen among them, is 35.2%.")
SUM_AR = ("وتضيف نسخة Global Findex 2025 مشاهدات لعام 2024 في اقتصادات عديدة، لكنها لا تضيف مشاهدة أحدث لليمن.",
          "وتضيف نسخة Global Findex 2025 مشاهدات لعام 2024 في اقتصادات عديدة، لكنها لا تضيف مشاهدة أحدث لليمن. وللسياق، "
          "يبلغ رقم البنك الدولي لموجة المسح نفسها في 19 اقتصادًا يصنّفها منخفضة الدخل، ومنها اليمن، 35.2%.")
LIM_EN = ("and more than a quarter of primary sampling units were replaced.",
          "and more than a quarter of primary sampling units were replaced. The low-income figure is context, not a "
          "benchmark, a target or a ranking: it averages economies in very different conditions, includes Yemen itself "
          "and uses the income classification of the World Bank's database (fiscal year 2024), while Yemen's own figure "
          "covers only the areas its survey reached.")
LIM_AR = ("كما استُبدل أكثر من ربع وحدات المعاينة الأولية.",
          "كما استُبدل أكثر من ربع وحدات المعاينة الأولية. ورقم الاقتصادات منخفضة الدخل للسياق فقط، وليس معيارًا ولا "
          "هدفًا ولا ترتيبًا: فهو متوسط لاقتصادات تعيش ظروفًا متباينة جدًا، ويشمل اليمن نفسه، ويستند إلى تصنيف الدخل "
          "الذي تعتمده قاعدة بيانات البنك الدولي (السنة المالية 2024)، في حين يقتصر رقم اليمن على المناطق التي بلغها "
          "المسح.")
METH_EN = ("Weighted survey estimate",
           "Weighted survey estimate. The low-income context figure is the World Bank's own aggregate for the same wave "
           "and indicator; this resource reproduced it as the average of the 19 economies' published values weighted by "
           "their adult populations.")
METH_AR = ("تقدير مسحي موزون وفق تصميم المسح وأوزانه.",
           "تقدير مسحي موزون وفق تصميم المسح وأوزانه. ورقم السياق للاقتصادات منخفضة الدخل هو التجميع الذي ينشره البنك "
           "الدولي نفسه للموجة والمؤشر ذاتيهما؛ وقد أعاد هذا المورد احتسابه متوسطًا لقيم الاقتصادات الـ19 المنشورة، مرجّحًا "
           "بعدد البالغين في كل منها.")
PEOPLE_EN = ("The value is a survey measure for that wave and fieldwork period, not a 2026 population rate.",
             "The value is a survey measure for that wave and fieldwork period, not a 2026 population rate. For context "
             "only, the World Bank's figure for the same wave across the 19 economies it classes as low income, Yemen "
             "among them, is 35.2%; it averages very different economies and is not a benchmark or a ranking.")
PEOPLE_AR = ("هذا قياس مسحي لتلك الموجة والفترة، وليس نسبة سكانية لعام 2026.",
             "هذا قياس مسحي لتلك الموجة والفترة، وليس نسبة سكانية لعام 2026. وللسياق فقط، يبلغ رقم البنك الدولي للموجة "
             "نفسها في 19 اقتصادًا يصنّفها منخفضة الدخل، ومنها اليمن، 35.2%؛ وهو متوسط لاقتصادات متباينة جدًا، وليس "
             "معيارًا ولا ترتيبًا.")


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    t06 = Table(s, "06_EVIDENCE_OBJECTS", 4)
    for field, (old, new) in (("summary_en", SUM_EN), ("summary_ar", SUM_AR), ("limitations_en", LIM_EN),
                              ("limitations_ar", LIM_AR), ("method_en", METH_EN), ("method_ar", METH_AR)):
        s.replace(F, "06_EVIDENCE_OBJECTS", t06.rows["CLM-001"], t06.col(field), old, new, f"CLM-001.{field}")
    s.replace_section(F, "/people/", 2, "en", "body", *PEOPLE_EN)
    s.replace_section(F, "/people/", 2, "ar", "body", *PEOPLE_AR)
    # the data row, before the currentness row of 25
    t25 = Table(s, "25_FINDEX_BASELINE", 4)
    if ROW[1] in t25.rows:
        raise TxError("25 already holds the context row")
    at = t25.rows["WB-FINDEX-CURRENTNESS-2025-001"]
    s.ed.insert_rows("25_FINDEX_BASELINE", at, [ROW])
    s.ledger.append(OrderedDict([("finding", F), ("sheet", "25_FINDEX_BASELINE"), ("row", at), ("col", None),
                                 ("field", ROW[1]), ("old", None), ("new", json.dumps(ROW, ensure_ascii=False))]))
    rep = s.save(out, ledger, OrderedDict([("transaction", "E2-3"), ("summary", "Same-source context: the World Bank's low-income aggregate for the same Findex wave (35.2%, 19 economies, Yemen included) beside Yemen's 11.9%")]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
