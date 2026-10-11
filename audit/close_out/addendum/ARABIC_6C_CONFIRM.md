# CLOSE-6C — Arabic confirmation pass on CWR-012 v2

Input: `c6c/CWR-012_review_bundle.md` (v2, as applied), cross-checked against `close_6c_text.py` / `close_6c_records.py`, VIS-PAYMENT-RAILS `summary_ar`, CLM-016 `limitations_ar`, VIS-REMITTANCE-COST and the terminology register. Read only; nothing in the repository was changed. Earlier SHOULD-FIX items S1–S13 were also re-read and all landed.

## Earlier MUST-FIX: did each fix land?
- **M1 LANDED** (Thesis and s1): «ولا تتضمن قاعدة الأدلة أي قيمة لقنوات الحوالات في تلك الموجة».
- **M2 LANDED** (s2): «من المؤشر العالمي للشمول المالي (Global Findex) التابع للبنك الدولي، وهي الموجة الخاصة باليمن».
- **M3 LANDED** (s5): «ما قد يبلغه حجم هذا الطريق حيث يعمل».
- **M4 LANDED** (ISP limitations): «فالدراسة لا تورد قناةً ولا تكرارًا ولا مبلغًا، ولا توزيعًا للدعم بين ما يأتي من داخل اليمن وما يأتي من خارجه».
- **M5 LANDED** (SAM limitations): «المضاعفان تقديران مستخرجان من نموذج … يشمل التحويل النقدي نفسه».
- **M6 LANDED** (SAM method): «آثار الجولة الأولى من الإنفاق» and «ولا تُنشر له فترة ثقة ولا مدى».

## New Arabic that checks out (no change needed)
- **Question, Thesis and s1:** the comparative «أكثر مما تنتقل عبر الحسابات» and «مقدمي خدمات تحويل الأموال» (TERM-003) are sound. «وتحدّ تغطيةُ المسح والعملةُ ومعنى «الحوالة» مما تُظهره» is grammatical, and its pronoun refers to «الأرقام».
- **s3:**
  - The roster-scope sentence names both central banks neutrally.
  - The CLM-016 wording matches the governed cell verbatim.
  - The 26 June 2024 paragraph uses VIS-PAYMENT-RAILS's terms exactly («شركات ومنشآت الصرافة ووكلاء الحوالات»، «الحوالات النقدية الداخلية الجديدة حصرًا»، «الشبكة الموحدة للحوالات المالية»).
- **s5:** «بتعبير الدراسة» and the ranking «ثانيةً في منطقتين من الثلاث» are correct.
- **s6:** «وفي ميزان المدفوعات، تعطي…», the UAE corridor (consistent with VIS-REMITTANCE-COST's «يرفع عرضٌ واحد») and «ولم تُحدَّد هنا التغطية الجغرافية» are correct.
- **s8 and the route meta:** «لم تُقَس» is the correct passive jussive.
- **Records:** «تسميها الدراسة عُزلًا», the SAM reordering, and «بما فيه المساعدات نفسها» are correct.

## NEW findings (changed Arabic only)
**SHOULD-FIX**
**C-S1 · `evidence_period_ar` — «قاعدة … للحوالات الداخلية» reads as "the CBY's domestic-remittance base/database".** On a page that says «قاعدة الأدلة» throughout, this is a real misreading. The instrument is a decision («قرار المحافظ رقم (23)», 146 cells), and s3 itself says «قرار». Corrected:
```text
المؤشر العالمي للشمول المالي (Global Findex) 2021، العمل الميداني في اليمن نوفمبر 2022 – يناير 2023 · الملف القطري للبنك الدولي لعام 2014 · قائمة البنك المركزي اليمني – عدن لعام 2026 · قرار البنك المركزي اليمني – عدن بشأن الحوالات الداخلية الصادر في يونيو 2024 · أسعار الحوالات لعام 2023 والربع الثالث من 2025 · التقريران السنويان للبنك المركزي اليمني – عدن 2024 و2025 · دراستا تحالف النقد في اليمن (Cash Consortium of Yemen) عن متلقي المساعدات (بيانات مسوح يناير ويونيو 2024)
```
**C-S2 · s5 «طرق أخرى» — "also" is dropped, and "had an account" becomes present tense.** «يملكون» states account ownership *now*, but the 11.9% is ownership at fieldwork. The Thesis uses «كان لدى». Corrected:
```text
- طرق أخرى: قد تنتقل الأموال أيضًا باليد أو مع المسافرين أو عبر مقدمي خدمات غير شركات الصرافة، وقد يكون بعض المتلقين ضمن نسبة 11.9% من البالغين الذين كان لديهم حساب؛ ولا تفصل قيم المسح بين هذه الطرق.
```
**C-S3 · ISP `summary_ar` — «في مناطق الحكومة المعترف بها دوليًا».** This form has 0 cells on the site, it is colloquial, and it repeats «مناطق … مناطق». The house form is «في المناطق الخاضعة للحكومة المعترف بها دوليًا» (258 cells). Corrected:
```text
وفق مسح لتحالف النقد في اليمن جُمعت بياناته في يونيو 2024 من أسر تتلقى مساعدات نقدية متعددة الأغراض في ثلاث مناطق تسميها الدراسة عُزلًا وتقول إنها تقع في المناطق الخاضعة للحكومة المعترف بها دوليًا (المظفر في تعز، وقعطبة في الضالع، وتُبن في لحج)، شكّلت المساعدات معظم الدخل النقدي لهذه الأسر، وسجّلت قعطبة أكبر حصة للمساعدات بين المناطق الثلاث (68%). وجاءت القروض من شبكات الدعم غير الرسمية في المرتبة الثانية في المظفر (47%) وقعطبة (26%)، وكانت الهدايا أصغر الحصص في المناطق الثلاث. وفي المظفر أفادت 26% من الأسر بأن قدرتها على تقديم الدعم لشبكاتها ازدادت بعد تلقي المساعدات، مقابل 4% أفادت بازدياد قدرتها على تلقي الدعم.
```
**C-S4 · SAM `summary_ar` — same house-form issue as C-S3, plus about 30 words between «بأن 61%» and its verb «ذكرت».** The fix moves the appositive after the finding. The meaning and every hedge are unchanged. Corrected:
```text
تفيد دراسة تجريبية لتحالف النقد في اليمن عام 2024 بأن 61% في المتوسط من الأسر التي شملها التقييم في قرى مختارة من الضالع وجعار ذكرت المساعدات النقدية مصدرًا رئيسيًا للدخل خلال 30 يومًا سبقت المقابلة، وأن 55% ذكرت العمل العرضي أو بالأجر اليومي؛ والضالع وجعار منطقتان تسميهما الدراسة عزلتين وتقول إنهما تقعان في المناطق الخاضعة للحكومة المعترف بها دوليًا. وتشير الدراسة إلى أن بعض المستجيبين لم يحتسبوا ما تلقوه عن طريق «الحوالة» (بتعبير الدراسة) ولا الديون دخلًا. وباستخدام مصفوفة محاسبة اجتماعية واحدة لكل منطقة، بُنيت من مسح لأسر تتلقى مساعدات نقدية متعددة الأغراض ومقابلات مع أصحاب أعمال محليين، قدّرت الدراسة أن كل دولار أمريكي واحد من المساعدات أنتج نشاطًا اقتصاديًا قيمته 2.56 دولار، بما فيه التحويل النقدي نفسه، في قرى الضالع، و2.29 دولار في قرى جعار، وتذكر أن القيمتين لا تقبلان المقارنة المباشرة.
```
**NIT**
**C-N1 · s3, rule paragraph.** The English "a rule is not evidence" is generic, but the definite «ووجود القاعدة» narrows it to this rule. Corrected:
```text
ومنذ 26 يونيو 2024 يُلزم قرار صادر عن البنك المركزي اليمني – عدن شركات ومنشآت الصرافة ووكلاء الحوالات بتنفيذ الحوالات النقدية الداخلية الجديدة حصرًا عبر الشبكة الموحدة للحوالات المالية. وهذا القرار لاحق للعمل الميداني للمسح، ووجود قاعدة لا يدل بذاته على كيفية انتقال الحوالات فعليًا.
```
**C-N2 · s4 «الملف المتاح هنا».** "held here" is about holdings, not availability (see ARABIC_6A S2). Replace only the fragment «ولا يبيّن الملف المتاح هنا كيف تلقى الباقون أموالهم» with «ولا يبيّن الملف الوارد في قاعدة الأدلة هذه كيف تلقى الباقون أموالهم».
**C-N3 · s7 «زيادة … زيادة».** The repeated noun is avoidable. Replace only the fragment «ولا أن زيادة منافذ الصرافة أدت إلى زيادة الحوالات» with «ولا أن ازدياد منافذ الصرافة أدى إلى زيادة الحوالات».
**C-N4 · SAM `universe_ar` «منطقتي».** Unvowelled, it can be read as "my area" (ARABIC_6A N3). Replace «من منطقتي الضالع» with «من منطقتَي الضالع».
**C-N5 · s9, third bullet.** The English says "their supervisor", and «الجهة الرقابية» drops "their". Corrected:
```text
- أرقام منشورة، من شركات الصرافة أو وكلاء الحوالات أو الجهة الرقابية عليها، تفصل تسليم الحوالات عن تصريف العملات، بحسب المنطقة؛
```

## Numeral parity
I compared the digits in 37 EN–AR pairs: 33 Reading and record fields mechanically, plus the route meta by hand. There is **0 value drift**. The only differences are the four accepted word forms from the first pass: "2025 Q3" → «الربع الثالث» (evidence period and s6), and "USD 1" → «دولار أمريكي واحد» / «لكل دولار» (SAM summary and meta). "30" is now printed in digits. All corrected strings above have the same digits as their English. The spelling and bidi scan found no hamza slips, Latin punctuation, bidi control characters or Arabic-Indic digits. The new mixed runs («26 يونيو 2024»، «(… 7.53%، …)»، «(بتعبير الدراسة)») resolve RTL.

## Final check (regenerated bundle)
- **C-S1 to C-S4 landed exactly as written.** C-S1 is in the evidence period («قرار البنك المركزي اليمني – عدن بشأن الحوالات الداخلية الصادر في يونيو 2024»), C-S2 in «طرق أخرى» («أيضًا»، «كان لديهم حساب»), C-S3 in the ISP summary («المناطق الخاضعة للحكومة المعترف بها دوليًا»; only «في محافظة الضالع» was added since), and C-S4 in the SAM summary, which is verbatim.
- **1 · Route meta: sound.** «ولا تتضمن قاعدة الأدلة قيمة لقنوات الحوالات في تلك الموجة» has the same meaning as "no channel value for that wave is held here", and it matches the Thesis.
- **2 · s3 rule sentence: sound.** The past tense «ألزم» matches "required". «الخاضعين لرقابته» renders "under its supervision"; its pronoun refers naturally to the bank, and the masculine plural is correct because the list includes «وكلاء». The generic «ووجود قاعدة» (C-N1) is kept.
- **3 · ISP summary: sound.** «وقعطبة في محافظة الضالع» matches "Ad-Dali governorate", and the English has the same asymmetry with Taiz and Lahj.
- **4 · SAM meta: SHOULD-FIX (F-S1).** «الأسر المقيَّمة» reads as «المقيمة» ("resident households") wherever the shadda is lost, for example in snippets or when a reader skims. «المشمولة» means the same as "assessed" here and keeps the length at 192 characters. Corrected:
  `دراسة تجريبية لتحالف النقد في اليمن عام 2024: ذكرت 61% من الأسر المشمولة، في المتوسط، المساعدات مصدرًا رئيسيًا للدخل؛ والنشاط المقدَّر 2.56 و2.29 دولار لكل دولار، بما فيه المساعدات، لا الدخل.`
- **Numeral parity (re-run on the regenerated bundle):** 0 value drift. The only differences are the four accepted word forms ("2025 Q3" twice, "USD 1" twice). The SAM meta has the same digits as its English, apart from "USD 1".

## Alias 001 (boundary note)
- **Meaning matches the English.** The note now says the evidence base holds one law, «قانونًا واحدًا … هو قانون مؤسسة ضمان الودائع المصرفية», which matches the /data/ line. «لوائحها…» refers back to the evidence base, as "Its" does. «أصدرها … أو نشرها» = "issued or posted", and «عدا تعميم واحد» = "except one circular".
- **SHOULD-FIX (A-S1), naming.** The house form for the Sana'a bank, set in ARABIC_6A, is «البنك المركزي اليمني في صنعاء» (73 cells). The note uses «البنك المركزي اليمني – صنعاء», a form found in only 5 cells, which puts the two banks side by side as if they had parallel names. Corrected:
  `أداة اكتشاف فقط: تضم قاعدة الأدلة هذه قانونًا واحدًا بوصفه وثيقة مصدرية، هو قانون مؤسسة ضمان الودائع المصرفية. أما لوائحها وتعاميمها وقراراتها وقوائمها الرسمية فقد أصدرها البنك المركزي اليمني – عدن أو نشرها، عدا تعميم واحد للبنك المركزي اليمني في صنعاء. وجميعها مدرجة في صفحة البيانات والمصادر.`
- **Outside Arabic scope.** The English "Central Bank of Yemen – Sana'a" should follow the site's "Central Bank of Yemen in Sana'a". The note has no digits, so there is nothing to check for parity.

ARABIC: PASS
