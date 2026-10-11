# -*- coding: utf-8 -*-
"""Close-out transaction CLOSE-6B (Stage A addendum, advisor review of 11 October 2026, item 3): source utilisation.
English and Arabic change together.

  python3 close_6b.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Every write checks the exact current value. The reads behind it (11 October 2026) are kept in audit/close_out/addendum/:
R2 (the two Sana'a Center papers), R3 (Circular No. 12 of 2024 of the Central Bank of Yemen in Sana'a, the UN Panel of
Experts' report S/2024/731, the DOI of the University of Aden article, the CBY-Aden Quarterly Bulletin, the 2015 annual
report and the two Sana'a news locators), R4 (the AMB paper, KfW 47229, the CCY cover) and R7 (the CBY-Aden instruments,
re-read in the original with page locators).

- Merges. SRC-SANAA-CTR-MFB-2024 and SRC-SANAA-CTR-EMONEY-2022 were second records of SRC-SANAA-MFB-2024 and
  SRC-SANAA-EMONEY-2022 (R2: the e-money PDFs are byte-identical; the microfinance PDFs differ only on the cover). Their
  addresses become additional URLs of the canonical records; the two records are retired, with a note naming the record
  that carries them, and feed nothing. Both papers are by the Sana'a Center Economic Unit, prepared by the Sana'a Center
  for Strategic Studies with DeepRoot Consulting and CARPO (Rethinking Yemen's Economy); "Publisher: DeepRoot
  Consulting" misstated them and is corrected in the retired rows too.
- Completions. Circular No. 12 of 2024 of the Central Bank of Yemen in Sana'a (13 March 2024, in force 14 March) gets its
  title, issuer, label and date, with the note that a news site republished it; it is the one Sana'a instrument in the
  regulatory group, whose scope line now says so. The University of Aden article (DOI 10.36056/0442-000-018-001) is a
  journal article, not a CBY-Aden publication; 32_QUAL_LITERATURE is reconciled with the Crossref metadata. The Quarterly
  Bulletin gets its subtitle. The AMB card names its two authors and says the paper does not distinguish the two central
  banks. The CCY report's issuer line gives the cover as printed (logos, no "with").
- Withheld (the XIDIAN precedent: primary URL removed, address kept in a NON_PUBLIC note; none feeds a record): the 2015
  annual report (unreachable, captures unopened), LIT-INVEST and LIT-OEB (not Yemen evidence; method-bounded), CBY-Sana'a
  Circular No. 14 (reproduced only in S/2024/731, which would be cited as its own source if used), the Saba/CBY-Sana'a
  2024 item (unreadable) and the KfW RMMV conference page (a method reference).
- Regulation on /data/. The ten CBY instruments and reports whose cards were bare carry what they require (why it
  matters) and what they do not establish, from 31_REFORMS_REGULATION and R7, in both languages.
- Chronology (issuance is not implementation). New: the e-KYC instructions (9 November 2023) and
  Decision No. 7 of 2026 (9 April 2026, in force 12 April 2026); the e-KYC event refers to MA-007. YSC-012 gains Decision No. 19 of 2024, paired neutrally
  with Circular No. 12 of 2024 of the Central Bank of Yemen in Sana'a. YSC-015 gains CBY-Aden's news item on the
  committee's first meeting (17 July 2025), which states no establishing decision. The AML circulars of 2025 stay as
  directory cards: neither changes an access channel that a dated event could show.
- Not changed: KfW 47229 prints no date, so its card keeps none (EUR 4.5 million belongs to phase III, and to phase I, by the KfW funding
  field and the IATI commitment of 24 November 2021, but the card does not print it). The two duplicate-free context
  cards the advisor named (ACAPS 2021, the Sana'a Center trade-finance brief) stay as they are.
"""
import json, os, sys, unicodedata
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from close_lib import Session, Table, TxError, refresh_self_counts, set_ui  # noqa: E402
from rc_lib import S04, ui_block_end  # noqa: E402

F = "CLOSE-6B"
TODAY = "2026-10-11"
READ = "read 11 October 2026"
CBY, CBY_AR = "Central Bank of Yemen — Aden", "البنك المركزي اليمني – عدن"
SANAA_CB, SANAA_CB_AR = "Central Bank of Yemen — Sana'a", "البنك المركزي اليمني – صنعاء"
SC, SC_AR = "Sana’a Center for Strategic Studies", "مركز صنعاء للدراسات الاستراتيجية"


def nfc(o):
    if isinstance(o, str):
        return unicodedata.normalize("NFC", o)
    if isinstance(o, (list, tuple)):
        return type(o)(nfc(x) for x in o)
    if isinstance(o, dict):
        return OrderedDict((k, nfc(v)) for k, v in o.items())
    return o


def vs(t, k, s, src=None, loc=None):
    e = OrderedDict([("t", t), ("k", k), ("s", s)])
    if src:
        e["src"] = src
    if loc:
        e["loc"] = loc + "; " + READ
    return e


def d(t, src, loc):
    return vs(t, "d", "READ", src, loc)


# ================================================================================================ merges
DR = "https://deeproot.consulting/en/publications/"
MERGES = OrderedDict([
    ("SRC-SANAA-CTR-MFB-2024", OrderedDict([
        ("into", "SRC-SANAA-MFB-2024"),
        ("urls", [DR + "enhancing-the-role-of-microfinance-banks-for-sustainable-impact-in-yemen", DR + "83/download"]),
        ("same", "the same policy brief (RYE Policy Brief 29; pages 2 to 16 are identical, only the cover build differs)"),
        ("title", ("Enhancing the Role of Microfinance Banks for Sustainable Impact in Yemen (2024)",
                   "Enhancing the Role of Microfinance Banks for Sustainable Impact in Yemen (Sana’a Center Economic Unit, "
                   "September 2024)")),
        ("title_ar", ("تعزيز دور بنوك التمويل الأصغر لتحقيق أثر مستدام في اليمن (2024)",
                      "تعزيز دور بنوك التمويل الأصغر لتحقيق أثر مستدام في اليمن (الوحدة الاقتصادية في مركز صنعاء، سبتمبر 2024)")),
        ("date", ("2024-09-23", "2024-09-23")),
        ("issuer", "Sana’a Center Economic Unit (author line, p.1); prepared by the Sana’a Center for Strategic Studies in "
                   "coordination with DeepRoot Consulting and CARPO, Rethinking Yemen’s Economy, RYE Policy Brief 29"),
        ("hosting", "Sana’a Center for Strategic Studies; a copy is also hosted by DeepRoot Consulting (pages 2–16 identical; "
                    "the cover's preparation line differs)"),
    ])),
    ("SRC-SANAA-CTR-EMONEY-2022", OrderedDict([
        ("into", "SRC-SANAA-EMONEY-2022"),
        ("urls", [DR + "challenges-and-prospects-for-electronic-money-and-payment-systems-in-yemen", DR + "73/download"]),
        ("same", "the same white paper (the two PDFs are byte-identical)"),
        ("title", ("Challenges and Prospects for Electronic Money and Payment Systems in Yemen",
                   "Challenges and Prospects for Electronic Money and Payment Systems in Yemen (Sana’a Center Economic Unit, "
                   "March 2022)")),
        ("title_ar", ("تحديات وآفاق النقود الإلكترونية وأنظمة الدفع في اليمن",
                      "تحديات وآفاق النقود الإلكترونية وأنظمة الدفع في اليمن (الوحدة الاقتصادية في مركز صنعاء، مارس 2022)")),
        ("date", ("2022-03-07", "2022-03")),          # the PDF prints only "March 2022"; 7 March is the web page's date
        ("issuer", "Sana’a Center Economic Unit (author line, p.1); prepared by the Sana’a Center for Strategic Studies in "
                   "coordination with DeepRoot Consulting and CARPO, Rethinking Yemen’s Economy (white paper)"),
        ("hosting", "Sana’a Center for Strategic Studies (first posted 7 March 2022); an identical copy is hosted by "
                    "DeepRoot Consulting"),
    ])),
])

# ================================================================================================ completions
C12 = "SRC-CBY-SANAA-C12-2024"
C12_CARD = OrderedDict([
    ("display_title", "Circular No. 12 to all banks and exchange companies and establishments: services of banks and "
                      "financial institutions operating external remittance services (13 March 2024)"),
    ("display_title_ar", "تعميم رقم (12) موجه إلى كافة البنوك وشركات ومنشآت الصرافة بشأن خدمات البنوك والمؤسسات المالية "
                         "المشغلة لخدمات الحوالات الخارجية (13 مارس 2024)"),
    ("publisher", SANAA_CB), ("publisher_ar", SANAA_CB_AR),
    ("issuer", "Central Bank of Yemen, Head Office, Sana'a, Banking Supervision Sector (letterhead, every page)"),
    ("hosting_platform", "Yemen Eco (yemeneco.org), a news site that republished the document; it is not the issuer"),
    ("document_label", "Circular or instruction"), ("document_label_ar", "تعميم أو تعليمات"),
    ("document_date", "2024-03-13"), ("public_card_state", "CITATION_CARD"), ("retrieval_date", TODAY),
])
LIQ = "SRC-ADEN-CBY-LIQ-2016"
LIQ_DOI = "https://doi.org/10.36056/0442-000-018-001"
LIQ_CARD = OrderedDict([
    ("primary_url", LIQ_DOI), ("additional_urls", json.dumps(["https://search.mandumah.com/Record/932295"])),
    ("display_title", "The Central Bank of Yemen and Domestic Liquidity Management (Journal of Administrative and Economic "
                      "Sciences, University of Aden, 2016)"),
    ("display_title_ar", "البنك المركزي اليمني وإدارة السيولة المحلية (مجلة العلوم الإدارية والاقتصادية، جامعة عدن، 2016)"),
    ("publisher", "University of Aden, Faculty of Economics and Administration"),
    ("publisher_ar", "جامعة عدن، كلية الاقتصاد والإدارة"),
    ("issuer", "A journal article by Majdoleen Mohammed Abdo Saeed (مجدولين محمد عبده سعيد in the Crossref record; the "
               "transliteration is not printed); published by the University of "
               "Aden, Faculty of Economics and Administration (Crossref member 21867); not a publication of the Central Bank "
               "of Yemen"),
    ("hosting_platform", "The DOI resolves to the Dar Almandumah database record, whose page requires sign-in"),
    ("document_label", "Research or policy paper"), ("document_label_ar", "ورقة بحثية أو سياساتية"),
    ("document_date", "2016"), ("public_card_state", "CITATION_CARD"), ("retrieval_date", TODAY),
])
LIQ_32 = OrderedDict([
    ("source_reported_content", (
        "Verified metadata identifies author Majdoleen Mohammad Abdu Saeed, issue 18, Dec 2016, pp. 9–40, DOI "
        "10.36056/0442-000-018-001.",
        "Crossref metadata (read 11 October 2026): author مجدولين محمد عبده سعيد; title «البنك المركزي اليمني وإدارة السيولة "
        "المحلية»; Journal of Administrative and Economic Sciences, published by the University of Aden, Faculty of Economics "
        "and Administration; issued 2016; first page 9; DOI 10.36056/0442-000-018-001, which resolves to "
        "search.mandumah.com/Record/932295. Issue 18 is inferred from the DOI suffix and an end page of about 40 from the next "
        "article's first page (41); the month is not in the metadata.")),
    ("study_population_or_method", ("Full substantive text not yet reviewed.",
                                    "Full substantive text not yet reviewed: the record page requires sign-in.")),
    ("source_url", ("https://search.mandumah.com/Record/932295", LIQ_DOI)),
])
HIST = "SRC-CBY-HIST-METHOD-001"
HIST_CARD = OrderedDict([
    ("display_title", ("Quarterly Bulletin, Issue No. 1 (December 2020)",
                       "Quarterly Bulletin: Economic and Monetary Developments, Issue No. 1 (December 2020)")),
    ("display_title_ar", ("النشرة الفصلية، العدد 1 (ديسمبر 2020)", "النشرة الفصلية: التطورات الاقتصادية والنقدية، العدد 1 (ديسمبر 2020)")),
    ("issuer", (None, "General Department of Research and Statistics, Central Bank of Yemen, Head Office – Aden (title page)")),
    ("retrieval_date", ("2026-10-04", TODAY)),
])
AMB = "SRC-AMB-MFB-SUPERVISION-2026"
AMB_TEXT = OrderedDict([
    ("why_it_matters", ("A paper by authors from Al-Amal Microfinance Bank on how",
                        "A policy brief by Mohammed Al-Lai and Dhekra Al-Gabri, published by Al-Amal Microfinance Bank, on how")),
    ("why_it_matters_ar", ("ورقة أعدها مؤلفون من بنك الأمل للتمويل الأصغر حول",
                           "ورقة سياسات موجزة أعدها محمد اللاعي وذكرى الجبري، ونشرها بنك الأمل للتمويل الأصغر، حول")),
    ("does_not_establish", ("A proposal by authors from a microfinance bank: it is not a statement by the regulator or an "
                            "independent assessment,",
                            "A proposal published by a microfinance bank: it is not a statement by the regulator or an "
                            "independent assessment. It treats the Central Bank of Yemen as a single supervisor, without "
                            "distinguishing the one in Aden from the one in Sana'a, and")),
    ("does_not_establish_ar", ("مقترح أعده مؤلفون من بنك للتمويل الأصغر: فهو ليس بيانًا صادرًا عن الجهة الرقابية ولا تقييمًا مستقلًا،",
                               "مقترح نشره بنك للتمويل الأصغر: فهو ليس بيانًا صادرًا عن الجهة الرقابية ولا تقييمًا مستقلًا. "
                               "ويتناول البنك المركزي اليمني بوصفه جهة رقابية واحدة دون أن يميّز بين البنك المركزي اليمني في عدن "
                               "ونظيره في صنعاء،")),
])
AMB_ISSUER = ("Al-Amal Microfinance Bank",
              "Mohammed Saleh Al-Lai and Dhekra Ahmed Al-Gabri (authors, cover: “Prepared by”); Al-Amal Microfinance Bank "
              "(publisher, FinDev Gateway page); no author affiliation is printed in the paper")
CCY = "SRC-CCY-PRESSURE-2026"
CCY_ISSUER = ("Cash Consortium of Yemen, with Crisis Analysis MENA/Europe (cover)",
              "Cash Consortium of Yemen (cover logos: the Cash Consortium of Yemen; Crisis Analysis MENA/Europe, with a Mercy "
              "Corps mark; European Union Civil Protection and Humanitarian Aid); no author is printed")

# ================================================================================================ withheld
NP = "NON_PUBLIC (close-out CLOSE-6B, 11 October 2026; the XIDIAN precedent): "
WITHHOLD = OrderedDict([
    ("SRC-CBY-AR2015-HIST-001",
     "the address returned HTTP 503 or a reset connection on 11 October 2026; the Wayback Machine lists captures of 16 March "
     "2019 and 30 June 2022, which could not be opened from this environment, so the title and issuer were not read; feeds no "
     "record; withheld from the public directory until a person confirms an archived copy."),
    ("SRC-LIT-INVEST-ISLAMIC-FI-2024",
     "comparative Islamic-finance literature, not Yemen evidence (32_QUAL_LITERATURE LIT-ISLAMIC-2024-001, "
     "COMPARATIVE_CONCEPT_ONLY); feeds no public record; withheld from the public directory."),
    ("SRC-LIT-OEB-FX-PRICES-2025",
     "a regression on eight annual observations whose construction and territorial comparability have not been reviewed "
     "(32_QUAL_LITERATURE LIT-YEM-2025-006, QUANTITATIVE_HYPOTHESIS__METHOD_BOUNDED); feeds no public record; withheld from "
     "the public directory."),
    ("SRC-CBY-SANAA-C14-2024",
     "Circular No. 14 of 2024 of the Central Bank of Yemen in Sana'a (26 March 2024) has no locator of its own; the final "
     "report of the UN Panel of Experts on Yemen, S/2024/731 of 11 October 2024, reproduces it as Figure 28.2 of Annex 28 "
     "(printed p. 114). This record feeds no record and is withheld; if the circular is used, S/2024/731 is cited as its own "
     "source, never as if it were the circular. cbyemen.com must not be cited (the domain serves an unrelated site)."),
    ("SRC-CBY-SANAA-CURR-2024",
     "saba.ye returned HTTP 403 (a Cloudflare challenge) and centralbank.gov.ye HTTP 503 or a reset connection on 11 October "
     "2026; Wayback captures are listed (10 April 2026 and 31 August 2024) but could not be opened, so the title, date and "
     "issuer were not read; feeds no record; withheld from the public directory."),
    ("SRC-KFW-RMMV-2023-001",
     "a conference page and booklet on remote management, monitoring and verification tools: a method reference, not evidence "
     "on Yemen's financial system (33_ANALYTICS_MASTER CTR-007 reclassifies it to method); feeds no public record; withheld "
     "from the public directory."),
])

# ================================================================================================ /data/: what each instrument requires
SCOPE = ("UI-DATA-GROUP-REGULATORY-SCOPE",
         ("All were issued or posted by the Central Bank of Yemen – Aden; its undated pages on credit-risk information cite "
          "older instructions, the earliest from 1991. This group holds no law and no instrument issued in Sana'a; the one law",
          "All but one were issued or posted by the Central Bank of Yemen – Aden; its undated pages on credit-risk information "
          "cite older instructions, the earliest from 1991. The one instrument issued in Sana'a, a circular of the Central Bank "
          "of Yemen – Sana'a on paying out incoming external transfers, is held in the copy a news site republished. This group "
          "holds no law; the one law"),
         ("وقد أصدرها جميعًا أو نشرها البنك المركزي اليمني – عدن؛ وتشير صفحتاه غير المؤرختين عن معلومات مخاطر الائتمان إلى "
          "تعليمات أقدم، أولها من عام 1991. ولا تضم هذه المجموعة أي قانون ولا أي وثيقة صادرة في صنعاء؛ أما",
          "وجميعها، عدا وثيقة واحدة، أصدرها البنك المركزي اليمني – عدن أو نشرها؛ وتشير صفحتاه غير المؤرختين عن معلومات مخاطر "
          "الائتمان إلى تعليمات أقدم، أولها من عام 1991. والوثيقة الوحيدة الصادرة في صنعاء تعميمٌ للبنك المركزي اليمني – صنعاء "
          "بشأن صرف الحوالات الخارجية الواردة، والنسخة المتوفرة منه هي التي أعاد موقع إخباري نشرها. ولا تضم هذه المجموعة أي "
          "قانون؛ أما"))

CARDS = OrderedDict([   # source -> (why EN, why AR, does not establish EN, AR)
    ("SRC-CBY-EKYC-2023", (
        "CBY-Aden's instructions for banks and licensed mobile e-money providers on opening accounts remotely, without the "
        "customer present in person; the institutions report, every half year, figures that include the average time to "
        "complete an application and to open and activate an account.",
        "تعليمات البنك المركزي اليمني – عدن للبنوك ولمقدمي خدمات النقود الإلكترونية عبر الهاتف المحمول المرخص لهم بشأن فتح "
        "الحسابات عن بُعد دون حضور العميل شخصيًا؛ وتُبلغ هذه المؤسسات كل نصف سنة عن بيانات منها متوسط الوقت المستغرق لاستكمال "
        "الطلب ولفتح الحساب وتفعيله.",
        "The instructions do not show that remote account opening is offered or used, how long it takes in practice, or how "
        "many people opened accounts this way; they fix no date of entry into force, only compliance periods counted from it.",
        "لا تُظهر التعليمات أن فتح الحسابات عن بُعد متاح أو مستخدم، ولا المدة التي يستغرقها فعليًا، ولا عدد من فتحوا حسابات بهذه "
        "الطريقة؛ ولا تحدد تاريخ نفاذها، وإنما تحدد مُهَلًا للامتثال تُحسب من ذلك التاريخ.")),
    ("SRC-CBY-CIRC-01-2024", (
        "Rules for banks that wish to ship surplus foreign-currency banknotes abroad: an application to the Governor ahead of "
        "each shipment, a ceiling per shipment, a minimum period for which the funds shipped must have been deposited, and "
        "confirmation of the credit abroad after shipment.",
        "قواعد للبنوك التي ترغب في ترحيل فوائض أوراق النقد الأجنبي إلى الخارج: طلب يُقدَّم إلى المحافظ قبل كل شحنة، وسقف لكل "
        "شحنة، وحد أدنى لمدة إيداع الأموال المرحَّلة، وتأكيد قيد المبالغ في الخارج بعد الشحن.",
        "The circular does not show how many shipments were requested, approved or made, or any effect on banks' "
        "foreign-currency liquidity.",
        "لا يُظهر المنشور عدد الشحنات التي طُلبت أو وُوفق عليها أو نُفذت، ولا أي أثر على سيولة البنوك من النقد الأجنبي.")),
    ("SRC-CBY-DEC-19-2024", (
        "CBY-Aden's rules for external money transfers: only through qualified banks or exchange companies, with its "
        "no-objection letter before any contract with an international money-transfer company or a sub-agent; sub-agents "
        "licensed by CBY-Aden, for which the main agent answers; and incoming transfers paid in the currency received unless "
        "the beneficiary asks to convert them at the market rate.",
        "قواعد البنك المركزي اليمني – عدن للتحويلات الخارجية: ألا تجري إلا عبر البنوك أو شركات الصرافة المؤهلة، مع الحصول على "
        "خطاب عدم ممانعة منه قبل أي تعاقد مع شركة حوالات دولية أو وكيل فرعي؛ وأن يكون الوكلاء الفرعيون مرخصًا لهم منه، ويكون "
        "الوكيل الرئيسي مسؤولًا عنهم؛ وأن تُصرف الحوالات الواردة بالعملة التي وردت بها ما لم يطلب المستفيد مصارفتها بسعر السوق.",
        "The decision does not show how many providers obtained no-objection letters, how transfers were actually paid out, "
        "or any effect on remittance costs or access.",
        "لا يُظهر القرار عدد مقدمي الخدمة الذين حصلوا على خطابات عدم ممانعة، ولا كيف صُرفت الحوالات فعليًا، ولا أي أثر على "
        "تكلفة الحوالات أو الوصول إليها.")),
    ("SRC-CBY-CIRC-02-2025", (
        "An anti-money laundering and counter-terrorist financing circular to banks and exchange companies and "
        "establishments, supplementing the earlier circulars on the subject (of 2012, 2013, 2014 and 2021).",
        "منشور لمكافحة غسل الأموال وتمويل الإرهاب موجه إلى البنوك وشركات ومنشآت الصرافة، مُلحق بالمنشورات السابقة في هذا "
        "الشأن (الصادرة في 2012 و2013 و2014 و2021).",
        "The circular does not show how it is supervised or enforced, or any effect on correspondent banking, remittance "
        "channels or access.",
        "لا يُظهر المنشور كيف يُراقَب تطبيقه أو كيف يجري إنفاذه، ولا أي أثر على علاقات المراسلة المصرفية أو قنوات الحوالات أو "
        "الوصول.")),
    ("SRC-CBY-CIRC-03-2025", (
        "Risk-management instructions applying to all banks, prepared with technical support from the IMF's Middle East "
        "Regional Technical Assistance Center (METAC).",
        "تعليمات لإدارة المخاطر تسري على جميع البنوك، أُعدّت بدعم فني من المركز الإقليمي للمساعدة الفنية للشرق الأوسط (METAC) "
        "التابع لصندوق النقد الدولي.",
        "The instructions do not show banks' compliance, the quality of their risk management, or any effect on lending or "
        "access.",
        "لا تُظهر التعليمات مدى امتثال البنوك، ولا جودة إدارتها للمخاطر، ولا أي أثر على الإقراض أو الوصول.")),
    ("SRC-CBY-CIRC-04-2025", (
        "Instructions to banks and exchange companies and establishments on enhanced due diligence and on screening against "
        "international sanctions lists, including those of the UN Security Council, the US Treasury (OFAC), the European "
        "Union and the UK Treasury.",
        "تعليمات للبنوك وشركات ومنشآت الصرافة بشأن إجراءات العناية الواجبة المعززة والتحقق من قوائم العقوبات الدولية، ومنها "
        "قوائم مجلس الأمن الدولي ومكتب مراقبة الأصول الأجنبية التابع لوزارة الخزانة الأمريكية (OFAC) والاتحاد الأوروبي ووزارة "
        "الخزانة البريطانية.",
        "The instructions do not show how screening is applied, how many customers or transfers it affects, or any effect on "
        "access to accounts or remittances.",
        "لا تُظهر التعليمات كيف يُطبَّق التحقق، ولا عدد العملاء أو التحويلات التي يمسّها، ولا أي أثر على الوصول إلى الحسابات أو "
        "الحوالات.")),
    ("SRC-CBY-DEC-07-2026", (
        "Sets a minimum rate of 18% a year on new Yemeni-rial savings deposits at commercial banks, leaves foreign-currency "
        "deposit rates and lending rates to banks, exempts Islamic banks, and applies to contracts concluded after it took "
        "effect on 12 April 2026.",
        "يحدد حدًا أدنى لسعر الفائدة قدره 18% سنويًا على ودائع الادخار الجديدة بالريال اليمني لدى البنوك التجارية، ويترك أسعار "
        "الفائدة على الودائع بالعملات الأجنبية وعلى الإقراض للبنوك، ويستثني البنوك الإسلامية، ويسري على العقود المبرمة بعد نفاذه "
        "في 12 أبريل 2026.",
        "The decision does not show the rates banks actually pay, deposit growth, or any effect on saving or on access to "
        "accounts.",
        "لا يُظهر القرار الأسعار التي تدفعها البنوك فعليًا، ولا نمو الودائع، ولا أي أثر على الادخار أو الوصول إلى الحسابات.")),
    ("SRC-CBY-CIRC-01-2026", (
        "Prohibits banks, exchange companies and establishments, payment-service providers and e-wallet operators from "
        "dealing in virtual assets or cryptocurrencies or with their service providers, in force from issue.",
        "يحظر على البنوك وشركات ومنشآت الصرافة ومقدمي خدمات الدفع ومشغلي المحافظ الإلكترونية التعامل بالأصول الافتراضية أو "
        "العملات المشفرة أو مع مقدمي خدماتها، ويُعمل به من تاريخ صدوره.",
        "The circular does not show how much such dealing there was before it, or how it is enforced.",
        "لا يُظهر المنشور حجم هذا التعامل قبل صدوره، ولا كيفية إنفاذه.")),
    ("SRC-CBY-BANKS-BS-2022", (
        "A Central Bank of Yemen statistical report on the banks' consolidated balance sheet to December 2022: total assets, "
        "deposits, loans and financing and equity, with the number of banks, branches and accounts. No issue date or issuing "
        "department appears on the pages read.",
        "تقرير إحصائي للبنك المركزي اليمني عن الميزانية المجمعة للبنوك حتى ديسمبر 2022: إجمالي الأصول والودائع والقروض "
        "والتمويلات وحقوق الملكية، مع عدد البنوك والفروع والحسابات. ولا يظهر تاريخ إصدار ولا اسم الإدارة المصدرة في الصفحات التي "
        "قُرئت.",
        "A count of accounts is not a count of people, and the report does not show who holds them or how they are used; one "
        "change figure it prints does not match its own values, so its figures are not taken without checking.",
        "عدد الحسابات ليس عدد الأشخاص، ولا يُظهر التقرير مَن يملكها ولا كيف تُستخدم؛ وفيه رقم للتغير لا يتطابق مع القيمتين اللتين "
        "يذكرهما، فلا تؤخذ أرقامه دون تحقق.")),
    (C12, (
        "The circular of the Central Bank of Yemen in Sana'a on how banks and exchange companies acting as main agents for "
        "external remittance services pay out incoming transfers: transfers in Saudi riyals are paid in Saudi riyals; "
        "individual transfers in US dollars are paid in their Saudi-riyal equivalent at the dollar rate its Foreign Exchange "
        "Dealing Unit approves, and those in other foreign currencies at the international selling rate against the Saudi "
        "riyal on the day the transfer was issued; it applies from 14 March 2024.",
        "تعميم البنك المركزي اليمني في صنعاء بشأن صرف الحوالات الواردة عبر البنوك وشركات الصرافة العاملة وكلاءَ رئيسيين لخدمات "
        "الحوالات الخارجية: تُصرف الحوالات الواردة بالريال السعودي بالريال السعودي، والحوالات الفردية الواردة بالدولار الأمريكي "
        "بما يعادلها بالريال السعودي بسعر الدولار الذي تعتمده وحدة التعاملات بالنقد الأجنبي لديه، والواردة بعملات أجنبية أخرى "
        "بما يعادلها بالريال السعودي بسعر البيع العالمي مقابل الريال السعودي يوم إصدار الحوالة؛ ويُعمل به اعتبارًا من 14 مارس "
        "2024.",
        "A circular states rules; it does not show how transfers were actually paid, at what rates, or how many recipients were "
        "affected. This copy was republished by a news site, not by the issuer.",
        "يحدد التعميم قواعد، ولا يُظهر كيف صُرفت الحوالات فعليًا، ولا بأي أسعار، ولا عدد المستفيدين المتأثرين. وهذه النسخة أعاد "
        "نشرها موقع إخباري، لا الجهة المصدرة.")),
])

# ================================================================================================ search: the Sana'a alias
# Alias 017 sends "Aden" to /providers/ and /data/; the cards that matched "Sanaa" by their placeholder titles are now
# titled or withheld, so the probe "Sanaa" (scripts/search_canonical_probe.json) needs the same neutral discovery aid.
ALIAS = OrderedDict([("alias_id", "SEARCH-ALIAS-046"), ("terms_en", "Sanaa; Sana'a; CBY Sanaa; CBY-Sanaa; CBY Sana'a"),
                     ("terms_ar", "صنعاء; البنك المركزي في صنعاء"), ("targets", "route:/providers/ | route:/data/"),
                     ("boundary_note_en", "Discovery aid only: this evidence base holds few documents issued in Sana'a; each source "
                                          "carries the scope of its issuer and does not describe all of Yemen."),
                     ("boundary_note_ar", "وسيلة للعثور على المحتوى فقط: لا تضم قاعدة الأدلة هذه إلا وثائق قليلة صادرة في صنعاء؛ "
                                          "ويحمل كل مصدر نطاق الجهة التي أصدرته، ولا يصف اليمن كله.")])


# ================================================================================================ chronology
def event(eid, period, period_ar, cls, fact, fact_ar, srcs, scope, impl, impl_ar, rel, rel_ar, dne, dne_ar, routes, note, states):
    return OrderedDict([("event_id", eid), ("period_en", period), ("event_class", cls), ("fact_en", fact), ("fact_ar", fact_ar),
                        ("source_ids", " | ".join(srcs)), ("source_scope", scope), ("system_implication_en", impl),
                        ("system_implication_ar", impl_ar), ("fi_relevance_en", rel), ("fi_relevance_ar", rel_ar),
                        ("does_not_establish_en", dne), ("does_not_establish_ar", dne_ar), ("relationship_type", "CONTEXT"),
                        ("linked_routes", routes), ("interpretation_note", note), ("period_ar", period_ar),
                        ("value_states", json.dumps(states, ensure_ascii=False, separators=(",", ":")))])


FL = "cby-ye.com/files/"
EVENTS = OrderedDict([   # event -> (row, the event it follows)
    ("YSC-031", (event(
        "YSC-031", "9 November 2023", "9 نوفمبر 2023", "CUSTOMER_DUE_DILIGENCE_RULE",
        "CBY-Aden issued instructions regulating electronic know-your-customer procedures (ref. 840/CBY/2023) for banks and "
        "licensed mobile e-money providers, setting how accounts may be opened remotely, without the customer present in "
        "person, and requiring these institutions to report every half year figures that include the average time to open "
        "and activate an account.",
        "أصدر البنك المركزي اليمني – عدن تعليمات تنظيم إجراءات اعرف عميلك إلكترونيًا (المرجع 840/CBY/2023) للبنوك ولمقدمي "
        "خدمات النقود الإلكترونية عبر الهاتف المحمول المرخص لهم، تحدد كيفية فتح الحسابات عن بُعد دون حضور العميل شخصيًا، "
        "وتُلزم هذه المؤسسات بالإبلاغ كل نصف سنة عن بيانات منها متوسط الوقت المستغرق لفتح الحساب وتفعيله.",
        ["SRC-CBY-EKYC-2023"], "CBY-Aden instructions (the rule text); no data on use.",
        "Remote account opening became a regulated route for the banks and e-money providers CBY-Aden supervises; whether they "
        "offer it, and to whom, is not reported.",
        "أصبح فتح الحسابات عن بُعد مسارًا منظمًا للبنوك ولمقدمي خدمات النقود الإلكترونية الخاضعين لرقابة البنك المركزي اليمني – "
        "عدن؛ ولم يُفصَح عمّا إذا كانوا يقدمونه ولا لمن يقدمونه.",
        "Identity checks and onboarding are a step at which account access can be lost; the average onboarding time the "
        "instructions ask institutions to report is the kind of journey measure that the measurement priority on digital "
        "onboarding and identity journeys asks for.",
        "التحقق من الهوية وإجراءات الانضمام مرحلةٌ قد يتعثر فيها الوصول إلى الحسابات؛ ومتوسط وقت فتح الحساب الذي تطلب التعليمات "
        "من المؤسسات الإبلاغ عنه هو من نوع مقاييس الرحلة التي تطلبها أولوية القياس «رحلات الانضمام الرقمي وإثبات الهوية».",
        "Issuing the instructions does not establish that remote onboarding is offered or used, how long it takes in practice, "
        "or that any reported figures were published; the instructions fix no date of entry into force, only compliance "
        "periods counted from it.",
        "لا يثبت إصدار التعليمات أن فتح الحسابات عن بُعد متاح أو مستخدم، ولا المدة التي يستغرقها فعليًا، ولا أن أي بيانات مُبلَّغ "
        "عنها قد نُشرت؛ ولا تحدد التعليمات تاريخ نفاذها، وإنما تحدد مُهَلًا للامتثال تُحسب من ذلك التاريخ.",
        "/people | /payments | /measurement | /reforms", "Issuance is not implementation.",
        [d("9 November 2023", "SRC-CBY-EKYC-2023", FL + "65806fe2b3757.pdf p.1: ref. 840/CBY/2023, dated 9/11/2023; Hijri date "
                                                  "(25 Rabi' al-Akhir 1445) p.16; remote opening without the customer present, "
                                                  "p.2; half-yearly reporting deadlines, p.15; Annex 5 item 3, average times, "
                                                  "p.30; compliance periods, pp.14 and 16; no effective-date clause in the 30 "
                                                  "pages"),
         vs("840", "v", "TRIVIAL")]), "YSC-025")),
    ("YSC-032", (event(
        "YSC-032", "9 April 2026 (in force 12 April 2026)", "9 أبريل 2026 (يُعمل به اعتبارًا من 12 أبريل 2026)", "MONETARY_POLICY_RULE",
        "CBY-Aden's Governor's Decision No. 7 of 2026 set a minimum rate of 18% a year on new Yemeni-rial savings deposits at "
        "commercial banks, left foreign-currency deposit rates and lending rates to banks and exempted Islamic banks; it "
        "applies to contracts concluded after it took effect on 12 April 2026.",
        "حدّد قرار محافظ البنك المركزي اليمني رقم (7) لسنة 2026، الصادر في عدن، حدًا أدنى لسعر الفائدة قدره 18% سنويًا على "
        "ودائع الادخار الجديدة بالريال اليمني لدى البنوك التجارية، وترك أسعار الفائدة على الودائع بالعملات الأجنبية وعلى الإقراض "
        "للبنوك، واستثنى البنوك الإسلامية؛ ويسري على العقود المبرمة بعد نفاذه في 12 أبريل 2026.",
        ["SRC-CBY-DEC-07-2026"], "CBY-Aden decision (the rule text); no data on rates paid or deposits.",
        "A floor on the rate paid on new rial savings deposits at commercial banks became a monetary-policy instrument; the "
        "rates banks pay are not reported.",
        "أصبح الحد الأدنى لسعر الفائدة على ودائع الادخار الجديدة بالريال لدى البنوك التجارية أداة من أدوات السياسة النقدية؛ ولم "
        "يُفصَح عن الأسعار التي تدفعها البنوك.",
        "Deposit rates bear on whether keeping savings in a bank account is worthwhile, but a minimum rate is not a measure of "
        "saving or of account use.",
        "لأسعار الفائدة على الودائع صلة بجدوى الاحتفاظ بالمدخرات في حساب مصرفي، لكن الحد الأدنى للسعر ليس مقياسًا للادخار ولا "
        "لاستخدام الحسابات.",
        "The decision does not establish the rates banks actually pay, deposit growth, or any effect on saving or on access to "
        "accounts.",
        "لا يثبت القرار الأسعار التي تدفعها البنوك فعليًا، ولا نمو الودائع، ولا أي أثر على الادخار أو الوصول إلى الحسابات.",
        "/finance | /reforms", "A rule is not a rate paid.",
        [d("9 April 2026", "SRC-CBY-DEC-07-2026", FL + "69dcac86e3520.pdf p.1: ref. 220/CBY/2026, header date 9/4/2026 (the issue "
                                                    "line prints the Hijri and Gregorian months swapped); MPC meeting 8 April 2026"),
         d("12 April 2026", "SRC-CBY-DEC-07-2026", FL + "69dcac86e3520.pdf p.1, Art. 7 (entry into force)"),
         vs("18%", "v", "READ", "SRC-CBY-DEC-07-2026", FL + "69dcac86e3520.pdf p.1, Art. 1 (minimum rate on new rial savings "
                                                         "deposits at commercial banks)"),
         vs("7", "v", "TRIVIAL")]), "YSC-019")),
])
YSC012 = OrderedDict([
    ("fact_en", (None,
                 " Circular No. 12 of the Central Bank of Yemen in Sana'a (dated 13 March 2024, applying from 14 March 2024) "
                 "set how incoming external transfers are paid out through banks and exchange companies acting as main "
                 "agents, paying individual transfers in US dollars or other foreign currencies in their Saudi-riyal "
                 "equivalent; on 23 May 2024 Decision No. 19 of 2024 of the Governor of the Central Bank of Yemen in Aden "
                 "required external transfers to pass only through qualified banks or exchange companies, with the bank's "
                 "no-objection letter before contracts with international money-transfer companies or sub-agents, and "
                 "incoming transfers to be paid in the currency received unless the beneficiary asks to convert them.")),
    ("fact_ar", (None,
                 " وحدّد التعميم رقم (12) الصادر عن البنك المركزي اليمني في صنعاء (المؤرخ 13 مارس 2024، والمعمول به من 14 "
                 "مارس 2024) كيفية صرف الحوالات الخارجية الواردة عبر البنوك وشركات الصرافة العاملة وكلاءَ رئيسيين، فتُصرف "
                 "الحوالات الفردية الواردة بالدولار الأمريكي أو بعملات أجنبية أخرى بما يعادلها بالريال السعودي؛ وفي 23 مايو "
                 "2024 ألزم قرار محافظ البنك المركزي رقم (19) لسنة 2024، الصادر عن البنك المركزي اليمني في عدن، بأن تجري "
                 "التحويلات الخارجية عبر البنوك أو شركات الصرافة المؤهلة وحدها، مع الحصول على خطاب عدم ممانعة منه قبل التعاقد "
                 "مع شركات الحوالات الدولية أو الوكلاء الفرعيين، وبأن تُصرف الحوالات الواردة بالعملة التي وردت بها ما لم يطلب "
                 "المستفيد مصارفتها.")),
    ("does_not_establish_en", ("A directive or prohibition does not prove actual compliance, closure, relocation or user "
                               "access at every location.",
                               "A directive, circular, decision or prohibition does not prove actual compliance, closure, "
                               "relocation, how transfers were actually paid, or user access at every location.")),
    ("does_not_establish_ar", ("لا يثبت التوجيه أو الحظر الامتثال الفعلي أو الإغلاق أو الانتقال أو وصول المستخدم في كل موقع.",
                               "لا يثبت التوجيه أو التعميم أو القرار أو الحظر الامتثال الفعلي أو الإغلاق أو الانتقال أو كيفية "
                               "صرف الحوالات فعليًا أو وصول المستخدم في كل موقع.")),
])
YSC012_SOURCES = ["SRC-CBY-SANAA-C12-2024", "SRC-CBY-DEC-19-2024"]
YSC012_SCOPE = (" Rule texts of both central banks on paying out incoming external transfers: Circular No. 12 of the Central "
                "Bank of Yemen in Sana'a (in the copy a news site republished) and Decision No. 19 of 2024 of the Governor of "
                "the Central Bank of Yemen in Aden; neither shows how transfers were paid.")
YSC012_STATES = [
    d("13 March 2024", C12, "yemeneco.org copy of Circular No. 12, p.1, date field 'Date: 13/ 3 / 2024' and 3/9/1445 AH"),
    d("14 March 2024", C12, "same, p.1: 'ابتداءً من تاريخ 1445/09/04هـ الموافق 2024/03/14م'"),
    d("23 May 2024", "SRC-CBY-DEC-19-2024", FL + "6653499a7181b.pdf p.1: ref. 289/CBY/2024, dated 23/5/2024; issue line with "
                                                  "Hijri date (15 Dhu al-Qa'da 1445) p.3; Art.1 p.1, Art.2 p.2, Art.3 (payout "
                                                  "currency) and Art.4 (in force) p.3"),
    vs("12", "v", "TRIVIAL"), vs("19", "v", "TRIVIAL")]
NEWS832 = "SRC-CBY-NEWS-832"
NEWS832_ROW = OrderedDict([
    ("source_id", NEWS832), ("primary_url", "https://cby-ye.com/news/832"), ("additional_urls", None),
    ("datasets_or_use", "DS-REFORM-EVENTS"), ("row_count", 0),
    ("display_title", "The Committee for Financing and Regulating Imports holds its first meeting (17 July 2025)"),
    ("display_title_ar", "لجنة تمويل وتنظيم الاستيراد تدشن أولى اجتماعاتها (17 يوليو 2025)"),
    ("publisher", CBY), ("publisher_ar", CBY_AR), ("public_card_state", "CITATION_CARD"), ("rights_state", "NOT_ASSESSED"),
    ("retrieval_date", TODAY), ("document_label", "News release"), ("document_label_ar", "بيان صحفي"),
    ("document_date", "2025-07-17"),
])
YSC015 = OrderedDict([
    ("fact_en", (None,
                 " CBY-Aden reported that the committee, which it called the Committee for Financing and Regulating Imports, "
                 "held its first meeting on 17 July 2025 at the central bank in Aden, chaired by the Governor with the Minister "
                 "of Trade and Industry as deputy chair, and that its members include the government bodies concerned with "
                 "finance, trade, and customs and judicial enforcement, with representatives of banks, exchange companies and "
                 "the commercial sector.")),
    ("fact_ar", (None,
                 " وأفاد البنك المركزي اليمني – عدن بأن اللجنة، التي سمّاها «لجنة تمويل وتنظيم الاستيراد»، عقدت أول اجتماعاتها "
                 "في 17 يوليو 2025 في مبنى البنك المركزي بعدن برئاسة المحافظ وبحضور وزير التجارة والصناعة نائبًا لرئيسها، وأنها "
                 "تضم الجهات الحكومية المعنية بالتمويل والتجارة والضبطية الجمركية والقضائية إلى جانب ممثلي البنوك وشركات الصرافة "
                 "والقطاع التجاري.")),
    ("does_not_establish_en", (None, " The news release of its first meeting does not say who established the committee or "
                                     "under which decision.")),
    ("does_not_establish_ar", (None, " ولا يذكر البيان الصحفي عن اجتماعها الأول الجهة التي أنشأتها ولا القرار الذي أُنشئت بموجبه.")),
    ("source_scope", (None, " CBY-Aden news release on the committee's first meeting (it states no establishing decision and "
                            "no mandate).")),
])
YSC015_STATES = [d("17 July 2025", NEWS832, "cby-ye.com/news/832, dated 2025-07-17: 'صباح اليوم الخميس الموافق 17 يوليو 2025م'")]


def add_states(cur, extra):
    lst = json.loads(cur) if isinstance(cur, str) and cur.strip() else []
    have = {(x.get("t"), x.get("k")) for x in lst}
    for e in extra:
        if (e["t"], e["k"]) not in have:
            lst.append(e)
            have.add((e["t"], e["k"]))
    return json.dumps(lst, ensure_ascii=False, separators=(",", ":"))


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    t15 = Table(s, "15_SOURCE_LIBRARY")

    # ---------------------------------------------------------------- merges (canonical record carries the addresses)
    for dup, m in MERGES.items():
        can = m["into"]
        if t15.get(dup, "primary_url") != m["urls"][0] or json.loads(t15.get(dup, "additional_urls")) != m["urls"][1:]:
            raise TxError(f"{F}: {dup} does not carry the addresses expected")
        cur = t15.get(can, "additional_urls")
        if cur:
            raise TxError(f"{F}: {can} already has additional URLs")
        t15.set(F + ":MERGE", can, "additional_urls", json.dumps(m["urls"]), cur)
        t15.set(F + ":MERGE", can, "display_title", m["title"][1], m["title"][0])
        t15.set(F + ":MERGE", can, "display_title_ar", nfc(m["title_ar"][1]), m["title_ar"][0])
        if m["date"][0] != m["date"][1]:
            t15.set(F + ":MERGE", can, "document_date", m["date"][1], m["date"][0])
        t15.set(F + ":MERGE", can, "issuer", m["issuer"], t15.get(can, "issuer"))
        t15.set(F + ":MERGE", can, "hosting_platform", m["hosting"], t15.get(can, "hosting_platform"))
        use = t15.get(can, "datasets_or_use")
        if "DS-K04-PUBLICATION-BENCHMARK" not in use:
            t15.set(F + ":MERGE", can, "datasets_or_use", use + ",DS-K04-PUBLICATION-BENCHMARK", use)
        note = ("RETIRED (close-out CLOSE-6B, 11 October 2026): a second record of " + can + ", " + m["same"] + ". Its two "
                "addresses are now additional URLs of " + can + ", and this record feeds no record. Its publisher line, "
                "which named DeepRoot Consulting as publisher, misstated the paper, which the Sana'a Center Economic Unit wrote and the Sana'a Center "
                "for Strategic Studies prepared with DeepRoot Consulting and CARPO. Addresses: " + "; ".join(m["urls"]))
        t15.set(F + ":MERGE", dup, "non_public_locator_note", note, t15.get(dup, "non_public_locator_note"))
        t15.set(F + ":MERGE", dup, "primary_url", None, m["urls"][0])
        t15.set(F + ":MERGE", dup, "additional_urls", None, t15.get(dup, "additional_urls"))
        t15.set(F + ":MERGE", dup, "public_card_state", "LOCATOR_ONLY", t15.get(dup, "public_card_state"))
        t15.set(F + ":MERGE", dup, "publisher", SC, t15.get(dup, "publisher"))
        t15.set(F + ":MERGE", dup, "publisher_ar", SC_AR, t15.get(dup, "publisher_ar"))

    # ---------------------------------------------------------------- completions
    if t15.get(C12, "public_card_state") != "LOCATOR_ONLY":
        raise TxError(f"{F}: {C12} is not the bare card expected")
    for k, v in C12_CARD.items():
        t15.set(F + ":COMPLETE", C12, k, nfc(v), t15.get(C12, k))
    if t15.get(LIQ, "primary_url") != "https://search.mandumah.com/Record/932295":
        raise TxError(f"{F}: {LIQ} locator is not the one expected")
    for k, v in LIQ_CARD.items():
        t15.set(F + ":COMPLETE", LIQ, k, nfc(v), t15.get(LIQ, k))
    t32 = Table(s, "32_QUAL_LITERATURE", header_row=5)
    for k, (old, new) in LIQ_32.items():
        t32.set(F + ":COMPLETE", "LIT-YEM-2016-001", k, nfc(new), old)
    for k, (old, new) in HIST_CARD.items():
        t15.set(F + ":COMPLETE", HIST, k, nfc(new), old)
    for k, (old, new) in AMB_TEXT.items():
        cur = t15.get(AMB, k)
        if not isinstance(cur, str) or cur.count(old) != 1:
            raise TxError(f"{F}: {AMB} {k} does not hold {old[:40]!r} once")
        t15.set(F + ":COMPLETE", AMB, k, cur.replace(old, nfc(new)), cur)
    t15.set(F + ":COMPLETE", AMB, "issuer", AMB_ISSUER[1], AMB_ISSUER[0])
    t15.set(F + ":CR-11", CCY, "issuer", CCY_ISSUER[1], CCY_ISSUER[0])

    # ---------------------------------------------------------------- withheld (XIDIAN precedent)
    for sid, why in WITHHOLD.items():
        url, more = t15.get(sid, "primary_url"), t15.get(sid, "additional_urls")
        if not url:
            raise TxError(f"{F}: {sid} has no primary URL to withhold")
        addrs = [url] + (json.loads(more) if more else [])
        t15.set(F + ":WITHHOLD", sid, "non_public_locator_note", NP + why + " Address" + ("es" if len(addrs) > 1 else "") +
                ": " + "; ".join(addrs), t15.get(sid, "non_public_locator_note"))
        t15.set(F + ":WITHHOLD", sid, "primary_url", None, url)
        if more:
            t15.set(F + ":WITHHOLD", sid, "additional_urls", None, more)
        t15.set(F + ":WITHHOLD", sid, "public_card_state", "LOCATOR_ONLY", t15.get(sid, "public_card_state"))

    # ---------------------------------------------------------------- /data/: what each instrument requires, and the scope line
    for sid, (w, w_ar, n, n_ar) in CARDS.items():
        for k, v in (("why_it_matters", w), ("why_it_matters_ar", w_ar), ("does_not_establish", n), ("does_not_establish_ar", n_ar)):
            if t15.get(sid, k):
                raise TxError(f"{F}: {sid} already has {k}")
            t15.set(F + ":REG", sid, k, nfc(v), None)
    ui_id, (old_en, new_en), (old_ar, new_ar) = SCOPE
    _, ui = ui_block_end(s)
    cur_en, cur_ar = s.ed.get_value(S04, ui[ui_id], 2), s.ed.get_value(S04, ui[ui_id], 3)
    if cur_en.count(old_en) != 1 or cur_ar.count(old_ar) != 1:
        raise TxError(f"{F}: {ui_id} is not the text expected")
    set_ui(s, F + ":REG", ui_id, cur_en.replace(old_en, new_en), cur_ar.replace(old_ar, nfc(new_ar)), cur_en, cur_ar)

    # ---------------------------------------------------------------- 04: the Sana'a search alias, after alias 045
    g04 = s.grid(S04)
    ids = {r[0]: i for i, r in enumerate(g04, 1) if r and isinstance(r[0], str) and r[0].startswith("SEARCH-ALIAS-")}
    if ALIAS["alias_id"] in ids or max(ids) != "SEARCH-ALIAS-045" or any(c not in (None, "") for c in g04[ids["SEARCH-ALIAS-045"]]):
        raise TxError(f"{F}: the search-alias block is not the one expected")
    at = ids["SEARCH-ALIAS-045"] + 1
    s.ed.insert_rows(S04, at, [{j: nfc(v) for j, v in enumerate(ALIAS.values(), 1)}])
    s.ledger.append(OrderedDict([("finding", F + ":SEARCH"), ("sheet", S04), ("row", at), ("col", None), ("field", ALIAS["alias_id"]),
                                 ("old", None), ("new", json.dumps(ALIAS, ensure_ascii=False))]))

    # ---------------------------------------------------------------- 15: the CBY-Aden news item behind YSC-015
    if NEWS832 in t15.rows:
        raise TxError(f"{F}: 15 already holds {NEWS832}")
    h15 = t15.head
    last15 = max(t15.rows.values())
    s.ed.insert_rows("15_SOURCE_LIBRARY", last15 + 1, [{h15.index(k) + 1: nfc(v) for k, v in NEWS832_ROW.items() if v is not None}])
    for k, v in NEWS832_ROW.items():
        if v is not None:
            s.ledger.append(OrderedDict([("finding", F + ":EVENTS"), ("sheet", "15_SOURCE_LIBRARY"), ("row", last15 + 1),
                                         ("col", h15.index(k) + 1), ("field", f"{NEWS832}.{k}"), ("old", None), ("new", v)]))

    # ---------------------------------------------------------------- 14: two dated events; YSC-012 and YSC-015 extended
    for eid, (row, after) in EVENTS.items():
        t14 = Table(s, "14_SYSTEM_CHRONOLOGY")
        if eid in t14.rows:
            raise TxError(f"{F}: 14 already holds {eid}")
        h14 = t14.head
        pos = t14.rows[after] + 1
        row = nfc(row)
        s.ed.insert_rows("14_SYSTEM_CHRONOLOGY", pos, [{h14.index(k) + 1: v for k, v in row.items() if v is not None}])
        for k, v in row.items():
            if v is not None:
                s.ledger.append(OrderedDict([("finding", F + ":EVENTS"), ("sheet", "14_SYSTEM_CHRONOLOGY"), ("row", pos),
                                             ("col", h14.index(k) + 1), ("field", f"{eid}.{k}"), ("old", None), ("new", v)]))
    t14 = Table(s, "14_SYSTEM_CHRONOLOGY")
    for eid, spec, srcs, states, scope in (("YSC-012", YSC012, YSC012_SOURCES, YSC012_STATES, YSC012_SCOPE),
                                           ("YSC-015", YSC015, [NEWS832], YSC015_STATES, None)):
        for k, (old, new) in spec.items():
            cur = t14.get(eid, k)
            if old is None:                       # appended
                t14.set(F + ":EVENTS", eid, k, cur + nfc(new), cur)
            else:
                if cur != old:
                    raise TxError(f"{F}: {eid} {k} is not the text expected")
                t14.set(F + ":EVENTS", eid, k, nfc(new), cur)
        cur = t14.get(eid, "source_ids")
        t14.set(F + ":EVENTS", eid, "source_ids", cur + "".join(" | " + x for x in srcs), cur)
        if scope:
            cur = t14.get(eid, "source_scope")
            t14.set(F + ":EVENTS", eid, "source_scope", cur + scope, cur)
        cur = t14.get(eid, "value_states")
        t14.set(F + ":EVENTS", eid, "value_states", add_states(cur, states), cur)

    counts = refresh_self_counts(s, F + ":OWN-10")
    rep = s.save(out, ledger, OrderedDict([
        ("transaction", F),
        ("summary", "Stage A addendum item 3: two duplicate Sana'a Center records merged and retired; CBY-Sana'a Circular "
                    "No. 12, the University of Aden article, the Quarterly Bulletin, the AMB and CCY cards completed; six "
                    "sources withheld; nine regulatory cards and one CBY statistical report carry what they require and do not establish; two dated events "
                    "added and two extended."),
        ("self_counts", counts)]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
