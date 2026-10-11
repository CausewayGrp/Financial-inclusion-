# Red-team review: CLOSE-6C, Reading CWR-012 "How money reaches households" and records CCY-ISP-2024 and CCY-SAM-2024

- **Reviewed:** `scratchpad/c6c/CWR-012_review_bundle.md` (EN, AR, bindings and both records as they will be applied). Line numbers (`L…`) refer to that file.
- **Evidence used:**
  - `addendum/reads/R5_ccy_isp_sam.md`;
  - `addendum/txt_r5/` and `addendum/img_r5/isp-01.png`;
  - the governed records in `site-src/content/evidence/evidence_objects.json` (CLM-026, VIS-FINDEX-FLOW-CHANNELS, CLM-030, CLM-009, CLM-016, VIS-REMITTANCE-COST, CLM-032, plus CLM-007 and VIS-PAYMENT-RAILS for context);
  - `source_library.json`, `readings.json`, `navigation_interaction.json` and `authority/CORE_CONSTITUTION.md`.
- **Readers:** each finding names its reader: **EXCHANGE** (compliance head at a licensed exchange company), **CBY** (a statistician or supervisor at either central bank) or **EVIDENCE** (a methodologist).
- **Scope:** nothing under the repository was modified.

**Counts:** 3 BLOCKER · 15 SHOULD-FIX · 12 NIT.

---

## BLOCKER

### B1 [EXCHANGE]: the hypothesis routes "informal transfers" through licensed exchange companies

- **Quote:**
  - EN s4 (L21): "that remittances, including informal transfers between households, are a main channel through which many households receive cash, and that this money travels mainly through exchange companies rather than through accounts."
  - AR s4 (L69): «الحوالات، بما فيها الأموال المرسلة بين الأسر بطرق غير رسمية، قناة رئيسية … وأن هذه الأموال تمر أساسًا عبر شركات الصرافة».
- **Evidence:**
  - "This money" includes the "informal transfers", so the sentence says informal transfers travel through exchange companies.
  - The Reading's own s6 (L30) treats exchange-company products as formal: the World Bank prices are "formal products … they do not cover informal channels".
  - The governed record VIS-PAYMENT-RAILS (on /reforms/) states that CBY-Aden Governor's Decision No. 23 of 2024 requires "exchange companies, exchange establishments and money-transfer agents to execute new domestic cash transfers only through the unified money-transfer network (26 June 2024)".
  - The Findex domestic-remittance indicator has no formal or informal classification.
- **Failure:**
  - The Reading internally contradicts itself and goes beyond its source.
  - A licensed exchange company can reasonably read it as calling its regulated transfers "informal", which also implies they sit outside the supervised system.
  - The same framing is carried by "money sent between households" in the Thesis and s1 (L6, L10).
- **Replacement:**
  - EN s4: "…that transfers from relatives and friends are a main channel through which many households receive cash, and that this money moves more through exchange companies and other money-transfer providers than through accounts."
  - AR s4: «…أن الأموال التي يرسلها الأقارب والأصدقاء قناة رئيسية تتلقى عبرها أسر كثيرة النقد، وأن هذه الأموال تنتقل عبر شركات الصرافة وغيرها من مقدمي خدمات تحويل الأموال أكثر مما تنتقل عبر الحسابات.»
  - Do not use "informal" for anything that passes through a licensed provider. Keep "informal" only in s6, for channels outside RPW's formal products.

### B2 [EVIDENCE]: "mainly through exchange companies" overreaches the only channel evidence the Reading cites

- **Quote:**
  - Question (L5): "mainly through exchange companies rather than through accounts". AR L53: «أساسًا».
  - Thesis and s1 (L6, L10): "consistent with the hypothesis that money … travels mainly through exchange companies rather than accounts". AR L54, L58: «تمر أساسًا».
  - s4 (L21): "mainly … in 2014, recipients named a money transfer operator far more often than a financial institution".
- **Evidence:**
  - CLM-030 (Little Data Book 2015, printed p. 160) gives 31.1% of recipients via a money transfer operator and 2.0% via a financial institution.
  - In the one source with channel values, about three in ten recipients named an MTO. The profile held here does not show how the other recipients received money.
  - s4 itself concedes that "a money transfer operator in the survey is not necessarily an exchange company".
  - The 2021 wave holds no channel value (VIS-FINDEX-FLOW-CHANNELS limitations).
- **Failure:**
  - The word "mainly" means "for the most part". The cited evidence does not support that, and the 2014 values lean against it.
  - So "consistent with" is an overreach: the bound evidence supports a comparative statement (more by MTO than by financial institution), not "mainly".
  - The hypothesis appears in the Question, Thesis, s1 and s4 in both languages.
- **Replacement:**
  - EN Question: "Does money sent between people in Yemen reach households more through exchange companies than through accounts?"
  - EN Thesis and s1: "…consistent with the hypothesis that money sent between people moves more through exchange companies and other money-transfer providers than through accounts, but it is a hypothesis: …"
  - EN s4, second sentence: "…in 2014, about three in ten recipients named a money transfer operator and 2.0% a financial institution, and the profile held here does not show how the others received money; …"
  - AR Question: «هل تصل الأموال المرسلة بين الأفراد في اليمن إلى الأسر عبر شركات الصرافة أكثر مما تصل عبر الحسابات؟»
  - AR Thesis and s1: «…ويتسق ذلك مع فرضية أن الأموال المرسلة بين الأفراد تنتقل عبر شركات الصرافة وغيرها من مقدمي خدمات تحويل الأموال أكثر مما تنتقل عبر الحسابات، لكنه يبقى فرضية: …»
  - AR s4: «…وفي 2014 ذكر نحو ثلاثة من كل عشرة متلقين مشغل تحويل أموال، و2.0% مؤسسة مالية، ولا يبيّن الملف المتاح هنا كيف تلقى الباقون أموالهم؛ …»

### B3 [CBY]: "for the economy as a whole" assigns CBY-Aden's balance-of-payments figure a territory the evidence base says is open

- **Quote:**
  - EN s6 (L30): "For the economy as a whole, CBY-Aden's annual reports give different values for the same year…"
  - AR s6 (L78): «وعلى مستوى الاقتصاد ككل، تورد التقارير السنوية للبنك المركزي اليمني – عدن…»
- **Evidence:**
  - CLM-032 `universe_en`: the series' "exact territorial and conceptual mapping to the IMF reconstruction for areas under the internationally recognized government remains open".
  - CLM-007 says the IMF series covers areas under the internationally recognized government and "is not a whole-of-Yemen figure".
- **Failure:**
  - This is an unsourced territorial claim. A statistician in Aden could contest it as wrong, because the coverage is not stated.
  - A supervisor in Sana'a could contest it as political loading, because it presents one authority's balance of payments as the whole economy's.
- **Replacement:**
  - EN: "In the balance of payments, CBY-Aden's annual reports give different values for the same year: … Neither value says how many households received money, or through which channel, and the territory these values cover has not been mapped here."
  - AR: «وفي ميزان المدفوعات، تورد التقارير السنوية للبنك المركزي اليمني – عدن قيمًا مختلفة للسنة نفسها: … ولا تبيّن أيٌّ من القيمتين عدد الأسر التي تلقت أموالًا ولا القناة التي وصلت عبرها، ولم تُحدَّد هنا التغطية الجغرافية لهذه القيم.»

---

## SHOULD-FIX

### S1 [EVIDENCE]: the "four other explanations" are mostly caveats, and the rival channels are missing

- **Quote:** s5 heading (L23): "Four other explanations fit the same numbers". Thesis (L6): "survey coverage, humanitarian cash, currency and the meaning of 'remittance' all fit the same numbers".
- **Failure:**
  - "Survey coverage" and "Currency" (L24, L26) are limits on the data, not rival explanations of the gap between recipients and account holders.
  - The obvious rivals to "through exchange companies" are absent:
    - money carried by hand or by travellers. Not verified here: the Findex 2021 domestic-remittance question is understood to count money "you brought yourself or sent in some other way", which should be checked against the questionnaire before it is cited;
    - account holders being among the recipients (s2 already allows this);
    - other providers;
    - wallets, which the survey did not ask about.
  - So the hypothesis is not set against real alternatives.
- **Replacement:**
  - Retitle s5 "Other explanations and limits" (AR «تفسيرات أخرى وحدود للأدلة»).
  - Add a first bullet. EN: "Other routes. Money may also travel by hand, with travellers or through providers other than exchange companies, and some recipients may be among the 11.9% who had an account; the survey values do not separate these routes."
  - AR: «طرق أخرى: قد تنتقل الأموال باليد أو مع المسافرين أو عبر مقدمي خدمات غير شركات الصرافة، وقد يكون بعض المتلقين ضمن نسبة 11.9% التي تملك حسابًا؛ ولا تفصل قيم المسح بين هذه الطرق.»
  - Mirror the change in the Thesis list.

### S2 [EXCHANGE / CBY]: "the network" collides with the Unified Network

- **Quote:** s3 heading (L16) "…and the network is listed, not measured". AR (L64) «والشبكة مُدرجة في قوائم لا مَقيسة».
- **Evidence:** «الشبكة الموحدة للحوالات المالية» is a governed term in VIS-PAYMENT-RAILS and CLM-018.
- **Failure:** In Arabic, «الشبكة» in a remittance context reads as the Unified Network. An exchange compliance head would read the heading as "the Unified Network is only a list".
- **Replacement:**
  - EN: "The channel evidence is old, and providers are listed, not measured".
  - AR: «أدلة القنوات قديمة، ومقدمو الخدمة مُدرجون في قوائم لا مَقيسون».

### S3 [EXCHANGE]: the governed domestic-transfer rule is left out of a Reading about domestic transfers

- **Quote:** none. s3 and s4 describe the supply side only through the roster.
- **Evidence:** VIS-PAYMENT-RAILS: Decision No. 23 of 2024 (26 June 2024) makes the unified network the only route for licensed providers' new domestic cash transfers.
- **Failure:**
  - Without this rule, the Reading suggests the licensed sector moves domestic money unsupervised.
  - The rule also post-dates the Findex fieldwork (November 2022 to January 2023), which a reader needs to know.
- **Replacement:**
  - Add to s3, and bind VIS-PAYMENT-RAILS. EN: "Since 26 June 2024, a CBY-Aden decision has required exchange companies, exchange establishments and money-transfer agents to execute new domestic cash transfers only through the unified money-transfer network. The rule post-dates the survey's fieldwork, and a rule is not evidence of how transfers actually move."
  - AR: «ومنذ 26 يونيو 2024 يُلزم قرار صادر عن البنك المركزي اليمني – عدن شركات الصرافة ومنشآتها ووكلاء الحوالات بتنفيذ الحوالات النقدية الداخلية الجديدة عبر الشبكة الموحدة للحوالات المالية حصرًا. والقرار لاحق للعمل الميداني للمسح، والقاعدة ليست دليلًا على كيفية انتقال الحوالات فعليًا.»
  - "2024" and "26 June 2024" need date states.

### S4 [CBY]: the roster's scope is not stated, though the Reading uses it for a Yemen-wide hypothesis

- **Quote:**
  - s3 (L18): "the official 2026 roster of the Central Bank of Yemen – Aden (CBY-Aden) lists 100 exchange companies…"
  - s4 (L21): "CBY-Aden lists … as separate licensed classes".
- **Failure:**
  - The roster is CBY-Aden's licensing list. No list from the Central Bank of Yemen in Sana'a is held here, and missing is not zero.
  - The house already states this kind of scope elsewhere: "these are CBY-Aden's rules, not those the Central Bank of Yemen in Sana'a has issued" (evidence_objects.json).
- **Replacement:**
  - EN, append to the s3 roster sentence: "The roster covers entities licensed by CBY-Aden; this evidence base holds no list from the Central Bank of Yemen in Sana'a, so these entries are not a count for all of Yemen."
  - AR: «وتشمل القائمة الجهات المرخّصة من البنك المركزي اليمني – عدن، ولا تتضمن قاعدة الأدلة هذه قائمة صادرة عن البنك المركزي اليمني في صنعاء، فلا تمثل هذه القيود عددًا لليمن كله.»

### S5 [CBY]: the records state control of territory as fact, in a different verb from the sources and the house style

- **Quote:**
  - CCY-ISP summary (L107): "three sub-districts administered by the internationally recognized government". AR (L108) «تخضع لإدارة الحكومة المعترف بها دوليًا».
  - CCY-SAM summary (L215): "both administered by the internationally recognized government". AR (L216) «وكلتاهما تخضع لإدارة الحكومة…».
- **Evidence:**
  - The sources say "IRG-controlled" (ISP p. 5) and "under the control of" (SAM p. 1).
  - The house style is "areas under the internationally recognized government" (CLM-007 and others).
  - Qa'tabah lies near front lines (general knowledge, not verified here).
- **Failure:** The records make an unattributed territorial assertion in their own voice.
- **Replacement:**
  - EN: "…in three sub-districts that the study places in areas under the internationally recognized government".
  - AR: «…في ثلاث مناطق تقول الدراسة إنها تقع في مناطق الحكومة المعترف بها دوليًا».
  - SAM: "…both in areas that the study places under the internationally recognized government". AR: «وكلتاهما في مناطق تقول الدراسة إنها تحت سيطرة الحكومة المعترف بها دوليًا».

### S6 [EVIDENCE / AR]: «عزلة» ("sub-district") misnames Yemeni districts

- **Quote:**
  - ISP title and summary (L106, L108): «ثلاث عُزل (المظفر…قعطبة…تُبن)».
  - SAM (L214, L216, L222): «عزلة الضالع»، «عزلة جعار».
  - Reading s5 AR (L73): «ثلاث عُزل».
- **Evidence:**
  - SAM fn 2 says "Ad-Dali district" and fn 3 says "Khanfir district" (R5 §2.2).
  - Al Mudhaffar, Qa'tabah and Tuban are districts (مديريات), and Ja'ar is a town in Khanfar district. This is general knowledge, not checked against a gazetteer.
- **Failure:** «عزلة» is a specific administrative level, so a Yemeni reader sees a wrong unit.
- **Replacement:**
  - EN: "three areas the study calls sub-districts" (once, then "areas").
  - AR: «ثلاث مناطق تسميها الدراسة «عُزلًا»» and «منطقة الضالع» / «منطقة جعار (مديرية خنفر)».

### S7 [EVIDENCE]: s5 misstates the ranking of income sources in ISP

- **Quote:**
  - EN (L25): "the assistance made up most of the recipients' cash income, with informal loans and gifts behind it".
  - AR (L73): «تليها القروض والهدايا غير الرسمية».
- **Evidence:** ISP p. 9: loans were second in Al Mudhaffar and Qa'tabah; "loans and earnings were approximately equal in Tub[a]n"; "Gifts comprised the lowest proportion … in all three".
- **Failure:** The wording leaves out earnings and puts gifts next in line, when gifts were last.
- **Replacement:**
  - EN: "…made up most of the recipients' cash income; loans from informal networks came second in two of the three areas, and gifts were the smallest share in all three".
  - AR: «…شكّلت المساعدات معظم الدخل النقدي للمستفيدين، وجاءت القروض من الشبكات غير الرسمية ثانيةً في منطقتين من الثلاث، وكانت الهدايا أصغر الحصص فيها جميعًا».

### S8 [EVIDENCE / EXCHANGE, EN–AR parity]: "hawala transfers" and «الحوالات» do not say the same thing

- **Quote:**
  - EN s5 (L25): "some respondents did not count hawala transfers as income at all". AR (L73): «لم يحتسب بعض المستجيبين الحوالات دخلًا أصلًا».
  - The same pair appears in the SAM summary (L215–216).
- **Evidence:** SAM p. 36: "different interpretations of what constitutes income (i.e., hawala and debt not considered as income)".
- **Failure:**
  - In this Reading, «الحوالات» is the word for Findex "remittances", so the Arabic says that some respondents did not count remittances. That is broader than the English.
  - The English "hawala" signals an unlicensed system to a compliance reader.
  - The respondents were in the study's selected villages, not in the two areas as a whole.
- **Replacement:**
  - EN: "in the study's sample in Ad-Dali and Ja'ar, some respondents did not count money received by 'hawala' (the study's word) as income".
  - AR: «وفي عينة الدراسة في الضالع وجعار لم يحتسب بعض المستجيبين ما تلقوه عن طريق «الحوالة» (بتعبير الدراسة) دخلًا».

### S9 [EVIDENCE]: the unit of the SAM income-source shares is ambiguous

- **Quote:**
  - L215: "the main income sources … were the cash assistance (61%) and casual or daily wage labour (55%)".
  - AR (L216): «…المساعدات النقدية (61%) والعمل بالأجر اليومي أو العرضي (55%)».
- **Failure:** The values can be read as shares of income. They are shares of households reporting each source (Figure 5, "Reported HH income sources … per sub-district"), and they add to more than 100%.
- **Replacement:**
  - EN: "the study reports that, on average, 61% of the households assessed named the cash assistance as a main income source in the 30 days before the interview, and 55% casual or daily wage labour".
  - AR: «تفيد الدراسة بأن 61% من الأسر التي شملها التقييم، في المتوسط، ذكرت المساعدات النقدية مصدرًا رئيسيًا للدخل في الأيام الثلاثين السابقة للمقابلة، و55% العمل بالأجر اليومي أو العرضي».

### S10 [EVIDENCE]: the multiplier record leads with a value the remittances page cannot use

- **Quote:** CCY-SAM title (L213): "The estimated multiplier of cash assistance…", with `public_routes` /remittances/ (L212).
- **Evidence:**
  - Its own limitation (L225) says the multipliers "say nothing about how money reaches households".
  - R5 §0.4: the multiplier "belongs on a cash or humanitarian surface rather than in this Reading".
  - CORE_CONSTITUTION, "Product boundary" and "Counterfactual deletion test".
  - The Reading uses only the income-source and hawala points from this study.
- **Failure:** The record's headline value is off the route's question, which invites a reader to put the multiplier next to the remittance figures.
- **Replacement:** Retitle the record to lead with what the Reading uses. EN: "Income sources reported by cash-assistance households, with a multiplier estimate, in selected villages of Ad-Dali and Ja'ar (CCY pilot study, 2024)". AR: «مصادر الدخل التي أفادت بها أسر تتلقى مساعدات نقدية، مع تقدير للمضاعف، في قرى مختارة من الضالع وجعار (دراسة تجريبية لتحالف النقد في اليمن، 2024)». Alternatively, move the multiplier to the cash surface where CWR-010 sits (/reforms/).

### S11 [EVIDENCE]: the SAM `meta` drops "the transfer included"

- **Quote:**
  - `meta_en` (L324): "estimated USD 2.56 and 2.29 of activity per USD 1 of cash aid in selected villages; an estimate, not income."
  - `meta_ar` (L325).
- **Failure:** The meta is the text shown on cards and in search. Without "the aid itself included", 2.56 reads as 2.56 of additional activity.
- **Replacement:**
  - EN: "…estimated USD 2.56 and 2.29 of activity, the aid itself included, per USD 1 of cash aid in selected villages; an estimate, not income."
  - AR: «…نشاطًا قيمته 2.56 و2.29 دولار، بما فيه المساعدات نفسها، لكل دولار…».

### S12 [EVIDENCE]: the ISP method contradicts its summary and relies on unbound figure values

- **Quote:** `method_en` (L115): "the four shares for a site add to more than 100% and are not summed or compared across categories".
- **Failure:**
  - The summary (L107) compares categories: "majority", "largest share", "second-largest", "smallest".
  - "Add to more than 100%" rests on Figure 4 labels, which R5 marks **[image]**: read visually and not yet confirmed by a second reader.
- **Replacement:**
  - EN: "Values and rankings are those printed in the report's text (p. 9), not its figure labels; the figure's shares for a site do not add to 100%, which the report does not explain, so the shares are not summed."
  - Make the matching AR change.
  - Have a second reader confirm Figure 4 before release.

### S13 [EVIDENCE]: s6 cites the cheaper of the two corridors held

- **Quote:**
  - EN (L30): "in 2025 Q3, quoted formal products for sending US$200 from Saudi Arabia to Yemen averaged 2.70%".
  - AR (L78).
- **Evidence:** VIS-REMITTANCE-COST also holds the United Arab Emirates corridor at 7.53%, which is lifted by one quote of 22.71%.
- **Failure:** Picking one corridor without saying that a second is held reads as selective.
- **Replacement:**
  - EN: "…from Saudi Arabia to Yemen averaged 2.70%, one of the two corridors held here (the other, from the United Arab Emirates, averaged 7.53%, lifted by a single high quote)".
  - AR: «…بلغ 2.70% من السعودية إلى اليمن، وهو أحد ممرين متاحين هنا (وبلغ متوسط الممر الآخر من الإمارات 7.53%، ويرفعه عرض سعر مرتفع واحد)».

### S14 [EVIDENCE, traceability]: the record locators point to a file that is not in the repository

- **Quote:** every READ `loc` in both records ends "(audit/close_out/addendum/R5_ccy_isp_sam.md)".
- **Evidence:** `audit/close_out/addendum/` holds R1, R2, R4, R6, ARABIC_6A and REDTEAM_6A, but not R5.
- **Failure:** The locator chain breaks on publication.
- **Replacement:** Commit R5 to that path in the same transaction, then check that every `loc` path resolves.

### S15 [EVIDENCE / AR]: the Arabic name of the Cash Consortium

- **Quote:**
  - «تحالف النقد في اليمن» in both records' titles and summaries, and in Reading s5 AR (L73).
  - «دراستا تحالف النقد في اليمن» (L55).
- **Evidence:** the ISP cover (`img_r5/isp-01.png`) prints the organisation's own Arabic name, «إتحاد المساعدات النقدية في اليمن».
- **Failure:**
  - The Arabic text names an organisation by a name it does not use.
  - The same rendering is already in governed text (readings.json, reading_sections.json), so a local fix would make the site inconsistent.
- **Replacement:**
  - Use «اتحاد المساعدات النقدية في اليمن (Cash Consortium of Yemen)» at first mention.
  - Change it everywhere in one terminology change, recorded as an open item if it is not done in this transaction.

---

## NIT

- **N1 [EVIDENCE], Thesis and s1 (L6, L10).** "while 11.9% of adults had an account" should read "…11.9% of adults in those areas had an account", so the universe matches the 31.9%.
- **N2 [EVIDENCE], s2 (L13).** "Each is a share of all adults, from a separate question" is not accurate for 37.8%, which combines two questions.
  - EN: "each from its own question, or, for 'either', from two combined".
  - AR: «كلٌّ من سؤاله الخاص، أو من سؤالين معًا في حالة "أيٍّ من الأمرين"».
- **N3 [EVIDENCE], all Findex shares.** No recall period is stated (the Findex questions refer to the past 12 months; not verified here). Consider adding "in the 12 months before the interview".
- **N4 [CBY, parity], AR s6 (L78).** «قدّر التقرير السنوي 2024 الحوالات» says "estimated", where the EN says "put" and CLM-032 AR says «أورد». Use «أورد التقرير السنوي 2024 قيمة الحوالات لعام 2024 عند…».
- **N5 [EXCHANGE], s8 (L40).** "a roster entry is not proof that it operates now" reads as insinuation.
  - EN: "a roster entry shows a licence listed for 2026; it does not by itself show that the provider operates now".
  - AR: «يُظهر القيد في القائمة ترخيصًا مدرجًا لعام 2026، ولا يُثبت وحده أن مقدم الخدمة يعمل حاليًا».
- **N6 [EXCHANGE / CBY], s9 (L46).** "reporting by exchange companies and remittance agents that separates…" implies they do not report.
  - EN: "published figures, from exchange companies, remittance agents or their supervisor, that separate…"
  - AR: «أرقام منشورة، من شركات الصرافة أو وكلاء الحوالات أو الجهة الرقابية، تفصل…».
- **N7 [EVIDENCE].** CCY-SAM is classed `TEMPORAL_OBSERVATION` although its headline values are model estimates, and its change trigger says "a newer comparable observation". The class is not rendered publicly (checked on `dist/en/evidence/FAS-YEM-2015/`), so this is an internal label only. Note it for the Master.
- **N8 [EVIDENCE], ISP summary (L107–108).** "Qa'tabah reporting the largest share (68%)" is ambiguous.
  - EN: "the largest assistance share of the three areas (68%)".
  - AR: «أكبر حصة للمساعدات بين المناطق الثلاث (68%)».
- **N9 [EVIDENCE].** One governorate is spelled two ways on the same route: "Al Dhale'e" (ISP) and "Ad-Dali" (SAM). Pick one EN form and gloss the study's spelling.
- **N10 [AR style], s7 (L81).** «وقيمة القناة الغائبة غير معروفة — لا يعني ذلك صفرًا» should read «وغياب قيمة للقناة يعني أنها غير معروفة، لا أنها صفر».
- **N11 [EVIDENCE], s3 (L18, L66).** The IGC paraphrase "estimates of entities, including microfinance institutions" drops the "World Bank" attribution and "exchange firms" that CLM-016 carries. Use CLM-016's wording: "as World Bank estimates of entities, including exchange firms and microfinance institutions".
- **N12 [process].** Owner question 1 holds: in `readings.json` only CWR-001 ("Same year, different number", whose title matches s6 in both languages) lists `/remittances/`, so after this change /remittances/ carries CWR-001 and CWR-012. Two follow-ups:
  - CWR-012 still needs its detail-route entry in `navigation_interaction.json`, as its own steward commit (D9).
  - The `/remittances/` entry's `search_record_count` (2) may need regenerating.

---

## Checks that passed

- **CR-21:** every Findex mention is month-precise, "November 2022 – January 2023" or "November 2022 to January 2023", in EN and AR. No day-precise Findex date remains.
- **Numbers:** every numeric token in EN and AR resolves to a value state in a bound record or in the two new records (years excepted, as usual).
- **Multiplier:** described as economic activity including the transfer in the summary, definition, method and limitations of both languages. The only gap is S11. It is not generalised beyond selected villages, and the Reading body does not use it.
- **Firewall:** people ≠ accounts, missing ≠ zero, chronology ≠ causality, and a survey of aid recipients ≠ the population are all stated (s2, s4, s5, s7; record limitations).
- **Naming:** CBY-Aden is named consistently in EN and AR. The cross-reference to "Same year, different number" is correct (CWR-001).
- **Arabic numbers:** numbers, units and periods match the EN in s2, s3, s5 and s6.

VERDICT: HOLD — B1, B2, B3
