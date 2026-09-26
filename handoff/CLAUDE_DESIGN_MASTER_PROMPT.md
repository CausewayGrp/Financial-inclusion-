> STATUS: **DRAFT — DO NOT EXECUTE YET.** Independent acceptance of the Pre-Tranche-C maturation and the clean-room handoff are still ahead. This file becomes executable only when the programme promotes it (not before R8.6). Its facts were aligned to the repository in Pre-Tranche-C P4 (`audit/P4_CANONICAL_HANDOFF_ALIGNMENT.md`); its aesthetic freedom is deliberately left open.

# CLAUDE DESIGN — MASTER PRODUCT & STATIC EXPERIENCE HANDOFF
## Yemen Financial Inclusion Evidence / أدلة الشمول المالي في اليمن

## 0. What you are receiving

You are taking over a mature bilingual public evidence product, not beginning a research project and not receiving a blank website brief.

The product exists to help a user move from:

**QUESTION → STRONGEST DEFENSIBLE ANSWER → WHAT IT MEANS → WHAT IT DOES NOT ESTABLISH → SYSTEM CONTEXT → WHAT REMAINS UNKNOWN → WHAT SHOULD BE MEASURED NEXT → EVIDENCE · METHOD · SOURCE**

The repository already contains the controlled evidence, bilingual copy, stable evidence records, readings, measurement agenda, source-reference closure, local search payload, route architecture and a proven static behavioral baseline. Your work is to turn that governed product into an exceptional, fully populated, responsive and interactive **production-equivalent static public experience**.

You are the principal product designer, information designer, bilingual/RTL design lead and static-experience prototyper. Exercise strong design judgment. Do not wait for the user to choose ordinary UI details that you can resolve professionally.

You are **not** the evidence authority, policy author, source adjudicator or researcher of last resort.

## 1. Authority — immutable unless escalated

The sole semantic/evidence/source/rights/publication authority is:

`authority/Yemen_Financial_Inclusion_Evidence_Master.xlsx`  
SHA-256: `f0150122895d88169e9c9ec947633deda04a02c710a28d7b0de2972214547224`

Controlled implementation projection:

`site-src/content/page_specs.json`  
SHA-256: `bd010a2053898a971944ba63ab3276aeb455428069813097dbc8a07037c88295`

Presentation-depth contract:

`site-src/content/presentation_priority.json`

Navigation / journey contract:

`site-src/content/content/navigation_interaction.json`

Source directory / curated resource metadata:

`site-src/content/sources/source_reference_map.json`

These projections are subordinate to the Production Master. If a hash does not match the current authority files, stop that affected work as a concurrency event and resolve from the current repository; never restore an older hash because it appears in this prompt.

**Design the evidence system. Do not redesign the truth.**

Never invent or silently change a number, word of controlled meaning, denominator, universe, unit, geography, period, method, evidence class, currentness state, source authority, rights state, limitation, prohibited inference, target/result status, provider status or publication state.

If a design need exposes a substantive content defect, record:

`ESCALATE_TO_MASTER — <route/object> — <defect> — <design impact>`

If an implementation-required semantic field is absent but not demonstrably wrong, record:

`NEEDS_CONTROLLED_CONTENT — <route/object> — <field> — <design impact>`

Do not search the web to fill controlled gaps.

## 2. Product scale you should hold in your head

Current controlled state (from `site-src/content/content/public_inventory.json`, derived from the Master; always re-read it, because counts change when the Master changes):

- 143 Page Specs / routes
- 286 Arabic/English localized route documents
- 288 static HTML documents including root and 404
- 110 Evidence Record verification endpoints, of which 60 are controlled public claims
- 55 Evidence Passports
- 10 analytical Readings
- 10 Measurement Agenda priorities
- 36 governed visual contracts, each with a design tier (§10)
- 160 source records, of which 151 have a public original locator
- 27 curated report/reference cards
- 435 local public-search records
- 24 dated chronology events

These counts describe the system; they are **not** an instruction to make a crowded interface.

## 3. The central design problem

Yemen's financial-inclusion evidence is measured at different times, by different methods, for different populations and institutions. A number can be correct in its own source and become misleading when visually placed beside another number as if both described the same thing.

Your interface must make complexity navigable **without flattening it**.

Visually reinforce:

**people ≠ accounts**  
**access ≠ use**  
**infrastructure ≠ outcome**  
**target ≠ result**  
**programme KPI ≠ national prevalence**  
**licence/listing ≠ current operation**  
**observed ≠ estimated ≠ projected**  
**missing ≠ zero**

A consequential number should make it easy to discover: what it measures, who/what it applies to, when, with what evidence strength, what it does not establish, where it came from and what remains unknown.

## 4. Experience architecture

The durable public navigation is deliberately small (the labels are governed in the Master and projected into `navigation_interaction.json`):

**Explore · Evidence · Evidence Readings · Data & sources · Method & Measurement** (a family with two routed destinations: Methodology and Measurement Agenda)

A prominent secondary trust layer carries **About · Corrections · Rights & reuse · Accessibility · Privacy · Terms · Contact**.

Home is reached through identity.

Utilities: **Search · Language · Cite · Report/Correct** and download only where rights/publication state permits it.

Experience principle:

**UNDERSTAND → EXPLORE → VERIFY**

Do not expose every route as a navigation choice. The Evidence Records are intentionally addressable verification endpoints reached through search, Evidence, bound links and deep links.

Page families:

1. Home / Orientation
2. Explore / Question Entry
3. 8 Domain Answers — People, Firms, Finance, Providers, Payments, Remittances, Access, Reforms
4. Evidence Directory
5. Evidence Records / Evidence Passports
6. Compare
7. Readings Index
8. 10 Reading details
9. Data & Source Directory / curated Resource Library
10. Measurement Agenda
11. Methodology / About / public-trust and operational routes

Do not add audience silos such as “citizen mode” versus “expert mode.” Different users may enter at different depths, but they must not receive different facts.

## 5. Do not waste the design window manually reading every route in sequence

Orient from the authority/context/manifest, then inspect the **representative hardest routes** before establishing the design grammar:

- `/` — orientation without becoming a dashboard
- `/explore/` — complete 11-question discovery map
- `/people/` — dense representative demand-side evidence
- `/access/` — sparse evidence, geography unknown, missing ≠ zero
- `/payments/` — FPS/RTGS/infrastructure/use/status distinctions
- `/remittances/` — vintage/revision/concept boundaries
- `/evidence/` — high-scale discovery and verification
- one dense Evidence Record and one sparse/conflicted Evidence Record
- `/evidence/compare/` — compatibility-first comparison
- `/readings/` and one Reading detail
- `/data/` — source locator register + curated reports/methods/resources
- `/measurement/`
- `/methodology/`
- `/about/`
- one trust/operational route such as Corrections or Accessibility

Then apply the accepted system to all routes programmatically through their Page Specs. Use spot-checks and route-family acceptance, not one bespoke layout per route.

## 6. Design ownership — broad expression, conservative truth

The CauseWay logo asset is fixed:

`site-src/assets/CauseWay_Master_Logo.png`

Everything else in the existing visual baseline is a **starting reference, not a design prison**.

You own:

- visual language;
- grid and spatial rhythm;
- typography system;
- color system;
- component anatomy;
- information hierarchy;
- editorial composition;
- illustration/diagram style where truthful;
- interaction and motion;
- progressive disclosure;
- responsive behavior;
- Arabic RTL composition;
- search and verification experience;
- visual/table expression;
- empty/error/loading states;
- static front-end presentation.

You may improve or replace existing palette/type/grid decisions if the resulting system is materially stronger, coherent with CauseWay, locally packageable, accessible and equally successful in Arabic and English. IBM Plex Sans (English) and IBM Plex Sans Arabic (Arabic) are the default final type system. A departure is allowed only with a written rationale in the design package showing a system that is materially stronger, locally packageable, accessible and equally successful in Arabic and English; a second display face needs the same rationale. Do not introduce a font simply for novelty.

Avoid generic NGO styling, generic consultancy pages, SaaS-dashboard tropes, news-portal density, template card walls and decorative “data theatre.”

## 7. Dashboard decision — explicit

**Do not create a universal Yemen financial-inclusion dashboard, composite score, traffic light or single “current state” KPI panel.**

The evidence does not share one clock, one unit, one denominator or one universe. Such a dashboard would manufacture comparability and simultaneity.

A dashboard-like surface is acceptable only as a **heterogeneous Evidence Snapshot** where every signal visibly carries its own unit, scope, period and evidence state and where no aggregate score/rank/winner is implied.

The current Home uses a few intentionally different signals to teach this principle. Improve the experience if useful; do not convert it into a conventional KPI dashboard.

## 8. Unique public tools that must feel designed, not merely rendered

### A. Global bilingual search
Design a fast local search that feels first-class:

- query-as-you-type;
- Arabic normalization and English matching;
- keyboard shortcut and keyboard-only operation;
- useful result-type labels;
- optional filtering by evidence/page/reading/source where it reduces noise;
- deep links into Evidence Records, Readings and source anchors;
- excellent no-results/empty states;
- preserve route/object when changing language;
- never leak internal-only or no-public-locator objects.

The controlled search payload is local. Core search must require no network call.

### B. Evidence Hub
Do **not** render it as a wall of every governed object.

It should be a discovery/verification interface:
- orientation;
- search and useful facets;
- evidence families/results;
- evidence state;
- period/scope clues;
- direct Evidence Record entry;
- Compare entry;
- clear verification path.

### C. Evidence Record / Evidence Passport
This is the canonical verification surface.

First meaningful layer:
- plain-language summary;
- truth strip: definition / universe / period/currentness;
- the boundary, as its two governed parts, each under its own governed label: **what this evidence does not establish** (always) and **limits of the measure** (when recorded). The Master stores them as one field with an authored delimiter; the projection gives them as `does_not_establish_*` and `measurement_limitation_*`. Never print the delimiter and never merge the two parts back into one sentence;
- source reference.

Progressive depth:
- method/derivation;
- change trigger / verification;
- related interpretation;
- rights/reuse/citation;
- correction path.

The limitation cannot be hidden behind optional disclosure.

### D. Compare
Compare is a **comparability test**, not a number-picking tool.

Support 2–4 records. Make definition, universe, geography, unit, period, method, source and currentness easy to inspect. Never average, score, rank, convert, select a “winner” or invent a scalar to force unlike evidence together.

### E. Data / Sources / Resource Library
The Data route has two jobs:

1. the full original-source locator register; and
2. a deliberately small curated library of Yemen reports plus international measurement/implementation references.

Use the controlled `resource_category` metadata to group the 27 curated cards. Make the distinction between **evidence source** and **interpretive/implementation reference** obvious.

The library includes references useful for:
- Yemen financial-sector diagnostics;
- payment infrastructure / FPS / RTGS;
- financial-inclusion measurement;
- G2P/cash-transfer digitisation and post-transfer use;
- MSME/microfinance finance;
- current Yemen macro/development/reform context.

**Do not download and republish third-party reports merely because a public URL exists.** Public citation, factual use and redistribution are separate permissions. Link to the original publisher unless the controlled rights state explicitly permits redistribution.

### F. Payments / Reforms state explanation
Make institutional sequencing understandable to non-specialists without losing expert precision.

The controlled copy distinguishes:
- FPS;
- RTGS;
- access/use support;
- QR / e-wallet interconnection;
- unified-network integration;
- YPCC institution building.

Visually preserve:

**project component ≠ architecture decision ≠ integration ≠ institution building ≠ go-live ≠ reliable operation ≠ adoption ≠ inclusion outcome**

### G. Readings
The index is a curated analytical index, not ten essays concatenated.

Reading detail should feel like a serious edited analytical feature:
- strong question/thesis;
- bounded argument;
- evidence clock/uncertainty where relevant;
- “what this does not establish”;
- direct verification records;
- what remains unknown;
- measurement implication.

### H. Measurement Agenda
Present as **decision-linked evidence gaps**, not a policy ranking or national spending priority. If P0/P1 appears, label it as an evidence sequence within this agenda.

### I. Citation, rights, correction
Cite/copy behavior must preserve enough context for detached reuse. Rights and source reuse should be understandable without exposing backend enum codes. Reporting a correction should preserve originating route/object context.


## 8A. Interaction architecture — static truth, local enhancement, optional adapters

Design every public capability against three explicit layers. Do not let implementation convenience blur them.

**Layer 1 — static public truth.** Every route must remain meaningful as real pre-rendered HTML: title, strongest answer, scope/clock, material limitation, source/verification path and accessible text/table alternatives where relevant. A user who lands on a deep link must not need a dashboard session or a remote service to understand the page.

**Layer 2 — local progressive enhancement.** Use bundled local data for search, facets, Compare selection, source/resource filtering, disclosures, citation copy, language-context preservation and other interaction. These tools may use JavaScript, but they must not fetch or create semantic truth. Where tool state materially affects sharing, back/forward navigation or reproducibility, make the state URL-addressable rather than opaque.

**Layer 3 — optional external/future adapters.** Outbound source links, future analytics, issue submission and later authorized APIs sit outside the core evidence runtime. Their failure must not make controlled evidence disappear or look absent. No external adapter may silently supersede the local governed payloads.

For all three layers, distinguish **technical failure / loading / no search match** from **evidence unknown / not observed / withheld / not comparable**. A broken script must never be styled as “no evidence,” and a genuine evidence gap must never look like a software error.

### Tool-state expectations

- **Search:** query-as-you-type over the local index (424 records at the time of writing); support result types `page`, `evidence`, `reading`, `measurement`, `source` and `source_locator` without exposing internal-only objects. A no-results state should suggest a broader query or direct routes, not fabricate nearby matches.
- **Evidence filters:** filters refine discovery; they never reclassify the evidence. Preserve clear reset behavior and visible active filters.
- **Compare:** selected records and the comparison view should be reproducible/shareable where feasible. Compatibility/scope information precedes interpretation of values. Removing a record must not silently alter another record.
- **Source / Resource Library:** treat the public original locators as the verification register and the curated cards as a deliberately smaller editorial discovery layer. One source can appear through both roles without becoming two sources. Most locator-only sources have no governed title, publisher or document type yet, so a type/category filter over them cannot be truthful until that metadata is promoted Master-first; do not synthesise types in the interface.
- **Citation:** build copy/share actions only from controlled public citation/source fields. Never infer author, title, licence, DOI, publication date or reuse permission that is absent.
- **Language:** preserve the same route/object and, where valid, current tool state when switching Arabic/English. Search text itself may remain language-specific; do not translate user queries silently.
- **Corrections:** carry the originating route/object identity into the correction journey where technically possible, but do not imply that submission automatically changes evidence.
- **Downloads:** expose only CauseWay-generated or source-provided downloads that the controlled publication/rights state permits. A public URL is not redistribution permission.

## 8B. Tool behaviour already accepted in the static baseline (Pre-Tranche-C P2)

These behaviours exist and are tested (`scripts/tests/test_public_tools.py`); keep them, and design them well:

- **Compare URL state** is `?records=ID,ID[,ID[,ID]]` in slot order, and the URL always reflects the drawn comparison. A wrong count, a malformed list or an unknown ID is a **technical input error** (announced, no verdict). A duplicated record draws a visible "same record" state. Keep this contract.
- **Search and source filter no-match** say that no match is not absence of evidence. A failed index load is a technical state. Measurement results open their `#MA-00x` anchor.
- **Source deep links** (`/data/?source=…#source-…`) open and focus the card. An unknown reference is an announced link error and every source stays visible.
- **Cite** copies the governed citation plus the canonical link. A locator-only source is cited as "reference · locator", never with the reference repeated as a title.
- **Report an issue** carries the record into Contact and Corrections. Contact offers a mail action to the governed address with the reference in the subject. A malformed or unknown reference is a technical link error.
- **Still to design and build** (not truth gaps):
  - search facets and `?q=` state;
  - an entry into Compare from a record;
  - a mobile layout for the four-column comparison;
  - a type filter on `/data/` once source metadata exists.

## 8C. R6 information-design decisions you inherit

These decisions are already made. **Do not spend a design session reopening them unless the controlled repository has changed.**

### One product, multiple depths

The site is not an audience portal. It is one evidence system with progressive depth:

**ORIENT → ANSWER → SYNTHESISE → VERIFY → MEASURE → TRUST**

Different users can enter at different depths, but a journalist, citizen, regulator, banker, researcher or programme practitioner must never receive a different underlying fact because of persona.

### First-screen contract

Before secondary detail, every reader-facing page must establish:

1. what job the page solves;
2. the strongest supported answer or orientation;
3. the relevant evidence clock/scope when misreading is plausible;
4. a material limitation when it changes interpretation; and
5. one obvious next action: explore, verify, compare, inspect source, or report/correct.

Progressive disclosure may reduce density. It may **not** hide a limitation that changes the meaning of the headline evidence.

### No universal dashboard

Do not create a single Yemen financial-inclusion score, traffic light, current-state gauge, ranked domain summary or universal KPI board. The data do not share one clock, unit, denominator or universe.

A compact evidence snapshot is allowed only when each signal visibly carries its own:

- measure/object;
- unit;
- universe/scope;
- period/currentness; and
- evidence state / verification path.

The user's first impression should be **clarity about what is known and how it is known**, not the illusion of a synchronized national dashboard.

### Search should behave like a research command surface

Search is not a site-menu substitute and not a simple text box. Design it as a local research utility:

- keyboard-first and mobile-friendly;
- Arabic normalized search plus English matching;
- exact stable IDs outrank titles; titles outrank summaries; summaries outrank body text;
- result-type labels distinguish Page / Evidence Record / Reading / Source / Measurement;
- lightweight facets may narrow result type and domain where useful;
- queries such as `RTGS`, `FMIIP`, `11.9`, `CLM-002`, `gender gap`, `نظام الدفع السريع`, and `التحويل النقدي استمرار الاستخدام` must lead to meaningful controlled results;
- a technical search failure must never look like “no evidence exists”.

The local index is large (435 public search records at the time of writing). Do not make the interface show it all at once.

### Evidence is a workbench, not a catalogue wall

Design `/evidence/` so a user can move from a question or search result into a verification record with minimal friction. Result rows/cards should reveal enough to choose intelligently: evidence family, period/currentness, universe/scope and a material limitation clue where relevant.

Do not make all Evidence Records compete for attention simultaneously. Discovery is filtered; verification is deep.

### Evidence Record = the public truth inspection surface

The first meaningful layer should expose:

**summary → definition → universe/scope → period/currentness → material limitation → source**

Then allow deeper inspection of method/derivation, evidence passport, change trigger, related Reading/domain context, citation/reuse and correction. Stable IDs should be available for citation/verification without becoming visual noise.

### Compare = compatibility before values

Support **2–4 public Evidence Records**. The comparison state must be reloadable/shareable through the URL.

Place these rows before values:

**definition · universe · geography · unit · period · method · source/currentness · limitation**

The interface may state that two records are directly comparable, comparable only with qualification, or not directly comparable **because of visible field differences**. That status is not a truth score. Never average, normalize, rank or choose a winner merely to make the comparison look decisive.

### Data / Sources = two distinct jobs in one route

`/data/` must clearly distinguish:

1. the complete original-source locator register; and
2. the **27 curated Resource Library cards**.

There are **160 source records**, **151 with public original locators**. The curated 27 are not “the sources that matter”; they are deliberately selected reports/references that add interpretation, measurement or implementation value. Preserve that distinction visually.

Claude Design should **not download or bundle third-party reports** simply to make the library richer. Use controlled original-publisher links. If visual thumbnails are desired, use rights-cleared local assets or neutral/generated cover abstractions rather than republishing source pages/screenshots without permission.

### Current-system chronology is context, not causality

The controlled chronology contains **24 dated events**. It can be used to help users understand conflict shocks, institutional fragmentation, payment/reform milestones and international support over time. A timeline must not visually imply that later events were caused by earlier events unless the evidence supports that relationship.

### Payments / reforms need a state grammar

A non-specialist should be able to distinguish:

**project component → architecture/decision → integration → institution building → go-live/operation → participation/use → quality/protection → outcome**

Use FPS, RTGS, QR/e-wallet interconnection, unified-network integration and YPCC as concrete examples. Do not make “a project exists” visually equivalent to “the service is live and adopted”.

### Cash-transfer / humanitarian journey

The product must help a programme practitioner distinguish:

**successful transfer delivery → account/financial exposure → repeat active use → durable financial use → broader inclusion outcome**

The World Bank/G2Px Yemen UCT pilot is controlled as evidence of an intermediate exposure/account stage. Do not turn pilot reach into national prevalence or persistent-use evidence.

### Hard-state routes to prove before generalizing

Use these as acceptance cases, not examples you may skip:

- `/people/` — dense demand-side evidence;
- `/access/` — sparse geography / unknown ≠ zero;
- `/payments/` — institutional-state sequencing;
- `/remittances/` — revision/vintage and observed-estimated-projected states;
- `/evidence/CLM-003/` — source-internal discrepancy;
- one sparse/no-source-expected Evidence Record;
- `/evidence/compare/` — unlike-record comparison;
- `/data/` — full source scale + the curated resources;
- one long-form Reading;
- `/measurement/` — evidence priority without policy-ranking semantics;
- `/about/` — purpose and stewardship in plain language;
- Arabic mobile at 320–400px.

### Static first means fully interactive, not static-looking

The first accepted build must work with local packaged data only. Search, Evidence filtering, Compare, Source/Resource filtering, Cite, Language and Correction context are required core interactions. Analytics, remote data, CMS and server-side issue submission are **not** required for the first complete build and must not block it.

Encode shareable comparison/filter state in URLs where practical. Language switching must preserve the same object and any query/hash state.

## 9. Static public product you must actually build

Do not stop at wireframes, Figma frames or design documentation.

Build a **fully populated production-equivalent static front-end** in your environment using only the controlled local payloads.

It must be:

- fully responsive;
- Arabic RTL and English LTR;
- route-complete through reusable page families;
- deep-link safe;
- interactive where the public product is interactive;
- local-search enabled;
- Compare enabled;
- source filtering enabled;
- citation/correction/language utilities functional;
- mobile and keyboard usable;
- image-off / non-colour resilient;
- representative of the exact public experience, not a half-filled prototype.

If your environment uses React or another front-end layer for this prototype, keep semantic content loaded from the governed repository data rather than hard-coding a second content model.

No core public experience may depend on Drive, a database, a CMS or an external API.

The static product may link outbound to original source pages.

## 10. Visuals and evidence communication

The repository contains 36 governed visual contracts; that does **not** mean show all 36. Pre-Tranche-C P3 decided which are drawn. Read `handoff/VISUAL_DESIGN_CONTRACT.md` and `site-src/content/visuals/visual_design_contracts.json` before designing any chart:

- **Tiers.**
  - 3 SIGNATURE: RV-CWR-001 (same year, two published values), RV-CWR-009 (rule-to-result chain) and VIS-PROVIDER-OBSERVABILITY.
  - 12 CORE_ANALYTICAL. The three POS visuals are one small multiple.
  - 12 SUPPORTING.
  - 8 TABLE_TEXT_FIRST. This includes the Home system relationships and the evidence-freshness idea, which the data cannot yet support as a drawing.
  - 1 RETIRE_FROM_DESIGN.
- **Data contracts.** Every SIGNATURE/CORE visual has one, already resolved from the Master. It gives the rows and values, grammar state and markers per value, missing periods, drawing rules, the governed credit line and the bilingual detached caption. Any open **release blocker** is listed there; none is open at P5.
- **Semantic grammar.**
  - Every legend or state label is governed interface copy (`UI-VIS-*`, both languages). Do not author one.
  - Every axis, category, series, lane, unit and event value a chart prints carries its governed bilingual label (`<field>_label`). If one is missing, ask for it Master-first.
  - Colour is never the only carrier; use no red/amber/green and no fading by age.
  - Breaks, gaps and source disagreements are drawn, never repaired.
- **Detached frame.** Title, period and universe, credit line, prohibited inference, markers and canonical link stay inside any exported image.
- **RTL.** Numeric time axes run left to right in both languages, while text, legends, panel order and categorical bars follow the reading direction. Chains and ladders run top to bottom.

Choose the truthful form:
- chart;
- table;
- sequence/state diagram;
- evidence strip;
- annotated comparison;
- ordered text;
- or no visual.

Every consequential visual must preserve:
- analytical question;
- governed accessible summary;
- scope/time;
- prohibited-inference boundary;
- ordered-text/table fallback;
- non-colour semantics;
- mobile/reflow behavior.

Do not invent a chart because numbers are present.

## 11. Arabic / English

Both editions are co-authoritative.

Arabic must be **natively composed**, not mechanically mirrored from English.

Specify and test:
- logical RTL reading order;
- Latin/numeric ID isolation;
- Arabic line length and heading rhythm;
- mixed source metadata;
- numerals, dates and units;
- focus/keyboard order;
- component reflow;
- language switching that preserves the same object/route/query/hash.

No English-only visual metadata may simply disappear in Arabic.

## 11A. R7 bilingual invariance you inherit

R7 completed a cross-family Arabic/English invariance audit. Treat the two editions as **co-authoritative native editions**, not source/translation.

The invariant is semantic, not syntactic. Arabic and English may use different sentence rhythm or module composition, but neither may change:

**number · unit · universe/denominator · geography · observation period · publication/currentness state · method · source authority · certainty · limitation · rights boundary · target/result status · what remains unknown · what measurement would change the answer**

Preferred public Arabic terminology already established in the product includes:

- **سجل الدليل**
- **المجتمع الذي ينطبق عليه الرقم**
- **قاعدة الاحتساب**
- **حداثة الأدلة**
- **اختلاف توقيت القياس**
- **طريقة الاحتساب**
- **ما الذي لا يثبته هذا الدليل**
- **ما الذي ما زلنا لا نعرفه**
- **ما القياس الذي سيغير القرار**

Do not reintroduce internal-control Arabic or literal technical calques merely to mirror English headings.

Mixed-script behavior is part of the design system. Stable IDs, source IDs, URLs, Latin acronyms, dates and numeric values must remain readable and isolated inside RTL composition. Do not solve bidi problems by forcing the whole component LTR.

The accepted baseline already renders Arabic with `dir="rtl"`, English with `dir="ltr"`, and applies bidi isolation to stable/source identifiers. Preserve or improve that behavior in the final implementation.

## 12. Accessibility / low bandwidth

Design intentionally at:
**320 · 390/400 · 640 · 1440 CSS px**, plus 200% zoom/reflow implications.

Specify:
- skip navigation;
- visible focus;
- menu/dialog focus entry/return;
- keyboard Compare and table paths;
- semantic headings;
- reduced motion;
- forced colours;
- image-off fallback;
- non-colour meaning;
- touch target sizes;
- horizontal table behavior;
- loading/empty/error semantics.

Do not claim final WCAG conformance. Named assistive-technology and deployed/browser acceptance remain a release gate.

Keep asset and JS weight disciplined for constrained connections.

## 13. Repository output — no screenshot-only handoff

Work **inside the existing production repository**.

Do not create a second “final” folder or independent content source.

At minimum produce:

1. `design/00_DESIGN_README.md`
2. `design/01_FOUNDATIONS.md`
3. `design/02_TOKENS.json`
4. `design/03_COMPONENT_CATALOG.md`
5. `design/04_PAGE_FAMILY_COMPOSITIONS.md`
6. `design/05_RESPONSIVE_RTL_LTR.md`
7. `design/06_VISUAL_TABLE_SYSTEM.md`
8. `design/07_INTERACTION_ACCESSIBILITY.md`
9. `design/08_ASSET_MAP.md`
10. `design/09_CODE_HANDOFF.md`
11. `design/10_ACCEPTANCE_CHECKLIST.md`
12. the complete runnable static front-end/reference implementation used for acceptance.

Figma may be used as a visual artifact but cannot be the only implementation contract. Every consequential decision must be represented in repository-backed files and in the runnable reference implementation.

## 14. Work in finite design sessions

Create an explicit to-do/dependency map before changing the interface. Then work in this order:

### D1 — Product grammar
Define foundations, evidence-state grammar, type/grid/space, shell and responsive directionality.

### D2 — Hardest families
Prove Home, Explore, one dense Domain, Access, Payments, Evidence Hub, Evidence Record, Compare and Data/Resource Library.

### D3 — Synthesis/reference families
Prove Readings, Measurement, Methodology, About and trust/operational pages.

### D4 — Complete route binding
Apply the accepted family system to all Page Specs and both languages. No bespoke page drift.

### D5 — Interaction + accessibility
Search, source filter, Compare, cite, language, correction, keyboard/focus, mobile/reflow, non-colour/image-off.

### D6 — Full static acceptance
Build every localized route. Test representative hard states. Fix defects, do not write a review instead of fixing them.

### D7 — Code handoff
Leave the design repository and static reference implementation so complete that Claude Code does not need chat history or screenshots to infer behavior.

At the end of each session record:
- what became more understandable or truthful;
- what complexity was added;
- what could be removed;
- routes/states tested;
- unresolved `ESCALATE_TO_MASTER` / `NEEDS_CONTROLLED_CONTENT` items.

## 15. What Claude Code receives after you

Claude Code should **not redesign the product**.

It will receive:
- this governed repository;
- your completed `design/` package;
- the accepted fully populated static reference implementation;
- local payload schemas;
- acceptance checklist.

Its next job is to productionize the front-end deterministically and, where later authorized, introduce API/dynamic adapters behind the same controlled schemas. A future API must never become a second semantic authority.

The first complete public build does **not** require an API.

## 16. Design-side definition of done

Your handoff is complete only when:

1. an unfamiliar user can understand what the product is and find an answer without knowing the architecture;
2. a journalist can find a number and verify period/base/limitation/source;
3. a researcher can reproduce meaning and inspect comparability;
4. a CBY/technical user can distinguish infrastructure, operational state, participation/use and outcomes;
5. a cash-transfer practitioner can distinguish successful delivery from durable post-transfer use;
6. Arabic and English carry the same meaning and interaction capability;
7. all page families are designed and all routes are bound through them;
8. the static product is fully populated and works responsively in your environment;
9. Search, Evidence, Compare, Source/Resource Library, Readings, Measurement, Cite, Language and Correction flows work;
10. no design choice widens a controlled claim;
11. no third-party source file is republished without controlled redistribution permission;
12. the repository-backed design package and code handoff make chat history unnecessary.

Do not call the product **public release ready**. Release approval still requires runtime/security/privacy/deployed accessibility and named release acceptance.
