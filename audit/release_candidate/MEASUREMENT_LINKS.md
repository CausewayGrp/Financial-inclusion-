# Measurement links: Readings → Measurement Agenda (B6)

Status: APPLIED in transaction RC-9 (`audit/release_candidate/rc_9_b6_measurement.py`, 3 October 2026), Master-first and
through `audit/tranche_b_execution/run_stage.py`. Each binding was written with an exact-value guard. The Reading
pages now render their priorities under "Related measurement priorities" / «أولويات قياس ذات صلة»; /measurement/ shows
each priority's `decisions_unlocked` and `blocked_evidence` under two new labels; gate RC-B6 in `scripts/validate.py`
(with a negative control) checks both. The analysis below was drafted on 2 October 2026 against `origin/main` and
re-checked against the RC-8b Master before it was applied. The bindings it reads as "today" are those before RC-9.

Data read: `site-src/content/content/readings.json`, `reading_sections.json` and `measurement_agenda.json` (projections
of the Master), the Master sheets `08_READINGS`, `10_MEASUREMENT_AGENDA` and `04_NAV_UX`, and the built site `dist/en`
and `dist/ar`.

## How a link was chosen

A Reading is linked to a priority only when the Reading names something it does not yet know, and the priority's
stated purpose (`missing_evidence` or `unlocked_decision`) is to supply that evidence. Each link below quotes both
sides in English and Arabic, word for word from the projections. A link means "this priority would supply evidence
the Reading says is missing". It does not mean the priority would settle the Reading as a whole. Where only part of a
Reading's unknown is covered, the record says which part.

Where the binding is stored: Master `08_READINGS`, column 20 (T) `measurement_bindings`, rows 5–14 (header on
row 4). Each cell holds a JSON array written without spaces, for example `["MA-005"]`, the same form as
`related_readings` (`["CWR-002","CWR-004"]`). The validator `scripts/projection/derived.py` (`reading_relations`,
lines 797–803) accepts any list of existing MA ids. The same cells drive "This gap is examined in" on
`/measurement/`.

## Summary

| Reading | Today | Proposed | Change |
|---|---|---|---|
| CWR-001 Same year, different number | `[]` | `["MA-001"]` | add (covers part of the unknown, see below) |
| CWR-002 Banking jump / measurement basis | `[]` | `[]` | none: no priority fits (gap recorded) |
| CWR-003 Define what you count | `["MA-005"]` | `["MA-005","MA-002"]` | keep MA-005, add MA-002 |
| CWR-004 Reforms newer than people evidence | `["MA-001"]` | `["MA-001"]` | keep |
| CWR-005 Digital workaround, not yet durable | `["MA-002"]` | `["MA-002"]` | keep |
| CWR-006 Microfinance structural divergence | `[]` | `["MA-005"]` | add (covers part of the unknown, see below) |
| CWR-007 Gender gap measured, causes open | `["MA-003"]` | `["MA-003","MA-007"]` | keep MA-003, add MA-007 |
| CWR-008 Finance constraint, different questions | `["MA-004"]` | `["MA-004"]` | keep |
| CWR-009 From rail to result | `["MA-010"]` | `["MA-010","MA-006"]` | keep MA-010, add MA-006 |
| CWR-010 After the transfer | `["MA-009"]` | `["MA-009"]` | keep |

All seven existing bindings are correct, and none is proposed for removal. After the change, 9 of the 10 Readings
carry one or two links. CWR-002 carries none, for the reason given in its section.

---

## CWR-001 · Same year, different number (`/readings/same-year-different-number/`)

Master cell: `08_READINGS` r5 c20 `measurement_bindings`, from `[]` to `["MA-001"]`.

The Reading has two unknowns:

1. **The main unknown: the method behind the restated series.** No priority addresses it (see "Gaps in the agenda").
   - EN (what_would_change): "A primary methodological note linking the restated CBY-Aden series to the external-sector reconstruction would change the analysis materially."
   - AR: "من شأن مذكرة منهجية صادرة عن المصدر نفسه، تربط سلسلة البنك المركزي في عدن المعاد عرضها بإعادة بناء إحصاءات القطاع الخارجي، أن تغيّر التحليل تغييرًا جوهريًا."
2. **The household side, which this link covers.**
   - EN (boundary, "What this evidence does not tell us"): "It says nothing about how remittances are distributed across households, governorates or channels."
   - AR: "ولا تقول شيئًا عن توزيع التحويلات بين الأسر أو المحافظات أو القنوات."

**Link → MA-001 · A current people-side inclusion baseline**
- Priority purpose, EN (missing_evidence): "New representative Yemen demand-side survey or equivalent approved microdata with weights and clear coverage, including remittance receipt, channel and frequency."
- AR: "مسح تمثيلي جديد للطلب في اليمن، أو بيانات فردية موزونة ومعتمدة ذات تغطية واضحة، يشمل تلقي الحوالات وقنواته وتكراره."
- Why it fits: MA-001 names remittance receipt and channel at the household level, which is the distribution the Reading's boundary says the evidence lacks. MA-001 already lists `/remittances/` among its routes, and that is this Reading's domain page.
- Limit, to keep in view: MA-001 does not explain the vintage revision, and a household survey cannot be converted into a balance-of-payments value. This is SL-010 in `13_SYSTEM_RELATIONSHIPS`: "Household percentages can be converted into macro values without a valid bridge" is not supported. The link points to the evidence on distribution only.

## CWR-002 · Banking jump / measurement basis (`/readings/banking-jump-measurement-basis/`)

Master cell: `08_READINGS` r6 c20 stays `[]`. No change is proposed.

- Stated unknown, EN (evidence_break): "It does not provide a line-by-line bridge showing how much of each restated balance comes from valuation, classification, coverage or economic movement, so that decomposition remains open."
- AR: "لكنها لا تقدم جسرًا بندًا ببند يبين مقدار ما يعود في كل رصيد معاد عرضه إلى التقييم أو التصنيف أو نطاق التغطية أو الحركة الاقتصادية الفعلية، ولذلك يبقى هذا التفكيك مفتوحًا."
- EN (boundary): "The evidence does not yet include a verified line-by-line reconciliation of the old and new 2022 bases."
- AR: "لا تتضمن الأدلة حتى الآن مطابقة بندًا ببند جرى التحقق منها بين أساس 2022 القديم والأساس المعاد عرضه."

**Why no link.** No priority's purpose is a reconciliation of a restated statistical series. Each candidate was
checked and rejected:
- MA-008 (credit-infrastructure reach) and MA-004 (firm-finance journey) would answer "more borrowers" or "wider
  access". The Reading lists those as "separate questions, each with its own evidence". They are not the unknown it
  states.
- MA-010 (reform transmission) concerns payment reforms, not balance-sheet valuation.

Linking any of these would suggest that the measurement would resolve the restatement, and it would not. See "Gaps in
the agenda".

## CWR-003 · Define what you count (`/readings/define-what-you-count/`)

Master cell: `08_READINGS` r7 c20, from `["MA-005"]` to `["MA-005","MA-002"]`.

**Keep → MA-005 · A register of active financial access points**
- Reading unknown, EN (evidence_programme): "Nor can it be added to, or compared directly with, counts of ATMs, POS terminals or agents unless the project’s access-point definitions and de-duplication rules are documented, and in the evidence base they are not."
- AR: "ولا يجوز جمعه مع أعداد أجهزة الصراف الآلي أو نقاط البيع أو الوكلاء، أو مقارنته بها مباشرة، ما لم تُوثَّق تعريفات المشروع لنقاط الوصول وقواعد إزالة الازدواج، وهي غير موثقة في قاعدة الأدلة."
- Priority purpose, EN (missing_evidence): "An authoritative or jointly documented register of individual access points recording type, active status, date, location and services, plus population denominators and road-network data that allow coverage and travel distance or time to be calculated."
- AR: "سجل رسمي أو موثق بالاشتراك لنقاط الوصول فرادى، يسجل النوع ووضع النشاط والتاريخ والموقع الجغرافي والخدمات المتاحة، مع قواعد احتساب سكانية وأخرى لطرق الوصول تسمح بحساب التغطية ومسافة الوصول أو زمنه."
- Why it fits: a register of individual access points that records type and active status is the documented,
  de-duplicable unit the Reading says is missing.

**Add → MA-002 · Active and repeat digital use**
- Reading unknown, EN (evidence_unit): "A person can hold several accounts; an account can generate many transactions; a registered subscriber may be inactive."
- AR: "وقد يملك الشخص أكثر من حساب، وقد يولد الحساب الواحد معاملات كثيرة، وقد يكون المشترك المسجل غير نشط."
- EN (interpretation_drift, the checklist): "What makes the unit active, or included?"
- AR: "ما الذي يجعل الوحدة نشطة أو مشمولة؟"
- Priority purpose, EN (missing_evidence): "Provider/rail administrative data with deduplication rules and/or demand-side active-use measures."
- AR: "بيانات إدارية من مقدمي الخدمة أو أنظمة الدفع مع قواعد إزالة الازدواج، أو مقاييس طلب تقيس الاستخدام النشط."
- EN (unlocked_decision): "This evidence would distinguish registration or temporary activity from repeat use, merchant use and sustained financial use."
- AR: "من شأن هذا القياس أن يميّز بين التسجيل أو النشاط المؤقت وبين الاستخدام المتكرر والاستخدام لدى التجار والاستخدام المالي المستمر."
- Why it fits: the Reading's drift chain (accounts → registered accounts → active wallets → transactions) is the
  registration-versus-use problem. MA-002 supplies de-duplication rules and an activity rule for it.

## CWR-004 · Reforms newer than people evidence (`/readings/reforms-newer-than-people-evidence/`)

Master cell: `08_READINGS` r8 c20 stays `["MA-001"]`. No change.

- Reading unknown, EN (strongest_reading): "The gap between the two is not an answer to guess; it is the next thing to measure."
- AR: "والفجوة بين الأمرين ليست نتيجة يجوز افتراضها؛ إنها ما ينبغي قياسه تاليًا."
- EN (what_would_change): "A new representative measurement of people that keeps comparability on account ownership and adds:"
- AR: "قياس سكاني ممثل جديد يحافظ على قابلية المقارنة في امتلاك الحساب، ويضيف:"
- Priority purpose (MA-001), EN (unlocked_decision): "A current population measure would allow change since the previous wave to be assessed without projecting reform results onto the population."
- AR: "من شأن هذا القياس أن يسمح بتقييم التغير منذ الموجة السابقة من دون إسقاط نتائج الإصلاح على السكان."
- Why it fits: the two texts describe the same measurement almost word for word, and the binding is correct. A second
  link is not needed. The Reading's list also names repeated digital use (MA-002) and persistence after a transfer
  (MA-009), but its stated unknown is the population baseline.

## CWR-005 · Digital workaround, not yet durable inclusion (`/readings/digital-workaround-not-yet-durable-inclusion/`)

Master cell: `08_READINGS` r9 c20 stays `["MA-002"]`. No change.

- Reading unknown, EN (strongest_reading): "The open question is whether people choose to return to digital finance and find enough value to keep using it."
- AR: "والسؤال المفتوح هو: هل يعود الناس إلى الخدمات المالية الرقمية باختيارهم، ويجدون فيها منفعة تكفي للاستمرار في استخدامها؟"
- Priority purpose (MA-002), EN (unlocked_decision): "This evidence would distinguish registration or temporary activity from repeat use, merchant use and sustained financial use."
- AR: "من شأن هذا القياس أن يميّز بين التسجيل أو النشاط المؤقت وبين الاستخدام المتكرر والاستخدام لدى التجار والاستخدام المالي المستمر."
- Why it fits: return use and persistence beyond registration are exactly what MA-002 measures. The binding is correct.

## CWR-006 · Microfinance structural divergence (`/readings/microfinance-structural-divergence/`)

Master cell: `08_READINGS` r10 c20, from `[]` to `["MA-005"]`.

The Reading has two unknowns:

1. **The main unknown: a reconciled provider-level panel.** No priority addresses it (see "Gaps in the agenda").
   - EN (what_would_change): "Answering them needs a reconciled provider-level panel with stable definitions for unique active borrowers, unique active depositors or savers, balances and outstanding exposure, loan size, portfolio quality, geography, provider type, operating status, and complaints and customer outcomes, together with explicit rules for provider coverage, de-duplication, and prices or exchange rates when nominal values are compared over time."
   - AR: "وتتطلب الإجابة عنها بيانات طولية مطابَقة على مستوى مقدمي الخدمة، بتعريفات ثابتة للمقترضين الفريدين النشطين، والمودعين أو المدخرين الفريدين النشطين، والأرصدة والتمويل القائم، وحجم القرض، وجودة المحفظة، والجغرافيا، ونوع مقدم الخدمة، وحالة التشغيل، والشكاوى ونتائج العملاء، مع قواعد صريحة لنطاق مقدمي الخدمة، وإزالة الازدواج، ومعالجة الأسعار أو سعر الصرف عند مقارنة القيم الاسمية عبر الزمن."
2. **Licence versus operation, which this link covers.**
   - EN (evidence_institutions): "A listing or licence establishes an institutional status. It does not establish current operation, geographic reach, client mix or outreach, so institutional change can matter without answering the inclusion question."
   - AR: "ويثبت الإدراج أو الترخيص وضعًا مؤسسيًا، لكنه لا يثبت التشغيل الحالي ولا الانتشار الجغرافي ولا تركيبة العملاء ولا حجم الوصول؛ ولذلك قد يكون التغير المؤسسي مهمًا من دون أن يجيب عن سؤال الشمول."

**Link → MA-005 · A register of active financial access points**
- Priority purpose, EN (unlocked_decision): "This evidence would distinguish listing and licensing from operation and observed access before any access or opportunity map is interpreted."
- AR: "من شأن هذا القياس أن يميّز بين الإدراج والترخيص من جهة، وبين التشغيل والوصول المرصود من جهة أخرى، قبل تفسير أي خريطة للوصول أو الفرص."
- Why it fits: both texts draw the same line, licence ≠ operation. A dated register of operating access points, with
  location, is the evidence of "current operation" and "geographic reach" for the twelve microfinance banks. MA-005
  already lists `/providers/`, one of this Reading's two domain pages.
- Limit, and a decision for the steward: MA-005 says nothing about borrower or saver harmonisation, nominal versus real
  portfolio, client mix or outreach. If the steward reads this as too partial, leave the cell `[]` and record CWR-006
  next to CWR-002 under "Gaps in the agenda".

## CWR-007 · Gender gap measured, causes open (`/readings/gender-gap-measured-causes-open/`)

Master cell: `08_READINGS` r11 c20, from `["MA-003"]` to `["MA-003","MA-007"]`.

**Keep → MA-003 · Financial inclusion across population groups**
- Reading unknown, EN (strongest_reading): "The evidence tells us where the disparity is. It does not yet tell us which barriers produce it."
- AR: "تخبرنا الأدلة أين يقع التفاوت، لكنها لا تخبرنا بعدُ أي العوائق تنتجه."
- Priority purpose, EN (unlocked_decision): "This evidence would show which subgroup differences are actually measured and would allow plausible mechanisms to be tested without treating untested explanations as causes."
- AR: "من شأن هذا القياس أن يوضح الفروق التي قِيست فعليًا بين الفئات، وأن يتيح اختبار الآليات المحتملة من دون معاملة التفسيرات غير المختبرة بوصفها أسبابًا."
- Why it fits: measuring a disparity before explaining it is the Reading's own argument.

**Add → MA-007 · Digital onboarding and identity journeys**
- Reading unknown, EN (what_would_change, closing question): "If we can measure the gap but cannot yet locate where women are being lost — at access, activation, use, persistence or quality — how can we know that an intervention is aimed at the right problem?"
- AR: "إذا كنا نستطيع قياس الفجوة، لكننا لا نعرف بعدُ أين تخرج النساء من المسار — عند الوصول أو التفعيل أو الاستخدام أو الاستمرار أو الجودة — فكيف نعرف أن التدخل موجَّه إلى المشكلة الصحيحة؟"
- EN (interpretation_journey): "Provider data can follow the same path from the other side: applications, approvals, rejections, active use, dormancy, balances, credit, complaints, fraud, resolution and exit, each with a visible denominator."
- AR: "ويمكن لبيانات مقدمي الخدمة أن تتتبع المسار نفسه من الجهة الأخرى: الطلبات، والموافقات، وحالات الرفض، والاستخدام النشط، والخمول، والأرصدة، والائتمان، والشكاوى، والاحتيال، ومعالجتها، والخروج، مع إظهار قاعدة الاحتساب لكل منها."
- Priority purpose, EN (unlocked_decision): "This evidence would identify where users leave or fail the onboarding journey and which frictions are associated with those points."
- AR: "من شأن هذا القياس أن يحدد أين يترك المستخدمون مسار الانضمام أو يتعثرون فيه، وما الاحتكاكات المرتبطة بتلك النقاط."
- EN (missing_evidence): "Journey-level administrative or survey data across onboarding stages: identity and KYC verification, attempts, completion, rejection, abandonment, time and cost."
- AR: "بيانات إدارية أو مسحية على مستوى رحلة الانضمام عبر مراحلها: التحقق من الهوية وإجراءات «اعرف عميلك» (KYC)، والمحاولة، والإكمال، والرفض، والانسحاب، والوقت، والتكلفة."
- Why it fits: the Reading asks where on the journey women are lost, and names identity documents among the
  hypotheses (interpretation_mechanism). MA-007 is the journey-stage measurement, from identity and KYC through to
  rejection and abandonment. MA-007 already lists `/people/`, which is this Reading's domain page.
- Limit: MA-007 does not itself promise disaggregation by sex. That comes from MA-003, so the two links are meant to
  be read together.

## CWR-008 · Finance constraint, different questions (`/readings/finance-constraint-different-questions/`)

Master cell: `08_READINGS` r12 c20 stays `["MA-004"]`. No change.

- Reading unknown, EN (boundary): "None of this supports a current national rate of MSME access to finance, or a causal effect."
- AR: "ولا يسند شيء من ذلك معدلًا وطنيًا حاليًا لوصول المنشآت الأصغر والصغيرة والمتوسطة إلى التمويل، ولا أثرًا سببيًا."
- EN (what_would_change): "A current, representative measure of the firm-finance journey — need, demand, application or discouragement, approval, terms, source, use and outcome — linked to firm size, sector, formality, ownership, the owner’s sex where statistically supportable, geography and the other operating constraints firms face."
- AR: "قياس حديث وممثل لمسار تمويل المنشأة — الحاجة، والطلب، والتقدم بطلب أو الإحجام عنه، والموافقة، والشروط، والمصدر، والاستخدام، والنتيجة — مرتبطًا بحجم المنشأة وقطاعها ورسميتها وملكيتها، وجنس المالك حيث يسمح الإحصاء بذلك، والجغرافيا، وبقية قيود التشغيل التي تواجهها."
- Priority purpose (MA-004), EN (missing_evidence): "A representative survey of firms/MSMEs, or validated administrative data linked to firm-level data, with explicit definitions, covering finance need, application, approval or rejection, amount, terms, source, use, repayment pressure and outcome."
- AR: "مسح ممثل للمنشآت الأصغر والصغيرة والمتوسطة، أو بيانات إدارية متحقق منها ومربوطة ببيانات على مستوى المنشأة، بتعريفات صريحة، يغطي الحاجة إلى التمويل والتقديم والموافقة أو الرفض والمبلغ والشروط والمصدر والاستخدام وضغوط السداد والنتيجة."
- Why it fits: the two texts describe the same journey, stage for stage. The binding is correct. MA-008 (credit
  infrastructure) does not answer anything this Reading asks.

## CWR-009 · From rail to result (`/readings/from-rail-to-result-missing-middle/`)

Master cell: `08_READINGS` r13 c20, from `["MA-010"]` to `["MA-010","MA-006"]`.

**Keep → MA-010 · Reform transmission and service quality**
- Reading unknown, EN (boundary): "For each major reform or system change, monitoring should identify the furthest stage that is actually evidenced and then ask for the next missing link."
- AR: "ولكل إصلاح رئيسي أو تغير في المنظومة، ينبغي أن تحدد المتابعة أبعد مرحلة أثبتتها الأدلة فعلًا، ثم تسأل عن أول حلقة مفقودة بعدها."
- Priority purpose, EN (unlocked_decision): "This evidence would show the furthest evidenced state of each reform and the next unmeasured result without treating missing evidence as failure."
- AR: "من شأن هذا القياس أن يُظهر أبعد مرحلة تثبتها الأدلة لكل إصلاح، والنتيجة التالية التي لم تُقَس بعد، من دون اعتبار غياب الدليل فشلًا."
- Why it fits: the texts are near-identical. The binding is correct.

**Add → MA-006 · Consumer experience and redress outcomes**
- Reading unknown, EN (strongest_reading): "A rule can be issued, infrastructure can expand, institutions can be created and transactions can appear while evidence on reach, repeated use, service quality, protection and outcomes remains incomplete."
- AR: "قد تصدر قاعدة جديدة، وتتوسع البنية التحتية، وتنشأ مؤسسات، وتظهر معاملات، بينما يظل ما نعرفه عن الوصول الفعلي والاستخدام المتكرر وجودة الخدمة والحماية والنتائج ناقصًا."
- EN (boundary): "use may be proven while reliability, cost or redress remain open"
- AR: "وقد يثبت الاستخدام بينما تبقى الموثوقية أو الكلفة أو الانتصاف مفتوحة"
- Priority purpose, EN (unlocked_decision): "This evidence would allow redress performance and service quality to be assessed rather than inferred from the existence of rules."
- AR: "من شأن هذا القياس أن يسمح بتقييم أداء التظلم وجودة الخدمة بدل استنتاجهما من مجرد وجود القواعد."
- Why it fits: the "quality and protection" link in the Reading's chain is the one MA-006 measures. Its "rather than
  inferred from the existence of rules" restates the Reading's argument. MA-006 already lists `/reforms/`, one of this
  Reading's domain pages. The Master's own relationship SL-015 already pairs MA-006 with MA-010 for downstream
  redress and service-quality evidence.

## CWR-010 · After the transfer (`/readings/after-transfer-persistence/`)

Master cell: `08_READINGS` r14 c20 stays `["MA-009"]`. No change.

- Reading unknown, EN (opening): "But possibility is not persistence. The available Yemen evidence does not yet tell us whether recipients used those accounts between transfers, kept balances in them, received other money, paid merchants or bills, made transfers of their own, switched providers, or kept using the account after the programme payments that prompted it weakened or ended. That is the missing observation."
- AR: "لكن الإمكانية لا تعني الاستمرار. فالأدلة المتاحة عن اليمن لا تخبرنا بعدُ ما إذا كان المستفيدون قد استخدموا هذه الحسابات بين دفعة وأخرى، أو أبقوا فيها أرصدة، أو تلقوا فيها أموالًا من خارج البرنامج، أو دفعوا منها لتجار أو سددوا فواتير، أو أجروا تحويلات بمبادرتهم، أو بدّلوا مقدم الخدمة، أو واصلوا استخدام الحساب بعد أن ضعفت دفعات البرنامج التي دفعتهم إليه أو انتهت. وهذه هي الملاحظة المفقودة."
- Priority purpose (MA-009), EN (missing_evidence): "Longitudinal programme or provider cohort data, or repeated beneficiary follow-up, with privacy-safe linkage from transfer receipt to account or wallet activation, repeat use, merchant use, saving and cash-out."
- AR: "بيانات طولية لمجموعات المستفيدين من البرنامج أو مقدم الخدمة، أو متابعة متكررة للمستفيدين، تربط، بطريقة تحمي الخصوصية، استلامَ التحويل النقدي بما يليه من تفعيل الحساب أو المحفظة الإلكترونية، والاستخدام المتكرر، والاستخدام لدى التجار، والادخار، والسحب النقدي."
- Why it fits: the Reading's "what would change" names "A longitudinal follow-up of recipients", and that is MA-009.
  The binding is correct. CWR-010 is the Reading through which MA-009 becomes reachable (see the table below).

---

## Gaps in the agenda (recorded, not filled)

- **Reconciling a restated official series.** No priority covers a bridge between the vintages of a restated
  official series:
  - CWR-001: the method note linking the restated CBY-Aden remittance series to the external-sector reconstruction.
  - CWR-002: the line-by-line reconciliation of the January 2023 banking restatement.

  This is why CWR-002 has no link and CWR-001's link covers only its household-side unknown. Closing it would take a
  new priority (MA-011), authored in both languages by the programme steward. That is a content decision, so it is
  not proposed here.
- **A reconciled microfinance provider panel (CWR-006).** No priority covers unique active borrowers and savers,
  outstanding exposure, or nominal-to-real treatment across providers. MA-005 covers only the licence-versus-operation
  part.

## Reachability of each priority

A priority counts as reachable when a Reading page or a domain answer page carries a link to `/{lang}/measurement/#MA-0xx`.
- "Today" comes from grepping `dist/en` and `dist/ar` (the two languages are identical).
- `/explore/`, `/evidence/` and `/measurement/` are hubs, not domain pages, so they are listed separately.
- A domain page shows only the first `measurement_limit` priorities (2, or 1 on `/remittances/`) of its governed list,
  in MA id order. These limits are set in `presentation_priority.json`, a controlled contract.

| MA | Governed for (affected_route_list) | Linked today from domain pages | Linked today from Readings | Hubs today | After the proposal (Readings) | Reachable after? |
|---|---|---|---|---|---|---|
| MA-001 | /people/, /, /explore/, /remittances/ | /people/, /remittances/ | none | /explore/ | CWR-001, CWR-004 | yes |
| MA-002 | /payments/, /people/, /reforms/ | /payments/, /people/, /reforms/ | none | none | CWR-003, CWR-005 | yes |
| MA-003 | /people/, /explore/ | **none** (cut by the limit of 2 on /people/) | none | /explore/ | CWR-007 | yes |
| MA-004 | /firms/, /finance/, /explore/ | /firms/, /finance/ | none | /explore/ | CWR-008 | yes |
| MA-005 | /access/, /providers/, /explore/ | /access/, /providers/ | none | /explore/ | CWR-003, CWR-006 | yes |
| MA-006 | /reforms/, /evidence/, /explore/ | /reforms/ | none | /evidence/, /explore/ | CWR-009 | yes |
| MA-007 | /people/, /payments/, /providers/ | /payments/, /providers/ | none | none | CWR-007 | yes |
| MA-008 | /finance/, /firms/, /reforms/ | /finance/, /firms/ | none | none | none (no Reading's unknown fits) | yes (domain pages) |
| MA-009 | /payments/, /people/, /reforms/ | **none** (3rd, 5th and 4th on those lists, all cut by the limit of 2) | none | none | CWR-010 | yes |
| MA-010 | /reforms/, /payments/, /access/, /people/ | /access/ | none | none | CWR-009 | yes |

"Linked today from Readings" is empty for every priority because no Reading page renders its `measurement_bindings`
yet; the bindings for seven Readings exist in the Master but never reach the page. MA-009 and MA-003 are reachable
today only from `/measurement/` (and MA-003 from `/explore/`).

Once the Reading pages render their bindings, every priority is reachable from a page where it genuinely belongs:
MA-008 from its two domain pages, and every other priority from at least one Reading. No change to
`presentation_priority.json` is needed for B6. Raising `measurement_limit` on `/people/`, `/payments/` or `/reforms/`
would also put MA-009 on its domain pages, but that is a steward decision and is not proposed here.

`/measurement/` "This gap is examined in" (built from the same cells) after the change:
- MA-001: CWR-001, CWR-004
- MA-002: CWR-003, CWR-005
- MA-003: CWR-007
- MA-004: CWR-008
- MA-005: CWR-003, CWR-006
- MA-006: CWR-009
- MA-007: CWR-007
- MA-008: none
- MA-009: CWR-010
- MA-010: CWR-009

## /measurement/: `decisions_unlocked` and `blocked_evidence`

**Governed?** Yes.
- Both fields are Master columns of `10_MEASUREMENT_AGENDA`: P `decisions_unlocked_en`, Q `decisions_unlocked_ar`,
  R `blocked_evidence_en` and S `blocked_evidence_ar` (columns 16–19, rows 5–14).
- They are declared in `scripts/projection/master_structure.json` (lines 219–222) and projected to
  `measurement_agenda.json`.
- They were part of the RF5 bilingual editorial corpus (`audit/final_integration/rf5_corpus.py` line 40). Every F5
  finding on these fields has been applied in the current text: qmc-005, qmc-008, qmc-030, qmc-031, qmc-039 and qmc-044.

**Complete in both languages?** Yes, for all 10 priorities.

| MA | decisions_unlocked EN items | AR items | blocked_evidence EN | AR |
|---|---|---|---|---|
| MA-001 | 3 | 3 | present | present |
| MA-002 | 3 | 3 | present | present |
| MA-003 | 3 | 3 | present | present |
| MA-004 | 3 | 3 | present | present |
| MA-005 | 3 | 3 | present | present |
| MA-006 | 3 | 3 | present | present |
| MA-007 | 3 | 3 | present | present |
| MA-008 | 3 | 3 | present | present |
| MA-009 | 3 | 3 | present | present |
| MA-010 | 3 | 3 | present | present |

**Shown today?** No.
- `/measurement/` shows current evidence, missing evidence and the single `unlocked_decision` ("Decision it would
  strengthen").
- Its "More about this priority" section shows the guardrail, feasibility, priority basis and what would change.
- Neither field appears in `dist/en/measurement/index.html` or `dist/ar/measurement/index.html`, and they are not in
  `audit/PUBLIC_LITERAL_CLOSURE.json`.

**What is missing before they can be shown:**
1. **A clean list format.** `decisions_unlocked_*` is one string with the items joined by commas. Some English items
   contain commas themselves: MA-003 items 1–2, MA-004 item 1 and MA-009 item 2. A plain split on `,` therefore
   gives 9, 5 and 4 items. Splitting on a comma that follows the end of a sentence gives exactly 3 items in both
   languages for every priority: `(?<=[.?]),` in English and `(?<=[.؟?]),` in Arabic.
   - Recommendation: render with that split, and add a gate that EN item count == AR item count == 3.
   - Alternatively, the steward can convert the cells to JSON arrays in the Master, but `dimensions_en` and
     `dimensions_ar` already use mixed formats, so this is not required for B6.
2. **Two interface labels in both languages, which do not exist yet** (new rows in `04_NAV_UX`, columns `ui_id`,
   `label_en`, `label_ar`, `use_rule`). Wording proposed for the steward and the Arabic reviewer:
   - `UI-MA-DECISIONS`: EN "Questions it would answer:" / AR "الأسئلة التي سيجيب عنها القياس:"
   - `UI-MA-BLOCKED`: EN "Evidence that cannot be produced without it:" / AR "الدليل الذي لا يمكن إنتاجه من دونه:"
3. **Small Arabic points to check once the text is visible.** None blocks B6.
   - MA-010 `decisions_unlocked_ar` item 3 spells «تالياً», while the house form elsewhere is «تاليًا» (for example
     CWR-004).
   - MA-005 `missing_evidence_ar` renders "road-network data" as «قواعد احتساب … لطرق الوصول». This is already
     public on `/access/` and `/providers/`, and will now also appear on CWR-003 and CWR-006.
   - MA-001 `missing_evidence_ar` uses «الحوالات» for remittances, where CWR-001's essay uses «التحويلات». This is
     probably a deliberate choice to keep remittances apart from «التحويلات النقدية» (cash transfers, MA-009).


## Applied (RC-9, 3 October 2026)

- The five bindings in the summary table, written exactly as proposed.
- Labels `UI-MA-DECISIONS` ("Questions it would answer:" / «الأسئلة التي سيجيب عنها القياس:») and `UI-MA-BLOCKED`
  ("Evidence that cannot be produced without it:" / «الأدلة التي لا يمكن إنتاجها من دونه:»; plural, like the existing
  «الأدلة الناقصة:»).
- `decisions_unlocked` is split on a comma that follows a sentence end (`(?<=[.?؟]),`). That gives three items in each
  language for every priority, and gate RC-B6 holds the counts equal.
- MA-010 `decisions_unlocked_ar`: «تالياً» → «تاليًا».
- Not changed: the MA-005 and MA-001 Arabic points above (house choices, already public); `presentation_priority.json`
  (a steward decision; every priority is reachable without it).
- Currentness lines for people-side evidence, checked for the same transaction: the Global Findex 2025 edition's
  non-coverage of Yemen, and the latest wave's exclusions (Al Baydaa, Al Jawf, Mareb, Sadah, Socotra and several
  districts; about 23% of the population). Both are already stated: CLM-002, CLM-027, VIS-FINDEX-ACCESS-USE and
  VIS-FINDEX-OBSERVED-WAVES for the first; CLM-025 and /people/ for the second. Result: MATCH; nothing to add.

## Independent review of RC-9, applied in RC-9b (3 October 2026)

One bilingual reviewer who did not write B6 read it, Arabic first. Verdict: NOT ACCEPTABLE, with one blocking finding.
All findings are applied in `rc_10_evidence_landscape.py`, tagged RC-9b, in cells RC-10 does not touch.

- **Blocking: CWR-001 → MA-001 removed.**
  - The Reading concerns balance-of-payments inflows, i.e. cross-border personal transfers. Its unknown is how those
    inflows are distributed across households, governorates and channels.
  - MA-001's remittance evidence is domestic household receipt («الحوالات المحلية»), and its missing evidence names
    neither receipt from abroad nor amounts. The link therefore mixed two universes.
  - CWR-001 now joins CWR-002 under "Gaps in the agenda". No priority covers the distribution of the balance-of-payments
    remittance flow.
  - Widening MA-001 to receipt from within Yemen and from abroad would close this gap, but that is a content decision
    for the programme steward and is not taken here.
  - MA-001 stays reachable from CWR-004, /people/ and /remittances/.
- **S1: what a link means.** Reading pages print a line under "Related measurement priorities", from the new label
  `UI-READING-MEASUREMENT-NOTE`: "Each priority below would supply evidence that this Reading says is missing; the link
  does not mean the priority would settle the Reading."
- **S2–S5: Arabic in `decisions_unlocked_ar`.**
  - MA-002: «النشاط الإداري» → «النشاط المسجل في البيانات الإدارية».
  - MA-007: «خطوات الهوية/اعرف عميلك … أكبر احتكاك» → «خطوات التحقق من الهوية وإجراءات «اعرف عميلك» … احتكاكًا».
  - MA-004: «وكم تتقدم» → «وكم تتقدم بطلب».
  - MA-005: «ما السكان» → «ما الفئات السكانية».
- **Accepted as checked.**
  - The two labels.
  - All 20 decision lists: three items each, in the same order in both languages, and an exact match to the governed
    strings.
  - The other four links.
  - The semantic firewall on the changed pages.

After RC-9b, 8 of the 10 Readings carry links; CWR-001 and CWR-002 are recorded gaps.
