# D7 cold read — Arabic edition (28 September 2026)

Reader: a fresh agent with no repository or conversation context, briefed in Arabic to read the built site at
`design/reference/out` (the checkpoint tree, before the Explore fix of DL-D7-003) as a researcher, a regulator and a
journalist, report only material findings, and change nothing. The report is the reader's, verbatim (written in English
with the Arabic quotations as found); its adjudication is in `design/10_ACCEPTANCE_CHECKLIST.md` §K.4. Its scratch
evidence (screenshots, text dumps, link and anchor check, bidi measurements) was not committed.

---

Arabic cold-read (/ar/, 12 pages, 1440 + 390 px, search tested). No BLOCKING finding.

1. MATERIAL · /ar/payments/, /ar/readings/same-year-different-number/ · One value, two notations: prose «إلى 1.262 مليار ريال», table «1,262» (مليون) beside «317.639 … 910.688»; readings «6.245 مليار دولار» vs chart «6,245». Dot-decimal, comma-thousands and mixed precision collide; 317.639 reads as 317,639. Fix: one unit and fixed precision per series; name the decimal mark in the unit label.

2. MATERIAL · /ar/ hero; /ar/evidence/compare/?records=CLM-001,CLM-010 · One Findex number, three years: «لعام 2021 … (نُفذ العمل الميداني من نوفمبر 2022 إلى يناير 2023؛ وسنة البيانات لدى البنك الدولي 2022)»; one table writes the window three ways: «من نوفمبر 2022 إلى يناير 2023», «من 2022-11-07 إلى 2023-01-09», «من 7 نوفمبر 2022 إلى 9 يناير 2023». A writer cannot tell which year to cite. Fix: one canonical label everywhere plus a one-line citation form.

3. MATERIAL · /ar/payments/ (also readings, providers) · The screen-reader alternative renders for everyone: four visible «وصف نصي لهذا العرض» blocks; each caveat appears up to three times («لا يثبت: …» in the description, «ما لا يُستنتج: …» in the foot, again in the table caption); page height 17,379 px. Which block is authoritative is unclear. Fix: sr-only/collapsed once the chart renders; one caveat per figure.

4. MATERIAL · /ar/payments/ · «معاملات نقاط البيع — يُحجب الرقم إلى أن يُوثَّق تعريفه» (H1 2025) sits above a chart of monthly POS transactions for the same months (8,015…11,832). The withheld state is clear; why the neighbouring series is admissible is not. Fix: one sentence naming the withheld release.

5. MINOR · /ar/explore/ · «04 ابدأ بالسؤال — أسئلة للبدء» promises «استخدم الأسئلة أدناه…» and holds nothing; rubric numbers (01, 04) disagree with the index (02, 05). Fix: remove or link to #questions; align numbering.

6. MINOR · compare page · «ليست مقارنة مباشرة. 2 سجلات مختارة.» is ungrammatical (template «سجلات مختارة»+numeral); «اختر سجلين على الأقل» shows with two loaded; «لا يثبت:» and «لا يُستنتج:» repeat one sentence. Fix: «سجلان مختاران»; suppress the prompt; one caveat.

7. MINOR · compare table, /ar/explore/, CLM-003 · Bidi: ISO dates split across lines («من 2022-11-» / «07 إلى 2023-01-09» at 390; «2023-» / «09-01» at 1440) because compare cells lack the <bdi> used on /ar/; signed figures render «%11+», «%7.6+»; unwrapped ranges mirror («خلال 2022–2023» displays 2023–2022) while wrapped ones read 2021–2024. Fix: <bdi dir="ltr" class="nw"> on every date, signed number and range.

8. MINOR · payments, readings, providers, measurement · Untranslated footers «المصدر: Central Bank of Yemen — Aden», «المصدر: Yemen Microfinance Network; …»; raw path as link label «السجل الكامل: /ar/evidence/VIS-POS-TERMINALS/» (41 pages), self-link on the reading page. Fix: Arabic publisher names; «افتح سجل الدليل ←» as on /ar/.

9. MINOR · site-wide · Authored Arabic, not machine translation, but terms drift: bare «التحويلات» for remittances beside «التحويلات النقدية» (cash transfers, 28×) and «الحوالات المحلية» (50×); «خدمة أموال عبر الهاتف المحمول» (14×) vs «النقود الإلكترونية» (156×); «المحفظة الاسمية» (calque of nominal portfolio); «نموذج المتبقي البديل» vs «نموذج القيمة المتبقية». Fix: one term per concept («تحويلات المغتربين», «النقود الإلكترونية», «إجمالي محفظة القروض») plus a glossary line.

10. MINOR · /ar/evidence/CLM-003/ · «07 المنهج وطريقة التحقق» hides «كيف أُنتج؟» (the 8.55% formula) behind a summary that reads as prose, not a control; «استشهد بهذا السجل» copies a ~900-character paragraph with only «✓ / تم النسخ», no preview or access date; POS legend says «يُعرض الرقمان» yet the chart plots one value per point. Fix: open by default or label «اعرض التفاصيل»; show the citation; plot the +11% or reword.

11. MINOR · CLM-003, CLM-044 at 390 px · The 01–07 index is injected between «01 ما الذي يثبته هذا الدليل؟» and «02 ما الذي يقيسه؟», so the record seems to end after one paragraph. Fix: place the index above Q1 on mobile.

12. MINOR · /ar/data/, /ar/explore/ · All 151 cards say «شروط إعادة الاستخدام: غير مقيّمة»; «P0 · الأفراد» is unexplained on /ar/explore/ (defined only on /ar/measurement/). Fix: one page-level statement and assess the open-licensed WB/IMF items; expand P0 at first use.

Works clearly: CLM-044 shows no value anywhere (HTML, meta, citation); search behaves («الحوالات» 10 typed results; «زززز» → «لا توجد نتيجة… ولا يعني ذلك غياب الأدلة»); 170 internal links and 157 anchors resolve; no console errors, no horizontal scroll at 390.

Researcher — Record schema (يثبت/يقيس/ينطبق/حداثة/لا يثبت/المصدر/المنهج) is usable and sources open. Mixed notation (1) and the three-format Findex window (2) tax every reuse. Collapsed method and copy-only citation (10) slow reproduction. Term drift (9) makes search unreliable. Usable with care; fix 1–2 before citing at scale.

Regulator — Firewall is explicit (licence ≠ operation, missing ≠ zero). The withheld cell beside monthly data (4) raises a "why" nothing answers. English source lines (8) and «غير مقيّمة» ×151 (12) look unfinished to an official reader. No misstated number found. Presentable internally, not yet polished for an official audience.

Journalist — In 30 s the hero says what this is and that limits are part of it; the "three numbers" block works at 90 s, but the Findex-year question (2) stops a fast writer. Charts crop safely; duplication (3) buries the one caveat that matters. «%11+» and «1.262/1,262» (1, 7) are what a subeditor queries. Quotable, with a fact-check on years and units.
