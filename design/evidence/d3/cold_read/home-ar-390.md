# Home cold-reader report — ar-390

Recorded at D3 (27 September 2026). Reader: a fresh agent with no access to the repository, shown only the rendered Home page (`design/reference/out/`, commit before the D3 corrections) as five PNG captures at this language and width, in order; asked what the site is after 30 s, after 90 s and after 180 s, what confused it, what a screenshot could make someone misread, and whether the page reads as serious, trustworthy and clear (Arabic readers: whether the Arabic reads naturally). Verbatim; nothing edited. Findings are classified and acted on in `design/00_DESIGN_README.md` DL-D3-001 and `design/ESCALATIONS.md`.

Reader: a fresh agent shown only the rendered Home page (Arabic, 390 px), screens read in order. Method: opened the five PNGs with Read only, in the order given; stopped after screen 1 and after screens 1–2 to fix impressions before reading on; the full-page capture (390×8748 px, roughly 10–11 phone screens) was rendered downscaled, so text below the end of screen 4 is not legible to me and I report only its gross structure. No other file, code or command was used.

**1. After screen 1 only (~30 s)**

What it is: a text-only page titled "أدلة الشمول المالي في اليمن" with a slogan headline "الشمول المالي في اليمن ليس رقمًا واحدًا." and one long paragraph about a World Bank survey. I read it as a policy/statistics brief about Yemen, published by someone I cannot identify: the logo at top right is tiny and washed-out (looks like Latin letters, unreadable), and the only institution named is "البنك الدولي", so a cold reader could assume this is a World Bank page.

Real ambiguity in the title: "أدلة" is the plural of "دليل", whose everyday meaning is "guide/directory". On first sight "أدلة الشمول المالي في اليمن" can be read as "Financial-inclusion guides in Yemen", i.e., a directory of banks and services. Only the smaller label "إشارات من الأدلة" and (later) "سجل الدليل" push the reader towards "evidence". In an evidence-based-policy register the word is standard, but a general reader will hesitate.

Why it looks different from other country-economy sites: no hero image, no big KPI tile, no chart, no map, no "Yemen at a glance"; the first thing it does is deny a headline number ("ليس رقمًا واحدًا") and then hedge the one figure it gives: "في المناطق التي شملها المسح", "ولم يشمل المسح مناطق يسكنها نحو 23% من السكان", plus a metadata block "متى قيس أو رُصد؟". It reads like a methodological note, not a landing page. Header is plain words ("بحث", "EN", "القائمة"), no icons.

Where I would start: the only visibly clickable thing is the underlined line "أحدث قياس سكاني ممثل متاح لامتلاك الحساب", so I would tap that, though I was unsure whether it is a link or a caption, because it comes after the paragraph rather than before it. Otherwise "القائمة". Nothing on screen 1 says "start here".

The paragraph itself is one ~60-word sentence with a parenthesis inside a parenthesis, a semicolon, and four year references (Findex "لعام 2021", fieldwork "من نوفمبر 2022 إلى يناير 2023", data year "2022"). I had to read it twice to sort out which year the 11.9% belongs to.

**2. After screens 1–2 (~90 s)**

Scope and limits: yes, and they are stated explicitly for every figure. Screen 1: "الأشخاص بعمر 15 سنة فأكثر ضمن التغطية التي شملها المسح." Screen 2: the gender gap is "في المسح نفسه", "فجوة مقاسة بين النساء والرجال"; the POS figure is "ضمن نطاق الإبلاغ لديه" and "ولا يثبت الدليل مدى تغطية هذا النطاق لكل مناطق اليمن." The source is even qualified as "البنك المركزي اليمني – عدن", which signals awareness that there is more than one central bank, though a non-Yemeni reader will not know why "– عدن" is appended and may read the dash as a typo.

Explorable/verifiable: the page promises it. "افتح سجل الدليل" appears under each of the three items, and each item has a dated "متى قيس أو رُصد؟" block ("موجة Global Findex 2021؛ العمل الميداني في اليمن من 2022-11-07 إلى 2023-01-09", "مارس 2025 – يناير 2026"). But on the Home page itself there is no source locator, no link text that names a dataset or document, and no table, so "verify" is asserted, not demonstrated yet.

What confused me at this stage:
- Each item carries two links, the underlined title and "افتح سجل الدليل"; I could not tell whether they go to the same place.
- The item structure is inverted (paragraph, then date, then underlined title, then scope note, then "افتح سجل الدليل"). Screen 2 opens with a bare "افتح سجل الدليل" separated by white space from the text above, so I first attached it to the paragraph below it.
- Precision drifts: "11.9%" on screen 1, then "18.35% من الرجال و5.44% من النساء حساب، بفارق 12.91 نقطة مئوية" on screen 2, two decimals on a survey estimate.
- The heading "ثلاثة أرقام تقيس ثلاثة أشياء مختلفة" promises three numbers; I counted seven (11.9, 23, 18.35, 5.44, 12.91, 561, 1,473). "Three measures" is what is meant.

**3. After everything (~180 s)**

Link I would tap: "افتح سجل الدليل" under the first item (the 11.9% account figure). I expect a record page with the exact figure, the definition of "حساب", the age universe, the 23% coverage exclusion, fieldwork dates, the World Bank/Findex citation with a URL, and ideally the English twin. Second choice: "تحقق من الأدلة" in the block "افهم ← استكشف ← تحقّق", which reads as the entry to the whole evidence base. Third: question "01 من هم الأقل وصولًا، وأين تظهر الفجوات المقاسة؟".

Inside evidence within ~3 minutes: probably yes, if "افتح سجل الدليل" is a single tap to a record. But the Home page consumed almost all of the three minutes: screens 1–4 are continuous prose, the purpose statement ("«أدلة الشمول المالي في اليمن» مورد عام ثنائي اللغة يساعد المستخدمين على فهم … ومقارنتها والتحقق منها") only arrives on screen 3, and the navigational list "أسئلة للبدء" only on screen 4. There are three overlapping entry CTAs within one screen: "ابدأ بسؤال", "تحقق من الأدلة", then "ابدأ من المسألة التي تريد حسمها". From the full-page thumbnail the remaining ~60% of the page is more prose blocks, further numbered questions (I could make out 03 and 04), at least one bordered box, and a grey footer; I saw no chart, table or image anywhere on the page.

**4. What confused me, labels I did not understand, screenshot risk**

- "أدلة / الدليل": guides vs evidence (see 1).
- "قياس سكاني ممثل": a calque of "representative population measurement"; a lay Arabic reader would expect "مسح تمثيلي" or "مسح ممثل للسكان".
- "متى قيس أو رُصد؟": a question used as a field label, repeated four times; "رُصد" with diacritic reads like a translated UI string.
- "سجل الدليل": what is a "record"? a page, a PDF, a database row?
- "موجة Global Findex 2021": "wave" is survey jargon; in item 2 the survey is given only in Latin, while item 1 gave "مسح المؤشر العالمي للشمول المالي (Global Findex)".
- "ضمن نطاق الإبلاغ لديه": stiff, "within its reporting scope".
- "لا درجة واحدة" in "الشمول المالي منظومة مترابطة، لا درجة واحدة": "درجة" for "score" is odd; "مؤشرًا واحدًا" or "رقمًا واحدًا" would match the headline.
- "البنك المركزي اليمني – عدن": the dash-suffix is unexplained.
- Date formatting is inconsistent inside one screen: prose says "من نوفمبر 2022 إلى يناير 2023", the metadata says "من 2022-11-07 إلى 2023-01-09" (ISO in Arabic running text).
- Bidi wrap: "دراسة Global" ends one line and "Findex 2021؛" starts the next, splitting the Latin name across the line edge.

If someone screenshots screen 1 and posts it: the likely caption is "11.9% of Yemenis have a bank account (2021)". That drops the 15+ age universe, drops "في المناطق التي شملها المسح", drops the ~23% population excluded, and picks the wrong year (fieldwork was Nov 2022–Jan 2023). A skimmer may also confuse the two percentages sitting close together (11.9% vs 23%). And the screenshot carries no legible publisher identity, so the source of the claim becomes "the World Bank".

**5. Serious, credible, clear? Is the Arabic natural?**

Serious and credible: yes. Named sources, dated fieldwork, explicit universes, the section "ما الذي لا ينبغي استنتاجه؟" ("وجود بنية تحتية أكبر لا يثبت وحده أن عدد المستخدمين زاد … عدد الحسابات لا يساوي عدد الأشخاص") is the kind of honesty most dashboards lack. Typography is clean, RTL layout is correct throughout: logo/title on the right, "القائمة" on the left, list numbers "01/02" on the leading (right) edge, arrows "افهم ← استكشف ← تحقّق" point in reading direction, Arabic punctuation ("؛", "؟", «») used consistently, diacritics placed where they help ("رقمًا واحدًا", "المُمكِّنة", "جُمعت", "تحقّق").

Clear: partly. Grammar is correct MSA and the sentence-initial "و" cadence ("وفي المسح نفسه", "وبصورة منفصلة", "ويدعم", "ولا يتخذ") is genuinely Arabic, not mirrored English. But sentences are long, the first paragraph is over-nested, the page is prose-only with weak visual hierarchy, and the inverted item order (claim, date, title, note, link) makes boundaries hard to see on a phone.

Translated feel is in terminology, not grammar: "إشارات من الأدلة", "قياس سكاني ممثل", "ضمن نطاق الإبلاغ لديه", "لا درجة واحدة", the question-form metadata label, and the concept "سجل الدليل" all read as English-first system vocabulary rendered into Arabic. Numbers are Western digits throughout with Latin thousands comma ("1,473") and ISO dates in metadata; this is consistent and legible, but combined with the calques it gives the page a machine/English-origin texture. Nothing is "flipped": direction, alignment and mirroring are right; what betrays the English source is word choice and the dense, caveat-first sentence architecture.