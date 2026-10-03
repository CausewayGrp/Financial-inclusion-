# -*- coding: utf-8 -*-
"""Release-candidate transaction RC-7 — Part A items 3 and 6 on Path A (audit/release_candidate/INSTRUCTIONS.md, Part A
items 3 and 6; the owner's update of 3 October 2026: the originals are readable, "replace the Path B wording only where
the original supports it").

  python3 rc_7_path_a.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Item 3 — IMF Country Report No. 26/80 (Republic of Yemen: 2025 Article IV Consultation; staff report dated 20 November
2025; published April 2026), read in full from the IMF eLibrary on 3 October 2026. Every element of the four events is
confirmed or corrected against the report, with its paragraph locator in the ledger:
  YSC-008  confirmed (staff report ¶6): the flag is removed; the fact is unchanged.
  YSC-014  values confirmed against ¶13; corrected: the values are the staff report's text, not "the IMF's banking data",
           and the end value is 2½, not "about 2.5"; the report's own FSI table (Table 5) gives different values and
           dates and neither states a unit — said with the event in place of the flag.
  YSC-015  confirmed (¶8, ¶39); corrected to the report's wording: "FX use", "enhance", "into the formal banking sector".
  YSC-017  confirmed (¶12); corrected: the report gives US$350 million, not "about" US$350 million.
The Methodology lead sentence keeps its Path B wording, which stays true and precise (no event is now flagged).

Item 6 — Yemen Financial Sector Diagnostics (World Bank, 5 April 2024), Annex III, Table 8, p. 146, read in the original
PDF on 3 October 2026 (page text and the rendered page image). All sixteen values match the table; rows 9–16 are bound
to VIS-FIRM-CONSTRAINTS with eight new governed labels in the source's own item wording (the contract change is staged
by rc_7_stage_inputs.py), and the partial-list frame note is unbound. Two truth fixes from the same reading:
  * the survey is named as the source names it, "the 2022 Yemen Enterprise Survey" (the World Bank's Enterprise Survey
    of 2022); "custom" is not the source's word and is removed everywhere it was written, in both languages;
  * the method cited Figure 108 and Table 8 together; Figure 108 shows only the six most named challenges and gives a
    different share for transport or road blockades, so the method now cites Table 8 and says so.
  * the Arabic title of the report is written one way, as the source library already writes it.
An independent bilingual review before commit (Arabic first, English, and every fact against the originals) found nothing
blocking; its ten should-fix findings and four of its optional ones are applied here (ledger: independent_review).
"""
import json, os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from rc_lib import Session, Table, TxError, insert_ui_rows, set_ui  # noqa: E402
sys.path.insert(0, os.path.join(HERE, "..", "..", "scripts"))
from projection.master_reader import Workbook  # noqa: E402
import tempfile  # noqa: E402


def snapshot(s):
    """The session's edited Master, read once (Session.grid saves the workbook on every call)."""
    tmp = tempfile.NamedTemporaryFile(suffix=".xlsx", delete=False, dir=s.work)
    tmp.close()
    s.ed.save(tmp.name)
    wb = Workbook(tmp.name)
    for name in wb.sheet_names:
        wb.grid(name)   # parse every sheet before the file goes
    os.remove(tmp.name)
    return wb

CH = "14_SYSTEM_CHRONOLOGY"
NOTE_EN = "This event has not yet been checked against the original source document."
NOTE_AR = "لم يُراجَع هذا الحدث بعدُ مقابل وثيقة المصدر الأصلية."

# ---------------------------------------------------------------- item 3: the four IMF-attributed chronology events
EVENTS = OrderedDict([
    ("YSC-008", dict(
        locator="IMF CR 26/80, staff report ¶6 (printed p. 6): 'Following the October 2022 attacks on oil export facilities in "
                "Hadramout and Shabwa governorates, oil exports have been suspended since January 2023.' ¶4: revenues cut by "
                "almost half. The suspected October–November 2022 date for the suspension is not in the report.",
        fact=None, note=(None, None))),
    ("YSC-014", dict(
        locator="IMF CR 26/80, staff report ¶13 (printed p. 9): 'a decline in the capital to assets ratio from about 5 in 2022 "
                "to 2½ in April 2025. The liquid assets to short term liability ratio have sharply declined, from 148 in 2022 "
                "to 69 in April 2025'. Table 5 (printed p. 31; source 'Yemeni Authorities; IMF Staff Calculations'; no unit "
                "line; no April 2025 column): Dec-22 147.2 and 4.9; Aug-25 73.6 and 3.8. ¶2: data relate to areas under the "
                "authorities' control.",
        fact=("In the IMF's banking data for areas under the internationally recognized government, the liquid-assets to "
              "short-term-liabilities ratio fell from 148 in 2022 to 69 in April 2025, while the capital-to-assets ratio fell "
              "from about 5 to about 2.5.",
              "According to the IMF staff report, which focuses on areas under the internationally recognized government, the "
              "banking sector's ratio of liquid assets to short-term liabilities fell from 148 in 2022 to 69 in April 2025, while "
              "its capital-to-assets ratio fell from about 5 in 2022 to 2.5 in April 2025.",
              "في بيانات صندوق النقد الدولي عن القطاع المصرفي في المناطق الخاضعة للحكومة المعترف بها دوليًا، انخفضت نسبة الأصول "
              "السائلة إلى الالتزامات قصيرة الأجل من 148 في 2022 إلى 69 في أبريل 2025، كما تراجعت نسبة رأس المال إلى الأصول من "
              "نحو 5 إلى نحو 2.5.",
              "بحسب تقرير خبراء صندوق النقد الدولي، وهو تقرير يركّز على المناطق الخاضعة للحكومة المعترف بها دوليًا، انخفضت في "
              "القطاع المصرفي نسبة الأصول السائلة إلى الالتزامات قصيرة الأجل من 148 في 2022 إلى 69 في أبريل 2025، كما تراجعت نسبة "
              "رأس المال إلى الأصول من نحو 5 في 2022 إلى 2.5 في أبريل 2025."),
        note=("These values are from the text of the staff report (paragraph 13). "
              "The report's own table of financial soundness indicators (Table 5) gives different values and dates for the "
              "same two ratios. Neither the text nor the table states a unit. The report says its data relate to areas under "
              "the authorities' control unless otherwise stated (paragraph 2), but its statistical annex says the banks' "
              "balance-sheet data cover the whole of Yemen (Annex IV); it does not state the coverage of these two ratios.",
              "هذه القيم من متن تقرير الخبراء (الفقرة 13). أما جدول "
              "مؤشرات السلامة المالية في التقرير نفسه (الجدول 5) فيورد قيمًا وتواريخ مختلفة للنسبتين نفسيهما. ولا يذكر المتن ولا "
              "الجدول وحدة القياس. ويذكر التقرير أن بياناته تخص المناطق الخاضعة لسيطرة السلطات ما لم يُذكر خلاف ذلك (الفقرة 2)، "
              "غير أن ملحقه الإحصائي يذكر أن بيانات الميزانيات العمومية للبنوك تغطي اليمن كله (الملحق الرابع)، ولا يحدد نطاق هاتين "
              "النسبتين."))),
    ("YSC-015", dict(
        locator="IMF CR 26/80, staff report ¶8 (printed p. 7): 'the authorities created the National Committee for the "
                "Regulation and Financing of Imports (NCRFI) to prioritize FX use for essential imports, enhance import "
                "transparency, and channel FX into the formal banking sector.' ¶39 (printed p. 21): 'the government "
                "established the NCRFI in July 2025.'",
        fact=("The internationally recognized government established the National Committee for the Regulation and Financing "
              "of Imports to prioritize FX for essential imports, improve import transparency and channel FX through the formal "
              "banking sector.",
              "The internationally recognized government established the National Committee for the Regulation and Financing "
              "of Imports to prioritize FX use for essential imports, enhance import transparency and channel FX into the "
              "formal banking sector.",
              "أنشأت الحكومة المعترف بها دوليًا اللجنة الوطنية لتنظيم وتمويل الواردات لإعطاء الأولوية للنقد الأجنبي للواردات "
              "الأساسية، وتعزيز شفافية الاستيراد، وتوجيه النقد الأجنبي عبر القطاع المصرفي الرسمي.",
              "أنشأت الحكومة المعترف بها دوليًا اللجنة الوطنية لتنظيم وتمويل الواردات لإعطاء الأولوية في استخدام النقد الأجنبي "
              "للواردات الأساسية، وتعزيز شفافية الاستيراد، وتوجيه النقد الأجنبي إلى القطاع المصرفي الرسمي."),
        note=(None, None))),
    ("YSC-017", dict(
        locator="IMF CR 26/80, staff report ¶12 (printed p. 9): 'operational FX reserves as of September 2025 remain low at "
                "USD$350million, covering about a month worth of imports.' (Table 1 gives gross reserves, a different "
                "measure; the DSA dates US$0.35 billion to June 2025.)",
        fact=("The IMF reports operational foreign-exchange reserves of about US$350 million in September 2025, covering roughly "
              "one month of imports.",
              "The IMF reports operational foreign-exchange reserves of US$350 million in September 2025, covering about one "
              "month of imports.",
              "يفيد صندوق النقد بأن الاحتياطيات التشغيلية من النقد الأجنبي بلغت نحو 350 مليون دولار في سبتمبر 2025، بما يغطي "
              "قرابة شهر واحد من الواردات.",
              "يفيد صندوق النقد بأن الاحتياطيات التشغيلية من النقد الأجنبي بلغت 350 مليون دولار في سبتمبر 2025، بما يغطي نحو "
              "شهر واحد من الواردات."),
        note=("This value and its date are from the text of the staff report (paragraph 12). The debt sustainability analysis "
              "published in the same country report gives reserves of the same amount as of June 2025.",
              "هذه القيمة وتاريخها من متن تقرير الخبراء (الفقرة 12). أما تحليل القدرة على تحمّل الدين المنشور في التقرير القُطري "
              "نفسه فيورد احتياطيات بالمبلغ نفسه في يونيو 2025."))),
])

# ---------------------------------------------------------------- item 6: rows 9–16 of Table 8, in the source's wording
NEW_LABELS = [
    ("UI-VIS-CAT-FIRM-CH-LABOUR", "Labour regulations", "لوائح العمل"),
    ("UI-VIS-CAT-FIRM-CH-CUSTOMS", "Customs and trade regulation", "الجمارك ولوائح التجارة"),
    ("UI-VIS-CAT-FIRM-CH-CORRUPTION", "Corruption", "الفساد"),
    ("UI-VIS-CAT-FIRM-CH-LAND", "Access to land", "الحصول على الأراضي"),
    ("UI-VIS-CAT-FIRM-CH-LICENSING", "Business licensing and permits", "تراخيص الأعمال والتصاريح"),
    ("UI-VIS-CAT-FIRM-CH-WORKFORCE", "Inadequately educated workers", "العمالة التي تفتقر إلى التعليم الكافي"),
    ("UI-VIS-CAT-FIRM-CH-COURTS", "Courts", "المحاكم"),
    ("UI-VIS-CAT-FIRM-CH-CRIME", "Crime, theft and disorder", "الجريمة والسرقة والاضطرابات"),
]
LABEL_RULE = ("RC-7 (Part A item 6, Path A). VIS-FIRM-CONSTRAINTS bar and table label for a row of Table 8, Annex III, p. 146 "
              "of Yemen Financial Sector Diagnostics (World Bank, 2024), in the source's own item wording, checked against "
              "the original on 3 October 2026.")

# The method of VIS-FIRM-CONSTRAINTS and of the records that cite the same page: Table 8 is the tabulation; Figure 108
# shows the six most named challenges and does not match the table for one of them.
FIG_EN = ("The shares are the source's own tabulation in Annex III, Figure 108 ('Challenges in Business Environment') and "
          "Table 8 ('List of Challenges to the Establishment'), p. 146.")
FIG_EN_NEW = ("The shares are the source's own tabulation in Annex III, Table 8 ('List of Challenges to the Establishment'), "
              "p. 146. On the same page, the source's chart of the six most often named challenges (Figure 108, 'Challenges in "
              "Business Environment') gives a different share for transport or road blockades; the table's value is used. "
              "Elsewhere the source tabulates the same survey differently: its chart of the top constraints cited by formal "
              "firms (Figure 83, p. 111) puts access to finance level with political instability, behind electricity, and its "
              "text on p. 145 says access to finance 'remained on top of the main challenges'. Neither is used here.")
FIG_AR = ("والنسب كما بوّبها المصدر نفسه في الملحق الثالث: الشكل 108 («تحديات بيئة الأعمال») والجدول 8 («قائمة التحديات "
          "التي تواجه المنشأة»)، ص 146.")
FIG_AR_NEW = ("والنسب كما بوّبها المصدر نفسه في الملحق الثالث، الجدول 8 («قائمة التحديات التي تواجه المنشأة»)، ص 146. "
              "وفي الصفحة نفسها، يورد الرسم البياني الذي يعرض فيه المصدر التحديات الستة الأكثر ذكرًا (الشكل 108، «تحديات بيئة "
              "الأعمال») نسبةً مختلفة لصعوبات النقل أو إغلاق الطرق، والمعتمد هنا قيمة الجدول. ويعرض المصدر في موضع آخر جدولة "
              "مختلفة للمسح نفسه: فرسمه البياني لأبرز القيود التي ذكرتها المنشآت الرسمية (الشكل 83، ص 111) يضع الوصول إلى "
              "التمويل في مرتبة واحدة مع عدم الاستقرار السياسي بعد الكهرباء، ويقول نصه في ص 145 إن الوصول إلى التمويل «ظل في "
              "صدارة التحديات الرئيسية». ولا يُعتمد هنا أيٌّ منهما.")

# The survey's name as the source gives it, and the report's Arabic title as the source library writes it. Ordered
# longest first; every rule must apply at least once, and each application is guarded by the cell's exact text.
RENAME = [
    ("A World Bank custom enterprise survey of formal firms in seven governorates (September 2022), reported in",
     "The formal-firm sample of the World Bank's 2022 Yemen Enterprise Survey, conducted in seven governorates (September 2022) and reported in"),
    ("for the 2022 World Bank custom enterprise survey (September 2022)",
     "for the World Bank's 2022 Yemen Enterprise Survey (September 2022)"),
    ("reported by a World Bank custom enterprise survey", "reported by the World Bank's 2022 Yemen Enterprise Survey"),
    ("World Bank custom enterprise survey, September 2022", "World Bank Yemen Enterprise Survey, September 2022"),   # one "2022", as the Arabic
    ("World Bank 2022 custom enterprise survey", "World Bank 2022 Yemen Enterprise Survey"),
    ("2022 custom enterprise survey", "2022 Yemen Enterprise Survey"),
    ("in a 2022 custom survey covering seven selected governorates", "in the 2022 Yemen Enterprise Survey, which covered seven selected governorates"),
    ("formal firms in a 2022 custom survey of seven governorates", "formal firms in the 2022 Yemen Enterprise Survey of seven governorates"),
    ("not directly comparable to 2022 custom survey including micro firms", "not directly comparable to the 2022 Yemen Enterprise Survey, which includes micro firms"),
    ("beyond the seven-governorate custom survey", "beyond the seven governorates of the 2022 Yemen Enterprise Survey"),
    ("2022 custom survey", "2022 Yemen Enterprise Survey"),
    ("Custom enterprise survey", "Enterprise survey (formal and informal samples, seven governorates); tabulations as reported in "
                                 "Yemen Financial Sector Diagnostics (2024), Annex III"),
    # O2 — the two internal cells the first pass missed
    ("Custom 2022 sample includes micro firms under 5 employees and seven selected governorates",
     "The 2022 Yemen Enterprise Survey's formal sample includes micro firms under 5 employees and covers seven selected governorates"),
    ("Seven selected governorates; custom sample; not national prevalence.", "Seven selected governorates; survey-specific sample; not national prevalence."),
    ("لمسح المنشآت المخصص الذي أجراه البنك الدولي عام 2022 (سبتمبر 2022)", "لمسح البنك الدولي للمنشآت في اليمن لعام 2022 (سبتمبر 2022)"),
    ("مسح المنشآت في اليمن لعام 2022 الذي أجراه البنك الدولي", "مسح البنك الدولي للمنشآت في اليمن لعام 2022"),
    ("في مسح المنشآت المخصص الذي شمل سبع محافظات عام 2022", "في مسح المنشآت في اليمن لعام 2022، وهو مسح شمل سبع محافظات"),
    ("في المسح المخصص الذي شمل سبع محافظات عام 2022", "في مسح المنشآت في اليمن لعام 2022، وهو مسح شمل سبع محافظات"),
    ("التي شملها المسح المخصص لعام 2022", "التي شملها مسح المنشآت في اليمن لعام 2022"),
    ("مسح مخصص للمنشآت الرسمية أجراه البنك الدولي في سبع محافظات (سبتمبر 2022)، ونُشرت نتائجه في «التشخيص المالي لليمن (2024)»",
     "عينة المنشآت الرسمية في مسح البنك الدولي للمنشآت في اليمن لعام 2022، وهو مسح أُجري في سبع محافظات (سبتمبر 2022) ونُشرت نتائجه في «تشخيص القطاع المالي في اليمن (2024)»"),
    ("في مسح مخصص شمل سبع محافظات عام 2022", "في مسح المنشآت في اليمن لعام 2022، وهو مسح شمل سبع محافظات"),
    ("في مسح مخصص أُجري عام 2022 وشمل سبع محافظات مختارة", "في مسح المنشآت في اليمن لعام 2022، وهو مسح شمل سبع محافظات مختارة"),
    ("كما أورده مسح مخصص للمنشآت أجراه البنك الدولي", "كما أورده مسح البنك الدولي للمنشآت في اليمن لعام 2022"),
    ("مسح مخصص للمنشآت أجراه البنك الدولي في سبتمبر 2022 في سبع محافظات", "مسح البنك الدولي للمنشآت في اليمن، سبتمبر 2022، في سبع محافظات"),
    # the RC-6 reviewer's note: without "custom", the boundary names the standard surveys it is not comparable with
    ("They follow the source's own item wording and are not comparable with the standard Enterprise Survey 'biggest obstacle' indicator.",
     "They follow the source's own item wording and can count more than one challenge per firm, so they are not comparable with the "
     "'biggest obstacle' indicator of the World Bank's standard Enterprise Surveys."),
    ("وهي تتبع صياغة البنود كما وردت في المصدر، ولا تُقارن بمؤشر «أكبر عائق» في مسوح المنشآت المعيارية للبنك الدولي.",
     "وهي تتبع صياغة البنود كما وردت في المصدر، وقد تحتسب أكثر من تحدٍّ للمنشأة الواحدة، ولذلك لا تُقارن بمؤشر «أكبر عائق» في "
     "المسوح المعيارية للمنشآت التي يجريها البنك الدولي."),
    # F8 (workflow review): the Reading's boundary uses the same wording as the record's
    ("it is not the standard Enterprise Survey \u201cbiggest obstacle\u201d indicator",
     "it is not the \u201cbiggest obstacle\u201d indicator of the World Bank\u2019s standard Enterprise Surveys"),
    ("وليست مؤشر «أكبر عائق» المعياري في مسوح المنشآت", "وليست مؤشر «أكبر عائق» في المسوح المعيارية للمنشآت التي يجريها البنك الدولي"),
    # RC7-AR-06: one Arabic name for the survey, on the source card too
    ("ويتضمن ملحق مسح المنشآت اليمنية لعام 2022", "ويتضمن ملحقًا عن مسح المنشآت في اليمن لعام 2022"),
    # RC7-AR-10: MA-004 names the survey and its formal-firm scope
    ("A 2022 survey of formal firms in seven governorates and programme evidence",
     "The 2022 Yemen Enterprise Survey (formal firms in seven governorates) and programme evidence"),
    ("يقدم مسح المنشآت الرسمية الذي شمل سبع محافظات عام 2022 وأدلة", "يقدم مسح المنشآت في اليمن لعام 2022 (المنشآت الرسمية في سبع محافظات) وأدلة"),
    # S7 — the summary and text alternative cover all sixteen bars
    ("18% named siege and 17% practices of informal competitors.",
     "18% named siege and 17% practices of informal competitors, and each of the other eight challenges listed was named by 15% "
     "or fewer, down to 0% for crime, theft and disorder."),
    ("فيما ذكرت 18% الحصار و17% ممارسات المنافسين غير الرسميين.",
     "فيما ذكرت 18% الحصار و17% ممارسات المنافسين غير الرسميين، وذكرت 15% أو أقل كلًّا من التحديات الثمانية الأخرى المدرجة، "
     "وصولًا إلى 0% للجريمة والسرقة والاضطرابات."),
    ("«التشخيص المالي لليمن (2024)»", "«تشخيص القطاع المالي في اليمن (2024)»"),
]
LEFTOVER = ("مسح المنشآت اليمنية", "custom enterprise survey", "Custom enterprise survey", "custom survey", "custom sample", "Custom 2022", "المسح المخصص", "المنشآت المخصص", "مسح مخصص", "التشخيص المالي لليمن")   # «التقديرات المخصصة» (Findex custom estimates) is another thing


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    notes = OrderedDict()
    # item 3
    t = Table(s, CH)
    for eid, e in EVENTS.items():
        for lang, (old_note, new_note) in (("en", (NOTE_EN, e["note"][0])), ("ar", (NOTE_AR, e["note"][1]))):
            t.set("RC-7:item3", eid, f"verification_note_{lang}", new_note, old_note)
        if e["fact"]:
            old_en, new_en, old_ar, new_ar = e["fact"]
            t.set("RC-7:item3", eid, "fact_en", new_en, old_en)
            t.set("RC-7:item3", eid, "fact_ar", new_ar, old_ar)
    notes["item_3"] = OrderedDict([("path", "A — IMF Country Report No. 26/80 read in full on the IMF eLibrary, 3 October 2026 "
                                             "(www.imf.org refuses automated clients at its CDN; the eLibrary is the IMF's own publication platform)"),
                                   ("events", OrderedDict((k, v["locator"]) for k, v in EVENTS.items())),
                                   ("methodology_lead", "kept in its Path B wording: it stays true and precise, and no event is now flagged")])
    # item 6: labels, method, names
    insert_ui_rows(s, "RC-7:item6", [(k, en, ar, LABEL_RULE) for k, en, ar in NEW_LABELS])
    hits = OrderedDict((r[0], 0) for r in RENAME)
    fig = 0
    wb = snapshot(s)   # one read of the edited state (after the 04 rows are inserted, so row numbers are current)
    for sheet in wb.sheet_names:
        for i, row in enumerate(wb.grid(sheet), 1):
            for j, val in enumerate(row or [], 1):
                if not isinstance(val, str):
                    continue
                new = val
                if FIG_EN in new:
                    new = new.replace(FIG_EN, FIG_EN_NEW); fig += 1
                if FIG_AR in new:
                    new = new.replace(FIG_AR, FIG_AR_NEW); fig += 1
                for old, rep in RENAME:
                    if old in new:
                        hits[old] += new.count(old); new = new.replace(old, rep)
                if new != val:
                    s.set("RC-7:item6", sheet, i, j, new, val)
    # S8 (review): CLM-005 ranks challenges, so it states the comparability boundary itself
    t06 = Table(s, "06_EVIDENCE_OBJECTS")
    for lang, old_seg, add in (
            ("en", "The comparison is not nationally representative and is not a ranking of constraints for all Yemeni firms.",
             " Because firms could name more than one challenge, it is not comparable with the 'biggest obstacle' indicator of the "
             "World Bank's standard Enterprise Surveys."),
            ("ar", "لا تمثل المقارنة منشآت اليمن تمثيلًا وطنيًا، وليست ترتيبًا للقيود التي تواجهها جميع المنشآت اليمنية.",
             " ولأن المنشأة كان بإمكانها ذكر أكثر من تحدٍّ، فلا تُقارن بمؤشر «أكبر عائق» في المسوح المعيارية للمنشآت التي يجريها "
             "البنك الدولي.")):
        cur = t06.get("CLM-005", f"limitations_{lang}")
        if cur.count(old_seg + " |") != 1:
            raise TxError(f"S8: CLM-005 limitations_{lang} not as expected")
        t06.set("RC-7:item6", "CLM-005", f"limitations_{lang}", cur.replace(old_seg + " |", old_seg + add + " |"), cur)
    # S9 (review): the internal locators of the sixteen rows say what was read — Table 8, and where Figure 108 agrees or not
    g20 = s.grid("20_FIRM_FINANCE")
    old_loc = "Annex III, Table 8 / Figure 108, p.146"
    seen = 0
    for i, row in enumerate(g20, 1):
        if row and isinstance(row[0], str) and row[0].startswith("FFO-2022-CH-"):
            n = int(row[0].rsplit("-", 1)[1])
            new_loc = ("Annex III, Table 8, p.146 (Figure 108 shows a different value)" if n == 3 else
                       "Annex III, Table 8, p.146 (also shown in Figure 108)" if n in (1, 2, 4, 5, 6) else "Annex III, Table 8, p.146")
            s.set("RC-7:item6", "20_FIRM_FINANCE", i, 17, new_loc, old_loc, f"{row[0]}.source_page_figure")
            seen += 1
    if seen != 16:
        raise TxError(f"S9: found {seen} challenge rows, expected 16")
    # O5 (review): the existing label in the source's own wording
    set_ui(s, "RC-7:item6", "UI-VIS-CAT-FIRM-CH-INFORMAL", "Practices of competitors in the informal sector",
           "ممارسات المنافسين في القطاع غير الرسمي", "Practices of informal competitors", "ممارسات المنافسين غير الرسميين")
    unused = [k for k, n in hits.items() if not n]
    if unused:
        raise TxError(f"rename rules that matched nothing: {unused}")
    left = []
    wb = snapshot(s)
    for sheet in wb.sheet_names:
        for i, row in enumerate(wb.grid(sheet), 1):
            for j, val in enumerate(row or [], 1):
                if isinstance(val, str) and any(x in val for x in LEFTOVER):
                    left.append(f"{sheet}!r{i}c{j}")
    if left:
        raise TxError(f"the old survey name or report title remains in: {left[:12]}")
    notes["item_6"] = OrderedDict([
        ("path", "A — Yemen Financial Sector Diagnostics (World Bank, 5 April 2024; Report No. 194269), Annex III, Table 8, p. 146, "
                 "read in the original PDF on 3 October 2026 (text and rendered page image)"),
        ("values", "all sixteen match Table 8: Electricity 50, Fuel shortages 46, Transport/road blockade 32, Tax administration/tax "
                   "rates 30, Political instability 27, Access to finance 22, Siege 18, Practices of competitors in informal sector "
                   "17, Labor regulations 15, Customs and trade regulation 14, Corruption 10, Access to land 7, Business licensing "
                   "and permits 6, Inadequately educated workers 5, Courts 1, Crime, theft, disorder 0 (percent; the sixteen add "
                   "up to 300)"),
        ("labels", "eight new governed labels (rows 9–16) in the source's item wording; the eight existing labels kept"),
        ("survey_name", f"'custom' removed: {sum(hits.values())} replacements in {len(hits)} phrasings; the source calls it 'the "
                        "2022 Yemen Enterprise Survey' and 'the World Bank's Enterprise Survey of 2022' (Introduction; Annex III title)"),
        ("method", f"Figure 108 / Table 8: {fig} method cells now cite Table 8 and state that Figure 108 differs for transport "
                   "or road blockades (Figure 108: 22; Table 8: 32)"),
        ("source_caution", "the source states no caution that Table 8 is not the standard Enterprise Survey 'biggest obstacle' "
                           "question; that caution is the resource's own method statement and is kept as such"),
        ("contract", "rc_7_stage_inputs.py binds FFO-2022-CH-09..16 to VIS-FIRM-CONSTRAINTS with their labels and unbinds "
                     "UI-VIS-NOTE-FIRM-CONSTRAINTS-PARTIAL"),
    ])
    notes["independent_review"] = OrderedDict([
        ("verdict", "ACCEPTABLE, nothing blocking; every fact checked against the originals; ten SHOULD FIX and six OPTIONAL findings"),
        ("applied", ["S1 YSC-014 note: 'neither the text nor the table states a unit' (the Arabic dual no longer attaches to the ratios)",
                     "S2 YSC-014 fact: 'According to the IMF staff report, which focuses on…' (¶2 says 'focusing'; the annex says the banks' "
                     "balance-sheet data cover the whole of Yemen — added to the note); Arabic «بحسب … وهو تقرير يركّز»",
                     "S3 Arabic «، وهو مسح شمل سبع محافظات» in place of «، الذي شمل…», which could attach to the year or to Yemen; English pair 'which covered'",
                     "S4 the Figure 108 sentence: 'On the same page, the source's chart of the six most often named challenges…'",
                     "S5 the method names the survey's formal-firm sample (the survey also covered 217 informal firms, p. 139)",
                     "S6 the boundary rests on the indicator, in both languages alike: shares can count more than one challenge per firm, "
                     "so they are not comparable with the 'biggest obstacle' indicator (the source counts this survey among its Enterprise Surveys, p. 108)",
                     "S7 the summary and text alternative account for all sixteen bars ('each of the other eight … 15% or fewer, down to 0%')",
                     "S8 CLM-005 states the comparability boundary itself",
                     "S9 the sixteen internal locators say Table 8, and whether Figure 108 agrees",
                     "S10 the source's other tabulations disclosed (Figure 83, p. 111; text on p. 145); neither is used",
                     "O1 «لوائح العمل» / «الجمارك ولوائح التجارة» («أنظمة» means systems in this resource)",
                     "O2 'custom' removed from the two internal cells the first pass missed",
                     "O4 internal wording of the passport method and the analytics boundary",
                     "O5 UI-VIS-CAT-FIRM-CH-INFORMAL in the source's wording: 'Practices of competitors in the informal sector'"]),
        ("second_review", "a workflow of three independent lenses (Arabic editor, English editor, source fidelity) with an adversarial "
                          "check of each finding; besides findings already applied above, it added: F2 the YSC-014 note leads with the "
                          "caveat, not with a verification status the Methodology reserves for unchecked events; F6 YSC-017 discloses "
                          "that the same report's debt sustainability analysis dates the same amount to June 2025; F8 the Reading's "
                          "boundary uses the record's wording; F10 and AR-01 the ratios are named as the banking sector's, with the "
                          "standard name 'ratio of liquid assets to short-term liabilities'; F11 the passport's method field states the "
                          "method; AR-05 a definite label for 'Inadequately educated workers'; AR-06 and AR-10 one Arabic name for the "
                          "survey on the source card and in MA-004"),
        ("kept", ["O3 internal record labels are binding keys; the public labels follow Table 8",
                  "O6 'Firms could name more than one challenge' is the resource's inference from shares adding up to 300; sound, kept"]),
    ])
    rep = s.save(out, ledger, OrderedDict([("transaction", "RC-7"), ("summary", "Part A items 3 and 6 on Path A: originals read"),
                                           ("items", notes)]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
