# CLOSE-6C — Arabic editorial review: Reading CWR-012 and records CCY-ISP-2024, CCY-SAM-2024

Reviewer: senior Arabic economic editor (subagent). Input: `scratchpad/c6c/CWR-012_review_bundle.md` (read only), with the source read `scratchpad/addendum/reads/R5_ccy_isp_sam.md` for meaning. Date: 11 October 2026. Nothing under the repository was modified.

**How to use this file.** Findings are ranked MUST-FIX, SHOULD-FIX and NIT. Where one Arabic field has several findings, the *Corrected* string at its highest-ranked finding already applies every fix for that field, and the lower findings point back to it. Corrected strings are complete field values, or complete paragraphs or bullets of a Reading section, ready to paste.

**Checks run.**
1. Every digit sequence in all 29 EN/AR pairs (14 Reading fields and sections, 15 record fields) was compared mechanically. Four pairs differ, and none is a value drift:
   - Evidence period and s6: "2025 Q3" is «الربع الثالث من 2025». This is acceptable and is the site's form.
   - CCY-SAM summary and meta: "USD 1" is «دولار أمريكي واحد» / «لكل دولار». This is acceptable, because the value state is TRIVIAL.
   - CCY-SAM summary: "30 days" is written in words («الأيام الثلاثين»), although `30` is a READ value state. This is fixed in S1.
   
   Every corrected string below was re-checked and has **0 numeral drift**.
2. Terminology was checked against `terminology_register.json` (TERM-001 «الحوالات», TERM-002 «التحويلات النقدية» for programme payments, TERM-003), the projected site Arabic (`evidence_objects.json`, `readings.json`, `page_specs.json`, `source_library.json`), `ARABIC_HOUSE_STYLE.md`, `NAMING_DECISIONS_2026-10-10.md` and the conventions of ARABIC_6A. The following are already correct:
   - «جرى التحقق في»
   - «ص 9»
   - «عُزل/عزلة» for sub-district
   - «البنك المركزي اليمني – عدن»
   - «الحكومة المعترف بها دوليًا»
   - «منشآت الصرافة الفردية»
   - «وكلاء الحوالات»
   - «عبر مشغل تحويل أموال»
   - «المحافظ الإلكترونية»
   - «الأموال عبر الهاتف»
   - «أعاد … عرض»
   - «أين يتوقف الدليل؟»
   - «ليس سببًا»
   - «ليس دليلًا على التشغيل»
   
   The `change_trigger_ar` and `verification_ar` strings match site text exactly (109 and 97 cells), so they were not reviewed further.
3. Bidi was checked against the renderer: `clock()` in `scripts/yfie/render.py` sets no `dir="auto"`, and `LTR_RUN`/`ID_RUN` are in `scripts/yfie/text.py`.
4. The E2-DATES gate (`scripts/validate.py`) was checked: every date in the corrected strings is already a stated value state.
5. A spelling and punctuation scan found 0 hamza slips, 0 Latin commas or semicolons, 0 bidi control characters, 0 Arabic-Indic digits and 0 double spaces.

**Tally:** 6 MUST-FIX · 14 SHOULD-FIX (one of them, S14, is programme-level and not for this change) · 7 NIT. The only numeral finding is the word-written «الثلاثين», which is fixed in S1. The drift is in qualifiers, hedges and claims about what a source prints, plus two mistranslations (M5, M6).

---

## MUST-FIX

### M1 · Thesis and s1 (identical text) — a "receipt" qualifier added to "no channel value"

Current (the clause in both fields):

```text
ولا تتضمن قاعدة الأدلة قيمة لقناة الاستلام في تلك الموجة؛
```

Problem: the English says "no channel value for that wave is held here". The Arabic «قيمة لقناة الاستلام» narrows this to the channel of *receipt*, which implies that sending-channel values might be held. s3 itself says the base holds no channel value for domestic remittances at all. Also, «أي» is needed to carry "no … value".

Corrected (paste into **both** `thesis_ar` and s1):

```text
في موجة 2021 من Global Findex الخاصة باليمن، تلقى 31.9% من البالغين في المناطق التي شملها المسح حوالات محلية، في حين كان لدى 11.9% من البالغين حساب. ويتسق ذلك مع فرضية أن الأموال المرسلة بين الأسر تمر أساسًا عبر شركات الصرافة لا عبر الحسابات، لكنه يبقى فرضية: فالمسح يعدّ البالغين لا الأسر، ولا تغطي قيمه الواردة هنا إلا الحوالات داخل اليمن، ولا تتضمن قاعدة الأدلة أي قيمة لقنوات الحوالات في تلك الموجة؛ كما أن تغطية المسح، والمساعدات النقدية الإنسانية، والعملة، ومعنى «الحوالة» كلها تنسجم مع الأرقام نفسها.
```

### M2 · s2, first paragraph — the World Bank attribution is dropped

Current:

```text
نسبة البالغين الذين تلقوا أموالًا من داخل البلاد في المناطق التي شملها المسح في اليمن أعلى من نسبة من يملكون حسابًا، لكن المسح لا يبيّن كيف وصلت تلك الأموال. ففي موجة 2021 من المؤشر العالمي للشمول المالي (Global Findex) الخاصة باليمن، التي نُفّذ عملها الميداني من نوفمبر 2022 إلى يناير 2023، أرسل 17.7% من البالغين في المناطق المشمولة حوالات محلية، وتلقاها 31.9%، وقام 37.8% بأيٍّ من الأمرين؛ وكان لدى 11.9% من البالغين حساب. وكل قيمة من هذه نسبة من جميع البالغين، مأخوذة من سؤال مستقل، فلا تُظهر الأرقام كم ممن تلقوا الأموال كان لديهم حساب. وينشر البنك الدولي أيضًا نسب الإرسال والاستلام بحسب الجنس والعمر والتعليم والدخل والمشاركة في قوة العمل، وتُعرض في الجدول في صفحة /people/؛ ولا تُنشر هنا فترة ثقة لقيمة أي فئة، والفرق بين الفئات ليس سببًا.
```

Problems:
- The English says "the **World Bank's** Global Findex 2021 wave". This is the page's first full naming of the survey, and the Arabic drops the publisher. That is the same class of fault as ARABIC_6A M2.
- N: «في المناطق المشمولة» is truncated. The site form is «في المناطق التي شملها المسح» (402 cells; the truncated form has 0).
- N: "how that money travelled" is «كيف انتقلت», which describes the route. «كيف وصلت» means "how it arrived".
- «التي نُفّذ عملها الميداني» now follows «البنك الدولي». The apposition «وهي الموجة الخاصة باليمن» keeps the antecedent unambiguous.
- «من نوفمبر 2022 إلى يناير 2023» is kept verbatim (CR-21 form).

Corrected (the second line of s2, «ويعدّ المسح البالغين لا الأسر…», is unchanged):

```text
نسبة البالغين الذين تلقوا أموالًا من داخل البلاد في المناطق التي شملها المسح في اليمن أعلى من نسبة من يملكون حسابًا، لكن المسح لا يبيّن كيف انتقلت تلك الأموال. ففي موجة 2021 من المؤشر العالمي للشمول المالي (Global Findex) التابع للبنك الدولي، وهي الموجة الخاصة باليمن التي نُفّذ عملها الميداني من نوفمبر 2022 إلى يناير 2023، أرسل 17.7% من البالغين في المناطق التي شملها المسح حوالات محلية، وتلقاها 31.9%، وقام 37.8% بأيٍّ من الأمرين؛ وكان لدى 11.9% من البالغين حساب. وكل قيمة من هذه نسبة من جميع البالغين، مأخوذة من سؤال مستقل، فلا تُظهر الأرقام كم ممن تلقوا الأموال كان لديهم حساب. وينشر البنك الدولي أيضًا نسب الإرسال والاستلام بحسب الجنس والعمر والتعليم والدخل والمشاركة في قوة العمل، وتُعرض في الجدول في صفحة /people/؛ ولا تُنشر هنا فترة ثقة لقيمة أي فئة، والفرق بين الفئات ليس سببًا.
```

### M3 · s5, "Humanitarian cash" bullet — the hedge "can be" is dropped

Current:

```text
- المساعدات النقدية الإنسانية: المساعدات النقدية التي تقدمها البرامج والجهات الإنسانية طريق آخر يصل به المال إلى الأسر، ولا تُظهر القيم المنشورة ما إذا كان أي مستجيب قد عدّ شيئًا منها حوالة. وتُظهر دراستان لتحالف النقد في اليمن (Cash Consortium of Yemen) عن متلقي المساعدات حجمَ هذا الطريق حيث يعمل: ففي ثلاث عُزل شملها مسح في يونيو 2024 شكّلت المساعدات معظم الدخل النقدي للمستفيدين، تليها القروض والهدايا غير الرسمية، وفي الضالع وجعار لم يحتسب بعض المستجيبين الحوالات دخلًا أصلًا. وتقتصر الدراستان على متلقي المساعدات، ولا تسجلان أي قناة لانتقال المال بين الأسر، فهما لا تؤكدان الفرضية ولا تنقضانها.
```

Problem: the English says the studies "show how large that route **can be** where it operates". «تُظهر … حجمَ هذا الطريق» says they show *the size* of the route. That turns two recipient-only studies into a measurement of the route. The modal must be restored. The rest of the bullet is accurate, including «فهما لا تؤكدان الفرضية ولا تنقضانها». See also O1 and O3 on the English.

Corrected:

```text
- المساعدات النقدية الإنسانية: المساعدات النقدية التي تقدمها البرامج والجهات الإنسانية طريق آخر يصل به المال إلى الأسر، ولا تُظهر القيم المنشورة ما إذا كان أي مستجيب قد عدّ شيئًا منها حوالة. وتُظهر دراستان لتحالف النقد في اليمن (Cash Consortium of Yemen) عن متلقي المساعدات ما قد يبلغه حجم هذا الطريق حيث يعمل: ففي ثلاث عُزل شملها مسح في يونيو 2024 شكّلت المساعدات معظم الدخل النقدي للمستفيدين، تليها القروض والهدايا غير الرسمية، وفي الضالع وجعار لم يحتسب بعض المستجيبين الحوالات دخلًا أصلًا. وتقتصر الدراستان على متلقي المساعدات، ولا تسجلان أي قناة لانتقال المال بين الأسر، فهما لا تؤكدان الفرضية ولا تنقضانها.
```

### M4 · CCY-ISP-2024 · `limitations_ar` — "prints no split" becomes "does not distinguish"

Current:

```text
تصف الحصص متلقي المساعدات النقدية في ثلاث عُزل، لا الأسر في اليمن، والهدايا والقروض من الشبكات غير الرسمية ليست حوالات: فالدراسة لا تذكر قناة ولا تكرارًا ولا مبلغًا ولا تفصل بين الدعم من داخل اليمن وخارجه. | التغيرات في تقديم الدعم وتلقيه هي ما أفاد به المستفيدون أنفسهم، دون خط أساس أو مجموعة مقارنة، ولا تستخلص الدراسة أي علاقة سببية.
```

Problem: the English is about what the study **prints**: "prints no channel, frequency, amount or split between support from inside and outside Yemen". «ولا تفصل بين الدعم من داخل اليمن وخارجه» says the study *does not distinguish* the two. The source does the opposite: its network-diversity dimension covers "support from those inside or outside Yemen" (R5 §1.3). It simply prints no split. The Arabic therefore makes a false claim about the study's design. «لا تذكر» ("does not mention") is also weaker than "prints no". Use «لا تورد».

Corrected:

```text
تصف الحصص متلقي المساعدات النقدية في ثلاث عُزل، لا الأسر في اليمن، والهدايا والقروض من الشبكات غير الرسمية ليست حوالات: فالدراسة لا تورد قناةً ولا تكرارًا ولا مبلغًا، ولا توزيعًا للدعم بين ما يأتي من داخل اليمن وما يأتي من خارجه. | التغيرات في تقديم الدعم وتلقيه هي ما أفاد به المستفيدون أنفسهم، دون خط أساس أو مجموعة مقارنة، ولا تستخلص الدراسة أي علاقة سببية.
```

### M5 · CCY-SAM-2024 · `limitations_ar` — «تقديران نموذجيان» means "exemplary estimates"

Current:

```text
المضاعفان تقديران نموذجيان لقرى مختارة، لا مضاعف لليمن أو لمحافظة، ويقيسان نشاطًا اقتصاديًا يشمل التحويل نفسه، لا دخل الأسر أو الدخل المحلي؛ ولا يقولان شيئًا عن طريقة وصول المال إلى الأسر. | تصف مصادر الدخل متلقي مساعدات اختيروا لأنهم تلقوا جولتين على الأقل، فحصة من ذكروا المساعدات تعكس طريقة اختيار العينة؛ ولا تحمل الحوالات والدعم من الأسرة أي قيمة مطبوعة، وهذا غياب للبيانات لا صفر.
```

Problems:
- «نموذجي» means "model" only in the sense of ideal, exemplary or typical («تقدير نموذجي» = "a model estimate" in the sense of a textbook-perfect one). The English "model estimates" means estimates *produced by a model*. The Arabic therefore reverses the hedge into praise. The phrase has 0 uses on the site. Use «تقديران مستخرجان من نموذج».
- «التحويل نفسه»: under TERM-001/002/003 a bare «التحويل» is the funds-transfer act. The programme payment is «التحويل النقدي» (TERM-002). This matters on the /remittances/ route.
- «جولتين على الأقل» is clearer as «جولتين على الأقل من المساعدات», because M6 uses «الجولة الأولى» for spending rounds.

Corrected:

```text
المضاعفان تقديران مستخرجان من نموذج لقرى مختارة، لا مضاعف لليمن أو لمحافظة، ويقيسان نشاطًا اقتصاديًا يشمل التحويل النقدي نفسه، لا دخل الأسر أو الدخل المحلي؛ ولا يقولان شيئًا عن طريقة وصول المال إلى الأسر. | تصف مصادر الدخل متلقي مساعدات اختيروا لأنهم تلقوا جولتين على الأقل من المساعدات، فحصة من ذكروا المساعدات تعكس طريقة اختيار العينة؛ ولا تحمل الحوالات والدعم من الأسرة أي قيمة مطبوعة، وهذا غياب للبيانات لا صفر.
```

### M6 · CCY-SAM-2024 · `method_ar` — «آثار الجولة الأولى» reads as "effects of the first assistance round"

Current:

```text
مضاعف مستخرج من مصفوفة محاسبة اجتماعية واحدة لكل منطقة، تمثل لقطة بأسعار ثابتة وحصص إنفاق ثابتة: إجمالي النشاط الاقتصادي، بما فيه النقد المضخوخ، مقسومًا على النقد المضخوخ. ولا يحتسب إلا آثار الجولة الأولى، ويستبعد إنفاق أصحاب الأعمال والعاملين لديهم والإنفاق خارج المنطقة، ولا يُنشر له أي مدى أو فترة؛ ولا تُطبع مصفوفات جعار، فلا يمكن إعادة حساب قيمتها من التقرير.
```

Problems:
- On the same record, «جولتين» means rounds *of assistance* (universe and limitations). «لا يحتسب إلا آثار الجولة الأولى» therefore reads as "it counts only the effects of the first assistance round", which is a different and false method statement. The English "first-round effects" means the first round of spending (the source: "first-order economic impact"). Use «آثار الجولة الأولى من الإنفاق».
- A bare «فترة» is a time period on this site, as in every `period_ar` (ARABIC_6A S11). "interval" here is a confidence interval. Use «فترة ثقة ولا مدى».
- «ولا تُطبع مصفوفات جعار» is a habitual present ("Ja'ar's matrices do not get printed"). The English says they are not printed in this report. Use «ولم ينشر التقرير مصفوفات جعار».

Corrected:

```text
مضاعف مستخرج من مصفوفة محاسبة اجتماعية واحدة لكل منطقة، تمثل لقطة بأسعار ثابتة وحصص إنفاق ثابتة: إجمالي النشاط الاقتصادي، بما فيه النقد المضخوخ، مقسومًا على النقد المضخوخ. ولا يحتسب إلا آثار الجولة الأولى من الإنفاق، ويستبعد إنفاق أصحاب الأعمال والعاملين لديهم والإنفاق خارج المنطقة، ولا تُنشر له فترة ثقة ولا مدى؛ ولم ينشر التقرير مصفوفات جعار، فلا يمكن إعادة حساب قيمتها منه.
```

---

## SHOULD-FIX

### S1 · CCY-SAM-2024 · `summary_ar` — bound value "30" written in words; «التحويل»; role verb

Current:

```text
قدّرت دراسة تجريبية أجراها تحالف النقد في اليمن عام 2024، باستخدام مصفوفة محاسبة اجتماعية واحدة بُنيت من مسح لأسر تتلقى مساعدات نقدية متعددة الأغراض ومقابلات مع أصحاب أعمال محليين، أن كل دولار أمريكي واحد من المساعدات أنتج نشاطًا اقتصاديًا قيمته 2.56 دولار، بما فيه التحويل نفسه، في قرى مختارة من عزلة الضالع، و2.29 دولار في قرى مختارة من عزلة جعار، وكلتاهما تخضع لإدارة الحكومة المعترف بها دوليًا؛ وتذكر الدراسة أن القيمتين لا تقبلان المقارنة المباشرة. وبين الأسر التي شملها التقييم، كانت مصادر الدخل الرئيسية المُبلَّغ عنها في الأيام الثلاثين السابقة للمقابلة المساعدات النقدية (61%) والعمل بالأجر اليومي أو العرضي (55%)، وتشير الدراسة إلى أن بعض المستجيبين لم يحتسبوا الحوالات أو الديون دخلًا.
```

Problems:
- **Numeral parity.** "30 days" is a READ value state (p. 12), but the Arabic writes it as «الثلاثين». The house rule is digits in data. The site form is «خلال 30 يومًا» (page_specs, /measurement/).
- «بما فيه التحويل نفسه» becomes «التحويل النقدي نفسه» (TERM-002; see M5).
- «أجراها تحالف النقد» asserts who conducted the study. The English possessive "A … CCY pilot study" does not; REACH, SI and ACTED had the stated roles (R5 §2.1). Use «دراسة تجريبية لتحالف النقد في اليمن», as the record's own `meta_ar` does.
- NIT: «العمل بالأجر اليومي أو العرضي» reverses the English order, "casual or daily wage labour".

Corrected:

```text
قدّرت دراسة تجريبية لتحالف النقد في اليمن عام 2024، باستخدام مصفوفة محاسبة اجتماعية واحدة بُنيت من مسح لأسر تتلقى مساعدات نقدية متعددة الأغراض ومقابلات مع أصحاب أعمال محليين، أن كل دولار أمريكي واحد من المساعدات أنتج نشاطًا اقتصاديًا قيمته 2.56 دولار، بما فيه التحويل النقدي نفسه، في قرى مختارة من عزلة الضالع، و2.29 دولار في قرى مختارة من عزلة جعار، وكلتاهما تخضع لإدارة الحكومة المعترف بها دوليًا؛ وتذكر الدراسة أن القيمتين لا تقبلان المقارنة المباشرة. وبين الأسر التي شملها التقييم، كانت مصادر الدخل الرئيسية المُبلَّغ عنها خلال 30 يومًا سبقت المقابلة المساعدات النقدية (61%) والعمل العرضي أو بالأجر اليومي (55%)، وتشير الدراسة إلى أن بعض المستجيبين لم يحتسبوا الحوالات أو الديون دخلًا.
```

If O2 is accepted, also change «مصفوفة محاسبة اجتماعية واحدة بُنيت» to «مصفوفة محاسبة اجتماعية واحدة لكل منطقة بُنيت».

### S2 · Reading · `evidence_period_ar` — the only Arabic Reading field that opens in Latin; no gloss at first mention

Current:

```text
Global Findex 2021، العمل الميداني في اليمن نوفمبر 2022 – يناير 2023 · الملف القطري للبنك الدولي لعام 2014 · قائمة البنك المركزي اليمني – عدن لعام 2026 · أسعار الحوالات لعام 2023 والربع الثالث من 2025 · التقريران السنويان للبنك المركزي اليمني – عدن 2024 و2025 · دراستا تحالف النقد في اليمن عن متلقي المساعدات (بيانات مسوح يناير ويونيو 2024)
```

Problems:
- Of the 11 Readings' Arabic fields, this is the only one that begins with a Latin run. The page clock inherits `dir="rtl"`, so it renders correctly, but the field reads as untranslated.
- The house style asks for «المؤشر العالمي للشمول المالي (Global Findex)» at first mention (the site form «المؤشر العالمي للشمول المالي (Global Findex) 2021» has 30 uses).
- The evidence-period clock is the first place on the page that names CCY. CWR-010 glosses it there: «(Cash Consortium of Yemen، 2026)».
- The en-dash form of the fieldwork dates is kept as in the English (see ARABIC_6A O2).

Corrected:

```text
المؤشر العالمي للشمول المالي (Global Findex) 2021، العمل الميداني في اليمن نوفمبر 2022 – يناير 2023 · الملف القطري للبنك الدولي لعام 2014 · قائمة البنك المركزي اليمني – عدن لعام 2026 · أسعار الحوالات لعام 2023 والربع الثالث من 2025 · التقريران السنويان للبنك المركزي اليمني – عدن 2024 و2025 · دراستا تحالف النقد في اليمن (Cash Consortium of Yemen) عن متلقي المساعدات (بيانات مسوح يناير ويونيو 2024)
```

### S3 · s6 — "put … at" becomes «قدّر» ("estimated")

Current:

```text
تتعلق سلسلتان أخريان بالأموال المرسلة إلى اليمن، لا داخله. فقد بلغ المتوسط السنوي الذي ينشره البنك الدولي لتكلفة إرسال 200 دولار أمريكي إلى اليمن 2.81% من المبلغ في 2023؛ وفي الربع الثالث من 2025 بلغ متوسط عروض الأسعار لمنتجات رسمية لإرسال 200 دولار أمريكي من السعودية إلى اليمن 2.70%. وهذه أسعار للإرسال، لا تكلفة استلام المال في اليمن ولا تكلفة تتحملها الأسرة، ولا تشمل القنوات غير الرسمية. وعلى مستوى الاقتصاد ككل، تورد التقارير السنوية للبنك المركزي اليمني – عدن قيمًا مختلفة للسنة نفسها: فقد قدّر التقرير السنوي 2024 الحوالات في عام 2024 بمبلغ 6,245 مليون دولار، ثم أعاد التقرير السنوي 2025 عرض عام 2024 عند 3,422.16 مليون دولار، كما تشرح القراءة التحليلية «العام نفسه، رقم مختلف». ولا تبيّن أيٌّ من القيمتين عدد الأسر التي تلقت أموالًا ولا القناة التي وصلت عبرها.
```

Problems:
- The English verb is neutral ("put remittances … at"). «قدّر» assigns the value the status of an estimate, which crosses the observed ≠ estimated line in the reader's mind. The dominant site form for this exact fact is «أورد التقرير السنوي 2024 قيمة عام 2024 عند 6,245 مليون دولار» (100 cells; «قدّر» has 7).
- «تورد … فقد أورد» would repeat the verb, so the first one becomes «تعطي», as in CWR-001's thesis.

Corrected:

```text
تتعلق سلسلتان أخريان بالأموال المرسلة إلى اليمن، لا داخله. فقد بلغ المتوسط السنوي الذي ينشره البنك الدولي لتكلفة إرسال 200 دولار أمريكي إلى اليمن 2.81% من المبلغ في 2023؛ وفي الربع الثالث من 2025 بلغ متوسط عروض الأسعار لمنتجات رسمية لإرسال 200 دولار أمريكي من السعودية إلى اليمن 2.70%. وهذه أسعار للإرسال، لا تكلفة استلام المال في اليمن ولا تكلفة تتحملها الأسرة، ولا تشمل القنوات غير الرسمية. وعلى مستوى الاقتصاد ككل، تعطي التقارير السنوية للبنك المركزي اليمني – عدن قيمًا مختلفة للسنة نفسها: فقد أورد التقرير السنوي 2024 قيمة الحوالات في عام 2024 عند 6,245 مليون دولار، ثم أعاد التقرير السنوي 2025 عرض عام 2024 عند 3,422.16 مليون دولار، كما تشرح القراءة التحليلية «العام نفسه، رقم مختلف». ولا تبيّن أيٌّ من القيمتين عدد الأسر التي تلقت أموالًا ولا القناة التي وصلت عبرها.
```

### S4 · s3, both paragraphs — "how much money" and "do not compare"

Current paragraph 1 (the sentence at issue):

```text
وهذه نسب من المتلقين لا من جميع البالغين؛ ولا تبيّن حصة الأموال التي مرت عبر كل قناة، ولا تصف الوضع الراهن.
```

Current paragraph 2 (the sentence at issue):

```text
ولا تُقارن بها أعداد أقدم:
```

Problems:
- "how much money moved through each channel" is an amount. «حصة الأموال» ("the share of the money") swaps a volume for a share, on a page whose firewall is shares versus amounts. Use «مقدار الأموال».
- «ولا تُقارن بها أعداد أقدم» says "older counts are not compared with them", which is an editorial choice. The English "do not compare with them" means they are *not comparable*. Use «ولا تقبل الأعدادُ الأقدم المقارنةَ بها».

Corrected paragraph 1:

```text
القيم الوحيدة المتعلقة بالقنوات في قاعدة الأدلة هذه قيم تاريخية. فالملف القطري الموزون للبنك الدولي لعام 2014 يفيد بأن 18.3% من البالغين تلقوا حوالات محلية، وأن 31.1% من هؤلاء المتلقين تلقوها عبر مشغل تحويل أموال، و2.0% عبر مؤسسة مالية. وهذه نسب من المتلقين لا من جميع البالغين؛ ولا تبيّن مقدار الأموال التي مرت عبر كل قناة، ولا تصف الوضع الراهن. أما موجة 2021، فلا تتضمن قاعدة الأدلة هذه أي قيمة لقنوات الحوالات المحلية فيها، ولم يطرح مسح اليمن أسئلة خدمات الأموال عبر الهاتف.
```

Corrected paragraph 2:

```text
وعلى جانب العرض، تُدرج القائمة الرسمية لعام 2026 الصادرة عن البنك المركزي اليمني – عدن 100 شركة صرافة و231 منشأة صرافة فردية و111 وكيلًا للحوالات. وهذه قيود معدودة بحسب فئات القائمة نفسها، لا عدد لمقدمي خدمات فريدين ولا لمن يعمل منهم حاليًا. ولا تقبل الأعدادُ الأقدم المقارنةَ بها: إذ تذكر وثيقة تقييم مشروع FMIIP الصادرة عن البنك الدولي (مايو 2025) أن فروع شركات الصرافة ارتفعت من 876 في 2017 إلى 3,244 في 2019، من دون ذكر مصدر، بينما يعرض تقرير للمركز الدولي للنمو (فبراير 2026) الزوج نفسه من الأرقام بوصفه تقديرات لعدد الكيانات، بما فيها مؤسسات التمويل الأصغر.
```

### S5 · s5 "Currency" bullet and s9 third bullet — «صرف» is used for two different acts

Current (s5):

```text
- العملة: تمارس شركات الصرافة تبديل العملات إلى جانب صرف الحوالات، فلا يُظهر عدد قيودها أو فروعها حجم ما يخص الحوالات من نشاطها، ويغيّر تحرك سعر الصرف قيمة الحوالة نفسها بالريال.
```

Current (s9):

```text
- بيانات من شركات الصرافة ووكلاء الحوالات تفصل صرف الحوالات عن تبديل العملات، بحسب المنطقة؛
```

Problems:
- In a sentence about *exchange* companies, «صرف الحوالات» (paying out transfers) and «سعر الصرف» (exchange rate) use the same root for opposite sides of the distinction the bullet draws.
- «تبديل العملات» has 0 uses on the site. The site and the CBY use «تصريف العملات» (CWR-010).
- Use «تسليم الحوالات» for pay-outs, which is common Yemeni usage at the counter, and «تصريف العملات» for exchange.

Corrected (s5):

```text
- العملة: تمارس شركات الصرافة تصريف العملات إلى جانب تسليم الحوالات، فلا يُظهر عدد قيودها أو فروعها حجم ما يخص الحوالات من نشاطها، ويغيّر تحرك سعر الصرف قيمة الحوالة نفسها بالريال.
```

Corrected (s9):

```text
- بيانات من شركات الصرافة ووكلاء الحوالات تفصل تسليم الحوالات عن تصريف العملات، بحسب المنطقة؛
```

### S6 · s7 — closing sentence: ambiguous attachment and a broken house formula

Current:

```text
يعدّ الدليل البالغين وقيود القوائم والأسعار، لكنه لا يرصد أموال الأسر نفسها. فلا يُظهر حصة الحوالات من النقد الذي تتلقاه الأسر، ولا كيف استلم المتلقون أموالهم في موجة 2021، ولا ما إذا كان البالغون الذين تلقوا الأموال هم أنفسهم من لا يملكون حسابًا. ولا يثبت أن شركات الصرافة تحل محل البنوك، ولا أن اتساع شبكة الصرافة أدى إلى زيادة الحوالات، ولا أن قواعد أي سلطة أنتجت هذا النمط. وقيمة القناة الغائبة غير معروفة — لا يعني ذلك صفرًا.
```

Problems:
- «قيمة القناة الغائبة»: «الغائبة» can agree with «القناة», which gives "the value of the missing channel". The English is "a channel value that is missing".
- «— لا يعني ذلك صفرًا» is a loose tag whose referent is unclear. The house formula is «غير معروف — ولا يعني صفرًا» (ARABIC_HOUSE_STYLE).

Corrected:

```text
يعدّ الدليل البالغين وقيود القوائم والأسعار، لكنه لا يرصد أموال الأسر نفسها. فلا يُظهر حصة الحوالات من النقد الذي تتلقاه الأسر، ولا كيف استلم المتلقون أموالهم في موجة 2021، ولا ما إذا كان البالغون الذين تلقوا الأموال هم أنفسهم من لا يملكون حسابًا. ولا يثبت أن شركات الصرافة تحل محل البنوك، ولا أن اتساع شبكة الصرافة أدى إلى زيادة الحوالات، ولا أن قواعد أي سلطة أنتجت هذا النمط. والقيمة الغائبة لأي قناة غير معروفة — ولا تعني صفرًا.
```

### S7 · CCY-ISP-2024 · `summary_ar` — 30 words between «وجد» and «أن»; "largest share" of what

Current:

```text
وجد مسح أجراه تحالف النقد في اليمن في يونيو 2024 على أسر تتلقى مساعدات نقدية متعددة الأغراض في ثلاث عُزل تخضع لإدارة الحكومة المعترف بها دوليًا (المظفر في تعز، وقعطبة في الضالع، وتُبن في لحج) أن المساعدات شكّلت معظم الدخل النقدي لهذه الأسر، وأن قعطبة سجّلت أكبر حصة (68%). وجاءت القروض من شبكات الدعم غير الرسمية في المرتبة الثانية في المظفر (47%) وقعطبة (26%)، وكانت الهدايا أصغر الحصص في المواقع الثلاثة. وفي المظفر أفادت 26% من الأسر بأن قدرتها على تقديم الدعم لشبكاتها ازدادت بعد تلقي المساعدات، مقابل 4% أفادت بازدياد قدرتها على تلقي الدعم.
```

Problems:
- The finding is far from its verb, the same problem as ARABIC_6A S13.
- «أجراه تحالف» states a role, while the English possessive "A CCY survey" does not. The data were collected by CCY partners (method field).
- «أكبر حصة (68%)» does not say whose share it is. The 68% is the *assistance* share.
- The English "collected in June 2024" is kept as «جُمعت بياناته».

Corrected:

```text
وفق مسح لتحالف النقد في اليمن جُمعت بياناته في يونيو 2024 من أسر تتلقى مساعدات نقدية متعددة الأغراض في ثلاث عُزل تخضع لإدارة الحكومة المعترف بها دوليًا (المظفر في تعز، وقعطبة في الضالع، وتُبن في لحج)، شكّلت المساعدات معظم الدخل النقدي لهذه الأسر، وسجّلت قعطبة أكبر حصة للمساعدات (68%). وجاءت القروض من شبكات الدعم غير الرسمية في المرتبة الثانية في المظفر (47%) وقعطبة (26%)، وكانت الهدايا أصغر الحصص في المواقع الثلاثة. وفي المظفر أفادت 26% من الأسر بأن قدرتها على تقديم الدعم لشبكاتها ازدادت بعد تلقي المساعدات، مقابل 4% أفادت بازدياد قدرتها على تلقي الدعم.
```

### S8 · CCY-ISP-2024 · `method_ar` — authorship added; "figure labels" unclear

Current:

```text
مسح أسري أجراه شركاء تحالف النقد في اليمن باستخدام مؤشر الحماية الاجتماعية غير الرسمية الذي وضعته منظمة ميرسي كور؛ وتقارن الدراسة الدخل النقدي الذي تفيد به الأسر بمبلغ المساعدة (240,000 ريال يمني). والقيم هي المطبوعة في نص التقرير (ص 9)، لا تسميات الشكل؛ ومجموع الحصص الأربع لكل موقع يتجاوز 100%، فلا تُجمع ولا تُقارن بين الفئات.
```

Problems:
- "Mercy Corps's Index" is a possessive. «الذي وضعته» ("which it designed") adds an authorship claim that the English does not make. Use «التابع لمنظمة ميرسي كور». A Latin gloss is added at first mention, as with CCY.
- «تسميات الشكل» ("the figure's names/captions") does not say *data labels*. The point is that the 68% / 47% / 26% come from the text, not from the 68.2% / 46.6% / 26.1% bar labels. Use «لا القيم المدوّنة على الشكل البياني».

Corrected:

```text
مسح أسري أجراه شركاء تحالف النقد في اليمن باستخدام مؤشر الحماية الاجتماعية غير الرسمية التابع لمنظمة ميرسي كور (Mercy Corps)؛ وتقارن الدراسة الدخل النقدي الذي تفيد به الأسر بمبلغ المساعدة (240,000 ريال يمني). والقيم هي المطبوعة في نص التقرير (ص 9)، لا القيم المدوّنة على الشكل البياني؛ ومجموع الحصص الأربع لكل موقع يتجاوز 100%، فلا تُجمع ولا تُقارن بين الفئات.
```

### S9 · CCY-ISP-2024 · `currentness_ar` — "lists it as posted" becomes "says it was published"

Current:

```text
جُمعت البيانات في يونيو 2024؛ ولا يحمل التقرير تاريخًا مطبوعًا، ويذكر موقع ReliefWeb أنه نُشر في 14 نوفمبر 2024 (جرى التحقق في 11 أكتوبر 2026).
```

Problem: the English separates the report's (unprinted) date from ReliefWeb's *posting* date. «أنه نُشر في 14 نوفمبر 2024» attributes a publication date to the report. Keep it to the posting on that site.

Corrected:

```text
جُمعت البيانات في يونيو 2024؛ ولا يحمل التقرير تاريخًا مطبوعًا، ويذكر موقع ReliefWeb أنه نُشر على الموقع في 14 نوفمبر 2024 (جرى التحقق في 11 أكتوبر 2026).
```

### S10 · CCY-SAM-2024 · `definition_ar` — ratio direction lost; «ومصادر الدخل» parses as a third term of «بين»

Current:

```text
النسبة التي تقدّرها الدراسة بين إجمالي النشاط الاقتصادي، بما فيه النقد المضخوخ، والمساعدات النقدية المضخوخة في كل منطقة، ومصادر الدخل الرئيسية التي أفادت بها الأسر التي شملها التقييم.
```

Problems:
- "ratio of A to B" has a direction. «النسبة بين A وB» does not, and the multiplier is A÷B.
- Because «بين» governs coordinated nouns, the trailing «ومصادر الدخل…» reads naturally as a third term of the ratio. «نسبة A إلى B» fixes both problems.

Corrected:

```text
نسبة إجمالي النشاط الاقتصادي، بما فيه النقد المضخوخ، إلى المساعدات النقدية المضخوخة في كل منطقة، كما تقدّرها الدراسة، ومصادر الدخل الرئيسية التي أفادت بها الأسر التي شملها التقييم.
```

### S11 · CCY-SAM-2024 · `period_ar` — "also" dropped

Current:

```text
آخر توزيع للمساعدات بين أكتوبر وديسمبر 2023؛ والمسح الأسري في يناير 2024 (ويذكر التقرير يناير 2023 في موضع واحد)
```

Problem: "(the report **also** gives January 2023 in one place)" marks an internal inconsistency in the report. Without «أيضًا», the bracket can read as a correction ("the report says January 2023"). This is the same class as ARABIC_6A S12.

Corrected:

```text
آخر توزيع للمساعدات بين أكتوبر وديسمبر 2023؛ والمسح الأسري في يناير 2024 (ويذكر التقرير أيضًا يناير 2023 في موضع واحد)
```

### S12 · CCY-SAM-2024 · `universe_ar` — «أعمال تجارية» and "rounds"

Current:

```text
قرى وبلدات مختارة من عزلة الضالع (محافظة الضالع) وعزلة جعار (مديرية خنفر، محافظة أبين) تلقت أكبر قدر من المساعدات وأمكن الوصول إليها: 291 مقابلة أسرية في الضالع و209 في جعار، مع أسر تلقت جولتين على الأقل، إضافة إلى أعمال تجارية محلية.
```

Problems:
- «أعمال تجارية» means "commercial activities". The interviews were with businesses, that is, firms, which the site calls «المنشآت». «إضافة إلى أعمال تجارية محلية» also loses the fact that these were interviews.
- «جولتين على الأقل من المساعدات» keeps assistance rounds apart from M6's spending rounds.

Corrected:

```text
قرى وبلدات مختارة من عزلة الضالع (محافظة الضالع) وعزلة جعار (مديرية خنفر، محافظة أبين) تلقت أكبر قدر من المساعدات وأمكن الوصول إليها: 291 مقابلة أسرية في الضالع و209 في جعار، مع أسر تلقت جولتين على الأقل من المساعدات، إضافة إلى مقابلات مع منشآت تجارية محلية.
```

### S13 · CCY-SAM-2024 · `meta_ar` — elliptical close «تقدير لا دخل»

Current:

```text
قدّرت دراسة تجريبية لتحالف النقد في اليمن عام 2024 نشاطًا قيمته 2.56 و2.29 دولار لكل دولار من المساعدات النقدية في قرى مختارة؛ تقدير لا دخل.
```

Problem: «تقدير لا دخل» opposes two things that are not of the same kind (an estimate against income) and has no subject. As a search snippet it reads as a fragment, the same fault as ARABIC_6A M2's «لا وصول اليوم». The English "an estimate, not income" means an estimate *of activity*, not of income.

Corrected (134 characters; the English is 146):

```text
قدّرت دراسة تجريبية لتحالف النقد في اليمن عام 2024 نشاطًا قيمته 2.56 و2.29 دولار لكل دولار من المساعدات النقدية في قرى مختارة؛ وهو تقدير للنشاط لا للدخل.
```

### S14 · Programme-level, not for this change — CCY's own Arabic name

The cover of the ISP report carries the consortium's own Arabic name, «إتحاد المساعدات النقدية في اليمن» (R5 §1.1). The site uses «تحالف النقد في اليمن» in 89 cells, which is a literal rendering, and the house style says «لا ترجمة حرفية للأسماء الرسمية». Do **not** change it in CWR-012 alone, because that would leave two names on the site. Record this for a site-wide naming decision. If adopted, write it «اتحاد المساعدات النقدية في اليمن» (hamzat wasl, no hamza on the alif) and keep the Latin gloss at first mention.

---

## NIT

**N1 · s8, first bullet.** The site form is «المناطق التي شملها المسح» (402 cells); «المشمولة بالمسح» has 0.

```text
- الوحدة: البالغون في المناطق التي شملها المسح، لا الأسر ولا الحسابات؛
```

**N2 · s5, "Survey coverage" bullet.** "smaller samples **still**" means even smaller samples, and «أصغر» on its own loses the comparison.

```text
- تغطية المسح: أجرى المسح مقابلات مع 1,000 من البالغين، ويستبعد إطاره محافظات البيضاء والجوف ومأرب وصعدة وسقطرى وعددًا من المديريات في محافظات أخرى، وهي مناطق تضم نحو 23% من السكان. وقد يصل المال إلى الأسر فيها بطرق مختلفة، ولا تقول النسب عنها شيئًا؛ كما تستند قيم الفئات إلى عينات أصغر من ذلك.
```

**N3 · s5, "What 'remittance' means" bullet.** «فالثلاثة» has no noun. «فالمعاني الثلاثة تشترك في اللفظ» states what the three are and avoids repeating «الكلمة/الحوالة».

```text
- معنى «الحوالة»: هي في المسح أموال أُرسلت أو استُلمت داخل اليمن بحسب إفادة البالغين، وهي في ميزان مدفوعات البنك المركزي اليمني – عدن تدفق عابر للحدود بالدولار الأمريكي، وهي في بيانات أسعار البنك الدولي منتج رسمي لإرسال المال إلى اليمن. فالمعاني الثلاثة تشترك في اللفظ لا في المقياس.
```

**N4 · CCY-SAM-2024 `currentness_ar`.** «موقع استضافته ضمن نوفمبر 2024» is compressed. The English means the host files it under November 2024 (the upload path).

```text
أُجري المسح الأسري في يناير 2024؛ ولا يحمل التقرير تاريخًا مطبوعًا، ويُدرجه الموقع الذي يستضيفه ضمن ملفات نوفمبر 2024 (جرى التحقق في 11 أكتوبر 2026).
```

**N5 · Accepted numeral forms (no change).** "2025 Q3" → «الربع الثالث من 2025» and "USD 1" → «دولار أمريكي واحد» / «لكل دولار» are the only remaining digit differences in the corrected set. Both are idiomatic, and neither carries a READ value.

**N6 · «دراسة تجريبية» for "pilot study" (no change).** This is the standard UN rendering. A reader could take «تجريبية» as "experimental", meaning a causal design. «دراسة أولية» is an alternative if the lead wants to remove that reading in both records, but switching is optional.

**N7 · Optional vowelling of place names.** «تُبَن» and «المظفَّر» are fully vowelled; the drafts' «تُبن» and «المظفر» are correct.

---

## Place names (CCY sites) — no defect

All nine names are spelled as in common Yemeni and official usage:
- المظفر (Taiz city)
- قعطبة (Al Dhale'e)
- تُبن (Lahj; the damma rules out «تِبن», "straw")
- الضالع
- جعار (town in Khanfar district, Abyan)
- خنفر (the report's "Khanfir" in fn 3 is its own slip; «خنفر» is correct)
- أبين
- لحج
- تعز

«عزلة/عُزل» renders the source's "sub-district" consistently, and «عزلتَي الضالع وجعار» is already the site's source title. See O5 on the administrative level.

## Bidi and mixed script — no defect after S2

- `evidence_period_ar` is the only field that opened with a Latin run. It renders correctly under the page's `dir="rtl"` (the `clock()` helper sets no `dir="auto"`), and S2 removes the problem.
- The following sit between Arabic runs and resolve RTL under the paired-bracket rule (N0), as in CWR-010:
  - «(Global Findex)»
  - «(Cash Consortium of Yemen)»
  - «(Mercy Corps)»
  - «ReliefWeb»
  - «FMIIP»
  - «/people/» (symmetric slashes, same form as page_specs)
- Percentages and decimals («(68%)»، «2.56 دولار»، «3,422.16»، «240,000 ريال يمني») follow site convention.
- «نوفمبر 2022 – يناير 2023» uses the spaced en dash between Arabic and digits, which resolves RTL.
- No LRM/RLM/isolate characters, Latin punctuation or Arabic-Indic digits are present.

## Outside Arabic scope (for the lead; if the English changes, the Arabic must follow)

- **O1 · s5 "Humanitarian cash", English.** "with informal loans and gifts behind it" omits earnings. ISP's Figure 4 shows earnings above gifts at every site and about equal to loans in Tuban, and loans came second in only two sites (R5 §1.3). Suggested EN: "…the assistance made up most of the recipients' cash income, with informal loans second in two of them and gifts the smallest share in all three". AR then: «…شكّلت المساعدات معظم الدخل النقدي للمستفيدين، وجاءت القروض غير الرسمية ثانيةً في اثنتين منها، والهدايا أصغر الحصص فيها جميعًا».
- **O2 · CCY-SAM `summary_en`.** "using one social accounting matrix" contradicts `method_en`, which says "a single social accounting matrix for each locality" (the source built one SAM per sub-district). Suggested: "using a single social accounting matrix for each locality". The AR change is noted under S1.
- **O3 · s5, English.** "in Ad-Dali and Ja'ar" is unqualified. Ad-Dali is also a governorate, and the SAM universe is selected villages. Suggested: "in selected villages of Ad-Dali and Ja'ar sub-districts". AR: «في قرى مختارة من عزلتَي الضالع وجعار».
- **O4 · CCY-ISP `universe_en`.** "bi-monthly" is ambiguous in English (twice a month or every two months), and the Arabic had to choose «كل شهرين». Confirm the intended sense. If it is "every two months", write that in the English.
- **O5 · "sub-district" for Al Mudhaffar, Qa'tabah and Tuban.** These names are also Yemen's *districts* (مديريات), and a Yemeni reader may take «عُزل» for a mistake. SAM states its levels (fn 2–3), but ISP does not. Consider "three areas the study calls sub-districts" in `universe_en`. AR: «ثلاث مناطق تسميها الدراسة عُزلًا».
- **O6 · CCY-SAM `limitations_en`.** "support from family" narrows the source category "Loans or support from family, friends, neighbours". Suggested: "remittances and loans or support from family, friends and neighbours carry no printed value". AR: «ولا تحمل الحوالات والقروض أو الدعم من الأسرة والأصدقاء والجيران أي قيمة مطبوعة».
- **O7 · CCY-ISP `method_en`.** "the four shares for a site add to more than 100%" rests on the Figure 4 bar labels, which R5 marks **[image]**, meaning a second reader must confirm them. The record itself binds only the text values. The steward should confirm the image read or reword the clause to "the report's figure shows shares that add to more than 100%".

ARABIC: PASS
