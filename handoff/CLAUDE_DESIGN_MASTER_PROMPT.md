> STATUS: **R8.6 FREEZE CANDIDATE — PENDING FINAL CLEAN-ROOM ACCEPTANCE.** Executable once `handoff/README_FIRST.md` reads **DESIGN HANDOFF READY**.

# Claude Design — master brief
## Yemen Financial Inclusion Evidence · أدلة الشمول المالي في اليمن

This is the one executable brief for the design of this product. It is written from the repository as it stands; where
it names a file, open that file — it is the detail this brief summarises. Nothing here requires an earlier conversation.
If this brief and a governed projection ever disagree, the projection is right and the difference is an escalation (§2).

---

## 0. How to work at full capability

You are the principal product designer, information designer, bilingual/RTL design lead and reference-implementation
engineer for a mature public evidence product. Use everything you can do:

- **Plan before pixels.** Build a dependency map of families, components, states and data bindings from
  `handoff/ROUTE_CONTENT_AND_STATE_INVENTORY.json` before you design a single screen. Keep it current as `design/00_DESIGN_README.md`.
- **Design with the real thing.** Every screen uses the real governed English and Arabic content and data from
  `site-src/content/`. No lorem ipsum, no placeholder figures, no invented labels — ever.
- **Build, don't describe.** Your main deliverable runs: a fully populated reference implementation of every route in
  both languages (§19). Mock-ups and documents support it; they do not replace it.
- **Prove on the hardest cases first** (§9.2), then generalise through page-family rules, never route-by-route drift.
- **Look at your own work.** Render every family at 320, 390, 640 and 1440 CSS px in Arabic and English, look at the
  screenshots, critique them against `handoff/DESIGN_ACCEPTANCE_CRITERIA.md`, fix, and repeat. Test keyboard paths, zoom,
  reduced motion, forced colours and image-off yourself.
- **Challenge weak inheritance.** The current layout and styles in `site-src/styles.css` are a behavioural baseline, not
  a design. Replace anything that is merely inherited. Keep only what earns its place.
- **Decide.** Resolve ordinary design questions professionally and record the reasoning; do not stop to ask about
  details a senior designer would settle. Escalate only truth and missing governed content (§2).

---

## 1. The product and its north star

A bilingual public evidence resource, built and maintained by CauseWay, that helps people **understand, compare and
verify** the evidence on financial inclusion in Yemen. It supports human decisions by clarifying evidence; it makes no
regulatory, political, business or funding decision for anyone.

**QUESTION → STRONGEST DEFENSIBLE ANSWER → WHAT IT MEANS → WHAT IT DOES NOT ESTABLISH → SYSTEM CONTEXT → WHAT REMAINS
UNKNOWN → WHAT SHOULD BE MEASURED NEXT → EVIDENCE → METHOD → SOURCE**

Experience principle: **UNDERSTAND → EXPLORE → VERIFY**. A consequential claim always travels as
**ANSWER → SCOPE → BOUNDARY → VERIFY**.

The central design problem: Yemen's evidence is measured at different times, by different methods, for different
populations and institutions. A number that is correct in its source becomes misleading when it sits beside another as
if both described the same thing. The interface must make that complexity navigable **without flattening it**.
Financial inclusion here is a system — people, households, firms, providers, accounts, cash, payments, remittances,
regulation, programmes, constraints — and the numbers exist to reveal that system, not to decorate a dashboard.

---

## 2. Authority — immutable unless escalated

| Layer | Path | Role |
|---|---|---|
| Production Master | `authority/Yemen_Financial_Inclusion_Evidence_Master.xlsx` (SHA-256 `ed3c5796cb0cca0109a0eb56f66d344ab0a5faa550e5235e05d65a6147f33fe1`) | The only semantic, evidence, source, rights and publication authority |
| Page Specs | `site-src/content/page_specs.json` (SHA-256 `2407cb4f9ca67aec60304630690488d04a3b05f9ea1eec03f805de24915cb3ad`) | Every route: titles, descriptions, sections, bound objects, prohibited inferences, render rules |
| Presentation depth | `site-src/content/presentation_priority.json` | What each page shows first and what may be disclosed later |
| Navigation and interaction | `site-src/content/content/navigation_interaction.json` | Navigation, trust layer, footer, breadcrumbs, next actions, page families, journeys, tools, hard states |
| Interface copy | `site-src/content/content/interface_copy.json` | Every interface label in both languages (`UI-*` IDs) — the only source of UI wording |
| Everything else | `site-src/content/**` | Evidence records, claims, passports, Readings, Measurement, questions, sources, visuals, chronology, search |

All of `site-src/content/**` is generated from the Master and is never edited by hand. If a hash in this brief differs
from the repository, the repository is right.

**Design the evidence system. Do not redesign the truth.** Never invent or silently change a number, a word of
controlled meaning, a denominator, population, unit, geography, period, method, evidence state, currentness state,
source authority, rights state, limitation, prohibited inference, target/result status, provider status or
publication state. When a design need exposes a problem, write it in `design/ESCALATIONS.md` and keep going:

- `ESCALATE_TO_MASTER — <route/object> — <defect> — <design impact>` — the controlled truth looks wrong;
- `NEEDS_CONTROLLED_CONTENT — <route/object> — <field> — <design impact>` — a field you need does not exist (for
  example a short label, an Arabic label for a chart value, an alt text).

Do not search the web to fill a controlled gap. Do not author interface labels: a new label is a
`NEEDS_CONTROLLED_CONTENT` request for a new `UI-*` entry in both languages.

---

## 3. Read-in (first working hour)

1. `handoff/README_FIRST.md` — rules, protocol, what is frozen and free.
2. `handoff/ROUTE_CONTENT_AND_STATE_INVENTORY.json` — every route with family, titles, sections, bound evidence,
   visuals, Readings, Measurement, sources, structured data and hard states; every evidence lineage state, visual tier,
   visual grammar state and technical state; the thirteen user journeys.
3. `site-src/content/content/navigation_interaction.json` — `global_navigation`, `trust_navigation`, `utilities`,
   `footer_groups`, `breadcrumbs`, `route_next_actions`, `page_families`, `interaction_tools`, `hard_state_acceptance`,
   `journeys`, `static_progressive_enhancement_boundary`.
4. `site-src/content/page_specs.json` — open the Page Specs of the hard-state routes (§9.2).
5. `handoff/VISUAL_DESIGN_CONTRACT.md` and `site-src/content/visuals/visual_design_contracts.json` — before any chart.
6. `handoff/DESIGN_ACCEPTANCE_CRITERIA.md`, `handoff/DESIGN_TO_CODE_CONTRACT.md`,
   `handoff/ENGINEERING_HANDOFF_EXPECTATIONS.md` — how you are accepted and what Code needs.
7. The running baseline: `python3 -m http.server 4173 --directory dist`, then `/ar/` and `/en/`. Try every tool.
8. `audit/ARABIC_TERMINOLOGY_AND_STYLE_LEDGER.md` and §3 of `audit/F5_PUBLIC_CORPUS_ACCEPTANCE.md` — the Arabic and
   English house terms.
9. `FINAL_OPEN_ITEMS_REGISTER.md` — what is unknown; design around it, never fill it.

Counts change when the Master changes: always take them from `site-src/content/content/public_inventory.json`. They
describe the system; they are not an instruction to show everything at once.

---

## 4. Product model

### 4.1 Page families (11) and routes

| Family | Routes | Job |
|---|---|---|
| Orientation | `/` | Identity, the product's promise, a few common questions, one Featured Reading, a truthful evidence snapshot |
| Question Entry | `/explore/` | All governed entry questions; one "Go deeper / تعمّق في التحليل" Reading |
| Domain Answer | `/people/ /firms/ /finance/ /providers/ /payments/ /remittances/ /access/ /reforms/` | The strongest bounded answer for a domain, its scope, boundary, unknowns, next measurement and verification path; at most two Readings |
| Evidence Directory | `/evidence/` | Discovery into verification records; entry to Compare |
| Evidence Record | `/evidence/<ID>/` (one per Evidence Record) | The canonical verification endpoint: summary, definition, population, period, currentness, boundary, method, source, Readings that use it |
| Comparison | `/evidence/compare/` | A comparability test for 2–4 records |
| Reading Index | `/readings/` | The ten Evidence Readings as a curated analytical index |
| Reading | `/readings/<slug>/` | A serious public-evidence essay |
| Data & Source | `/data/` | The full original-source register, the curated Resource Library, the system chronology |
| Measurement | `/measurement/` | Ten decision-linked evidence priorities |
| Reference / Trust | `/methodology/ /about/ /corrections/ /rights/ /accessibility/ /privacy/ /terms/ /contact/` | Method, stewardship, correction, reuse, accessibility, privacy, terms, contact |

Every route exists in Arabic (`/ar/…`) and English (`/en/…`); `/` is the neutral entry that opens the reader's chosen
edition (otherwise Arabic); there is a bilingual 404. The route set is frozen; the inventory lists every route.

### 4.2 Navigation (governed labels — use them verbatim)

Primary: **Explore / استكشف · Evidence / الأدلة · Evidence Readings / قراءات الأدلة · Data & sources / البيانات
والمصادر · Method & Measurement / المنهج والقياس** (a family with two destinations: Methodology / المنهجية and Measurement
Agenda / أولويات القياس). Home is reached through the identity.

Trust layer (prominent, secondary): **About · Corrections · Rights & reuse · Accessibility · Privacy · Terms · Contact**.
Utilities: **Search · Language · Cite this page · Report an issue**. Footer groups and breadcrumbs are in
`navigation_interaction.json`. The grouping and prominence you give them are yours; the labels and destinations are not.

### 4.3 First-screen contract (every reader-facing page)

Before secondary detail, a page establishes: (1) the job it solves; (2) the strongest supported answer or orientation;
(3) the evidence clock and scope wherever a number could be misread; (4) a material limitation when it changes the
interpretation; (5) one obvious next action — explore, verify, compare, inspect source, or report/correct. Progressive
disclosure may reduce density; it may **never** hide a limitation that changes the meaning of the headline evidence.

### 4.4 No universal dashboard

No composite score, traffic light, "current state" gauge, ranked domain summary or KPI board: the evidence does not share
one clock, unit, denominator or population. A compact **evidence snapshot** is allowed only when each signal visibly
carries its own measure, unit, population, period and evidence state, and nothing implies an aggregate, rank or winner.

---

## 5. The semantic firewall and public-state distinctions

These distinctions must be visible in every surface, in both languages, and survive when a component is cropped,
screenshotted or read without colour:

people ≠ households ≠ firms ≠ accounts ≠ active accounts ≠ customers ≠ transactions ≠ terminals ≠ agents ≠ providers ≠
beneficiaries · access ≠ ownership ≠ registration ≠ adoption ≠ active use ≠ frequency ≠ persistence ≠ quality ≠ outcome
· infrastructure ≠ use · target ≠ result · programme KPI ≠ national prevalence · regulation ≠ implementation ≠ operation
≠ experienced outcome · licence/listing ≠ operation · observation ≠ fieldwork ≠ publication ≠ retrieval · historical ≠
current · observed ≠ estimated ≠ projected · missing ≠ zero · chronology ≠ causality · source-owner analysis ≠
independently established impact · financial-education activity ≠ literacy ≠ capability ≠ behaviour ≠ outcome.

States you must give a distinct, non-colour-only visual grammar (the inventory lists them all, with their governed
labels):

- **Evidence lineage** of a record — bound to its sources, partly bound, composite of other records, framing rule with no
  fact; each has its governed verification copy (`UI-VERIFY-*`, `UI-EVID-*`).
- **Visual grammar states** — measured, reported, administrative, derived, historical, programme, projected/estimated,
  withheld, missing, disagreement, same-year revision, breaks of vintage or universe (`visual_design_contracts.json` →
  `grammar`, labels `UI-VIS-*`).
- **Technical states** — a failed index, a malformed link, an unknown reference, a duplicate in Compare, no search
  match, 404, no JavaScript. A technical state must never look like "no evidence", and an evidence gap must never look
  like a software error.

---

## 6. Frozen for Design · free for Design

**Frozen:** factual content; evidence relationships; public-state distinctions; route purpose; required behaviours and
actions; Arabic/English equality; accessibility outcomes (§14); visual semantics and prohibited inferences; the
canonical CauseWay logo; the IBM Plex family requirement; citation and source behaviour; rights constraints; the rule
that no internal or repository language reaches the public.

**Free:** composition; grid; hierarchy; rhythm; spacing; palette within contrast and identity constraints; component
form; chart form where several forms satisfy the visual contract; interaction choreography; micro-motion; responsive
expression; editorial pacing.

---

## 7. Design character

**Ask of the design:** white-dominant · restrained · serious · modern · distinctive · unusually clear · editorial rather
than SaaS or dashboard · high-end without luxury decoration · excellent Arabic and RTL · dense where expert verification
needs density · spacious where comprehension needs space · **evidence as protagonist** · **CauseWay as steward**.

**Avoid:** generic AI-site aesthetics · card-wall dependence · decorative dashboards · gratuitous gradients · donor-report
visuals · badge clutter · over-animation · stock photography used as decoration · generic NGO or consultancy styling ·
news-portal density · "data theatre".

---

## 8. Identity

- **Logo.** `site-src/assets/CauseWay_Master_Logo.png` (6250 × 6250 px RGBA PNG, SHA-256
  `5830163d…`, full hash in `FINAL_REPOSITORY_MANIFEST.json`) is the only logo authority. Never redraw,
  recolour, distort, crop, trace, vectorise or AI-regenerate it. Specify where and at what rendered sizes it appears
  (header, footer, 404, social images) and its clear space. It is 96–99 % of every page's transfer today; web-size
  derivatives are an owner-approved engineering step after Design (open item EAD-03) — specify the sizes Code must
  export, do not produce them yourself. The reference build whitens the footer logo with a CSS filter
  (`brightness(0) invert(1)` in `site-src/styles.css`): that is a recolouring and must not be carried forward. On a dark
  surface, place the logo on a light field with its clear space, or record a request for an owner-supplied reversed
  version (`FINAL_OPEN_ITEMS_REGISTER.md`, OWN-06) — never derive one by filter, blend or tracing.
- **Typography.** IBM Plex Sans (English) and IBM Plex Sans Arabic (Arabic) are the default final system, self-hosted
  (SIL Open Font License) — no font CDN. Use weights and optical sizing deliberately; Arabic needs its own line height,
  size steps and heading rhythm, not English values mirrored. A departure, or a second display face, needs a written
  rationale showing a materially stronger system that is locally packageable, accessible and equally successful in both
  languages. No font for novelty.
- **Tokens.** `handoff/DESIGN_STARTING_TOKENS.json` is a hypothesis. Replace it with your own documented system
  (`design/02_TOKENS.json`), meeting contrast (§14) and the CauseWay identity.

---

## 9. Required coverage

### 9.1 Surfaces

Design and build every one of these, in both languages, desktop, tablet and mobile:

- **Global shell:** header, primary navigation with the Method & Measurement family, trust layer, footer, language
  switch, search entry, cite and report-issue utilities, skip link, breadcrumbs.
- **Home**; **Explore**; **all eight domain routes** (prove the hard ones first); **Evidence index** and **Evidence
  Record** (dense, sparse, conflicted, composite, framing, withheld); **Compare**; **Readings index**; **Reading detail**
  (at least three stress cases: the longest, the one with the most visual data, and one with a table-first visual);
  **Data/sources/Resource Library** (with the chronology); **Measurement Agenda**; **Methodology**; **About** and every
  **trust** route; **corrections/report-issue** journey; **404**.
- **Hard evidence states** (§5), **all visual families** (§12), the **social/OG system** (§16), **mobile**, **RTL** and
  **accessibility states** (focus, error, status, reduced motion, forced colours, zoom).

### 9.2 Hard-state acceptance — prove these before generalising

From `navigation_interaction.json` → `hard_state_acceptance` (routes in both languages):

| State | Route | Must prove |
|---|---|---|
| dense_domain | `/people/` | High density stays scannable; wave, fieldwork, population and limitation stay attached to the headline figure |
| sparse_unknown | `/access/` | Unknown geography is visibly unknown — not zero, not an empty map |
| institutional_sequence | `/payments/` | FPS, RTGS, interoperability, institution-building, operation, use and outcome are distinct states |
| vintage_conflict | `/remittances/` | Same-year revisions and observed/estimated/projected states are legible without choosing a winner |
| verification_dense | `/evidence/CLM-003/` | Raw totals and the source's own percentage coexist; the discrepancy is visible; the limitation prominent |
| verification_sparse | `/evidence/CLM-015/` | A record with no source expected is not styled as missing evidence or an error |
| compare_unlike | `/evidence/compare/` | No visual pressure to compare unlike units or populations; the boundary is the first conclusion |
| source_scale | `/data/` | Every source stays discoverable without a wall of links; curated cards are visibly curated, not a separate authority |
| reading_longform | `/readings/same-year-different-number/` | Long analysis stays bounded, readable and traceable to its records |
| measurement_nonranking | `/measurement/` | P0/P1 reads as sequencing within this agenda, never as national policy or spending priority |
| trust_plain_language | `/about/` | Purpose, CauseWay's role, limits, source authority and correction are clear without backend terms |
| mobile_rtl | `/ar/payments/` | At 320–400 px, Arabic order, numeral and Latin isolation, tables, controls and the verification path stay coherent |

Also prove: an Evidence Record whose value is **withheld** (`/evidence/CLM-044/` — the value is not published and must
never appear), a **composite** record (`/evidence/CLM-014/`), and the **framing** record (`/evidence/CLM-004/`).

### 9.3 Journeys

The thirteen journeys in the inventory are acceptance paths — first-time reader; journalist verifying a number;
journalist challenging a Reading; researcher testing comparability; regulator; payments analyst; provider; development
partner; humanitarian practitioner; anyone challenging a record; reuser; accessibility user; a payment-rail explainer.
Each must succeed on mobile and desktop, in both languages, by keyboard.

---

## 10. Tools — first-class, local, tested

All tools run on local packaged data; none may need a network call. Their accepted behaviour is tested in
`scripts/tests/test_public_tools.py`; keep it and design it well.

- **Search** (`static-data/search_index.json`, aliases in `search_aliases.json`): query as you type; Arabic normalisation
  and English matching; exact stable IDs outrank titles, titles outrank summaries, summaries outrank body text; result
  types page · question · evidence · Reading · Measurement · source · source locator; `Ctrl/Cmd+K` and `/` open it; focus
  enters the query and returns to the opener; results keyboard-reachable and announced; a no-match says that absence
  from search is not absence of evidence; a failed load is a technical state. Measurement results open their `#MA-00x`
  anchor. The index loads only when Search opens. Design facets and a `?q=` state (still to build).
- **Evidence workbench** (`/evidence/`): search and facets before browse-all; rows reveal family, period/currentness,
  population and a limitation clue; never a wall of every record.
- **Compare** (`/evidence/compare/?records=ID,ID[,ID[,ID]]`, slot order): 2–4 public records; compatibility rows
  (definition · population · geography · unit · period · method · source/currentness · limitation) **before** values;
  a verdict of directly comparable / comparable only with qualification / not directly comparable, never a truth score;
  never average, normalise, rank, convert or pick a winner; wrong count, malformed list and unknown ID are announced
  technical input errors; a duplicated record draws a visible "same record" state; language switch keeps the
  comparison. Still to build: entry into Compare from a record, and a mobile form of the four-column comparison.
- **Source directory and Resource Library** (`/data/`): the full original-source register and the small curated library
  are two jobs; `?source=` deep links open and focus the card; an unknown reference is an announced link error while every
  source stays visible; the nine sources without a public locator are never named or linked. Group the curated cards by
  their governed `resource_category`. The reader-facing document type is `document_label` / `document_label_ar`
  (`site-src/content/sources/source_reference_map.json`, 142 of 160 sources, both languages): a type filter, if you
  design one, uses only that field and shows the 18 locator-only sources as "type not recorded" — never a synthesised
  type.
- **Cite**: copies the governed citation plus the canonical link; a locator-only source is cited as "reference ·
  locator"; the edition line is governed ("Edition of 26 September 2026").
- **Report an issue**: carries the originating record into Contact and Corrections; Contact offers a mail action to the
  governed address with the reference in the subject; bad references are technical errors; a report never changes the
  record.
- **Language**: preserves route, object, query and hash; never translates a user's query.
- **Download**: design the pattern for CauseWay-generated downloads (a record's governed fields; a chart's governed data
  table; a citation file). They ship only when the owner sets the reuse licence for CauseWay content (open item OWN-04) — design
  the disabled and enabled states. Third-party documents are never offered for download: a public URL is not
  redistribution permission.

Page data travels in JSON blocks (`<script type="application/json" id="yfie-ui">`, `yfie-compare`,
`yfie-compare-dimensions`, `yfie-record-ids`), never in inline executable scripts; keep that pattern (§18).

---

## 11. The Evidence Readings — the flagship editorial family

A Reading is a **serious public-evidence essay**, not a blog post, a report page, a database record or a card.

- Title + a strong standfirst + the evidence tension, immediately.
- Light, truthful metadata: evidence period and last reviewed (both governed); main sources come from the bound records.
  Reading time only if computed from the actual text in each language.
- The essay: sections in order; the opening may run without a heading; the last section is always "What would change
  this reading? / ما الذي قد يغيّر هذه القراءة؟"; pull lines (`> `) and lists are governed markup.
- At most **one signature analytical visual**, placed after the opening, and only when its contract earns it.
- The prohibited inference ("Do not infer / ما لا يُستنتج") is visible, not buried.
- Then "Trace the evidence / تتبّع الأدلة" (the bound records and sources) and one or two related Readings.
- Home shows **one** Featured Reading, Explore **one** "Go deeper", a domain page **at most two**; an Evidence Record lists
  the Readings that use it; a Measurement priority says where its gap is examined. No carousels, no ten-card walls.

Readings data: `site-src/content/content/readings.json`, `reading_sections.json`; each Reading's Page Spec carries its
bindings.

---

## 12. Visuals

Read `handoff/VISUAL_DESIGN_CONTRACT.md` and `site-src/content/visuals/visual_design_contracts.json` before any chart.
Tier counts are in `tier_counts`; the tier of every visual is in the inventory.

- **SIGNATURE** — design first; full data contracts. **CORE_ANALYTICAL** — standard truthful forms; full data contracts
  (the three POS visuals are one small multiple). **SUPPORTING** — optional; the governed text alternative is complete
  content until drawn. **TABLE_TEXT_FIRST** — never drawn as a chart; render the governed ordered text or table.
  **RETIRE_FROM_DESIGN** — never drawn.
- No chart without a contract row. No number, label, legend or sentence authored in Design: legends and states come from
  `UI-VIS-*`; axis, category, series, lane, unit and event text from each value's `<field>_label`.
- Colour is never the only carrier; no red/amber/green; nothing fades with age. Breaks, gaps and disagreements are drawn,
  never repaired; missing is a labelled gap, never zero; lanes are separate series and never share a value axis.
- **Detached frame**: title, period and population, credit line, prohibited inference, markers and canonical link travel
  inside any exported or shared image. A crop without them is not a supported export.
- **RTL**: numeric time axes run left to right in both languages; text, legends, panel order and categorical bars follow
  the reading direction; chains and ladders run top to bottom; Western digits; IDs, currency codes and signed percentages
  are isolated left-to-right runs; no right-pointing arrow between numbers in Arabic.
- **Mobile**: each contract states its narrow form; plot areas never scroll horizontally.
- **Text alternative**: the governed analytical alt text plus a table or ordered-text fallback (caption, scoped headers,
  unit, population, period) ships with every chart and stays true if the chart fails.
- Choose the truthful form — chart, table, state diagram, evidence strip, annotated comparison, ordered text, or no
  visual. Do not invent a chart because numbers are present. The chronology is context, never a causal chain.

---

## 13. Arabic and English — native, co-authoritative

- Arabic is **natively composed**, not a mirrored English layout: its own line length, heading rhythm, size steps,
  line-height and component reflow; logical reading and focus order.
- Mixed script: stable IDs, source IDs, URLs, Latin acronyms, dates and numbers stay readable and isolated inside RTL
  (`<bdi>`, `dir="ltr"` on the run — never on the whole component).
- Neither edition may change number, unit, population/denominator, geography, period/currentness, method, source
  authority, certainty, limitation, rights boundary, target/result status, what remains unknown or what measurement would
  change the answer. The bilingual invariance gate fails on any numeric difference between a page pair.
- House terms are fixed (`audit/ARABIC_TERMINOLOGY_AND_STYLE_LEDGER.md`; §3 of `audit/F5_PUBLIC_CORPUS_ACCEPTANCE.md`):
  for example «سجل الدليل», «المجتمع الذي ينطبق عليه الرقم», «قاعدة الاحتساب», «حداثة الأدلة», «توقيت القياس»,
  «مستمر» for durable use, «التحويلات» for remittances as a flow, «البنك المركزي اليمني – عدن» at first mention.
- No English-only visual metadata may disappear in Arabic, and no internal-control vocabulary may appear in either.

---

## 14. Accessibility — WCAG 2.2 as the implementation target

No conformance may be claimed before the final implementation is audited. Design for these outcomes (details and the
current baseline in `audit/F6_DISCOVERY_ACCESSIBILITY_RIGHTS_SECURITY_ACCEPTANCE.md` §3):

keyboard access with a logical order and no trap (2.1.1, 2.1.2, 2.4.3) · visible focus that is never obscured by
sticky UI (2.4.7, 2.4.11) · targets at least 24 × 24 CSS px, 44 for primary touch controls (2.5.8) · reflow at 320 CSS px
and 400 % zoom (1.4.4, 1.4.10) · names, roles and headings for every control and landmark (4.1.2, 1.3.1, 2.4.6) ·
labelled inputs and text errors, announced status (3.3.1, 3.3.2, 4.1.3) · no meaning by colour alone; contrast 4.5:1
for text and 3:1 for UI and graphics (1.4.1, 1.4.3, 1.4.11) · analytical text alternatives for every visual (1.1.1) · RTL
focus and reading order (1.3.2) · reduced motion honoured; nothing needs motion (2.3.3) · single-pointer operation, no
drag-only interaction (2.5.1, 2.5.2). Also: forced-colours mode, image-off, and horizontal tables inside a named,
focusable scroll region.

---

## 15. Performance and sustainability in the visual system

Baseline in `audit/SUSTAINABILITY_PRE_DESIGN_BASELINE.json` and `docs/SUSTAINABILITY_METHOD.md`: without the logo a page
is about 0.09–0.45 MB in four requests; the search index (about 2 MB) loads only on use; no third-party resource. Keep it
that way: self-hosted, subset fonts; no decorative images; SVG or CSS for diagrams; charts drawn from local data; no
client framework weight a static page does not need. Specify the logo's rendered sizes so Code can export derivatives.
No "green" claim, badge or comparison anywhere. Accessibility, Arabic quality, security and evidence integrity outrank
marginal byte savings.

---

## 16. Social / Open Graph system

Every page already emits `og:title`, `og:description`, `og:type`, `og:locale` and a `summary` card from its governed title
and description (`scripts/discovery.py`), with no image. Design the **social-image system**: templates per family
(Home, domain answer, Evidence Record, Reading, Measurement, trust) in both languages, using only governed text (title,
scope/period line, the governed boundary where a figure appears), the logo at a specified size and the canonical link.
A shared image that shows a number must carry its period, population and boundary. Code generates the images at build
time and adds `og:image` only then.

---

## 17. Discovery (keep what F6 established)

One native `<title>` and meta description per page (governed, unique per language); one `<h1>`; self-canonical;
reciprocal `hreflang` for `en`, `ar` and `x-default` (the root); pre-release `robots.txt`; JSON-LD `WebSite`,
`BreadcrumbList` and `Article` (Readings) with governed fields only — no author, dates, image or `Dataset`. Your
templates must keep these head elements and keep the breadcrumb visible where it is today. Contract:
`docs/DEPLOYMENT.md` §Discovery; checks: validator F6-G01…G05.

---

## 18. Security and privacy constraints on the design

The design must work under a strict Content-Security-Policy: no inline executable script (data goes in JSON blocks), no
inline style attributes, no inline event handlers, no external script, stylesheet, font, image or frame, no form. No
analytics, tracking, cookies or accounts; one functional preference (`yfie-lang`). Links to original sources open with
`rel="noopener noreferrer"`. Render data only through escaping. Contract: `docs/DEPLOYMENT.md` §Security; checks: F6-G05.

---

## 19. Deliverables — repository-backed, no screenshot-only handoff

Work inside this repository. Create `design/` (the diagrams in `design/architecture/` are generated; leave them):

| File | Content |
|---|---|
| `design/00_DESIGN_README.md` | What the package is; how to run the reference implementation; the dependency map; decision log |
| `design/01_FOUNDATIONS.md` | Principles, evidence-state grammar, type, grid, space, colour, iconography, motion — with rationale |
| `design/02_TOKENS.json` | Machine-readable tokens (colour, type scale per language, space, radius, elevation, motion, breakpoints, z-index) |
| `design/03_COMPONENT_CATALOG.md` | Every component: anatomy, inputs (governed fields), states, RTL/LTR, responsive, accessibility |
| `design/04_PAGE_FAMILY_COMPOSITIONS.md` | Deterministic module order and composition rules for all 11 families, first-screen contract per family |
| `design/05_RESPONSIVE_RTL_LTR.md` | Breakpoints, reflow, Arabic composition rules, bidi isolation |
| `design/06_VISUAL_TABLE_SYSTEM.md` | Every visual family and table pattern against its contract; detached frame; fallbacks |
| `design/07_INTERACTION_ACCESSIBILITY.md` | Every tool's states and keyboard paths; focus management; announcements; WCAG outcome mapping |
| `design/08_ASSET_MAP.md` | Logo placements and sizes, fonts and subsets, icons, social-image templates |
| `design/09_CODE_HANDOFF.md` | The Design-to-Code mapping required by `handoff/DESIGN_TO_CODE_CONTRACT.md` |
| `design/10_ACCEPTANCE_CHECKLIST.md` | `handoff/DESIGN_ACCEPTANCE_CRITERIA.md` filled in with evidence (screenshots, test output, notes) |
| `design/ESCALATIONS.md` | Every `ESCALATE_TO_MASTER` and `NEEDS_CONTROLLED_CONTENT` item |
| `design/reference/` | **The runnable reference implementation** (below) |

**The reference implementation** renders **every route in both languages** (the same 288 documents as `dist/`) from
`site-src/content/**` — never from a copied or hand-written content model — with every tool working on local data, at
every width, with every state reachable. It may be a static generator, or a React static pre-render, or an extension of
`scripts/build.py`, `site-src/app.js` and `site-src/styles.css`; choose what produces the best implementation-grade
source for Code, and document how to run it. It must keep the discovery head, the JSON data blocks, the CSP constraints
and every behaviour tested by `scripts/tests/test_public_tools.py` and `audit/tranche_c/checks/viewport_acceptance.py`;
run those suites against it. If you cannot produce a runnable implementation, produce an implementation-grade design
source that Code can execute without guessing — and say which you delivered.

Maintain `design/09_CODE_HANDOFF.md` **as you work**, not at the end: tokens, components, states, routes, content
bindings, visual contracts, responsive rules, accessibility behaviour and every exception.

---

## 20. Work plan — gates, one pull request each

| Gate | Output |
|---|---|
| D0 Orientation | Dependency map from the inventory; plan; escalations so far |
| D1 Grammar | Foundations, tokens, evidence-state grammar, shell, type in both languages |
| D2 Hardest families | Home, Explore, `/people/`, `/access/`, `/payments/`, `/remittances/`, Evidence index and records (dense, sparse, withheld), Compare, `/data/` |
| D3 Synthesis and reference | Readings index and details, Measurement, Methodology, About and trust, corrections, 404 |
| D4 Complete binding | Every route in both languages through family rules; no bespoke drift |
| D5 Interaction and accessibility | Search, workbench, Compare, sources, Cite, language, report, download pattern; keyboard, focus, zoom, reduced motion, forced colours, image-off, mobile |
| D6 Visuals and social | Signature and core visuals, table-first renderings, detached frames, social-image templates |
| D7 Acceptance and Code handoff | `design/10_ACCEPTANCE_CHECKLIST.md` complete; `design/09_CODE_HANDOFF.md` final; all gates green |

After each gate record: what became more understandable or truthful; what complexity was added; what could be
removed; routes and states tested; open escalations.

---

## 21. Git protocol

Canonical repository: GitHub `CausewayGrp/Financial-inclusion-`, branch `main`. Branch `design/<gate>-<slug>`; one pull
request per gate; merge only when **Verify** is green. Never force-push; never rewrite `main` or a `checkpoint/*` tag;
never edit `authority/`, `site-src/content/`, `dist/`, `audit/` or `audit/PUBLIC_LITERAL_CLOSURE.json`. If the reference
implementation replaces `scripts/build.py`, `site-src/app.js` or `site-src/styles.css`, it must keep every existing gate
green (`CONTRIBUTING.md` §5). Commit with Conventional Commits; regenerate `FINAL_REPOSITORY_MANIFEST.json` and
`SHA256SUMS.txt` before each commit (`design/**` is already classified).

---

## 22. The twenty-two requirements (checklist)

You must:

1. absorb the actual governed repository (§3);
2. use real English and Arabic content and data — no lorem ipsum, no invented figures (§0);
3. preserve the semantic firewalls (§5);
4. own the visual and product solution boldly (§6, §7);
5. challenge weak inherited layout assumptions (§0);
6. never change evidence meaning silently (§2);
7. escalate semantic needs rather than inventing copy (§2);
8. design desktop, tablet and mobile (§9);
9. design native RTL, not mirrored LTR (§13);
10. use the canonical CauseWay logo without redrawing, recolouring, distorting or AI-regenerating it (§8);
11. use the IBM Plex family appropriately for English and Arabic (§8);
12. solve long and short content through hierarchy and progressive disclosure, not evidence deletion (§4.3);
13. design all core page families and hard states (§9);
14. design Search, Compare, citation, download and report-issue interactions (§10);
15. design the Readings as a flagship editorial family, not a blog or card wall (§11);
16. honour every visual contract and prohibited inference (§12);
17. provide analytical alt text and fallback behaviour (§12, §14);
18. meet WCAG 2.2 design expectations (§14);
19. keep performance and sustainability in the visual system (§15);
20. produce a runnable populated reference implementation or an implementation-grade design source that can be
    executed without guessing (§19);
21. build and maintain a Design-to-Code contract as you work (§19, `handoff/DESIGN_TO_CODE_CONTRACT.md`);
22. finish with a Code handoff that maps tokens, components, states, routes, content bindings, visual contracts,
    responsive rules, accessibility behaviour and exceptions (§19).

---

## 23. Never

- Invent, round, normalise, convert or "tidy" a number, date, label, author, title, licence or source.
- Print the withheld CLM-044 value, name a source without a public locator, or republish a third-party document.
- Merge the two parts of a boundary ("does not establish" · "limits of the measure") or print the internal delimiter.
- Show an internal ID, enum, field name or repository term as prose (stable IDs as citation references are fine).
- Turn missing into zero, a listing into operation, a target into a result, a sequence into a cause.
- Add analytics, tracking, a font CDN, an external script or a form.
- Claim WCAG conformance, legal review, rights clearance, native-language certification, security guarantees or public
  release readiness.

When the checklist in `handoff/DESIGN_ACCEPTANCE_CRITERIA.md` is complete with evidence and every gate is green, the
Design package is ready for acceptance and for Claude Code (`handoff/CLAUDE_CODE_MASTER_PROMPT.md`).
