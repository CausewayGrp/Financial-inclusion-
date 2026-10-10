# -*- coding: utf-8 -*-
"""Close-out transaction CLOSE-3A: U1 and CR-03 — the Global Findex values the World Bank publishes for Yemen's 2021
wave are unlocked (brief v5 W3c, Appendix B U1). English and Arabic change together.

  python3 close_3a.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Writes <work_dir>/visual_design_contract.json (three table-first contracts added) for run_stage.py --install.

Source: the open World Bank API only (api.worldbank.org/v2, source 28 "Global Findex database", no key) and the study's
public DDI metadata, snapshot committed as audit/close_out/fixtures/findex_api_2026-10-10.json (retrieved 10 October
2026, lastupdated 2025-10-06): the 354 series whose values the Master uses, every one of the 3,313 source-28 series for
Yemen 2022 as [label, value], the account series for all years, and the valid/invalid case counts of the 26 study
variables behind the unpublished measures. No respondent-level data is used or computed from. Every series is mapped to
its panel measure and group by the World Bank's own indicator label (checked below), never by the microdata code:
fin26/fin28 in the panel are fh1/fh2 in the open data. Every "no published value" statement is asserted against the
label query, never assumed.

- 147 new rows in 25_FINDEX_BASELINE (WB-FINDEX-OBS-2022-013 ...): the national values the panel lacked and the group
  values the World Bank publishes (sex, age, education, income, labour-force status), each with its series URL as
  locator and a caveat (no interval published here; group rows: smaller samples, no cause).
- 27_FINDEX_SUBGROUPS: the 51 contract rows the World Bank publishes become PUBLIC_WB_PUBLISHED_SAME_WAVE; the 105 it
  does not publish stay contract only, each with its reason: the World Bank publishes no value, or only the all-adults
  value (a value requires computation from licensed microdata, OWN-09); or, for the two mobile-money measures, Yemen's
  survey did not ask the question (DDI: no valid case), so no computation could produce one. FSG-0001..0004 were already
  public; the 32 rural/urban rows keep their reason, re-verified (no rural or urban series has a Yemen value).
- Three existing records become table-first governed visuals (VIS-FINDEX-ACCESS-USE and VIS-FINDEX-RESILIENCE on
  /people/, VIS-FINDEX-FLOW-CHANNELS on /people/ and /remittances/): a table of the published values by group, from
  governed rows only. VIS-FINDEX-BARRIERS stays text: the World Bank publishes no value for the reasons adults give for
  not having an account.
- CR-03: CLM-026 no longer says 29 of its 32 measures have no published value; 16 have World Bank values and the record
  lists them. Its claim that values were reproduced from the respondent file is replaced by the open-API source.
- Records that said these values were "not yet produced" now say what is published (02 meta, VIS-FINDEX-SAMPLE-SUPPORT,
  VIS-DEMAND-VINTAGE-LADDER, CLM-030, CLM-031, VIS-DOMESTIC-REMITTANCE-PATH-2014, MA-001, /people/ s7, /remittances/ s6).
"""
import json, os, re, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from close_lib import Session, Table, TxError, refresh_self_counts, insert_ui_rows, COL03, S03  # noqa: E402

F = "CLOSE-3A"
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
FIXTURE = os.path.join(HERE, "fixtures", "findex_api_2026-10-10.json")
CONTRACT = os.path.join(ROOT, "scripts", "projection", "controlled_inputs", "visual_design_contract.json")
SRC_AGG = "SRC-WB-FINDEX-AGG-2022"
SRC_STUDY = "SRC-WB-FINDEX-001"

# ------------------------------------------------------------------------------------------------ the series
# (suffix, group key as held in 25.group, World Bank label tail)
GROUPS = [("", "total", "  (% age 15+)"), (".1", "female", ", women (% age 15+)"), (".2", "male", ", men (% age 15+)"),
          (".3", "ages 15-24", ", young (% ages 15-24)"), (".4", "ages 25+", ", older (% age 25+)"),
          (".5", "primary education or less", ", primary education or less (% age 15+)"),
          (".6", "secondary education or more", ", secondary education or more (% age 15+)"),
          (".7", "poorest 40%", ", poorest 40% (% age 15+)"), (".8", "richest 60%", ", richest 60% (% age 15+)"),
          (".12", "in labor force", ", in laborforce (% age 15+)"), (".11", "out of labor force", ", out of laborforce (% age 15+)")]
G_ALL = [g for _, g, _ in GROUPS]
G_SUB = G_ALL[1:]
UNIT = {"ages 15-24": "percent of population ages 15-24", "ages 25+": "percent of population ages 25+"}
# (panel metric, open-data code, World Bank label head, groups added here)
SERIES = [
    ("FDP-001", "account.t.d", "Account", ["in labor force", "out of labor force"]),
    ("FDP-002", "fiaccount.t.d", "Bank or similar financial institution account", G_ALL),
    ("FDP-011", "fin17a", "Saved at a bank or similar financial institution", ["total"]),
    ("FDP-013", "fin22a", "Borrowed from a formal bank or similar financial institution", ["total"]),
    ("FDP-014", "fin22b", "Borrowed from family or friends", G_ALL),
    ("FDP-015", "fin24aN", "Coming up with emergency funds in 30 days: not possible", G_ALL),
    ("FDP-015", "fin24aVD", "Coming up with emergency funds in 30 days: possible and very difficult", G_ALL),
    ("FDP-015", "fin24aSD", "Coming up with emergency funds in 30 days: possible and somewhat difficult", G_ALL),
    ("FDP-015", "fin24aND", "Coming up with emergency funds in 30 days: possible and not difficult at all", G_ALL),
    ("FDP-017", "fh1", "Sent domestic remittances", G_ALL),
    ("FDP-018", "fh2", "Received domestic remittances", G_ALL),
    ("FDP-019", "fin32", "Received wages", G_ALL),
    ("FDP-020", "fin37", "Received government transfer", ["total"]),
    ("FDP-021", "fin42", "Received payments for the sale of agricultural products", G_ALL),
    ("FDP-026", "save.any.t.d", "Saved any money", G_SUB),
    ("FDP-027", "borrow.any.t.d", "Borrowed any money", G_SUB),
    ("FDP-028", "fh1.fh2", "Sent or received domestic remittances", G_ALL),
    ("FDP-032", "merchant.pay", "Made a digital merchant payment", ["total"]),
]
# rows the Master already held (their values are checked against the snapshot too)
LEGACY = OrderedDict([("account.t.d", "WB-FINDEX-OBS-2022-001"), ("account.t.d.1", "WB-FINDEX-OBS-2022-002"),
                      ("account.t.d.2", "WB-FINDEX-OBS-2022-003"), ("account.t.d.7", "WB-FINDEX-OBS-2022-004"),
                      ("account.t.d.8", "WB-FINDEX-OBS-2022-005"), ("account.t.d.5", "WB-FINDEX-OBS-2022-006"),
                      ("account.t.d.6", "WB-FINDEX-OBS-2022-007"), ("account.t.d.3", "WB-FINDEX-OBS-2022-008"),
                      ("account.t.d.4", "WB-FINDEX-OBS-2022-009"), ("save.any.t.d", "WB-FINDEX-OBS-2022-010"),
                      ("borrow.any.t.d", "WB-FINDEX-OBS-2022-011"), ("g20.any", "WB-FINDEX-OBS-2022-012")])
PERIOD_NOTE = ("World Bank Data labels the year 2022; the study is the Yemen Global Findex 2021, fielded 7 November 2022 "
               "to 9 January 2023")
# the caveat is internal (25 is not printed); the unrounded value stays in it as the locator's reading
CAVEAT_HEAD = ("World Bank published value for Yemen (Global Findex database, open API source 28; " + PERIOD_NOTE + "); "
               "unrounded value {raw}. No interval published here (EXT-07 held)")
CAVEAT_TOTAL = CAVEAT_HEAD + ". Close-out U1, 10 October 2026."
CAVEAT_GROUP = (CAVEAT_HEAD + "; a group rests on fewer than the 1,000 interviews of the whole sample; a difference "
                "between groups is not a cause (CAUSE_HELD). Close-out U1, 10 October 2026.")

# 27_FINDEX_SUBGROUPS: which panel metric is published by group, and where it is shown
PUBLISHED_BY_GROUP = OrderedDict([("FDP-001", "VIS-FINDEX-ACCESS-USE"), ("FDP-002", "VIS-FINDEX-ACCESS-USE"),
                                  ("FDP-014", "VIS-FINDEX-ACCESS-USE"), ("FDP-026", "VIS-FINDEX-ACCESS-USE"),
                                  ("FDP-027", "VIS-FINDEX-ACCESS-USE"), ("FDP-015", "VIS-FINDEX-RESILIENCE"),
                                  ("FDP-017", "VIS-FINDEX-FLOW-CHANNELS"), ("FDP-018", "VIS-FINDEX-FLOW-CHANNELS"),
                                  ("FDP-019", "VIS-FINDEX-FLOW-CHANNELS"), ("FDP-021", "VIS-FINDEX-FLOW-CHANNELS"),
                                  ("FDP-028", "VIS-FINDEX-FLOW-CHANNELS")])
TOTAL_ONLY = OrderedDict([("FDP-011", "fin17a"), ("FDP-013", "fin22a"), ("FDP-020", "fin37"), ("FDP-031", "g20.any"),
                          ("FDP-032", "merchant.pay")])
# mobile money: Yemen's survey did not ask these (CR-01); the study's public metadata print no valid case
NOT_ASKED = OrderedDict([("FDP-010", "fin13a"), ("FDP-012", "fin17a1")])
# the World Bank series that would carry each unpublished measure, found by label in the label query of every
# source-28 series; none may have a Yemen value (asserted below, not assumed). A family with no series at all
# (religious reasons, the 7-day question) is recorded as such.
NO_VALUE_LABELS = OrderedDict([
    ("FDP-003", r"mobile phone or the internet to (check (your |an )?account balance|access)"),
    ("FDP-004", r"^No account because .*too far"),
    ("FDP-005", r"^No account because .*too expensive"),
    ("FDP-006", r"^No account because .*documentation"),
    ("FDP-007", r"^No account because .*trust"),
    ("FDP-008", r"^No account because .*religio"),
    ("FDP-009", r"^No account because .*(insufficient funds|lack of money|enough money)"),
    ("FDP-010", r"^(Deposited money into|Sent money from|Took out ?money from|Sent or withdrew money from|"
                r"Took out ?or withdrew money from) a mobile money account|^Mobile money account"),
    ("FDP-012", r"^Saved money using a mobile money account"),
    ("FDP-016", r"\b7 days\b|\bseven days\b"),
    ("FDP-022", r"[Ww]orr"), ("FDP-023", r"[Ww]orr"), ("FDP-024", r"[Ww]orr"), ("FDP-025", r"[Ww]orr"),
    ("FDP-029", r"^Own a mobile phone"),
    ("FDP-030", r"^Has access to the Internet|^Used the internet in the past three months"),
])
NO_SERIES_OK = {"FDP-008", "FDP-016"}   # the database has no such series at all
RURAL_RX = r", (rural|urban) \("
DIM_TEXT = {"SEX": "sex", "AGE": "age", "EDUCATION": "education", "INCOME": "income", "WORKFORCE": "labour-force status"}
DIM_SUFFIX = {"SEX": (".1", ".2"), "AGE": (".3", ".4"), "EDUCATION": (".5", ".6"), "INCOME": (".7", ".8"),
              "WORKFORCE": (".11", ".12")}

# ------------------------------------------------------------------------------------------------ interface copy (04)
UI = [  # (ui_id, label_en, label_ar, note)
    ("UI-VIS-CAT-FINDEX-IN-LABOUR-FORCE", "Adults in the labour force", "البالغون داخل قوة العمل",
     "Close-out U1. Findex group row (World Bank: in laborforce)."),
    ("UI-VIS-CAT-FINDEX-OUT-LABOUR-FORCE", "Adults out of the labour force", "البالغون خارج قوة العمل",
     "Close-out U1. Findex group row (World Bank: out of laborforce)."),
    ("UI-VIS-TH-FINDEX-ADULTS", "Adults", "البالغون", "Close-out U1. Findex group tables: first column."),
    ("UI-VIS-TH-FINDEX-ACCOUNT", "Has an account", "يملك حسابًا", "Close-out U1. Column, account.t.d."),
    ("UI-VIS-TH-FINDEX-ACCOUNT-FI", "Account at a financial institution", "حساب لدى مؤسسة مالية",
     "Close-out U1. Column, fiaccount.t.d."),
    ("UI-VIS-TH-FINDEX-SAVED", "Saved any money", "ادّخر أي مبلغ", "Close-out U1. Column, save.any.t.d."),
    ("UI-VIS-TH-FINDEX-BORROWED", "Borrowed any money", "اقترض أي مبلغ", "Close-out U1. Column, borrow.any.t.d."),
    ("UI-VIS-TH-FINDEX-BORROWED-FAMILY", "Borrowed from family or friends", "اقترض من الأسرة أو الأصدقاء",
     "Close-out U1. Column, fin22b."),
    ("UI-VIS-TH-FINDEX-EMERG-NOT-POSSIBLE", "Not possible, or don't know or no answer", "غير ممكن، أو لا يعرف أو لا إجابة",
     "Close-out U1. Column, fin24aN (the World Bank counts don't know and refused with not possible)."),
    ("UI-VIS-TH-FINDEX-EMERG-VERY", "Possible, very difficult", "ممكن بصعوبة بالغة", "Close-out U1. Column, fin24aVD."),
    ("UI-VIS-TH-FINDEX-EMERG-SOMEWHAT", "Possible, somewhat difficult", "ممكن ببعض الصعوبة",
     "Close-out U1. Column, fin24aSD."),
    ("UI-VIS-TH-FINDEX-EMERG-NOT-DIFFICULT", "Possible, not difficult at all", "ممكن دون أي صعوبة",
     "Close-out U1. Column, fin24aND."),
    ("UI-VIS-TH-FINDEX-WAGES", "Received wages", "تلقى أجورًا", "Close-out U1. Column, fin32."),
    ("UI-VIS-TH-FINDEX-AGRI", "Received payments for agricultural sales", "تلقى مدفوعات عن مبيعات زراعية",
     "Close-out U1. Column, fin42."),
    ("UI-VIS-TH-FINDEX-REMIT-SENT", "Sent domestic remittances", "أرسل حوالات محلية", "Close-out U1. Column, fh1."),
    ("UI-VIS-TH-FINDEX-REMIT-RECEIVED", "Received domestic remittances", "تلقى حوالات محلية", "Close-out U1. Column, fh2."),
    ("UI-VIS-TH-FINDEX-REMIT-ANY", "Sent or received domestic remittances", "أرسل حوالات محلية أو تلقاها",
     "Close-out U1. Column, fh1.fh2."),
    ("UI-VIS-UNIT-PCT-ADULTS-IN-GROUP", "% of adults in each group, as published by the World Bank",
     "% من البالغين في كل فئة، كما ينشرها البنك الدولي", "Close-out U1. Caption of the Findex group tables."),
    ("UI-VIS-NOTE-FINDEX-EMERG-30", "Coming up with emergency funds within 30 days",
     "تدبير أموال للطوارئ خلال 30 يومًا", "Close-out U1. Caption, VIS-FINDEX-RESILIENCE."),
    ("UI-VIS-NOTE-FINDEX-GROUPS",
     "World Bank published values, shown without an interval: no interval is published here for a group value, each "
     "group rests on fewer than the 1,000 interviews, and a difference between groups is not a cause.",
     "قيم ينشرها البنك الدولي، تُعرض دون فترة ثقة: لا تُنشر هنا فترة ثقة لقيمة أي فئة، وتستند كل فئة إلى أقل من مقابلات "
     "العينة البالغة 1,000، والفرق بين الفئات ليس سببًا.",
     "Close-out U1. Marker row, Findex group tables."),
    ("UI-VIS-NOTE-FINDEX-ACCOUNT-FI",
     "Yemen's survey did not ask the mobile-money questions, so the World Bank's values for an account at a financial "
     "institution are the same as for any account.",
     "لم تُطرح أسئلة خدمات الأموال عبر الهاتف في مسح اليمن، لذلك تطابق قيمُ البنك الدولي لحساب لدى مؤسسة مالية قيمَه "
     "لأي حساب.",
     "Close-out U1 (CR-01). Marker row, VIS-FINDEX-ACCESS-USE."),
    ("UI-VIS-NOTE-FINDEX-EMERG-CATS",
     "The four answers are adults' own assessments, in the survey's categories, and are not combined into a score. "
     "\"Not possible\" includes adults who did not know or did not answer, as the World Bank counts them; the shares in "
     "a row do not quite add up to all adults, because a few adults who said it was possible did not say how difficult. "
     "The survey also asked about 7 days, but the World Bank publishes no value for that question.",
     "الإجابات الأربع تقديرات البالغين أنفسهم، بفئات المسح، ولا تُدمج في درجة واحدة. وتشمل فئة «غير ممكن» البالغين الذين "
     "لم يعرفوا أو لم يجيبوا، كما يحتسبهم البنك الدولي؛ ولا تبلغ الحصص في كل صف مجموع البالغين تمامًا، لأن قلة ممن قالوا "
     "إن ذلك ممكن لم يذكروا مدى صعوبته. وسأل المسح أيضًا عن مهلة 7 أيام، لكن البنك الدولي لا ينشر قيمة لذلك السؤال.",
     "Close-out U1. Marker row, VIS-FINDEX-RESILIENCE."),
    ("UI-VIS-NOTE-FINDEX-FLOWS",
     "Each value is a share of all adults in the group, not of those who received or sent the money; the channels "
     "through which it was paid, sent or received are not shown.",
     "كل قيمة نسبة من جميع البالغين في الفئة، لا ممن تلقوا الأموال أو أرسلوها؛ ولا تُعرض القنوات التي دُفعت أو أُرسلت "
     "أو استُلمت عبرها.",
     "Close-out U1. Marker row, VIS-FINDEX-FLOW-CHANNELS."),
]
ROW_UI = OrderedDict([("total", "UI-VIS-CAT-FINDEX-TOTAL"), ("female", "UI-VIS-CAT-FINDEX-FEMALE"),
                      ("male", "UI-VIS-CAT-FINDEX-MALE"), ("ages 15-24", "UI-VIS-CAT-FINDEX-AGE-15-24"),
                      ("ages 25+", "UI-VIS-CAT-FINDEX-AGE-25-PLUS"), ("primary education or less", "UI-VIS-CAT-FINDEX-PRIMARY-EDU"),
                      ("secondary education or more", "UI-VIS-CAT-FINDEX-SECONDARY-EDU"),
                      ("poorest 40%", "UI-VIS-CAT-FINDEX-POOREST40"), ("richest 60%", "UI-VIS-CAT-FINDEX-RICHEST60"),
                      ("in labor force", "UI-VIS-CAT-FINDEX-IN-LABOUR-FORCE"),
                      ("out of labor force", "UI-VIS-CAT-FINDEX-OUT-LABOUR-FORCE")])

# ------------------------------------------------------------------------------------------------ the three tables
# visual -> (columns [(code head, column UI)], caption UI ids, markers after the rows)
TABLES = OrderedDict([
    ("VIS-FINDEX-ACCESS-USE", ([("account.t.d", "UI-VIS-TH-FINDEX-ACCOUNT"), ("fiaccount.t.d", "UI-VIS-TH-FINDEX-ACCOUNT-FI"),
                                ("save.any.t.d", "UI-VIS-TH-FINDEX-SAVED"), ("borrow.any.t.d", "UI-VIS-TH-FINDEX-BORROWED"),
                                ("fin22b", "UI-VIS-TH-FINDEX-BORROWED-FAMILY")],
                               ["UI-VIS-UNIT-PCT-ADULTS-IN-GROUP"], ["UI-VIS-NOTE-FINDEX-ACCOUNT-FI", "UI-VIS-NOTE-FINDEX-GROUPS"])),
    ("VIS-FINDEX-RESILIENCE", ([("fin24aN", "UI-VIS-TH-FINDEX-EMERG-NOT-POSSIBLE"), ("fin24aVD", "UI-VIS-TH-FINDEX-EMERG-VERY"),
                                ("fin24aSD", "UI-VIS-TH-FINDEX-EMERG-SOMEWHAT"), ("fin24aND", "UI-VIS-TH-FINDEX-EMERG-NOT-DIFFICULT")],
                               ["UI-VIS-NOTE-FINDEX-EMERG-30", "UI-VIS-UNIT-PCT-ADULTS-IN-GROUP"],
                               ["UI-VIS-NOTE-FINDEX-EMERG-CATS", "UI-VIS-NOTE-FINDEX-GROUPS"])),
    ("VIS-FINDEX-FLOW-CHANNELS", ([("fin32", "UI-VIS-TH-FINDEX-WAGES"), ("fin42", "UI-VIS-TH-FINDEX-AGRI"),
                                   ("fh1", "UI-VIS-TH-FINDEX-REMIT-SENT"), ("fh2", "UI-VIS-TH-FINDEX-REMIT-RECEIVED"),
                                   ("fh1.fh2", "UI-VIS-TH-FINDEX-REMIT-ANY")],
                                  ["UI-VIS-UNIT-PCT-ADULTS-IN-GROUP"], ["UI-VIS-NOTE-FINDEX-FLOWS", "UI-VIS-NOTE-FINDEX-GROUPS"])),
])
RATIONALE = {
    "VIS-FINDEX-ACCESS-USE": "The World Bank's published shares for account ownership, saving and borrowing, all adults "
                             "and by group, as a table: no interval is published here for a group value, so a drawn gap "
                             "would suggest a precision the evidence does not carry.",
    "VIS-FINDEX-RESILIENCE": "The four published answer categories on emergency funds within 30 days, all adults and by "
                             "group, as a table: the categories are not a score, and no interval is published here for a "
                             "group value.",
    "VIS-FINDEX-FLOW-CHANNELS": "The World Bank's published shares of adults receiving wages or agricultural payments and "
                                "sending or receiving domestic remittances, all adults and by group, as a table; channels "
                                "are not shown.",
}
PROMOTION = ("A drawn comparison of groups needs an interval for each group value; none is published here (EXT-07 held), "
             "and this resource does not compute one from respondent-level data (OWN-09).")

# ------------------------------------------------------------------------------------------------ governed text
# period_en/period_ar are copied from CLM-001 at run time (brief U1: the period wording copies CLM-001)
FRAME_EN = (" The survey frame excludes Al Baydaa, Al Jawf, Mareb, Sadah, Socotra and several districts elsewhere: areas "
            "with about 23% of the population.")
FRAME_AR = (" ويستبعد إطار المسح محافظات البيضاء والجوف ومأرب وصعدة وسقطرى وعددًا من المديريات في محافظات أخرى، وهي "
            "مناطق تضم نحو 23% من السكان.")
METHOD_EN = ("The table's values are the World Bank's published estimates for Yemen, read from the open World Bank data "
             "API (Global Findex database, source 28) on 10 October 2026 and kept as a dated snapshot; each series is "
             "matched to its measure and group by the World Bank's own indicator label. Nothing in the table is computed "
             "here, and no respondent-level data are used.")
METHOD_AR = ("قيم الجدول هي التقديرات التي ينشرها البنك الدولي لليمن، قُرئت من واجهة البيانات المفتوحة للبنك الدولي "
             "(قاعدة بيانات Global Findex، المصدر 28) في 10 أكتوبر 2026 وحُفظت في لقطة مؤرخة؛ وطوبقت كل سلسلة مع مقياسها "
             "وفئتها وفق تسمية المؤشر لدى البنك الدولي نفسه. ولا يُحتسب في الجدول هنا أي رقم، ولا تُستخدم أي بيانات على "
             "مستوى المستجيبين.")
METHOD_DIGITAL_EN = (" The digital-payment share is the World Bank's own published value for the wave; its 95% interval is "
                     "computed by CauseWay from that value and the design effect the World Bank publishes for the survey.")
METHOD_DIGITAL_AR = (" ونسبة المدفوعات الرقمية هي القيمة التي نشرها البنك الدولي نفسه للموجة، وتحتسب CauseWay فترة الثقة "
                     "95% لها من هذه القيمة ومن أثر التصميم الذي ينشره البنك الدولي للمسح.")
LATER_EN = ("the World Bank's open data hold no later Yemen value for account ownership (all years checked on 10 October "
            "2026)")
LATER_AR = ("ولا تتضمن البيانات المفتوحة للبنك الدولي قيمة أحدث لليمن لامتلاك الحساب (جرى التحقق من جميع السنوات في 10 "
            "أكتوبر 2026)")
CURRENT_EN = ("The values refer to the Global Findex 2021 wave, which World Bank Data labels 2022, with Yemen fieldwork "
              "from 7 November 2022 to 9 January 2023; " + LATER_EN + ".")
CURRENT_AR = ("تعود القيم إلى موجة Global Findex 2021، التي يعرضها موقع بيانات البنك الدولي لسنة 2022، ونُفذ عملها "
              "الميداني في اليمن من 7 نوفمبر 2022 إلى 9 يناير 2023؛ " + LATER_AR + ".")
UNIVERSE_EN = ("Adults aged 15 and over in the areas the survey covered, and the groups by sex, age, education, income "
               "and labour-force status as the World Bank defines them." + FRAME_EN)
UNIVERSE_AR = ("البالغون بعمر 15 سنة فأكثر في المناطق التي شملها المسح، والفئات بحسب الجنس والعمر والتعليم والدخل "
               "والمشاركة في قوة العمل كما يعرّفها البنك الدولي." + FRAME_AR)
NO_GROUP_INTERVAL_EN = "no interval is published here for a group value"
NO_GROUP_INTERVAL_AR = "لا تُنشر هنا فترة ثقة لقيمة أي فئة"

V = OrderedDict()   # 06 and 11 text of the three table-first visuals
V["VIS-FINDEX-ACCESS-USE"] = dict(
    title_en="Account ownership, saving and borrowing, by group",
    title_ar="امتلاك الحساب والادخار والاقتراض بحسب الفئة",
    question_en="How do account ownership, saving and borrowing differ across groups of adults in the World Bank's "
                "published values?",
    question_ar="كيف يختلف امتلاك الحساب والادخار والاقتراض بين فئات البالغين في القيم التي ينشرها البنك الدولي؟",
    shows_en="World Bank published shares of adults who have an account, an account at a financial institution, saved "
             "any money, borrowed any money and borrowed from family or friends, for all adults and by sex, age, "
             "education, income and labour-force status.",
    shows_ar="النسب التي ينشرها البنك الدولي للبالغين الذين يملكون حسابًا، أو حسابًا لدى مؤسسة مالية، أو ادخروا أي مبلغ، "
             "أو اقترضوا أي مبلغ، أو اقترضوا من الأسرة أو الأصدقاء، لجميع البالغين وبحسب الجنس والعمر والتعليم والدخل "
             "والمشاركة في قوة العمل.",
    value_en="Shows where the published shares differ by group in the same wave, without intervals or causes, so that a "
             "gap is read as a description, not an explanation.",
    value_ar="يبين مواضع اختلاف النسب المنشورة بين الفئات في الموجة نفسها، من دون فترات ثقة أو أسباب، حتى تُقرأ الفجوة "
             "وصفًا لا تفسيرًا.",
    encoding="Table: one row per group, one column per measure, values as the World Bank publishes them (one decimal); "
             "no gap column, no interval, no ranking.",
    prohibited_en="A difference between two groups is not a cause, and " + NO_GROUP_INTERVAL_EN + "; group values rest "
                  "on smaller samples than the value for all adults. Owning an account does not show that it is used, "
                  "and borrowing any money includes borrowing from family and friends, which needs no provider.",
    prohibited_ar="الفرق بين فئتين ليس سببًا، و" + NO_GROUP_INTERVAL_AR + "؛ وتستند قيم الفئات إلى عينات أصغر من عينة "
                  "القيمة الخاصة بجميع البالغين. وامتلاك الحساب لا يدل على استخدامه، واقتراض أي مبلغ يشمل الاقتراض من "
                  "الأسرة والأصدقاء الذي لا يحتاج إلى مقدم خدمة.",
    summary_en="World Bank published values for Yemen's Global Findex 2021 wave: 11.9% of adults had an account (the "
               "same share at a financial institution), 21.6% saved any money, 51.3% borrowed any money and 41.1% "
               "borrowed from family or friends. The table gives each share for women and men, two age groups, two "
               "education groups, adults in the poorest 40% and the richest 60% of households by income, and adults in "
               "and out of the labour force; " + NO_GROUP_INTERVAL_EN + ", groups rest on smaller samples, and a "
               "difference between groups is not a cause. A different measure of the same wave: 9.3% of adults made or "
               "received a digital payment (95% interval 6.8% to 11.8%, computed by CauseWay from the World Bank's "
               "published value and design effect); it is a separate measure of payments, shown for all adults only, and "
               "not a measure of account ownership.",
    summary_ar="قيم ينشرها البنك الدولي لموجة 2021 من Global Findex الخاصة باليمن: كان لدى 11.9% من البالغين حساب "
               "(والنسبة نفسها لحساب لدى مؤسسة مالية)، وادخر 21.6% أي مبلغ، واقترض 51.3% أي مبلغ، واقترض 41.1% من "
               "الأسرة أو الأصدقاء. ويعرض الجدول كل نسبة للنساء والرجال، ولفئتين عمريتين، وفئتين تعليميتين، وللبالغين في "
               "أفقر 40% وأغنى 60% من الأسر بحسب الدخل، وللبالغين داخل قوة العمل وخارجها؛ و" + NO_GROUP_INTERVAL_AR +
               "، وتستند الفئات إلى عينات أصغر، والفرق بين الفئات ليس سببًا. ومقياس مختلف من الموجة نفسها: أجرى 9.3% "
               "من البالغين مدفوعة رقمية أو تلقوها (فترة ثقة 95% من 6.8% إلى 11.8%، من احتساب CauseWay من القيمة التي "
               "ينشرها البنك الدولي ومن أثر التصميم)؛ وهو مقياس منفصل للمدفوعات، يُعرض لجميع البالغين فقط، وليس مقياسًا "
               "لامتلاك الحساب.",
    definition_en="Five measures for adults aged 15 and over in the areas the survey covered, as the World Bank publishes "
                  "them for Yemen's 2021 wave: having an account, having an account at a financial institution, saving "
                  "any money, borrowing any money and borrowing from family or friends in the past year, each for all "
                  "adults and by group; and, for all adults, making or receiving a digital payment.",
    definition_ar="خمسة مقاييس للبالغين بعمر 15 سنة فأكثر في المناطق التي شملها المسح، كما ينشرها البنك الدولي لموجة 2021 "
                  "الخاصة باليمن: امتلاك حساب، وامتلاك حساب لدى مؤسسة مالية، وادخار أي مبلغ، واقتراض أي مبلغ، والاقتراض "
                  "من الأسرة أو الأصدقاء خلال السنة الماضية، لكلٍّ منها قيمة لجميع البالغين ولكل فئة؛ وكذلك إجراء مدفوعة "
                  "رقمية أو تلقيها، لجميع البالغين.",
    limitations_en="A difference between groups does not establish its cause, and " + NO_GROUP_INTERVAL_EN + "; group "
                   "values rest on smaller samples than the value for all adults. Owning an account does not establish "
                   "that it is used, and the table shows no measure of account use; a digital payment is a different "
                   "measure again. The five measures have their own question bases and are not stages of one process.",
    limitations_ar="الفرق بين الفئات لا يثبت سببه، و" + NO_GROUP_INTERVAL_AR + "؛ وتستند قيم الفئات إلى عينات أصغر من "
                   "عينة القيمة الخاصة بجميع البالغين. وامتلاك الحساب لا يثبت استخدامه، ولا يعرض الجدول أي مقياس لاستخدام "
                   "الحساب؛ والمدفوعة الرقمية مقياس مختلف آخر. ولكل من المقاييس الخمسة قاعدة سؤاله الخاصة، ولا تمثل مراحل "
                   "في مسار واحد.",
    method_extra_en=METHOD_DIGITAL_EN, method_extra_ar=METHOD_DIGITAL_AR,
    current_extra_en=" The digital-payment value refers to the same wave.",
    current_extra_ar=" وتعود قيمة المدفوعات الرقمية إلى الموجة نفسها.",
)
V["VIS-FINDEX-RESILIENCE"] = dict(
    title_en="Coming up with emergency funds within 30 days, by group",
    title_ar="تدبير أموال للطوارئ خلال 30 يومًا بحسب الفئة",
    question_en="Did adults say they could come up with emergency funds within 30 days, and how difficult it would be, by "
                "group?",
    question_ar="هل قال البالغون إن بإمكانهم تدبير أموال للطوارئ خلال 30 يومًا، وما مدى صعوبة ذلك، بحسب الفئة؟",
    shows_en="The World Bank's published shares of adults who said that coming up with emergency funds within 30 days "
             "would not be possible (with those who did not know or did not answer), or would be possible but very "
             "difficult, somewhat difficult, or not difficult at all, for all adults and by group.",
    shows_ar="النسب التي ينشرها البنك الدولي للبالغين الذين قالوا إن تدبير أموال للطوارئ خلال 30 يومًا سيكون غير ممكن "
             "(ومعهم من لم يعرفوا أو لم يجيبوا)، أو ممكنًا بصعوبة بالغة، أو ببعض الصعوبة، أو دون أي صعوبة، لجميع البالغين "
             "وبحسب الفئة.",
    value_en="Keeps the survey's own answer categories, including saying the money could not be raised, so that "
             "resilience is not reduced to a single score.",
    value_ar="يحافظ على فئات الإجابة كما وردت في المسح، بما فيها القول بتعذر تدبير المال، حتى لا يُختزل الصمود في درجة "
             "واحدة.",
    encoding="Table: one row per group, the four answer categories as columns, values as the World Bank publishes them "
             "(one decimal); the categories are not summed into a score, and a row need not add up to all adults.",
    prohibited_en="The four answers are adults' own assessments of a hypothetical emergency, not a resilience score or "
                  "an observed event; a difference between groups is not a cause, and " + NO_GROUP_INTERVAL_EN + ". The "
                  "survey also asked about 7 days, but the World Bank publishes no value for that question, so the two "
                  "time horizons are not compared.",
    prohibited_ar="الإجابات الأربع تقديرات البالغين أنفسهم لحالة طارئة افتراضية، وليست درجة للصمود ولا حدثًا مرصودًا؛ "
                  "والفرق بين الفئات ليس سببًا، و" + NO_GROUP_INTERVAL_AR + ". وسأل المسح أيضًا عن مهلة 7 أيام، لكن البنك "
                  "الدولي لا ينشر قيمة لذلك السؤال، لذلك لا يُقارن الأفقان الزمنيان.",
    summary_en="World Bank published values for Yemen's Global Findex 2021 wave: 10.8% of adults said that coming up "
               "with emergency funds within 30 days would not be possible, or did not know or did not answer (the World "
               "Bank counts these together); 25.1% said it would be possible but very difficult, 40.4% somewhat "
               "difficult and 23.2% not difficult at all. The table gives the same four answers by sex, age, education, "
               "income and labour-force status; the shares in a row do not quite add up to all adults, because a few "
               "adults who said it was possible did not say how difficult. " + NO_GROUP_INTERVAL_EN[0].upper()
               + NO_GROUP_INTERVAL_EN[1:] + ", groups rest on smaller samples, and a difference between groups is not a "
               "cause.",
    summary_ar="قيم ينشرها البنك الدولي لموجة 2021 من Global Findex الخاصة باليمن: قال 10.8% من البالغين إن تدبير أموال "
               "للطوارئ خلال 30 يومًا سيكون غير ممكن، أو لم يعرفوا أو لم يجيبوا (ويحتسب البنك الدولي هذه الإجابات معًا)؛ وقال 25.1% إنه "
               "سيكون ممكنًا بصعوبة بالغة، و40.4% ببعض الصعوبة، و23.2% دون أي صعوبة. ويعرض الجدول الإجابات الأربع نفسها "
               "بحسب الجنس والعمر والتعليم والدخل والمشاركة في قوة العمل؛ ولا تبلغ الحصص في كل صف مجموع البالغين تمامًا، "
               "لأن قلة ممن قالوا إن ذلك ممكن لم يذكروا مدى صعوبته. و" + NO_GROUP_INTERVAL_AR
               + "، وتستند الفئات إلى عينات أصغر، والفرق بين الفئات ليس سببًا.",
    definition_en="What adults aged 15 and over in the areas the survey covered said about coming up with emergency funds "
                  "within 30 days, and how difficult it would be, in the four answer categories the World Bank publishes "
                  "for Yemen's 2021 wave, for all adults and by group; \"not possible\" includes adults who did not know "
                  "or did not answer, as the World Bank counts them. The survey also asked about 7 days; the World Bank "
                  "publishes no value for that question.",
    definition_ar="ما قاله البالغون بعمر 15 سنة فأكثر في المناطق التي شملها المسح عن تدبير أموال للطوارئ خلال "
                  "30 يومًا، ومدى صعوبة ذلك، في فئات الإجابة الأربع التي ينشرها البنك الدولي لموجة 2021 الخاصة باليمن، "
                  "لجميع البالغين ولكل فئة؛ وتشمل فئة «غير ممكن» البالغين الذين لم يعرفوا أو لم يجيبوا، كما يحتسبهم البنك "
                  "الدولي. وسأل المسح أيضًا عن مهلة 7 أيام، ولا ينشر البنك الدولي قيمة لذلك السؤال.",
    limitations_en="The answers are self-assessments of a hypothetical emergency, not observed events, and the ordered "
                   "categories do not form a resilience score; no method for combining them is used here. A difference "
                   "between groups does not establish its cause, and " + NO_GROUP_INTERVAL_EN + ". Saying the money "
                   "could be raised does not show where it would come from: it may be borrowed, including from family "
                   "and friends.",
    limitations_ar="الإجابات تقديرات ذاتية لحالة طارئة افتراضية، لا أحداث مرصودة، ولا تشكّل فئات الإجابة المرتبة درجة "
                   "مركبة للصمود، ولا تُستخدم هنا أي طريقة لدمجها. والفرق بين الفئات لا يثبت سببه، و" + NO_GROUP_INTERVAL_AR
                   + ". والقول بإمكان تدبير المال لا يبين مصدره: فقد يكون مقترضًا، بما في ذلك من الأسرة والأصدقاء.",
)
V["VIS-FINDEX-FLOW-CHANNELS"] = dict(
    title_en="Wages, agricultural payments and domestic remittances, by group",
    title_ar="الأجور والمدفوعات الزراعية والحوالات المحلية بحسب الفئة",
    question_en="Which adults received wages or agricultural payments, or sent or received domestic remittances, in the "
                "World Bank's published values?",
    question_ar="من هم البالغون الذين تلقوا أجورًا أو مدفوعات زراعية، أو أرسلوا حوالات محلية أو تلقوها، في القيم التي "
                "ينشرها البنك الدولي؟",
    shows_en="The World Bank's published shares of adults who received wages, received payments for agricultural sales, "
             "sent domestic remittances, received them, or did either, for all adults and by group.",
    shows_ar="النسب التي ينشرها البنك الدولي للبالغين الذين تلقوا أجورًا، أو تلقوا مدفوعات عن مبيعات زراعية، أو أرسلوا "
             "حوالات محلية، أو تلقوها، أو قاموا بأيٍّ من الأمرين، لجميع البالغين وبحسب الفئة.",
    value_en="Shows how common each kind of payment received or sent is, as a share of all adults in each group, so that "
             "receiving money is not mistaken for financial use or for a payment volume.",
    value_ar="يبين مدى شيوع كل نوع من المدفوعات المتلقاة أو المرسلة، بوصفه نسبة من جميع البالغين في كل فئة، حتى لا يُقرأ "
             "تلقي المال استخدامًا ماليًا أو حجمًا للمدفوعات.",
    encoding="Table: one row per group, one column per payment type, values as the World Bank publishes them (one "
             "decimal), each a share of all adults in the group; channels are not shown.",
    prohibited_en="Each value is a share of all adults in the group, not of recipients, and is not a payment volume or a "
                  "programme outcome; a difference between groups is not a cause. The channels through which money was "
                  "paid, sent or received are not shown.",
    prohibited_ar="كل قيمة نسبة من جميع البالغين في الفئة، لا من المتلقين، وليست حجمًا للمدفوعات ولا نتيجةً لبرنامج؛ والفرق "
                  "بين الفئات ليس سببًا. ولا تُعرض القنوات التي دُفعت أو أُرسلت أو استُلمت عبرها الأموال.",
    summary_en="World Bank published values for Yemen's Global Findex 2021 wave: 12.4% of adults received wages, 28.9% "
               "received payments for agricultural sales, 17.7% sent domestic remittances, 31.9% received them and "
               "37.8% did either. The table gives each share by sex, age, education, income and labour-force status. "
               "Each is a share of all adults in the group; " + NO_GROUP_INTERVAL_EN + ", and a difference between "
               "groups is not a cause.",
    summary_ar="قيم ينشرها البنك الدولي لموجة 2021 من Global Findex الخاصة باليمن: تلقى 12.4% من البالغين أجورًا، وتلقى "
               "28.9% مدفوعات عن مبيعات زراعية، وأرسل 17.7% حوالات محلية، وتلقاها 31.9%، وقام 37.8% بأيٍّ من الأمرين. "
               "ويعرض الجدول كل نسبة بحسب الجنس والعمر والتعليم والدخل والمشاركة في قوة العمل. وكل منها نسبة من جميع "
               "البالغين في الفئة؛ و" + NO_GROUP_INTERVAL_AR + "، والفرق بين الفئات ليس سببًا.",
    definition_en="Shares of adults aged 15 and over in the areas the survey covered who, in the past year, received "
                  "wages, received payments for agricultural sales, sent domestic remittances, received them, or did "
                  "either, as the World Bank publishes them for Yemen's 2021 wave, for all adults and by group.",
    definition_ar="نسب البالغين بعمر 15 سنة فأكثر في المناطق التي شملها المسح الذين تلقوا خلال السنة الماضية أجورًا، أو "
                  "مدفوعات عن مبيعات زراعية، أو أرسلوا حوالات محلية، أو تلقوها، أو قاموا بأيٍّ من الأمرين، كما ينشرها البنك "
                  "الدولي لموجة 2021 الخاصة باليمن، لجميع البالغين ولكل فئة.",
    limitations_en="Each value is a share of all adults, not of recipients, and does not measure payment volumes, "
                   "programme outcomes or remittance flows for the economy as a whole. The channels through which money "
                   "was paid, sent or received are not shown: the World Bank publishes most channel values for all "
                   "adults only, and Yemen's survey did not ask the mobile-money questions. A difference between groups "
                   "does not establish its cause.",
    limitations_ar="كل قيمة نسبة من جميع البالغين لا من المتلقين، ولا تقيس أحجام المدفوعات ولا نتائج البرامج ولا تدفقات "
                   "الحوالات على مستوى الاقتصاد ككل. ولا تُعرض القنوات التي دُفعت أو أُرسلت أو استُلمت عبرها الأموال: "
                   "فالبنك الدولي ينشر معظم قيم القنوات لجميع البالغين فقط، ولم يطرح مسح اليمن أسئلة خدمات الأموال عبر "
                   "الهاتف. والفرق بين الفئات لا يثبت سببه.",
)
BARRIERS = OrderedDict([
    ("summary_en", "The World Bank publishes no value for Yemen's 2021 wave on the reasons adults give for not having an "
                   "account: none of its Global Findex series on these reasons has a Yemen value (open World Bank data "
                   "API, source 28, checked on 10 October 2026), so no values are shown. The survey asked the questions, "
                   "so a value would require computation from licensed respondent-level data, which this resource does "
                   "not do. Any value published later must state its base."),
    ("summary_ar", "لا ينشر البنك الدولي أي قيمة لموجة 2021 الخاصة باليمن عن الأسباب التي يذكرها البالغون لعدم امتلاك "
                   "حساب: فلا قيمة لليمن في أيٍّ من سلاسل Global Findex عن هذه الأسباب (واجهة البيانات المفتوحة للبنك "
                   "الدولي، المصدر 28، جرى التحقق في 10 أكتوبر 2026)، لذلك لا تُعرض أي قيم. وقد طرح المسح هذه الأسئلة، لذلك "
                   "تتطلب أي قيمة احتسابًا من بيانات المستجيبين المرخّصة، وهو ما لا يقوم به هذا المورد. وأي قيمة تُنشر "
                   "لاحقًا يجب أن تذكر قاعدتها."),
    ("definition_en", "The reasons that adults aged 15 and over without an account, in the areas the survey covered, give "
                      "for not having one, as asked in the Yemen Findex 2021 survey; the World Bank publishes no value for "
                      "Yemen."),
    ("definition_ar", "الأسباب التي يذكرها البالغون بعمر 15 سنة فأكثر الذين لا يملكون حسابًا، في المناطق التي شملها المسح، "
                      "لعدم امتلاكهم حسابًا، كما وردت في مسح Findex 2021 لليمن؛ ولا ينشر البنك الدولي أي قيمة لليمن."),
    ("method_en", "The open World Bank data API (Global Findex database, source 28) was checked on 10 October 2026 for every "
                  "series on the reasons for not having an account: none has a value for Yemen. The study's public "
                  "metadata show that the questions were asked. This resource does not compute values from "
                  "respondent-level data."),
    ("method_ar", "جرى التحقق في 10 أكتوبر 2026 من واجهة البيانات المفتوحة للبنك الدولي (قاعدة بيانات Global Findex، المصدر "
                  "28) لكل سلسلة عن أسباب عدم امتلاك حساب: ولا قيمة لأيٍّ منها لليمن. وتُظهر البيانات الوصفية العامة للدراسة "
                  "أن هذه الأسئلة طُرحت. ولا يحتسب هذا المورد قيمًا من بيانات المستجيبين."),
    ("currentness_en", "No values are shown. The 2021 Findex wave, with Yemen fieldwork from 7 November 2022 to 9 January "
                       "2023, is the latest wave available for Yemen: " + LATER_EN + "."),
    ("currentness_ar", "لا تُعرض أي قيم. وموجة Findex 2021، التي نُفذ عملها الميداني في اليمن من 7 نوفمبر 2022 إلى 9 يناير "
                       "2023، هي أحدث موجة متاحة لليمن: " + LATER_AR[1:] + "."),
])

# CLM-026 (CR-03): the panel and its 16 published measures
CLM026 = OrderedDict([
    ("title_en", "Demand-side panel: 16 of its 32 measures have World Bank published values for Yemen"),
    ("title_ar", "مجموعة مقاييس جانب الطلب: لـ16 من مقاييسها الـ32 قيم ينشرها البنك الدولي لليمن"),
    ("summary_en",
     "A 32-measure demand-side panel has been specified across access, barriers, digital use, saving, borrowing, "
     "resilience, remittances, income flows, financial worry and connectivity. Sixteen of its measures have values that "
     "the World Bank publishes for Yemen in the 2021 wave: an account (11.9% of adults) and an account at a financial "
     "institution (11.9%); saving any money (21.6%) and saving at a financial institution (3.1%); borrowing any money "
     "(51.3%), from a financial institution (1.8%) and from family or friends (41.1%); saying that emergency funds within "
     "30 days would not be possible, or not knowing or not answering (10.8%; the other three answers are in the "
     "emergency-funds table on /people/); "
     "sending (17.7%), receiving (31.9%) or either sending or receiving (37.8%) domestic remittances; receiving wages "
     "(12.4%), a government transfer (3.8%) or payments for agricultural sales (28.9%); making or receiving a digital "
     "payment (9.3%); and making a digital merchant payment (0.6%). Of the other 16, two were not asked in Yemen's survey "
     "and 14 have no World Bank published value for Yemen."),
    ("summary_ar",
     "حُدِّدت مجموعة من 32 مقياسًا لجانب الطلب تغطي الوصول والعوائق والاستخدام الرقمي والادخار والاقتراض والقدرة على الصمود "
     "والحوالات وتدفقات الدخل والقلق المالي والاتصال. ولستة عشر من مقاييسها قيم ينشرها البنك الدولي لليمن في موجة 2021: "
     "امتلاك حساب (11.9% من البالغين) وحساب لدى مؤسسة مالية (11.9%)؛ وادخار أي مبلغ (21.6%) والادخار لدى مؤسسة مالية (3.1%)؛ "
     "واقتراض أي مبلغ (51.3%) والاقتراض من مؤسسة مالية (1.8%) ومن الأسرة أو الأصدقاء (41.1%)؛ والقول بعدم إمكان تدبير أموال "
     "للطوارئ خلال 30 يومًا، أو عدم المعرفة أو عدم الإجابة (10.8%؛ وترد الإجابات الثلاث الأخرى في جدول أموال الطوارئ في "
     "صفحة /people/)؛ وإرسال حوالات محلية "
     "(17.7%) وتلقيها (31.9%) أو أيٍّ من الأمرين (37.8%)؛ وتلقي أجور (12.4%) أو تحويل حكومي (3.8%) أو مدفوعات عن مبيعات زراعية "
     "(28.9%)؛ وإجراء مدفوعة رقمية أو تلقيها (9.3%)؛ وإجراء مدفوعة رقمية لتاجر (0.6%). أما المقاييس الـ16 الأخرى، فلم يُطرح "
     "اثنان منها في مسح اليمن، ولا توجد لـ14 منها قيمة ينشرها البنك الدولي لليمن."),
    ("definition_en",
     "This record describes a set of 32 defined people-side measures for the Yemen Findex 2021 study and carries the 16 of "
     "them that the World Bank publishes for Yemen, each as a share of adults aged 15 and over in the areas the survey "
     "covered; values by group, for the 11 measures the World Bank publishes by group, are shown in the three tables "
     "of /people/."),
    ("definition_ar",
     "يصف هذا السجل مجموعة من 32 مقياسًا محددًا على جانب الأفراد لدراسة Findex 2021 الخاصة باليمن، ويحمل المقاييس الـ16 منها التي "
     "ينشرها البنك الدولي لليمن، وكل منها نسبة من البالغين بعمر 15 سنة فأكثر في المناطق التي شملها المسح؛ وتُعرض القيم بحسب "
     "الفئة، للمقاييس الـ11 التي ينشر البنك الدولي قيمها بحسب الفئة، في الجداول الثلاثة في صفحة /people/."),
    ("universe_en",
     "A pre-specified 32-measure panel: 16 measures with World Bank published values for Yemen; 14 measures the survey "
     "asked but for which the World Bank publishes no Yemen value, so that a value would require computation from "
     "licensed respondent-level data; and two mobile-money measures that Yemen's survey did not ask."),
    ("universe_ar",
     "مجموعة محددة مسبقًا من 32 مقياسًا: 16 مقياسًا لها قيم ينشرها البنك الدولي لليمن؛ و14 مقياسًا طرح المسح أسئلتها لكن "
     "البنك الدولي لا ينشر لها قيمة لليمن، لذلك تتطلب أي قيمة لها احتسابًا من بيانات المستجيبين المرخّصة؛ ومقياسان لخدمات "
     "الأموال عبر الهاتف لم يطرحهما مسح اليمن."),
    ("limitations_en",
     "Of the 32 specified measures, 14 have no World Bank published value for Yemen in this wave and this resource does not "
     "compute them from respondent-level data, so they are planned, not measured; two (using and saving with a mobile-money "
     "account) were not asked in Yemen's survey, so no value exists for this wave. | In this record, saving any money, "
     "borrowing any money and making or receiving a digital payment carry a 95% interval computed by CauseWay "
     "(account ownership has a margin of error in VIS-FINDEX-GAPS); the other published values, and every group "
     "value, are shown without one. The published measures are shares of all adults in the areas the survey covered, "
     "each on its own question base. They do not add up and are not stages of one process: borrowing any money includes "
     "borrowing from family and friends, which needs no provider, and making or receiving a digital payment is not a "
     "measure of account ownership."),
    ("limitations_ar",
     "من المقاييس المحددة البالغة 32، لا توجد لـ14 منها قيمة منشورة من البنك الدولي لليمن في هذه الموجة، ولا يحتسبها هذا "
     "المورد من بيانات المستجيبين، لذلك تبقى مخططة لا مقاسة؛ ولم يُطرح سؤالا مقياسين منها (استخدام حساب لخدمات الأموال عبر "
     "الهاتف والادخار به) في مسح اليمن، لذلك لا توجد لهما قيمة في هذه الموجة. | وفي هذا السجل، تحمل قيم ادخار أي مبلغ واقتراض أي "
     "مبلغ وإجراء مدفوعة رقمية أو تلقيها فترة ثقة 95% من احتساب CauseWay (ولامتلاك الحساب هامش خطأ في السجل "
     "VIS-FINDEX-GAPS)؛ وتُعرض القيم المنشورة الأخرى، وكل قيم الفئات، دونها. والمقاييس "
     "المنشورة نسب من جميع البالغين في المناطق التي شملها المسح، ولكل منها قاعدة سؤاله الخاصة. ولا تُجمع هذه النسب ولا تمثل "
     "مراحل في مسار واحد: فاقتراض أي مبلغ يشمل الاقتراض من الأسرة والأصدقاء وهو لا يحتاج مقدم خدمة، وإجراء مدفوعة رقمية أو "
     "تلقيها ليس مقياسًا لامتلاك الحساب."),
    ("currentness_en",
     "The panel and its published values apply to the Yemen Findex 2021 study, whose fieldwork ran from 7 November 2022 "
     "to 9 January 2023 and which World Bank Data labels 2022. The other measures stay unpublished unless the World Bank "
     "publishes a value for them; the two that Yemen's survey did not ask have none for this wave. A newer wave would "
     "require an updated panel."),
    ("currentness_ar",
     "تنطبق مجموعة المقاييس وقيمها المنشورة على دراسة اليمن ضمن Findex 2021، التي نُفذ عملها الميداني من 7 نوفمبر 2022 إلى 9 "
     "يناير 2023 ويعرضها موقع بيانات البنك الدولي لسنة 2022. وتبقى المقاييس الأخرى غير منشورة ما لم ينشر البنك الدولي قيمة "
     "لها؛ ولا قيمة في هذه الموجة للمقياسين اللذين لم يطرحهما مسح اليمن. وتحتاج أي موجة أحدث إلى تحديث مجموعة المقاييس."),
])

CLM026_METHOD_OLD_EN = ("The variables, definitions and derivations were specified in advance, and a numeric estimate is "
                        "published only after authorized respondent-level data are available, the correct survey weights are "
                        "applied and the official benchmark values are reproduced. For these three measures all three "
                        "conditions are met: the respondent file was supplied under the World Bank Microdata Research "
                        "License, the published survey weight was used, and each measure's weighted estimate reproduces the "
                        "World Bank's own published value for Yemen in 2022. ")
CLM026_METHOD_OLD_AR = ("تُحدد المتغيرات والتعريفات وطريقة الاحتساب مسبقًا، ولا يُنشر تقدير رقمي إلا بعد توفر بيانات المستجيبين "
                        "المصرح باستخدامها، وتطبيق أوزان المسح الصحيحة، وإعادة إنتاج القيم المرجعية الرسمية. ولهذه المقاييس "
                        "الثلاثة استوفيت الشروط الثلاثة: فقد أُتيح ملف المستجيبين بموجب رخصة البحث للبيانات الجزئية لدى البنك "
                        "الدولي، واستُخدم وزن المسح المنشور، ويعيد التقدير الموزون لكل مقياس إنتاج القيمة التي نشرها البنك "
                        "الدولي نفسه لليمن في 2022. ")
CLM026_METHOD_NEW_EN = ("The measures were specified in advance. Their values are the World Bank's published estimates for "
                        "Yemen, read from the open World Bank data API (Global Findex database, source 28) on 10 October 2026 "
                        "and kept as a dated snapshot; each series is matched to its measure by the World Bank's own "
                        "indicator label, never by a questionnaire code. No respondent-level data are used. ")
CLM026_METHOD_NEW_AR = ("حُدِّدت المقاييس مسبقًا. وقيمها هي التقديرات التي ينشرها البنك الدولي لليمن، قُرئت من واجهة البيانات "
                        "المفتوحة للبنك الدولي (قاعدة بيانات Global Findex، المصدر 28) في 10 أكتوبر 2026 وحُفظت في لقطة مؤرخة؛ "
                        "وطوبقت كل سلسلة مع مقياسها وفق تسمية المؤشر لدى البنك الدولي نفسه، ولا تُطابَق أبدًا وفق رمز الاستبيان. ولا تُستخدم أي "
                        "بيانات على مستوى المستجيبين. ")
CLM026_INTERVAL_OLD_EN = "The 95% interval beside each is computed by CauseWay"
CLM026_INTERVAL_NEW_EN = "The 95% interval beside saving, borrowing and digital payments is computed by CauseWay"
CLM026_INTERVAL_OLD_AR = "وفترة الثقة 95% بجانب كل قيمة تحتسبها CauseWay"
CLM026_INTERVAL_NEW_AR = "وفترة الثقة 95% بجانب قيم الادخار والاقتراض والمدفوعات الرقمية تحتسبها CauseWay"

SRC_AGG_TITLE = ("Global Findex indicators for Yemen, adults 15+, total and by group: account ownership, saving, "
                 "borrowing, emergency funds, payments received and domestic remittances (World Bank data year 2022)")
SRC_AGG_TITLE_AR = ("مؤشرات Global Findex لليمن، البالغون بعمر 15 سنة فأكثر، الإجمالي وبحسب الفئة: امتلاك الحساب والادخار "
                    "والاقتراض وأموال الطوارئ والمدفوعات المتلقاة والحوالات المحلية (سنة بيانات البنك الدولي 2022)")
API_SOURCE_URL = "https://api.worldbank.org/v2/sources/28"

FIXTURE_REL = "audit/close_out/fixtures/findex_api_2026-10-10.json"

# ------------------------------------------------------------------------------------------------ records that said
# "not yet produced" (one object, one state: every place that describes these values says what is published now)
SITE_META = OrderedDict([  # route -> (en anchor, ar anchor, new en, new ar)
    ("/evidence/CLM-026/", (
        "custom weighted estimates are not yet published", "ولم تُنشر التقديرات الموزونة المخصصة بعد",
        "A 32-measure demand-side panel for Yemen's Findex 2021 study; 16 of its measures have World Bank published "
        "values, listed in the record.",
        "مجموعة من 32 مقياسًا لجانب الطلب لدراسة Findex 2021 الخاصة باليمن؛ ولـ16 من مقاييسها قيم ينشرها البنك الدولي، وهي "
        "مدرجة في السجل.")),
    ("/evidence/VIS-FINDEX-ACCESS-USE/", (
        "are not yet produced", "ولم تُنتج بعد",
        "World Bank published values for Yemen's Findex 2021 wave: 11.9% of adults had an account; saving and borrowing "
        "shares are given for all adults and by group.",
        "قيم ينشرها البنك الدولي لموجة Findex 2021 الخاصة باليمن: كان لدى 11.9% من البالغين حساب؛ وتُعرض نسب الادخار "
        "والاقتراض لجميع البالغين وبحسب الفئة.")),
    ("/evidence/VIS-FINDEX-BARRIERS/", (
        "are not yet produced", "لم تُنتج بعد",
        "The World Bank publishes no Yemen value for the 2021 wave on why adults without an account do not have one, so "
        "no values are shown.",
        "لا ينشر البنك الدولي أي قيمة لليمن في موجة 2021 عن أسباب عدم امتلاك البالغين حسابًا، لذلك لا تُعرض أي قيم.")),
    ("/evidence/VIS-FINDEX-FLOW-CHANNELS/", (
        "are not yet produced", "لم تُنتج بعد",
        "World Bank published values for Yemen's Findex 2021 wave: shares of adults who received wages or agricultural "
        "payments, or sent or received domestic remittances, for all adults and by group.",
        "قيم ينشرها البنك الدولي لموجة Findex 2021 الخاصة باليمن: نسب البالغين الذين تلقوا أجورًا أو مدفوعات زراعية، أو "
        "أرسلوا حوالات محلية أو تلقوها، لجميع البالغين وبحسب الفئة.")),
    ("/evidence/VIS-FINDEX-RESILIENCE/", (
        "are not yet produced", "لم تُنتج بعد",
        "World Bank published values for Yemen's Findex 2021 wave: what adults said about coming up with emergency funds "
        "within 30 days, and how difficult it would be, for all adults and by group.",
        "قيم ينشرها البنك الدولي لموجة Findex 2021 الخاصة باليمن: ما قاله البالغون عن تدبير أموال للطوارئ خلال 30 يومًا "
        "ومدى صعوبة ذلك، لجميع البالغين وبحسب الفئة.")),
    ("/evidence/CLM-031/", (
        "centre on 2014", "تتركز أدلة",
        "People-side evidence has no single latest year: most functions are measured in the 2021 Findex wave (2022), "
        "historical detail is from 2014, and the reasons for not having an account have no value.",
        "لا تشترك أدلة الأفراد في سنة واحدة هي الأحدث: تُقاس معظم الوظائف في موجة Findex 2021 (2022)، وتعود التفاصيل التاريخية إلى "
        "2014، ولا توجد قيمة لأسباب عدم امتلاك الحساب.")),
    ("/evidence/VIS-DEMAND-VINTAGE-LADDER/", (
        "from 2014", "من 2014",
        "As checked on 10 October 2026, the latest evidence on people comes from the 2021 Findex wave for most functions; "
        "the World Bank publishes no Yemen value for the reasons for not having an account.",
        "وفق التحقق في 10 أكتوبر 2026، يأتي أحدث دليل عن الأفراد من موجة Findex 2021 لمعظم الوظائف؛ ولا ينشر البنك الدولي "
        "أي قيمة لليمن لأسباب عدم امتلاك الحساب.")),
])
SAMPLE_SUPPORT = OrderedDict([  # field -> (anchor, new)
    ("summary_en", ("have not yet been produced",
                    "No counts are shown here. The 2021-wave values shown on /people/ are the World Bank's published "
                    "estimates; the study's public metadata record, for each question, the number of valid and of "
                    "missing or invalid answers, but these counts are not yet shown in this resource. Such counts "
                    "describe the sample and are not population estimates.")),
    ("summary_ar", ("لم تُنتج بعد",
                    "لا تُعرض هنا أي أعداد. والقيم المعروضة لموجة 2021 في صفحة /people/ هي التقديرات التي ينشرها البنك "
                    "الدولي؛ وتسجل البيانات الوصفية العامة للدراسة، لكل سؤال، عدد الإجابات الصالحة وعدد الإجابات المفقودة "
                    "أو غير الصالحة، لكن هذه الأعداد لا تُعرض بعد في هذا المورد. وهذه الأعداد تصف العينة وليست تقديرات "
                    "سكانية.")),
    ("currentness_en", ("When they are produced",
                        "No counts are shown yet. They would refer to the 2021 Findex wave, with Yemen fieldwork from 7 "
                        "November 2022 to 9 January 2023, the latest wave available for Yemen.")),
    ("currentness_ar", ("وعند إنتاجها",
                        "لا تُعرض أي أعداد بعد. وستعود إلى موجة Findex 2021، التي نُفذ عملها الميداني في اليمن من 7 نوفمبر "
                        "2022 إلى 9 يناير 2023، وهي أحدث موجة متاحة لليمن.")),
])
LADDER = OrderedDict([
    ("summary_en", ("18.3% received them",
                    "The latest weighted evidence for each financial function: the 2021 Findex wave gives World Bank "
                    "published values, for the year World Bank Data labels 2022, for account ownership (11.9%), saving "
                    "(21.6%) and borrowing (51.3%) any money, making or receiving a digital payment (9.3%), receiving "
                    "domestic remittances (31.9%) and emergency funds within 30 days (10.8% of adults said it would not "
                    "be possible, or did not know or answer); the World Bank publishes no Yemen value for the reasons adults give for not having an "
                    "account, so that function has none.")),
    ("summary_ar", ("تلقاها 18.3%",
                    "أحدث دليل موزون لكل وظيفة مالية: تعطي موجة Findex 2021 قيمًا ينشرها البنك الدولي، للسنة التي يعرضها "
                    "موقع بيانات البنك الدولي بوصفها 2022، لامتلاك الحساب (11.9%)، ولادخار أي مبلغ (21.6%) واقتراضه "
                    "(51.3%)، ولإجراء مدفوعة رقمية أو تلقيها (9.3%)، ولتلقي الحوالات المحلية (31.9%)، ولأموال الطوارئ خلال "
                    "30 يومًا (قال 10.8% من البالغين إن ذلك غير ممكن، أو لم يعرفوا أو لم يجيبوا)؛ ولا ينشر البنك الدولي أي قيمة لليمن لأسباب عدم "
                    "امتلاك البالغين حسابًا، لذلك لا توجد لهذه الوظيفة قيمة.")),
    ("period_en", ("no weighted values yet",
                   "2022 (the 2021 Findex wave); no value for the reasons for not having an account")),
    ("period_ar", ("ولا توجد بعد قيم موزونة",
                   "2022 (موجة Findex 2021)؛ ولا توجد قيمة لأسباب عدم امتلاك الحساب")),
    ("currentness_en", ("2014 for domestic remittances",
                        "The latest observations are from the 2021 Findex wave (World Bank Data year 2022; fieldwork 7 "
                        "November 2022 to 9 January 2023) for account ownership, saving, borrowing, digital payments, "
                        "domestic remittances and emergency funds; the reasons for not having an account have no "
                        "published value. None of them describes a later period unless a newer comparable observation "
                        "is published.")),
    ("currentness_ar", ("و2014 للحوالات المحلية",
                        "أحدث المشاهدات من موجة Findex 2021 (سنة بيانات البنك الدولي 2022؛ والعمل الميداني من 7 نوفمبر "
                        "2022 إلى 9 يناير 2023) لامتلاك الحساب والادخار والاقتراض والمدفوعات الرقمية والحوالات المحلية "
                        "وأموال الطوارئ؛ ولا توجد قيمة منشورة لأسباب عدم امتلاك الحساب. ولا يصف أي منها فترة لاحقة ما لم "
                        "تُنشر مشاهدة أحدث قابلة للمقارنة.")),
])
REMIT_2014_CURRENT = OrderedDict([  # CLM-030 and VIS-DOMESTIC-REMITTANCE-PATH-2014 carry the same text
    ("currentness_en", ("so no later value is published here",
                        "The values refer to 2014, from the World Bank's 2014 country profile for Yemen. The World Bank's "
                        "current series for received domestic remittances carries a 2022 value from the 2021 Findex wave "
                        "(31.9% of adults), shown with its group values on /people/ and /remittances/, but it carries no "
                        "2014 value at all, while the figure on this record comes from the 2014 country profile. A series "
                        "that does not hold the earlier year cannot establish a change against it, so the two values are "
                        "not read as a trend. What it would take to compare them is a measurement question, not a "
                        "presentation one.")),
    ("currentness_ar", ("لذلك لا تُنشر هنا قيمة أحدث",
                        "تعود هذه القيم إلى عام 2014، وهي مأخوذة من الملف القطري لليمن الذي نشره البنك الدولي لعام 2014. "
                        "وسلسلة البنك الدولي الحالية لتلقي الحوالات المحلية تحمل قيمة لعام 2022 من موجة Findex 2021 (31.9% "
                        "من البالغين)، تُعرض مع قيم الفئات في صفحتي /people/ و/remittances/، لكنها لا تحمل أي قيمة لعام "
                        "2014، في حين أن القيمة في هذا السجل مأخوذة من الملف القطري لعام 2014. والسلسلة التي لا تحمل السنة "
                        "الأقدم لا تستطيع إثبات تغير مقابلها، لذلك لا تُقرأ القيمتان اتجاهًا. وما يلزم لمقارنتهما مسألة قياس، "
                        "لا مسألة عرض.")),
])
CLM031 = OrderedDict([
    ("summary_en", ("centered on 2014",
                    "The people-side evidence here does not have one latest year. The 2021 Findex wave (World Bank Data "
                    "year 2022) gives World Bank published values for account ownership, saving, borrowing, digital "
                    "payments, payments received, domestic remittances and emergency funds within 30 days; the 2014 "
                    "country profile gives the historical detail shown here on how adults borrowed, saved and received "
                    "domestic remittances in 2014; and the World Bank publishes no Yemen value for the reasons for not "
                    "having an account. The 2014 and 2021-wave results stay separate and are not read as a trend.")),
    ("summary_ar", ("تتركز الأدلة العامة",
                    "لا تشترك أدلة جانب الأفراد هنا في سنة واحدة هي الأحدث. فموجة Findex 2021 (سنة بيانات البنك الدولي 2022) "
                    "تعطي قيمًا ينشرها البنك الدولي لامتلاك الحساب والادخار والاقتراض والمدفوعات الرقمية والمدفوعات "
                    "المتلقاة والحوالات المحلية وأموال الطوارئ خلال 30 يومًا؛ ويعطي الملف القطري لعام 2014 التفاصيل "
                    "التاريخية المعروضة هنا عن كيفية اقتراض البالغين وادخارهم وتلقيهم الحوالات المحلية في 2014؛ ولا ينشر "
                    "البنك الدولي أي قيمة لليمن لأسباب عدم امتلاك الحساب. وتبقى نتائج 2014 ونتائج موجة 2021 منفصلة، ولا "
                    "تُقرأ اتجاهًا.")),
    ("period_en", ("centered on 2014",
                   "Function-specific people-side evidence: World Bank published values from the Findex 2021 wave (Yemen "
                   "fieldwork 2022–2023) for most functions, and the 2014 country profile for historical detail.")),
    ("period_ar", ("تتركز الأدلة العامة",
                   "أدلة جانب الأفراد بحسب الوظيفة المالية: قيم ينشرها البنك الدولي من موجة Findex 2021 (العمل الميداني في "
                   "اليمن خلال 2022–2023) لمعظم الوظائف، والملف القطري لعام 2014 للتفاصيل التاريخية.")),
    ("currentness_en", ("refer to 2014",
                        "Each function has its own latest observation: account ownership, saving, borrowing, digital "
                        "payments, payments received, domestic remittances and emergency funds refer to the 2021 Findex "
                        "wave, with Yemen fieldwork from 7 November 2022 to 9 January 2023; the historical detail refers "
                        "to 2014; the reasons for not having an account have no published value. Each is updated "
                        "separately when newer comparable evidence is published.")),
    ("currentness_ar", ("إلى 2014",
                        "لكل وظيفة أحدث مشاهدة خاصة بها: يعود امتلاك الحساب والادخار والاقتراض والمدفوعات الرقمية "
                        "والمدفوعات المتلقاة والحوالات المحلية وأموال الطوارئ إلى موجة Findex 2021، التي نُفذ عملها "
                        "الميداني في اليمن من 7 نوفمبر 2022 إلى 9 يناير 2023؛ وتعود التفاصيل التاريخية إلى 2014؛ ولا توجد "
                        "قيمة منشورة لأسباب عدم امتلاك الحساب. ويُحدَّث كل منها على حدة عند نشر دليل أحدث قابل للمقارنة.")),
])
MA001 = OrderedDict([
    ("current_evidence_en", (
        "The latest published people-level values for receiving domestic remittances, and through which channels, are "
        "from 2014; the 2021-wave microdata contain these questions, but weighted estimates have not yet been produced.",
        "The World Bank publishes 2021-wave values for domestic remittances: 17.7% of adults aged 15 and over in the "
        "areas surveyed sent them and 31.9% received them, also by group (shown on /people/); the channels through which "
        "the money moved are not shown.")),
    ("current_evidence_ar", (
        "كما تعود أحدث القيم المنشورة على مستوى الأفراد بشأن تلقي الحوالات المحلية وقنواتها إلى 2014؛ وتتضمن البيانات "
        "الفردية لموجة 2021 هذه الأسئلة، لكن التقديرات الموزونة لم تُنتج بعد.",
        "وينشر البنك الدولي قيمًا لموجة 2021 عن الحوالات المحلية: أرسلها 17.7% من البالغين بعمر 15 سنة فأكثر في المناطق "
        "التي شملها المسح، وتلقاها 31.9%، مع قيم بحسب الفئة (تُعرض في صفحة /people/)؛ ولا تُعرض القنوات التي انتقلت "
        "عبرها الأموال.")),
])
SECTION_ADD = [  # (route, order, lang, must contain, sentence appended to the body)
    ("/people/", 7, "en", "In the 2014 World Bank weighted country profile",
     " The 2021 wave's published values for domestic remittances are in the table of wages, agricultural payments and "
     "domestic remittances by group; they are not read against this 2014 profile as a trend, because the World Bank's "
     "current series holds no 2014 value."),
    ("/people/", 7, "ar", "في الملف القطري الموزون للبنك الدولي لعام 2014",
     " وترد القيم المنشورة لموجة 2021 عن الحوالات المحلية في جدول الأجور والمدفوعات الزراعية والحوالات المحلية بحسب "
     "الفئة؛ ولا تُقرأ مقابل ملف 2014 هذا اتجاهًا، لأن سلسلة البنك الدولي الحالية لا تحمل قيمة لعام 2014."),
    ("/remittances/", 6, "en", "The 2014 weighted World Bank profile",
     " The 2021 wave's published values for domestic remittances are in the table of wages, agricultural payments and "
     "domestic remittances by group; they are not read against this 2014 profile as a trend, because the World Bank's "
     "current series holds no 2014 value."),
    ("/remittances/", 6, "ar", "أفاد الملف الموزون للبنك الدولي لعام 2014",
     " وترد القيم المنشورة لموجة 2021 عن الحوالات المحلية في جدول الأجور والمدفوعات الزراعية والحوالات المحلية بحسب "
     "الفئة؛ ولا تُقرأ مقابل ملف 2014 هذا اتجاهًا، لأن سلسلة البنك الدولي الحالية لا تحمل قيمة لعام 2014."),
]

SECTION_REPLACE = [  # (route, order, lang, old fragment, new fragment): sentences the published values make false
    ("/people/", 6, "en",
     "For the sources people borrowed from and the methods they saved by, the latest values this resource holds are "
     "older, from the World Bank's 2014 country profile: 51.7% of adults borrowed from family or friends, 15.0% from a "
     "private informal lender and 0.4% from a financial institution, while 0.9% saved at a financial institution and "
     "4.5% through a savings club or a person outside the family. Those categories are not additive, each percentage "
     "applies to the all-adult base used by its question, and they are not subtracted from the 2022 figures above.",
     "For where people borrowed and saved, the same wave also gives World Bank published values: 41.1% of adults "
     "borrowed from family or friends and 1.8% from a financial institution, and 3.1% saved at a financial institution. "
     "These categories are not additive, and each percentage applies to the all-adult base used by its question. Older "
     "detail from the World Bank's 2014 country profile stays in its own records and is not read against the 2021 wave "
     "as a trend."),
    ("/people/", 6, "ar",
     "أما جهات الاقتراض وأساليب الادخار فأحدث ما يحمله هذا المورد عنها أقدم، من الملف القطري للبنك الدولي لعام 2014: فقد "
     "اقترض 51.7% من البالغين من الأسرة أو الأصدقاء، و15.0% من مقرض خاص غير رسمي، و0.4% من مؤسسة مالية، بينما ادخر 0.9% "
     "لدى مؤسسة مالية و4.5% عبر جمعية ادخار أو شخص من خارج الأسرة. وهذه الفئات غير قابلة للجمع، وكل نسبة تنطبق على قاعدة "
     "جميع البالغين المستخدمة في سؤالها، ولا تُطرح من أرقام 2022 أعلاه.",
     "أما جهات الاقتراض وأماكن الادخار، فتعطي الموجة نفسها عنها أيضًا قيمًا ينشرها البنك الدولي: فقد اقترض 41.1% من "
     "البالغين من الأسرة أو الأصدقاء و1.8% من مؤسسة مالية، وادخر 3.1% لدى مؤسسة مالية. وهذه الفئات غير قابلة للجمع، وكل "
     "نسبة تنطبق على قاعدة جميع البالغين المستخدمة في سؤالها. أما التفاصيل الأقدم من الملف القطري للبنك الدولي لعام 2014 "
     "فتبقى في سجلاتها الخاصة، ولا تُقرأ مقابل موجة 2021 اتجاهًا."),
    ("/methodology/", 4, "en",
     "or on 2014 values, and several — frequency of use, financial resilience, digital capability, affordability and "
     "differences by age — are defined in the 2021 survey data but not yet estimated.",
     "or on 2014 values; several — frequency of use, digital capability and affordability — are defined in the 2021 "
     "survey but have no World Bank published value for Yemen, and financial resilience is published only for emergency "
     "funds within 30 days."),
    ("/methodology/", 4, "ar",
     "أو إلى قيم 2014، كما أن عددًا منها — كتكرار الاستخدام والصمود المالي والقدرات الرقمية والقدرة على تحمل التكلفة "
     "والفروق بحسب العمر — معرَّف في بيانات مسح 2021 لكنه لم يُقدَّر بعد.",
     "أو إلى قيم 2014؛ كما أن عددًا منها — وهي تكرار الاستخدام والقدرات الرقمية والقدرة على تحمل التكلفة — معرَّف في مسح "
     "2021 لكن البنك الدولي لا ينشر له قيمة لليمن، ولا تُنشر قيم الصمود المالي إلا لتدبير أموال الطوارئ خلال 30 يومًا."),
]
RECORD_REPLACE = OrderedDict([  # (record, field) -> (old fragment, new fragment)
    (("CLM-031", "method_en"), (
        "account ownership to the 2021 Findex wave (World Bank data year 2022), and account use, saving, borrowing and "
        "domestic remittances to the World Bank's 2014 country profile.",
        "account ownership, saving, borrowing, digital payments, payments received, domestic remittances and emergency "
        "funds within 30 days to the World Bank's published values for the 2021 Findex wave (World Bank data year 2022), "
        "and historical detail to the World Bank's 2014 country profile.")),
    (("CLM-031", "method_ar"), (
        "امتلاك الحساب بموجة Findex 2021 (سنة البيانات لدى البنك الدولي 2022)، واستخدام الحساب والادخار والاقتراض والحوالات "
        "المحلية بالملف القطري للبنك الدولي لعام 2014؛",
        "امتلاك الحساب والادخار والاقتراض والمدفوعات الرقمية والمدفوعات المتلقاة والحوالات المحلية وأموال الطوارئ خلال 30 "
        "يومًا بالقيم التي ينشرها البنك الدولي لموجة Findex 2021 (سنة بيانات البنك الدولي 2022)، والتفاصيل التاريخية "
        "بالملف القطري للبنك الدولي لعام 2014؛")),
    (("DS-DEMAND-VINTAGE-LENS", "period_en"), (
        "2014 to 2022; no newer weighted values yet",
        "2022 (the 2021 Findex wave) for most functions; 2014 for historical detail; no value for the reasons for not "
        "having an account")),
    (("DS-DEMAND-VINTAGE-LENS", "period_ar"), (
        "من 2014 إلى 2022؛ ولا توجد بعد قيم موزونة أحدث",
        "2022 (موجة Findex 2021) لمعظم الوظائف؛ و2014 للتفاصيل التاريخية؛ ولا توجد قيمة لأسباب عدم امتلاك الحساب")),
    (("DS-DEMAND-VINTAGE-LENS", "currentness_en"), (
        "The latest evidence differs by function, from 2014 to 2022 (the 2021 Findex wave, fieldwork 7 November 2022 to 9 "
        "January 2023); for a function with no newer value, the older evidence is not current.",
        "Most functions refer to the 2021 Findex wave (fieldwork 7 November 2022 to 9 January 2023); historical detail "
        "refers to 2014, and the reasons for not having an account have no published value. For a function with no "
        "newer value, the older evidence is not current.")),
    (("DS-DEMAND-VINTAGE-LENS", "currentness_ar"), (
        "يختلف أحدث دليل بحسب الوظيفة، من 2014 إلى 2022 (موجة Findex 2021، والعمل الميداني من 7 نوفمبر 2022 إلى 9 يناير "
        "2023)؛ وأي وظيفة لا تتوفر لها قيمة أحدث يبقى دليلها الأقدم غير حديث.",
        "تعود معظم الوظائف إلى موجة Findex 2021 (العمل الميداني من 7 نوفمبر 2022 إلى 9 يناير 2023)؛ وتعود التفاصيل "
        "التاريخية إلى 2014، ولا توجد قيمة منشورة لأسباب عدم امتلاك الحساب. وأي وظيفة لا تتوفر لها قيمة أحدث يبقى دليلها "
        "الأقدم غير حديث.")),
    (("DS-FINDEX-HISTORY-CROSSWALK", "summary_en"), (
        "while separating publishable historical values from latest-wave measures whose required computation is not yet "
        "complete.",
        "while separating publishable historical values from the latest-wave measures, 16 of the 32 of which have World "
        "Bank published values.")),
    (("DS-FINDEX-HISTORY-CROSSWALK", "summary_ar"), (
        "بأحدث مجموعة مقاييس مخطط لها، مع الفصل الصريح بين القيم التاريخية القابلة للنشر والمقاييس الأحدث التي لم تُستكمل "
        "حساباتها المطلوبة بعد.",
        "بالمقاييس المحددة لأحدث موجة، مع الفصل الصريح بين القيم التاريخية القابلة للنشر ومقاييس أحدث موجة، التي لـ16 من "
        "مقاييسها الـ32 قيم ينشرها البنك الدولي.")),
    (("DS-FINDEX-HISTORY-CROSSWALK", "limitations_en"), (
        "and latest-wave values remain unavailable until the required computation and quality checks are complete.",
        "and a latest-wave measure without a World Bank published value has no value here.")),
    (("DS-FINDEX-HISTORY-CROSSWALK", "limitations_ar"), (
        "ولا تُنشر القيم الأحدث حتى تكتمل الحسابات المطلوبة وتنجح فحوص الجودة.",
        "ولا قيمة هنا لأي مقياس من أحدث موجة لا ينشر له البنك الدولي قيمة.")),
])
META_EXTRA = OrderedDict([
    ("/evidence/DS-FINDEX-HISTORY-CROSSWALK/", (
        "keeping publishable values apart from pending ones.", "مع الفصل بين القيم القابلة للنشر والمقاييس التي لم تُستكمل حساباتها.",
        "This comparability map links historical Findex measures for Yemen to those for the 2021 wave, 16 of whose 32 "
        "measures have World Bank published values.",
        "تربط خريطة قابلية المقارنة هذه مقاييس Findex التاريخية لليمن بمقاييس موجة 2021، التي لـ16 من مقاييسها الـ32 قيم "
        "ينشرها البنك الدولي.")),
])
BASELINE_CAVEAT = OrderedDict([  # 25: the FC-1 intervals the caveats still named (CR-02 replaced them)
    ("WB-FINDEX-OBS-2022-010", ("A 95% interval of 18.4% to 24.9% is derived from the respondent file (CW-FINDEX-MOE-2022-015).",
                                "A 95% interval of 18.1% to 25.2% is computed by CauseWay from the published value and the design "
                                "effect the World Bank publishes for the survey (CW-FINDEX-MOE-2022-015).")),
    ("WB-FINDEX-OBS-2022-011", ("A 95% interval of 47.1% to 55.5% is derived from the respondent file (CW-FINDEX-MOE-2022-016).",
                                "A 95% interval of 47.0% to 55.6% is computed by CauseWay from the published value and the design "
                                "effect the World Bank publishes for the survey (CW-FINDEX-MOE-2022-016).")),
    ("WB-FINDEX-OBS-2022-012", ("A 95% interval of 7.4% to 11.3% is derived from the respondent file (CW-FINDEX-MOE-2022-017).",
                                "A 95% interval of 6.8% to 11.8% is computed by CauseWay from the published value and the design "
                                "effect the World Bank publishes for the survey (CW-FINDEX-MOE-2022-017).")),
])


# ================================================================================================ helpers
def load_fixture():
    return json.load(open(FIXTURE, encoding="utf-8"))


def check_label(code, head, label, group_tail):
    if not (label.startswith(head) and label.endswith(group_tail)):
        raise TxError(f"{F}: {code} is labelled {label!r}; expected '{head} … {group_tail}' (labels map the series)")


def vs_read(t, code, ser):
    return {"t": t, "k": "v", "s": "READ", "src": SRC_AGG,
            "loc": ser[code]["url"].replace("https://", "") + f" (World Bank label '{ser[code]['label']}'), value "
                   f"{ser[code]['value']}, lastupdated {ser[code]['lastupdated']}; snapshot {FIXTURE_REL}, read 10 "
                   "October 2026"}


def vs_add(vs, entries):
    have = {e["t"] for e in vs}
    for e in entries:
        if e["t"] not in have:
            vs.append(dict(e))
            have.add(e["t"])
    return vs


def rewrite(t, rec, field, anchor, new, finding):
    cur = t.get(rec, field)
    if not isinstance(cur, str) or anchor not in cur:
        raise TxError(f"{finding} {t.sheet} {rec}.{field}: anchor {anchor[:60]!r} not found in {str(cur)[:80]!r}")
    t.set(finding, rec, field, new, cur)


def no_value(lq, rx):
    """The label query's series whose label matches rx: (all of them, those with a Yemen value)."""
    hits = [(c, v) for c, v in lq.items() if re.search(rx, v[0] or "")]
    return hits, [(c, v) for c, v in hits if v[1] is not None]


DATE_VS = [{"t": "7 November 2022", "k": "d", "s": "READ", "src": SRC_STUDY,
            "loc": "microdata.worldbank.org/index.php/catalog/5862/study-description > Data collection > Dates of Data "
                   "Collection: Start 2022-11-07"},
           {"t": "9 January 2023", "k": "d", "s": "READ", "src": SRC_STUDY,
            "loc": "microdata.worldbank.org/index.php/catalog/5862/study-description > Data collection > Dates of Data "
                   "Collection: End 2023-01-09"},
           {"t": "23%", "k": "v", "s": "READ", "src": SRC_STUDY,
            "loc": "microdata.worldbank.org/index.php/catalog/5862/study-description > Coverage > Geographic Coverage"},
           {"t": "1,000", "k": "v", "s": "READ", "src": SRC_STUDY,
            "loc": "The Global Findex Database 2021, Appendix A 'Survey Methodology', Table A.1, Yemen row, printed p.17: "
                   "1,000 interviews"},
           {"t": "10 October 2026", "k": "d", "s": "SITE"}, {"t": "15", "k": "v", "s": "TRIVIAL"},
           {"t": "28", "k": "v", "s": "TRIVIAL"}]


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    fx = load_fixture()
    ser, lq, ddi = fx["series"], fx["label_query"]["series"], fx["ddi_valid_cases"]["variables"]
    if fx["label_query"]["queried"] < 3000 or len(lq) < 3000:
        raise TxError(f"{F}: the label query holds {len(lq)} series; every source-28 series must be read")
    for code, rec in ser.items():
        if lq.get(code, [None, "absent"])[1] != rec["value"]:
            raise TxError(f"{F}: {code} differs between the series read and the label query")

    # ---------------------------------------------------------------- what is not published, checked by label
    held_reason = OrderedDict()   # FDP -> (kind, detail)
    for fdp, rx in NO_VALUE_LABELS.items():
        hits, vals = no_value(lq, rx)
        if vals:
            raise TxError(f"{F}: {fdp} is said to have no published value, but {vals[0][0]} ({vals[0][1][0]}) has "
                          f"{vals[0][1][1]}")
        if not hits and fdp not in NO_SERIES_OK:
            raise TxError(f"{F}: no source-28 series is labelled like {fdp} ({rx}); the label pattern must find them")
        held_reason[fdp] = ("NONE", len(hits))
    for fdp, var in NOT_ASKED.items():
        d = ddi.get(var)
        if not d or d["valid"] != 0:
            raise TxError(f"{F}: {fdp} ({var}) is said not to have been asked, but the DDI prints {d}")
        held_reason[fdp] = ("NOT_ASKED", var)
    for fdp, base in TOTAL_ONLY.items():
        if lq.get(base, [None, None])[1] is None:
            raise TxError(f"{F}: {fdp} ({base}) has no all-adults value")
        for dim, sfx in DIM_SUFFIX.items():
            for x in sfx:
                v = lq.get(base + x)
                if v is not None and v[1] is not None:
                    raise TxError(f"{F}: {fdp} is said to have only an all-adults value, but {base + x} has {v[1]}")
        held_reason[fdp] = ("TOTAL_ONLY", base)
    for var, d in ddi.items():   # every unpublished measure that is computable was asked
        if var not in NOT_ASKED.values() and d["valid"] == 0 and var not in ("fin34b", "fin39b", "fin43b"):
            raise TxError(f"{F}: {var} has no valid case in the DDI but is not treated as not asked")
    rural = [(c, v) for c, v in lq.items() if re.search(RURAL_RX, v[0] or "")]
    if len(rural) < 100 or any(v[1] is not None for _, v in rural):
        raise TxError(f"{F}: the rural/urban series are not all empty for Yemen ({len(rural)} read)")
    later = [r for r in fx["account_all_years"]["rows"] if int(r["date"]) > 2022]
    if not later or any(r["value"] is not None for r in later):
        raise TxError(f"{F}: the account series shows a later Yemen value or no later year: {later}")
    fh2 = {r["date"]: r["value"] for r in fx["received_domestic_remittances_all_years"]["rows"]}
    if fh2.get("2014") is not None or round(fh2.get("2022") or 0, 1) != 31.9:
        raise TxError(f"{F}: the received-remittances series does not read as recorded: {fh2}")

    # ---------------------------------------------------------------- 25_FINDEX_BASELINE: the published values
    t25 = Table(s, "25_FINDEX_BASELINE")
    head = t25.head
    for code, rid in LEGACY.items():
        want = round(ser[code]["value"], 1)
        got = float(t25.get(rid, "value"))
        if abs(got - want) > 1e-9:
            raise TxError(f"{F}: {rid} holds {got}, the World Bank publishes {want} ({code})")
    last = max(t25.rows.values())
    g = s.grid("25_FINDEX_BASELINE")
    if any(r and any(x not in (None, "") for x in r) for r in g[last:last + 3]):
        raise TxError(f"{F}: 25_FINDEX_BASELINE has content below row {last}")
    n = 13
    new_rows, by_code = [], OrderedDict()
    for fdp, base, label_head, groups in SERIES:
        for suffix, grp, tail in GROUPS:
            if grp not in groups:
                continue
            code = base + suffix
            if code not in ser or ser[code].get("value") is None:
                raise TxError(f"{F}: {code} has no published value in the snapshot")
            check_label(code, label_head, ser[code]["label"], tail)
            rid = f"WB-FINDEX-OBS-2022-{n:03d}"
            n += 1
            raw = ser[code]["value"]
            cav = (CAVEAT_TOTAL if grp == "total" else CAVEAT_GROUP).format(raw=raw)
            row = OrderedDict([("observation_id", rid), ("indicator_code", code), ("indicator", ser[code]["label"]),
                               ("group", grp), ("year", 2022), ("value", round(raw, 1)),
                               ("unit", UNIT.get(grp, "percent of population ages 15+")),
                               ("publisher", "World Bank Global Findex"), ("source_url", ser[code]["url"]),
                               ("evidence_state", "PUBLIC_PRIMARY_AGGREGATE"),
                               ("caveat", cav + f" Panel measure {fdp}.")])
            new_rows.append(row)
            by_code[code] = rid
    for code, rid in LEGACY.items():
        by_code.setdefault(code, rid)
    s.ed.insert_rows("25_FINDEX_BASELINE", last + 1, [{head.index(k) + 1: v for k, v in r.items()} for r in new_rows])
    for i, r in enumerate(new_rows):
        for k, v in r.items():
            s.ledger.append({"finding": F + ":U1", "sheet": "25_FINDEX_BASELINE", "row": last + 1 + i,
                             "col": head.index(k) + 1, "field": f"{r['observation_id']}.{k}", "old": None, "new": v})

    # ---------------------------------------------------------------- 27_FINDEX_SUBGROUPS: published, or why not
    t27 = Table(s, "27_FINDEX_SUBGROUPS")
    pub = withheld = rur = 0
    for key, row in t27.rows.items():
        if not str(key).startswith("FSG-"):
            continue
        fdp, dim, state = t27.get(key, "panel_metric_id"), t27.get(key, "subgroup_dimension"), t27.get(key, "current_state")
        if dim == "RURALITY":
            cur = t27.get(key, "public_behavior")
            if state != "DECIDED__NO_PUBLISHED_RURAL_URBAN_SPLIT" or "no rural/urban split" not in str(cur):
                raise TxError(f"{F}: {key} rural row reads {state!r} / {str(cur)[:60]!r}")
            t27.set(F + ":U1", key, "public_behavior",
                    str(cur).rstrip() + f" Re-checked 10 October 2026: none of the {len(rural)} rural or urban series of "
                    "the World Bank's Global Findex database (open API source 28) has a Yemen value.", cur)
            rur += 1
            continue
        if state == "PUBLIC_SAME_WAVE_GAP_READY":
            continue
        if state != "CONTROLLED_MICRODATA_WEIGHTED_COMPUTE_REQUIRED":
            raise TxError(f"{F}: {key} is in state {state!r}")
        if fdp in PUBLISHED_BY_GROUP:
            vis = PUBLISHED_BY_GROUP[fdp]
            where = "/people/ and /remittances/" if vis == "VIS-FINDEX-FLOW-CHANNELS" else "/people/"
            t27.set(F + ":U1", key, "current_state", "PUBLIC_WB_PUBLISHED_SAME_WAVE", state)
            t27.set(F + ":U1", key, "published_anchor_state", "WB_PUBLISHED_OPEN_API_SOURCE_28",
                    t27.get(key, "published_anchor_state"))
            t27.set(F + ":U1", key, "calculation_requirement",
                    "None: the World Bank publishes these values (open API, source 28); nothing is computed here.",
                    t27.get(key, "calculation_requirement"))
            t27.set(F + ":U1", key, "public_behavior",
                    f"Shown in {vis} ({where}): the World Bank's published values by {DIM_TEXT[dim]}; no interval "
                    "published here (EXT-07 held); each group rests on fewer than the 1,000 interviews; a difference "
                    "between groups is not a cause (CAUSE_HELD). Close-out U1, 10 October 2026.",
                    t27.get(key, "public_behavior"))
            pub += 1
            continue
        kind, detail = held_reason[fdp]
        if kind == "NOT_ASKED":
            d = ddi[detail]
            why = (f"Contract only: Yemen's survey did not ask this question (the study's public DDI metadata print no "
                   f"valid case for {detail}: valid {d['valid']}, invalid {d['invalid']}; {d['url']}), so the World Bank "
                   "publishes no value and no computation from licensed microdata (OWN-09) could produce one. Checked 10 "
                   "October 2026.")
            t27.set(F + ":U1", key, "current_state", "NOT_ASKED_IN_SURVEY", state)
            t27.set(F + ":U1", key, "calculation_requirement",
                    f"None possible: not asked in Yemen's survey (public DDI metadata, {detail}: valid 0).",
                    t27.get(key, "calculation_requirement"))
        elif kind == "TOTAL_ONLY":
            why = (f"Contract only: the World Bank publishes only the all-adults value for this measure for Yemen (series "
                   f"{detail}), not a value by {DIM_TEXT[dim]} (open API source 28, checked 10 October 2026); a value by "
                   f"{DIM_TEXT[dim]} requires computation from licensed microdata (OWN-09), which this resource does not "
                   "do.")
        elif detail == 0:   # the database has no such series at all (religious reasons; the 7-day question)
            why = ("Contract only: the World Bank's Global Findex database has no series for this measure (all source-28 "
                   "series checked by label, 10 October 2026), so it publishes no value for Yemen; a value requires "
                   "computation from licensed microdata (OWN-09), which this resource does not do.")
        else:
            why = ("Contract only: the World Bank publishes no value for this measure for Yemen (open API source 28: no "
                   "series labelled for it has a Yemen value; checked 10 October 2026); a value requires computation from "
                   "licensed microdata (OWN-09), which this resource does not do.")
        t27.set(F + ":U1", key, "public_behavior", why, t27.get(key, "public_behavior"))
        withheld += 1
    if (pub, withheld, rur) != (51, 105, 32):
        raise TxError(f"{F}: {pub} rows published, {withheld} withheld, {rur} rural; the brief counts 51, 105 (and 32)")

    # ---------------------------------------------------------------- 04: interface copy for the tables
    have = {r[0] for r in s.grid("04_NAV_UX") if r and isinstance(r[0], str)}
    if any(u[0] in have for u in UI):
        raise TxError(f"{F}: interface rows already present")
    insert_ui_rows(s, F + ":U1", [(a, b, c, d) for a, b, c, d in UI])

    # ---------------------------------------------------------------- the period copies CLM-001 (brief U1)
    t06 = Table(s, "06_EVIDENCE_OBJECTS")
    period_en, period_ar = t06.get("CLM-001", "period_en"), t06.get("CLM-001", "period_ar")
    period_vs = [e for e in json.loads(t06.get("CLM-001", "value_states"))
                 if e["t"] in ("01", "07", "09", "11") and (e["t"] in period_en)]
    if len(period_vs) != 4:
        raise TxError(f"{F}: CLM-001's period states are not the four date parts: {period_vs}")

    # ---------------------------------------------------------------- 11 + 06: three table-first visuals
    t11 = Table(s, "11_VISUAL_LIBRARY")
    h11 = t11.head
    last11 = max(t11.rows.values())
    g11 = s.grid("11_VISUAL_LIBRARY")
    if any(r and any(x not in (None, "") for x in r) for r in g11[last11:last11 + 3]):
        raise TxError(f"{F}: 11_VISUAL_LIBRARY has content below row {last11}")
    rows11 = []
    for vid, tx in V.items():
        if vid in t11.rows:
            raise TxError(f"{F}: {vid} already in 11")
        routes = ["/people", "/remittances"] if vid == "VIS-FINDEX-FLOW-CHANNELS" else ["/people"]
        rows11.append(OrderedDict([
            ("visual_id", vid), ("title_en", tx["title_en"]), ("title_ar", tx["title_ar"]), ("visual_form", "TABLE_TEXT_FIRST"),
            ("question_en", tx["question_en"]), ("question_ar", tx["question_ar"]),
            ("what_it_shows_en", tx["shows_en"]), ("what_it_shows_ar", tx["shows_ar"]),
            ("decision_value_en", tx["value_en"]), ("decision_value_ar", tx["value_ar"]),
            ("source_period", period_en),
            ("evidence_strength", "HIGH_PUBLISHED_SURVEY_AGGREGATE__GROUP_SAMPLES_SMALLER"),
            ("freshness_profile", "Global Findex 2021 wave; Yemen fieldwork 7 November 2022 to 9 January 2023"),
            ("data_inputs", "25_FINDEX_BASELINE WB-FINDEX-OBS-2022 rows (World Bank open API, source 28)"),
            ("unit_or_object", "percent of adults in each group"),
            ("denominator_universe", "Adults aged 15 and over in the areas the survey covered; each group as the World Bank "
                                     "defines it"),
            ("period", period_en), ("encoding_contract", tx["encoding"]),
            ("prohibited_inference_en", tx["limitations_en"]), ("prohibited_inference_ar", tx["limitations_ar"]),
            ("accessible_summary_en", tx["summary_en"]), ("accessible_summary_ar", tx["summary_ar"]),
            ("public_routes", json.dumps(routes)), ("period_ar", period_ar),
            ("universe_ar", "البالغون بعمر 15 سنة فأكثر في المناطق التي شملها المسح؛ وكل فئة كما يعرّفها البنك الدولي")]))
    s.ed.insert_rows("11_VISUAL_LIBRARY", last11 + 1, [{h11.index(k) + 1: v for k, v in r.items()} for r in rows11])
    for i, r in enumerate(rows11):
        for k, v in r.items():
            s.ledger.append({"finding": F + ":U1", "sheet": "11_VISUAL_LIBRARY", "row": last11 + 1 + i,
                             "col": h11.index(k) + 1, "field": f"{r['visual_id']}.{k}", "old": None, "new": v})

    nums = {
        "VIS-FINDEX-ACCESS-USE": [("11.9%", "account.t.d"), ("21.6%", "save.any.t.d"), ("51.3%", "borrow.any.t.d"),
                                  ("41.1%", "fin22b")],
        "VIS-FINDEX-RESILIENCE": [("10.8%", "fin24aN"), ("25.1%", "fin24aVD"), ("40.4%", "fin24aSD"), ("23.2%", "fin24aND")],
        "VIS-FINDEX-FLOW-CHANNELS": [("12.4%", "fin32"), ("28.9%", "fin42"), ("17.7%", "fh1"), ("31.9%", "fh2"),
                                     ("37.8%", "fh1.fh2")],
    }
    for vid, tx in V.items():
        f1 = F + ":U1"
        cur_vs = json.loads(t06.get(vid, "value_states") or "[]")
        for field, new in (("title_en", tx["title_en"]), ("title_ar", tx["title_ar"]), ("summary_en", tx["summary_en"]),
                           ("summary_ar", tx["summary_ar"]), ("definition_en", tx["definition_en"]),
                           ("definition_ar", tx["definition_ar"]), ("period_en", period_en), ("period_ar", period_ar),
                           ("universe_en", UNIVERSE_EN), ("universe_ar", UNIVERSE_AR),
                           ("method_en", METHOD_EN + tx.get("method_extra_en", "")),
                           ("method_ar", METHOD_AR + tx.get("method_extra_ar", "")),
                           ("limitations_en", tx["limitations_en"]), ("limitations_ar", tx["limitations_ar"]),
                           ("currentness_en", CURRENT_EN + tx.get("current_extra_en", "")),
                           ("currentness_ar", CURRENT_AR + tx.get("current_extra_ar", ""))):
            t06.set(f1, vid, field, new, t06.get(vid, field))
        t06.set(f1, vid, "source_dependencies", f"{SRC_STUDY}; {SRC_AGG}", t06.get(vid, "source_dependencies"))
        t06.set(f1, vid, "visual_contract_state", None, "NO_GOVERNED_CONTRACT__TABLE_ONLY")
        vs = [vs_read(t, code, ser) for t, code in nums[vid]]
        vs = vs_add(vs, DATE_VS + period_vs)
        # the group labels the table prints (ages 15–24 and 25+, poorest 40% and richest 60%) are names, not values
        vs = vs_add(vs, [{"t": x, "k": "v", "s": "TRIVIAL"} for x in ("24", "25", "40%", "60%")])
        if vid == "VIS-FINDEX-RESILIENCE":
            vs = vs_add(vs, [{"t": "30", "k": "v", "s": "TRIVIAL"}, {"t": "7", "k": "v", "s": "TRIVIAL"}])
        if vid == "VIS-FINDEX-ACCESS-USE":   # the digital-payment value and its CauseWay interval (CR-02) carry over
            keep = [e for e in cur_vs if e["t"] in ("9.3%", "95%", "6.8%", "11.8%")]
            if len(keep) != 4:
                raise TxError(f"{F}: VIS-FINDEX-ACCESS-USE does not hold the digital-payment states it prints")
            vs = vs_add(vs, keep)
        t06.set(f1, vid, "value_states", json.dumps(vs, ensure_ascii=False, separators=(",", ":")),
                t06.get(vid, "value_states"))
    for field, new in list(BARRIERS.items()) + [("period_en", period_en), ("period_ar", period_ar)]:
        t06.set(F + ":U1", "VIS-FINDEX-BARRIERS", field, new, t06.get("VIS-FINDEX-BARRIERS", field))
    cur = t06.get("VIS-FINDEX-BARRIERS", "value_states")
    vs = [e for e in json.loads(cur) if e["t"] not in ("November 2022", "January 2023")]
    vs = vs_add(vs, [e for e in DATE_VS if e["t"] in ("7 November 2022", "9 January 2023", "10 October 2026", "15", "28")]
                + period_vs)
    t06.set(F + ":U1", "VIS-FINDEX-BARRIERS", "value_states", json.dumps(vs, ensure_ascii=False, separators=(",", ":")), cur)

    # ---------------------------------------------------------------- CLM-026 (CR-03)
    f3 = F + ":CR-03"
    for field, new in list(CLM026.items()) + [("period_en", period_en), ("period_ar", period_ar)]:
        t06.set(f3, "CLM-026", field, new, t06.get("CLM-026", field))
    for lang, old, new, iold, inew in (("en", CLM026_METHOD_OLD_EN, CLM026_METHOD_NEW_EN, CLM026_INTERVAL_OLD_EN, CLM026_INTERVAL_NEW_EN),
                                       ("ar", CLM026_METHOD_OLD_AR, CLM026_METHOD_NEW_AR, CLM026_INTERVAL_OLD_AR, CLM026_INTERVAL_NEW_AR)):
        cur = t06.get("CLM-026", f"method_{lang}")
        if cur.count(old) != 1 or cur.count(iold) != 1:
            raise TxError(f"{f3}: CLM-026 method_{lang} is not the text expected")
        t06.set(f3, "CLM-026", f"method_{lang}", cur.replace(old, new).replace(iold, inew), cur)
    cur = t06.get("CLM-026", "value_states")
    vs = json.loads(cur)
    vs = vs_add(vs, [vs_read(t, code, ser) for t, code in (
        ("11.9%", "account.t.d"), ("3.1%", "fin17a"), ("1.8%", "fin22a"), ("41.1%", "fin22b"), ("10.8%", "fin24aN"),
        ("17.7%", "fh1"), ("31.9%", "fh2"), ("37.8%", "fh1.fh2"), ("12.4%", "fin32"), ("3.8%", "fin37"),
        ("28.9%", "fin42"), ("0.6%", "merchant.pay"))])
    vs = vs_add(vs, [{"t": "16", "k": "v", "s": "SITE"}, {"t": "14", "k": "v", "s": "SITE"},
                     {"t": "30", "k": "v", "s": "TRIVIAL"}, {"t": "10 October 2026", "k": "d", "s": "SITE"},
                     {"t": "28", "k": "v", "s": "TRIVIAL"}] + period_vs)
    t06.set(f3, "CLM-026", "value_states", json.dumps(vs, ensure_ascii=False, separators=(",", ":")), cur)

    # ---------------------------------------------------------------- records that said "not yet produced"
    f4 = F + ":U1"
    for field, (anchor, new) in SAMPLE_SUPPORT.items():
        rewrite(t06, "VIS-FINDEX-SAMPLE-SUPPORT", field, anchor, new, f4)
    for field, (anchor, new) in LADDER.items():
        rewrite(t06, "VIS-DEMAND-VINTAGE-LADDER", field, anchor, new, f4)
    cur = t06.get("VIS-DEMAND-VINTAGE-LADDER", "value_states")
    vs = vs_add(json.loads(cur), [vs_read("31.9%", "fh2", ser), vs_read("10.8%", "fin24aN", ser),
                                  {"t": "30", "k": "v", "s": "TRIVIAL"}])
    t06.set(f4, "VIS-DEMAND-VINTAGE-LADDER", "value_states", json.dumps(vs, ensure_ascii=False, separators=(",", ":")), cur)
    cur = t06.get("VIS-DEMAND-VINTAGE-LADDER", "source_dependencies")
    if "VIS-FINDEX-FLOW-CHANNELS" not in cur:
        t06.set(f4, "VIS-DEMAND-VINTAGE-LADDER", "source_dependencies",
                cur.rstrip() + "; VIS-FINDEX-FLOW-CHANNELS", cur)
    for rec in ("CLM-030", "VIS-DOMESTIC-REMITTANCE-PATH-2014"):
        for field, (anchor, new) in REMIT_2014_CURRENT.items():
            rewrite(t06, rec, field, anchor, new, f4)
        cur = t06.get(rec, "value_states")
        vs = vs_add(json.loads(cur), [vs_read("31.9%", "fh2", ser)])
        t06.set(f4, rec, "value_states", json.dumps(vs, ensure_ascii=False, separators=(",", ":")), cur)
    for field, (anchor, new) in CLM031.items():
        rewrite(t06, "CLM-031", field, anchor, new, f4)
    cur = t06.get("CLM-031", "value_states")
    vs = vs_add(json.loads(cur), [{"t": "30", "k": "v", "s": "TRIVIAL"}])
    t06.set(f4, "CLM-031", "value_states", json.dumps(vs, ensure_ascii=False, separators=(",", ":")), cur)
    cur = t06.get("CLM-031", "source_dependencies")
    if "CLM-026" not in cur:
        t06.set(f4, "CLM-031", "source_dependencies", cur.rstrip() + "; CLM-026", cur)
    t10 = Table(s, "10_MEASUREMENT_AGENDA")
    for field, (old, new) in MA001.items():
        cur = t10.get("MA-001", field)
        if not isinstance(cur, str) or cur.count(old) != 1:
            raise TxError(f"{f4}: MA-001.{field} does not hold the sentence expected")
        t10.set(f4, "MA-001", field, cur.replace(old, new), cur)
    t02 = Table(s, "02_SITE_MAP")
    for route, (a_en, a_ar, n_en, n_ar) in SITE_META.items():
        rewrite(t02, route, "meta_description_en", a_en, n_en, f4)
        rewrite(t02, route, "meta_description_ar", a_ar, n_ar, f4)
    for route, order, lang, must, add in SECTION_ADD:
        row = s.section_row(route, order, lang)
        cur = s.ed.get_value(S03, row, COL03["body_" + lang])
        if not isinstance(cur, str) or must not in cur or add.strip() in cur:
            raise TxError(f"{f4}: {route} s{order} {lang} is not the text expected")
        s.set(f4, S03, row, COL03["body_" + lang], cur.rstrip() + add, cur, f"{route}#s{order}.body_{lang}")
    for route, order, lang, old, new in SECTION_REPLACE:
        s.replace_section(f4, route, order, lang, "body", old, new)
    for (rec, field), (old, new) in RECORD_REPLACE.items():
        cur = t06.get(rec, field)
        if not isinstance(cur, str) or cur.count(old) != 1:
            raise TxError(f"{f4}: {rec}.{field} does not hold the text expected")
        t06.set(f4, rec, field, cur.replace(old, new), cur)
    for rec in ("DS-DEMAND-VINTAGE-LENS", "DS-FINDEX-HISTORY-CROSSWALK"):
        cur = t06.get(rec, "value_states")
        vs = vs_add(json.loads(cur or "[]"), [{"t": "16", "k": "v", "s": "SITE"}, {"t": "32", "k": "v", "s": "SITE"}]
                    if rec == "DS-FINDEX-HISTORY-CROSSWALK" else [])
        if json.dumps(vs, ensure_ascii=False, separators=(",", ":")) != (cur or "[]"):
            t06.set(f4, rec, "value_states", json.dumps(vs, ensure_ascii=False, separators=(",", ":")), cur)
    for route, (a_en, a_ar, n_en, n_ar) in META_EXTRA.items():
        rewrite(t02, route, "meta_description_en", a_en, n_en, f4)
        rewrite(t02, route, "meta_description_ar", a_ar, n_ar, f4)
    for rid, (old, new) in BASELINE_CAVEAT.items():
        cur = t25.get(rid, "caveat")
        if not isinstance(cur, str) or cur.count(old) != 1:
            raise TxError(f"{f4}: {rid} caveat does not hold the FC-1 interval expected")
        t25.set(f4, rid, "caveat", cur.replace(old, new), cur)
    t07 = Table(s, "07_PUBLIC_CLAIMS")
    t07.set(f3, "CLM-026", "evidence_badge", "ANALYTIC_CONTRACT_PLUS_WB_PUBLISHED_VALUES",
            "ANALYTIC_CONTRACT_PLUS_OPEN_MICRODATA_PENDING")

    # ---------------------------------------------------------------- 15: the aggregate source names what it now carries
    t15 = Table(s, "15_SOURCE_LIBRARY")
    t15.set(F + ":U1", SRC_AGG, "display_title", SRC_AGG_TITLE, t15.get(SRC_AGG, "display_title"))
    t15.set(F + ":U1", SRC_AGG, "display_title_ar", SRC_AGG_TITLE_AR, t15.get(SRC_AGG, "display_title_ar"))
    au = t15.get(SRC_AGG, "additional_urls")
    urls = json.loads(au) if au else []
    if API_SOURCE_URL not in urls:
        t15.set(F + ":U1", SRC_AGG, "additional_urls", json.dumps(urls + [API_SOURCE_URL]), au)
    t15.set(F + ":U1", SRC_AGG, "retrieval_date", "2026-10-10", t15.get(SRC_AGG, "retrieval_date"))

    # ---------------------------------------------------------------- the contract: three table-first visuals
    c = json.load(open(CONTRACT, encoding="utf-8"), object_pairs_hook=OrderedDict)
    if any(v["visual_id"] in TABLES for v in c["visuals"]):
        raise TxError(f"{F}: contract already holds the Findex tables")
    for vid, (cols, caption, markers) in TABLES.items():
        ids, must = [], OrderedDict()
        rows = []
        for grp, ui_row in ROW_UI.items():
            cells = []
            for base, _ in cols:
                code = base if grp == "total" else base + next(sfx for sfx, g, _ in GROUPS if g == grp)
                rid = by_code[code]
                if rid not in ids:
                    ids.append(rid)
                    must[rid] = OrderedDict([("value", round(ser[code]["value"], 1))])
                cells.append(OrderedDict([("ref", f"fx.{rid}.value"), ("dp", 1)]))
            rows.append(OrderedDict([("head", ui_row), ("cells", cells)]))
        rows += [OrderedDict([("marker", m)]) for m in markers]
        table = OrderedDict([
            ("form", "One row per group (all adults first), one column per measure; values as the World Bank publishes "
                     "them, to one decimal; governed notes close the table. No gap column, no interval, no ranking."),
            ("objects", [OrderedDict([("id", "fx"),
                                      ("rows", OrderedDict([("file", "data/findex_baseline.json"), ("header_key", "observation_id"),
                                                            ("ids", ids)])),
                                      ("fields", OrderedDict([("value", "value"), ("group", "group"), ("source", "source_url")])),
                                      ("must_equal", must)])]),
            ("head", ["UI-VIS-TH-FINDEX-ADULTS"] + [ui for _, ui in cols]),
            ("caption", caption),
            ("rows", rows)])
        c["visuals"].append(OrderedDict([("visual_id", vid), ("tier", "TABLE_TEXT_FIRST"), ("rationale", RATIONALE[vid]),
                                         ("promotion_requires", PROMOTION), ("table", table)]))
    with open(os.path.join(work, "visual_design_contract.json"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(c, ensure_ascii=False, indent=2) + "\n")

    counts = refresh_self_counts(s, F + ":OWN-10")
    rep = s.save(out, ledger, OrderedDict([
        ("transaction", F),
        ("summary", f"U1: {len(new_rows)} World Bank published Findex values added (open API source 28, snapshot of 10 "
                    "October 2026); 51 subgroup contract rows published, 105 kept with their reason (2 not asked, 5 "
                    "all-adults only, 14 no published value; checked by label); three table-first visuals; CR-03: "
                    "CLM-026 lists its 16 published measures; nine records and two page sections that said 'not yet "
                    "produced' corrected"),
        ("new_rows", len(new_rows)), ("self_counts", counts)]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
