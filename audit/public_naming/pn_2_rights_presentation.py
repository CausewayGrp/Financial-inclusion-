# -*- coding: utf-8 -*-
"""Rights presentation, transaction PN-2. English and Arabic together.

  python3 pn_2_rights_presentation.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

The owner's brief of 10 October 2026, Part B4: present the rights of this resource to the standard of the World Bank
or Our World in Data, Master-first. The rights DECISION was taken on 3 October 2026 and closed on 10 October 2026
(audit/OWNER_DECISIONS_2026-10-10.md, OWN-04-R); this transaction decides nothing about it and changes no figure,
period, universe, limit or source. It claims no rights clearance, no legal review and no certification.

What it adds:

1. UI-FOOTER-LICENCE — one text line in every page's footer, beside the existing copyright and edition line: that
   CauseWay's own content is under CC BY 4.0 unless otherwise noted, that third-party material stays under its
   owners' terms, and where to read the detail. Text only; no badge image. The renderer prints it in the footer's
   fine line and emits <link rel="license" href="https://creativecommons.org/licenses/by/4.0/"> in every page's head
   — the deed's own canonical URL, with no language or legalcode suffix.

2. /rights/ section 6 restated so the scope is exact, with a covered list and a not-covered list, as the brief sets
   it out. Added to what the page already said:
     - the CauseWay NAME and MARKS, not only the logo, are outside the licence;
     - the repository's SOFTWARE CODE is outside this licence, and nothing is decided about it;
     - FIGURES DERIVED FROM THE WORLD BANK FINDEX MICRODATA are outside it, and CC BY does not extend to the
       underlying data. Published figures do derive from it (the three 95% intervals on /evidence/CLM-026/, CauseWay
       derivation FC-1 from micro_yem.dta, which is never redistributed), and whether the World Bank Microdata
       Research License permits publishing them is a legal question escalated to the owner and counsel
       (design/ESCALATIONS.md; audit/public_naming/RIGHTS_PRESENTATION.md §3). The page therefore states only what is
       true on any reading of that licence, and asserts no permission;
     - the legal code is linked beside the deed, and in Arabic the official Arabic legal code is linked too, with the
       English named as the canonical text (Creative Commons' own canonical URL is the English one, and its 2020
       corrections notice leaves the current Arabic text's status unverifiable);
     - attribution follows CC's TASL practice — title, author, source, licence, and whether changes were made —
       inside the existing two-line format, which is unchanged in substance.

3. UI-RIGHTS-ATTRIBUTION-NOTE — the "changes made" element of TASL, stated once as a governed label so the two-line
   format does not have to grow.

Nothing is removed from /rights/: the three conditions, the exclusion of third-party material, the two-line
attribution and the statement that the page does not say any third-party rights have been cleared all stay.
"""
import json, os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "release_candidate"))
from rc_lib import Session, TxError, insert_ui_rows  # noqa: E402

F = "PN-2:RIGHTS"
S03 = "03_PAGE_SECTIONS"
RULE = "PN-2. The owner's brief of 10 October 2026, Part B4 (rights presentation). "

UI_ROWS = [
    ("UI-FOOTER-LICENCE",
     "Text, analysis and visual designs © 2026 CauseWay, licensed under CC BY 4.0 unless otherwise noted; "
     "third-party material remains under its owners' terms. See Rights and reuse.",
     "النصوص والتحليلات والتصاميم المرئية © 2026 CauseWay، وتُتاح بموجب رخصة CC BY 4.0 ما لم يُذكر خلاف ذلك؛ "
     "وتبقى مواد الجهات الأخرى خاضعة لشروط أصحابها. انظر صفحة الحقوق وإعادة الاستخدام.",
     RULE + "The licence line in the footer of every page, beside the copyright and edition line. Text only, no badge "
            "image. The machine-readable form is <link rel=\"license\" "
            "href=\"https://creativecommons.org/licenses/by/4.0/\"> in every page's head — the licence deed's own "
            "canonical URL. It states the licence; it claims no rights clearance."),
    ("UI-RIGHTS-ATTRIBUTION-NOTE",
     "Where you have changed what you reused — recalculated, reformatted, translated, cropped or combined it — say so, "
     "so a reader can tell your version from this one.",
     "وإذا غيّرت ما أعدت استخدامه — بإعادة الحساب أو إعادة التنسيق أو الترجمة أو الاقتطاع أو الدمج — فاذكر ذلك، "
     "ليتمكن القارئ من التمييز بين نسختك وهذه النسخة.",
     RULE + "/rights/: the 'changes made' element of CC's recommended attribution practice (title, author, source, "
            "licence), stated once beside the existing two-line citation format rather than lengthening it."),
]

RIGHTS_EN_OLD = (
    "CauseWay licenses the content it owns in this resource under the Creative Commons Attribution 4.0 International "
    "licence (CC BY 4.0, https://creativecommons.org/licenses/by/4.0): its text, analysis and visual designs, the "
    "compiled evidence records, and the structure and annotations of the data exports when they are published. The "
    "CauseWay logo is not part of the licensed content. You may share and adapt that content for any purpose, provided "
    "you credit CauseWay, link to the licence and indicate whether you made changes. The licence does not cover "
    "third-party material: documents, data, tables, figures and text published by others remain under their "
    "publishers' terms, including where this resource reports them, and this resource does not host copies of their "
    "files. CauseWay asks that a reused figure be credited in two lines: first this resource (Yemen Financial "
    "Inclusion Evidence, the record, CauseWay, the edition and the page address), then the original source that the "
    "record names (publisher, title, year and link). This page states the licence CauseWay applies to its own content; "
    "it does not state that any third-party rights have been cleared."
)

RIGHTS_EN_NEW = (
    "CauseWay licenses the content it owns in this resource under the Creative Commons Attribution 4.0 International "
    "licence (CC BY 4.0). The licence summary is at https://creativecommons.org/licenses/by/4.0 and its legal text, "
    "which is the text that governs, is at https://creativecommons.org/licenses/by/4.0/legalcode; Creative Commons "
    "publishes an official Arabic translation of that legal text at "
    "https://creativecommons.org/licenses/by/4.0/legalcode.ar, and the English text is the reference text.\n"
    "Covered: CauseWay's text and analysis; its visual designs; the compiled evidence records and the annotations "
    "CauseWay wrote for them; and the structure and annotations of the data exports when they are published.\n"
    "Not covered: material published by others — documents, data, tables, figures and text — which remains under its "
    "publishers' terms, including where this resource reports it, and of which this resource hosts no copies; the "
    "CauseWay name, logo and other marks; the software code in this resource's repository, which is outside this "
    "licence and about which nothing is decided here; and figures this resource derived from the World Bank's Global "
    "Findex microdata, because CC BY 4.0 does not extend to that underlying data or to a figure computed from it. "
    "Where such a figure is published, the record that carries it names the data, the licence it was supplied under "
    "and the method, and this resource holds no copy of that data for anyone else to take.\n"
    "You may share and adapt the covered content for any purpose, provided you credit CauseWay, link to the licence "
    "and say whether you changed anything. CauseWay asks that a reused figure be credited in two lines: first this "
    "resource (Yemen Financial Inclusion Evidence, the record, CauseWay, the edition and the page address), then the "
    "original source that the record names (publisher, title, year and link).\n"
    "This page states the licence CauseWay applies to its own content. It does not state that any third-party rights "
    "have been cleared, and it is not legal advice."
)

RIGHTS_AR_OLD = (
    "تتيح CauseWay المحتوى الذي تملكه في هذا المورد بموجب رخصة المشاع الإبداعي «نَسب المُصنَّف 4.0 دولي» "
    "(CC BY 4.0، https://creativecommons.org/licenses/by/4.0): نصوصه وتحليلاته وتصاميمه المرئية، وسجلات الأدلة "
    "المجمَّعة، وبنية ملفات البيانات المُصدَّرة وشروحها عند نشرها. ولا يدخل شعار CauseWay في المحتوى المرخَّص. ويجوز لك "
    "مشاركة هذا المحتوى وتعديله لأي غرض، بشرط أن تنسبه إلى CauseWay، وأن تضع رابطًا إلى الرخصة، وأن تبيّن ما إذا كنت قد "
    "أجريت تغييرات. ولا تشمل الرخصة مواد الجهات الأخرى: فالوثائق والبيانات والجداول والرسوم والنصوص التي تنشرها جهات "
    "أخرى تبقى خاضعة لشروط ناشريها، بما في ذلك حين يوردها هذا المورد، ولا يستضيف هذا المورد نسخًا من ملفاتها. وتطلب "
    "CauseWay أن يُنسب الرقم المُعاد استخدامه في سطرين: أولًا هذا المورد (أدلة الشمول المالي في اليمن، والسجل، "
    "وCauseWay، والإصدار، ورابط الصفحة)، ثم المصدر الأصلي الذي يسمّيه السجل (الناشر، والعنوان، والسنة، والرابط). "
    "وتذكر هذه الصفحة الرخصة التي تطبقها CauseWay على محتواها الخاص، ولا تفيد بأن أي حقوق لجهات أخرى قد سُوّيت."
)

RIGHTS_AR_NEW = (
    "تتيح CauseWay المحتوى الذي تملكه في هذا المورد بموجب رخصة المشاع الإبداعي «نَسب المُصنَّف 4.0 دولي» (CC BY 4.0). "
    "وملخص الرخصة في https://creativecommons.org/licenses/by/4.0، ونصها القانوني، وهو النص الحاكم، في "
    "https://creativecommons.org/licenses/by/4.0/legalcode، وتنشر مؤسسة المشاع الإبداعي ترجمة عربية رسمية له في "
    "https://creativecommons.org/licenses/by/4.0/legalcode.ar؛ والنص الإنجليزي هو النص المرجعي.\n"
    "ما تشمله الرخصة: نصوص CauseWay وتحليلاتها؛ وتصاميمها المرئية؛ وسجلات الأدلة المجمَّعة والشروح التي كتبتها CauseWay "
    "لها؛ وبنية ملفات البيانات المُصدَّرة وشروحها عند نشرها.\n"
    "ما لا تشمله: المواد التي تنشرها جهات أخرى — من وثائق وبيانات وجداول ورسوم ونصوص — فهي تبقى خاضعة لشروط ناشريها، "
    "بما في ذلك حين يوردها هذا المورد، ولا يستضيف هذا المورد نسخًا من ملفاتها؛ واسم CauseWay وشعارها وعلاماتها الأخرى؛ "
    "والشيفرة البرمجية في مستودع هذا المورد، فهي خارج هذه الرخصة ولا يُقرَّر هنا شيء بشأنها؛ والأرقام التي استخلصها هذا "
    "المورد من البيانات الجزئية للمؤشر العالمي للشمول المالي (Global Findex) الصادر عن البنك الدولي، إذ لا تمتد رخصة "
    "CC BY 4.0 إلى تلك البيانات الأصلية ولا إلى رقم محتسب منها. وحيث يُنشر رقم من هذا النوع، يسمّي السجل الذي يحمله "
    "البياناتَ والرخصةَ التي أتيحت بموجبها والطريقةَ المتّبعة، ولا يحتفظ هذا المورد بنسخة من تلك البيانات ليأخذها أحد.\n"
    "ويجوز لك مشاركة المحتوى المشمول وتعديله لأي غرض، بشرط أن تنسبه إلى CauseWay، وأن تضع رابطًا إلى الرخصة، وأن تذكر "
    "ما إذا كنت قد غيّرت شيئًا. وتطلب CauseWay أن يُنسب الرقم المُعاد استخدامه في سطرين: أولًا هذا المورد (أدلة الشمول "
    "المالي في اليمن، والسجل، وCauseWay، والإصدار، ورابط الصفحة)، ثم المصدر الأصلي الذي يسمّيه السجل (الناشر، والعنوان، "
    "والسنة، والرابط).\n"
    "وتذكر هذه الصفحة الرخصة التي تطبقها CauseWay على محتواها الخاص، ولا تفيد بأن أي حقوق لجهات أخرى قد سُوّيت، "
    "وليست استشارة قانونية."
)


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)

    for ui_id, en, ar, _ in UI_ROWS:
        if not en or not ar:
            raise TxError(f"{ui_id}: both languages are required")
    insert_ui_rows(s, F, UI_ROWS)

    g03 = s.grid(S03)
    en_rows = [i for i, r in enumerate(g03, 1)
               if r and r[0] == "/rights/" and str(r[1]) == "6" and (r[4] or "").startswith("CauseWay licenses")]
    ar_rows = [i for i, r in enumerate(g03, 1)
               if r and r[0] == "/rights/" and str(r[1]) == "6" and (r[6] or "").startswith("تتيح CauseWay")]
    if len(en_rows) != 1 or len(ar_rows) != 1:
        raise TxError(f"03: /rights/ section 6 found en={len(en_rows)} ar={len(ar_rows)} times")
    s.set(F, S03, en_rows[0], 5, RIGHTS_EN_NEW, RIGHTS_EN_OLD, "03!/rights/.6.body_en")
    s.set(F, S03, ar_rows[0], 7, RIGHTS_AR_NEW, RIGHTS_AR_OLD, "03!/rights/.6.body_ar")

    rep = s.save(out, ledger, OrderedDict([
        ("transaction", "PN-2"),
        ("summary", "Rights presentation (the owner's brief of 10 October 2026, Part B4): a footer licence line and "
                    "its machine-readable form, and /rights/ section 6 restated with an exact covered and not-covered "
                    "scope, the legal code linked beside the deed, and TASL attribution. The licence decision is "
                    "unchanged; licence_text_confirmed and public_downloads stay false; no rights clearance, legal "
                    "review or certification is claimed."),
        ("items", OrderedDict([("interface_rows", len(UI_ROWS)), ("page_section_bodies", 2)])),
    ]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
