# Tranche C — Lead drafting rules (binding for every drafting agent)

You DRAFT replacement text. You never edit the repository. The Team Lead reviews every draft before anything reaches the
Production Master. Drafts that add facts, change numbers, or weaken a limitation are rejected.

## A. Absolute constraints
1. No new facts. Use only what the governed record, its bound data rows (site-src/content/data/*.json), its passport
   (site-src/content/evidence/evidence_passports.json), its source records (site-src/content/sources/source_library.json)
   and the rendered page already hold. If a sentence needs a fact that is not governed, do not write it; flag it in
   `lead_note`.
2. Numbers, units, periods, universes, geography and evidence states must survive exactly (same digits, same precision).
   Never round, never add a figure.
3. Every prohibited inference and every limitation in the current text must survive in the new text as a statement of
   what the evidence does NOT establish/show. Rewording must not weaken certainty or scope.
4. English and Arabic are co-authored editions: the same meaning, numbers, scope, limitation and certainty in both.
   Write each natively; do not translate word-for-word.
5. Keep the publication firewall: never name or quantify material that has no public locator (CCY family, CLM-044 value,
   SRC-LIT-*, SRC-MOPIC). Do not add rights claims, licence claims, WCAG/legal/security claims or response times.
6. Conflict is context, not cause: never add a causal explanation.

## B. Field rules for Evidence Records (Master 06_EVIDENCE_OBJECTS)
- `title_en/_ar` ("the record's name"): plain sentence-case title saying what the evidence is. No product nicknames
  ("Time Machine", "Spine", "Lab", "Pulse"), no slash taxonomies ("Demand-side / …"), no internal nouns ("contract",
  "object", "panel contract", "negative-authority", "study contract"). Only change a title if it has one of these defects.
- `definition_en/_ar` (rendered under "What does it measure?"): ONE plain sentence naming the measured object/unit, the
  population or universe, and the period where the record holds it. For a record that states a method rule or framing
  and measures nothing, say that plainly (e.g. "This record sets out a measurement rule; it reports no value."). Never
  "A visual summary of the evidence…", never object-class taxonomy ("Actor-specific regulatory status event").
- `method_en/_ar` (rendered under "How was it produced?"): how the underlying evidence was produced — source type,
  collection, the source's tabulation, and for CauseWay-derived values the inputs and the rule (e.g. "Difference between
  two published weighted estimates: men 18.35% minus women 5.44%"). Never chart-drawing instructions ("Plot…",
  "Annotate…", "bars sorted…", "progress bar only after compatibility PASS", "node OPEN", "funnel").
- `limitations_en/_ar` = "A | B". A = what this evidence does NOT establish; B (optional) = limits of the measure.
  * A must be DECLARATIVE statements about the evidence: "It is not a 2026 rate and cannot be mapped to governorates."
    Not imperatives ("Do not…", "Never…", "must…", «لا يجوز…»), not instructions to publishers or designers
    ("fields may display", "must remain held", "preserve source wording", "do not allege source misconduct").
  * Preferred EN openers: "It does not establish…", "It is not…", "X is not Y…", "This does not show…".
    Preferred AR: «لا يثبت هذا الدليل…»، «ليس…»، «لا يعني…»، «لا تمثل…». Avoid «لا يجوز».
  * Keep every item of the old A text. Keep the " | " separator only when B exists. Do not merge A into B.
  * B: keep content; fix only imperatives/jargon.
- `currentness_en/_ar` (rendered under "How current is it?"): answer the question. Name the latest observation or
  reference period the record holds and, where governed, whether a newer comparable observation is known. Never
  "Currentness is bounded to…", never "…latest comparable evidence available from a comparable source without a newer
  comparable observation". If the record is a method rule or has no observation date, say so plainly in one sentence.
  Pattern if nothing more specific is governed: EN "The latest observation in this record refers to <period in words>.
  It should not be read as describing a later period unless a newer comparable observation is published." AR «تعود أحدث
  مشاهدة في هذا السجل إلى <الفترة>، ولا تُقرأ على أنها تصف فترة لاحقة ما لم تُنشر مشاهدة أحدث قابلة للمقارنة.»
  Write periods in words ("March 2025 to January 2026", «من مارس 2025 إلى يناير 2026»), not codes ("Mar-2025–Jan-2026",
  "AR2022 vs AR2023+" → "the 2022 and 2023 annual reports").
- `change_trigger_en`: descriptive, not imperative: "This record is updated when …". `change_trigger_ar`: keep the
  passive «يُحدَّث هذا السجل عند …» but use «المصدر المعتمد» not «المصدر المرجعي».
- `summary_en/_ar`: change only where a panel finding requires it (see below). Keep figures identical.

## C. Terminology (Lead decisions)
- The central bank in Aden. EN prose: "the Central Bank of Yemen – Aden (CBY-Aden)" at first mention in a field, then
  "CBY-Aden". Never bare "CBY" when attributing an issuing authority, a list, a decision or a reporting scope.
  AR: «البنك المركزي اليمني – عدن» at first mention, then «البنك المركزي في عدن». Never bare «البنك المركزي» for an
  issuing/reporting authority. Do not use «المركز الرئيسي».
- Reporting scope of CBY-Aden payment statistics: "within CBY-Aden's reporting scope"; never "national" totals.
- IMF remittance series scope: "on the IMF's analytical scope for areas under the internationally recognized government".
  EN: spell out "internationally recognized government" (no bare "IRG"); AR «الحكومة المعترف بها دوليًا».
- Remittance lexicon (AR): balance-of-payments inflow series = «التحويلات» (first mention «التحويلات الواردة في ميزان
  المدفوعات»); transfer transactions/channels/providers = «الحوالات» (شركات الصرافة، وكلاء الحوالات، الحوالات المحلية);
  informal channel = «الحوالة غير الرسمية»; social-protection cash transfers = «التحويلات النقدية» (always with
  «النقدية»). Do not use «تحويلات العاملين» unless the source line is literally "workers' remittances" (it is not here).
- Statistical Arabic: indexing = «تحويل السلسلة إلى رقم قياسي (2021 = 100)» (never «التطبيع/مُطبَّع»); reconciliation =
  «مطابقة» (never «مصالحة»); adopted baseline = «المعتمد» (never «الحاكم»); smoothing = «التمهيد/التنعيم» (never
  «التسوية»); universal = «موحّد/ينطبق على كل…» (never «عالمي» for universal); reporting panel = «مجموعة الجهات
  المُبلِّغة» (never «لوحة»); provider universe = «نطاق مقدمي الخدمات» (never «عوالم»); material = «جوهري» (never
  «مادي»); primary (source) = «صادر عن المصدر الأصلي/أولي المصدر» (never «أولية» meaning preliminary); reported =
  «التي يُبلغ عنها» / «المنشورة» / «كما وردت في المصدر» (avoid bare «المبلغ عنها» which reads as "the amount").
- Stages vs status (AR): chain stage = «مرحلة»; a provider's standing = «وضع»; enforcement event = «قرار إنفاذ»;
  observed/estimated/projected = «نوع الدليل». Do not use «حالة» as schema jargon.
- MSMEs (AR): «المنشآت الأصغر والصغيرة والمتوسطة» (not «الصغرى»).
- Self-reference: EN "this resource"; AR «هذا المورد». Never "this product", «المنتج», «هذا الموقع» for the resource.
- Findex (AR): first mention «المؤشر العالمي للشمول المالي (Global Findex)», then «مسح Findex». Never bare «المؤشر العالمي».
- Official names: FMIIP = EN "Financial Market Infrastructure and Inclusion Project (FMIIP)" / AR «مشروع البنية التحتية
  للأسواق المالية والشمول المالي في اليمن (FMIIP)». YPCC = AR «الشركة اليمنية للمدفوعات والمقاصة» (feminine agreement)
  / EN "Yemeni Payments and Clearing Company (YPCC)". IMF SMP = EN "Staff-Monitored Program (SMP)" / AR «برنامج يراقبه
  خبراء صندوق النقد الدولي (SMP)». SFD = "Social Fund for Development (SFD)" / «الصندوق الاجتماعي للتنمية». SMEPS =
  "Small and Micro Enterprise Promotion Service (SMEPS)" / «وكالة تنمية المنشآت الصغيرة والأصغر (SMEPS)» (feminine).
  IBS = "Institute of Banking Studies (IBS)" / «معهد الدراسات المصرفية». Expand an acronym at first use in a field.
- Account ownership (Global Findex definition, verified 26 Sep 2026 from the World Bank API): EN "the share of adults
  aged 15 and over who report having an account, alone or with someone else, at a bank or another type of financial
  institution, or who report personally using a mobile-money service in the past 12 months". AR «نسبة البالغين بعمر 15
  سنة فأكثر الذين أفادوا بامتلاك حساب، منفردين أو بالاشتراك مع غيرهم، لدى بنك أو نوع آخر من المؤسسات المالية، أو
  باستخدامهم الشخصي خدمة أموال عبر الهاتف المحمول خلال الاثني عشر شهرًا السابقة».
- Dates of checks made in this window: POS monthly releases, RPW corridor pages, CBY news list — "as checked on
  26 September 2026" / «كما رُوجع في 26 سبتمبر 2026» (use «اطُّلع عليه» when "reviewed" could be read as "revised").
- Avoid rhetoric: "fingerprint", "laundering", "rupture", "extraordinarily", "powerful", "Pulse", "Time Machine".
  Do not hedge a 2-decimal figure with "about".
- EN register: restrained, economical, no consultancy filler, sentence case, no "≠" or "→" in prose.
