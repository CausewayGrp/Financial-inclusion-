# F5 — Whole public corpus acceptance

**Date:** 26 September 2026 · **Directive:** D7 §F5 · **State:** CLOSED
**Transactions:** RF5 (Master `440614d7…` → `168a0ad8…`, 837 cells) and RF5b (→ `ed3c5796…`, 72 cells), both committed
through `audit/tranche_b_execution/run_stage.py`. Script, inputs, Master ledgers and run reports:
`audit/final_integration/rf5_corpus.py`, `inputs/F5_*`, `inputs/F5B_*`, `runs/RF5*`. Every finding with its Lead
decision: [`F5_CORPUS_FINDINGS_LEDGER.csv`](F5_CORPUS_FINDINGS_LEDGER.csv) (692 rows).

## 1. What was reviewed — every public surface, not a sample

Eleven independent reviewers read the governed public text of the Master under one brief (Arabic read as Arabic by a
senior Arab economic editor; English by an institutional research editor; then meaning parity and the semantic firewall).
Each slice was the complete population of its kind:

| Slice | Content | Objects |
|---|---|---|
| pages_a, pages_b | Every page section of every static and domain route (03) and every route title and meta description the Master owns (02) | 23 routes, 296 section blocks, 23 titles |
| evidence_a/b/c | Every Evidence Record (06), all fields: title, summary, definition, period, population, method, limitations, currentness, change trigger, verification | 110 records |
| claims_visuals | Every visual contract's public text (11), including the ten Reading visuals; public claims carry no own text (they derive from 06) | 36 visuals |
| questions_ma_chronology | Every entry question (05), Measurement priority (10) and chronology event (14) | 11 + 10 + 24 |
| sources | Every source card with public text (15); locator-only records have none | 143 cards |
| interface | Every governed interface label (04), including the `app.js` labels moved into the Master in F4 | 412 labels |
| readings_1, readings_2 | Every Evidence Reading: title, question, thesis, prohibited inference, evidence period (08) and every essay section (03) | 10 Readings |

## 2. Findings and decisions

667 review findings (57 material, 17 query, 593 editorial) plus 25 Lead items found by scanning the staged corpus.

| Decision | Count | Meaning |
|---|---|---|
| Accepted as proposed | 595 | Applied verbatim |
| Accepted, modified | 34 | Applied with the Lead's wording (house term, clearer subject, or a resolved query) |
| Rejected | 26 | Two house rulings (below) and two boundaries kept |
| Superseded | 7 | Same sentence fixed by another finding (usually the visual twin) |
| Deferred | 3 | Need a source that could not be read in this session; recorded as open items (§5) |
| Structural | 2 | One chronology row moved into date order; one duplicate source record retired |
| Lead edits / sweeps | 20 / 5 | Same defects found elsewhere by the Lead's scan |

Every material finding was accepted. The most consequential corrections:

- **Scope restored in Arabic** where the English bounded a figure and the Arabic did not: CBY-Aden payment totals are
  totals *within that bank's reporting scope*, not national (/access/, /payments/); the Fast Payment System is supported
  in areas under the internationally recognized government (/payments/, /reforms/); the OECD/INFE report does not
  establish that the Yemen sample is nationally representative (/people/); microfinance anchors are *among providers
  reporting to SFD* and the 2024 paper is not called a "strong" source (/finance/).
- **Firewall errors removed:** «بدء التشغيل الكامل» ("full go-live", implying partial go-live) → «بدء التشغيل»; «غير
  موجودة» ("does not exist") → «لم يُعثر عليها» ("not located"); "Access is not use" titled a chart of *ownership*;
  "18 formal firms" were 18 *responses*; «الاشتراكات/الأجهزة» (subscriptions/devices) → subscribers/terminals; "exposure
  persists" → use continues; "support sustained use" → associated with; «نتيجة» (as a result of) → «بما يعكس»
  (reflecting); IMF framework for IRG areas, not the government's framework held by the IMF.
- **Queries resolved from the Master's own evidence:** three periods that no bound source supported
  (VIS-OECD-FCP-TIMELINE 2021 → 2023; VIS-DEMAND-VINTAGE-LADDER 2011 → 2014; CLM-040 reconstruction 2014–2025 →
  statistics 2014–2024, per its own summary) and one opaque comparison-rule period.
- **Control language removed** from public prose in both languages: "held", "locator", "universe", "vintage", "content
  version", "promoted", "evidence clocks", "surface", "object", "crosswalk", internal shorthand (AR2025, BOP universe).
- **Directory hygiene:** the Sources page listed the World Bank Saudi Arabia–Yemen corridor page twice under two IDs;
  the unbound duplicate (`SRC-WB-RPW-KSA-YEM-2025Q3`) is retired (source records 161 → 160; public locators 152 → 151).
  The chronology now runs in date order (YSC-018 before YSC-015).

## 3. House rulings (binding for later editing)

- **«فريد / الفريدين»** stays the Arabic term for unique (de-duplicated) people, users, firms and providers. It is used
  consistently in every domain; switching some fields to «دون تكرار» would give one concept two names.
- **Remittances.** «التحويلات» names remittances as a macro or balance-of-payments flow; «الحوالة / الحوالات» stays for
  individual money transfers and their prices (Remittance Prices Worldwide), for person-to-person domestic remittances in
  Findex, and for the licensed exchange-and-remittance sector, where it is the regulator's and the market's own word.
- **Missing here is not non-existent.** Where the evidence base lacks something, the sentence names the evidence base as
  its subject ("the evidence base holds no …", "not recorded in the evidence base"), never "no X is held" or "no X exists".
- **Exposure** is «أول تعامل مع …» (first contact with a formal service), never «التعرض لـ».
- **Durable use** is «مستمر»; «مستدام» is kept only for sustainability in its own sense (macroeconomic stability, a
  publication title).
- **Denominator** is «قاعدة الاحتساب»; **OECD** is «منظمة التعاون الاقتصادي والتنمية»; **CBY-Aden** is
  «البنك المركزي اليمني – عدن» at the first mention in every field or page (a later «البنك المركزي في عدن» is a
  short form; the scan found no field that uses the short form first).
- **Edition, not version.** The resource's dated release is "the edition of this resource dated …" / «إصدار هذا المورد
  المؤرخ …»; the citation line reads "Edition of 26 September 2026" / «إصدار 26 سبتمبر 2026».
- **Twins stay identical.** An edit to an Evidence Record also applies to its visual twin, field by field, and a change to a
  verification template is mirrored into every record that carries it (closure rule v2); the transaction enforces both.

## 4. Trust surfaces — do they describe the real product?

About, Methodology, Contact, Corrections, Rights & reuse, Privacy, Terms and Accessibility were in the page slices and
were read against what the product actually does.

- **About** states CauseWay's role (organising, synthesis, derivations, corrections), that original publishers remain
  authoritative, that the resource confirms no institution's licence or operation, and that nothing is advice. Accurate.
  The CauseWay identity and funding statement remains an owner input (TRUST-09); nothing about funding or commissioning
  was invented.
- **Contact / report an issue** names one channel, `office@causewaygrp.com`, asks for the record or source reference,
  says a report is an input to review and does not change the record silently, publishes no response time, and warns
  against sending personal or sensitive data. Bounded and professional. Whether the mailbox is monitored is an owner
  confirmation before release (open item).
- **Corrections** records material changes only, keeps earlier citations interpretable and forbids silent material
  correction; the empty-state wording invents no history.
- **Accessibility** names WCAG 2.2 as the reference the resource is designed against and *will be* tested against (the
  sentence previously read as if testing had happened); no conformance is claimed.
- **Privacy** now says plainly what the one stored preference does (opens the site in the last language chosen) and that
  search runs inside the site.
- **Methodology** keeps "evidence state" where it explains the concept with examples; elsewhere the term is gone.

## 5. Deferred (open items, not defects of this state)

| Item | Class | Why deferred |
|---|---|---|
| YSC-008 "suspension of oil exports from January 2023" | EXTERNAL_EVIDENCE_DEPENDENCY | Must be checked against IMF Country Report No. 26/80 (the bound source), which could not be retrieved in this session; widely reported accounts date the halt to the October–November 2022 attacks. Text unchanged. |
| YSC-014 units of two IMF prudential ratios (148 → 69; about 5 → about 2.5) | EXTERNAL_EVIDENCE_DEPENDENCY | Presumably per cent; to be read from the IMF table before a unit is printed. |
| Date of Governor's Decision No. 10 of 2026 (SRC-CBY-ENF-10-2026) | EXTERNAL_EVIDENCE_DEPENDENCY | The decision page could not be read here; the title stays undated, which is true. |
| Contact mailbox monitored | OWNER_INPUT / RELEASE_ONLY | The page calls the channel monitored; the owner confirms before release. |

## 6. Scans on the accepted corpus

- **Leakage (public build):** no private locator or machine path (R85-G07), no internal finding or transaction code in
  visible text (R85-G06), no authoring token (R85-G05). The only e-mail address is `office@causewaygrp.com`. The public
  stylesheet no longer names the design tool in its comments.
- **House terms (Master, public prose fields):** «قاعدة القياس», «المقام», «التعرض», «ساعات الدليل», «نسخة المحتوى»,
  «بدء التشغيل الكامل», "content version", "evidence clock", "locator" — 0 occurrences each. The two remaining
  «مستدام» are sustainability in its own sense.
- **AI/editorial residue:** delve, crucial, robust, holistic, seamless, pivotal, furthermore, moreover, "it is important to
  note", «من الجدير بالذكر», «في الختام» — none; "landscape" (2, ordinary use) and "unlock" (2, investment sense)
  reviewed and kept.

## 7. Gates at the accepted state

Validator PASS 0/0; generator check and 21/21 tests; build 288 HTML from 143 Page Specs; public-literal audit 12,760
records, 0 unresolved; bilingual invariance 0 differing page pairs; browser suites and viewport acceptance as recorded in
the CI run of the commit. `run_stage.py` now rewrites `FINAL_REPOSITORY_MANIFEST.json` before validating, so a Master
transaction no longer trips the manifest gate (R85-G09).

## 8. Definition of Done (D7 §F5)

| Requirement | State |
|---|---|
| Whole Arabic corpus accepted | **Met** — every public Arabic field reviewed; all material and editorial defects applied or ruled; accepted by the Team Lead for this pre-design candidate (not a native-language certification) |
| Whole English corpus accepted | **Met** — same scope and standard |
| Zero unresolved semantic bilingual mismatch | **Met** — every parity finding applied; invariance 0; the three deferred items are single-source checks, identical in both languages |
| About / Methodology / Trust describe the real product | **Met** (§4) |
| Corrections and contact professional and bounded | **Met** (§4); mailbox monitoring is an owner confirmation |
| Public leakage scan passes | **Met** (§6) |
| No material AI or editorial residue | **Met** (§6) |
