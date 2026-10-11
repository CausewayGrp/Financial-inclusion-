# -*- coding: utf-8 -*-
"""Close-out transaction CLOSE-4: regulation and chronology (brief v5 W3d, Appendix C). English and Arabic change together.

  python3 close_4.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Every instrument was read in the original on cby-ye.com, the Arabic scans as page images (audit/close_out/w0/A3_cby.md,
section 5, and the CLOSE-4 reading of 10 October 2026 recorded in PROGRESS: Decision No. 19 of 2024, Periodic Circular
No. 1 of 2024, Decision No. 20 of 2024, the December 2022 bank balance-sheet report, the statement of the Office of the
UN Special Envoy for Yemen of 23 July 2024 in English and Arabic, and CBY-Aden's notice of 6 August 2024). File names on
cby-ye.com carry the upload time, not the instrument's date: every date below is the one printed on the instrument, or
a posting date where it says so.

- Instruments (rules) go to 31_REFORMS_REGULATION (reform events) and, as sources with a regulatory document label, to
  the regulatory group of /data/. Rule is not implementation, and implementation is not operation: each entry says
  what the instrument requires, never that it is applied.
- Dated events go to 14_SYSTEM_CHRONOLOGY, in date order, with neutral wording on the two authorities: the Buna
  connection, the first phase of the national switch, the 2024 bank measures and the agreement the UN Special Envoy's
  office announced (the parties' text is Arabic; the UN's English is an informal translation, so neither edition says
  "all"), the decision to relocate the Deposit Insurance Institution's head office, the 2025 enforcement wave (counts
  only, no names, posting dates) and the launch of the defaulters registry (launch is not coverage).
- The law on the Deposit Insurance Institution is held as a source labelled Law, issued by the Republic of Yemen, in the
  copy CBY-Aden hosts. It is not in the regulatory group of CBY-Aden instruments, whose scope line said the evidence
  base holds no law; that line now says where the one law is.
- The chronology is kept once, on /finance/ (folded); /data/ carries a one-line pointer to it.
- CWR-006 explains that a licence conversion can be a reclassification, and binds the two Board decisions it cites.
- The nine files of the CBY-Aden licensing and regulation page not held at the 3 October cut-off are now held
  (audit/FINAL_CURRENTNESS_CUTOFF.md, appended).
- Not found, recorded as FRONTIER in PROGRESS and the register: Governor's Decisions Nos. 8, 12 and 16 of 2026, the
  February 2026 exchange-rate pricing decision and the text of Decision No. 4 of 1991 (cited, not published); news items
  709, 722 and 731 of July 2024 returned errors.
"""
import json, os, sys, unicodedata
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from close_lib import Session, Table, TxError, refresh_self_counts, insert_ui_rows, set_ui  # noqa: E402
from rc_lib import S04, ui_block_end  # noqa: E402  (close_lib puts audit/release_candidate on the path)

F = "CLOSE-4"
TODAY = "2026-10-10"
CBY, CBY_AR = "Central Bank of Yemen — Aden", "البنك المركزي اليمني – عدن"
N = "https://cby-ye.com/news/"
FL = "https://cby-ye.com/files/"


def src_row(sid, url, more, title, title_ar, label, label_ar, date, pub=CBY, pub_ar=CBY_AR, use="DS-REFORM-EVENTS"):
    return OrderedDict([("source_id", sid), ("primary_url", url), ("additional_urls", json.dumps(more) if more else None),
                        ("datasets_or_use", use), ("row_count", 0), ("display_title", title), ("display_title_ar", title_ar),
                        ("publisher", pub), ("publisher_ar", pub_ar), ("public_card_state", "CITATION_CARD"),
                        ("rights_state", "NOT_ASSESSED"), ("retrieval_date", TODAY), ("document_label", label),
                        ("document_label_ar", label_ar), ("document_date", date)])


REG, REG_AR = "Regulatory decision", "قرار تنظيمي"
CIR, CIR_AR = "Circular or instruction", "تعميم أو تعليمات"
RGL, RGL_AR = "Regulation", "لائحة تنظيمية"
ENF, ENF_AR = "Enforcement decision", "قرار إنفاذ"
NEWS, NEWS_AR = "News release", "بيان صحفي"
STAT, STAT_AR = "Statistical release", "إصدار إحصائي"
LAW, LAW_AR = "Law", "قانون"
ROY, ROY_AR = "Republic of Yemen", "الجمهورية اليمنية"
UN_SE = "Office of the Special Envoy of the Secretary-General for Yemen"
UN_SE_AR = "مكتب المبعوث الخاص للأمين العام للأمم المتحدة لليمن"
OSESGY = "https://osesgy.unmissions.org/en/speeches-and-statements/statement-office-un-special-envoy-yemen"
OSESGY_AR = "https://osesgy.unmissions.org/ar/speeches-and-statements/statement-office-un-special-envoy-yemen"
OSESGY_NODE = "https://osesgy.unmissions.org/en/node/15786"   # the page's own shortlink
WAVE_NEWS = ["836", "837", "838", "839", "840", "841", "843", "846", "847", "848"]

SOURCES = [
    src_row("SRC-CBY-DEC-07-2026", FL + "69dcac86e3520.pdf", None,
            "Governor's Decision No. 7 of 2026 on interest rates on deposits and credit at banks (9 April 2026; ref. "
            "220/CBY/2026)",
            "قرار محافظ البنك المركزي اليمني رقم (7) لسنة 2026 بشأن أسعار الفائدة على الودائع والائتمان لدى البنوك (9 أبريل "
            "2026؛ المرجع 220/CBY/2026)", REG, REG_AR, "2026-04-09"),
    src_row("SRC-CBY-EKYC-2023", FL + "65806fe2b3757.pdf", None,
            "Instructions regulating electronic know-your-customer procedures (9 November 2023; ref. 840/CBY/2023)",
            "تعليمات تنظيم إجراءات اعرف عميلك إلكترونيًا (9 نوفمبر 2023؛ المرجع 840/CBY/2023)", CIR, CIR_AR, "2023-11-09"),
    src_row("SRC-CBY-CIRC-02-2025", FL + "68dcd80cd12b9.pdf", None,
            "Periodic Circular No. 2 of 2025 to banks and exchange companies and establishments, supplementing the "
            "anti-money laundering and counter-terrorist financing circulars (24 September 2025)",
            "منشور دوري رقم (2) لسنة 2025 إلى البنوك وشركات ومنشآت الصرافة، ملحق بمنشورات مكافحة غسل الأموال وتمويل الإرهاب (24 "
            "سبتمبر 2025)", CIR, CIR_AR, "2025-09-24"),
    src_row("SRC-CBY-CIRC-03-2025", FL + "690e0e07d4981.pdf", None,
            "Periodic Circular No. 3 of 2025 on risk-management instructions for banks (2 November 2025)",
            "منشور دوري رقم (3) لسنة 2025 بشأن تعليمات إدارة المخاطر في البنوك (2 نوفمبر 2025)", CIR, CIR_AR, "2025-11-02"),
    src_row("SRC-CBY-CIRC-04-2025", FL + "690e0e39ce5d9.pdf", None,
            "Periodic Circular No. 4 of 2025: instructions on applying enhanced due diligence procedures and screening "
            "against international sanctions lists (2 November 2025)",
            "منشور دوري رقم (4) لسنة 2025: تعليمات تطبيق إجراءات العناية الواجبة المعززة والتحقق من قوائم العقوبات الدولية (2 "
            "نوفمبر 2025)", CIR, CIR_AR, "2025-11-02"),
    src_row("SRC-CBY-CIRC-01-2026", FL + "6aaa38b226baa.pdf", None,
            "Circular No. 1 of 2026 prohibiting dealings in virtual assets or cryptocurrencies and with their service "
            "providers (15 September 2026; ref. CBY/L/258/2026)",
            "منشور رقم (1) لسنة 2026 بشأن حظر التعامل بالأصول الافتراضية أو العملات المشفرة ومع مقدمي خدماتها (15 سبتمبر 2026؛ "
            "المرجع CBY/L/258/2026)", CIR, CIR_AR, "2026-09-15"),
    src_row("SRC-CBY-DEC-19-2024", FL + "6653499a7181b.pdf", None,
            "Governor's Decision No. 19 of 2024 regulating external money-transfer activity through international "
            "money-transfer companies (23 May 2024; ref. 289/CBY/2024)",
            "قرار محافظ البنك المركزي رقم (19) لسنة 2024 بشأن تنظيم مزاولة نشاط التحويلات الخارجية عبر شركات الحوالات الدولية (23 "
            "مايو 2024؛ المرجع 289/CBY/2024)", REG, REG_AR, "2024-05-23"),
    src_row("SRC-CBY-CIRC-01-2024", FL + "663c8ad5cafdc.pdf", None,
            "Periodic Circular No. 1 of 2024 on the instructions and controls for shipping surplus foreign-currency "
            "banknotes abroad (29 April 2024; ref. 235/CBY/2024)",
            "منشور دوري رقم (1) لسنة 2024 بشأن التعليمات والضوابط المنظمة لعمليات ترحيل فوائض أوراق النقد الأجنبي إلى الخارج (29 "
            "أبريل 2024؛ المرجع 235/CBY/2024)", CIR, CIR_AR, "2024-04-29"),
    src_row("SRC-CBY-BANKS-BS-2022", FL + "64bada99e708e.pdf", None,
            "Developments in the consolidated balance sheet of banks, to December 2022 (no issue date printed)",
            "تطورات الميزانية المجمعة للبنوك حتى ديسمبر 2022 (لا تحمل تاريخ إصدار مطبوعًا)", STAT, STAT_AR, None,
            use="RESOURCE_LIBRARY_ONLY__CONTEXT"),
    src_row("SRC-CBY-BOARD-2022-2-11", FL + "623ad771a78d7.pdf", None,
            "Board of Directors' Decision No. (2022/2/11) amending the regulation of the Microfinance Banks Law (21 March "
            "2022; ref. 176/CBY/2022)",
            "قرار مجلس إدارة البنك المركزي اليمني رقم (2022/2/11) بتعديل اللائحة التنفيذية لقانون بنوك التمويل الأصغر (21 مارس "
            "2022؛ المرجع 176/CBY/2022)", REG, REG_AR, "2022-03-21"),
    src_row("SRC-CBY-BOARD-2023-11-3", FL + "659aa2ee5852b.pdf", None,
            "Board of Directors' Decision No. (2023/11/3) raising the capital of microfinance banks to YER 15 billion (31 "
            "December 2023; ref. 957/CBY/2023)",
            "قرار مجلس الإدارة رقم (2023/11/3) بشأن رفع رؤوس أموال بنوك التمويل الأصغر إلى 15 مليار ريال يمني (31 ديسمبر 2023؛ "
            "المرجع 957/CBY/2023)", REG, REG_AR, "2023-12-31"),
    src_row("SRC-CBY-CRI-149", "https://cby-ye.com/publications/149", None,
            "Credit-risk information exchange system and Form No. 6 (CBY-Aden publications page; cites Governor's Decision No. "
            "4 of 1991)",
            "نظام تبادل معلومات مخاطر الائتمان ومتطلبات الاستمارة رقم (6) (صفحة منشورات البنك المركزي اليمني – عدن؛ يشير إلى قرار "
            "المحافظ رقم (4) لسنة 1991)", RGL, RGL_AR, None),
    src_row("SRC-CBY-CRI-150", "https://cby-ye.com/publications/150", None,
            "Credit-risk information: enquiry before granting credit (CBY-Aden publications page)",
            "معلومات مخاطر الائتمان: الاستعلام قبل منح الائتمان (صفحة منشورات البنك المركزي اليمني – عدن)", CIR, CIR_AR, None),
    src_row("SRC-CBY-NEWS-963", N + "963", None,
            "CBY-Aden launches the defaulters registry system (5 August 2026)",
            "البنك المركزي اليمني – عدن يدشّن نظام سجل المتعثرين (5 أغسطس 2026)", NEWS, NEWS_AR, "2026-08-05"),
    src_row("SRC-CBY-NEWS-645", N + "645", None,
            "CBY-Aden launches the first phase of the national switch, connecting seven banks (7 March 2024)",
            "البنك المركزي اليمني – عدن يدشّن المرحلة الأولى من العمل بنظام المقسم الوطني بربط سبعة بنوك (7 مارس 2024)", NEWS,
            NEWS_AR, "2024-03-07"),
    src_row("SRC-CBY-NEWS-656", N + "656", None,
            "CBY-Aden Board of Directors reviews the first phase of the national switch and the unified money-transfer "
            "network (28 March 2024)",
            "مجلس إدارة البنك المركزي اليمني – عدن يستعرض المرحلة الأولى من المقسم الوطني والشبكة الموحدة للحوالات (28 مارس "
            "2024)", NEWS, NEWS_AR, "2024-03-28"),
    src_row("SRC-CBY-NEWS-579", N + "579", None,
            "CBY-Aden joins the Buna regional payment platform (14 September 2023)",
            "انضمام البنك المركزي اليمني – عدن إلى منصة بُنى الإقليمية للمدفوعات (14 سبتمبر 2023)", NEWS, NEWS_AR, "2023-09-14"),
    src_row("SRC-CBY-ENF-2025-JUL-AUG", N + "834", [N + x for x in WAVE_NEWS],
            "Governor's Decisions Nos. 7 to 17 of 2025 on licence suspensions and withdrawals (posted 23 July to 6 August "
            "2025)",
            "قرارات المحافظ من رقم (7) إلى رقم (17) لسنة 2025 بشأن إيقاف تراخيص وسحبها (نُشرت من 23 يوليو إلى 6 أغسطس 2025)",
            ENF, ENF_AR, "2025-07-23"),
    src_row("SRC-CBY-DEC-06-2025", FL + "687c9970b82d9.pdf", [N + "833"],
            "Governor's Decision No. 6 of 2025: relocation of the head office of the Deposit Insurance Institution to Aden "
            "(20 July 2025; ref. 376/CBY/2025)",
            "قرار المحافظ رقم (6) لسنة 2025: نقل المركز الرئيسي لمؤسسة ضمان الودائع إلى عدن (20 يوليو 2025؛ المرجع "
            "376/CBY/2025)", REG, REG_AR, "2025-07-20"),
    src_row("SRC-CBY-DEC-20-2024", FL + "665878ad66e09.pdf", [N + "691"],
            "Governor's Decision No. 20 of 2024 on ceasing dealings with a number of banks (30 May 2024; ref. 294/CBY/2024)",
            "قرار محافظ البنك المركزي رقم (20) لسنة 2024 بشأن إيقاف التعامل مع عدد من البنوك والمصارف (30 مايو 2024؛ المرجع "
            "294/CBY/2024)", ENF, ENF_AR, "2024-05-30"),
    src_row("SRC-CBY-NEWS-724", N + "724", None,
            "CBY-Aden clarification notice on cancelling the recent decisions concerning banks (6 August 2024)",
            "إشعار توضيحي من البنك المركزي اليمني – عدن بشأن إلغاء القرارات الأخيرة بحق البنوك (6 أغسطس 2024)", NEWS, NEWS_AR,
            "2024-08-06"),
    src_row("SRC-UN-OSESGY-2024-07-23", OSESGY, [OSESGY_AR, OSESGY_NODE],
            "Statement by the Office of the UN Special Envoy for Yemen (23 July 2024)",
            "بيان صادر عن مكتب المبعوث الأممي الخاص إلى اليمن (23 يوليو 2024)", NEWS, NEWS_AR, "2024-07-23", pub=UN_SE,
            pub_ar=UN_SE_AR),
]

# ================================================================================================ 31: the instruments (rules)
R = "/reforms/regulation + /data"


def ref(eid, date, actor, event, desc, cls, src_id, route=R):
    url = next(s["primary_url"] for s in SOURCES if s["source_id"] == src_id)
    return OrderedDict([("event_id", eid), ("date", date), ("actor_event_type", actor), ("event", event),
                        ("normalized_description", desc), ("event_class", cls), ("route", route), ("source_url", url)])


INSTRUMENTS = [
    ref("REF-REG-001", "2022-03-21", "CBY-Aden Board decision", "Board Decision (2022/2/11): microfinance banks and exchange",
        "Amends the regulation of Microfinance Banks Law No. 15 of 2009: exchange activity and microfinance activity may not "
        "be combined; an application to establish a microfinance bank is refused where its shareholders own exchange "
        "companies, unless the exchange company converts; earlier approvals must exit exchange activity within one year; "
        "minimum paid-up capital YER 5 billion (Art. 10, 15).", "MFB_LICENSING_RULE", "SRC-CBY-BOARD-2022-2-11"),
    ref("REF-REG-002", "2023-11-09", "CBY-Aden regulatory issuance", "Electronic know-your-customer instructions",
        "Instructions for banks and licensed mobile e-money providers on opening accounts remotely, without the customer "
        "present in person, with reporting requirements that include the average time to open or activate an account. "
        "No effective-date clause was found on the pages read; a requirement is not evidence of use.",
        "CUSTOMER_DUE_DILIGENCE_RULE", "SRC-CBY-EKYC-2023"),
    ref("REF-REG-003", "2023-12-31", "CBY-Aden Board decision", "Board Decision (2023/11/3): microfinance bank capital",
        "Raises the minimum paid-up capital of microfinance banks to YER 15 billion, half of the increase each year from "
        "2024, deadline 31 December 2025; non-compliance can lead to licence withdrawal (Art. 6).", "MFB_CAPITAL_RULE",
        "SRC-CBY-BOARD-2023-11-3"),
    ref("REF-REG-004", "2024-04-29", "CBY-Aden periodic circular",
        "Circular No. 1 of 2024: shipping surplus FX banknotes abroad",
        "Banks wishing to ship surplus foreign-currency banknotes abroad apply to the Governor at least a week ahead; no "
        "answer within five days of the Banking Supervision Sector receiving a complete request, after referral by the "
        "Governor, counts as refusal; one shipment at most USD 25 million or its equivalent, from funds deposited for at "
        "least six months; SWIFT and credit advices within 10 days after shipment.", "FX_BANKNOTE_RULE", "SRC-CBY-CIRC-01-2024"),
    ref("REF-REG-005", "2024-05-23", "CBY-Aden Governor decision", "Decision No. 19 of 2024: external transfers",
        "External transfers only through qualified banks or exchange companies; a CBY-Aden no-objection letter before any "
        "contract with an international money-transfer company or a sub-agent; a sub-agent must hold a valid CBY-Aden "
        "licence, and main agents with existing sub-agencies were to apply within two weeks of the decision to register "
        "them and obtain a no-objection letter; the main agent answers for its sub-agents; incoming transfers paid in the "
        "currency received, converted only at the beneficiary's wish at the market rate; in force from issue.", "CROSS_BORDER_TRANSFER_RULE", "SRC-CBY-DEC-19-2024"),
    ref("REF-REG-006", "2025-07-20", "CBY-Aden Governor decision",
        "Decision No. 6 of 2025: Deposit Insurance Institution head office",
        "Provides for relocating the head office of the Deposit Insurance Institution to Aden, in force from issue; it "
        "does not show that the move was completed. It does not establish the Institution (Law No. 21 of 2008, in the copy "
        "CBY-Aden hosts; the decision's recital cites Law No. 40 of 2008) and does not show that deposit cover operates.",
        "DEPOSIT_INSURANCE_INSTITUTION", "SRC-CBY-DEC-06-2025"),
    ref("REF-REG-007", "2025-09-24", "CBY-Aden periodic circular", "Circular No. 2 of 2025: AML/CFT supplement",
        "Addressed to banks and exchange companies and establishments; supplements the anti-money laundering and "
        "counter-terrorist financing circulars of 2012, 2013, 2014 and 2021.", "AML_CFT_RULE", "SRC-CBY-CIRC-02-2025"),
    ref("REF-REG-008", "2025-11-02", "CBY-Aden periodic circular", "Circular No. 3 of 2025: risk management in banks",
        "Risk-management instructions applying to all banks, prepared with IMF technical support (METAC).", "PRUDENTIAL_RULE",
        "SRC-CBY-CIRC-03-2025"),
    ref("REF-REG-009", "2025-11-02", "CBY-Aden periodic circular",
        "Circular No. 4 of 2025: enhanced due diligence and sanctions screening",
        "Addressed to banks and exchange firms: enhanced due diligence and screening against UN Security Council and OFAC "
        "sanctions lists.", "AML_CFT_RULE", "SRC-CBY-CIRC-04-2025"),
    ref("REF-REG-010", "2026-04-09", "CBY-Aden Governor decision", "Decision No. 7 of 2026: deposit and credit rates",
        "Minimum 18% a year on new rial savings deposits at commercial banks; foreign-currency deposit rates and lending "
        "rates left to banks; Islamic banks exempt; applies to contracts after it takes effect on 12 April 2026.",
        "MONETARY_POLICY_RULE", "SRC-CBY-DEC-07-2026"),
    ref("REF-REG-011", "2026-09-15", "CBY-Aden circular", "Circular No. 1 of 2026: virtual assets",
        "Prohibits banks, exchange firms, payment-service providers and e-wallet operators from dealing in virtual assets "
        "or cryptocurrencies or with their service providers; in force from issue.", "VIRTUAL_ASSETS_RULE",
        "SRC-CBY-CIRC-01-2026"),
    ref("REF-REG-012", "undated (web posting 2021-10-06)", "CBY-Aden regulation (legacy, web-posted)",
        "Credit-risk information exchange and pre-credit enquiry",
        "Commercial and specialised banks report credit exposures from YER 500,000 on Form No. 6 by the 15th of the "
        "following month, and grant no credit before an enquiry to the Credit and Banking Risk Department; the pages cite "
        "Governor's Decision No. 4 of 1991, whose text is not published. Web posting is not an issue date.",
        "CREDIT_INFORMATION_RULE", "SRC-CBY-CRI-149"),
]

# a source CLOSE-4 also needs: the law the Deposit Insurance Institution rests on (A3, CR-20). A law, issued by the state
# and held in the copy CBY-Aden hosts: labelled Law, so it is not in the regulatory group of CBY-Aden instruments.
SOURCES.append(src_row("SRC-CBY-DIL-21-2008", FL + "62c2edbaad8eb.pdf", None,
                       "Law No. 21 of 2008 on the Bank Deposit Insurance Institution (certified copy hosted by CBY-Aden)",
                       "القانون رقم (21) لسنة 2008 بشأن مؤسسة ضمان الودائع المصرفية (نسخة مصدقة يستضيفها البنك المركزي اليمني – عدن)",
                       LAW, LAW_AR, "2008-04-23", pub=ROY, pub_ar=ROY_AR))

# /data/: the regulatory group's scope line said the evidence base holds no law; it now says where the one law is
SCOPE = ("UI-DATA-GROUP-REGULATORY-SCOPE",
         ("All were issued by the Central Bank of Yemen – Aden. The evidence base holds no law as a source document, and "
          "this group holds no instrument issued in Sana'a.",
          "All were issued or posted by the Central Bank of Yemen – Aden; its undated pages on credit-risk information cite "
          "older instructions, the earliest from 1991. This group holds no law and no instrument issued in Sana'a; the one "
          "law the evidence base holds, on the Bank Deposit Insurance Institution, is listed below with the other sources."),
         ("وقد أصدرها جميعًا البنك المركزي اليمني – عدن. ولا تضم قاعدة الأدلة أي قانون بوصفه وثيقة مصدرية، ولا تضم هذه المجموعة "
          "أي وثيقة صادرة في صنعاء.",
          "وقد أصدرها جميعًا أو نشرها البنك المركزي اليمني – عدن؛ وتشير صفحتاه غير المؤرختين عن معلومات مخاطر الائتمان إلى "
          "تعليمات أقدم، أولها من عام 1991. ولا تضم هذه المجموعة أي قانون ولا أي وثيقة صادرة في صنعاء؛ أما القانون الوحيد الذي "
          "تضمه قاعدة الأدلة، وهو قانون مؤسسة ضمان الودائع المصرفية، فمدرج أدناه مع المصادر الأخرى."))


def vs(t, src=None, loc=None, k="v", s="READ"):
    e = OrderedDict([("t", t), ("k", k), ("s", s)])
    if src:
        e["src"], e["loc"] = src, loc + "; read 10 October 2026"
    return e


def d(t, src, loc):
    return vs(t, src, loc, k="d")


# ================================================================================================ 14: dated events
def event(eid, period, period_ar, cls, fact, fact_ar, srcs, scope, impl, impl_ar, rel, rel_ar, dne, dne_ar, routes, note, states):
    return OrderedDict([("event_id", eid), ("period_en", period), ("event_class", cls), ("fact_en", fact), ("fact_ar", fact_ar),
                        ("source_ids", " | ".join(srcs)), ("source_scope", scope), ("system_implication_en", impl),
                        ("system_implication_ar", impl_ar), ("fi_relevance_en", rel), ("fi_relevance_ar", rel_ar),
                        ("does_not_establish_en", dne), ("does_not_establish_ar", dne_ar), ("relationship_type", "CONTEXT"),
                        ("linked_routes", routes), ("interpretation_note", note), ("period_ar", period_ar),
                        ("value_states", json.dumps(states, ensure_ascii=False, separators=(",", ":")))])


EVENTS = OrderedDict([   # event -> (event, the event it follows in the sheet)
    ("YSC-025", (event(
        "YSC-025", "14 September 2023", "14 سبتمبر 2023", "REGIONAL_PAYMENT_CONNECTION",
        "CBY-Aden announced that it had joined the Buna regional payment platform, describing itself as the seventh Arab "
        "central bank to join.",
        "أعلن البنك المركزي اليمني – عدن انضمامه إلى منصة بُنى الإقليمية للمدفوعات، مشيرًا إلى أنه سابع بنك مركزي عربي ينضم "
        "إليها.",
        ["SRC-CBY-NEWS-579"], "CBY-Aden news release on its connection to a regional platform; no transaction data.",
        "A cross-border payment rail became available to the central bank in Aden; who uses it, and for which transfers, is "
        "not reported.",
        "أصبح مسار دفع عابر للحدود متاحًا للبنك المركزي في عدن؛ ولم يُفصَح عمّن يستخدمه ولا عن التحويلات التي تمر عبره.",
        "Cross-border rails matter for remittance channels and their cost, but a connection is not a channel that households "
        "use.",
        "لمسارات الدفع العابرة للحدود أهمية بالنسبة إلى قنوات الحوالات وتكلفتها، لكن الربط ليس قناة تستخدمها الأسر.",
        "Joining the platform does not establish transactions through it, lower remittance costs or wider access.",
        "لا يثبت الانضمام إلى المنصة وجود معاملات عبرها ولا انخفاض تكلفة الحوالات ولا اتساع الوصول.",
        "/payments | /remittances | /reforms", "Connection is not operation, and operation is not use.",
        [d("14 September 2023", "SRC-CBY-NEWS-579", "cby-ye.com/news/579, dated 14 September 2023")]), "YSC-011")),
    ("YSC-026", (event(
        "YSC-026", "7 and 28 March 2024", "7 و28 مارس 2024", "NATIONAL_SWITCH_PHASE",
        "CBY-Aden launched the first phase of the national switch on 7 March 2024, connecting seven banks, and said official "
        "operation would follow once all banks were connected; on 28 March 2024 its Board of Directors reviewed the first "
        "phase (ATMs, POS and e-wallets) and the launch of the unified money-transfer network.",
        "دشّن البنك المركزي اليمني – عدن في 7 مارس 2024 المرحلة الأولى من العمل بنظام المقسم الوطني بربط سبعة بنوك، وذكر أن "
        "التشغيل الرسمي سيبدأ بعد ربط جميع البنوك؛ وفي 28 مارس 2024 استعرض مجلس إدارته المرحلة الأولى (أجهزة الصراف الآلي ونقاط "
        "البيع والمحافظ الإلكترونية) وإطلاق الشبكة الموحدة للحوالات.",
        ["SRC-CBY-NEWS-645", "SRC-CBY-NEWS-656"], "CBY-Aden news releases on a launch and a Board review; no transaction data.",
        "As CBY-Aden reported it, the first phase connected part of the banking system; the bank named the connection of all "
        "banks as the condition for official operation.",
        "بحسب ما أفاد به البنك المركزي اليمني – عدن، ربطت المرحلة الأولى جزءًا من الجهاز المصرفي؛ وجعل البنك ربط جميع البنوك "
        "شرطًا للتشغيل الرسمي.",
        "An interoperable switch is a precondition for card, POS and e-wallet payments between different providers, not a "
        "measure of their use.",
        "المقسم القابل للتشغيل البيني شرط مسبق لمدفوعات البطاقات ونقاط البيع والمحافظ الإلكترونية بين مقدمي الخدمات المختلفين، "
        "وليس مقياسًا لاستخدامها.",
        "The launch does not establish that all banks connected, that the switch operates officially, or that transactions "
        "moved through it.",
        "لا يثبت التدشين أن جميع البنوك ارتبطت، ولا أن المقسم يعمل رسميًا، ولا أن معاملات مرّت عبره.",
        "/payments | /reforms", "Launch is not operation; a first phase is not the system.",
        [d("7 March 2024", "SRC-CBY-NEWS-645", "cby-ye.com/news/645 (posted 9 March 2024): launch on Thursday 7 March, first "
                                                "phase connecting seven banks"),
         d("28 March 2024", "SRC-CBY-NEWS-656", "cby-ye.com/news/656, Board meeting 2 of 2024, 28 March 2024")]), "YSC-025")),
    ("YSC-027", (event(
        "YSC-027", "30 May to 6 August 2024", "من 30 مايو إلى 6 أغسطس 2024", "BANKING_MEASURES_AND_CANCELLATION",
        "On 30 May 2024 CBY-Aden's Governor's Decision No. 20 of 2024 ordered a halt to dealings with a number of banks from "
        "2 June 2024, and directed those banks to keep serving the public and meeting their obligations to customers until "
        "further notice. On 23 July 2024 the Office of the UN Special Envoy for Yemen announced that the Government of Yemen "
        "and Ansar Allah had agreed to cancel the recent decisions and procedures against banks by both sides and to "
        "refrain in future from any similar decisions or procedures; on 6 August 2024 CBY-Aden posted that it had cancelled "
        "the recent decisions concerning banks, in implementation of those commitments.",
        "في 30 مايو 2024 قضى قرار محافظ البنك المركزي اليمني – عدن رقم (20) لسنة 2024 بإيقاف التعامل مع عدد من البنوك والمصارف "
        "اعتبارًا من 2 يونيو 2024، وألزم تلك البنوك بالاستمرار في تقديم خدماتها للجمهور والوفاء بالتزاماتها تجاه عملائها حتى "
        "إشعار آخر. وفي 23 يوليو 2024 أعلن مكتب المبعوث الأممي الخاص إلى اليمن أن الحكومة اليمنية وجماعة أنصار الله اتفقا على "
        "إلغاء القرارات والإجراءات الأخيرة ضد البنوك من الجانبين والتوقف مستقبلًا عن أي قرارات أو إجراءات مماثلة؛ وفي 6 أغسطس "
        "2024 نشر البنك المركزي اليمني – عدن أنه ألغى القرارات الأخيرة بحق البنوك تنفيذًا لتلك الالتزامات.",
        ["SRC-CBY-DEC-20-2024", "SRC-UN-OSESGY-2024-07-23", "SRC-CBY-NEWS-724"],
        "A CBY-Aden decision and notice, and the statement of the Office of the UN Special Envoy; the parties' own measures "
        "are named only as the statement names them.",
        "Under an agreement the Office of the UN Special Envoy announced, both sides committed to cancel the recent "
        "decisions and procedures against banks and to refrain in future from any similar decisions or procedures; CBY-Aden "
        "posted that it had cancelled the recent decisions concerning banks. The sources held do not report whether or when "
        "the other side's measures were cancelled.",
        "بموجب اتفاق أعلنه مكتب المبعوث الأممي الخاص إلى اليمن، التزم الجانبان بإلغاء القرارات والإجراءات الأخيرة ضد البنوك "
        "وبالتوقف مستقبلًا عن أي قرارات أو إجراءات مماثلة؛ ونشر البنك المركزي اليمني – عدن أنه ألغى القرارات الأخيرة بحق البنوك. "
        "ولا تُبلغ المصادر التي تضمها قاعدة الأدلة عمّا إذا كانت إجراءات الجانب الآخر قد أُلغيت ولا عن موعد ذلك.",
        "Measures on banks, and their cancellation, bear on whether customers in either area can use banks' services; the "
        "sources do not report effects on customers.",
        "تتصل الإجراءات المتخذة بحق البنوك وإلغاؤها بقدرة العملاء في أيٍّ من المنطقتين على استخدام خدمات البنوك؛ ولا تُبلغ "
        "المصادر عن آثارها على العملاء.",
        "The decision, the agreement and the cancellation notice do not establish whether each side cancelled its "
        "measures, which ones or when, what each measure required in practice, which banks or customers were affected, or "
        "any later effect on access to services.",
        "لا يثبت القرار ولا الاتفاق ولا إشعار الإلغاء ما إذا كان كل جانب قد ألغى إجراءاته، ولا أيّها ولا موعد إلغائها، ولا ما "
        "اقتضاه كل إجراء عمليًا، ولا البنوك أو العملاء الذين تأثروا، ولا أي أثر لاحق على الوصول إلى الخدمات.",
        "/finance | /providers | /access | /reforms",
        "Neutral wording: the event follows the UN statement's own words for the parties and their measures. The parties' "
        "text is Arabic; the UN's English is an informal translation and adds 'all', which neither edition of this event "
        "carries.",
        [d("30 May 2024", "SRC-CBY-DEC-20-2024", "cby-ye.com/files/665878ad66e09.pdf p.1, ref. 294/CBY/2024, dated 30/5/2024"),
         d("2 June 2024", "SRC-CBY-DEC-20-2024", "cby-ye.com/files/665878ad66e09.pdf p.2, Art. 3: in force from 2024/6/2"),
         d("23 July 2024", "SRC-UN-OSESGY-2024-07-23", "osesgy.unmissions.org statement dated 23 July 2024, item 1"),
         d("6 August 2024", "SRC-CBY-NEWS-724", "cby-ye.com/news/724, clarification notice of 6 August 2024"),
         vs("20", s="TRIVIAL")]), "YSC-024")),
    ("YSC-028", (event(
        "YSC-028", "20 July 2025", "20 يوليو 2025", "DEPOSIT_INSURANCE_INSTITUTION",
        "Governor's Decision No. 6 of 2025 provided for relocating the head office of the Deposit Insurance Institution to "
        "Aden, in force from issue. The law on the Institution is Law No. 21 of 2008 in the copy CBY-Aden hosts; the "
        "decision's recital cites Law No. 40 of 2008.",
        "نصّ قرار المحافظ رقم (6) لسنة 2025 على نقل المركز الرئيسي لمؤسسة ضمان الودائع إلى عدن، ويُعمل به من تاريخ صدوره. "
        "والقانون الخاص بالمؤسسة هو القانون رقم (21) لسنة 2008 وفق النسخة التي يستضيفها البنك المركزي اليمني – عدن؛ وتشير ديباجة "
        "القرار إلى القانون رقم (40) لسنة 2008.",
        ["SRC-CBY-DEC-06-2025", "SRC-CBY-DIL-21-2008"],
        "A CBY-Aden decision and the law copy it hosts; the two cite different law numbers.",
        "The decision provides for the head office to move; it does not show that the move was completed, and a relocation "
        "is not the start of deposit cover.",
        "ينصّ القرار على نقل المركز الرئيسي، ولا يُظهر أن النقل اكتمل؛ والنقل ليس بدءًا لتغطية الودائع.",
        "Deposit insurance matters for trust in deposits, but no source here reports cover, premiums or payouts.",
        "لضمان الودائع أهمية في الثقة بالودائع، لكن لا يُبلغ أي مصدر هنا عن التغطية أو الأقساط أو التعويضات.",
        "The decision does not establish that deposit cover operates, which deposits are covered or that depositors are "
        "protected.",
        "لا يثبت القرار أن تغطية الودائع تعمل، ولا الودائع المشمولة، ولا أن المودعين محميون.",
        "/finance | /providers | /reforms", "Relocation is not establishment, and establishment is not operating cover.",
        [d("20 July 2025", "SRC-CBY-DEC-06-2025", "cby-ye.com/files/687c9970b82d9.pdf p.1, ref. 376/CBY/2025, signed 20 July "
                                                  "2025"),
         vs("6", s="TRIVIAL"),
         vs("21", "SRC-CBY-DIL-21-2008", "cby-ye.com/files/62c2edbaad8eb.pdf p.1, «قانون رقم (٢١) لسنة ٢٠٠٨م»"),
         vs("40", "SRC-CBY-DEC-06-2025", "cby-ye.com/files/687c9970b82d9.pdf p.1, recital «القانون رقم (40) لسنة 2008»")]),
        "YSC-015")),
    ("YSC-029", (event(
        "YSC-029", "23 July to 6 August 2025", "من 23 يوليو إلى 6 أغسطس 2025", "EXCHANGE_SECTOR_ENFORCEMENT",
        "Between 23 July and 6 August 2025 CBY-Aden posted in its news 11 Governor's decisions (Nos. 7 to 17 of 2025) "
        "covering 51 licences: 44 suspensions and 7 withdrawals of exchange companies and establishments and their branches, "
        "including one remittance agent, on the basis of field-inspection reports of the Banking Supervision Sector.",
        "في الفترة من 23 يوليو إلى 6 أغسطس 2025 نشر البنك المركزي اليمني – عدن في أخباره 11 قرارًا للمحافظ (من رقم (7) إلى رقم "
        "(17) لسنة 2025) شملت 51 ترخيصًا: إيقاف 44 ترخيصًا وسحب 7 تراخيص لشركات ومنشآت صرافة وفروعها، من بينها وكيل حوالة "
        "واحد، استنادًا إلى تقارير النزول الميداني لقطاع الرقابة على البنوك.",
        ["SRC-CBY-ENF-2025-JUL-AUG"], "CBY-Aden decisions as posted in its news; counts only, no names.",
        "The decisions changed the status of 51 exchange-sector licences; later reinstatements, if any, are not covered here.",
        "غيّرت القرارات حالة 51 ترخيصًا في قطاع الصرافة؛ ولا يغطي هذا الحدث أي إعادة لاحقة للتراخيص إن وُجدت.",
        "Exchange companies handle transfers and remittances, so licence actions bear on where people can send or collect "
        "money; the decisions report licences, not customers or volumes.",
        "تتولى شركات الصرافة الحوالات والتحويلات، فتتصل إجراءات التراخيص بالأماكن التي يستطيع الناس فيها إرسال المال أو "
        "استلامه؛ والقرارات تُبلغ عن تراخيص لا عن عملاء أو أحجام.",
        "The counts do not establish which areas lost service, for how long, how many customers were affected, or any effect "
        "on transfer costs; names are deliberately not recorded here.",
        "لا تثبت هذه الأعداد المناطق التي فقدت الخدمة ولا مدة ذلك ولا عدد العملاء المتأثرين ولا أي أثر على تكلفة التحويلات؛ "
        "ولا تُسجَّل الأسماء هنا، وذلك عن قصد.",
        "/providers | /remittances | /access | /reforms", "Licence status is not service availability; counts only.",
        [d("6 August 2025", "SRC-CBY-ENF-2025-JUL-AUG", "cby-ye.com/news/848, posting date of the last of the eleven decisions"),
         vs("11", "SRC-CBY-ENF-2025-JUL-AUG", "cby-ye.com/news/834 to /news/848: Governor's Decisions Nos. 7 to 17 of 2025"),
         vs("51", "SRC-CBY-ENF-2025-JUL-AUG", "sum of the licences named in Decisions Nos. 7 to 17 of 2025 (44 + 7)"),
         vs("44", "SRC-CBY-ENF-2025-JUL-AUG", "suspensions: Decisions 7 (13), 8 (5), 9 (10), 10 (2), 11 (7, one a remittance "
                                              "agent), 12 (2), 15 (4), 17 (1)"),
         vs("7", "SRC-CBY-ENF-2025-JUL-AUG", "withdrawals: Decisions 13 (4 company branches), 14 (1), 16 (2)"),
         vs("17", s="TRIVIAL")]), "YSC-016")),
    ("YSC-030", (event(
        "YSC-030", "5 August 2026", "5 أغسطس 2026", "CREDIT_INFORMATION_INFRASTRUCTURE",
        "CBY-Aden launched a defaulters registry system: a digital platform for exchanging data on defaulting customers among "
        "the banks operating in Yemen, whose success, it said, depends on all banks supplying accurate data.",
        "دشّن البنك المركزي اليمني – عدن نظام سجل المتعثرين: منصة رقمية لتبادل البيانات عن العملاء المتعثرين بين البنوك العاملة "
        "في اليمن، وذكر أن نجاحه مرهون بتزويد جميع البنوك له ببيانات دقيقة.",
        ["SRC-CBY-NEWS-963", "SRC-CBY-CRI-149", "SRC-CBY-CRI-150"],
        "CBY-Aden news release on a launch, beside the credit-information rules the bank publishes.",
        "The registry adds a platform to the credit-information rules CBY-Aden publishes (exposure reporting on Form No. 6 "
        "and an enquiry before lending).",
        "يضيف السجل منصة إلى قواعد معلومات الائتمان التي ينشرها البنك المركزي اليمني – عدن (الإبلاغ عن التعرضات الائتمانية على "
        "الاستمارة رقم (6) والاستعلام قبل منح الائتمان).",
        "A defaulters registry holds data on defaulting customers; any effect on access to credit depends on the data "
        "being complete and on lenders using them.",
        "يضم سجل المتعثرين بيانات العملاء المتعثرين؛ وأي أثر على الوصول إلى الائتمان مشروط بأن تكون البيانات كاملة وأن "
        "يستخدمها المقرضون.",
        "The launch does not establish coverage, data completeness, lender use or any effect on access to credit.",
        "لا يثبت التدشين التغطية ولا اكتمال البيانات ولا استخدام المقرضين لها ولا أي أثر على الوصول إلى الائتمان.",
        "/firms | /finance | /reforms", "Launch is not coverage.",
        [d("5 August 2026", "SRC-CBY-NEWS-963", "cby-ye.com/news/963, dated 5 August 2026"), vs("6", s="TRIVIAL")]),
        "YSC-023")),
])

# ================================================================================================ /data/: a pointer to the one chronology
DATA_S9 = (("The chronology brings together documented events across Yemen’s macro-financial and financial-inclusion system.",
            "The dated chronology of Yemen’s macro-financial and financial-inclusion system is kept in one place, on the Banks "
            "and microfinance page, where each event keeps its date, its source and what it does not establish."),
           ("تجمع السلسلة الزمنية أحداثًا موثقة عبر النظام الاقتصادي والمالي ومنظومة الشمول المالي في اليمن.",
            "تُحفظ السلسلة الزمنية المؤرخة للنظام الاقتصادي والمالي ومنظومة الشمول المالي في اليمن في موضع واحد، في صفحة «البنوك "
            "والتمويل الأصغر»، حيث يحتفظ كل حدث بتاريخه ومصدره وما لا يثبته."))
UI = [("UI-DATA-CHRONOLOGY-OPEN", "Open the dated events on the Banks and microfinance page",
       "افتح الأحداث المؤرخة في صفحة «البنوك والتمويل الأصغر»",
       "Close-out W3d. The /data/ pointer to the one chronology on /finance/ (#chronology).")]

# ================================================================================================ CWR-006: a licence conversion can be reclassification
CWR006 = "/readings/microfinance-structural-divergence/"
CWR006_S6 = ("The rules on microfinance banks make the point concrete. A 2022 decision of the Board of Directors of CBY-Aden "
             "barred combining exchange and microfinance activity, and let the owners of an exchange company apply for a "
             "microfinance bank only by converting that company; a 2023 decision raised the minimum capital of microfinance "
             "banks, with a deadline at the end of 2025. A microfinance bank licensed through such a conversion can be an "
             "existing business reclassified, not new inclusion.",
             "وتجسّد القواعد الخاصة ببنوك التمويل الأصغر هذه النقطة. فقد منع قرار لمجلس إدارة البنك المركزي اليمني – عدن صدر عام "
             "2022 الجمع بين نشاط الصرافة ونشاط التمويل الأصغر، ولم يُجز لمالكي شركة صرافة التقدم بطلب إنشاء بنك تمويل أصغر إلا "
             "بتحويل تلك الشركة؛ ورفع قرار صدر عام 2023 الحد الأدنى لرأس مال بنوك التمويل الأصغر، على أن يكتمل ذلك بنهاية 2025. "
             "وقد يكون بنك التمويل الأصغر المرخّص عبر مثل هذا التحويل نشاطًا قائمًا أُعيد تصنيفه، لا شمولًا جديدًا.")
CWR006_SOURCES = ["SRC-CBY-BOARD-2022-2-11", "SRC-CBY-BOARD-2023-11-3"]   # the two decisions s6 cites, with their locators

# ================================================================================================ 34: the credit-information passport gets its locators
PASSPORT = "EP-CBY-CREDIT-INFO-SPINE-K04"
PASSPORT_METHOD = ("Official CBY web publications + dated launch event",
                   "Official CBY-Aden web publications (cby-ye.com/publications/149 and /150; SRC-CBY-CRI-149, SRC-CBY-CRI-150) "
                   "+ dated launch event (cby-ye.com/news/963, 5 August 2026; SRC-CBY-NEWS-963)")


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    fs, fi, fe, fd = F + ":SOURCES", F + ":INSTRUMENTS", F + ":EVENTS", F + ":DEDUP"

    # ---------------------------------------------------------------- 15: the instruments and event sources
    t15 = Table(s, "15_SOURCE_LIBRARY")
    held = {str(x) for r in s.grid("15_SOURCE_LIBRARY")[4:] if r for x in r[1:3] if x}
    for row in SOURCES:
        if row["source_id"] in t15.rows or row["primary_url"] in held:
            raise TxError(f"{fs}: {row['source_id']} or its locator is already in the library")
    h15 = t15.head
    last15 = max(t15.rows.values())
    s.ed.insert_rows("15_SOURCE_LIBRARY", last15 + 1,
                     [{h15.index(k) + 1: v for k, v in row.items() if v is not None} for row in SOURCES])
    for j, row in enumerate(SOURCES):
        for k, v in row.items():
            if v is not None:
                s.ledger.append(OrderedDict([("finding", fs), ("sheet", "15_SOURCE_LIBRARY"), ("row", last15 + 1 + j),
                                             ("col", h15.index(k) + 1), ("field", f"{row['source_id']}.{k}"),
                                             ("old", None), ("new", v)]))

    # ---------------------------------------------------------------- 04: the regulatory group's scope line (the one law)
    ui_id, (old_en, new_en), (old_ar, new_ar) = SCOPE
    _, ui = ui_block_end(s)
    if ui_id not in ui:
        raise TxError(f"{fs}: 04 has no {ui_id}")
    cur_en, cur_ar = s.ed.get_value(S04, ui[ui_id], 2), s.ed.get_value(S04, ui[ui_id], 3)
    if not isinstance(cur_en, str) or not isinstance(cur_ar, str) or cur_en.count(old_en) != 1 or cur_ar.count(old_ar) != 1:
        raise TxError(f"{fs}: {ui_id} is not the text expected")
    set_ui(s, fs, ui_id, cur_en.replace(old_en, new_en), cur_ar.replace(old_ar, new_ar), cur_en, cur_ar)

    # ---------------------------------------------------------------- 31: the instruments, after the last reform event
    g31 = s.grid("31_REFORMS_REGULATION")
    hi = next(i for i, r in enumerate(g31) if r and r[0] == "event_id")
    h31 = [str(x) if x is not None else None for x in g31[hi]]
    ev_rows = [i for i, r in enumerate(g31[hi + 1:], start=hi + 1) if r and str(r[0] or "").startswith("REF-")]
    if any(str(g31[i][0]).startswith("REF-REG-") for i in ev_rows):
        raise TxError(f"{fi}: 31 already holds REF-REG rows")
    if ev_rows != list(range(hi + 1, hi + 1 + len(ev_rows))):
        raise TxError(f"{fi}: the reform events are not one contiguous block")
    at = ev_rows[-1] + 2                                     # 1-based row after the last reform event
    s.ed.insert_rows("31_REFORMS_REGULATION", at, [{h31.index(k) + 1: v for k, v in r.items()} for r in INSTRUMENTS])
    for j, r in enumerate(INSTRUMENTS):
        for k, v in r.items():
            s.ledger.append(OrderedDict([("finding", fi), ("sheet", "31_REFORMS_REGULATION"), ("row", at + j),
                                         ("col", h31.index(k) + 1), ("field", f"{r['event_id']}.{k}"), ("old", None),
                                         ("new", v)]))

    # ---------------------------------------------------------------- 14: dated events, each after the event it follows
    for eid, (row, after) in EVENTS.items():                   # in order; the table is re-read after every insert
        t14 = Table(s, "14_SYSTEM_CHRONOLOGY")
        if eid in t14.rows:
            raise TxError(f"{fe}: 14 already holds {eid}")
        h14 = t14.head
        pos = t14.rows[after] + 1
        s.ed.insert_rows("14_SYSTEM_CHRONOLOGY", pos, [{h14.index(k) + 1: v for k, v in row.items() if v is not None}])
        for k, v in row.items():
            if v is not None:
                s.ledger.append(OrderedDict([("finding", fe), ("sheet", "14_SYSTEM_CHRONOLOGY"), ("row", pos),
                                             ("col", h14.index(k) + 1), ("field", f"{eid}.{k}"), ("old", None), ("new", v)]))

    # ---------------------------------------------------------------- /data/: the one-line pointer; 04: its link
    for lang, (start, new) in (("en", DATA_S9[0]), ("ar", DATA_S9[1])):
        s.rewrite_section(fd, "/data/", 9, lang, "body", new, start)
    insert_ui_rows(s, fd, UI)

    # ---------------------------------------------------------------- CWR-006 s6, its two sources, the credit passport
    for lang, add in (("en", CWR006_S6[0]), ("ar", CWR006_S6[1])):
        row = s.section_row(CWR006, 6, lang)
        cur = s.ed.get_value("03_PAGE_SECTIONS", row, {"en": 5, "ar": 7}[lang])
        if not isinstance(cur, str) or add in cur:
            raise TxError(f"{fi}: CWR-006 s6 body_{lang} is not the text expected")
        s.set(fi, "03_PAGE_SECTIONS", row, {"en": 5, "ar": 7}[lang], cur.rstrip() + "\n" + add, cur,
              f"{CWR006}#s6.body_{lang}")
    t08 = Table(s, "08_READINGS")
    old_b = t08.get("CWR-006", "source_bindings")
    bound = json.loads(old_b)
    if any(x in bound for x in CWR006_SOURCES):
        raise TxError(f"{fi}: CWR-006 already binds a Board decision")
    t08.set(fi, "CWR-006", "source_bindings", json.dumps(bound + CWR006_SOURCES, separators=(",", ":")), old_b)
    t34 = Table(s, "34_EVIDENCE_PASSPORTS")
    t34.set(fi, PASSPORT, "method", PASSPORT_METHOD[1], PASSPORT_METHOD[0])
    t34.set(fi, PASSPORT, "publisher_ar", CBY_AR, None)

    counts = refresh_self_counts(s, F + ":OWN-10")
    rep = s.save(out, ledger, OrderedDict([
        ("transaction", F),
        ("summary", "W3d: 23 sources (CBY-Aden instruments, decisions and news; the UN Special Envoy's statement of 23 July "
                    "2024; the deposit-insurance law copy, labelled Law, with the /data/ regulatory scope line saying where "
                    "it is); 12 instruments in 31; 6 dated events in 14; the /data/ chronology becomes a pointer to "
                    "/finance/; CWR-006 on licence conversion, binding the two Board decisions it cites; passport locators."),
        ("self_counts", counts)]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


def _nfc(o):
    if isinstance(o, str):
        return unicodedata.normalize("NFC", o)
    if isinstance(o, tuple):
        return tuple(_nfc(x) for x in o)
    if isinstance(o, list):
        return [_nfc(x) for x in o]
    if isinstance(o, dict):
        return type(o)((_nfc(k), _nfc(v)) for k, v in o.items())
    return o


for _name in [n for n in list(globals()) if n.isupper() and not n.startswith("_")]:
    globals()[_name] = _nfc(globals()[_name])


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
