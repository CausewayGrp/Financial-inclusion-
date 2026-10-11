# -*- coding: utf-8 -*-
"""Close-out transaction CLOSE-6A (Stage A addendum, advisor review of 11 October 2026): source closure of the
Measurement Agenda and of composite records, the Findex fieldwork date and precision, and three bounded statements.
English and Arabic change together.

  python3 close_6a.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Every write checks the exact current value. Reads behind this transaction (retrieved 11 October 2026) are kept in
audit/close_out/addendum/: R1 (Findex methodology, Brief 40), R2 (Sana'a Center papers), R4 (CCY, AMB, KfW), R6 (MICS,
phone survey); the World Development Indicators values are a dated snapshot in audit/close_out/fixtures/.

- Item 1a (Measurement Agenda). 10_MEASUREMENT_AGENDA gains evidence_bindings and source_bindings (master_structure.json
  is installed with the two labels). Each priority binds the records behind its current evidence; MA-008 binds none,
  because its text says this resource holds no measure. Three Evidence Records hold the figures no record held:
  FAS-YEM-2015 (World Development Indicators, IMF Financial Access Survey, 2015), MICS-YEM-2022-23 (the survey design and
  its one bank-account item) and YMPS-YEM-2022-R1 (the World Bank's phone survey, August–September 2022). MA-005's
  branch value is printed to the decimals the World Bank publishes for that series (1.5, from 1.4756; the rule CLOSE-3D
  used), not to two (1.48).
- Item 1b (composites). VIS-DEMAND-VINTAGE-LADDER lists CLM-026 and VIS-MFI-DIVERGENCE lists MFI-SPINE-2015-Q4, the
  records that hold their figures. Of the nine records whose members were not listed: VIS-PROVIDER-OBSERVABILITY,
  DS-DEMAND-VINTAGE-LENS and CLM-014 list their members; VIS-ACCESS-EVIDENCE-LAYER names its members in 11 data_inputs;
  VIS-INCLUSION-TRANSMISSION, VIS-SOURCE-COMPARISON, VIS-MECHANISM-METRIC-BRIDGE, VIS-EVIDENCE-CLASS-LADDER and
  VIS-EVIDENCE-GAPS state no figure from a source and become FRAMING_NO_FACT with the governed framing text.
- CR-21. Public clocks and prose give the Yemen Global Findex 2021 fieldwork as "November 2022 to January 2023". CLM-023
  keeps both World Bank dates with their locators and says in one clause that they differ by a day (catalogue 5862:
  9 January 2023; methodology Table A.1: 10 January 2023). Date states move with the text.
- CR-22. /methodology/ s7: the design effect reflects the weights only, not intraclass correlation (Table A.1, note b);
  the ~23% excluded population is a separate coverage limit; no adjusted interval.
- CLM-039. Brief 40 is not "corroboration that Yemen was excluded": the note to its Figure A.4.2 says Yemen is excluded,
  while panel (a) of the same figure plots a Yemen value for 2023 (R1, checked on the rendered page). It is recorded as a
  further sign that World Bank products differ on Yemen; no value is taken from it.
- CCY-PRESSURE. CWR-010 s6 gains a third later finding: banks and exchangers in areas administered by the internationally
  recognized government limited rial withdrawals and currency exchange from late February to mid-May 2026 (reported
  practice, interviews and a small trader survey; not prevalence, not a cause). Its "12%" is not reused (no traceable
  source; R4).
- E-money history. VIS-E-MONEY-RULE-STACK gains one attributed statement from the Sana'a Center paper (March 2022):
  bank-led under Circular No. 11 of 2014; CBY in Sana'a opening e-money licensing to non-banks from March 2020 (licence
  is not operation); CBY-Aden, as of the paper's writing, keeping the pre-conflict bank-led framework. The advisor's
  "until its own 2023 instructions" is right for e-money (the instructions of 9 August 2023 regulate non-bank e-money)
  and is completed, not replaced: CBY-Aden's instructions of 14 September 2022 had already defined payment service
  providers as non-bank institutions (R2). No number is taken from the paper (it contradicts itself; R2). CLM-012 says
  its rules are CBY-Aden's, with no territorial attribute for either central bank.
- Review pair (audit/close_out/addendum/REDTEAM_6A.md, ARABIC_6A.md): every blocker and must-fix is applied, and every
  should-fix but the optional ones the files mark as such; MA-003 states the age gap its bound record holds, MA-007 and
  MA-008 bind the CBY-Aden e-KYC instructions and credit-information sources their texts describe, and VIS-INCLUSION-
  TRANSMISSION reads as a frame. Not applied: red-team S22 (a composite lists records only, and the microfinance
  sentence prints no number; SRC-YMN-MEMBERS-2026-001 stays bound through DS-PROVIDER-UNIVERSE). A post-condition fails the transaction if any printed cell keeps 9 January 2023.
"""
import json, os, re, sys, unicodedata
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from close_lib import Session, Table, TxError, refresh_self_counts, COL03, S03  # noqa: E402

F = "CLOSE-6A"
TODAY = "2026-10-11"


def nfc(o):
    if isinstance(o, str):
        return unicodedata.normalize("NFC", o)
    if isinstance(o, (list, tuple)):
        return type(o)(nfc(x) for x in o)
    if isinstance(o, dict):
        return OrderedDict((k, nfc(v)) for k, v in o.items())
    return o


def vs(t, k, s, src=None, loc=None):
    d = OrderedDict([("t", t), ("k", k), ("s", s)])
    if src:
        d["src"] = src
    if loc:
        d["loc"] = loc
    return d


# ================================================================================================ item 1a: priorities
MA_BIND = OrderedDict([
    ("MA-001", (["CLM-001", "CLM-025", "CLM-026", "VIS-FINDEX-FLOW-CHANNELS", "MICS-YEM-2022-23", "YMPS-YEM-2022-R1"], ["SRC-WB-FINDEX-2025-EDITION"])),
    ("MA-002", (["CLM-004", "CLM-010", "CLM-050", "CLM-051", "VIS-PAYMENT-ANATOMY"], [])),
    ("MA-003", (["CLM-002", "VIS-FINDEX-GAPS"], [])),
    ("MA-004", (["CLM-062", "VIS-FIRM-CONSTRAINTS", "CLM-059", "CLM-060"], [])),
    ("MA-005", (["FAS-YEM-2015", "CLM-008", "CLM-009", "CLM-055", "CLM-019"], [])),
    ("MA-006", (["DS-FCP-ARCH", "CLM-011", "VIS-FCP-REDRESS-PATH"], [])),
    ("MA-007", (["CLM-012", "VIS-E-MONEY-RULE-STACK"], ["SRC-CBY-EKYC-2023"])),
    ("MA-008", ([], ["SRC-CBY-CRI-149", "SRC-CBY-CRI-150", "SRC-CBY-NEWS-963"])),
    ("MA-009", (["CLM-045", "YMPS-YEM-2022-R1"], [])),
    ("MA-010", (["CLM-018", "FMIIP-BASELINE-2025-01", "VIS-TARGET-RESULT-STATE", "VIS-PAYMENT-RAILS"], [])),
])
MA005_BRANCH = (("5.81 ATMs and 1.48 commercial bank branches", "5.81 ATMs and 1.5 commercial bank branches"),
                ("5.81 جهاز صراف آلي و1.48 فرع", "5.81 جهاز صراف آلي و1.5 فرع"))
MA005_TERM_AR = ("وقواعد الاحتساب السكانية فيها هي التي يعتمدها الصندوق", "وأعداد السكان المعتمدة مقامًا فيها هي أعداد الصندوق")
MA005_END = (("the values are dated historical context, not a current measure of access.",
              "the values are dated historical context, not a current measure of access to, or use of, financial services."),
             ("فهذه القيم سياق تاريخي مؤرخ، لا مقياس حالي للوصول.",
              "فهذه القيم سياق تاريخي مؤرخ، لا مقياس حالي للوصول إلى الخدمات المالية أو استخدامها."))
# S1: MA-003 states the age gap its bound record holds; S4: MA-007 names the e-KYC instructions it now binds;
# S5: MA-008 names the credit-information sources it now binds
MA_TEXT = OrderedDict([
    ("MA-003", OrderedDict([
        ("current_evidence_en", (
            "and by 9.0 percentage points between adults in the poorest 40% (6.5%) and the richest 60% (15.5%) by household income. "
            "Comparable current differences by age group and displacement status are not established in the evidence base,",
            "by 9.0 percentage points between adults in the poorest 40% (6.5%) and the richest 60% (15.5%) by household income, and "
            "by 11.1 percentage points between adults aged 15–24 (5.0%) and those aged 25 and over (16.1%). Comparable current "
            "differences by finer age groups and by displacement status are not established in the evidence base,")),
        ("current_evidence_ar", (
            "وبين البالغين في أفقر 40% (6.5%) وأغنى 60% (15.5%) بحسب دخل الأسرة بمقدار 9.0 نقطة مئوية. أما الفروق الراهنة القابلة "
            "للمقارنة بحسب الفئة العمرية وحالة النزوح",
            "وبين البالغين في أفقر 40% (6.5%) وأغنى 60% (15.5%) بحسب دخل الأسرة بمقدار 9.0 نقطة مئوية، وبين البالغين بعمر 15–24 "
            "سنة (5.0%) والبالغين بعمر 25 سنة فأكثر (16.1%) بمقدار 11.1 نقطة مئوية. أما الفروق الراهنة القابلة للمقارنة بحسب فئات "
            "عمرية أدق وبحسب حالة النزوح")),
        ("priority_basis_en", (
            "because material disparities by sex and by household income are measured within one survey wave, while current age- "
            "and displacement-disaggregated evidence and causal explanations remain incomplete;",
            "because material disparities by sex, household income and age are measured within one survey wave, while current "
            "evidence for finer age groups and by displacement status, and causal explanations, remain incomplete;")),
        ("priority_basis_ar", (
            "لأن تفاوتات مهمة بحسب الجنس ودخل الأسرة مقاسة بالفعل داخل موجة مسح واحدة، بينما تظل الأدلة الراهنة المفصلة بحسب العمر "
            "وحالة النزوح والتفسيرات السببية غير مكتملة؛",
            "لأن تفاوتات مهمة بحسب الجنس ودخل الأسرة والعمر مقاسة بالفعل داخل موجة مسح واحدة، بينما تظل الأدلة الراهنة المفصلة بحسب "
            "فئات عمرية أدق وبحسب حالة النزوح، والتفسيرات السببية، غير مكتملة؛")),
    ])),
    ("MA-007", OrderedDict([
        ("current_evidence_en", (
            "KYC and e-money rules are documented, but",
            "CBY-Aden's e-money rules and its electronic know-your-customer (KYC) instructions, which ask providers to report the "
            "average time to open or activate an account, are documented, but")),
        ("current_evidence_ar", (
            "قواعد «اعرف عميلك» (KYC) وقواعد النقود الإلكترونية موثقة، لكن",
            "قواعد النقود الإلكترونية الصادرة عن البنك المركزي اليمني – عدن وتعليماته بشأن إجراءات «اعرف عميلك» (KYC) إلكترونيًا، "
            "التي تطلب من مقدمي الخدمة الإبلاغ عن متوسط الوقت اللازم لفتح الحساب أو تفعيله، موثقة، لكن")),
    ])),
    ("MA-008", OrderedDict([
        ("current_evidence_en", (
            "Legal texts, project documents and institutional records can establish that credit infrastructure exists or is being "
            "developed;",
            "CBY-Aden's published credit-information rules (exposure reporting on a set form and an enquiry before lending) and its "
            "launch of a defaulters registry show that credit-information infrastructure exists;")),
        ("current_evidence_ar", (
            "قد تثبت النصوص القانونية ووثائق المشروعات والسجلات المؤسسية وجود بنية تحتية ائتمانية أو أنها قيد التطوير، لكن",
            "تُظهر قواعد معلومات الائتمان التي ينشرها البنك المركزي اليمني – عدن (الإبلاغ عن التعرضات الائتمانية على استمارة "
            "محددة والاستعلام قبل منح الائتمان) وتدشينه نظام سجل المتعثرين وجود بنية تحتية لمعلومات الائتمان، لكن")),
    ])),
])

BOUND_EN = ("This record is drawn from the source(s) listed on this page. Open a source record to reach the original document, "
            "and check that the definition, period, population and geography match what is stated here.")
BOUND_AR = ("يستند هذا السجل إلى المصدر أو المصادر المدرجة في هذه الصفحة. افتح سجل المصدر للوصول إلى الوثيقة الأصلية، وتحقق من "
            "تطابق التعريف والفترة والمجتمع والنطاق الجغرافي مع ما يرد هنا.")
TRIGGER_EN = ("This record is updated when an authoritative source is revised or replaced, a newer comparable observation becomes "
              "available, the definition, population or method changes, or the conditions for public use change.")
TRIGGER_AR = ("يُحدَّث هذا السجل عند مراجعة المصدر المعتمد أو استبداله، أو توفر مشاهدة أحدث قابلة للمقارنة، أو تغير التعريف أو المجتمع "
              "أو الطريقة، أو تغير شروط الاستخدام العام.")

FAS_SRC, MICS_SRC, YMPS_SRC = "SRC-WB-WDI-FAS-YEM-001", "SRC-UNICEF-MICS-YEM-2022-001", "SRC-WB-YMPS-R1-2022-001"
FAS_LOC = ("World Bank open data API, World Development Indicators, country YEM, series {s}, as fetched 11 October 2026 "
           "(last updated 8 October 2026); audit/close_out/fixtures/wdi_fas_yem_2026-10-11.json")
MICS_URL = "https://www.unicef.org/yemen/media/9006/file/YEMEN%20MICS%20MULTIPLE%20INDICATOR%20CLUSTER%20SURVEY.pdf"
YMPS_URL = "https://microdata.worldbank.org/index.php/catalog/5999"

NEW_RECORDS = [
    OrderedDict([
        ("object_id", "FAS-YEM-2015"), ("object_class", "TEMPORAL_OBSERVATION"), ("public_routes", "/measurement/ | /access/"),
        ("title_en", "ATMs, bank branches and depositors: Yemen's last values from the IMF Financial Access Survey in the World Development Indicators (2015)"),
        ("title_ar", "أجهزة الصراف الآلي وفروع البنوك والمودعون: آخر قيم اليمن من مسح الوصول المالي لصندوق النقد الدولي في مؤشرات التنمية العالمية (2015)"),
        ("summary_en", "The IMF Financial Access Survey, as published in the World Bank's World Development Indicators, last reports "
                       "Yemen for 2015: 5.81 automated teller machines (ATMs) and 1.5 commercial bank branches per 100,000 adults, "
                       "and 103.1 depositors with commercial banks per 1,000 adults. The series stop in 2015; these are dated "
                       "historical values, not a current measure of access to, or use of, financial services."),
        ("summary_ar", "يعود آخر ما يورده مسح الوصول المالي لصندوق النقد الدولي عن اليمن، كما تعرضه مؤشرات التنمية العالمية للبنك "
                       "الدولي، إلى عام 2015: 5.81 جهاز صراف آلي و1.5 فرع للبنوك التجارية لكل 100,000 بالغ، و103.1 مودِع لدى "
                       "البنوك التجارية لكل 1,000 بالغ. وتتوقف السلاسل عند عام 2015، فهذه قيم تاريخية مؤرخة، لا مقياس حالي للوصول إلى "
                       "الخدمات المالية أو استخدامها."),
        ("definition_en", "Three IMF Financial Access Survey indicators for Yemen as published in the World Development Indicators: "
                          "automated teller machines per 100,000 adults (FB.ATM.TOTL.P5), commercial bank branches per 100,000 "
                          "adults (FB.CBK.BRCH.P5) and depositors with commercial banks per 1,000 adults (FB.CBK.DPTR.P3), for "
                          "the last year reported."),
        ("definition_ar", "ثلاثة مؤشرات لليمن من مسح الوصول المالي لصندوق النقد الدولي، كما تعرضها مؤشرات التنمية العالمية: أجهزة "
                          "الصراف الآلي لكل 100,000 بالغ (FB.ATM.TOTL.P5)، وفروع البنوك التجارية لكل 100,000 بالغ "
                          "(FB.CBK.BRCH.P5)، والمودعون لدى البنوك التجارية لكل 1,000 بالغ (FB.CBK.DPTR.P3)، لآخر سنة تُورَد عنها قيم."),
        ("period_en", "2015, the last year reported for Yemen"), ("period_ar", "2015، آخر سنة تُورَد عنها قيم لليمن"),
        ("universe_en", "Adults in Yemen, with the population denominators the IMF uses for the Financial Access Survey; branches "
                        "and depositors of commercial banks only."),
        ("universe_ar", "البالغون في اليمن، وفق أعداد السكان التي يعتمدها صندوق النقد الدولي مقامًا في مسح الوصول المالي؛ وتقتصر "
                        "الفروع والمودعون على البنوك التجارية."),
        ("method_en", "Values from the World Bank's open data API (World Development Indicators; series last updated 8 October "
                      "2026), as fetched on 11 October 2026 and kept as a dated snapshot. Each value is rounded half up to the "
                      "decimals the World Bank publishes for its series: two for ATMs, one for branches and depositors."),
        ("method_ar", "قيم مأخوذة من واجهة البيانات المفتوحة للبنك الدولي (مؤشرات التنمية العالمية؛ آخر تحديث للسلاسل في 8 أكتوبر "
                      "2026)، كما قُرئت في 11 أكتوبر 2026 وحُفظت نسخةً مؤرخة. وتُقرَّب كل قيمة، بتقريب النصف إلى الأعلى، إلى عدد "
                      "المنازل العشرية الذي ينشره البنك الدولي لسلسلتها: منزلتان لأجهزة الصراف الآلي، ومنزلة واحدة للفروع والمودعين."),
        ("limitations_en", "The values describe 2015, not access today, and count machines, branches and depositors, not the people "
                           "who use them or where those points are. | The series stop in 2015 and their population denominators "
                           "are the IMF's; a count of depositors is not a count of unique people with an account."),
        ("limitations_ar", "تصف القيم عام 2015، لا الوصول اليوم، وتعدّ الأجهزة والفروع والمودعين، لا الأشخاص الذين يستخدمونها ولا "
                           "أماكن هذه النقاط. | تتوقف السلاسل عند عام 2015، وأعداد السكان المعتمدة مقامًا فيها هي أعداد صندوق النقد "
                           "الدولي؛ وعدد المودعين ليس عدد الأشخاص الفريدين الذين يملكون حسابًا."),
        ("currentness_en", "The latest observation in this record refers to 2015, the last year these series report for Yemen "
                           "(checked on 11 October 2026). It should not be read as describing a later period unless a newer "
                           "observation is published."),
        ("currentness_ar", "تعود أحدث مشاهدة في هذا السجل إلى عام 2015، وهو آخر عام تورده هذه السلاسل لليمن (جرى التحقق في 11 "
                           "أكتوبر 2026)، ولا تُقرأ على أنها تصف فترة لاحقة ما لم تُنشر مشاهدة أحدث."),
        ("change_trigger_en", TRIGGER_EN), ("change_trigger_ar", TRIGGER_AR),
        ("verification_en", BOUND_EN), ("verification_ar", BOUND_AR),
        ("source_dependencies", FAS_SRC),
        ("source_links", json.dumps([{"source_id": FAS_SRC, "url": "https://data.worldbank.org/indicator/FB.ATM.TOTL.P5?locations=YE",
                                      "audit_state": "PASS_AUTHORITY_OR_PROVIDER_LOCATOR"}], separators=(",", ":"))),
        ("lineage_state", "BOUND_EXACT"),
        ("value_states", [vs("5.81", "v", "DERIVED", FAS_SRC, FAS_LOC.format(s="FB.ATM.TOTL.P5") + "; 2015 = 5.80977836621394, decimal 2"),
                          vs("1.5", "v", "DERIVED", FAS_SRC, FAS_LOC.format(s="FB.CBK.BRCH.P5") + "; 2015 = 1.47559111890891, decimal 1"),
                          vs("103.1", "v", "DERIVED", FAS_SRC, FAS_LOC.format(s="FB.CBK.DPTR.P3") + "; 2015 = 103.054647215096, decimal 1"),
                          vs("100,000", "v", "TRIVIAL"), vs("1,000", "v", "TRIVIAL"),
                          vs("8 October 2026", "d", "READ", FAS_SRC, "World Bank open data API, lastupdated field of each series"),
                          vs("11 October 2026", "d", "SITE", None, "retrieval date of the snapshot")]),
        ("meta_en", "Yemen's last IMF Financial Access Survey values (2015), as the World Development Indicators publish them: ATMs and bank branches per 100,000 adults, depositors per 1,000."),
        ("meta_ar", "آخر قيم اليمن (2015) في مسح الوصول المالي لصندوق النقد الدولي كما تنشرها مؤشرات التنمية العالمية: أجهزة الصراف الآلي وفروع البنوك لكل 100,000 بالغ، والمودعون لكل 1,000."),
    ]),
    OrderedDict([
        ("object_id", "MICS-YEM-2022-23"), ("object_class", "TEMPORAL_OBSERVATION"), ("public_routes", "/measurement/ | /people/"),
        ("title_en", "MICS 2022–2023: one household question on bank accounts, not tabulated in its findings report"),
        ("title_ar", "المسح العنقودي متعدد المؤشرات 2022–2023: سؤال واحد في استبيان الأسرة عن الحسابات المصرفية، لم تُجدوَل إجاباته في تقرير نتائجه"),
        ("summary_en", "The Multiple Indicator Cluster Survey (MICS) 2022–2023, carried out by the Central Statistical Organization "
                       "with technical and financial support from UNICEF, was designed to give estimates for the 22 governorates of "
                       "Yemen; 41 of the 880 selected enumeration areas could not be visited for security and safety reasons. Its "
                       "household questionnaire asks one question on financial accounts, "
                       "whether any member of the household has a bank account (item HC19), and its survey findings report does not "
                       "tabulate the answers."),
        ("summary_ar", "صُمّم المسح العنقودي متعدد المؤشرات (MICS) 2022–2023، الذي نفّذه الجهاز المركزي للإحصاء بدعم فني ومالي من "
                       "اليونيسف، ليقدّم تقديرات للمحافظات الـ22 في اليمن؛ وتعذرت زيارة 41 من مناطق العدّ المختارة، البالغ عددها 880 "
                       "منطقة، لأسباب تتعلق بالأمن والسلامة. ويطرح استبيان الأسرة فيه سؤالًا واحدًا عن الحسابات المالية، هو ما إذا كان أي فرد في الأسرة يملك "
                       "حسابًا مصرفيًا (البند HC19)، ولا يعرض تقرير نتائج المسح جدولًا لإجاباته."),
        ("definition_en", "What the MICS 2022–2023 for Yemen was designed to cover, and the one item on financial accounts in its "
                          "household questionnaire."),
        ("definition_ar", "ما صُمّم المسح العنقودي متعدد المؤشرات 2022–2023 في اليمن ليغطيه، والبند الوحيد عن الحسابات المالية في "
                          "استبيان الأسرة."),
        ("period_en", "Fieldwork July–September 2022 (Aden hub) and January–May 2023 (Sana'a hub)"),
        ("period_ar", "العمل الميداني: يوليو–سبتمبر 2022 (مركز عدن)، ويناير–مايو 2023 (مركز صنعاء)"),
        ("universe_en", "Households in the governorates covered by the survey design, apart from the enumeration areas that could "
                        "not be visited."),
        ("universe_ar", "الأسر في المحافظات التي يشملها تصميم المسح، باستثناء مناطق العدّ التي تعذرت زيارتها."),
        ("method_en", "Taken from the Survey Findings Report: the sample design (section 5.12, printed p. 3), the fieldwork periods "
                      "(section 5.17, printed p. 5) and the household questionnaire (Appendix E, item HC19, printed p. 330). A text "
                      "search of the report finds the item only in the questionnaire."),
        ("method_ar", "مأخوذ من تقرير نتائج المسح (أرقام الصفحات بحسب ترقيم التقرير المطبوع): تصميم العينة (القسم 5.12، ص 3)، "
                      "وفترات العمل الميداني (القسم 5.17، ص 5)، واستبيان الأسرة (الملحق E، البند HC19، ص 330). ولا يَرِد البند في "
                      "التقرير، بحسب بحث في نصه، إلا في الاستبيان."),
        ("limitations_en", "The survey does not measure individual account ownership, account use, mobile money, saving or borrowing, "
                           "and its findings report gives no result for the bank-account item. | Even if tabulated, the item would "
                           "show whether any member of a household has a bank account, not which members do. The two parts of the "
                           "sample were fielded in different periods, July–September 2022 from the Aden hub and January–May 2023 from "
                           "the Sana'a hub, and some governorates were collected partly by each hub, so a tabulation of the item would "
                           "mix periods across areas."),
        ("limitations_ar", "لا يقيس المسح امتلاك الأفراد للحسابات ولا استخدامها ولا الأموال عبر الهاتف المحمول ولا الادخار ولا الاقتراض، "
                           "ولا يعرض تقرير نتائجه أي نتيجة لبند الحساب المصرفي. | حتى لو جُدوِل البند، لأظهر ما إذا كان أي فرد في "
                           "الأسرة يملك حسابًا مصرفيًا، لا أيّ أفرادها يملكونه. وجُمعت بيانات جزأي العينة في فترتين مختلفتين، "
                           "يوليو–سبتمبر 2022 من مركز عدن ويناير–مايو 2023 من مركز صنعاء، وجُمعت بيانات بعض المحافظات جزئيًا من كل "
                           "مركز، فأي جدولة للبند ستخلط فترات مختلفة بين المناطق."),
        ("currentness_en", "Fieldwork ended in May 2023; the Survey Findings Report is the MICS publication this record uses "
                           "(checked on 11 October 2026)."),
        ("currentness_ar", "انتهى العمل الميداني في مايو 2023؛ وتقرير نتائج المسح هو إصدار المسح الذي يستند إليه هذا السجل (جرى "
                           "التحقق في 11 أكتوبر 2026)."),
        ("change_trigger_en", TRIGGER_EN), ("change_trigger_ar", TRIGGER_AR),
        ("verification_en", BOUND_EN), ("verification_ar", BOUND_AR),
        ("source_dependencies", MICS_SRC),
        ("source_links", json.dumps([{"source_id": MICS_SRC, "url": "https://www.unicef.org/yemen/documents/yemen-mics-multiple-indicator-cluster-survey",
                                      "audit_state": "PASS_AUTHORITY_OR_PROVIDER_LOCATOR"}], separators=(",", ":"))),
        ("lineage_state", "BOUND_EXACT"),
        ("value_states", [vs("22", "v", "READ", MICS_SRC, "Survey Findings Report, section 5.12, printed p.3 (PDF p.17), '...for the 22 governorates in Yemen'; " + MICS_URL),
                          vs("41", "v", "READ", MICS_SRC, "Survey Findings Report, section 5.12, printed p.3 (PDF p.17), 'forty-one (41) of the selected enumeration areas could not be visited'"),
                          vs("880", "v", "READ", MICS_SRC, "Survey Findings Report, section 5.12, printed p.3 (PDF p.17), 'The total target sample size for the Yemen MICS was 880 clusters and 22,000 households'"),
                          vs("July", "d", "READ", MICS_SRC, "Survey Findings Report, section 5.17, printed p.5 (PDF p.19): July-September 2022, Aden hub; January-May 2023, Sana'a hub; footnote 6, governorates 'collected partly from Aden and Sana'a hubs'"),
                          vs("5.12", "v", "TRIVIAL"), vs("5.17", "v", "TRIVIAL"), vs("3", "v", "TRIVIAL"), vs("5", "v", "TRIVIAL"), vs("330", "v", "TRIVIAL"),
                          vs("September 2022", "d", "READ", MICS_SRC, "Survey Findings Report, section 5.17, printed p.5 (PDF p.19): July-September 2022, Aden hub"),
                          vs("May 2023", "d", "READ", MICS_SRC, "Survey Findings Report, section 5.17, printed p.5 (PDF p.19)"),
                          vs("11 October 2026", "d", "SITE", None, "date the report was checked")]),
        ("meta_en", "MICS 2022–2023 in Yemen: designed for 22 governorates; one household bank-account question that its findings report does not tabulate."),
        ("meta_ar", "المسح العنقودي متعدد المؤشرات 2022–2023 في اليمن: صُمّم لـ22 محافظة، وفي استبيان الأسرة سؤال واحد عن الحساب المصرفي لا يجدوِل تقرير النتائج إجاباته."),
    ]),
    OrderedDict([
        ("object_id", "YMPS-YEM-2022-R1"), ("object_class", "TEMPORAL_OBSERVATION"), ("public_routes", "/measurement/ | /people/"),
        ("title_en", "The World Bank's phone survey of August–September 2022 records respondents in both areas of control"),
        ("title_ar", "مسح الهاتف المحمول للبنك الدولي في أغسطس–سبتمبر 2022 يسجل مستجيبين في منطقتَي السيطرة كلتيهما"),
        ("summary_en", "The World Bank's Mobile Phone Survey Monitoring, Round I, interviewed 1,297 adult Yemenis aged 18 and over "
                       "with mobile phones in August–September 2022, from a probability sample targeted across 21 governorates. It "
                       "records each respondent's area of control, coded in the catalogue as the internationally recognized "
                       "government or 'DFA', which this resource reads as the de facto authorities (the catalogue does not expand the "
                       "abbreviation), and asks respondents to rank the three most important sources of income."),
        ("summary_ar", "أجرت الجولة الأولى من مسح الهاتف المحمول للرصد التابع للبنك الدولي، في أغسطس–سبتمبر 2022، مقابلات مع "
                       "1,297 بالغًا يمنيًا بعمر 18 سنة فأكثر ممن يملكون هواتف محمولة، من عينة احتمالية استهدفت 21 محافظة. ويسجل "
                       "المسح منطقة السيطرة لكل مستجيب، مرمَّزةً في الفهرس بوصفها الحكومة المعترف بها دوليًا أو «DFA»، وهو اختصار "
                       "يقرؤه هذا المورد على أنه سلطات الأمر الواقع (إذ لا يفسّره الفهرس)، ويطلب من المستجيبين ترتيب أهم ثلاثة "
                       "مصادر للدخل."),
        ("definition_en", "The sample, period and two items of the World Bank's Yemen Mobile Phone Survey Monitoring, Round I (2022), "
                          "as documented in its Microdata Library catalogue entry: the respondent's area of control and the ranking of "
                          "income sources."),
        ("definition_ar", "العينة والفترة وبندان من الجولة الأولى (2022) لمسح الهاتف المحمول للرصد في اليمن التابع للبنك الدولي، "
                          "كما توثقها صفحة المسح في فهرس مكتبة البيانات الجزئية (Microdata Library): منطقة سيطرة المستجيب وترتيب "
                          "مصادر الدخل."),
        ("period_en", "August–September 2022 (Round I)"), ("period_ar", "أغسطس–سبتمبر 2022 (الجولة الأولى)"),
        ("universe_en", "Adult Yemenis aged 18 and over with mobile phones, from a probability sample targeted across 21 governorates; "
                        "the catalogue reports a response rate of around 28 percent."),
        ("universe_ar", "اليمنيون البالغون بعمر 18 سنة فأكثر ممن يملكون هواتف محمولة، من عينة احتمالية استهدفت 21 محافظة؛ وأكمل "
                        "ويذكر الفهرس معدل استجابة يقارب 28 في المئة."),
        ("method_en", "Taken from the survey's catalogue metadata (Microdata Library, catalog 5999: abstract, sampling, response "
                      "rate and data dictionary). No data file was used."),
        ("method_ar", "مأخوذ من البيانات الوصفية للمسح في الفهرس (مكتبة البيانات الجزئية، الفهرس رقم 5999: الملخص والمعاينة ومعدل "
                      "الاستجابة وقاموس البيانات). ولم يُستخدم أي ملف بيانات."),
        ("limitations_en", "Adults with mobile phones are not all adults; with a response rate of around 28 percent, and some "
                           "governorate quotas not achieved, respondents may not represent all adults with mobile phones; the "
                           "catalogue's sampling text names 18 governorates while its abstract says 21. | Recording area of control and income sources does not measure financial inclusion; "
                           "the survey is shown as an existing instrument that a later round could extend."),
        ("limitations_ar", "البالغون الذين يملكون هواتف محمولة ليسوا كل البالغين؛ ومع معدل استجابة يقارب 28 في المئة وعدم بلوغ حصص "
                           "بعض المحافظات، قد لا يمثل المستجيبون جميع البالغين الذين يملكون هواتف محمولة؛ ويسمّي نص المعاينة في الفهرس 18 محافظة بينما يذكر الملخص 21. | تسجيل منطقة "
                           "السيطرة ومصادر الدخل لا يقيس الشمول المالي؛ ويُعرض المسح بوصفه أداة قائمة يمكن أن توسعها جولة لاحقة."),
        ("currentness_en", "Round I fieldwork took place in August–September 2022 (checked on 11 October 2026); whether later "
                           "rounds have been published was not checked."),
        ("currentness_ar", "نُفّذ العمل الميداني للجولة الأولى في أغسطس–سبتمبر 2022 (جرى التحقق في 11 أكتوبر 2026)؛ ولم يُتحقق "
                           "مما إذا كانت قد نُشرت جولات لاحقة."),
        ("change_trigger_en", TRIGGER_EN), ("change_trigger_ar", TRIGGER_AR),
        ("verification_en", BOUND_EN), ("verification_ar", BOUND_AR),
        ("source_dependencies", YMPS_SRC),
        ("source_links", json.dumps([{"source_id": YMPS_SRC, "url": YMPS_URL, "audit_state": "PASS_AUTHORITY_OR_PROVIDER_LOCATOR"}],
                                    separators=(",", ":"))),
        ("lineage_state", "BOUND_EXACT"),
        ("value_states", [vs("1,297", "v", "READ", YMPS_SRC, "Microdata Library catalog 5999, Abstract: 'a probability sample of 1,297 adult Yemenis (18 years of age and older) with mobile phones'; Response Rate: '1,297 respondents completed the interview'"),
                          vs("18", "v", "READ", YMPS_SRC, "catalog 5999, Abstract, '18 years of age and older'; and Sampling > Sampling Procedure, which lists 18 governorates by name for the quotas (counted)"),
                          vs("28", "v", "READ", YMPS_SRC, "catalog 5999, Sampling > Response Rate, 'a response rate of around 28 percent'; Deviations from the Sample Design, 'Some governorate quotas were not achieved'"),
                          vs("21", "v", "READ", YMPS_SRC, "catalog 5999, Abstract, 'targeted across 21 governorates'"),
                          vs("5999", "v", "TRIVIAL"),
                          vs("September 2022", "d", "READ", YMPS_SRC, "catalog 5999, Dates of Data Collection: 2022-08 to 2022-09 (Round 1)"),
                          vs("11 October 2026", "d", "SITE", None, "date the catalogue entry was checked")]),
        ("meta_en", "The World Bank's 2022 phone survey interviewed 1,297 adults with mobile phones and records each respondent's area of control."),
        ("meta_ar", "أجرى مسح الهاتف المحمول التابع للبنك الدولي عام 2022 مقابلات مع 1,297 بالغًا ممن يملكون هواتف محمولة، ويسجل منطقة السيطرة لكل مستجيب."),
    ]),
]

# ================================================================================================ item 1b: composites
COMPOSITE_MEMBERS = OrderedDict([
    ("VIS-DEMAND-VINTAGE-LADDER", ("CLM-001; CLM-027; CLM-028; CLM-029; CLM-030; VIS-FINDEX-RESILIENCE; VIS-FINDEX-BARRIERS; VIS-FINDEX-FLOW-CHANNELS",
                                   "CLM-001; CLM-026; CLM-027; CLM-028; CLM-029; CLM-030; VIS-FINDEX-RESILIENCE; VIS-FINDEX-BARRIERS; VIS-FINDEX-FLOW-CHANNELS")),
    ("VIS-PROVIDER-OBSERVABILITY", (None, "CLM-008; CLM-055; CLM-009; CLM-019; CLM-010; CLM-015")),
    ("DS-DEMAND-VINTAGE-LENS", (None, "CLM-001; CLM-026; CLM-027; CLM-028; CLM-029; CLM-030; VIS-FINDEX-RESILIENCE; VIS-FINDEX-BARRIERS; VIS-FINDEX-FLOW-CHANNELS")),
    ("CLM-014", (None, "CLM-001; CLM-025; CLM-029; CLM-031; CLM-028; CLM-013; VIS-FL-EVIDENCE-LADDER; VIS-FINDEX-RESILIENCE; CLM-002; "
                       "VIS-FINDEX-GAPS; XW-FMIIP-005; CLM-052; CLM-050; FMIIP-BASELINE-2025-01; CLM-003; CLM-017; CLM-012; CLM-045; "
                       "CLM-030; CLM-007; CLM-032; VIS-REMITTANCE-COST; CLM-008; CLM-009; CLM-019; CLM-015; CLM-053; CLM-054; CLM-033; "
                       "CLM-038; CLM-005; CLM-006; CLM-059; CLM-060; CLM-011; DS-FCP-ARCH; CLM-018")),
])
MFI_DIV = ("VIS-MFI-DIVERGENCE", "CLM-021 + CLM-053 + CLM-054 + CLM-057 + CLM-058",           # a visual contract (11 only)
           "MFI-SPINE-2015-Q4 + CLM-021 + CLM-053 + CLM-054 + CLM-057 + CLM-058")
FRAME_TEXT = OrderedDict([
    ("summary_en", ("The documented relationships describe context, dependency or plausible mechanisms where evidence supports them;",
                    "The relationships it names are of context, dependency or plausible mechanism, each to be checked in the evidence "
                    "records of the parts it joins;")),
    ("summary_ar", ("وتصف العلاقات الموثقة السياق أو الاعتماد أو آليات محتملة حين تسندها الأدلة؛",
                    "والعلاقات التي يسمّيها علاقات سياق أو اعتماد أو آلية محتملة، يُتحقق من كل منها في سجلات الأدلة الخاصة بالأجزاء "
                    "التي تربط بينها؛")),
    ("method_en", ("Compiled from the relationships between system parts documented in this resource's evidence base. Each "
                   "relationship is described by its type,",
                   "A reading frame that names the parts of the system and the kinds of relationship to look for; each relationship "
                   "must be checked in the evidence records of the parts it joins. Each relationship is described by its type,")),
    ("method_ar", ("يستند هذا السجل إلى العلاقات الموثقة بين أجزاء المنظومة في قاعدة أدلة هذا المورد. وتوصف كل علاقة بنوعها،",
                   "إطار للقراءة يسمّي أجزاء المنظومة وأنواع العلاقات التي يُبحث عنها؛ ويجب التحقق من كل علاقة في سجلات الأدلة الخاصة "
                   "بالأجزاء التي تربط بينها. وتوصف كل علاقة بنوعها،")),
])
FRAMING = ["VIS-INCLUSION-TRANSMISSION", "VIS-SOURCE-COMPARISON", "VIS-MECHANISM-METRIC-BRIDGE", "VIS-EVIDENCE-CLASS-LADDER", "VIS-EVIDENCE-GAPS"]
ACCESS_LAYER = ("VIS-ACCESS-EVIDENCE-LAYER",
                "Provider/status objects + payment-infrastructure totals + historical provider concentration; future national access-point register.",
                "CLM-008 listing and licensing + CLM-009 exchange and remittance roster + CLM-019 enforcement events + CLM-003 POS "
                "infrastructure totals + CLM-052 historical provider concentration + future national access-point register (not yet available)")

# ================================================================================================ CR-21: fieldwork dates
CR21_PHRASES = [
    ("7 November 2022 to 9 January 2023", "November 2022 to January 2023"),
    ("7 نوفمبر 2022 إلى 9 يناير 2023", "نوفمبر 2022 إلى يناير 2023"),
    ("fieldwork 2022-11-07 to 2023-01-09", "fieldwork November 2022 to January 2023"),
    ("من 2022-11-07 إلى 2023-01-09", "من نوفمبر 2022 إلى يناير 2023"),
    ("7 November 2022 – 9 January 2023", "November 2022 – January 2023"),
    ("7 نوفمبر 2022 – 9 يناير 2023", "نوفمبر 2022 – يناير 2023"),
]
# Not changed: provenance metadata that states the catalogue's dates as the World Bank DDI gives them and is not printed
# (16_DATASET_CATALOG period_min/period_max, 28_METHODS_RIGHTS fieldwork_start/fieldwork_end, 11 source_period and
# freshness_profile), and the 06 value-state locators.
CR21_SKIP_COLS = {"11_VISUAL_LIBRARY": ("source_period", "freshness_profile")}
CR21_KEEP = ("CLM-023",)                       # the method note keeps both World Bank dates (its own value states are written below)
CLM023_NOTE = (
    " The two World Bank records of the fieldwork dates differ by one day on the end date: the Microdata Library catalogue (study 5862, Data "
    "collection, Dates of Data Collection) gives 7 November 2022 to 9 January 2023, and the Global Findex 2021 methodology "
    "(Appendix A, Table A.1, p. 17) gives 7 November 2022 to 10 January 2023; elsewhere this resource gives the period as "
    "November 2022 to January 2023.",
    " ويختلف سجلّا البنك الدولي لتاريخَي العمل الميداني بيوم واحد في تاريخ الانتهاء: إذ يذكر فهرس مكتبة البيانات الجزئية (Microdata Library) "
    "للدراسة 5862، في قسم «جمع البيانات» وبند «تواريخ جمع البيانات»، الفترة من 7 نوفمبر 2022 إلى 9 يناير 2023، وتذكر منهجية "
    "Global Findex 2021 (الملحق A، الجدول A.1، ص 17) الفترة من 7 نوفمبر 2022 إلى 10 يناير 2023؛ أما في سائر هذا المورد فتُذكر الفترة من نوفمبر 2022 "
    "إلى يناير 2023.")
METHOD_PDF = "https://thedocs.worldbank.org/en/doc/fe026d04da1eb78f5ce8bb5e1529d60b-0430062023/original/Findex2021-22-Methodology.pdf"
CLM023_STATES = [vs("10 January 2023", "d", "READ", "SRC-WB-FINDEX-001",
                    "Global Findex 2021 methodology, Appendix A, Table A.1, Yemen row 'Nov 7, 2022–Jan 10, 2023', printed p.17 (PDF p.15), "
                    + METHOD_PDF + "; read 11 October 2026"),
                 vs("5862", "v", "TRIVIAL"), vs("17", "v", "TRIVIAL")]

# ================================================================================================ CR-22: /methodology/ s7
CR22 = (("the method and every interval are recorded with their figures.",
         "the method and every interval are recorded with their figures. The World Bank's design effect reflects the survey weights "
         "only and does not incorporate intraclass correlation coefficients, because they vary by question (Global Findex 2021 "
         "methodology, Table A.1, note b); these intervals therefore leave out the extra uncertainty that clustering usually adds "
         "and may be narrower than the true sampling uncertainty. The areas the survey excluded, home to approximately 23% of the "
         "population according to the World Bank, are a separate limit on coverage, and no adjusted interval is computed."),
        ("والطريقة وكل فترة مسجّلتان مع قيمتهما.",
         "والطريقة وكل فترة مسجّلتان مع قيمتهما. ويعكس أثر التصميم الذي ينشره البنك الدولي أوزانَ المسح وحدها، ولا يأخذ في الحسبان "
         "معاملات الارتباط داخل العناقيد لأنها تختلف من سؤال إلى آخر (منهجية Global Findex 2021، الجدول A.1، الحاشية b)؛ ولذلك لا "
         "تشمل فترات الثقة هذه عدم اليقين الإضافي الذي تضيفه العنقدة عادةً، وقد تكون أضيق من عدم اليقين الفعلي في المعاينة. أما "
         "المناطق التي استبعدها المسح، ويقطنها نحو 23% من السكان بحسب البنك الدولي، فهي قيد مستقل على التغطية، ولا تُحتسب أي فترة "
         "ثقة معدَّلة."))

# ================================================================================================ CLM-039: Brief 40
MDB40 = "SRC-WB-MDB40-2024"
MDB40_URL = "https://documents1.worldbank.org/curated/en/099714008132436612/pdf/IDU-a9cf73b5-fcad-425a-a0dd-cc8f2f3331ce.pdf"
CLM039 = (
    " One World Bank publication is also inconsistent on Yemen: the note to Figure A.4.2 of Migration and Development Brief 40 "
    "(June 2024) says Yemen is excluded “due to data availability”, yet panel (a), remittances in US dollars for 2023, shows a "
    "value for Yemen, and only panel (b), remittances as a share of GDP, omits it. The brief does not say which panel the note "
    "applies to, and this resource takes no value from the figure.",
    " ويقع منشور واحد للبنك الدولي أيضًا في عدم اتساق بشأن اليمن: إذ تذكر الملاحظة المرافقة للشكل A.4.2 في موجز الهجرة والتنمية "
    "رقم 40 (يونيو 2024) أن اليمن مستبعد «لأسباب تتعلق بتوفر البيانات»، غير أن اللوحة (a)، وهي التحويلات بالدولار الأمريكي لعام "
    "2023، تعرض قيمة لليمن، ولا تغفله إلا اللوحة (b)، وهي التحويلات نسبةً إلى الناتج المحلي الإجمالي. ولا يحدد الموجز اللوحة التي "
    "تنطبق عليها الملاحظة، ولا يأخذ هذا المورد أي قيمة من الشكل.")
CLM039_STATES = [vs("June 2024", "d", "READ", MDB40, "Migration and Development Brief 40, cover and title page; " + MDB40_URL),
                 vs("2023", "d", "READ", MDB40, "Brief 40, Figure A.4.2 'Top Remittance Recipients in the Middle East and North Africa, "
                    "2023', printed p.29 (PDF p.39): note '*...the Republic of Yemen are excluded due to data availability'; panel a "
                    "plots 'Yemen, Rep.'; panel b (percentage of GDP, 2023) has no Yemen bar (render-checked 11 October 2026)"),
                 vs("40", "v", "TRIVIAL"), vs("4.2", "v", "TRIVIAL")]

# ================================================================================================ CCY-PRESSURE: CWR-010 s6
CWR010_ROUTE = "/readings/after-transfer-persistence/"
CCY_P = "SRC-CCY-PRESSURE-2026"
CWR010 = (
    (("Two later findings mark where the evidence stops.", "Three later findings mark where the evidence stops."),
     ("given the scarcity of bank branches and ATMs.",
      "given the scarcity of bank branches and ATMs. The third, a separate May 2026 report by the Cash Consortium of Yemen based "
      "on desk research, a small survey of traders in Taiz and interviews with a few financial and humanitarian experts, concerns "
      "access to cash itself: it reports that in areas administered by the internationally recognized government, currency "
      "exchangers and banks limited currency exchange and the rials they handed out from February 2026, and rial withdrawals from "
      "late April; its summary gives the period as late February to mid-May, and it does not report the limits ending. That is "
      "reported practice in those areas and months, not a measure of how many people were affected, and the report attributes it "
      "to the regional conflict and to cash hoarding without testing that explanation.")),
    (("وتحدّد خلاصتان لاحقتان موضع توقف الدليل.", "وتحدّد ثلاث خلاصات لاحقة موضع توقف الدليل."),
     ("نظرًا إلى ندرة فروع البنوك وأجهزة الصراف الآلي.",
      "نظرًا إلى ندرة فروع البنوك وأجهزة الصراف الآلي. أما الخلاصة الثالثة فتخص الوصول إلى النقد نفسه، ومصدرها تقرير منفصل لتحالف "
      "النقد في اليمن صدر في مايو 2026 واستند إلى بحث مكتبي ومسح صغير لتجار في تعز ومقابلات مع عدد قليل من الخبراء في الشأن المالي "
      "والعمل الإنساني: إذ يفيد التقرير بأن شركات ومنشآت الصرافة والبنوك في المناطق الخاضعة لإدارة الحكومة المعترف بها دوليًا قيّدت "
      "تصريف العملات وما تسلّمه من ريالات اعتبارًا من فبراير 2026، والسحب بالريال اعتبارًا من أواخر أبريل؛ ويحدد ملخصه الفترة من "
      "أواخر فبراير إلى منتصف مايو، ولا يفيد بانتهاء هذه القيود. وهذه ممارسة مُبلَّغ عنها في تلك المناطق وتلك الأشهر، لا مقياس لعدد "
      "الأشخاص المتأثرين بها، ويعزوها التقرير إلى النزاع الإقليمي وإلى اكتناز النقد دون أن يختبر هذا التفسير.")))
CWR010_PERIOD = (("Cash Consortium of Yemen study (2026) and World Bank project documents (2025–2026)",
                  "Cash Consortium of Yemen study (2026) and report (May 2026) and World Bank project documents (2025–2026)"),
                 ("دراسة لتحالف النقد في اليمن (Cash Consortium of Yemen، 2026) ووثائق مشروعات البنك الدولي (2025–2026)",
                  "دراسة لتحالف النقد في اليمن (Cash Consortium of Yemen، 2026) وتقرير له (مايو 2026) ووثائق مشروعات البنك الدولي "
                  "(2025–2026)"))

# ================================================================================================ e-money history
SANAA = "SRC-SANAA-EMONEY-2022"
EMONEY = (
    " For the history behind these layers, a March 2022 paper by the Sana'a Center for Strategic Studies, a secondary analysis "
    "rather than a regulator's statement, describes mobile e-money as bank-led under the central bank's Circular No. 11 of 2014, "
    "and reports that after the central bank divided, the Central Bank of Yemen in Sana'a opened e-money licensing to non-bank "
    "institutions from March 2020 while CBY-Aden, as of the paper's writing, kept the pre-conflict, bank-led framework. CBY-Aden "
    "later issued its own instructions for payment service providers, which it defines as non-bank financial institutions "
    "licensed by the central bank (14 September 2022), and the e-money instructions of 9 August 2023 described above.",
    " وللاطلاع على الخلفية التاريخية لهذه الطبقات، تصف ورقة نشرها مركز صنعاء للدراسات الاستراتيجية في مارس 2022، وهي تحليل ثانوي "
    "لا بيان صادر عن جهة رقابية، خدماتِ النقود الإلكترونية عبر الهاتف المحمول بأنها كانت قائمة على البنوك بموجب المنشور رقم 11 لسنة "
    "2014 الصادر عن البنك المركزي اليمني، وتذكر أنه بعد انقسام البنك المركزي فتح البنك المركزي اليمني في صنعاء باب الترخيص لإصدار "
    "النقود الإلكترونية أمام مؤسسات غير مصرفية اعتبارًا من مارس 2020، في حين أبقى البنك المركزي اليمني – عدن، حتى تاريخ كتابة الورقة، "
    "على الإطار القائم على البنوك الذي سبق النزاع. ثم أصدر البنك المركزي اليمني – عدن نفسه تعليمات لمقدمي خدمات الدفع، الذين يعرّفهم "
    "بأنهم مؤسسات مالية غير مصرفية مرخص لها من البنك المركزي (14 سبتمبر 2022)، وتعليمات النقود الإلكترونية الصادرة في 9 أغسطس 2023 "
    "المذكورة أعلاه.")
EMONEY_STATES = [vs("March 2022", "d", "READ", SANAA, "Sana'a Center for Strategic Studies, 'Challenges and Prospects for Electronic Money "
                    "and Payment Systems in Yemen', cover ('March 2022'); https://sanaacenter.org/publications/policy-research/16974"),
                 vs("March 2020", "d", "READ", SANAA, "same paper, p.18: in 'March 2020' CBY-Sana'a issued a directive that 'paved the way "
                    "for non-bank institutions' and 'expanded the scope of ... eligible to obtain a license'"),
                 vs("14 September 2022", "d", "READ", "SRC-CBY-PSP-RULES-2022-001", "CBY-Aden instructions for payment service "
                    "providers and payment system operators (ref. 720/CBY/2022), 14 September 2022, definitions, pp.1-5"),
                 vs("11", "v", "READ", SANAA, "same paper, p.12: 'Circular No. 11 of 2014'"),
                 vs("2014", "d", "READ", SANAA, "same paper, p.12: 'Circular No. 11 of 2014'")]
CLM012 = (("or adoption. |", "or adoption, and these are CBY-Aden's rules, not those the Central Bank of Yemen in Sana'a has issued. |"),
          ("ولا التبني. |", "ولا التبني؛ وهذه قواعد البنك المركزي اليمني – عدن، لا القواعد التي أصدرها البنك المركزي اليمني في "
                           "صنعاء. |"))


def add_states(cur, extra):
    lst = json.loads(cur) if isinstance(cur, str) and cur.strip() else []
    have = {(x.get("t"), x.get("k")) for x in lst}
    for e in extra:
        if (e["t"], e["k"]) not in have:
            lst.append(e)
            have.add((e["t"], e["k"]))
    return json.dumps(lst, ensure_ascii=False, separators=(",", ":"))


def cr21_states(cur):
    """The date states of a record that now prints "November 2022 to January 2023": the two month states are added (from
    the day states they replace in the text); the day states stay as provenance."""
    if not isinstance(cur, str) or not cur.strip():
        return cur
    lst = json.loads(cur)
    have = {(x.get("t"), x.get("k")) for x in lst}
    out = list(lst)
    for day, month in (("7 November 2022", "November 2022"), ("9 January 2023", "January 2023")):
        src = next((x for x in lst if x.get("t") == day and x.get("k") == "d"), None)
        if src and (month, "d") not in have:
            e = OrderedDict(src)
            e["t"] = month
            out.append(e)
            have.add((month, "d"))
    return json.dumps(out, ensure_ascii=False, separators=(",", ":"))


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)

    # ---------------------------------------------------------------- 06: three new Evidence Records (item 1a)
    t06 = Table(s, "06_EVIDENCE_OBJECTS")
    h06 = t06.head
    last06 = max(t06.rows.values())
    rows = []
    for r in nfc(NEW_RECORDS):
        if r["object_id"] in t06.rows:
            raise TxError(f"{F}: 06 already holds {r['object_id']}")
        row = OrderedDict((k, v) for k, v in r.items() if k not in ("meta_en", "meta_ar"))
        row["value_states"] = json.dumps(row["value_states"], ensure_ascii=False, separators=(",", ":"))
        rows.append(row)
    s.ed.insert_rows("06_EVIDENCE_OBJECTS", last06 + 1, [{h06.index(k) + 1: v for k, v in row.items() if v is not None} for row in rows])
    for j, row in enumerate(rows):
        for k, v in row.items():
            if v is not None:
                s.ledger.append(OrderedDict([("finding", F + ":1a"), ("sheet", "06_EVIDENCE_OBJECTS"), ("row", last06 + 1 + j),
                                             ("col", h06.index(k) + 1), ("field", f"{row['object_id']}.{k}"), ("old", None), ("new", v)]))
    # 02: their routes (title blank: it derives from 06; sections derive from 06 and 04)
    t02 = Table(s, "02_SITE_MAP")
    h02 = t02.head
    after = max(i for k, i in t02.rows.items() if str(k).startswith("/evidence/") and str(k) != "/evidence/compare/")
    new02 = [OrderedDict([("route", f"/evidence/{r['object_id']}/"), ("page_class", "evidence_detail"), ("template_route", "/evidence/[id]"),
                          ("instance_id", r["object_id"]), ("meta_description_en", r["meta_en"]), ("meta_description_ar", r["meta_ar"])])
             for r in nfc(NEW_RECORDS)]
    s.ed.insert_rows("02_SITE_MAP", after + 1, [{h02.index(k) + 1: v for k, v in row.items()} for row in new02])
    for j, row in enumerate(new02):
        for k, v in row.items():
            s.ledger.append(OrderedDict([("finding", F + ":1a"), ("sheet", "02_SITE_MAP"), ("row", after + 1 + j),
                                         ("col", h02.index(k) + 1), ("field", f"{row['route']}.{k}"), ("old", None), ("new", v)]))

    # ---------------------------------------------------------------- 10: bindings (two new columns) and MA-005's branch value
    g10 = s.grid("10_MEASUREMENT_AGENDA")
    h10 = [str(x) if x is not None else None for x in g10[3]]
    if "evidence_bindings" in h10 or "source_bindings" in h10:
        raise TxError(f"{F}: 10 already has binding columns")
    width = max(i for i, x in enumerate(h10, 1) if x)
    ce, cs = width + 1, width + 2
    s.set(F + ":1a", "10_MEASUREMENT_AGENDA", 4, ce, "evidence_bindings", None, "10.header.evidence_bindings")
    s.set(F + ":1a", "10_MEASUREMENT_AGENDA", 4, cs, "source_bindings", None, "10.header.source_bindings")
    rows10 = {r[0]: i for i, r in enumerate(g10, 1) if i > 4 and r and r[0]}
    if list(rows10) != list(MA_BIND):
        raise TxError(f"{F}: 10 priorities are {list(rows10)}")
    for mid, (ev, so) in MA_BIND.items():
        s.set(F + ":1a", "10_MEASUREMENT_AGENDA", rows10[mid], ce, json.dumps(ev), None, f"{mid}.evidence_bindings")
        s.set(F + ":1a", "10_MEASUREMENT_AGENDA", rows10[mid], cs, json.dumps(so), None, f"{mid}.source_bindings")
    t10 = Table(s, "10_MEASUREMENT_AGENDA")
    ma005 = [(MA005_BRANCH[0], MA005_END[0]), (MA005_BRANCH[1], MA005_END[1], MA005_TERM_AR)]
    for pairs, fld in zip(ma005, ("current_evidence_en", "current_evidence_ar")):
        cur = new = t10.get("MA-005", fld)
        for old, rep in pairs:
            if not isinstance(new, str) or new.count(old) != 1:
                raise TxError(f"{F}: MA-005 {fld} does not hold {old!r} once")
            new = new.replace(old, nfc(rep))
        t10.set(F + ":1a", "MA-005", fld, new, cur)
    for mid, fields in MA_TEXT.items():   # red-team S1, S4, S5: each text states what its bindings hold
        for fld, (old, rep) in fields.items():
            cur = t10.get(mid, fld)
            if not isinstance(cur, str) or cur.count(old) != 1:
                raise TxError(f"{F}: {mid} {fld} does not hold {old[:50]!r} once")
            t10.set(F + ":1a", mid, fld, cur.replace(old, nfc(rep)), cur)

    # ---------------------------------------------------------------- 06/11: composite members and framing (item 1b)
    t06 = Table(s, "06_EVIDENCE_OBJECTS")
    for oid, (old, new) in COMPOSITE_MEMBERS.items():
        t06.set(F + ":1b", oid, "source_dependencies", new, old)
    ui = {r[0]: r for r in s.grid("04_NAV_UX") if r and isinstance(r[0], str) and r[0].startswith("UI-")}
    unlisted = (ui["UI-VERIFY-COMPOSITE-UNLISTED"][1], ui["UI-VERIFY-COMPOSITE-UNLISTED"][2])
    composite = (ui["UI-VERIFY-COMPOSITE"][1], ui["UI-VERIFY-COMPOSITE"][2])
    framing = (ui["UI-EVID-FRAMING"][1], ui["UI-EVID-FRAMING"][2])
    for oid in ("VIS-PROVIDER-OBSERVABILITY", "DS-DEMAND-VINTAGE-LENS", "CLM-014"):
        t06.set(F + ":1b", oid, "verification_en", composite[0], unlisted[0])
        t06.set(F + ":1b", oid, "verification_ar", composite[1], unlisted[1])
    for fld, (old, rep) in FRAME_TEXT.items():   # red-team S21: the record reads as a frame, not as documented relationships
        cur = t06.get("VIS-INCLUSION-TRANSMISSION", fld)
        if not isinstance(cur, str) or cur.count(old) != 1:
            raise TxError(f"{F}: VIS-INCLUSION-TRANSMISSION {fld} does not hold {old[:50]!r} once")
        t06.set(F + ":1b", "VIS-INCLUSION-TRANSMISSION", fld, cur.replace(old, nfc(rep)), cur)
    for oid in FRAMING:
        t06.set(F + ":1b", oid, "lineage_state", "FRAMING_NO_FACT", "COMPOSITE_OF_OBJECTS")
        t06.set(F + ":1b", oid, "verification_en", framing[0], unlisted[0])
        t06.set(F + ":1b", oid, "verification_ar", framing[1], unlisted[1])
    t11 = Table(s, "11_VISUAL_LIBRARY")
    t11.set(F + ":1b", ACCESS_LAYER[0], "data_inputs", ACCESS_LAYER[2], ACCESS_LAYER[1])
    t11.set(F + ":1b", MFI_DIV[0], "data_inputs", MFI_DIV[2], MFI_DIV[1])

    # ---------------------------------------------------------------- CR-21: every cell that prints the day-precise period
    keep_rows = {t06.rows[k] for k in CR21_KEEP}
    vs_col = t06.col("value_states")
    changed = 0
    for sheet in ("02_SITE_MAP", "03_PAGE_SECTIONS", "06_EVIDENCE_OBJECTS", "08_READINGS", "11_VISUAL_LIBRARY", "15_SOURCE_LIBRARY",
                  "25_FINDEX_BASELINE", "34_EVIDENCE_PASSPORTS"):
        g = s.grid(sheet)
        hdr = [str(x) if x is not None else None for x in g[3]] if len(g) > 3 else []
        skip = {hdr.index(c) + 1 for c in CR21_SKIP_COLS.get(sheet, ()) if c in hdr}
        for i, row in enumerate(g, 1):
            for j, v in enumerate(row, 1):
                if not isinstance(v, str) or j in skip:
                    continue
                if sheet == "06_EVIDENCE_OBJECTS" and j == vs_col:
                    continue
                new = v
                for old_p, new_p in CR21_PHRASES:
                    new = new.replace(old_p, new_p)
                if new != v:
                    s.set(F + ":CR-21", sheet, i, j, new, v, f"{sheet}!r{i}c{j}")
                    changed += 1
                    if sheet == "06_EVIDENCE_OBJECTS" and i not in keep_rows:
                        cur_vs = s.ed.get_value(sheet, i, vs_col)
                        nv = cr21_states(cur_vs)
                        if nv != cur_vs:
                            s.set(F + ":CR-21", sheet, i, vs_col, nv, cur_vs, f"06!r{i}.value_states")
    if changed < 100:
        raise TxError(f"{F}: CR-21 changed only {changed} cells")
    # red-team B1: no printed cell keeps the day-precise end date (provenance columns and value states excepted)
    for sheet in ("02_SITE_MAP", "03_PAGE_SECTIONS", "06_EVIDENCE_OBJECTS", "08_READINGS", "11_VISUAL_LIBRARY", "15_SOURCE_LIBRARY",
                  "25_FINDEX_BASELINE", "34_EVIDENCE_PASSPORTS"):
        g = s.grid(sheet)
        hdr = [str(x) if x is not None else None for x in g[3]] if len(g) > 3 else []
        skip = {hdr.index(c) + 1 for c in CR21_SKIP_COLS.get(sheet, ()) if c in hdr}
        for i, row in enumerate(g, 1):
            for j, v in enumerate(row, 1):
                if (not isinstance(v, str) or j in skip or (sheet == "06_EVIDENCE_OBJECTS" and (j == vs_col or i in keep_rows))):
                    continue
                if any(x in v for x in ("9 January 2023", "9 يناير 2023", "2023-01-09")):
                    raise TxError(f"{F}: CR-21 left a day-precise date in {sheet}!r{i}c{j}")
    # CLM-023: the method note keeps both World Bank dates, with their locators, and states the one-day difference
    for fld, add in (("method_en", CLM023_NOTE[0]), ("method_ar", CLM023_NOTE[1])):
        cur = t06.get("CLM-023", fld)
        if "10 January 2023" in str(cur) or "10 يناير 2023" in str(cur):
            raise TxError(f"{F}: CLM-023 {fld} already carries the note")
        t06.set(F + ":CR-21", "CLM-023", fld, cur + nfc(add), cur)
    cur = t06.get("CLM-023", "value_states")
    t06.set(F + ":CR-21", "CLM-023", "value_states", add_states(cr21_states(cur), CLM023_STATES), cur)

    # ---------------------------------------------------------------- CR-22: /methodology/ s7 (one row per language)
    for lang, (old, new) in zip(("en", "ar"), CR22):
        s.replace_section(F + ":CR-22", "/methodology/", 7, lang, "body", old, nfc(new))

    # ---------------------------------------------------------------- CLM-039: Brief 40 recorded, no value taken
    for fld, add in (("summary_en", CLM039[0]), ("summary_ar", CLM039[1])):
        cur = t06.get("CLM-039", fld)
        t06.set(F + ":CLM-039", "CLM-039", fld, cur + nfc(add), cur)
    cur = t06.get("CLM-039", "source_dependencies")
    t06.set(F + ":CLM-039", "CLM-039", "source_dependencies", cur + "; " + MDB40, cur)
    cur = t06.get("CLM-039", "value_states")
    t06.set(F + ":CLM-039", "CLM-039", "value_states", add_states(cur, CLM039_STATES), cur)

    # ---------------------------------------------------------------- e-money history (VIS-E-MONEY-RULE-STACK, CLM-012)
    for fld, add in (("summary_en", EMONEY[0]), ("summary_ar", EMONEY[1])):
        cur = t06.get("VIS-E-MONEY-RULE-STACK", fld)
        t06.set(F + ":EMONEY", "VIS-E-MONEY-RULE-STACK", fld, cur + nfc(add), cur)
    for oid in ("VIS-E-MONEY-RULE-STACK", "CLM-012"):
        cur = t06.get(oid, "source_dependencies")
        t06.set(F + ":EMONEY", oid, "source_dependencies", cur + "; " + SANAA, cur)
    cur = t06.get("VIS-E-MONEY-RULE-STACK", "value_states")
    t06.set(F + ":EMONEY", "VIS-E-MONEY-RULE-STACK", "value_states", add_states(cur, EMONEY_STATES), cur)
    for fld, (old, new) in zip(("limitations_en", "limitations_ar"), CLM012):
        cur = t06.get("CLM-012", fld)
        if not isinstance(cur, str) or cur.count(old) != 1:
            raise TxError(f"{F}: CLM-012 {fld} does not hold {old!r} once")
        t06.set(F + ":EMONEY", "CLM-012", fld, cur.replace(old, nfc(new)), cur)

    # ---------------------------------------------------------------- CCY-PRESSURE: CWR-010 s6 and its source binding
    row = s.section_row(CWR010_ROUTE, 6, "en")
    for lang, pairs in zip(("en", "ar"), CWR010):
        col = COL03[f"body_{lang}"]
        cur = s.ed.get_value(S03, row, col)
        new = cur
        for old, rep in pairs:
            if new.count(old) != 1:
                raise TxError(f"{F}: CWR-010 s6 {lang} does not hold {old[:40]!r} once")
            new = new.replace(old, nfc(rep))
        s.set(F + ":CCY", S03, row, col, new, cur, f"{CWR010_ROUTE}#s6.body_{lang}")
    t08 = Table(s, "08_READINGS")
    cur = t08.get("CWR-010", "source_bindings")
    lst = json.loads(cur)
    if CCY_P in lst:
        raise TxError(f"{F}: CWR-010 already binds {CCY_P}")
    t08.set(F + ":CCY", "CWR-010", "source_bindings", json.dumps(lst + [CCY_P]), cur)
    t08.set(F + ":CCY", "CWR-010", "last_reviewed", TODAY, t08.get("CWR-010", "last_reviewed"))
    for fld, (old, rep) in zip(("evidence_period_en", "evidence_period_ar"), CWR010_PERIOD):   # red-team S19: the reading's clock
        cur = t08.get("CWR-010", fld)
        if not isinstance(cur, str) or cur.count(old) != 1:
            raise TxError(f"{F}: CWR-010 {fld} does not hold {old[:50]!r} once")
        t08.set(F + ":CCY", "CWR-010", fld, cur.replace(old, nfc(rep)), cur)

    t15 = Table(s, "15_SOURCE_LIBRARY")   # red-team NIT 11: the source's retrieval date is the snapshot's
    t15.set(F + ":1a", FAS_SRC, "retrieval_date", TODAY, t15.get(FAS_SRC, "retrieval_date"))

    counts = refresh_self_counts(s, F + ":OWN-10")
    rep = s.save(out, ledger, OrderedDict([
        ("transaction", F),
        ("summary", "Stage A addendum: Measurement Agenda bindings and three new Evidence Records (item 1a); composite members "
                    "listed or framing stated (item 1b); CR-21 fieldwork period; CR-22 precision; CLM-039 Brief 40; the CCY "
                    "cash-pressure finding in CWR-010; the e-money history statement."),
        ("self_counts", counts)]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
