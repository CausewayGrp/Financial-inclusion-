# CLOSE-6B: Arabic editorial review

Reviewer: senior Arabic economic editor (subagent). Input: `scratchpad/c6b/close_6b.py`, as it stood on 11 October 2026 after the SEARCH-ALIAS-046 block was added. I only read it. Nothing under the repository was modified.

**How to use this file.** Findings are ranked MUST-FIX, SHOULD-FIX and NIT. Each *Corrected* string is a complete value, ready to paste:
- For a whole field, it is the whole field.
- For an `(old, new)` pair or an appended fragment, it is the complete `new` value.
- A string that begins with a space in the transaction keeps that space.

Where one field has several findings, the corrected string at its highest-ranked finding applies all of them.

**Checks run.**
1. **Digit parity.** Every digit sequence in all 44 EN/AR pairs was compared mechanically (`review/tools/parity6b.py`). The pairs are:
   - the MERGES titles, C12, LIQ and HIST titles;
   - the AMB why and does-not-establish texts;
   - the new SCOPE line;
   - the CARDS (10 × 2);
   - YSC-031 and YSC-032 (5 fields each);
   - the YSC-012 and YSC-015 appended text;
   - the NEWS832 title and SEARCH-ALIAS-046.

   Result: **0 drift** in the draft and in every corrected string below. Numbers, units, periods and dates agree.
2. **Legal names.** Checked against the verbatim titles in R7 and R3.
3. **Terminology.** Checked against `terminology_register.json`, the projected `source_library.json`, `system_chronology.json`, `measurement_agenda.json`, `interface_copy.json` and `search_aliases.json`, and against the ARABIC_6A conventions.
4. **Bidi.** Checked against the UBA and the renderer's `LTR_RUN` and `ID_RUN` (`scripts/yfie/text.py`).
5. **Punctuation and controls.** The Arabic contains no Latin comma or semicolon, no double space and no LRM, RLM or isolate characters.

**Tally:** 2 MUST-FIX · 10 SHOULD-FIX · 9 NIT · 8 outside Arabic scope.

**What is already right:**
- The naming is neutral: «البنك المركزي اليمني – عدن» and «البنك المركزي اليمني – صنعاء» / «في صنعاء». No «الحرب» and no «سلطات» appear for the central banks.
- «شركات ومنشآت الصرافة» appears in the C12 title and the CIRC-02 card.
- The legal titles in C12_CARD and NEWS832 are verbatim («تعميم رقم (12) … موجه إلى كافة البنوك وشركات ومنشآت الصرافة …»; «لجنة تمويل وتنظيم الاستيراد تدشن أولى اجتماعاتها»).
- «منشور» is used for the CBY-Aden periodic circulars and «تعميم» for the Sana'a circular, as each names itself.
- «خطاب عدم ممانعة», «وكيل فرعي» / «الوكيل الرئيسي», «وحدة التعاملات بالنقد الأجنبي» and «الضبطية الجمركية والقضائية» all follow the originals.
- «الوحدة الاقتصادية في مركز صنعاء» follows the site's existing form.
- The firewall holds: «عدد الحسابات ليس عدد الأشخاص»، «لا يثبت إصدار التعليمات…»، «ولم يُفصَح…».
- SEARCH-ALIAS-046 matches the form of alias 017. Its `boundary_note_ar` is accurate and natural.

---

## MUST-FIX

### M1 · SRC-AMB-MFB-SUPERVISION-2026 · `why_it_matters_ar`: the replacement breaks gender agreement in the rest of the cell

Current `new` value:

```text
موجز سياسات أعده محمد اللاعي وذكرى الجبري، ونشره بنك الأمل للتمويل الأصغر، حول
```

Problem: the transaction replaces only the opening fragment. The cell continues «… في اليمن، **وتدعو** إلى أن يقيّم الإشراف … . **وهي** نقطة انطلاق مفيدة …». Both «تدعو» and «هي» agree with the old feminine head «ورقة». The new head «موجز» is masculine, so the published sentence becomes ungrammatical: «موجز سياسات … وتدعو … وهي». A feminine head fixes this without touching the rest of the cell. «ورقة سياسات موجزة» renders "policy brief" exactly, and the cover prints "POLICY BRIEF".

Corrected `new`:

```text
ورقة سياسات موجزة أعدها محمد اللاعي وذكرى الجبري، ونشرها بنك الأمل للتمويل الأصغر، حول
```

(Alternative: keep «موجز سياسات» and widen `old` to the whole cell, changing «وتدعو» to «ويدعو» and «وهي» to «وهو». The one-fragment fix above is safer.)

### M2 · YSC-031 · `fi_relevance_ar`: a register-banned term, «أجندة القياس», on a public page

Current:

```text
التحقق من الهوية وإجراءات فتح الحساب موضعٌ يتعثر فيه الوصول إلى الحسابات كثيرًا؛ ومتوسط وقت فتح الحساب الذي تطلب التعليمات من مقدمي الخدمة الإبلاغ عنه من نوع مقاييس الرحلة التي تطلبها أولوية «رحلات الانضمام الرقمي وإثبات الهوية» في أجندة القياس.
```

Problems:
- TERM-013 lists «أجندة القياس» (and "Measurement Agenda") under `do_not_use`, as a search alias only. The section is «أولويات القياس», and a single item is «أولوية القياس». No public string on the site uses «أجندة القياس» today, so this would be the first.
- "onboarding": MA-007, the priority cited here, uses «الانضمام» («رحلات الانضمام», «مسار الانضمام»). Rendering it once as «إجراءات فتح الحساب» and once as «فتح الحساب» blurs the link to that priority.
- «من نوع» needs a copula to read cleanly («هو من نوع»). «كثيرًا» sits better before the verb («كثيرًا ما يتعثر»).

Corrected:

```text
التحقق من الهوية وإجراءات الانضمام موضعٌ كثيرًا ما يتعثر فيه الوصول إلى الحسابات؛ ومتوسط وقت فتح الحساب الذي تطلب التعليمات من مقدمي الخدمة الإبلاغ عنه هو من نوع مقاييس الرحلة التي تطلبها أولوية القياس «رحلات الانضمام الرقمي وإثبات الهوية».
```

The English needs the same change (O1).

---

## SHOULD-FIX

### S1 · SRC-CBY-DEC-19-2024 `why_it_matters_ar` and YSC-012 `fact_ar`: «تحويلها» means "transfer it", not "convert it"

In a sentence about remittances, «ما لم يطلب المستفيد تحويلها» reads first as "unless the beneficiary asks to *transfer* them". The decision itself says «ولا يجوز **مصارفتها** بأي عملة إلا في حال رغبة العميل (المستفيد)». The DEC-19 card has a second problem: it moves from a verb clause («لا تجري إلا عبر…») to a bare nominal fragment («ووكلاء فرعيون مرخص لهم منه، …»). Parallel «ألا / أن» clauses fix the list.

Current (DEC-19 card):

```text
قواعد البنك المركزي اليمني – عدن للتحويلات الخارجية: لا تجري إلا عبر البنوك أو شركات الصرافة المؤهلة، مع خطاب عدم ممانعة منه قبل أي تعاقد مع شركة حوالات دولية أو وكيل فرعي؛ ووكلاء فرعيون مرخص لهم منه، يكون الوكيل الرئيسي مسؤولًا عنهم؛ وتُصرف الحوالات الواردة بالعملة التي وردت بها ما لم يطلب المستفيد تحويلها بسعر السوق.
```

Corrected (DEC-19 card):

```text
قواعد البنك المركزي اليمني – عدن للتحويلات الخارجية: ألا تجري إلا عبر البنوك أو شركات الصرافة المؤهلة، مع الحصول على خطاب عدم ممانعة منه قبل أي تعاقد مع شركة حوالات دولية أو وكيل فرعي؛ وأن يكون الوكلاء الفرعيون مرخصًا لهم منه، ويكون الوكيل الرئيسي مسؤولًا عنهم؛ وأن تُصرف الحوالات الواردة بالعملة التي وردت بها ما لم يطلب المستفيد مصارفتها بسعر السوق.
```

The corrected YSC-012 `fact_ar` is given in S2, which also fixes this.

### S2 · YSC-012 `fact_ar` (appended): a split construction, legal-name fidelity, and a lopsided pairing

Current (keep the leading space):

```text
 وفي مارس 2024 حدّد التعميم رقم (12) الصادر عن البنك المركزي اليمني في صنعاء (13 مارس 2024، ويُعمل به من 14 مارس 2024) كيفية صرف البنوك وشركات الصرافة، بوصفها وكلاء رئيسيين، للحوالات الخارجية الواردة، فتُصرف الحوالات الفردية الواردة بالدولار الأمريكي أو بعملات أجنبية أخرى بما يعادلها بالريال السعودي؛ وفي 23 مايو 2024 ألزم قرار محافظ البنك المركزي اليمني – عدن رقم (19) بأن تجري التحويلات الخارجية عبر البنوك أو شركات الصرافة المؤهلة وحدها، مع خطاب عدم ممانعة منه قبل التعاقد مع شركات الحوالات الدولية أو الوكلاء الفرعيين، وبأن تُصرف الحوالات الواردة بالعملة التي وردت بها ما لم يطلب المستفيد تحويلها.
```

Problems:
- In «كيفية صرف البنوك وشركات الصرافة، بوصفها وكلاء رئيسيين، للحوالات…», the verbal noun «صرف» is cut off from its object by the agent and a parenthetical. Readers parse «صرف البنوك» as "the banks' payout" before they find the object.
- **Legal name.** The decision calls itself «قرار محافظ البنك المركزي رقم (19) لسنة 2024». The draft inserts «اليمني – عدن» inside the name. Placing the issuer in an apposition keeps the name intact. That is also how the Sana'a circular is introduced in the same sentence («التعميم رقم (12) الصادر عن …»), so the two banks are paired in the same way. Using the same preposition, «في», for both banks completes the symmetry (6A allows «البنك المركزي اليمني في عدن»; alias 017 and the AMB card use it).
- «منه» after «قرار … – عدن رقم (19)» could refer to the decision. With the issuer named just before it, it refers to the bank.
- «تحويلها» becomes «مصارفتها» (S1).
- The parenthesis mixes a bare date and a verb clause. «المؤرخ … والمعمول به …» is the register form.

Corrected (keep the leading space):

```text
 وفي مارس 2024 حدّد التعميم رقم (12) الصادر عن البنك المركزي اليمني في صنعاء (المؤرخ 13 مارس 2024، والمعمول به من 14 مارس 2024) كيفية صرف الحوالات الخارجية الواردة عبر البنوك وشركات الصرافة العاملة وكلاءَ رئيسيين، فتُصرف الحوالات الفردية الواردة بالدولار الأمريكي أو بعملات أجنبية أخرى بما يعادلها بالريال السعودي؛ وفي 23 مايو 2024 ألزم قرار محافظ البنك المركزي رقم (19)، الصادر عن البنك المركزي اليمني في عدن، بأن تجري التحويلات الخارجية عبر البنوك أو شركات الصرافة المؤهلة وحدها، مع الحصول على خطاب عدم ممانعة منه قبل التعاقد مع شركات الحوالات الدولية أو الوكلاء الفرعيين، وبأن تُصرف الحوالات الواردة بالعملة التي وردت بها ما لم يطلب المستفيد مصارفتها.
```

### S3 · YSC-032 `fact_ar`: «– عدن» is inserted inside the decision's own name

Current:

```text
حدّد قرار محافظ البنك المركزي اليمني – عدن رقم (7) لسنة 2026 حدًا أدنى لسعر الفائدة قدره 18% سنويًا على ودائع الادخار الجديدة بالريال اليمني لدى البنوك التجارية، وترك أسعار الفائدة على الودائع بالعملات الأجنبية وعلى الإقراض للبنوك، واستثنى البنوك الإسلامية؛ ويسري على العقود المبرمة بعد نفاذه في 12 أبريل 2026.
```

Problem: the instrument calls itself «قرار محافظ البنك المركزي اليمني رقم (7) لسنة 2026» (R7, doc 2), and the card title uses that form. The fix keeps the name whole and gives the place in an apposition.

Corrected:

```text
حدّد قرار محافظ البنك المركزي اليمني رقم (7) لسنة 2026، الصادر في عدن، حدًا أدنى لسعر الفائدة قدره 18% سنويًا على ودائع الادخار الجديدة بالريال اليمني لدى البنوك التجارية، وترك أسعار الفائدة على الودائع بالعملات الأجنبية وعلى الإقراض للبنوك، واستثنى البنوك الإسلامية؛ ويسري على العقود المبرمة بعد نفاذه في 12 أبريل 2026.
```

### S4 · SRC-CBY-SANAA-C12-2024 `why_it_matters_ar`: the same split construction as in S2

Current:

```text
تعميم البنك المركزي اليمني في صنعاء بشأن صرف البنوك وشركات الصرافة، بوصفها وكلاء رئيسيين لخدمات الحوالات الخارجية، للحوالات الواردة: تُصرف الحوالات الواردة بالريال السعودي بالريال السعودي، والحوالات الفردية الواردة بالدولار الأمريكي أو بعملات أجنبية أخرى بما يعادلها بالريال السعودي، بأسعار تعتمدها وحدة التعاملات بالنقد الأجنبي لديه؛ ويُعمل به اعتبارًا من 14 مارس 2024.
```

Corrected (meaning unchanged; see O2 for a content error that both languages share):

```text
تعميم البنك المركزي اليمني في صنعاء بشأن صرف الحوالات الواردة عبر البنوك وشركات الصرافة العاملة وكلاءَ رئيسيين لخدمات الحوالات الخارجية: تُصرف الحوالات الواردة بالريال السعودي بالريال السعودي، والحوالات الفردية الواردة بالدولار الأمريكي أو بعملات أجنبية أخرى بما يعادلها بالريال السعودي، بأسعار تعتمدها وحدة التعاملات بالنقد الأجنبي لديه؛ ويُعمل به اعتبارًا من 14 مارس 2024.
```

### S5 · SRC-CBY-EKYC-2023 `does_not_establish_ar` and YSC-031 `does_not_establish_ar`: «لا تحدد تاريخًا للنفاذ … من تاريخ نفاذها» contradicts itself

The English separates "effective date" from "entry into force". The Arabic uses «النفاذ» for both, so it reads: "they set no date of entry into force, only periods counted from the date of their entry into force". The instrument does use «تاريخ نفاذها» without defining it (R7, doc 3). The fix says exactly that.

Current (card):

```text
لا تُظهر التعليمات أن فتح الحسابات عن بُعد متاح أو مستخدم، ولا المدة التي يستغرقها فعليًا، ولا عدد من فتحوا حسابات بهذه الطريقة؛ ولا تحدد تاريخًا للنفاذ، بل مُهلًا للامتثال تُحسب من تاريخ نفاذها.
```

Corrected (card):

```text
لا تُظهر التعليمات أن فتح الحسابات عن بُعد متاح أو مستخدم، ولا المدة التي يستغرقها فعليًا، ولا عدد من فتحوا حسابات بهذه الطريقة؛ ولا تحدد تاريخ نفاذها، وإنما تحدد مُهَلًا للامتثال تُحسب من ذلك التاريخ.
```

Current (YSC-031):

```text
لا يثبت إصدار التعليمات أن فتح الحسابات عن بُعد متاح أو مستخدم، ولا المدة التي يستغرقها فعليًا، ولا أن أي بيانات مُبلَّغ عنها قد نُشرت؛ ولا تحدد التعليمات تاريخًا للنفاذ، بل مُهلًا للامتثال تُحسب من تاريخ نفاذها.
```

Corrected (YSC-031):

```text
لا يثبت إصدار التعليمات أن فتح الحسابات عن بُعد متاح أو مستخدم، ولا المدة التي يستغرقها فعليًا، ولا أن أي بيانات مُبلَّغ عنها قد نُشرت؛ ولا تحدد التعليمات تاريخ نفاذها، وإنما تحدد مُهَلًا للامتثال تُحسب من ذلك التاريخ.
```

### S6 · SRC-CBY-CIRC-04-2025 and SRC-CBY-CIRC-01-2026 `why_it_matters_ar`: «شركات الصرافة» narrows the regulated universe

Both instruments address «شركات / منشآت الصرافة»: CIRC-04 in its title and Second clause, and CIRC-01-2026 in its First and Third clauses («شركات ومنشآت الصرافة»). Both card titles use that form, and so does the 6A convention. «شركات الصرافة» alone drops the individual establishments, which is a universe change. (The English "exchange firms" is generic; see O3.)

Current (CIRC-04):

```text
تعليمات للبنوك وشركات الصرافة بشأن إجراءات العناية الواجبة المعززة والتحقق من قوائم العقوبات الدولية، ومنها قوائم مجلس الأمن الدولي ومكتب مراقبة الأصول الأجنبية التابع لوزارة الخزانة الأمريكية (OFAC) والاتحاد الأوروبي ووزارة الخزانة البريطانية.
```

Corrected (CIRC-04):

```text
تعليمات للبنوك وشركات ومنشآت الصرافة بشأن إجراءات العناية الواجبة المعززة والتحقق من قوائم العقوبات الدولية، ومنها قوائم مجلس الأمن الدولي ومكتب مراقبة الأصول الأجنبية التابع لوزارة الخزانة الأمريكية (OFAC) والاتحاد الأوروبي ووزارة الخزانة البريطانية.
```

Current (CIRC-01-2026):

```text
يحظر على البنوك وشركات الصرافة ومقدمي خدمات الدفع ومشغلي المحافظ الإلكترونية التعامل بالأصول الافتراضية أو العملات المشفرة أو مع مقدمي خدماتها، ويُعمل به من تاريخ صدوره.
```

Corrected (CIRC-01-2026):

```text
يحظر على البنوك وشركات ومنشآت الصرافة ومقدمي خدمات الدفع ومشغلي المحافظ الإلكترونية التعامل بالأصول الافتراضية أو العملات المشفرة أو مع مقدمي خدماتها، ويُعمل به من تاريخ صدوره.
```

### S7 · SRC-CBY-CIRC-02-2025 `does_not_establish_ar`: "enforced" is rendered as "implemented"

«يُنفَّذ» means "is implemented, carried out". "Enforced" is «يجري إنفاذه», and the CIRC-01-2026 card uses «إنفاذه» for the same English word. Implementation and enforcement are different states under the firewall (issuance ≠ implementation).

Current:

```text
لا يُظهر المنشور كيف يُراقَب تطبيقه أو يُنفَّذ، ولا أي أثر على علاقات المراسلة المصرفية أو قنوات الحوالات أو الوصول.
```

Corrected:

```text
لا يُظهر المنشور كيف يُراقَب تطبيقه أو كيف يجري إنفاذه، ولا أي أثر على علاقات المراسلة المصرفية أو قنوات الحوالات أو الوصول.
```

### S8 · SRC-CBY-CIRC-03-2025 `why_it_matters_ar`: METAC's name is garbled

«مركز صندوق النقد الدولي الإقليمي للمساعدة الفنية» puts the adjective «الإقليمي» after a construct chain, so it reads as qualifying «الدولي» or «الصندوق». The circular names the centre itself: «المركز الإقليمي للمساعدة الفنية للشرق الأوسط (METAC) التابع لصندوق النقد الدولي» (R7, doc 6, p.1).

Current:

```text
تعليمات لإدارة المخاطر تسري على جميع البنوك، أُعدّت بدعم فني من مركز صندوق النقد الدولي الإقليمي للمساعدة الفنية في الشرق الأوسط (METAC).
```

Corrected:

```text
تعليمات لإدارة المخاطر تسري على جميع البنوك، أُعدّت بدعم فني من المركز الإقليمي للمساعدة الفنية للشرق الأوسط (METAC) التابع لصندوق النقد الدولي.
```

### S9 · UI-DATA-GROUP-REGULATORY-SCOPE `label_ar` (new): a delayed subject, two «أما» in a row, and «محفوظة»

Current `new_ar`:

```text
وقد أصدرها كلها أو نشرها، عدا وثيقة واحدة، البنك المركزي اليمني – عدن؛ وتشير صفحتاه غير المؤرختين عن معلومات مخاطر الائتمان إلى تعليمات أقدم، أولها من عام 1991. أما الوثيقة الوحيدة الصادرة في صنعاء، وهي تعميم للبنك المركزي اليمني – صنعاء بشأن صرف الحوالات الخارجية الواردة، فمحفوظة في النسخة التي أعاد موقع إخباري نشرها. ولا تضم هذه المجموعة أي قانون؛ أما
```

Problems:
- The subject («البنك المركزي اليمني – عدن») comes after two verbs, their objects and the exception, so the sentence reads "issued all of them or published, except one document, the CBY–Aden".
- The new «أما … فمحفوظة» is followed one sentence later by the existing «أما القانون الوحيد … فمدرج». Two contrastive «أما» clauses in a row flatten both.
- «محفوظة» means "preserved, archived". The English "held" echoes the label's opening («المتوفرة في قاعدة الأدلة»), so «المتوفرة» is the matching word.

Corrected `new_ar` (it still ends with «أما», so the existing continuation stays grammatical):

```text
وجميعها، عدا وثيقة واحدة، أصدرها البنك المركزي اليمني – عدن أو نشرها؛ وتشير صفحتاه غير المؤرختين عن معلومات مخاطر الائتمان إلى تعليمات أقدم، أولها من عام 1991. والوثيقة الوحيدة الصادرة في صنعاء تعميمٌ للبنك المركزي اليمني – صنعاء بشأن صرف الحوالات الخارجية الواردة، والنسخة المتوفرة منه هي التي أعاد موقع إخباري نشرها. ولا تضم هذه المجموعة أي قانون؛ أما
```

### S10 · Bidi · YSC-031 `fact_ar`: «(المرجع 840/CBY/2023)» displays as "CBY/2023/840"

Under the UBA in an RTL paragraph, "840" follows Arabic, so it stays a number with the right-to-left direction (EN). By rule W7, "2023" follows "CBY" and becomes left-to-right. The first «/» sits between a right-to-left run and a left-to-right run, so it takes the paragraph direction (RTL). The visual order is therefore «CBY/2023/840». `LTR_RUN` and `ID_RUN` do not match this pattern, which the renderer test confirms. The same defect is **already live** in the Arabic card titles of SRC-CBY-EKYC-2023, DEC-19 (289/CBY/2024), CIRC-01-2024 (235/CBY/2024) and DEC-07 (220/CBY/2026), as `dist/` shows. «CBY/L/258/2026», «(METAC)», «(OFAC)» and «18%» render correctly.

Corrected: **no text change.** The fix belongs in the renderer (O6). It isolates every such reference at once, and it avoids putting isolate characters in Master text. Do not hand-insert LRI/PDI into this one cell.

---

## NIT

**N1 · YSC-031 `fact_ar`: the instrument's name in guillemets.** The card title, and the instrument itself, give the name without quotation marks: «تعليمات تنظيم إجراءات اعرف عميلك إلكترونيًا». Guillemets around «اعرف عميلك» are fine in running prose (MA-007), but this is the formal title. N2 is also applied. Corrected:

```text
أصدر البنك المركزي اليمني – عدن تعليمات تنظيم إجراءات اعرف عميلك إلكترونيًا (المرجع 840/CBY/2023) للبنوك ولمقدمي خدمات النقود الإلكترونية عبر الهاتف المحمول المرخص لهم، تحدد كيفية فتح الحسابات عن بُعد دون حضور العميل شخصيًا، وتُلزم مقدمي الخدمة بالإبلاغ كل نصف سنة عن بيانات منها متوسط الوقت المستغرق لفتح الحساب وتفعيله.
```

**N2 · «متوسط الوقت اللازم» (EKYC card `why_it_matters_ar`; YSC-031 `fact_ar`).** «اللازم» can read as "the time required" (a norm), while the form asks for time actually taken: «متوسط الوقت المستغرق» (R7, doc 3, p.30). MA-007 already says «اللازم», so this is optional. Corrected (card):

```text
تعليمات البنك المركزي اليمني – عدن للبنوك ولمقدمي خدمات النقود الإلكترونية عبر الهاتف المحمول المرخص لهم بشأن فتح الحسابات عن بُعد دون حضور العميل شخصيًا؛ ويُبلغ مقدمو الخدمة كل نصف سنة عن بيانات منها متوسط الوقت المستغرق لاستكمال الطلب ولفتح الحساب وتفعيله.
```

**N3 · YSC-031 `system_implication_ar`.** «ولا لمن» is elliptical. Corrected:

```text
أصبح فتح الحسابات عن بُعد مسارًا منظمًا للبنوك ولمقدمي خدمات النقود الإلكترونية الخاضعين لرقابة البنك المركزي اليمني – عدن؛ ولم يُفصَح عمّا إذا كانوا يقدمونه ولا لمن يقدمونه.
```

**N4 · YSC-032 `period_ar`.** The site uses «نافذ من» nowhere and «اعتبارًا من» 209 times. Corrected:

```text
9 أبريل 2026 (يُعمل به اعتبارًا من 12 أبريل 2026)
```

**N5 · YSC-015 `does_not_establish_ar` (appended).** The source's label is «بيان صحفي» (NEWS832 `document_label_ar`, 261 uses on the site), and «خبر» appears 3 times. Corrected (keep the leading space):

```text
 ولا يذكر البيان الصحفي عن اجتماعها الأول الجهة التي أنشأتها ولا القرار الذي أُنشئت بموجبه.
```

**N6 · AMB author names.** «محمد اللاعي» and «ذكرى الجبري» are back-transliterations. The paper prints only "Mohammed Saleh Al-Lai" and "Dhekra Ahmed Al-Gabri" (R4). Both spellings are the usual Yemeni forms, so they are acceptable. If no Arabic printing can be found, nothing changes.

**N7 · SRC-CBY-BANKS-BS-2022 `does_not_establish_ar`.** «مع القيمتين اللتين يذكرهما» says "two values", where the English says "its own values". It is accurate to the source (a "from … to …" pair, R7, doc 9, p.3), so the wording is acceptable. A literal alternative is «مع القيم التي يذكرها».

**N8 · YSC-032 `system_implication_ar`.** A bare «أداة من أدوات السياسة» can read as "politics". «السياسة النقدية» is more precise: the decision rests on the Monetary Policy Committee, and the event class is MONETARY_POLICY_RULE. Change it only if the English becomes "a monetary-policy instrument".

**N9 · SEARCH-ALIAS-046 `terms_ar`.** You could add the common unhamzated spelling «صنعا» and the full form «البنك المركزي اليمني في صنعاء». Alias 017 has no such variants either, so this is optional.

---

## Outside Arabic scope (English or code; Arabic counterparts given where both languages change)

- **O1 · YSC-031 `fi_relevance_en`.** "the Measurement Agenda's priority on digital onboarding and identity journeys" uses a TERM-013 `do_not_use` term. Change it to "the measurement priority on digital onboarding and identity journeys" (pairs with M2).
- **O2 · C12 `why_it_matters` (both languages): a content error.** The text says "at rates its Foreign Exchange Dealing Unit approves". That holds for US dollars (§2a). For other currencies, §3a sets "the international selling rate of the foreign currency against the Saudi riyal on the day the transfer was issued", not a Unit-approved rate.
  - EN fix: "…in their Saudi-riyal equivalent (dollars at the rate its Foreign Exchange Dealing Unit approves, other currencies at the international selling rate against the Saudi riyal on the day the transfer was issued); it applies from 14 March 2024."
  - AR (on top of S4): replace «بما يعادلها بالريال السعودي، بأسعار تعتمدها وحدة التعاملات بالنقد الأجنبي لديه؛» with «بما يعادلها بالريال السعودي (الدولار بسعر تعتمده وحدة التعاملات بالنقد الأجنبي لديه، والعملات الأخرى بسعر البيع العالمي مقابل الريال السعودي يوم إصدار الحوالة)؛».
  - Digit parity is unaffected.
- **O3 · CIRC-04-2025 and CIRC-01-2026 `why_it_matters`.** "exchange firms" should read "exchange companies and establishments", as the card titles and the instruments have it (pairs with S6).
- **O4 · YSC-012 `does_not_establish` (both languages).** The event now carries Decision No. 19, but the list names only "directive, circular or prohibition". Suggested EN: "A directive, circular, decision or prohibition …". AR: «لا يثبت التوجيه أو التعميم أو القرار أو الحظر الامتثال الفعلي أو الإغلاق أو الانتقال أو كيفية صرف الحوالات فعليًا أو وصول المستخدم في كل موقع.»
- **O5 · LIQ `issuer` (an English-only field).** The field prints the Arabic author name with no transliteration. LIQ_32's old text has "Majdoleen Mohammad Abdu Saeed" and R3 has "Majdoleen Mohammed Abdo Saeed". If `issuer` is shown to English readers, add one transliteration, marked as not printed.
- **O6 · Renderer (`scripts/yfie/text.py`).** Add a reference pattern such as `(?<![\w/])\d+/[A-Z]+/\d{4}(?![\w/])` to `LTR_RUN`, or isolate it alongside `ID_RUN`. This fixes S10 and the four live card titles. It is a code change for the steward, and it must pass the gates.
- **O7 · EKYC `why_it_matters` and YSC-031 `fact_en`.** "providers report" leaves unclear whether banks report too. The duty falls on every «مؤسسة مالية» (banks and e-money providers). If the English is clarified, change «مقدمو الخدمة» / «مقدمي الخدمة» to «المؤسسات المالية» in step.
- **O8 · SEARCH-ALIAS-001 `boundary_note` (both languages; not touched by CLOSE-6B).** The note says the regulatory documents are "issued by the Central Bank of Yemen – Aden". That is still true, because the wording is not exclusive. The /data/ scope line now says "All but one", so the note should be aligned in a later transaction.

---

ARABIC: HOLD — M1, M2
