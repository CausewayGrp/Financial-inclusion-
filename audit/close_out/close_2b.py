# -*- coding: utf-8 -*-
"""Close-out transaction CLOSE-2B: the rest of Appendix A that needs an original (brief v5 W3b). English and Arabic
change together; the conditional Arabic register rows tied to these findings ride with them.

  python3 close_2b.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Writes <work_dir>/visual_design_contract.json, the controlled visual contract with the new remittance state, for
run_stage.py --install.

Read in the originals on 10 October 2026 (audit/close_out/w0/A2_imf_yem.md, A3_cby.md, A4_projects.md; re-checked here):
- CR-05 MATERIAL, CONFIRMED. IMF Country Report No. 26/80 (2025 Article IV), Annex IV "Statistical Enhancements ...",
  para 2, printed p.41: personal transfers were estimated with "a demographic and behavioral model—based on the number
  of Yemenis abroad, family size, and average transfer amounts— as well as the ratio of 33percent to the IRG controlled
  areas"; the 33 percent is the population ratio the mission applied "as proposed by the authorities" (footnote 2).
  Table 4 (printed p.31) prints the values, source "Yemeni Authorities; IMF Staff Calculations". The 2018-2024 values
  are therefore model-based estimates for areas under the internationally recognized government, not reported or
  observed history: relabelled everywhere (23_REMITTANCES state, geography and caveat; CLM-007; VIS-REMITTANCE-MACRO in
  06 and 11; /remittances/ s2; the evidence passport; the visual contract's state map). Values unchanged.
- CR-07 CONFIRMED. IMF press release, 7 October 2026 (pr26324): "IMF Management approved an 18-month non-financing
  Staff-Monitored Program (SMP) with Yemen"; SMPs "do not entail endorsement by the IMF Executive Board". The 16 July
  2026 release (pr26249), unreachable on 4 October, was re-read: "The proposed 18-month SMP ..."; "This staff-level
  agreement is subject to approval by IMF Management." New source SRC-IMF-YEM-SMP-2026-APPROVAL; CLM-049, /reforms/
  s7 and the July chronology event's value states updated (READ). The dated approval event is CLOSE-4's (brief W3d).
- CR-08 CONFIRMED. CR 26/80 Table 5 (printed p.31) prints financial soundness indicators 2014-Aug 2025, source
  "Yemeni Authorities; IMF Staff Calculations"; NPL to gross loans 0.0 for Dec-14..Dec-19, 58.5-60.8 after. The
  report says CBY began reporting a set of FSIs in 2025 (Annex V) and comprehensive FSI data are being compiled
  (para 35); its text (para 13) gives values for two other ratios that differ from Table 5. /finance/ s6 now states
  what the IMF publishes and its limits; the zeros are read as not reported; no bank is named; no ratio is charted.
- CR-09 TRACED. The untraced input of CLM-039, CLM-046 and CLM-056 is in each case an internal analytical dataset
  (DS-K04-REMIT-SOURCE-LENSES, DS-K04-SAUDI-SUPPORT-TRANSMISSION, DS-V041-STRICT-COUNSEL) that supplies no figure the
  record prints: every printed figure is READ from a listed source with a public locator, or is this resource's date.
  The dataset tokens leave the source dependencies; the records are BOUND_EXACT with the bound verification text.
- CR-11 CONFIRMED. SRC-CCY-PRESSURE-2026: the cover names the Cash Consortium of Yemen (with Crisis Analysis
  MENA/Europe; EU humanitarian funding); ReliefWeb carries it (posted 29 July 2026). It gets a public locator and a
  citation card; DS-QUAL-EVIDENCE keeps it.
- CR-13 CONFIRMED. SRC-CBY-PAYREPORT-H1-2025 p.1: 81/18/1 sit in the Accounts panel (5,202,019 accounts), 84/16 in
  the E-wallets panel (2,102,484 subscribers). IND-0018..0022 labels swapped back; locators name the panels.
- CR-15 CONFIRMED (wording). World Bank, Yemen Economic Monitor, Spring 2026, printed p.7: "the CBY has discontinued
  remittance data production". CBY-Aden's Annual Report 2025 still prints a 2025 remittance line; CLM-043 now says both.
- CR-16 CONFIRMED. OECD/INFE 2023: 42 is the printed label for Yemen in Figure 2.1 (p.14), 15 in Figure 4.1 (p.49);
  neither is read from a bar. Recorded in the value states of CLM-013 and VIS-FL-EVIDENCE-LADDER.
- CR-19 (D10). The 91% share of saver growth is in a secondary source only (Sana'a Center, 2024); no regulator or
  provider publication states it (search of 10 October 2026). CLM-056, its page description and the Reading that
  repeats it describe "one microfinance bank" and no longer name it.
- CR-20 CLOSED. The law's certified copy hosted by CBY-Aden (cby-ye.com/files/62c2edbaad8eb.pdf) is "Law No. (21) of
  2008"; Governor's Decision 6 of 2025 (head-office relocation to Aden) cites "Law No. (40) of 2008" in its recital.
  CON-038's hold is closed with both recorded.
- Register: AR-022, ED-035 and ED-036 take their new_ar and en_new as written: the bank list (A3, re-read 10 October
  2026) has no type column and no printed issue date, so neither condition's alternative applies. CLM-055 says the
  same as the sections it binds (one object, one state), and its count of 12 is DERIVED (by name), not READ.
"""
import json, os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from close_lib import (Session, Table, TxError, refresh_self_counts, register_rows, apply_register_ar,  # noqa: E402
                       apply_register_en)

F = "CLOSE-2B"
DATE = "10 October 2026"
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
CONTRACT = os.path.join(ROOT, "scripts", "projection", "controlled_inputs", "visual_design_contract.json")

# ------------------------------------------------------------------------------------------------ CR-05 remittances
ANNEX_LOC = ("IMF Country Report No. 26/80 (2025 Article IV consultation), Annex IV 'Statistical Enhancements with the "
             "Resumption of the 2025 Article IV Consultation with Yemen', para 2 'External Sector': population ratio "
             "allocating 33 percent to the IRG controlled areas (footnote 2: 'As proposed by the authorities'), and "
             "bullet 'Personal transfers': demographic and behavioral model (number of Yemenis abroad, family size, "
             "average transfer amounts) with the ratio of 33 percent to the IRG controlled areas; printed p.41 (PDF "
             "p.46); read 10 October 2026")
GEO_IRG = "Areas under the internationally recognized government (IMF allocation)"
IMF_ROWS_HIST = [f"RMO-IMF-{y}-HIST" for y in range(2018, 2025)]
CAV_EN_ADD = (" Not an observed or reported flow: estimated with a demographic and behavioural model (number of Yemenis "
              "abroad, family size, average transfer amounts); the value for areas under the internationally recognized "
              "government is 33% of the modelled total of personal transfers, by population ratio, as proposed by the "
              "authorities (IMF Country Report No. 26/80, Annex IV para 2, printed p.41; close-out CR-05, 10 October "
              "2026).")
CAV_AR_ADD = (" وليست تدفقًا مرصودًا أو مُبلَّغًا عنه: قُدِّرت بنموذج ديمغرافي وسلوكي (عدد اليمنيين في الخارج وحجم الأسرة "
              "ومتوسط مبالغ التحويل)؛ وتمثل القيمة الخاصة بالمناطق الخاضعة للحكومة المعترف بها دوليًا 33% من إجمالي "
              "التحويلات الشخصية المقدَّرة، وفق نسبة السكان، كما اقترحت السلطات (تقرير صندوق النقد الدولي القُطري رقم "
              "26/80، المرفق الرابع، الفقرة 2، ص 41؛ مراجعة الإغلاق CR-05، 10 أكتوبر 2026).")

METHOD_EN = ("Values as published by the IMF: 2018–2024 in the 2025 Article IV staff report (Table 4, external sector; "
             "sources given as the Yemeni authorities and IMF staff calculations), estimated with the demographic and "
             "behavioural model that the report's statistical annex (Annex IV) describes, and 2025–2030 in a later "
             "supplement to the same consultation (Supplementary Table 2).")
METHOD_AR = ("قيم كما نشرها صندوق النقد الدولي: 2018–2024 في تقرير الخبراء لمشاورات المادة الرابعة لعام 2025 (الجدول 4، "
             "القطاع الخارجي؛ والمصدر المذكور فيه: السلطات اليمنية وحسابات خبراء الصندوق)، وهي مقدَّرة بالنموذج "
             "الديمغرافي والسلوكي الذي يصفه المرفق الإحصائي للتقرير (المرفق الرابع)؛ و2025–2030 في ملحق لاحق للمشاورات "
             "نفسها (الجدول التكميلي 2).")

CLM007 = OrderedDict([
    ("title_en", ("reported history",
                  "IMF remittance series: model-based estimates, a later estimate and projections kept separate")),
    ("title_ar", ("القيم التاريخية المنشورة",
                  "سلسلة الحوالات لدى صندوق النقد الدولي: التقديرات القائمة على نموذج والتقدير اللاحق والتوقعات منفصلة")),
    ("summary_en", ("not reported values", (
        "In the IMF 2025 Article IV staff report, remittance inflows for 2018–2024 are estimates, not reported or "
        "observed flows: the report's statistical annex says personal transfers were estimated with a demographic and "
        "behavioural model (the number of Yemenis abroad, family size and average transfer amounts), with 33% allocated "
        "to areas under the internationally recognized government by population ratio. The 2024 estimate is higher than "
        "the 2018 estimate (both from the same document). The 2025 estimate and the 2026–2030 projections come from a "
        "later supplement. The IMF series covers areas under the internationally recognized government, so its level is "
        "not a whole-of-Yemen figure and is not comparable in level with the annual-report values of the Central Bank of "
        "Yemen – Aden (CBY-Aden)."))),
    ("summary_ar", ("لا قيم مُبلَّغ عنها", (
        "في تقرير خبراء صندوق النقد الدولي لمشاورات المادة الرابعة لعام 2025، قيم الحوالات الواردة للفترة 2018–2024 "
        "تقديرات، لا تدفقات مُبلَّغ عنها أو مرصودة: إذ يذكر المرفق الإحصائي للتقرير أن التحويلات الشخصية قُدِّرت بنموذج "
        "ديمغرافي وسلوكي (عدد اليمنيين في الخارج وحجم الأسرة ومتوسط مبالغ التحويل)، وأن 33% منها نُسبت إلى المناطق "
        "الخاضعة للحكومة المعترف بها دوليًا وفق نسبة السكان. وتقدير 2024 أعلى من تقدير 2018 (والقيمتان من الوثيقة "
        "نفسها). أما تقدير 2025 وتوقعات 2026–2030 فمصدرها ملحق لاحق. وتغطي سلسلة الصندوق المناطق الخاضعة للحكومة "
        "المعترف بها دوليًا، لذلك لا يمثل مستواها رقمًا لليمن كله، ولا يُقارن مستواها بقيم التقارير السنوية للبنك "
        "المركزي اليمني – عدن."))),
    ("definition_en", ("reported history for 2018–2024", (
        "Annual external-sector remittances, in US$ million, in the IMF series: model-based estimates for 2018–2024, an "
        "estimate for 2025 and projections for 2026–2030."))),
    ("definition_ar", ("قيم تاريخية للفترة 2018–2024", (
        "الحوالات السنوية في الحساب الخارجي بملايين الدولارات الأمريكية في سلسلة صندوق النقد الدولي: تقديرات قائمة على "
        "نموذج للفترة 2018–2024، وتقدير لعام 2025، وتوقعات للفترة 2026–2030."))),
    ("period_en", ("Reported history 2018–2024",
                   "Model-based estimates 2018–2024 (staff report); estimate 2025; projection 2026–2030")),
    ("period_ar", ("قيم تاريخية للفترة 2018–2024",
                   "تقديرات قائمة على نموذج للفترة 2018–2024 (تقرير الخبراء)؛ تقدير 2025؛ توقعات 2026–2030")),
    ("method_en", ("based on staff calculations (Table 4, external sector)", METHOD_EN)),
    ("method_ar", ("استنادًا إلى حسابات الخبراء (الجدول 4، القطاع الخارجي)", METHOD_AR)),
    ("currentness_en", ("The latest reported value is for 2024", (
        "The latest value in the staff-report series is the 2024 estimate. The 2025 value is an estimate and the "
        "2026–2030 values are projections; none of them is an observation. The 2024 value should not be read as a "
        "current level unless a newer comparable value is published."))),
    ("currentness_ar", ("آخر قيمة تاريخية واردة في المصدر هي لعام 2024", (
        "آخر قيمة في سلسلة تقرير الخبراء هي تقدير 2024. أما قيمة 2025 فتقدير، وقيم 2026–2030 توقعات، وليس أيٌّ منها "
        "مشاهدة. ولا تُقرأ قيمة 2024 على أنها مستوى حالي ما لم تُنشر قيمة أحدث قابلة للمقارنة."))),
])

VIS_SUMMARY_EN = (
    "For external-sector remittances, the IMF's 2025 Article IV staff report gives model-based estimates for 2018–2024, "
    "including US$1,861.7 million in 2024; the report's statistical annex says personal transfers were estimated with a "
    "demographic and behavioural model, with 33% allocated to areas under the internationally recognized government. A "
    "later supplement to the same consultation gives US$1,977 million as the 2025 estimate and projections rising from "
    "US$2,159 million in 2026 to US$3,110 million in 2030. The two documents were published at different times, so the "
    "two parts are not joined into one continuous series. The series covers the IMF's analytical scope for areas under "
    "the internationally recognized government, not the whole of Yemen.")
VIS_SUMMARY_AR = (
    "في سلسلة الحوالات الواردة في ميزان المدفوعات، يورد تقرير خبراء صندوق النقد الدولي لمشاورات المادة الرابعة لعام 2025 "
    "تقديرات قائمة على نموذج للفترة 2018–2024، منها 1,861.7 مليون دولار في 2024؛ ويذكر المرفق الإحصائي للتقرير أن "
    "التحويلات الشخصية قُدِّرت بنموذج ديمغرافي وسلوكي، وأن 33% منها نُسبت إلى المناطق الخاضعة للحكومة المعترف بها "
    "دوليًا. ويورد ملحق لاحق للمشاورات نفسها تقديرًا قدره 1,977 مليون دولار لعام 2025، وتوقعات ترتفع من 2,159 مليون "
    "دولار في 2026 إلى 3,110 مليون دولار في 2030. ولأن الوثيقتين صدرتا في وقتين مختلفين، لا يُوصل الجزءان في سلسلة "
    "واحدة متصلة. وتغطي السلسلة النطاق التحليلي للصندوق الخاص بالمناطق الخاضعة للحكومة المعترف بها دوليًا، لا اليمن "
    "كله.")
VIS_TITLE_EN = "Remittances — IMF estimates and projections, by source document"
VIS_TITLE_AR = "الحوالات: تقديرات صندوق النقد الدولي وتوقعاته بحسب الوثيقة المصدر"
VIS_UNIVERSE_EN = ("IMF external-sector remittance series on the IMF’s analytical scope for areas under the "
                   "internationally recognized government; each year labelled as an estimate or a projection, with its "
                   "source document")
VIS06 = OrderedDict([
    ("title_en", ("IMF-reported history", VIS_TITLE_EN)),
    ("title_ar", ("القيم التاريخية الواردة في تقارير", VIS_TITLE_AR)),
    ("summary_en", ("as reported history based on staff calculations", VIS_SUMMARY_EN)),
    ("summary_ar", ("بوصفها قيمًا تاريخية تستند إلى حسابات خبراء الصندوق", VIS_SUMMARY_AR)),
    ("definition_en", ("labelled as reported history (2018–2024)", (
        "Annual external-sector remittances, in US$ million, in the IMF series for 2018–2030, with each year labelled as "
        "a model-based estimate (2018–2024), an estimate (2025) or a projection (2026–2030)."))),
    ("definition_ar", ("بوصفها قيمة تاريخية (2018–2024)", (
        "الحوالات السنوية في القطاع الخارجي بملايين الدولارات الأمريكية في سلسلة صندوق النقد الدولي للفترة 2018–2030، مع "
        "وسم كل سنة بوصفها تقديرًا قائمًا على نموذج (2018–2024) أو تقديرًا (2025) أو توقعًا (2026–2030)."))),
    ("universe_en", ("labelled as reported history, estimate or projection", VIS_UNIVERSE_EN)),
    ("method_en", ("based on staff calculations (Table 4, external sector)", METHOD_EN)),
    ("method_ar", ("استنادًا إلى حسابات الخبراء (الجدول 4، القطاع الخارجي)", METHOD_AR)),
    ("currentness_en", ("Reported history runs to 2024", (
        "The staff report's model-based estimates run to 2024; 2025 is an estimate and 2026–2030 are projections from a "
        "later supplement. None of these values is an observation: the 2025–2030 values are not current evidence, and "
        "the 2024 value should not be read as a current level unless a newer comparable value is published."))),
    ("currentness_ar", ("تمتد القيم التاريخية الواردة في المصدر حتى 2024", (
        "تمتد التقديرات القائمة على نموذج في تقرير الخبراء حتى 2024؛ أما 2025 فتقدير، و2026–2030 توقعات من ملحق لاحق. "
        "وليس أيٌّ من هذه القيم مشاهدة: فقيم 2025–2030 ليست أدلة حالية، ولا تُقرأ قيمة 2024 على أنها مستوى حالي ما لم "
        "تُنشر قيمة أحدث قابلة للمقارنة."))),
])
VIS11 = OrderedDict([
    ("title_en", ("IMF-reported history", VIS_TITLE_EN)),
    ("title_ar", ("القيم التاريخية الواردة في تقارير", VIS_TITLE_AR)),
    ("visual_form", ("REPORTED_HISTORY", "TWO_SERIES_LINE__MODEL_ESTIMATE_VS_ESTIMATE_PROJECTION__VINTAGE_BREAK")),
    ("question_en", ("What does the IMF report for past remittance inflows",
                     "What does the IMF estimate for past remittance inflows, and what does it project?")),
    ("question_ar", ("ما الذي يورده صندوق النقد الدولي عن تدفقات الحوالات السابقة",
                     "ما الذي يقدّره صندوق النقد الدولي لتدفقات الحوالات السابقة، وما الذي يتوقعه؟")),
    ("what_it_shows_en", ("IMF-reported 2018–24 history", (
        "The IMF's model-based estimates for 2018–2024 are drawn apart from the 2025 estimate and the 2026–2030 projections, "
        "with a break where the source document changes."))),
    ("what_it_shows_ar", ("القيم الواردة في تقارير الصندوق", (
        "يفصل بصريًا بين تقديرات الصندوق القائمة على نموذج للفترة 2018–2024، وتقدير 2025، وتوقعات 2026–2030، مع انقطاع "
        "عند تغير الوثيقة المصدر."))),
    ("decision_value_en", ("Separates IMF-reported 2018–2024 values", (
        "Separates the IMF's model-based estimates for 2018–2024 from the 2025 estimate and 2026–2030 projections, and "
        "keeps the two IMF documents apart, so that neither a model estimate nor a forecast change is mistaken for an "
        "observed economic change."))),
    ("decision_value_ar", ("يفصل القيم التي يوردها صندوق النقد الدولي", (
        "يفصل تقديرات صندوق النقد الدولي القائمة على نموذج للفترة 2018–2024 عن تقدير 2025 وتوقعات 2026–2030، ويُبقي "
        "وثيقتي الصندوق منفصلتين، حتى لا يُقرأ تقديرٌ قائم على نموذج أو تغيرٌ في التوقع على أنه تغير اقتصادي مرصود."))),
    ("freshness_profile", ("reported history (staff report)",
                           "2018–2030: model-based estimates (staff report) / estimate and projections (supplement)")),
    ("denominator_universe", ("labelled as reported history, estimate or projection", VIS_UNIVERSE_EN)),
    ("encoding_contract", ("reported-history, estimate and projection states", (
        "Line with estimate and projection states visibly distinct by label and line treatment; the line breaks at the "
        "2024→2025 change of source document and both documents are labelled."))),
    ("accessible_summary_en", ("as reported history based on staff calculations", VIS_SUMMARY_EN)),
    ("accessible_summary_ar", ("بوصفها قيمًا تاريخية تستند إلى حسابات خبراء الصندوق", VIS_SUMMARY_AR)),
])
SITE_MAP = OrderedDict([
    (("/evidence/CLM-007/", "meta_description_en"), ("keep reported history", (
        "IMF figures for remittance inflows keep the model-based estimates for 2018–2024, the 2025 estimate and the "
        "2026–2030 projections separate; they are not a whole-of-Yemen figure."))),
    (("/evidence/CLM-007/", "meta_description_ar"), ("القيم التاريخية المنشورة", (
        "تفصل أرقام صندوق النقد الدولي للحوالات الواردة بين التقديرات القائمة على نموذج للفترة 2018–2024 وتقدير 2025 "
        "وتوقعات 2026–2030؛ ولا تمثل رقمًا لليمن كله."))),
    (("/evidence/VIS-REMITTANCE-MACRO/", "meta_description_en"), ("keep reported history for 2018–2024", (
        "IMF remittance figures for areas under Yemen's internationally recognized government keep model-based estimates "
        "for 2018–2024, a 2025 estimate and 2026–2030 projections apart."))),
    (("/evidence/VIS-REMITTANCE-MACRO/", "meta_description_ar"), ("القيم التاريخية للفترة 2018–2024", (
        "تفصل أرقام صندوق النقد الدولي للحوالات في المناطق الخاضعة للحكومة اليمنية المعترف بها دوليًا بين التقديرات "
        "القائمة على نموذج للفترة 2018–2024 وتقدير 2025 وتوقعات 2026–2030."))),
])
REMIT_S2 = [  # (lang, field, must_start, new)
    ("en", "heading", "Reported history, estimates and projections",
     "The IMF's past values are model-based estimates, not reported history"),
    ("en", "body", "The IMF staff report gives 2018–2024 as reported history", (
        "The IMF staff report gives 2018–2024 as estimates, not reported values: its statistical annex says personal "
        "transfers were estimated with a demographic and behavioural model (the number of Yemenis abroad, family size and "
        "average transfer amounts), with 33% allocated to areas under the internationally recognized government. A later "
        "supplement to the same consultation gives 2025 as an estimate and 2026–2030 as projections. The series is kept "
        "apart where the source document changes, and none of its years is an observation. A forecast revision is not an "
        "observed economic change, and the macro series is not a measure of informal hawala volume.")),
    ("ar", "heading", "القيم التاريخية المنشورة والتقديرات والتوقعات",
     "القيم السابقة لدى صندوق النقد الدولي تقديرات قائمة على نموذج، لا قيم تاريخية مُبلَّغ عنها"),
    ("ar", "body", "يورد تقرير خبراء صندوق النقد قيم 2018–2024 بوصفها قيمًا تاريخية", (
        "يورد تقرير خبراء صندوق النقد قيم 2018–2024 بوصفها تقديرات، لا قيمًا مُبلَّغًا عنها: إذ يذكر مرفقه الإحصائي أن "
        "التحويلات الشخصية قُدِّرت بنموذج ديمغرافي وسلوكي (عدد اليمنيين في الخارج وحجم الأسرة ومتوسط مبالغ التحويل)، "
        "وأن 33% منها نُسبت إلى المناطق الخاضعة للحكومة المعترف بها دوليًا. ويورد ملحق لاحق للمشاورات نفسها قيمة 2025 "
        "كتقدير وقيم 2026–2030 كتوقعات. وتُفصل السلسلة عند تغير الوثيقة المصدر، وليس أيٌّ من سنواتها مشاهدة. مراجعة "
        "التوقع ليست تغيرًا اقتصاديًا مرصودًا، كما أن سلسلة الحوالات الكلية لا تقيس حجم التحويلات عبر نظام الحوالة غير "
        "الرسمي.")),
]
PASSPORT_REMIT = OrderedDict([
    ("reference_period", ("Reported history 2018–2024",
                          "Model-based estimates 2018–2024 (staff report); estimate 2025; projection 2026–2030")),
    ("method", ("Source-reported/staff calculations",
                "Source-published estimates: a demographic and behavioural model with a 33% allocation to areas under the "
                "internationally recognized government (IMF CR 26/80, Annex IV); supplement estimate and projections")),
    ("display_requirements", ("Reported-history, estimate and projection states",
                              "Estimate and projection states must be visually distinct, and the line breaks where the "
                              "source document changes.")),
])

# ------------------------------------------------------------------------------------------------ CR-07 SMP
URL_JUL = "https://www.imf.org/en/news/articles/2026/07/16/pr26249-yemen-imf-reaches-sla-on-new-staff-monitored-program"
URL_OCT = "https://www.imf.org/en/news/articles/2026/10/07/pr26324-imf-management-approves-a-staff-monitored-program-with-yemen"
SRC_OCT = "SRC-IMF-YEM-SMP-2026-APPROVAL"
LOC_JUL = ("IMF press release 'IMF Reaches Staff-Level Agreement with Yemen on a New Staff-Monitored Program', published "
           "16 July 2026 (" + URL_JUL.replace("https://", "") + "): 'The proposed 18-month SMP aims to ...'; 'This "
           "staff-level agreement is subject to approval by IMF Management.'; '... the mission will not result in a Board "
           "discussion ...'; mission in Amman, 5-16 July 2026; read 10 October 2026 (WebFetch; curl refused)")
LOC_OCT = ("IMF press release 'IMF Management Approves a Staff-Monitored Program with Yemen', published 7 October 2026 ("
           + URL_OCT.replace("https://", "") + "): 'IMF Management approved an 18-month non-financing Staff-Monitored "
           "Program (SMP) with Yemen'; SMPs 'are informal agreements between national authorities and IMF staff and do "
           "not entail endorsement by the IMF Executive Board'; read 10 October 2026 (WebFetch; curl refused)")
SRC_OCT_ROW = OrderedDict([
    ("source_id", SRC_OCT),
    ("primary_url", URL_OCT),
    ("datasets_or_use", "DS-V4R3-SYSTEM-CHRONOLOGY"),
    ("row_count", 1),
    ("display_title", "Yemen: IMF Management approves a Staff-Monitored Program (7 October 2026)"),
    ("display_title_ar", "اليمن: إدارة صندوق النقد الدولي توافق على برنامج يراقبه خبراء الصندوق (7 أكتوبر 2026)"),
    ("publisher", "International Monetary Fund"),
    ("publisher_ar", "صندوق النقد الدولي"),
    ("public_card_state", "CITATION_CARD"),
    ("rights_state", "NOT_ASSESSED"),
    ("retrieval_date", "2026-10-10"),
    ("document_label", "News release"),
    ("document_label_ar", "بيان صحفي"),
    ("document_date", "2026-10-07"),
])
CLM049 = OrderedDict([
    ("title_en", "IMF Staff-Monitored Program (SMP) for Yemen: approved by IMF Management on 7 October 2026, with no IMF "
                 "financing"),
    ("title_ar", "البرنامج الذي يراقبه خبراء صندوق النقد الدولي (SMP) لليمن: وافقت عليه إدارة الصندوق في 7 أكتوبر 2026، من "
                 "دون تمويل من الصندوق"),
    ("summary_en", "On 7 October 2026, the International Monetary Fund (IMF) announced that IMF Management had approved an "
                   "18-month non-financing Staff-Monitored Program (SMP) with Yemen. This follows the staff-level agreement "
                   "that IMF staff and the Yemeni authorities announced on 16 July 2026, which was then subject to "
                   "Management approval. The IMF describes SMPs as informal agreements between national authorities and IMF "
                   "staff that do not entail endorsement by the IMF Executive Board; the programme provides no IMF "
                   "financing."),
    ("summary_ar", "في 7 أكتوبر 2026 أعلن صندوق النقد الدولي أن إدارة الصندوق وافقت على برنامج يراقبه خبراء الصندوق (SMP) "
                   "مع اليمن، مدته 18 شهرًا ولا يتضمن تمويلًا. ويأتي ذلك بعد الاتفاق على مستوى الخبراء الذي أعلنه خبراء "
                   "الصندوق والسلطات اليمنية في 16 يوليو 2026، والذي كان حينها خاضعًا لموافقة الإدارة. ويصف الصندوق هذه "
                   "البرامج بأنها اتفاقات غير رسمية بين السلطات الوطنية وخبراء الصندوق لا تتضمن تأييدًا من المجلس التنفيذي "
                   "للصندوق؛ ولا يقدم البرنامج تمويلًا من الصندوق."),
    ("definition_en", "The approval status of the 18-month Staff-Monitored Program (SMP) of the International Monetary Fund "
                      "(IMF) with Yemen, as announced by the IMF on 16 July 2026 (staff-level agreement) and on 7 October "
                      "2026 (Management approval)."),
    ("definition_ar", "وضع الموافقة على البرنامج الذي يراقبه خبراء صندوق النقد الدولي (SMP) مع اليمن ومدته 18 شهرًا، كما "
                      "أعلنه الصندوق في 16 يوليو 2026 (اتفاق على مستوى الخبراء) وفي 7 أكتوبر 2026 (موافقة الإدارة)."),
    ("period_en", "16 July 2026 (staff-level agreement); 7 October 2026 (approval by IMF Management); an 18-month "
                  "programme."),
    ("period_ar", "16 يوليو 2026 (اتفاق على مستوى الخبراء)؛ 7 أكتوبر 2026 (موافقة إدارة صندوق النقد الدولي)؛ برنامج مدته "
                  "18 شهرًا."),
    ("universe_en", "The Staff-Monitored Program (SMP) agreed between IMF staff and the Yemeni authorities and approved by "
                    "IMF Management; not an Executive Board-approved financing arrangement."),
    ("universe_ar", "البرنامج الذي يراقبه خبراء صندوق النقد الدولي (SMP) المتفق عليه بين خبراء الصندوق والسلطات اليمنية، "
                    "والذي وافقت عليه إدارة الصندوق؛ وليس ترتيب تمويل معتمدًا من المجلس التنفيذي."),
    ("method_en", "The status is taken from the wording of two press releases of the International Monetary Fund (IMF), "
                  "read in the original on 10 October 2026: 16 July 2026 (staff-level agreement, subject to IMF Management "
                  "approval, with no Board discussion) and 7 October 2026 (IMF Management approval of an 18-month "
                  "non-financing SMP)."),
    ("method_ar", "يؤخذ وضع البرنامج من نص بيانين صحفيين لصندوق النقد الدولي قُرئا في الأصل في 10 أكتوبر 2026: بيان 16 "
                  "يوليو 2026 (اتفاق على مستوى الخبراء، يخضع لموافقة إدارة الصندوق، من دون نقاش في المجلس التنفيذي)، وبيان "
                  "7 أكتوبر 2026 (موافقة إدارة الصندوق على برنامج مدته 18 شهرًا لا يتضمن تمويلًا)."),
    ("limitations_en", "The Staff-Monitored Program (SMP) is not an arrangement approved or endorsed by the Executive Board "
                       "of the International Monetary Fund (IMF) and does not involve IMF financing. Its approval does not "
                       "show that the reforms have been implemented or that they have changed financial inclusion, and it "
                       "is not evidence that external-sector statistics have been reconciled."),
    ("limitations_ar", "ليس البرنامج الذي يراقبه خبراء صندوق النقد الدولي (SMP) ترتيبًا معتمدًا أو مؤيدًا من المجلس التنفيذي "
                       "للصندوق، ولا ينطوي على تمويل من الصندوق. ولا تثبت الموافقة عليه أن الإصلاحات نُفذت أو أنها غيّرت "
                       "الشمول المالي، كما أنها ليست دليلًا على اكتمال مطابقة إحصاءات القطاع الخارجي."),
    ("currentness_en", "The latest information in this record is the IMF announcement of 7 October 2026 that IMF Management "
                       "approved the programme. It should not be read as describing the programme's progress or reviews at "
                       "a later date unless a newer IMF notice is published."),
    ("currentness_ar", "أحدث معلومة في هذا السجل هي إعلان صندوق النقد الدولي في 7 أكتوبر 2026 أن إدارة الصندوق وافقت على "
                       "البرنامج. ولا يُقرأ على أنه يصف تقدم البرنامج أو مراجعاته في تاريخ لاحق ما لم يُنشر إشعار أحدث من "
                       "الصندوق."),
])
CLM049_VS = [
    {"t": "16 July 2026", "k": "d", "s": "READ", "src": "SRC-IMF-YEM-SMP-2026", "loc": LOC_JUL},
    {"t": "16", "k": "v", "s": "READ", "src": "SRC-IMF-YEM-SMP-2026", "loc": LOC_JUL},
    {"t": "July 2026", "k": "d", "s": "READ", "src": "SRC-IMF-YEM-SMP-2026", "loc": LOC_JUL},
    {"t": "7 October 2026", "k": "d", "s": "READ", "src": SRC_OCT, "loc": LOC_OCT},
    {"t": "October 2026", "k": "d", "s": "READ", "src": SRC_OCT, "loc": LOC_OCT},
    {"t": "7", "k": "v", "s": "READ", "src": SRC_OCT, "loc": LOC_OCT},
    {"t": "18", "k": "v", "s": "READ", "src": SRC_OCT, "loc": LOC_OCT},
    {"t": "18-month", "k": "v", "s": "READ", "src": SRC_OCT, "loc": LOC_OCT},
    {"t": "10 October 2026", "k": "d", "s": "SITE"},
]
REFORMS_S7 = [
    ("en", "heading", "The July 2026 SMP agreement is staff-level and conditional",
     "IMF Management approved an 18-month Staff-Monitored Program in October 2026; it is not IMF financing"),
    ("en", "body", "On 16 July 2026, IMF staff and Yemeni authorities announced", (
        "On 16 July 2026, IMF staff and the Yemeni authorities announced staff-level agreement on policies and reforms "
        "that could underpin a proposed 18-month Staff-Monitored Program (SMP), subject to IMF Management approval. On 7 "
        "October 2026, the IMF announced that IMF Management had approved an 18-month non-financing SMP with Yemen. The "
        "IMF describes SMPs as informal agreements between national authorities and IMF staff that do not entail "
        "endorsement by its Executive Board. The programme is not an IMF financing arrangement, and its approval does not "
        "show that reforms have been implemented or that financial inclusion has changed.")),
    ("ar", "heading", "وضع البرنامج الذي يراقبه خبراء صندوق النقد الدولي (SMP) في يوليو 2026",
     "وافقت إدارة صندوق النقد الدولي في أكتوبر 2026 على برنامج يراقبه خبراء الصندوق مدته 18 شهرًا، ولا يتضمن تمويلًا من "
     "الصندوق"),
    ("ar", "body", "في 16 يوليو 2026 أعلن خبراء صندوق النقد والسلطات اليمنية", (
        "في 16 يوليو 2026 أعلن خبراء صندوق النقد والسلطات اليمنية اتفاقًا على مستوى الخبراء بشأن سياسات وإصلاحات يمكن أن "
        "يستند إليها برنامج مقترح يراقبه خبراء صندوق النقد الدولي (SMP) مدته 18 شهرًا، رهنًا بموافقة إدارة الصندوق. وفي 7 "
        "أكتوبر 2026 أعلن الصندوق أن إدارته وافقت على برنامج يراقبه خبراء الصندوق مع اليمن، مدته 18 شهرًا ولا يتضمن "
        "تمويلًا. ويصف الصندوق هذه البرامج بأنها اتفاقات غير رسمية بين السلطات الوطنية وخبراء الصندوق لا تتضمن تأييدًا من "
        "مجلسه التنفيذي. وليس البرنامج ترتيب تمويل من الصندوق، ولا تثبت الموافقة عليه أن الإصلاحات نُفذت أو أن الشمول "
        "المالي تغيّر.")),
]
CLM049_META = OrderedDict([
    ("meta_description_en", ("On 16 July 2026 IMF staff",
                             "On 7 October 2026 IMF Management approved an 18-month Staff-Monitored Program with Yemen; "
                             "it provides no IMF financing and is not Executive Board approval.")),
    ("meta_description_ar", ("في 16 يوليو 2026 أعلن خبراء",
                             "في 7 أكتوبر 2026 وافقت إدارة صندوق النقد الدولي على برنامج يراقبه خبراء الصندوق مع اليمن "
                             "مدته 18 شهرًا؛ ولا يقدم تمويلًا من الصندوق، وليس موافقة من المجلس التنفيذي.")),
])

FIN_S2_EN_OLD = "it does not interpolate the missing months or estimate a causal conflict effect."
FIN_S2_EN_ADD = (" Its starting point is dated in two ways: 1997, when the Social Fund for Development (SFD) was established, "
                 "and 1998, when SFD began operations and became active in microfinance. The SFD terms of reference that "
                 "date the start of microfinance to 1997 could not be re-opened (on 4 October 2026, and again on 10 "
                 "October 2026), so that dating has not been re-read in the original for this edition.")
FIN_S2_AR_OLD = "ولا يستكمل الأشهر المفقودة بالاستيفاء ولا يقدّر أثرًا سببيًا للنزاع."
FIN_S2_AR_ADD = (" ويؤرَّخ منطلقه بطريقتين: عام 1997، حين أُنشئ الصندوق الاجتماعي للتنمية، وعام 1998، حين بدأ الصندوق "
                 "عملياته وأصبح ناشطًا في التمويل الأصغر. أما الشروط المرجعية للصندوق التي تؤرخ بداية التمويل الأصغر بعام "
                 "1997 فتعذّرت إعادة فتحها (في 4 أكتوبر 2026، ثم في 10 أكتوبر 2026)، فلم تُعَد في هذا الإصدار قراءةُ هذا "
                 "التأريخ في الأصل.")

# ------------------------------------------------------------------------------------------------ CR-08 NPL (/finance/ s6)
NPL_EN_OLD = ("The current evidence base does not yet contain a harmonized, publication-ready set of non-performing-loan, "
              "capital-adequacy and liquidity ratios with common definitions and vintages.")
NPL_EN_NEW = (
    "The IMF's 2025 Article IV staff report does publish one set of financial soundness indicators for Yemen, sourced "
    "to the Yemeni authorities and IMF staff calculations, including the ratio of non-performing loans to total gross "
    "loans at each year-end from 2014 to 2024 and at one date in 2025. For each year-end from 2014 to 2019 that ratio "
    "is printed as zero, which this resource reads as not reported, not as zero. The table does not state which banks "
    "or areas it covers; the report says that the central bank began reporting a set of these indicators in 2025 and "
    "that comprehensive data are still being compiled, and its own text gives values for two other ratios that differ "
    "from the table. One published vintage of unstated coverage is not yet a harmonized series with common "
    "definitions, so this resource does not present these ratios as a series.")
NPL_AR_OLD = ("ولا تتضمن قاعدة الأدلة بعدُ مجموعة منسجمة وجاهزة للنشر لمؤشرات القروض المتعثرة وكفاية رأس المال والسيولة "
              "بتعريفات ونسخ زمنية قابلة للمقارنة.")
NPL_AR_NEW = (
    "ويَنشر تقرير خبراء صندوق النقد الدولي لمشاورات المادة الرابعة لعام 2025 مجموعةً واحدة من مؤشرات السلامة المالية "
    "لليمن، مصدرها السلطات اليمنية وحسابات خبراء الصندوق، ومنها نسبة القروض المتعثرة إلى إجمالي القروض في نهاية كل سنة "
    "من 2014 إلى 2024 وفي تاريخ واحد من 2025. وتَرِد هذه النسبة صفرًا في نهاية كل سنة من 2014 إلى 2019، ويقرأ هذا "
    "المورد تلك القيم على أنها غير مُبلَّغ عنها، لا على أنها صفر. ولا يحدد الجدول البنوك أو المناطق التي يغطيها؛ ويذكر "
    "التقرير أن البنك المركزي بدأ الإبلاغ عن مجموعة من هذه المؤشرات في 2025 وأن البيانات الشاملة ما تزال قيد التجميع، "
    "كما يورد متنُه لنسبتين أخريين قيمًا تختلف عما في الجدول. ولا تشكّل نسخةٌ منشورة واحدة غير محددة النطاق سلسلةً "
    "منسجمة بتعريفات موحدة بعد، لذلك لا يعرض هذا المورد هذه النسب في صورة سلسلة.")

# ------------------------------------------------------------------------------------------------ CR-13 payments shares
IND_LABELS = OrderedDict([   # 17_INDICATOR_LIBRARY row -> (indicator id, old label, new label)
    (70, ("IND-0018", "E-wallet subscribers — male share", "Accounts — male share")),
    (71, ("IND-0019", "E-wallet subscribers — female share", "Accounts — female share")),
    (72, ("IND-0020", "E-wallet subscribers — company share", "Accounts — company share")),
    (73, ("IND-0021", "Bank accounts — male share", "E-wallet subscribers — male share")),
    (74, ("IND-0022", "Bank accounts — female share", "E-wallet subscribers — female share")),
])
PAY_LOC_ACC = ("page 1, «الحسابات» (Accounts) panel, bottom left (NO. of Accounts 5,202,019): bars ذكر 81% / أنثى 18% / "
               "شركات 1%, caption «نسبة عدد المواطنين الذين يمتلكون حسابات بنكية وفق النوع»; re-read 10 October 2026 "
               "(close-out CR-13)")
PAY_LOC_EW = ("page 1, «المحافظ الإلكترونية» (E-wallets) panel, bottom right (NO. of Subscribers 2,102,484): donut 84% "
              "male / 16% female, caption «نسبة عدد المشتركين وفق النوع»; re-read 10 October 2026 (close-out CR-13)")
PAY_LOCS = OrderedDict([("OBS-00038", PAY_LOC_ACC), ("OBS-00039", PAY_LOC_ACC), ("OBS-00040", PAY_LOC_ACC),
                        ("OBS-00041", PAY_LOC_EW), ("OBS-00042", PAY_LOC_EW)])

# ------------------------------------------------------------------------------------------------ CR-15 CLM-043
WB_YEM_SRC = "SRC-WB-YEM-ECON-MONITOR-2026-SPRING-001"
WB_YEM_PDF = ("https://documents1.worldbank.org/curated/en/099630405192627146/pdf/"
              "IDU-915b334e-33e9-407b-b634-2ee6167b4790.pdf")
CLM043_CUR_EN_ADD = (" The World Bank's Yemen Economic Monitor, Spring 2026, states that “the CBY has discontinued "
                     "remittance data production”, without saying which series or publication it means; the CBY-Aden "
                     "Annual Report 2025 used here still prints a remittance line for 2025, and whether that line will "
                     "continue is not established.")
CLM043_CUR_AR_ADD = (" ويذكر المرصد الاقتصادي لليمن الصادر عن البنك الدولي (ربيع 2026) أن البنك المركزي اليمني توقف عن إنتاج "
                     "بيانات الحوالات، من دون أن يحدد السلسلة أو المنشور المقصود؛ ولا يزال التقرير السنوي 2025 للبنك "
                     "المركزي اليمني – عدن المستخدم هنا يورد بند الحوالات لعام 2025، ولم يثبت ما إذا كان هذا البند سيستمر.")

# ------------------------------------------------------------------------------------------------ CR-16 INFE labels
INFE_LOC_ADD = {
    "15": ("; the same value is printed as Yemen's data label in Figure 4.1 'Financial well-being' of the report (p. 49) "
           "— a printed label, not read from the bar; re-read 10 October 2026 (close-out CR-16)"),
    "42": ("; the same value is printed as Yemen's data label in Figure 2.1 'Overall financial literacy, average scores "
           "(out of 100)' of the report (p. 14) — a printed label, not read from the bar; re-read 10 October 2026 "
           "(close-out CR-16)"),
}

# ------------------------------------------------------------------------------------------------ CR-20 CON-038
CON038 = OrderedDict([   # 33_ANALYTICS_MASTER row 128: col -> (old prefix, new)
    (4, ("CBY lists/hosts the law",
         "Law No. (21) of 2008 on the Bank Deposit Guarantee Institution: certified copy (Ministry of Legal Affairs) "
         "hosted by CBY-Aden, https://cby-ye.com/files/62c2edbaad8eb.pdf, p.1 title, p.12 signature (Sana'a, 23 April "
         "2008). Governor's Decision No. (6) of 2025 (relocating the Institution's head office to Aden; signed 20 July "
         "2025; https://cby-ye.com/files/687c9970b82d9.pdf, p.1) cites 'Law No. (40) of 2008' in its recital. Earlier "
         "registers: Ministry of Justice registry No. 21/2008; another government legal library No. 40/2008.")),
    (5, ("CROSS_GOVERNMENT_LEGAL_IDENTITY_CONFLICT", "RESOLVED__LAW_NO_21_OF_2008__RECITAL_DISCREPANCY_RECORDED")),
    (6, ("HOLD_DEFINITIVE_LAW_NUMBER", "CLOSED__READ_IN_ORIGINAL_2026-10-10 (close-out CR-20)")),
    (7, ("Existence may be stated",
         "The law may be cited as Law No. 21 of 2008, with the certified copy as locator. Decision No. 6 of 2025 relocates "
         "the Institution's head office to Aden; it does not establish the Institution. The recital's 'No. 40' is a "
         "discrepancy in that decision, not a second law.")),
])

# ------------------------------------------------------------------------------------------------ CR-09 / CR-19
UNTRACED = OrderedDict([("CLM-039", "DS-K04-REMIT-SOURCE-LENSES"), ("CLM-046", "DS-K04-SAUDI-SUPPORT-TRANSMISSION"),
                        ("CLM-056", "DS-V041-STRICT-COUNSEL")])
CLM056 = OrderedDict([
    ("summary_en", ("attributes 91% to Al-Kuraimi's share of saver growth", (
        "The 2024 Sana’a Center paper on microfinance banks attributes 91% of saver growth to one microfinance bank; the "
        "2023 provider-level numerator, denominator and calculation have not been reproduced, and a search on 10 October "
        "2026 found no publication of the regulator or of the bank that states the figure. A 2025 Yemen Review restates "
        "91% as a share of active microfinance depositors. A share of growth and a share of the stock are different "
        "measures, so the 2025 stock-share wording is not supported by the evidence available here; it remains a "
        "secondary restatement pending primary 2023 provider data or an explicit source correction. Because no primary "
        "public source states the figure, this resource does not name the bank."))),
    ("summary_ar", ("إلى الكريمي 91% من نمو المدخرين", (
        "تنسب ورقة مركز صنعاء لعام 2024 عن بنوك التمويل الأصغر إلى بنك واحد للتمويل الأصغر 91% من نمو المدخرين، ولم "
        "يُعَد إنتاج البسط وقاعدة الاحتساب والحساب على مستوى مقدمي الخدمة لعام 2023، ولم يعثر بحثٌ أُجري في 10 أكتوبر 2026 "
        "على منشور للجهة الرقابية أو للبنك نفسه يورد هذه النسبة. وفي 2025 أعاد تقرير «Yemen Review» عرض نسبة 91% بوصفها "
        "حصة من المودعين النشطين في التمويل الأصغر. وحصة النمو وحصة الرصيد مقياسان مختلفان، لذلك لا تسند الأدلة المتاحة "
        "هنا صياغة 2025 بوصفها حصة من الرصيد، وتظل إعادة عرض ثانوية إلى أن تتاح بيانات أصلية لعام 2023 على مستوى مقدمي "
        "الخدمة أو يصدر تصحيح صريح من المصدر. ولأن النسبة لا ترد في مصدر عام أصلي، لا يسمّي هذا المورد البنك."))),
    ("definition_en", ("attributes to Al-Kuraimi", (
        "The 91% share of growth in microfinance savers that a 2024 policy paper attributes to one microfinance bank; the "
        "2023 provider-level numerator, denominator and calculation behind it have not been reproduced."))),
    ("definition_ar", ("إلى الكريمي", (
        "نسبة 91% من نمو المدخرين في التمويل الأصغر التي تنسبها ورقة سياسات منشورة في 2024 إلى بنك واحد للتمويل الأصغر؛ "
        "ولم يُعَد إنتاج البسط وقاعدة الاحتساب والحساب على مستوى مقدمي الخدمة لعام 2023 الذي تستند إليه."))),
])
CLM056_META = OrderedDict([
    ("meta_description_en", ("to Al-Kuraimi", "A 2024 Sana’a Center paper attributes 91% of saver growth to one "
                                              "microfinance bank; the figure is not a verified 2023 depositor stock share.")),
    ("meta_description_ar", ("إلى الكريمي", "تنسب ورقة مركز صنعاء لعام 2024 إلى بنك واحد للتمويل الأصغر 91% من نمو "
                                           "المدخرين؛ وليست هذه حصة محققة من رصيد المودعين في 2023.")),
])
MF_READING = "/readings/microfinance-structural-divergence/"
MF_READING_EDITS = [   # (lang, old, new)
    ("en", "over the period it analyses to Al-Kuraimi.", "over the period it analyses to one microfinance bank."),
    ("ar", "خلال الفترة التي تحللها إلى بنك الكريمي.", "خلال الفترة التي تحللها إلى بنك واحد للتمويل الأصغر."),
]

# ------------------------------------------------------------------------------------------------ CR-11 CCY pressure
CCY = "SRC-CCY-PRESSURE-2026"
CCY_SET = OrderedDict([
    ("primary_url", "https://reliefweb.int/report/yemen/yemen-under-pressure-how-iran-us-conflict-disrupting-trade-prices-"
                    "and-cash-access-may-2026"),
    ("additional_urls", json.dumps(["https://reliefweb.int/attachments/329ba888-6c77-46c3-b920-e0ca0d5ab982/Economic%20"
                                    "Impact%20of%20Iran-US%20War%20on%20Yemen_May%202026.pdf"])),
    ("display_title", "Yemen Under Pressure: How the Iran-US Conflict Is Disrupting Trade, Prices, and Cash Access (May "
                      "2026)"),
    ("display_title_ar", "اليمن تحت الضغط: كيف يُخلّ الصراع بين إيران والولايات المتحدة بالتجارة والأسعار والوصول إلى النقد "
                         "(مايو 2026)"),
    ("publisher", "Cash Consortium of Yemen (CCY)"),
    ("publisher_ar", "Cash Consortium of Yemen (CCY)"),
    ("issuer", "Cash Consortium of Yemen, with Crisis Analysis MENA/Europe (cover)"),
    ("hosting_platform", "ReliefWeb"),
    ("public_card_state", "CITATION_CARD"),
    ("non_public_locator_note", None),
    ("retrieval_date", "2026-10-10"),
    ("document_label", "Research or policy paper"),
    ("document_label_ar", "ورقة بحثية أو سياساتية"),
    ("document_date", "2026-05"),
])

# ------------------------------------------------------------------------------------------------ register + CLM-055
REG_EN_START = {
    "ED-035": "The list of licensed banks issued by the Central Bank of Yemen – Aden (CBY-Aden), as checked on 3 October "
              "2026, names 26 banks, and its 2026 exchange",
    "AR-022": "The list of licensed banks issued by the Central Bank of Yemen – Aden (CBY-Aden), as checked on 3 October "
              "2026, names 26 banks; 12 of them",
    "ED-036": "Of the 26 banks on the list of licensed banks",
}
CLM055 = OrderedDict([
    ("summary_en", ("12 of them are classified as microfinance banks", (
        "The list of licensed banks of the Central Bank of Yemen – Aden (CBY-Aden), as checked on 3 October 2026, names "
        "26 banks. This resource describes 12 of them as microfinance banks on the basis of their names in the list, not "
        "an independent regulatory classification. Appearing on the list is a formal listing by that authority: it does "
        "not mean operating, active or reaching underserved clients."))),
    ("summary_ar", ("منها 12 بنكًا مصنفة بنوكَ تمويل أصغر", (
        "تضم قائمة البنوك المرخصة الصادرة عن البنك المركزي اليمني – عدن، كما اطُّلع عليها في 3 أكتوبر 2026، 26 بنكًا. "
        "ويصف هذا المورد 12 منها بأنها بنوك تمويل أصغر استنادًا إلى أسمائها الواردة في القائمة، لا إلى تصنيف تنظيمي "
        "مستقل. والورود في القائمة إدراج رسمي لدى تلك الجهة، ولا يعني التشغيل أو النشاط أو الوصول إلى الفئات الأقل "
        "حصولًا على الخدمات."))),
    ("definition_en", ("that are classified as microfinance banks", (
        "The number of banks on the licensed-bank list of the Central Bank of Yemen – Aden (CBY-Aden), as checked on 3 "
        "October 2026, that this resource describes as microfinance banks on the basis of their names in the list."))),
    ("definition_ar", ("والمصنفة بنوكَ تمويل أصغر", (
        "عدد البنوك الواردة في قائمة البنوك المرخصة لدى البنك المركزي اليمني – عدن، كما اطُّلع عليها في 3 أكتوبر 2026، "
        "التي يصفها هذا المورد بأنها بنوك تمويل أصغر استنادًا إلى أسمائها في القائمة."))),
    ("method_en", ("12 of them are classified as microfinance banks", (
        "A count of the banks named on the licensed-bank list published by the Central Bank of Yemen – Aden (CBY-Aden), "
        "as checked on 3 October 2026. The list has no column that classifies banks by type; this resource counts as "
        "microfinance banks the 12 whose names include “microfinance” («للتمويل الأصغر»). The list establishes listing "
        "or licensing by CBY-Aden; it does not by itself establish current operation, service availability or "
        "geographic reach."))),
    ("method_ar", ("ومنها 12 بنكًا مصنفة بنوكَ تمويل أصغر", (
        "عدّ البنوك الواردة في قائمة البنوك المرخصة التي ينشرها البنك المركزي اليمني – عدن، كما اطُّلع عليها في 3 أكتوبر "
        "2026. ولا تتضمن القائمة عمودًا يصنّف البنوك بحسب نوعها؛ ويعدّ هذا المورد البنوكَ الـ12 التي "
        "تتضمن أسماؤها عبارة «للتمويل الأصغر» بنوكَ تمويل أصغر. وتثبت القائمة الإدراج أو الترخيص لدى البنك المركزي في عدن، ولا تثبت "
        "بذاتها التشغيل الحالي أو توفر الخدمة أو الانتشار الجغرافي."))),
])
CLM055_12 = {"t": "12", "k": "v", "s": "DERIVED", "src": "SRC-CBY-BANKLIST-AR-2026-001",
             "loc": "https://cby-ye.com/files/6a665add29feb.pdf, single-page scan «كشف بالبنوك المرخصة بالجمهورية اليمنية»: "
                    "the list has no type column; count of the names containing «للتمويل الأصغر» / 'Microfinance' (rows "
                    "10, 11, 15, 17, 18, 19, 20, 22, 23, 24, 25, 26); computed by CauseWay; re-read 10 October 2026"}


# ================================================================================================ helpers
def rewrite(t, rec, field, anchor, new, finding):
    cur = t.get(rec, field)
    if not isinstance(cur, str) or anchor not in cur:
        raise TxError(f"{finding} {t.sheet} {rec}.{field}: anchor {anchor[:60]!r} not found in {str(cur)[:80]!r}")
    t.set(finding, rec, field, new, cur)


def vs_load(t, rec):
    cur = t.get(rec, "value_states")
    return cur, (json.loads(cur) if cur else [])


def vs_save(t, rec, finding, cur, vs):
    t.set(finding, rec, "value_states", json.dumps(vs, ensure_ascii=False, separators=(",", ":")), cur)


def deps_without(cur, token):
    parts = [p.strip() for p in str(cur).split(";") if p.strip()]
    if parts.count(token) != 1:
        raise TxError(f"{F}: dependency {token} occurs {parts.count(token)} times in {cur!r}")
    return "; ".join(p for p in parts if p != token)


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    reg = register_rows()
    t06 = Table(s, "06_EVIDENCE_OBJECTS")
    t11 = Table(s, "11_VISUAL_LIBRARY")
    t02 = Table(s, "02_SITE_MAP")
    t15 = Table(s, "15_SOURCE_LIBRARY")

    # ======================================================== CR-05 remittances
    f5 = F + ":CR-05"
    t23 = Table(s, "23_REMITTANCES")
    for rid in IMF_ROWS_HIST:
        t23.set(f5, rid, "period_state", "MODEL_ESTIMATE", "HISTORICAL_REPORTED")
        t23.set(f5, rid, "calculation_state", "SOURCE_PUBLISHED_ESTIMATE__DEMOGRAPHIC_BEHAVIOURAL_MODEL",
                "SOURCE_REPORTED__IMF_STAFF_CALCULATIONS")
        t23.set(f5, rid, "source_table_or_section",
                "Table 4 / external sector (values, printed p.31); Annex IV para 2 (method, printed p.41)",
                "Table 4 / external sector")
        for fld, add in (("caveat_en", CAV_EN_ADD), ("caveat_ar", CAV_AR_ADD)):
            cur = t23.get(rid, fld)
            t23.set(f5, rid, fld, str(cur).rstrip() + add, cur)
    imf_rows = [k for k in t23.rows if str(k).startswith("RMO-IMF-")]
    if len(imf_rows) != 13:
        raise TxError(f"{f5}: expected 13 IMF rows, found {len(imf_rows)}")
    for rid in imf_rows:
        t23.set(f5, rid, "geography", GEO_IRG, "Yemen")
    for field, (anchor, new) in CLM007.items():
        rewrite(t06, "CLM-007", field, anchor, new, f5)
    for field, (anchor, new) in VIS06.items():
        rewrite(t06, "VIS-REMITTANCE-MACRO", field, anchor, new, f5)
    for field, (anchor, new) in VIS11.items():
        rewrite(t11, "VIS-REMITTANCE-MACRO", field, anchor, new, f5)
    for rec in ("CLM-007", "VIS-REMITTANCE-MACRO"):
        cur, vs = vs_load(t06, rec)
        if not any(e["t"] == "33%" for e in vs):
            vs.append({"t": "33%", "k": "v", "s": "READ", "src": "SRC-IMF-AIV-2025-STAFF-001", "loc": ANNEX_LOC})
        vs_save(t06, rec, f5, cur, vs)
    for (route, field), (anchor, new) in SITE_MAP.items():
        rewrite(t02, route, field, anchor, new, f5)
    for lang, field, must, new in REMIT_S2:
        s.rewrite_section(f5, "/remittances/", 2, lang, field, new, must)
    t07 = Table(s, "07_PUBLIC_CLAIMS")
    t07.set(f5, "CLM-007", "claim_type", "MODEL_ESTIMATE_VS_OUTLOOK", "REPORTED_HISTORY_VS_OUTLOOK")
    t34 = Table(s, "34_EVIDENCE_PASSPORTS")
    for field, (anchor, new) in PASSPORT_REMIT.items():
        rewrite(t34, "EP-REMITTANCE-MACRO", field, anchor, new, f5)
    # the controlled visual contract: the new state maps to the governed ESTIMATED grammar state
    c = json.load(open(CONTRACT, encoding="utf-8"))
    v = next(x for x in c["visuals"] if x["visual_id"] == "VIS-REMITTANCE-MACRO")
    ser = v["contract"]["series"][0]
    if ser["state_map"] != {"HISTORICAL_REPORTED": "REPORTED", "ESTIMATE": "ESTIMATED", "PROJECTION": "PROJECTED"}:
        raise TxError(f"{f5}: VIS-REMITTANCE-MACRO state map is not the expected one")
    ser["state_map"] = OrderedDict([("MODEL_ESTIMATE", "ESTIMATED"), ("ESTIMATE", "ESTIMATED"), ("PROJECTION", "PROJECTED")])
    v["rationale"] = ("The IMF series with its estimate and projection states and the document break, so that neither a "
                      "model estimate nor a forecast revision is read as an observed economic change.")
    v["contract"]["form"] = ("Line with model-based estimates (2018–2024) and the 2025 estimate (hollow marks) and "
                             "projections (dashed, hollow marks); BREAK_VINTAGE between 2024 and 2025.")
    with open(os.path.join(work, "visual_design_contract.json"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(c, ensure_ascii=False, indent=2) + "\n")

    # ======================================================== CR-07 SMP
    f7 = F + ":CR-07"
    if SRC_OCT in t15.rows:
        raise TxError(f"{f7}: {SRC_OCT} already present")
    for r in s.grid("15_SOURCE_LIBRARY")[4:]:
        if r and URL_OCT in [str(x) for x in r if x]:
            raise TxError(f"{f7}: locator already held by another source")
    head = t15.head
    last = max(t15.rows.values())
    s.ed.insert_rows("15_SOURCE_LIBRARY", last + 1, [{head.index(k) + 1: val for k, val in SRC_OCT_ROW.items()}])
    for k, val in SRC_OCT_ROW.items():
        s.ledger.append({"finding": f7, "sheet": "15_SOURCE_LIBRARY", "row": last + 1, "col": head.index(k) + 1,
                         "field": f"{SRC_OCT}.{k}", "old": None, "new": val})
    t15 = Table(s, "15_SOURCE_LIBRARY")
    t15.set(f7, "SRC-IMF-YEM-SMP-2026", "retrieval_date", "2026-10-10", t15.get("SRC-IMF-YEM-SMP-2026", "retrieval_date"))
    for field, new in CLM049.items():
        t06.set(f7, "CLM-049", field, new, t06.get("CLM-049", field))
    t06.set(f7, "CLM-049", "source_dependencies", "SRC-IMF-YEM-SMP-2026; " + SRC_OCT, "SRC-IMF-YEM-SMP-2026")
    cur = t06.get("CLM-049", "source_links")
    links = json.loads(cur)
    links.append({"source_id": SRC_OCT, "url": URL_OCT, "audit_state": "PASS_AUTHORITY_OR_PROVIDER_LOCATOR"})
    t06.set(f7, "CLM-049", "source_links", json.dumps(links, ensure_ascii=False, separators=(",", ":")), cur)
    cur, vs = vs_load(t06, "CLM-049")
    if not any(e.get("s") == "UNREACHABLE" for e in vs):
        raise TxError(f"{f7}: CLM-049 no longer carries the unreachable state it is expected to replace")
    vs_save(t06, "CLM-049", f7, cur, CLM049_VS)
    for lang, field, must, new in REFORMS_S7:
        s.rewrite_section(f7, "/reforms/", 7, lang, field, new, must)
    for field, (anchor, new) in CLM049_META.items():
        rewrite(t02, "/evidence/CLM-049/", field, anchor, new, f7)
    t14 = Table(s, "14_SYSTEM_CHRONOLOGY")
    cur, vs = vs_load(t14, "YSC-023")
    nvs = []
    for e in vs:
        if e.get("s") != "UNREACHABLE":
            raise TxError(f"{f7}: YSC-023 value {e.get('t')!r} is not UNREACHABLE")
        nvs.append({"t": e["t"], "k": e["k"], "s": "READ", "src": "SRC-IMF-YEM-SMP-2026", "loc": LOC_JUL})
    vs_save(t14, "YSC-023", f7, cur, nvs)
    for fld in ("verification_note_en", "verification_note_ar"):
        cur = t14.get("YSC-023", fld)
        if not cur or "4" not in str(cur):
            raise TxError(f"{f7}: YSC-023.{fld} is not the unreachable note")
        t14.set(f7, "YSC-023", fld, None, cur)
    g31 = s.grid("31_REFORMS_REGULATION")
    if g31[20][0] != "REF-IMF-001":
        raise TxError(f"{f7}: 31!r21 is not REF-IMF-001")
    s.replace(f7, "31_REFORMS_REGULATION", 21, 5, "focused on stabilization, implementation and reform track record.",
              "focused on stabilization, implementation and reform track record. IMF Management approved the 18-month "
              "non-financing SMP on 7 October 2026 (IMF press release of that date).", "REF-IMF-001.normalized_description")

    # The July release's note was the only "not re-read" label on /finance/; MF-ORIG-001+002 still prints an unreachable
    # 1997 there (its SFD terms of reference, refused again on 10 October 2026), so the page says so itself (E2-READ).
    fl = F + ":E2-LABEL"
    s.replace_section(fl, "/finance/", 2, "en", "body", FIN_S2_EN_OLD, FIN_S2_EN_OLD + FIN_S2_EN_ADD)
    s.replace_section(fl, "/finance/", 2, "ar", "body", FIN_S2_AR_OLD, FIN_S2_AR_OLD + FIN_S2_AR_ADD)

    # ======================================================== CR-08 NPL
    f8 = F + ":CR-08"
    s.replace_section(f8, "/finance/", 6, "en", "body", NPL_EN_OLD, NPL_EN_NEW)
    s.replace_section(f8, "/finance/", 6, "ar", "body", NPL_AR_OLD, NPL_AR_NEW)

    # ======================================================== CR-13 payments sex-composition labels
    f13 = F + ":CR-13"
    g17 = s.grid("17_INDICATOR_LIBRARY")
    for row, (iid, old, new) in IND_LABELS.items():
        if g17[row - 1][1] != iid:
            raise TxError(f"{f13}: 17!r{row} is not {iid}")
        s.set(f13, "17_INDICATOR_LIBRARY", row, 3, new, old, f"{iid}.label")
    t19 = Table(s, "19_PAYMENTS_DATA")
    for oid, loc in PAY_LOCS.items():
        t19.set(f13, oid, "source_locator", loc, "page 1; lines 32-83")

    # ======================================================== CR-15 CLM-043
    f15 = F + ":CR-15"
    for fld, add in (("currentness_en", CLM043_CUR_EN_ADD), ("currentness_ar", CLM043_CUR_AR_ADD)):
        cur = t06.get("CLM-043", fld)
        t06.set(f15, "CLM-043", fld, str(cur).rstrip() + add, cur)
    cur = t06.get("CLM-043", "source_dependencies")
    t06.set(f15, "CLM-043", "source_dependencies", cur + "; " + WB_YEM_SRC, cur)
    au = t15.get(WB_YEM_SRC, "additional_urls")
    urls = json.loads(au) if au else []
    if WB_YEM_PDF not in urls:
        t15.set(f15, WB_YEM_SRC, "additional_urls", json.dumps(urls + [WB_YEM_PDF]), au)

    # ======================================================== CR-16 OECD/INFE printed labels
    f16 = F + ":CR-16"
    for rec in ("CLM-013", "VIS-FL-EVIDENCE-LADDER"):
        cur, vs = vs_load(t06, rec)
        hit = 0
        for e in vs:
            if e["t"] in INFE_LOC_ADD and e.get("s") == "READ":
                e["loc"] = e["loc"] + INFE_LOC_ADD[e["t"]]
                hit += 1
        if hit != 2:
            raise TxError(f"{f16}: {rec} carries {hit} of the two scores")
        vs_save(t06, rec, f16, cur, vs)

    # ======================================================== CR-20 deposit-insurance law
    f20 = F + ":CR-20"
    g33 = s.grid("33_ANALYTICS_MASTER")
    if g33[127][0] != "CON-038":
        raise TxError(f"{f20}: 33!r128 is not CON-038")
    for col, (old_prefix, new) in CON038.items():
        cur = s.ed.get_value("33_ANALYTICS_MASTER", 128, col)
        if not str(cur).startswith(old_prefix):
            raise TxError(f"{f20}: 33!r128c{col} does not start with {old_prefix!r}")
        s.set(f20, "33_ANALYTICS_MASTER", 128, col, new, cur, f"CON-038.c{col}")

    # ======================================================== CR-09 untraced inputs / CR-19 provider naming
    f9 = F + ":CR-09"
    g04 = s.grid("04_NAV_UX")
    ui = {r[0]: r for r in g04 if r and isinstance(r[0], str) and r[0].startswith("UI-VERIFY-")}
    bound_en, bound_ar = ui["UI-VERIFY-BOUND"][1], ui["UI-VERIFY-BOUND"][2]
    part_en, part_ar = ui["UI-VERIFY-PARTIAL"][1], ui["UI-VERIFY-PARTIAL"][2]
    for rec, tok in UNTRACED.items():
        cur = t06.get(rec, "source_dependencies")
        t06.set(f9, rec, "source_dependencies", deps_without(cur, tok), cur)
        t06.set(f9, rec, "lineage_state", "BOUND_EXACT", "BOUND_PARTIAL")
        t06.set(f9, rec, "verification_en", bound_en, part_en)
        t06.set(f9, rec, "verification_ar", bound_ar, part_ar)
    f19 = F + ":CR-19"
    for field, (anchor, new) in CLM056.items():
        rewrite(t06, "CLM-056", field, anchor, new, f19)
    cur, vs = vs_load(t06, "CLM-056")
    if not any(e["t"] == "10 October 2026" for e in vs):
        vs.append({"t": "10 October 2026", "k": "d", "s": "SITE"})
    vs_save(t06, "CLM-056", f19, cur, vs)
    for field, (anchor, new) in CLM056_META.items():
        rewrite(t02, "/evidence/CLM-056/", field, anchor, new, f19)
    for lang, old, new in MF_READING_EDITS:
        s.replace_section(f19, MF_READING, 7, lang, "body", old, new)

    # ======================================================== CR-11 the CCY pressure report gets its public locator
    f11 = F + ":CR-11"
    if t15.get(CCY, "public_card_state") != "LOCATOR_ONLY" or t15.get(CCY, "primary_url"):
        raise TxError(f"{f11}: {CCY} is not the locator-only record expected")
    for field, new in CCY_SET.items():
        t15.set(f11, CCY, field, new, t15.get(CCY, field))

    # ======================================================== register AR-022, ED-035, ED-036 (+ CLM-055, one state)
    for rid in ("ED-035", "AR-022", "ED-036"):
        r = reg[rid]
        apply_register_ar(s, F, r)
        apply_register_en(s, F, r, r["en_new"], must_start=REG_EN_START[rid])
    f55 = F + ":AR-022"
    for field, (anchor, new) in CLM055.items():
        rewrite(t06, "CLM-055", field, anchor, new, f55)
    cur, vs = vs_load(t06, "CLM-055")
    if [e["t"] for e in vs].count("12") != 1:
        raise TxError(f"{f55}: CLM-055 value 12 not found once")
    vs = [CLM055_12 if e["t"] == "12" else e for e in vs]
    vs_save(t06, "CLM-055", f55, cur, vs)

    counts = refresh_self_counts(s, F + ":OWN-10")
    rep = s.save(out, ledger, OrderedDict([
        ("transaction", F),
        ("summary", "CR-05 (IMF 2018-2024 remittances are model-based estimates for IRG areas), CR-07 (SMP approved by "
                    "IMF Management, 7 Oct 2026), CR-08 (IMF FSI table described; zeros read as not reported), CR-09 "
                    "(three internal dataset inputs supply no printed figure), CR-11 (CCY report: public locator), "
                    "CR-13 (H1-2025 shares re-attached to their panels), CR-15 (WB 'discontinued' wording beside the "
                    "AR2025 line), CR-16 (INFE scores are printed labels), CR-19 (provider described, not named), "
                    "CR-20 (Law No. 21 of 2008); register rows AR-022, ED-035, ED-036"),
        ("self_counts", counts)]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
