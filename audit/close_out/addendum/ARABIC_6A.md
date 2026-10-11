# CLOSE-6A — Arabic editorial review

Reviewer: senior Arabic economic editor (subagent). Input: `scratchpad/addendum/review/close_6a_draft.py` (read only). Date: 11 October 2026. Nothing under the repository was modified.

**How to use this file.** Findings are ranked MUST-FIX, SHOULD-FIX, NIT. Where one Arabic field has several findings, the *Corrected* string at its highest-ranked finding already applies every fix for that field; lower findings point back to it. Corrected strings are complete field values (or complete replacement values for the transaction's `(old, new)` pairs), ready to paste. Strings that begin with a space in the draft keep it.

**Checks run.** (1) Every digit sequence in all 41 EN/AR pairs compared mechanically: **0 numeral drift** in the draft and in every corrected string below. (2) Terminology checked against the projected site Arabic (`evidence_objects.json`, `page_sections.json`, `measurement_agenda.json`, `interface_copy.json`, `terminology_register.json`), `ARABIC_HOUSE_STYLE.md` and `NAMING_DECISIONS_2026-10-10.md`. (3) Bidi checked against the Unicode bidi algorithm and the renderer's isolation rules (`LTR_RUN`, `ID_RUN` in `dist/assets/app.js` / `scripts/yfie/text.py`). (4) CR-21 Arabic phrase coverage: in paired `_en`/`_ar` fields the EN and AR replacement counts are equal (0 mismatches), and every Arabic occurrence is preceded by «من», so «من نوفمبر 2022 إلى يناير 2023» stays grammatical after replacement. `BOUND_AR` and `TRIGGER_AR` match site text exactly (95 and 105 cells) and are not reviewed further.

**Tally:** 8 MUST-FIX · 16 SHOULD-FIX · 13 NIT. No numeral, unit or period drift. The drift is in qualifiers, attribution and hedges.

---

## MUST-FIX

### M1 · FAS-YEM-2015 · `method_ar` — the rounding rule is dropped

Current:

```text
قيم مأخوذة من واجهة البيانات المفتوحة للبنك الدولي (مؤشرات التنمية العالمية؛ آخر تحديث للسلاسل في 8 أكتوبر 2026)، كما جُلبت في 11 أكتوبر 2026 وحُفظت نسخةً مؤرخة. وتُقرَّب كل قيمة إلى المنازل العشرية التي ينشرها البنك الدولي لسلسلتها: منزلتان لأجهزة الصراف الآلي، ومنزلة واحدة للفروع والمودعين.
```

Problem: the English says each value is "rounded half up". The Arabic says only «تُقرَّب» ("is rounded"), so the stated method is weaker in Arabic. The site's existing phrase for this rule is «بتقريب النصف إلى الأعلى» (VIS-REMITTANCE-COST, `method_ar`). Also N8: «جُلبت» is a calque of "fetched". The site says «قُرئت من واجهة البيانات المفتوحة للبنك الدولي».

Corrected (also applies N8):

```text
قيم مأخوذة من واجهة البيانات المفتوحة للبنك الدولي (مؤشرات التنمية العالمية؛ آخر تحديث للسلاسل في 8 أكتوبر 2026)، كما قُرئت في 11 أكتوبر 2026 وحُفظت نسخةً مؤرخة. وتُقرَّب كل قيمة، بتقريب النصف إلى الأعلى، إلى عدد المنازل العشرية الذي ينشره البنك الدولي لسلسلتها: منزلتان لأجهزة الصراف الآلي، ومنزلة واحدة للفروع والمودعين.
```

### M2 · FAS-YEM-2015 · `meta_ar` — attribution dropped, truncated term, ungrammatical close

Current:

```text
آخر قيم مسح الوصول المالي لليمن لعام 2015: أجهزة الصراف والفروع لكل 100,000 بالغ والمودعون لكل 1,000؛ تاريخ مؤرخ لا وصول اليوم.
```

Problems:
- The English names the IMF. The Arabic drops «لصندوق النقد الدولي», which leaves a bare «مسح الوصول المالي» in a search snippet. That is a dropped attribution.
- «أجهزة الصراف» without «الآلي» means "cashier/teller devices". The site term is «أجهزة الصراف الآلي». «الفروع» drops "bank": use «فروع البنوك».
- «تاريخ مؤرخ لا وصول اليوم» is a tautology («تاريخ مؤرخ», "a dated date") followed by an elliptical, ungrammatical «لا وصول اليوم». It does not work as a snippet.

Corrected (166 characters; the English is 160):

```text
آخر قيم لليمن في مسح الوصول المالي لصندوق النقد الدولي (2015): أجهزة الصراف الآلي وفروع البنوك لكل 100,000 بالغ، والمودعون لكل 1,000؛ قيم تاريخية لا تصف الوصول اليوم.
```

### M3 · MICS-YEM-2022-23 · `summary_ar` — roles added that the English does not state

Current:

```text
صُمّم المسح العنقودي متعدد المؤشرات (MICS) 2022–2023، الذي أجراه الجهاز المركزي للإحصاء بدعم من اليونيسف، ليقدّم تقديرات للمحافظات الـ22 في اليمن، وتعذرت زيارة 41 من مناطق العدّ المختارة لأسباب أمنية وتتعلق بالسلامة. ويطرح استبيان الأسرة فيه سؤالًا واحدًا عن الخدمات المالية، هو ما إذا كان أي فرد في الأسرة يملك حسابًا مصرفيًا (البند HC19)، ولا يعرض تقرير نتائج المسح جدولًا لإجاباته.
```

Problems:
- The English says "of the Central Statistical Organization and UNICEF", which makes no claim about roles. The Arabic «الذي أجراه الجهاز المركزي للإحصاء بدعم من اليونيسف» asserts who conducted the survey and that UNICEF only supported it. That is an added qualifier. It also differs from the Arabic of the same fact in MA-001 («للجهاز المركزي للإحصاء واليونيسف»).
- S6: «لأسباب أمنية وتتعلق بالسلامة» coordinates an adjective with a verb clause. Use «لأسباب تتعلق بالأمن والسلامة».
- The English has a semicolon after "22 governorates of Yemen"; use «؛».
- The apposition «وهو مسح للجهاز المركزي للإحصاء واليونيسف» avoids the misreading "designed *for* the CSO" that «صُمّم … للجهاز» invites (see N13 for MA-001).

Corrected (also applies S6):

```text
صُمّم المسح العنقودي متعدد المؤشرات (MICS) 2022–2023، وهو مسح للجهاز المركزي للإحصاء واليونيسف، ليقدّم تقديرات للمحافظات الـ22 في اليمن؛ وتعذرت زيارة 41 من مناطق العدّ المختارة لأسباب تتعلق بالأمن والسلامة. ويطرح استبيان الأسرة فيه سؤالًا واحدًا عن الخدمات المالية، هو ما إذا كان أي فرد في الأسرة يملك حسابًا مصرفيًا (البند HC19)، ولا يعرض تقرير نتائج المسح جدولًا لإجاباته.
```

### M4 · MICS-YEM-2022-23 · `meta_ar` — universe dropped; pronoun attaches to the wrong noun

Current:

```text
المسح العنقودي متعدد المؤشرات 2022–2023: صُمّم لـ22 محافظة، وفيه سؤال أسري واحد عن الحساب المصرفي لا يعرض تقرير نتائجه جدولًا له.
```

Problems:
- The English says "MICS 2022–2023 **in Yemen**". The Arabic drops the geography, which is a universe qualifier, and in a snippet it matters.
- In «لا يعرض تقرير نتائجه جدولًا له», «نتائجه» refers back to «سؤال» (the nearest noun), so the Arabic says "the question's findings report".
- S5: «سؤال أسري» reads as "a family(-matters) question". The survey term is a question in the household questionnaire («استبيان الأسرة»), as the record's own `summary_ar` says.

Corrected (148 characters; the English is 134):

```text
المسح العنقودي متعدد المؤشرات 2022–2023 في اليمن: صُمّم لـ22 محافظة، وفي استبيان الأسرة سؤال واحد عن الحساب المصرفي لا يجدوِل تقرير النتائج إجاباته.
```

### M5 · YMPS-YEM-2022-R1 · `meta_ar` — a hedge added to an exact count

Current:

```text
قابل مسح الهاتف المحمول للبنك الدولي عام 2022 نحو 1,297 بالغًا يملكون هواتف محمولة، ويسجل منطقة سيطرة كل مستجيب.
```

Problems:
- «نحو 1,297» ("about 1,297") hedges an exact count. The English and the source both say 1,297.
- «قابل مسح» makes the survey the one who "met" people. «بالغًا يملكون» is better as «بالغًا ممن يملكون», as in the record's `summary_ar`.

Corrected (133 characters; the English is 125):

```text
أجرى مسح الهاتف المحمول التابع للبنك الدولي عام 2022 مقابلات مع 1,297 بالغًا ممن يملكون هواتف محمولة، ويسجل منطقة السيطرة لكل مستجيب.
```

### M6 · CR-22 · /methodology/ s7 `body_ar` (new text) — the Arabic gives a cause the English does not

Current:

```text
والطريقة وكل فترة مسجّلتان مع قيمتهما. ويعكس أثر التصميم لدى البنك الدولي أوزان المسح وحدها، ولا يأخذ في الحسبان الارتباط داخل العناقيد لأنه يختلف من سؤال إلى آخر (منهجية Global Findex 2021، الجدول A.1، الحاشية b)، ولذلك لا تعكس هذه الفترات أثر العنقدة؛ أما المناطق التي استبعدها المسح، ونسبتها نحو 23% من السكان بحسب البنك الدولي، فهي حدٌّ مستقل على التغطية، ولا تُحتسب أي فترة معدَّلة.
```

Problem: the English says intraclass correlation "**which** varies by question", a non-restrictive description. The Arabic «**لأنه** يختلف من سؤال إلى آخر» states a cause. The two languages no longer say the same thing.

The source sides with the Arabic. `audit/close_out/w0/A1_findex_wb.md` quotes footnote b of Table A.1: "does not incorporate the intraclass correlation coefficients **because they vary by question**". **Recommended:** change the English to "…and does not incorporate intraclass correlation coefficients, because they vary by question (…)" and use corrected string A. If the English stays, use B.

The corrected strings also apply S11:
- «أثر التصميم لدى البنك الدولي» becomes «أثر التصميم الذي ينشره البنك الدولي», the phrase in CLM-026, VIS-FINDEX-ACCESS-USE and VIS-FINDEX-GAPS (`method_ar`). s7 itself says «ينشر البنك الدولي أثر تصميم قدره 1.9».
- «ونسبتها نحو 23% من السكان» (areas are not a population share) becomes «ويقطنها نحو 23% من السكان», as in s6 on the same page («مناطق يقطنها نحو 23% من السكان»).
- The calque «حدٌّ مستقل على التغطية» becomes «قيد مستقل على التغطية».
- Bare «الفترات» and «فترة معدَّلة» become «فترات الثقة» and «فترة ثقة معدَّلة». On this site «الفترة» also means a time period, as in every `period_ar`.

Corrected A (English aligned to the source; recommended):

```text
والطريقة وكل فترة مسجّلتان مع قيمتهما. ويعكس أثر التصميم الذي ينشره البنك الدولي أوزانَ المسح وحدها، ولا يأخذ في الحسبان معاملات الارتباط داخل العناقيد لأنها تختلف من سؤال إلى آخر (منهجية Global Findex 2021، الجدول A.1، الحاشية b)، ولذلك لا تعكس فترات الثقة هذه أثر العنقدة؛ أما المناطق التي استبعدها المسح، ويقطنها نحو 23% من السكان بحسب البنك الدولي، فهي قيد مستقل على التغطية، ولا تُحتسب أي فترة ثقة معدَّلة.
```

Corrected B (English unchanged):

```text
والطريقة وكل فترة مسجّلتان مع قيمتهما. ويعكس أثر التصميم الذي ينشره البنك الدولي أوزانَ المسح وحدها، ولا يأخذ في الحسبان الارتباط داخل العناقيد، الذي يختلف من سؤال إلى آخر (منهجية Global Findex 2021، الجدول A.1، الحاشية b)، ولذلك لا تعكس فترات الثقة هذه أثر العنقدة؛ أما المناطق التي استبعدها المسح، ويقطنها نحو 23% من السكان بحسب البنك الدولي، فهي قيد مستقل على التغطية، ولا تُحتسب أي فترة ثقة معدَّلة.
```

### M7 · CLM-039 · `summary_ar` (appended text) — the quotation reads as its opposite

Current: (keep the leading space)

```text
 وتختلف منشورات البنك الدولي نفسها في ما يخص اليمن: إذ تذكر الحاشية المرافقة للشكل A.4.2 في موجز الهجرة والتنمية رقم 40 (يونيو 2024) أن اليمن مستبعد «بسبب توفر البيانات»، بينما تعرض اللوحة (a) من الشكل نفسه قيمة لليمن لعام 2023؛ ولا يأخذ هذا المورد أي قيمة من ذلك الشكل.
```

Problems:
- "due to data availability" is an English idiom for a *lack* of data. Read literally, «بسبب توفر البيانات» says Yemen was excluded *because data are available*. Render the meaning: «لأسباب تتعلق بتوفر البيانات». It stays inside guillemets as the quoted reason.
- S12: the English "also differ" marks this as a further instance after the interface differences already in CLM-039. The Arabic drops "also"; add «أيضًا».
- N7: for a figure note the site uses «ملاحظة» («ملاحظة الرسم»). «الحاشية» is better kept for table footnotes, as in CR-22.

Corrected (also applies S12 and N7): (keep the leading space)

```text
 وتختلف منشورات البنك الدولي نفسها أيضًا في ما يخص اليمن: إذ تذكر الملاحظة المرافقة للشكل A.4.2 في موجز الهجرة والتنمية رقم 40 (يونيو 2024) أن اليمن مستبعد «لأسباب تتعلق بتوفر البيانات»، بينما تعرض اللوحة (a) من الشكل نفسه قيمة لليمن لعام 2023؛ ولا يأخذ هذا المورد أي قيمة من ذلك الشكل.
```

### M8 · all three records · `currentness_ar` — «(تحقق في 11 أكتوبر 2026)» misreads

Current (FAS):

```text
تعود أحدث مشاهدة في هذا السجل إلى عام 2015، وهو آخر عام تورده هذه السلاسل لليمن (تحقق في 11 أكتوبر 2026)، ولا تُقرأ على أنها تصف فترة لاحقة ما لم تُنشر مشاهدة أحدث.
```

Current (MICS):

```text
انتهى العمل الميداني في مايو 2023؛ وتقرير نتائج المسح هو منشور المسح الذي يستند إليه هذا السجل (تحقق في 11 أكتوبر 2026).
```

Current (YMPS):

```text
جرى العمل الميداني للجولة الأولى في أغسطس–سبتمبر 2022 (تحقق في 11 أكتوبر 2026).
```

Problem: unvowelled «تحقق في …» reads as the imperative «تحقَّقْ» ("verify on …") or as the intransitive past «تحقَّقَ» ("came true on …"), not as "(checked on …)". The site's established forms are «جرى التحقق في …» (VIS-FINDEX-ACCESS-USE, VIS-FINDEX-BARRIERS, VIS-FINDEX-RESILIENCE) and «كما اطُّلع عليها في …» (CLM-003, CLM-017). The MICS field also has S8: «منشور المسح» is ambiguous on a site where «منشور» names a central-bank circular. Use «إصدار المسح». The YMPS field begins with «جرى», so the verb changes to «نُفّذ» to avoid «جرى … (جرى …)».

Corrected (FAS):

```text
تعود أحدث مشاهدة في هذا السجل إلى عام 2015، وهو آخر عام تورده هذه السلاسل لليمن (جرى التحقق في 11 أكتوبر 2026)، ولا تُقرأ على أنها تصف فترة لاحقة ما لم تُنشر مشاهدة أحدث.
```

Corrected (MICS; also applies S8):

```text
انتهى العمل الميداني في مايو 2023؛ وتقرير نتائج المسح هو إصدار المسح الذي يستند إليه هذا السجل (جرى التحقق في 11 أكتوبر 2026).
```

Corrected (YMPS):

```text
نُفّذ العمل الميداني للجولة الأولى في أغسطس–سبتمبر 2022 (جرى التحقق في 11 أكتوبر 2026).
```

---

## SHOULD-FIX

### S1 · FAS-YEM-2015 · `summary_ar` — numeral–noun agreement for 103.1, and consistency with MA-005

Current:

```text
يورد مسح الوصول المالي لصندوق النقد الدولي، كما تنشره مؤشرات التنمية العالمية للبنك الدولي، آخر قيم لليمن لعام 2015: 5.81 جهاز صراف آلي و1.5 فرع للبنوك التجارية لكل 100,000 بالغ، و103.1 مودعًا لدى البنوك التجارية لكل 1,000 بالغ. وتتوقف السلاسل عند عام 2015، فهذه قيم تاريخية مؤرخة، لا مقياس حالي للوصول.
```

Problems:
- «103.1 مودعًا» uses the accusative singular, which applies only to numbers ending in 11–99. The same sentence uses the genitive singular after the other decimals («5.81 جهاز»، «1.5 فرع»). MA-005, which states the same three values on /measurement/, has «103.1 مودِع». Use «مودِع» with the kasra, which also separates it from «مودَع», "deposited".
- The record and MA-005 should read alike. MA-005 has «يعود آخر ما ينشره … عن اليمن … إلى عام 2015» and «كما تعرضه مؤشرات التنمية العالمية». WDI is a database that *displays* the IMF series, so «كما تنشره» suits it less well.
- «آخر قيم لليمن لعام 2015» stacks two «لـ» phrases.

Corrected:

```text
يعود آخر ما يورده مسح الوصول المالي لصندوق النقد الدولي عن اليمن، كما تعرضه مؤشرات التنمية العالمية للبنك الدولي، إلى عام 2015: 5.81 جهاز صراف آلي و1.5 فرع للبنوك التجارية لكل 100,000 بالغ، و103.1 مودِع لدى البنوك التجارية لكل 1,000 بالغ. وتتوقف السلاسل عند عام 2015، فهذه قيم تاريخية مؤرخة، لا مقياس حالي للوصول.
```

### S2 · FAS-YEM-2015 · `definition_ar` and `period_ar` — "reported" becomes «متاحة»

Current (definition):

```text
ثلاثة مؤشرات من مسح الوصول المالي لصندوق النقد الدولي لليمن كما تنشرها مؤشرات التنمية العالمية: أجهزة الصراف الآلي لكل 100,000 بالغ (FB.ATM.TOTL.P5)، وفروع البنوك التجارية لكل 100,000 بالغ (FB.CBK.BRCH.P5)، والمودعون لدى البنوك التجارية لكل 1,000 بالغ (FB.CBK.DPTR.P3)، لآخر سنة متاحة.
```

Current (period):

```text
2015، آخر سنة متاحة لليمن
```

Problem: "the last year reported" means the last year the source reports. «آخر سنة متاحة» means "the last year available", which is a statement about access to data. The record's own `currentness_ar` uses the right verb («آخر عام تورده هذه السلاسل»). Moving «لليمن» next to «مؤشرات» also removes the «لصندوق النقد الدولي لليمن» stack, and «تعرضها» aligns with S1.

Corrected (definition):

```text
ثلاثة مؤشرات لليمن من مسح الوصول المالي لصندوق النقد الدولي، كما تعرضها مؤشرات التنمية العالمية: أجهزة الصراف الآلي لكل 100,000 بالغ (FB.ATM.TOTL.P5)، وفروع البنوك التجارية لكل 100,000 بالغ (FB.CBK.BRCH.P5)، والمودعون لدى البنوك التجارية لكل 1,000 بالغ (FB.CBK.DPTR.P3)، لآخر سنة تُورَد عنها قيم.
```

Corrected (period):

```text
2015، آخر سنة تُورَد عنها قيم لليمن
```

### S3 · FAS-YEM-2015 · `universe_ar`, `limitations_ar` (+ MA-005) — one term for "population denominators"

Current (universe):

```text
البالغون في اليمن، بالمقامات السكانية التي يستخدمها صندوق النقد الدولي في مسح الوصول المالي؛ وتقتصر الفروع والمودعون على البنوك التجارية.
```

Current (limitations):

```text
تصف القيم عام 2015 لا الوصول اليوم، وتعدّ الأجهزة والفروع والمودعين، لا الأشخاص الذين يستخدمونها ولا أماكن هذه النقاط. | تتوقف السلاسل عند عام 2015، ومقاماتها السكانية هي مقامات صندوق النقد الدولي؛ وعدد المودعين ليس عدد الأشخاص الفريدين الذين يملكون حسابًا.
```

Problems:
- The record says «المقامات السكانية». MA-005, the same fact on /measurement/, says «قواعد الاحتساب السكانية». «المقامات» on its own is opaque to many readers (it also means musical modes or shrines).
- Use one transparent phrase in both places: «أعداد السكان المعتمدة مقامًا».
- N9: add a comma before the contrastive «لا»: «تصف القيم عام 2015، لا الوصول اليوم،».

Corrected (universe):

```text
البالغون في اليمن، وفق أعداد السكان التي يعتمدها صندوق النقد الدولي مقامًا في مسح الوصول المالي؛ وتقتصر الفروع والمودعون على البنوك التجارية.
```

Corrected (limitations; also applies N9):

```text
تصف القيم عام 2015، لا الوصول اليوم، وتعدّ الأجهزة والفروع والمودعين، لا الأشخاص الذين يستخدمونها ولا أماكن هذه النقاط. | تتوقف السلاسل عند عام 2015، وأعداد السكان المعتمدة مقامًا فيها هي أعداد صندوق النقد الدولي؛ وعدد المودعين ليس عدد الأشخاص الفريدين الذين يملكون حسابًا.
```

Optional third pair for `MA005_BRANCH` on `current_evidence_ar`, since the transaction already writes that cell. Old (occurs once):

```text
وقواعد الاحتساب السكانية فيها هي التي يعتمدها الصندوق
```

New:

```text
وأعداد السكان المعتمدة مقامًا فيها هي أعداد الصندوق
```

The `1.48 → 1.5` pair itself is correct Arabic («و1.5 فرع»).

### S4 · FAS-YEM-2015 · `title_ar` — register term and a stacked «لـ»

Current:

```text
نقاط الوصول لكل بالغ: آخر قيم مسح الوصول المالي لصندوق النقد الدولي لليمن (2015)
```

Problems:
- The terminology register (TERM-018) fixes "access point" as «نقطة الوصول المالي».
- «آخر قيم مسح الوصول المالي لصندوق النقد الدولي لليمن» chains a construct with two «لـ» phrases. «لليمن» can attach to the IMF.

Corrected:

```text
نقاط الوصول المالي لكل بالغ: آخر ما أورده مسح الوصول المالي لصندوق النقد الدولي عن اليمن (2015)
```

### S5 · MICS-YEM-2022-23 · `title_ar` — «سؤال أسري», "not tabulated"

Current:

```text
المسح العنقودي متعدد المؤشرات 2022–2023: سؤال أسري واحد عن الحسابات المصرفية، بلا جدول نتائج
```

Problem: «سؤال أسري» reads as "a family question", and the survey sense is a question in the household questionnaire. «بلا جدول نتائج» ("without a results table") is looser than "not tabulated" («لم تُجدوَل إجاباته»). The same term in `meta_ar` is fixed in M4.

Corrected:

```text
المسح العنقودي متعدد المؤشرات 2022–2023: سؤال واحد في استبيان الأسرة عن الحسابات المصرفية، لم تُجدوَل إجاباته
```

### S6 · MICS-YEM-2022-23 · `summary_ar` — «لأسباب أمنية وتتعلق بالسلامة»

Already applied in M3.

### S7 · MICS-YEM-2022-23 · `method_ar` — "printed p." loses "printed"

Current:

```text
مأخوذ من تقرير نتائج المسح: تصميم العينة (القسم 5.12، ص. 3)، وفترات العمل الميداني (القسم 5.17، ص. 5)، واستبيان الأسرة (الملحق E، البند HC19، ص. 330). ولا يستخدم أي جدول نتائج في التقرير هذا البند.
```

Problems:
- The English says "printed p." three times, because printed page 3 is PDF page 17 (see the value-state locators). «ص. 3» sends a reader to PDF page 3. State the numbering once.
- The site writes «ص 1» without a full stop (15 uses; «ص.» has 0). Change «ص.» to «ص».

Corrected:

```text
مأخوذ من تقرير نتائج المسح (أرقام الصفحات بحسب ترقيم التقرير المطبوع): تصميم العينة (القسم 5.12، ص 3)، وفترات العمل الميداني (القسم 5.17، ص 5)، واستبيان الأسرة (الملحق E، البند HC19، ص 330). ولا يستخدم أي جدول نتائج في التقرير هذا البند.
```

### S8 · MICS-YEM-2022-23 · `currentness_ar` — «منشور المسح»

Already applied in M8.

### S9 · YMPS-YEM-2022-R1 · `summary_ar` — doubled "conducted", date attachment, apposition

Current:

```text
أجرى مسح الهاتف المحمول للرصد الذي نفذه البنك الدولي، في جولته الأولى، مقابلات مع 1,297 بالغًا يمنيًا بعمر 18 سنة فأكثر ممن يملكون هواتف محمولة في أغسطس–سبتمبر 2022، من عينة احتمالية استهدفت 21 محافظة. ويسجل منطقة السيطرة لكل مستجيب، الحكومة المعترف بها دوليًا أو سلطات الأمر الواقع، ويطلب من المستجيبين ترتيب أهم ثلاثة مصادر لدخلهم.
```

Problems:
- «أجرى مسح … الذي نفذه البنك الدولي … مقابلات» says "the survey, which the World Bank carried out, conducted interviews", so the act of conducting appears twice. The English possessive "The World Bank's" is «التابع للبنك الدولي».
- «ممن يملكون هواتف محمولة في أغسطس–سبتمبر 2022» attaches the date to phone ownership. Move the date to the verb.
- The appositive «، الحكومة المعترف بها دوليًا أو سلطات الأمر الواقع،» between commas reads as a list. Parentheses, or a colon as in MA-001, make it an apposition. The authority names are correct and neutral.

Corrected:

```text
أجرت الجولة الأولى من مسح الهاتف المحمول للرصد التابع للبنك الدولي، في أغسطس–سبتمبر 2022، مقابلات مع 1,297 بالغًا يمنيًا بعمر 18 سنة فأكثر ممن يملكون هواتف محمولة، من عينة احتمالية استهدفت 21 محافظة. ويسجل المسح منطقة السيطرة لكل مستجيب (الحكومة المعترف بها دوليًا أو سلطات الأمر الواقع)، ويطلب من المستجيبين ترتيب أهم ثلاثة مصادر لدخلهم.
```

### S10 · YMPS-YEM-2022-R1 · `definition_ar` — locator name and «مدخل»

Current:

```text
العينة والفترة وبندان من الجولة الأولى لمسح الهاتف المحمول للرصد في اليمن (2022) الذي نفذه البنك الدولي، كما يوثقها مدخل الفهرس في مكتبة البيانات الجزئية: منطقة سيطرة المستجيب وترتيب مصادر الدخل.
```

Problems:
- This is the record's first mention of the World Bank Microdata Library. The catalogue exists only in English, so give «(Microdata Library)» here so readers can find it, as CLM-023's note does.
- Unvowelled «مدخل الفهرس» reads first as "the catalogue's entrance". «صفحة المسح في فهرس …» is unambiguous.
- «… (2022) الذي نفذه البنك الدولي» has an unclear antecedent. Use «التابع للبنك الدولي», as in S9.

Corrected:

```text
العينة والفترة وبندان من الجولة الأولى (2022) لمسح الهاتف المحمول للرصد في اليمن التابع للبنك الدولي، كما توثقها صفحة المسح في فهرس مكتبة البيانات الجزئية (Microdata Library): منطقة سيطرة المستجيب وترتيب مصادر الدخل.
```

### S11 · CR-22 — «لدى البنك الدولي», «ونسبتها», «حدٌّ … على التغطية», bare «فترة»

Already applied in M6 (A and B).

### S12 · CLM-039 — "also" dropped

Already applied in M7.

### S13 · CWR-010 s6 `body_ar` (new third finding) — "currency exchangers" is narrowed; the clause is hard to parse

Current (the `new` value of the second pair; the first pair «وتحدّد ثلاث خلاصات لاحقة موضع توقف الدليل.» is correct):

```text
نظرًا إلى ندرة فروع البنوك وأجهزة الصراف الآلي. أما الخلاصة الثالثة فتخص الوصول إلى النقد نفسه: إذ يفيد تقرير لتحالف النقد في اليمن صدر في مايو 2026، استند إلى بحث مكتبي ومسح صغير لتجار في تعز ومقابلات مع عدد قليل من خبراء المال والعمل الإنساني، بأن البنوك ومحلات الصرافة في المناطق الخاضعة لإدارة الحكومة المعترف بها دوليًا قيّدت سحب الريال وتصريف العملات من أواخر فبراير إلى منتصف مايو 2026. وهذه ممارسة مُبلَّغ عنها في تلك المناطق وتلك الأشهر، لا مقياس لعدد المستفيدين المتأثرين بها، ولا يثبت التقرير سببها.
```

Problems:
- «محلات الصرافة» means exchange *shops*. The English "currency exchangers" is generic. The site and CBY-Aden's own documents name the regulated categories «شركات ومنشآت الصرافة» (CLM-009 universe: «شركات الصرافة ومنشآت الصرافة الفردية»; CBY circulars: "exchange companies/establishments").
- 27 words separate «يفيد» from its complement «بأن», so the finding is hard to locate. The fix keeps the English order: the report and its basis first, then what it reports.
- N10: «خبراء المال» ("money experts") becomes «الخبراء في الشأن المالي». «سحب الريال» ("withdrawing the rial") becomes «السحب بالريال».
- The following are correct: «تحالف النقد في اليمن» (glossed earlier in s6), «تصريف العملات», «في المناطق الخاضعة لإدارة الحكومة المعترف بها دوليًا», «ثلاث خلاصات لاحقة», and the closing boundary sentence.

Corrected (also applies N10):

```text
نظرًا إلى ندرة فروع البنوك وأجهزة الصراف الآلي. أما الخلاصة الثالثة فتخص الوصول إلى النقد نفسه، ومصدرها تقرير لتحالف النقد في اليمن صدر في مايو 2026 واستند إلى بحث مكتبي ومسح صغير لتجار في تعز ومقابلات مع عدد قليل من الخبراء في الشأن المالي والعمل الإنساني: إذ يفيد التقرير بأن البنوك وشركات ومنشآت الصرافة في المناطق الخاضعة لإدارة الحكومة المعترف بها دوليًا قيّدت السحب بالريال وتصريف العملات من أواخر فبراير إلى منتصف مايو 2026. وهذه ممارسة مُبلَّغ عنها في تلك المناطق وتلك الأشهر، لا مقياس لعدد المستفيدين المتأثرين بها، ولا يثبت التقرير سببها.
```

### S14 · VIS-E-MONEY-RULE-STACK · `summary_ar` (appended text) — "own" dropped; split verb–object

Current: (keep the leading space)

```text
 وللاطلاع على الخلفية التاريخية لهذه الطبقات، تصف ورقة نشرها مركز صنعاء للدراسات الاستراتيجية في مارس 2022، وهي تحليل ثانوي لا بيان صادر عن جهة رقابية، خدماتِ النقود الإلكترونية عبر الهاتف المحمول بأنها كانت قائمة على البنوك بموجب المنشور رقم 11 لسنة 2014 الصادر عن البنك المركزي، وتذكر أن البنك المركزي اليمني في صنعاء فتح بعد انقسام البنك المركزي باب تقديم النقود الإلكترونية أمام مؤسسات غير مصرفية اعتبارًا من مارس 2020، في حين أبقى البنك المركزي اليمني – عدن على الإطار القائم على البنوك الذي سبق الحرب. ثم عرّفت تعليمات البنك المركزي اليمني – عدن الصادرة في 14 سبتمبر 2022 مقدمي خدمات الدفع بأنهم مؤسسات مالية غير مصرفية مرخص لها من البنك المركزي.
```

Problems:
- "CBY-Aden's **own** instructions" marks the shift from a secondary paper to the regulator's primary text, and the Arabic drops it. Add «نفسه».
- «فتح بعد انقسام البنك المركزي باب …» splits the verb from its object with a long adverbial. Front the time clause: «وتذكر أنه بعد انقسام البنك المركزي فتح البنك المركزي اليمني في صنعاء باب …».
- «الصادر عن البنك المركزي» becomes «… البنك المركزي اليمني». Since 2016 a bare «البنك المركزي» is ambiguous, and in 2014 there was one bank.
- The following are correct and neutral: «البنك المركزي اليمني في صنعاء»، «البنك المركزي اليمني – عدن»، «بعد انقسام البنك المركزي»، «مقدمي خدمات الدفع» (accusative object, correct case), and «تحليل ثانوي لا بيان صادر عن جهة رقابية».

Corrected (it keeps «الحرب» for parity; see S15): (keep the leading space)

```text
 وللاطلاع على الخلفية التاريخية لهذه الطبقات، تصف ورقة نشرها مركز صنعاء للدراسات الاستراتيجية في مارس 2022، وهي تحليل ثانوي لا بيان صادر عن جهة رقابية، خدماتِ النقود الإلكترونية عبر الهاتف المحمول بأنها كانت قائمة على البنوك بموجب المنشور رقم 11 لسنة 2014 الصادر عن البنك المركزي اليمني، وتذكر أنه بعد انقسام البنك المركزي فتح البنك المركزي اليمني في صنعاء باب تقديم النقود الإلكترونية أمام مؤسسات غير مصرفية اعتبارًا من مارس 2020، في حين أبقى البنك المركزي اليمني – عدن على الإطار القائم على البنوك الذي سبق الحرب. ثم عرّفت تعليمات البنك المركزي اليمني – عدن نفسه، الصادرة في 14 سبتمبر 2022، مقدمي خدمات الدفع بأنهم مؤسسات مالية غير مصرفية مرخص لها من البنك المركزي.
```

### S15 · VIS-E-MONEY-RULE-STACK (both languages) — "pre-war" / «الذي سبق الحرب»

Problem: the site's neutral register is "conflict" / «النزاع». The Arabic site text has 15 cells with «النزاع» and none with «الحرب», for example «قبل النزاع» and «فالنزاع سياق للتفسير». This paraphrase is not a quotation, so it should follow the house register. Change both languages together. EN: "the pre-conflict, bank-led framework". AR: replace the exact fragment

```text
الإطار القائم على البنوك الذي سبق الحرب
```

with

```text
الإطار القائم على البنوك الذي سبق النزاع
```

### S16 · CLM-012 `limitations` (both languages) — "the areas it administers" gives a central bank a territory

Current (`new` value of the Arabic pair):

```text
ولا التبني، وهذه قواعد البنك المركزي اليمني – عدن، لا القواعد التي أصدرها البنك المركزي اليمني في صنعاء للمناطق التي يديرها. |
```

Problem: "for the areas it administers" / «للمناطق التي يديرها» says the Central Bank of Yemen in Sana'a administers territory. That is a governmental attribute and reads as political loading. The house style asks for the issuer's scope to be given as recorded, without political judgement. A neutral and accurate form is "for the areas where it operates" / «للمناطق التي يعمل فيها». A semicolon also separates the new clause from the list of negations it follows («… ولا التبني؛ وهذه قواعد …»). EN `new`: "or adoption, and these are CBY-Aden's rules, not those the Central Bank of Yemen in Sana'a has issued for the areas where it operates. |".

Corrected (Arabic `new` value):

```text
ولا التبني؛ وهذه قواعد البنك المركزي اليمني – عدن، لا القواعد التي أصدرها البنك المركزي اليمني في صنعاء للمناطق التي يعمل فيها. |
```

---

## NIT

**N1 · MICS and YMPS `limitations_ar`: the second bullet begins with «و».** The renderer splits on " | " into separate items, and 47 of 53 second items on the site start without «و». The MICS fix is «ولو جُدول البند» → «حتى لو جُدوِل البند،». The YMPS fix is «وتسجيل» → «تسجيل».

Corrected (MICS):

```text
لا يقيس المسح امتلاك الأفراد للحسابات ولا استخدامها ولا الأموال عبر الهاتف المحمول ولا الادخار ولا الاقتراض، ولا يعرض تقرير نتائجه أي نتيجة لبند الحساب المصرفي. | حتى لو جُدوِل البند، لأظهر ما إذا كان أي فرد في الأسرة يملك حسابًا مصرفيًا، لا أيّ أفرادها يملكونه.
```

Corrected (YMPS; also applies N5):

```text
البالغون الذين يملكون هواتف محمولة ليسوا كل البالغين، والمسح الذي أكمله نحو 28 في المئة ممن جرى التواصل معهم لا يمثلهم جميعًا؛ ويسمّي نص المعاينة في الفهرس 18 محافظة بينما يذكر الملخص 21. | تسجيل منطقة السيطرة ومصادر الدخل لا يقيس الشمول المالي؛ ويُعرض المسح بوصفه أداة قائمة يمكن أن توسعها جولة لاحقة.
```

**N2 · MICS `period_ar`.** A label followed directly by a date reads as a fragment. Add a colon after «العمل الميداني» and a comma between the two hubs.

Current:

```text
العمل الميداني يوليو–سبتمبر 2022 (مركز عدن) ويناير–مايو 2023 (مركز صنعاء)
```

Corrected:

```text
العمل الميداني: يوليو–سبتمبر 2022 (مركز عدن)، ويناير–مايو 2023 (مركز صنعاء)
```

**N3 · YMPS `title_ar`.** Use «منطقتَي السيطرة كلتيهما», which renders "both" and matches MA-009. Vowelling «منطقتَي» also rules out the "my region" reading of «منطقتي».

Current:

```text
مسح الهاتف المحمول للبنك الدولي في أغسطس–سبتمبر 2022 يسجل مستجيبين في منطقتي السيطرة
```

Corrected:

```text
مسح الهاتف المحمول للبنك الدولي في أغسطس–سبتمبر 2022 يسجل مستجيبين في منطقتَي السيطرة كلتيهما
```

**N4 · YMPS `method_ar`.** «الفهرس 5999» reads as "catalogue no. 5999" only if «رقم» is added. The rest is correct («المعاينة»، «معدل الاستجابة»، «قاموس البيانات»).

Current:

```text
مأخوذ من البيانات الوصفية للمسح في الفهرس (مكتبة البيانات الجزئية، الفهرس 5999: الملخص والمعاينة ومعدل الاستجابة وقاموس البيانات). ولم يُستخدم أي ملف بيانات.
```

Corrected:

```text
مأخوذ من البيانات الوصفية للمسح في الفهرس (مكتبة البيانات الجزئية، الفهرس رقم 5999: الملخص والمعاينة ومعدل الاستجابة وقاموس البيانات). ولم يُستخدم أي ملف بيانات.
```

**N5 · YMPS `limitations_ar`, first clause.** «ليس كل البالغين ممن يملكون هواتف محمولة» is logically equivalent to the English but reads awkwardly. «البالغون الذين يملكون هواتف محمولة ليسوا كل البالغين» follows the English order. Applied in N1.

**N6 · CLM-023 note.** «في فهرس الدراسة 5862 (جمع البيانات، تواريخ جمع البيانات)» stacks two parentheticals and reads "the catalogue of study 5862". Name the catalogue section and field in quotation marks. Also change «ص. 17» to «ص 17» (site convention). The dates and the one-day difference are correct.

Current: (keep the leading space)

```text
 ويختلف سجلّا البنك الدولي لتاريخَي العمل الميداني بيوم واحد: إذ تذكر مكتبة البيانات الجزئية (Microdata Library) في فهرس الدراسة 5862 (جمع البيانات، تواريخ جمع البيانات) الفترة من 7 نوفمبر 2022 إلى 9 يناير 2023، وتذكر منهجية Global Findex 2021 (الملحق A، الجدول A.1، ص. 17) الفترة من 7 نوفمبر 2022 إلى 10 يناير 2023؛ أما في سائر هذا المورد فتُذكر الفترة من نوفمبر 2022 إلى يناير 2023.
```

Corrected: (keep the leading space)

```text
 ويختلف سجلّا البنك الدولي لتاريخَي العمل الميداني بيوم واحد: إذ يذكر فهرس مكتبة البيانات الجزئية (Microdata Library) للدراسة 5862، في قسم «جمع البيانات» وبند «تواريخ جمع البيانات»، الفترة من 7 نوفمبر 2022 إلى 9 يناير 2023، وتذكر منهجية Global Findex 2021 (الملحق A، الجدول A.1، ص 17) الفترة من 7 نوفمبر 2022 إلى 10 يناير 2023؛ أما في سائر هذا المورد فتُذكر الفترة من نوفمبر 2022 إلى يناير 2023.
```

**N7 · CLM-039 «الحاشية المرافقة للشكل».** Applied in M7.

**N8 · FAS `method_ar` «جُلبت».** Applied in M1.

**N9 · FAS `limitations_ar` comma.** Applied in S3.

**N10 · CWR-010 «خبراء المال», «سحب الريال».** Applied in S13.

**N11 · E-money «المنشور رقم 11 لسنة 2014».** This is acceptable. CBY's own genre name for circulars is «منشور دوري» (`audit/close_out/w0/A3_cby.md`), and the site elsewhere calls the June 2024 instrument «تعميم». If the 2014 instrument's Arabic title is not held, leave it as drafted. «قائمة على البنوك» for "bank-led" is also acceptable. «بقيادة البنوك» is a common alternative, and switching is optional.

**N12 · CR-22.** The new text ends «ولا تُحتسب أي فترة ثقة معدَّلة.» and the existing next sentence begins «ولا تُحتسب فترة لنسب الفئات…». The repetition mirrors the English ("no adjusted interval is computed. No interval is computed…"). It is acceptable, and changing it is optional.

**N13 · MA-001 (existing cell, not touched by CLOSE-6A).** «فقد صُمّم المسح العنقودي متعدد المؤشرات (MICS) 2022–2023 للجهاز المركزي للإحصاء واليونيسف ليشمل…» invites the reading "designed *for* the CSO". The apposition used in M3 («، وهو مسح للجهاز المركزي للإحصاء واليونيسف،») fixes it if the lead wants to touch that cell.

---

## Bidi and mixed script — no defect found

- **Year ranges.** The renderer isolates `\d{4}[–-]\d{4}` in `<bdi dir="ltr">` (LTR_RUN), so «(MICS) 2022–2023» and «المسح العنقودي متعدد المؤشرات 2022–2023» display the range the same way. Without that isolation, the W7 rule would order the first differently from the second.
- **Codes and labels.** FB.ATM.TOTL.P5, FB.CBK.BRCH.P5, FB.CBK.DPTR.P3, HC19, E, A, A.1, A.4.2, (a), b, (MICS) and (Microdata Library) each sit between Arabic runs. The paired-bracket rule (N0) resolves every parenthesis to RTL, so none mirrors wrongly or migrates, including «اللوحة (a)» and «الحاشية b)،». ID_RUN does not isolate them because they have no hyphen, and they do not need it.
- **Digits after «و» and «لـ».** «و1.5»، «و103.1» and «لـ22»/«الـ22» follow site convention («و1.48», «و3.46%», «المحافظات الـ22») and render in the right order.
- **Punctuation.** The draft's Arabic contains no Latin comma or semicolon, no stray LRM/RLM and no double spaces. «–» with spaces in «البنك المركزي اليمني – عدن» matches the house form. Guillemets «…» are used only for quotations.
- **Spelling.** No hamza omissions were found (الى/اذا/ان and similar). Tanwin is correct on «سؤالًا واحدًا»، «حسابًا مصرفيًا»، «بالغًا يمنيًا»، «نسخةً»، «اعتبارًا»، «دوليًا».

## Meta descriptions (after the fixes)

| Record | EN chars | AR draft | AR fixed | Notes |
|---|---|---|---|---|
| FAS-YEM-2015 | 160 | 127 | 166 | IMF restored; full ATM term; no tautology |
| MICS-YEM-2022-23 | 134 | 129 | 148 | "in Yemen" restored; pronoun fixed |
| YMPS-YEM-2022-R1 | 125 | 112 | 133 | exact count; «ممن يملكون»; idiomatic «أجرى … مقابلات» |

The site's Arabic meta descriptions have a median of 137 characters and a 90th percentile of 153. All three fixed snippets lead with the source and year, then the figure or design, then the boundary.

## Outside Arabic scope (for the lead)

- **O1 · CR-22 English.** Align it to the source's "because they vary by question" (M6, option A).
- **O2 · CR-21 coverage.** `CR21_PHRASES` does not match the en-dash form in CWR-007's `evidence_period` ("Global Findex, Yemen fieldwork 7 November 2022 – 9 January 2023" / «… 7 نوفمبر 2022 – 9 يناير 2023»; `readings.json[6]`, repeated in `page_specs`). Both languages stay day-precise. Parity holds, but that public clock misses CR-21's aim.
- **O3 · FAS English title.** "Access points per adult" does not match the content: the values are per 100,000 adults (ATMs, branches) and per 1,000 adults (depositors), and depositors are not access points. The Arabic follows the English. If the English changes, the Arabic changes with it.
