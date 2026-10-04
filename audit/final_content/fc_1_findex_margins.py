# -*- coding: utf-8 -*-
"""Final content pass, transaction FC-1: margins of error for every published Global Findex figure.

  python3 fc_1_findex_margins.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Finding FC-1:A1-MOE (owner message of 4 October 2026, block A). Edition 2 (E2-2) recorded that no interval could be
computed for Yemen's 2021-wave Findex figures because the respondent file needed a login, and left the public text
saying that the sampling uncertainty "is not quantified here". The owner supplied the file on 4 October 2026 under the
World Bank Microdata Research License, with the decision to publish aggregate statistics only. This transaction
quantifies the uncertainty and replaces that sentence in both languages.

METHOD (the CauseWay derivation this transaction records)
  Weighted point estimate, Hajek ratio estimator:   p  = sum(w_i y_i) / sum(w_i),  weight `wgt`
  Design-based variance by Taylor linearization:    SE = sqrt( sum( w_i^2 (y_i - p)^2 ) ) / sum(w_i)
  95% interval:                                     p +/- 1.959963985 * SE
The weight CV is 0.9023, so unequal weighting alone inflates variance by about 1.81 (Kish). The design effect of the
individual estimates runs from 0.82 to 1.82: for most of them a simple binomial standard error understates the
uncertainty, but for two small domains (the poorest 40% and ages 15-24) it slightly overstates it, so this record
states the range rather than claiming one direction. LIMIT, stated publicly: the public-use file carries the weight but
no PSU or stratum identifier, so clustering is not captured and the true interval may be wider, never narrower.

RECONCILIATION AGAINST THE PUBLISHED SOURCE (required before publishing; owner message, block A)
Every one of the nine published World Bank values for Yemen reproduces exactly from the respondent file, to the
unrounded value the World Bank itself publishes:
  account.t.d 11.9033656433415 | women 0.0543631 | men 0.1834518 | poorest 40% 0.0650494 | richest 60% 0.1549671
  primary or less 0.0698166 | secondary or more 0.1952705 | ages 15-24 0.0500996 | ages 25+ 0.1610805
  save.any.t.d 21.6445272422787 | borrow.any.t.d 51.2811034475895 | g20.any 9.33455931917802
There is no difference to record. Two method details were settled by that reconciliation and are recorded here because
they change the denominator a margin of error is computed on:
  (1) the World Bank's "ages 25+" group is the complement of ages 15-24 (n = 770): it carries the one respondent whose
      age is not recorded. Taking age >= 25 instead (n = 769) gives 0.1612575, which does not match the published
      value. The published base is used.
  (2) the `female` variable is coded 1 = female, 2 = male. The file's own value labels say so, and the resulting
      5.4% / 18.3% match the published female and male anchors exactly. The owner's hold on by-sex figures is
      therefore released on two independent confirmations, not one.

The respondent file never enters this repository, `dist/` or the site. This script reads it from a path given outside
the repository and is kept as the method record; it is not run by any gate.
"""
import json, os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "release_candidate"))
from rc_lib import Session, Table, TxError  # noqa: E402

F = "FC-1:A1-MOE"
S06 = "06_EVIDENCE_OBJECTS"
S25 = "25_FINDEX_BASELINE"
S28 = "28_METHODS_RIGHTS"

MICRO = "micro_yem.dta (YEM_2022_FINDEX_v01_M, 334,544 bytes)"
LOC = ("CauseWay derivation FC-1 from " + MICRO + ", held under the World Bank Microdata Research License and never "
       "redistributed; Hajek ratio estimator with Taylor-linearization variance on the survey weight wgt; the method, "
       "the point estimate, the interval, the base and the design effect of every figure are recorded in "
       "25_FINDEX_BASELINE rows CW-FINDEX-MOE-2022-*")
CAT = "https://microdata.worldbank.org/catalog/5862"
PUB = "CauseWay derivation from World Bank Global Findex 2021 Yemen microdata"
STATE = "CAUSEWAY_DERIVED_INTERVAL"
UNIT = "percentage points (95% margin of error, design-based)"

# group label -> (point %, MoE pp, low %, high %, n, design effect). Computed by the method above; see the module
# docstring for the reconciliation. Printed to one decimal place, the precision rule E2-2 set for every Findex figure.
ACC = OrderedDict([
    ("total",                       (11.9, 2.2,  9.7, 14.1, 1000, 1.16)),
    ("female",                      ( 5.4, 2.2,  3.2,  7.7,  500, 1.28)),
    ("male",                        (18.3, 3.7, 14.6, 22.1,  500, 1.21)),
    ("poorest 40%",                 ( 6.5, 2.4,  4.1,  8.9,  366, 0.93)),
    ("richest 60%",                 (15.5, 3.2, 12.3, 18.7,  634, 1.28)),
    ("primary education or less",   ( 7.0, 2.5,  4.5,  9.5,  430, 1.07)),
    ("secondary education or more", (19.5, 3.9, 15.7, 23.4,  569, 1.40)),
    ("ages 15-24",                  ( 5.0, 2.6,  2.5,  7.6,  230, 0.82)),
    ("ages 25+",                    (16.1, 3.1, 13.1, 19.2,  770, 1.38)),
])
GAPS = OrderedDict([
    ("sex: male minus female",                                       (12.9, 4.4,  8.5, 17.3)),
    ("income: richest 60% minus poorest 40%",                        ( 9.0, 4.0,  5.0, 13.0)),
    ("education: secondary or more minus primary or less",           (12.5, 4.6,  7.9, 17.1)),
    ("age: ages 25+ minus ages 15-24",                               (11.1, 4.0,  7.1, 15.1)),
])
# the other published Yemen 2022 indicators of the same wave, each reproduced exactly from the same file
OTHER = OrderedDict([
    ("account_fin",   ("Account at a financial institution", "fin_account_t_d", 11.9, 2.2,  9.7, 14.1, 1.16)),
    ("saved",         ("Saved any money in the past year",   "save.any.t.d",    21.6, 3.2, 18.4, 24.9, 1.58)),
    ("borrowed",      ("Borrowed any money in the past year", "borrow.any.t.d", 51.3, 4.2, 47.1, 55.5, 1.82)),
    ("anydigpayment", ("Made or received a digital payment",  "g20.any",          9.3, 1.9,  7.4, 11.3, 1.17)),
])

METHOD_NOTE = ("CauseWay derivation: Hajek ratio estimator with Taylor-linearization variance on the published survey "
               "weight (wgt) only. The public-use file carries no PSU or stratum identifier, so clustering is not "
               "captured and the true interval may be wider, never narrower. A simple binomial standard error is not "
               "used. The respondent file is held under the World Bank Microdata Research License and is never "
               "redistributed, committed to this repository or published.")


def baseline_rows():
    rows, n = [], 0
    for grp, (p, moe, lo, hi, base, deff) in ACC.items():
        n += 1
        rows.append({1: "CW-FINDEX-MOE-2022-%03d" % n, 2: "CW.MOE.ACCOUNT",
                     3: "Account ownership (any) - 95% margin of error", 4: grp, 5: "2022", 6: moe, 7: UNIT, 8: PUB,
                     9: CAT, 10: STATE,
                     11: ("Point estimate %.1f%%; 95%% confidence interval %.1f%% to %.1f%%; base %d respondents; "
                          "design effect %.2f. %s" % (p, lo, hi, base, deff, METHOD_NOTE))})
    for grp, (p, moe, lo, hi) in GAPS.items():
        n += 1
        rows.append({1: "CW-FINDEX-MOE-2022-%03d" % n, 2: "CW.MOE.ACCOUNT.GAP",
                     3: "Account ownership (any) - 95% margin of error of a measured difference", 4: grp, 5: "2022",
                     6: moe, 7: UNIT, 8: PUB, 9: CAT, 10: STATE,
                     11: ("Difference of the two printed shares %.1f points; 95%% confidence interval %.1f to %.1f "
                          "points. The two groups are disjoint samples, so the standard error of the difference is the "
                          "root of the sum of their squared standard errors. %s" % (p, lo, hi, METHOD_NOTE))})
    for var, (label, code, p, moe, lo, hi, deff) in OTHER.items():
        n += 1
        rows.append({1: "CW-FINDEX-MOE-2022-%03d" % n, 2: "CW.MOE." + var.upper(),
                     3: label + " - 95% margin of error", 4: "total", 5: "2022", 6: moe, 7: UNIT, 8: PUB, 9: CAT,
                     10: STATE,
                     11: ("Point estimate %.1f%%; 95%% confidence interval %.1f%% to %.1f%%; base 1,000 respondents; "
                          "design effect %.2f. Reproduces the World Bank's published unrounded value for Yemen 2022 "
                          "(indicator %s). %s" % (p, lo, hi, deff, code, METHOD_NOTE))})
    return rows


OLD_EN_002 = ("No standard errors or confidence intervals are published with these values; the Yemen sample is 1,000 "
              "respondents, so subgroup values and the gap carry sampling uncertainty that is not quantified here.")
NEW_EN_002 = ("The World Bank publishes no standard error or confidence interval with these values, so this resource "
              "derives them from the survey's own weights: on a sample of 1,000 respondents the 95% interval runs from "
              "3.2% to 7.7% for women and from 14.6% to 22.1% for men, and from 8.5 to 17.3 points for the gap. The "
              "file open to researchers carries no sampling-unit identifier, so clustering is not captured and the true "
              "intervals may be wider, never narrower.")
OLD_AR_002 = ("ولا تُنشر مع هذه القيم أخطاء معيارية أو فترات ثقة؛ وتبلغ عينة اليمن 1,000 مستجيب، لذلك تنطوي قيم الفئات "
              "الفرعية والفجوة بينها على عدم يقين ناتج عن المعاينة لا يُقدَّر كميًا هنا.")
NEW_AR_002 = ("ولا ينشر البنك الدولي مع هذه القيم خطأً معياريًا ولا فترة ثقة، لذلك يستخرجها هذا المورد من أوزان المسح "
              "نفسها: ففي عينة من 1,000 مستجيب تمتد فترة الثقة 95% من 3.2% إلى 7.7% للنساء، ومن 14.6% إلى 22.1% "
              "للرجال، ومن 8.5 إلى 17.3 نقطة للفجوة. ولا يحمل الملف المتاح للباحثين معرّف وحدة المعاينة، لذلك لا "
              "تُحتسب آثار التجمّع العنقودي، وقد تكون الفترات الحقيقية أوسع لا أضيق.")

OLD_EN_GAPS = ("No standard errors or confidence intervals are published with these values; the Yemen sample is 1,000 "
               "respondents, so subgroup values and the gaps carry sampling uncertainty that is not quantified here.")
NEW_EN_GAPS = ("The World Bank publishes no standard error or confidence interval with these values, so this resource "
               "derives them from the survey's own weights: on a sample of 1,000 respondents, and fewer in each group, "
               "the 95% margin of error is 2.2 points on the figure for all adults, between 2.2 and 3.9 points on each "
               "group's share, and between 4.0 and 4.6 points on each of the four differences. Each interval is printed "
               "with its figure on that figure's own record. The file open to researchers carries no sampling-unit "
               "identifier, so clustering is not captured and the true intervals may be wider, never narrower.")
OLD_AR_GAPS = ("ولا تُنشر مع هذه القيم أخطاء معيارية أو فترات ثقة؛ وتبلغ عينة اليمن 1,000 مستجيب، لذلك تنطوي قيم "
               "الفئات الفرعية والفجوات بينها على عدم يقين ناتج عن المعاينة لا يُقدَّر كميًا هنا.")
NEW_AR_GAPS = ("ولا ينشر البنك الدولي مع هذه القيم خطأً معياريًا ولا فترة ثقة، لذلك يستخرجها هذا المورد من أوزان المسح "
               "نفسها: ففي عينة من 1,000 مستجيب، وبعدد أقل في كل فئة، يبلغ هامش الخطأ عند ثقة 95% نحو 2.2 نقطة على "
               "القيمة الخاصة بجميع البالغين، وبين 2.2 و3.9 نقطة على نسبة كل فئة، وبين 4.0 و4.6 نقطة على كل فرق من "
               "الفروق الأربعة. وتُعرض كل فترة مع قيمتها في سجل تلك القيمة. ولا يحمل الملف المتاح للباحثين معرّف وحدة "
               "المعاينة، لذلك لا تُحتسب آثار التجمّع العنقودي، وقد تكون الفترات الحقيقية أوسع لا أضيق.")

# the method sentence each record adds, naming the derivation as this resource's own work
MADD_EN = (" The 95% intervals shown with these values are derived by this resource from the survey's own weights "
           "(a design-based interval for a weighted share), not published by the World Bank.")
MADD_AR = (" وفترات الثقة 95% المعروضة مع هذه القيم يستخرجها هذا المورد من أوزان المسح نفسها (فترة قائمة على تصميم "
           "المسح لنسبة موزونة)، ولم ينشرها البنك الدولي.")

METH_EN = ("Where it does not, no interval, standard error or significance test is added unless it can be reproduced "
           "from the survey's own weights and design.",
           "Where it does not, no interval, standard error or significance test is added unless it can be reproduced "
           "from the survey's own weights and design. For the Global Findex 2021 wave in Yemen this resource does "
           "reproduce it: the respondent file published for researchers carries the survey weight, so a 95% interval "
           "is derived for each published share by the design-based method for a weighted share, and shown with the "
           "figure. That file carries no sampling-unit identifier, so clustering is not captured and the derived "
           "intervals may be wider in reality, never narrower; the method and every interval are recorded with their "
           "figures, and the respondent file itself is never republished.")
METH_AR = ("وإذا لم ينشره فلا تُضاف فترة ثقة ولا خطأ معياري ولا اختبار دلالة ما لم يمكن إعادة احتسابها من أوزان المسح "
           "وتصميمه.",
           "وإذا لم ينشره فلا تُضاف فترة ثقة ولا خطأ معياري ولا اختبار دلالة ما لم يمكن إعادة احتسابها من أوزان المسح "
           "وتصميمه. وفي موجة Global Findex 2021 في اليمن يعيد هذا المورد احتسابها فعلًا: فملف المستجيبين المنشور "
           "للباحثين يحمل وزن المسح، ومن ثَمّ تُستخرج فترة ثقة 95% لكل نسبة منشورة بالطريقة القائمة على تصميم المسح "
           "لنسبة موزونة، وتُعرض مع القيمة. ولا يحمل ذلك الملف معرّف وحدة المعاينة، لذلك لا تُحتسب آثار التجمّع "
           "العنقودي وقد تكون الفترات المستخرجة أوسع في الواقع لا أضيق؛ والطريقة وكل فترة مسجّلتان مع قيمتهما، ولا "
           "يُعاد نشر ملف المستجيبين نفسه أبدًا.")

VS_002 = [("3.2%", "DERIVED"), ("7.7%", "DERIVED"), ("14.6%", "DERIVED"), ("22.1%", "DERIVED"),
          ("8.5", "DERIVED"), ("17.3", "DERIVED"), ("95%", "SITE")]
VS_GAPS = [("2.2", "DERIVED"), ("3.9", "DERIVED"), ("4.0", "DERIVED"), ("4.6", "DERIVED"), ("95%", "SITE")]


def add_states(s, t06, key, pairs):
    col = t06.col("value_states")
    cur = json.loads(s.ed.get_value(S06, t06.rows[key], col))
    have = {e["t"] for e in cur}
    new = list(cur)
    for tok, st in pairs:
        if tok in have:
            continue
        e = OrderedDict([("t", tok), ("k", "v"), ("s", st)])
        if st == "DERIVED":
            e["src"] = "SRC-WB-FINDEX-001"
            e["loc"] = LOC
        new.append(e)
    if len(new) == len(cur):
        return
    t06.set(F, key, "value_states", json.dumps(new, ensure_ascii=False, separators=(",", ":")),
            json.dumps(cur, ensure_ascii=False, separators=(",", ":")))


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    t06 = Table(s, S06, 4)

    # 1. the two records that carried "not quantified here"
    for key, (oe, ne, oa, na) in (("CLM-002", (OLD_EN_002, NEW_EN_002, OLD_AR_002, NEW_AR_002)),
                                  ("VIS-FINDEX-GAPS", (OLD_EN_GAPS, NEW_EN_GAPS, OLD_AR_GAPS, NEW_AR_GAPS))):
        s.replace(F, S06, t06.rows[key], t06.col("limitations_en"), oe, ne, key + ".limitations_en")
        s.replace(F, S06, t06.rows[key], t06.col("limitations_ar"), oa, na, key + ".limitations_ar")
        for fld, add in (("method_en", MADD_EN), ("method_ar", MADD_AR)):
            cur = s.ed.get_value(S06, t06.rows[key], t06.col(fld))
            if add.strip() in cur:
                continue
            t06.set(F, key, fld, cur.rstrip() + add, cur)
    add_states(s, t06, "CLM-002", VS_002)
    add_states(s, t06, "VIS-FINDEX-GAPS", VS_GAPS)

    # 2. the methodology page states the method
    s.replace_section(F, "/methodology/", 7, "en", "body", *METH_EN)
    s.replace_section(F, "/methodology/", 7, "ar", "body", *METH_AR)

    # 3. the derivation table
    t25 = Table(s, S25, 4)
    rows = baseline_rows()
    for r in rows:
        if r[1] in t25.rows:
            raise TxError("25 already holds " + r[1])
    at = t25.rows["WB-FINDEX-CURRENTNESS-2025-001"]
    s.ed.insert_rows(S25, at, rows)
    for r in rows:
        s.ledger.append(OrderedDict([("finding", F), ("sheet", S25), ("row", None), ("col", None), ("field", r[1]),
                                     ("old", None), ("new", json.dumps(r, ensure_ascii=False))]))

    # 4. rights and custody: the file is held, the publication rule is aggregate-only
    g28 = s.grid(S28)
    def r28(label, col, new, old):
        hits = [i for i, x in enumerate(g28, 1) if x and x[0] == label]
        if len(hits) != 1:
            raise TxError("%s: %r found %d times" % (S28, label, len(hits)))
        s.set(F, S28, hits[0], col, new, old, "%s.c%d" % (label, col))
    r28("data_file", 4,
        "Respondent microdata are held under the World Bank Microdata Research License for derivation only (owner "
        "decision of 4 October 2026). The file is never committed to this repository, to dist/ or to the site, and is "
        "never redistributed; only aggregate statistics derived from it are published.",
        "Respondent microdata are not yet held in the controlled evidence library.")
    r28("respondent_microdata_controlled", 2, "YES", "NO")
    r28("respondent_microdata_controlled", 4,
        "Weighted estimates derived from the respondent file are published as aggregate statistics only. Each is "
        "recorded as a CauseWay derivation with its method, base, point estimate, interval and design effect in "
        "25_FINDEX_BASELINE (rows CW-FINDEX-MOE-2022-*).",
        "Do not claim weighted microdata calculations have been completed.")
    r28("Findex microdata access state", 2,
        "Retrieved and held under the World Bank Microdata Research License; aggregate statistics only",
        "Login required for Yemen Findex microdata retrieval at the current catalog page")
    r28("Findex microdata access state", 4,
        "The catalog exposes metadata publicly and requires a login to retrieve the respondent-level file. That file "
        "was supplied to this programme on 4 October 2026 under the Microdata Research License; the Production Master "
        "records respondent_microdata_controlled=YES. Public indicators keep the World Bank's own published values; "
        "what this resource derives from the file is the 95% interval of each published share, labelled as its own "
        "derivation.",
        "The catalog exposes metadata publicly but requires login to retrieve the respondent-level file. The "
        "Production Master records respondent_microdata_controlled=NO; public indicators in this system are therefore "
        "not described as re-estimated from controlled respondent microdata.")
    r28("Findex microdata access state", 5,
        "The licence permits aggregate statistics with the dataset cited. It does not permit redistribution of the "
        "respondent file, any attempt to identify a respondent, or publication of a cell small enough to identify "
        "one. Counsel's confirmation of the licence text is a release-time formality and is recorded in the handover.",
        "If microdata are later acquired, verify the item-specific access category and terms before storage, analysis "
        "or redistribution.")

    # 5. the source record carries the licence and the required citation
    t15 = Table(s, "15_SOURCE_LIBRARY", 4)
    t15.set(F, "SRC-WB-FINDEX-001", "rights_state", "RESEARCH_LICENCE__AGGREGATE_STATISTICS_ONLY", "NOT_ASSESSED")
    t15.set(F, "SRC-WB-FINDEX-001", "licence", "World Bank Microdata Research License", None)
    t15.set(F, "SRC-WB-FINDEX-001", "attribution_requirement",
            "Demirguc-Kunt, A., Klapper, L., Singer, D., & Ansar, S. (2022). The Global Findex Database 2021: "
            "Financial Inclusion, Digital Payments, and Resilience in the Age of COVID-19. Washington, DC: World Bank.",
            None)

    rep = s.save(out, ledger, OrderedDict([
        ("transaction", "FC-1"),
        ("summary", "Design-based 95% margins of error for every published Global Findex figure for Yemen, derived "
                    "from the respondent file under the Microdata Research License; edition 2's \"not quantified "
                    "here\" replaced in both languages; the derivation, its method and the custody rule recorded")]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
