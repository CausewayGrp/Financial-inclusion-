> STATUS: **DESIGN HANDOFF READY.** Executable. Read `handoff/README_FIRST.md` first; this is step 2 of its reading order.

# Claude Design — master brief
## Yemen Financial Inclusion Evidence · أدلة الشمول المالي في اليمن

This is the one executable brief for the design of this product. It is written from the repository as it stands; where
it names a file, open that file — it is the detail this brief summarises. Nothing here requires an earlier conversation.
If this brief and a governed projection ever disagree, the projection is right and the difference is an escalation (§2).

---

## 0. How to work at full capability

> **The kernel — re-read it at the start of every gate.** Protect the truth: design the evidence system, never the
> facts. Aim for the most complete information with the least load at any one moment: keep complexity where it is true,
> and never make the reader carry the whole evidence system at once. Make evidence understandable, explorable and
> unusually easy to verify; make scope, uncertainty and boundaries visible. Give Arabic the same design intelligence as
> English. Use sophistication only where it improves comprehension. Do not flatten unlike evidence for visual
> consistency. Persist every accepted material decision in this repository so Claude Code can continue without your
> conversation.

You are the principal product designer, information designer, bilingual/RTL design lead and reference-implementation
engineer for a mature public evidence product. Use everything you can do:

- **Plan before pixels.** Build a dependency map of families, components, states and data bindings from
  `handoff/ROUTE_CONTENT_AND_STATE_INVENTORY.json` before you design a single screen. Keep it current as `design/00_DESIGN_README.md`.
- **Design with the real thing.** Every screen uses the real governed English and Arabic content and data from
  `site-src/content/`. No lorem ipsum, no placeholder figures, no invented labels — ever.
- **Build, don't describe.** Your main deliverable runs: a fully populated reference implementation of every route in
  both languages (§19). Mock-ups and documents support it; they do not replace it.
- **Compete before you commit.** At D1, build two or three materially different design theses — different answers to
  type, grid, density, evidence-state grammar and Arabic composition, not colour variants of one layout — and test each
  on the same stress trio with real English and Arabic content: Home, the dense Evidence Record `/evidence/CLM-003/` and
  the flagship Reading `/readings/same-year-different-number/`. Choose with recorded reasons; only then propagate (§20).
- **Prove on the hardest cases first** (§9.2), then generalise through page-family rules, never route-by-route drift.
- **Only what is in the repository binds you.** At D0, record in `design/00_DESIGN_README.md` whether an approved visual
  board, colour board or homepage mockup has actually been supplied (its path in the repository), or that none has. A board
  or mockup that is not in the repository — remembered, described elsewhere or assumed — binds nothing.
- **Keep a durable record.** Every decision goes into the decision log and every route and state into the coverage
  ledger as you go (§19); the next person must be able to see what was decided, why, and what has been proved.
- **Look at your own work.** Render every family at 320, 390, 640 and 1440 CSS px in Arabic and English, look at the
  screenshots, critique them against `handoff/DESIGN_ACCEPTANCE_CRITERIA.md`, fix, and repeat. Test keyboard paths, zoom,
  reduced motion, forced colours and image-off yourself.
- **Challenge weak inheritance.** The layout and styles of the pre-design baseline renderer (its stylesheet, removed with
  that renderer at EAD-01) are a behavioural baseline, not
  a design. Replace anything that is merely inherited. Keep only what earns its place.
- **Decide.** Resolve ordinary design questions professionally and record the reasoning; do not stop to ask about
  details a senior designer would settle. Escalate only truth and missing governed content (§2).

**The loop for every consequential decision** (a family composition, a component, a visual form, a tool pattern, a
state grammar — not a cosmetic tweak):

1. **Orient** — read the route's governed content, its Page Spec, its visual contracts and the baseline in `dist/`.
2. **Question** — what is governed, what is free (§6), and what problem is actually being solved for which reader.
3. **Explore** — where the decision matters, sketch materially different solutions, not variants of one.
4. **Challenge** — test them through the audience lenses (§9.3), the evidence and firewall (§5), Arabic (§13),
   accessibility (§14), mobile, the four review tests (§7) and what Code will have to build (§19).
5. **Decide** — choose, and write the decision-log entry (§19).
6. **Prototype** — in the reference implementation, with the real governed English and Arabic content.
7. **Test** — on the hard states (§9.2), not only on ideal content; at every width, in both languages, by keyboard.
8. **Persist** — update the decision log, the coverage ledger, the design-debt register, the escalations and
   `design/09_CODE_HANDOFF.md`.
9. **Continue** — to the next decision only when this one's tests pass; to the next gate only when its exit holds (§20).

**The repository is your memory.** A long conversation forgets; the repository does not. At the **start of every
gate**, re-read: the kernel above; the decision log (`design/00_DESIGN_README.md`); the coverage ledger
(`design/COVERAGE.csv`); `design/ESCALATIONS.md`; the design-debt register (`design/DESIGN_DEBT.md`);
`design/09_CODE_HANDOFF.md`; and the governed content and visual contracts of the routes the gate touches. At the **end
of every gate**: update those records, run the gate's tests (§20), commit, push (or deliver the bundle, §21) and leave
the working tree clean. Never keep a second copy of any of these records.

**The Code recipient test** closes every gate: could Claude Code take this commit, without your conversation, and tell
what is intentional, what is temporary, what is implemented, what remains, what must not be reinterpreted, which tests
must pass and which owner or release items remain? If not, the gate is not complete.

---

## 1. The product and its north star

A bilingual public evidence resource, built and maintained by CauseWay, that helps people **understand, compare and
verify** the evidence on financial inclusion in Yemen. It is a public evidence service, not a generic website: it
supports human decisions by clarifying evidence; it makes no regulatory, political, business or funding decision for
anyone.

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
| Production Master | `authority/Yemen_Financial_Inclusion_Evidence_Master.xlsx` (SHA-256 `8bf7e5aae3a80b21ebc3bb56248015f6dfd0a76c8efaf19c1ac86b93ecef08e1`) | The only semantic, evidence, source, rights and publication authority |
| Page Specs | `site-src/content/page_specs.json` (SHA-256 `bd4fa5b4b3de6d24b3313d105d1c0c25f1b3efd877df9f4a124002450c0d985d`) | Every route: titles, descriptions, sections, bound objects, prohibited inferences, render rules |
| Interface copy | `site-src/content/content/interface_copy.json` | Every interface label in both languages (`UI-*` IDs). With the navigation labels below (primary, trust and footer, which the generator writes from the Master's navigation rows into `navigation_interaction.json`), the only source of interface wording |
| Presentation depth (contract) | `site-src/content/presentation_priority.json` | For the Domain Answer, Evidence Record and Comparison families: what shows first, what may be disclosed later, how many Measurement cards a domain page shows |
| Navigation and interaction (contract) | `site-src/content/content/navigation_interaction.json` | Navigation, trust layer, footer, breadcrumbs, next actions, page families, journeys, tools, hard-state cases |
| Everything else | `site-src/content/**` | Evidence records, Readings, Measurement, questions, sources, visual contracts, chronology, search |

**Which files you render.** `handoff/ROUTE_CONTENT_AND_STATE_INVENTORY.json` → `projection_roles` classifies every file
under `site-src/content/`: **RENDER** (a direct input), **VIA_SPEC** (its public text already reaches each page through
the Page Spec — render the Page Spec's copy), **CONTRACT** (the two hand-maintained contracts above) and **REFERENCE**
(not public: the `data/*.json` tables, the Evidence Passports, the source library and catalogues — read them to understand
the system, never render them; their values reach pages only through Evidence Records and the resolved rows in
`site-src/content/visuals/visual_design_contracts.json`). Nothing under `site-src/content/` is edited by hand: the projections are
generated from the Master, and the two contracts are maintained by the programme and validated by the generator. If a
hash in this brief differs from the repository, the repository is right.

**Precedence.** Master → Page Specs and the other generated projections → the two contracts → the reference build in
`dist/` → this handoff's guidance (which never adds meaning, only says how to read the layers above).

**Page Spec structure worth knowing.** On 15 routes `sections` holds one row per language for the same `section_order`
(inventory `section_rows_split_by_language`): for each language render the rows that carry that language's heading and
body, in numeric `section_order`. Each Page Spec's `frontend_render_policy` lists what is never rendered directly (internal
fields, raw enums, file paths) and states that governed wording is rendered exactly as authored.

**The two contracts are maintained, not generated.** `presentation_priority.json` and `navigation_interaction.json` are
controlled contracts (class `CONTROLLED_CONTRACT` in `FINAL_REPOSITORY_MANIFEST.json`): the programme steward edits them
in place and the generator validates them against the Master's projections. You never edit them. Where one of their
descriptive fields ever disagrees with governed interface copy, a Page Spec or behaviour the test suites assert, the
governed copy, the Page Spec and the tested behaviour win, and you record the disagreement as `ESCALATE_TO_MASTER`. The
disagreements found before the handoff were corrected on 27 September 2026 (register OWN-07 and OWN-08, closed): the
report-issue path, the Reading breadcrumb, the six Compare dimensions and comparable set, the workbench inputs, three
hard-state sentences, journey J10, and the `/remittances/` Measurement card.

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

The reading order is the one in `handoff/README_FIRST.md` §4; this brief is its step 2. After it, go deeper in this order:

1. `handoff/ROUTE_CONTENT_AND_STATE_INVENTORY.json` — every route with its family, titles, sections, bound evidence,
   visuals, Readings, Measurement, sources, next actions and structured data; the collection each index route lists
   (`collection`); the verification state each Evidence Record renders; the hard-state cases with the data at their
   route; every lineage, verification, visual-tier, grammar and technical state; `projection_roles`; the thirteen
   journeys.
2. `site-src/content/content/navigation_interaction.json` — `global_navigation`, `trust_navigation`, `utilities`,
   `footer_groups`, `breadcrumbs`, `route_next_actions`, `page_families`, `interaction_tools`, `hard_state_acceptance`,
   `journeys`, `static_progressive_enhancement_boundary`.
3. `site-src/content/page_specs.json` — the Page Specs of the hard-state routes (§9.2).
4. `handoff/VISUAL_DESIGN_CONTRACT.md` and `site-src/content/visuals/visual_design_contracts.json` — before any chart.
5. `handoff/DESIGN_ACCEPTANCE_CRITERIA.md`, `handoff/DESIGN_TO_CODE_CONTRACT.md`,
   `handoff/ENGINEERING_HANDOFF_EXPECTATIONS.md` — how you are accepted and what Code needs.
6. The running baseline: `python3 -m http.server 4173 --directory dist`, then `/ar/` and `/en/`. Try every tool.
7. House terms: `audit/ARABIC_TERMINOLOGY_AND_STYLE_LEDGER.md`, §3 of `audit/F5_PUBLIC_CORPUS_ACCEPTANCE.md`, and
   `preferred_public_arabic_terms` in `handoff/IMPLEMENTATION_MANIFEST.json`.
8. `FINAL_OPEN_ITEMS_REGISTER.md` — what is unknown; design around it, never fill it.

Counts change when the Master changes: always take them from `site-src/content/content/public_inventory.json`. They
describe the system; they are not an instruction to show everything at once.

---

## 4. Product model

### 4.1 Page families (11) and routes

| Family | Routes | Job |
|---|---|---|
| Orientation | `/` | Identity, the product's promise, four common starting questions (QE-002, QE-003, QE-005, QE-011 — the R8.4A decision, in the inventory at `/` → `collection.starting_question_ids`), one Featured Reading, the evidence snapshot (Home section 3, §4.4) |
| Question Entry | `/explore/` | All eleven governed entry questions in the four clusters of the inventory (`/explore/` → `collection.question_groups`, headings `UI-QUESTIONS-*`); one "Go deeper / تعمّق في التحليل" Reading |
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
one clock, unit, denominator or population. The Home **evidence snapshot** is Home's governed section 3 ("Three figures,
three different things measured"), as authored: each figure already carries its measure, population and period in the
governed text, with the three records it cites. Do not extract numbers from it into a figure strip, and do not add an
evidence-state badge: records carry no governed unit or state label for that.

### 4.5 Governed text the baseline renders elsewhere

A few Page Spec sections introduce a component rather than stand alone; render each once, where it belongs:

- Home sections 2 ("Start with the question, not the dataset") and 9 ("Questions to start from") and Explore section 5
  ("Questions to start from") introduce the question lists; the baseline shows the lists under the governed headings
  `UI-QUESTIONS-*` instead. Use one of them as the list's introduction or leave them out; none carries a number or a
  limitation.
- Each Reading's section 1 ("What the evidence supports") repeats the Reading's thesis word for word; the baseline shows
  the thesis once, as the standfirst. Show it once.
- Home's order in the baseline — identity, starting questions, section 3 with its records, sections 4–6, the system visual
  at `#system` (where QE-001 lands), sections 7–8 — is a precedent, not a mandate; keep the `#system` anchor.

### 4.6 A connected evidence system, not isolated pages

A reader should move intelligently along question → answer → Evidence Record → source → method → Reading → measurement
gap, and back: from a record to the answers and Readings that use it, from a source to the records it supports, from a
Measurement priority to where its gap is examined. Use only relationships the projections bind (the inventory's
`next_actions`, each record's Readings, each Page Spec's bound objects, each priority's links) — never inferred ones —
and show the most relevant few at the moment they help, with the rest one step away. A link cloud is not a connected
system.

---

## 5. The semantic firewall and public-state distinctions

These distinctions must be visible in every surface, in both languages, and survive when a component is cropped,
screenshotted or read without colour:

people ≠ households ≠ firms ≠ accounts ≠ active accounts ≠ customers ≠ transactions ≠ terminals ≠ agents ≠ providers ≠
beneficiaries · access ≠ ownership ≠ registration ≠ adoption ≠ active use ≠ frequency ≠ persistence ≠ quality ≠ outcome
· infrastructure ≠ use · infrastructure ≠ outcome · target ≠ result · programme KPI ≠ national prevalence · regulation ≠
implementation ≠ operation ≠ experienced outcome · licence/listing ≠ operation · observation ≠ fieldwork ≠ publication ≠
retrieval or review · historical ≠ current · observed ≠ estimated ≠ projected · missing ≠ zero · chronology ≠ causality ·
source-owner analysis ≠ independently established impact · the same figure repeated from one lineage ≠ independent
corroboration · financial-education activity ≠ literacy ≠ capability ≠ behaviour ≠ outcome.

Layout is an argument: proximity, alignment, shared axes, shared colour, hierarchy, sequence and animation all imply
relationships. Use them so that they protect these distinctions, never so that two unlike things read as one.

States you must give a distinct, non-colour-only visual grammar (the inventory lists them all, with their governed
labels):

- **Verification state** of an Evidence Record — what its source section actually renders: sources listed; sources listed
  with a note that some have no public locator; partly resolved; composite with its members listed; composite whose
  members are not listed; framing rule with no fact (no source expected); original not public (the value may be withheld,
  as for CLM-044); plus the unbound and no-source states the grammar keeps for future records. Each state, its governed
  copy (`UI-VERIFY-*`, `UI-EVID-*`) and the records in it are in the inventory → `hard_states.verification_states`; each
  record's own state is on its route. Lineage (`BOUND_EXACT`, `BOUND_PARTIAL`, `COMPOSITE_OF_OBJECTS`, `FRAMING_NO_FACT`)
  is the Master's classification behind it.
- **Visual grammar states** — measured, reported, administrative, derived, historical, programme, estimated, projected,
  partial, unknown; and the structure markers break of vintage, break of universe, same-year revision, missing,
  disagreement, target, result, not comparable, nominal and withheld (`visual_design_contracts.json` → `grammar`, with a
  drawing rule each; labels in `grammar_labels`, `UI-VIS-*`).
- **Technical states** — a failed index, a malformed link, an unknown reference, a duplicate in Compare, no search
  match, 404, no JavaScript. A technical state must never look like "no evidence", and an evidence gap must never look
  like a software error.
- **Other states that must not collapse:** a rights-restricted or not-yet-licensed download is not a technical error; a
  source with no public locator is not a missing source; historical is not current; unknown is not "not applicable".
  Every such state is designed deliberately, in plain governed words — never cute, apologetic or alarming.

---

## 6. Frozen for Design · free for Design

**Frozen:** factual content; evidence relationships; public-state distinctions; route purpose; required behaviours and
actions; Arabic/English equality; accessibility outcomes (§14); visual semantics and prohibited inferences; the
canonical CauseWay logo; the IBM Plex family requirement; citation and source behaviour; rights constraints; the rule
that no internal or repository language reaches the public.

**Free:** composition; grid; hierarchy; rhythm; spacing and whitespace; density; typography within the IBM Plex family;
palette within contrast and identity constraints; component form; the visual grammar of states (within §5); chart form
where several forms satisfy the visual contract; how navigation, menus and the trust layer behave (labels and
destinations are governed, §4.2); progressive disclosure (never hiding a limitation, §4.3); interaction choreography;
motion; mobile behaviour; Arabic spatial composition; the presentation of search, sources and citation; the experience
of Evidence Records, Readings, Methodology and the Measurement Agenda; the download and export interaction; editorial
pacing. Challenge the inherited presentation in all of these.

**Who owns what.** Design owns the visual and interaction solution and the runnable reference site. Code owns the
production runtime after acceptance (`FINAL_OPEN_ITEMS_REGISTER.md`, class ENGINEERING_AFTER_DESIGN;
`handoff/ENGINEERING_HANDOFF_EXPECTATIONS.md`). The owner decides identity, funding, contact, licence, public origin and
logo variants (OWNER_INPUT). Release needs its own acceptance (RELEASE_ONLY). The Master, through the steward, owns every
fact and every governed word. Design never decides for the others: it designs the honest state that exists today.

---

## 7. Design character

**Ask of the design:** white-dominant · restrained · serious · modern · distinctive · unusually clear · editorial rather
than SaaS or dashboard · high-end without luxury decoration · excellent Arabic and RTL · dense where expert verification
needs density · spacious where comprehension needs space · **evidence as protagonist** · **CauseWay as steward**.

It should feel calm but powerful · formal but not bureaucratic · precise but not cold · distinctive but not theatrical ·
editorial but not magazine-like · deep but not crowded · accessible but not visually generic.

**Avoid:** generic AI-site aesthetics · card-wall dependence · identical rounded cards and pills everywhere · decorative
dashboards · meaningless mini-charts · giant decontextualised numbers · arbitrary three-column repetition · gratuitous
gradients · donor-report visuals · badge clutter · over-animation · stock photography used as decoration · generic NGO or
consultancy styling · news-portal density · "data theatre".

- **Motion** explains a change of state or a relationship, or it goes. Ask of every movement: what does the reader
  understand better because this moved? No count-up numbers, decorative parallax or fintech spectacle; nothing depends
  on motion, and reduced motion is honoured (§14).
- **Imagery.** The product is evidence-led, not photography-led; the baseline uses none. An image must earn its place
  with an editorial purpose. Never: generic Arab fintech stock, handshakes, coins and cash clichés, Gulf imagery used as
  Yemen, poverty or conflict as atmosphere, children as decoration, watermarked or provenance-unknown images, or
  AI-generated documentary-looking photography. Before any external image is proposed, record its purpose, source,
  creator, rights holder, licence, attribution, place and date, crop and derivative rights, consent and dignity, and
  conflict-sensitivity; request the image and its credit line as `NEEDS_CONTROLLED_CONTENT` — its use is an owner rights
  decision. If provenance or rights cannot be established, do not use the image.
- **Dark mode** is optional. Explore it only if it improves the product without weakening evidence-state semantics,
  contrast, charts, the CauseWay identity or performance, and record the decision either way. It is a preference, not an
  accessibility claim; the logo is never inverted or recoloured for it (§8).

**Four review tests** — apply them to your own work at every gate and record the results
(`design/10_ACCEPTANCE_CHECKLIST.md`):

1. **Anti-template.** If the Yemen content and the CauseWay identity disappeared, could this be sold tomorrow as a
   generic NGO, consultancy, SaaS or AI website? If yes, challenge the design again.
2. **Source owner.** If the source institution saw this screenshot without its page, could it reasonably say the product
   made its evidence claim more than it does? If yes, revise.
3. **Screenshot misuse.** If this figure, chart or statement is cropped and forwarded alone, is it likely to be
   misunderstood? If yes, carry enough scope and boundary inside the object.
4. **Portable evidence.** If this object leaves the site (print, export, citation, social image), does it stay
   intelligible, attributable and bounded? If not, it is incomplete.

---

## 8. Identity

- **Logo.** `site-src/assets/CauseWay_Master_Logo.png` (6250 × 6250 px RGBA PNG, SHA-256
  `5830163d…`, full hash in `FINAL_REPOSITORY_MANIFEST.json`) is the only logo authority. Never redraw,
  recolour, distort, crop, trace, vectorise or AI-regenerate it. Specify where and at what rendered sizes it appears
  (header, footer, 404, social images) and its clear space. It is 96–99 % of every page's transfer today; web-size
  derivatives are an owner-approved engineering step after Design (open item EAD-03) — specify the sizes Code must
  export, do not produce them yourself. The reference build whitens the footer logo with a CSS filter
  (`brightness(0) invert(1)` in the pre-design baseline stylesheet, removed at EAD-01): that is a recolouring and must not
  be carried forward. On a dark
  surface, place the logo on a light field with its clear space, or record a request for an owner-supplied reversed
  version (`FINAL_OPEN_ITEMS_REGISTER.md`, OWN-06) — never derive one by filter, blend or tracing.
- **Typography.** Required: IBM Plex Sans (English) and IBM Plex Sans Arabic (Arabic), self-hosted from
  `vendor/fonts/` (the `woff2` files of `@ibm/plex-sans@1.1.0` and `@ibm/plex-sans-arabic@1.1.0`, unchanged, with their
  SIL Open Font License; provenance and rules in `vendor/fonts/README.md`). Copy them into your reference
  implementation's output with the licence; never load a font from a CDN. Use the files as shipped: the licence reserves
  the name "Plex", so a self-made subset is an owner decision. Other members of the
  IBM Plex family (Serif, Mono, Sans Condensed) may be added for a defined role with a written rationale; no typeface
  outside the family. Use weights deliberately; Arabic needs its own line height, size steps and heading rhythm, not
  English values mirrored. The baseline's fallbacks (Arial, Tahoma) are not the design.
- **Tokens.** `handoff/DESIGN_STARTING_TOKENS.json` (and the palette echoed in `handoff/IMPLEMENTATION_MANIFEST.json`)
  is a hypothesis. Replace it with your own documented system (`design/02_TOKENS.json`), meeting contrast (§14). The
  identity constraints are only these: the canonical logo, unaltered, with its clear space, and the IBM Plex family.
  There is no approved brand palette in this repository: choose one that sits well beside the logo's own colours and
  record why.

---

## 9. Required coverage

### 9.1 Surfaces

Design and build every one of these, in both languages, desktop, tablet and mobile:

- **Global shell:** header, primary navigation with the Method & Measurement family, trust layer, footer, language
  switch, search entry, cite and report-issue utilities, skip link, breadcrumbs.
- **Home**; **Explore**; **all eight domain routes** (prove the hard ones first); **Evidence index** and **Evidence
  Record** (dense `/evidence/CLM-003/`, thin single-source `/evidence/CLM-015/`, conflicted `/evidence/CLM-037/`,
  composite with members `/evidence/CLM-031/`, composite without listed members `/evidence/CLM-014/`, partial
  `/evidence/CLM-039/`, framing `/evidence/CLM-004/`, withheld `/evidence/CLM-044/`); **Compare**; **Readings index**;
  **Reading detail**
  (at least three stress cases: the longest, `/readings/after-transfer-persistence/` (about 900 English words, seven
  sections); the one with the most visual data, `/readings/same-year-different-number/` (signature visual RV-CWR-001, two
  panels); and one whose visual is not drawn from data, `/readings/banking-jump-measurement-basis/` (RV-CWR-002,
  SUPPORTING — its values are not held as rows, so the governed text carries it); the second signature chain,
  `/readings/from-rail-to-result-missing-middle/`, is also required at D6);
  **Data/sources/Resource Library** (with the chronology); **Measurement Agenda**; **Methodology**; **About** and every
  **trust** route; **corrections/report-issue** journey; **404**.
- **Hard evidence states** (§5), **all visual families** (§12), the **social/OG system** (§16), **mobile**, **RTL** and
  **accessibility states** (focus, error, status, reduced motion, forced colours, zoom).
- **The small surfaces:** footer, search with no match and with a failed index, the language switch on every family,
  citation, original-source links and the no-public-locator state, the unavailable-download state, print, empty,
  unknown and error states, and every success or failure message a tool can show.

A family template applied to a route is not a reviewed page: each route is looked at, in both languages, and marked in
the coverage ledger (§19) on its own row.

### 9.2 Hard-state acceptance — prove these before generalising

From `navigation_interaction.json` → `hard_state_acceptance` (routes in both languages):

| State | Route | Must prove |
|---|---|---|
| dense_domain | `/people/` | High density stays scannable; wave, fieldwork, population and limitation stay attached to the headline figure |
| sparse_unknown | `/access/` | Unknown geography is visibly unknown — not zero, not an empty map |
| institutional_sequence | `/payments/`, then `/reforms/` | FPS, RTGS, institution-building, implementation, operation, use and outcome are distinct states. `/payments/` carries FPS, RTGS and institution-building; `/reforms/` carries the rule-to-outcome chain (VIS-PAYMENT-RAILS). Do not introduce a state the evidence does not name |
| vintage_conflict | `/remittances/`, then `/readings/same-year-different-number/` | Observed, estimated and projected states and the vintage break are legible without choosing a winner — on `/remittances/` through VIS-REMITTANCE-MACRO (its rows carry REPORTED, ESTIMATED, PROJECTED and BREAK_VINTAGE). The same-year revision itself is drawn by RV-CWR-001 in the Reading that `/remittances/` links to; do not draw a revision on the domain page without a contract row. The page's one Measurement card (MA-001, the people-side baseline that names household remittance receipt as missing evidence) is about households, not the macro series: keep the two visibly apart |
| verification_dense | `/evidence/CLM-003/` | Raw totals and the source's own percentage coexist; the discrepancy is visible; the limitation prominent |
| verification_sparse | `/evidence/CLM-004/` | A framing record that sets a measurement rule — no fact to source, so no source expected — is not styled as missing evidence or an error. Prove also the thin single-source record `/evidence/CLM-015/`: it must not look weaker or less trustworthy than a dense record |
| compare_unlike | `/evidence/compare/` | No visual pressure to compare unlike units or populations; the boundary is the first conclusion |
| source_scale | `/data/` | Every source stays discoverable without a wall of links; curated cards are visibly curated, not a separate authority |
| reading_longform | `/readings/same-year-different-number/` | Long analysis stays bounded, readable and traceable to its records |
| measurement_nonranking | `/measurement/` | P0/P1 reads as sequencing within this agenda, never as national policy or spending priority |
| trust_plain_language | `/about/` | Purpose, CauseWay's role, limits, source authority and correction are clear without backend terms |
| mobile_rtl | `/ar/payments/` | At 320–400 px, Arabic order, numeral and Latin isolation, tables, controls and the verification path stay coherent |

Also prove: an Evidence Record whose value is **withheld** (`/evidence/CLM-044/` — the value is not published and must
never appear), a **composite** record whose members are listed (`/evidence/CLM-031/`) and one whose members are not
(`/evidence/CLM-014/`), and a record with **partial** lineage (`/evidence/CLM-039/`). Each hard-state case in the
inventory carries the facts at its route (`data_at_route`).

### 9.3 Journeys

The thirteen journeys in the inventory are acceptance paths — first-time reader; journalist verifying a number;
journalist challenging a Reading; researcher testing comparability; regulator; payments analyst; provider; development
partner; humanitarian practitioner; anyone challenging a record; reuser; accessibility user; a payment-rail explainer.
Each must succeed on mobile and desktop, in both languages, by keyboard.

**Audience lenses.** Challenge every consequential decision (§0, step 4) through these readers: a citizen or
non-specialist; a journalist; a researcher or academic; a bank or other provider; the Central Bank or another regulator;
government; a development partner, donor or UN agency; a source institution; an Arabic-first reader; a mobile reader; a
keyboard or assistive-technology user; a reader on a slow or expensive connection. Design one governed evidence system
that serves their different intents — never a separate product, mode or entrance per audience.

### 9.4 What each family must achieve — tests, not layouts

These are outcomes to test; the composition is yours.

- **Home** orients; it does not reproduce the database. Test it with a cold reader — a person the owner supplies, or a
  fresh agent that has not seen this repository or your work and is shown only the rendered page — in each language,
  at 390 and 1440 px:
  within about 30 seconds they can say what the product is, why it differs and where to start; within about 90 seconds,
  that evidence here has scope and boundaries and can be explored and verified; within about 180 seconds they are inside a
  substantive evidence journey. Record who read, how, and what they said.
- **Explore** makes the governed questions a natural way into the evidence; no reader needs the internal taxonomy.
- **Domain answers** share one system without being identical: let each domain's evidence structure shape its
  composition (dense survey evidence, a sparse map, an institutional sequence, a vintage conflict are not one layout).
- **Evidence Records** are unusually strong professional objects: claim, unit, population, calculation base, period,
  evidence state, what it establishes, what it does not, source, citation, the Readings and answers that use it, the
  relevant method and the route to challenge or correct it — each readable at a glance, and the central figure harder
  to misuse in a screenshot than on any dashboard.
- **Readings** are one editorial family, not clones: pacing can follow the argument; long-form typography, inline
  evidence, source verification, print, Arabic and mobile are designed; "What would change this reading?" is the
  family's intellectual signature (§11).
- **Data & sources** makes provenance inspection easy for professionals and usable for non-specialists; the source
  owner stays visibly distinct from CauseWay's synthesis and presentation.
- **Methodology** is a learning experience, not a long document: a first-time reader first grasps how the product
  decides what it is safe to say, then goes deeper — authority flow, populations and units, calculation bases, evidence
  clocks, survey versus administrative evidence, observed/estimated/projected, programme versus population,
  uncertainty, corrections and editions — using the governed examples its Page Spec already carries.
- **The Measurement Agenda** shows, for each priority, the decision or question it constrains, what is known, what is
  not, and what measurement would change it. Unknowns look intentional and analytically useful, never like missing web
  content.
- **About and trust** answer why the product exists, what CauseWay adds and does not do, who owns the source evidence,
  stewardship and independence, maintenance and currentness, and how to challenge or correct — with the governed text
  that exists; the owner's identity and funding statement is an open item (OWN-01), never filled. Trust pages get the
  same design discipline as the flagship pages.

---

## 10. Tools — first-class, local, tested

All tools run on local packaged data; none may need a network call. Their accepted behaviour is tested in
`scripts/tests/test_public_tools.py`; keep it and design it well.

- **Search** (`static-data/search_index.json`, aliases in `search_aliases.json`): query as you type; Arabic normalisation
  and English matching; exact stable IDs outrank titles, titles outrank summaries, summaries outrank body text; result
  types page · question · evidence · Reading · Measurement · source · source locator; `Ctrl/Cmd+K` and `/` open it; focus
  enters the query and returns to the opener; results keyboard-reachable and announced; a no-match says that absence
  from search is not absence of evidence; a failed load is a technical state. Measurement results open their `#MA-00x`
  anchor. The index loads only when Search opens. Still to build: a `?q=` URL state and a facet by result type (the
  type labels exist: `UI-JS-TYPE-*`). A facet by domain needs a governed domain field on search records, which does not
  exist: request it as `NEEDS_CONTROLLED_CONTENT` rather than inferring a domain from routes or text. Treat Search as a
  product: result types visibly distinct in both languages (a question, a record, a Reading, a source, a priority); a
  no-match that offers a way on (Explore's questions, the Evidence index) in governed words; typo-tolerant matching only
  as a pattern Code can implement on the local index — design it, do not promise it.
- **Evidence workbench** (`/evidence/`): the baseline embeds the site search on this page (input `global-search`;
  results `.search-hit`; its failure state `#search-results .empty`) — keep it, the tests require it. A record filter, if
  you add one, is a separate control. Rows reveal the record's governed title, period or currentness, population and a
  limitation clue; never a wall of every record. The
  record's `object_class` is an internal enum and is not shown. Facets are optional: none has governed labels today, so a
  facet (by verification state, by domain) needs its heading and values requested as `NEEDS_CONTROLLED_CONTENT`.
  Add-to-Compare appears only on the 13 comparable records.
- **Compare** (`/evidence/compare/?records=ID,ID[,ID[,ID]]`, slot order): 2–4 records from the comparable set — the
  13 records bound to the Compare Page Spec (inventory → `/evidence/compare/` → `collection.comparable_record_ids`); any
  other ID, even a real record, is announced as "not available for comparison here", a link error and not a finding.
  Compatibility rows come **before** values, in the six governed dimensions of `yfie-compare-dimensions` — definition,
  population or base, period, method, source reference, currentness — each marked same / different / missing, then the
  boundary row ("What not to conclude"). One assessment per comparison, from the governed set: structurally aligned on
  the available fields · qualified comparison only · not a direct comparison · direct comparability cannot be established
  (a required field is missing) — plus the separate "same record selected more than once" state (`UI-JS-COMPARE-*`).
  Never a truth score; never average, normalise, rank, convert or pick a winner. Wrong count, malformed list and unknown
  ID are announced technical input errors; the language switch keeps the comparison (try `CLM-001,CLM-010`). Still to
  build: entry into Compare from a record — only on the pages of the 13 comparable records, pre-selecting that record —
  and a mobile form of the four-column comparison. CLM-044 is in the comparable set; its withheld value never appears.
- **Source directory and Resource Library** (`/data/`): the full original-source register and the small curated library
  are two jobs; `?source=` deep links open and focus the card; an unknown reference is an announced link error while every
  source stays visible; the nine sources without a public locator are never named or linked. Links to original sources
  are visibly external (an accessible cue whose words you request as governed copy) and open without an interstitial or
  modal. Group the curated cards by
  their governed `resource_category`. The reader-facing document type is `document_label` / `document_label_ar`
  (`site-src/content/sources/source_reference_map.json`, both languages): of the 151 displayed sources, 142 have one and 9
  do not (inventory → `/data/` → `collection.displayed_sources_without_document_type`). A type filter, if you design one,
  uses only that field and puts those nine in an explicit "type not recorded" group whose label you request as
  `NEEDS_CONTROLLED_CONTENT` — never a synthesised type.
- **Cite**: copies the governed citation plus the canonical link; a locator-only source is cited as "reference ·
  locator"; the edition line is governed ("Edition of 26 September 2026").
- **Report an issue** (`UI-HEADER-REPORT-AN-ISSUE`): opens `/{lang}/contact/`, from a record `/{lang}/contact/?record=<ID>`,
  carrying the originating record and route; Contact offers a mail action to the governed address with the reference in
  the subject and links to Corrections, which accepts the same `?record=`; bad references are technical errors; a report
  never changes the record. You may design a richer reporting intent — for example choosing what kind of problem it is
  and composing the message on the page before it opens in the reader's mail — only as client-side composition into that
  same mail action: no backend, no form element, no new address, no promised response time, and every new word
  requested as governed copy. Do not default to a generic name/email/message form: think in the reader's intents — a
  factual error, an interpretation challenge, an overlooked source, a methodology question, a technical problem, press,
  reuse or citation, general contact — carry the page, object and edition automatically, and ask for nothing the
  message does not need.
- **Controls and inputs** (search, filters, Compare slots, any reporting-intent choice or message composition): the site
  collects nothing and submits nothing (§18), so for every input ask why it exists; if there is no good answer, remove
  it. Each one has a visible label, a text error, preserved input after an error or a language switch, keyboard and
  touch operation, RTL behaviour and a success or failure state; where the reader might wonder what happens to what they
  type, a short privacy note in governed words.
- **Language**: preserves route, object, query and hash; never translates a user's query.
- **Download**: design the pattern for CauseWay-generated downloads (a record's governed fields; a chart's governed data
  table; a citation file; a Reading as PDF). None is enabled until the owner decides the reuse licence for CauseWay
  content (open item OWN-04): design the disabled and enabled states, and ship the disabled state. Third-party documents
  are never offered for download: a public URL is not redistribution permission. Downloads are not conversion buttons:
  design per object only the formats that serve it — a Reading as print and PDF; an Evidence Record as print, a citation
  file (for example RIS or BibTeX) and its governed fields as CSV; a chart as a framed image (PNG or SVG) with its
  governed data table as CSV; a table as CSV or XLSX; Methodology and the Measurement Agenda as print; a source as its
  citation and its original-source link, never its document. Arabic exports are first-class: Arabic headings and
  labels, right-to-left layout, correct encoding. Every portable object carries its title, period, population, source,
  key boundary, edition, canonical link, suggested citation and a reuse line (governed copy that follows the licence
  decision, OWN-04 — request it; never write it).
- **Rights in the interface.** Keep four kinds of material visibly apart: CauseWay's own material; third-party material
  that may be redistributed; third-party material whose redistribution is restricted or unclear; and values CauseWay
  derived from third-party evidence. CauseWay's identity never implies ownership of the underlying data; where
  redistribution is not permitted, send the reader to the original source instead of packaging it. A data package
  (data files, bilingual readme, data dictionary, source register, method, licence, checksums) is a later Code
  deliverable, only for substantial reusable data and only after the licence and source-rights decisions (OWN-04,
  REL-02); design its entry only if one is actually offered — no files for appearance.

### Print and portable evidence

Evidence gets printed, screenshotted, pasted into briefs and forwarded. Design for that, in proportion:

- **Print styles** for every page family and, with most care, for Readings, Evidence Records and Methodology (tables
  included, with repeated headers and sensible page breaks): navigation chrome
  hidden; title, edition line ("Edition of …"), canonical URL and language kept; every figure printed with its period,
  population, unit and boundary; "What not to conclude" kept on the same page as the claim it bounds; charts never split
  from their caption and fallback; source list and citation at the end; link targets printed where a reader needs them;
  Arabic prints right to left with its own type rhythm; nothing depends on colour.
- **Contextual exports** of charts and tables (image or the governed data table) always carry the detached frame: title,
  period and population, unit, credit line, prohibited inference, markers, canonical link and edition. Design the export
  control and its frame; like every CauseWay-content download, it ships disabled until the licence decision (OWN-04).
  The browser's own print and "save as PDF" of a page are not downloads and are always available.
- **A Reading as a document**: design the print and PDF layout of a Reading — title block with edition and evidence
  period, the essay, its signature visual with frame and fallback, "What would change this reading?", "What not to
  conclude", the evidence trace and the citation — in each language separately. A hosted PDF file is a download (gated
  as above); the print stylesheet that produces the same layout is not.
- **Provenance survives detachment**: any fragment that can leave the page — a printed page, an exported chart, a copied
  citation, a social image — carries its source credit, period, population, boundary, canonical link and edition.

**Labels you will need that do not exist yet.** Request each in `design/ESCALATIONS.md` as `NEEDS_CONTROLLED_CONTENT`
(both languages, one `UI-*` ID each) at the gate where the need appears; they are expected, not defects: the "compare
this record" action; the result-type facet's heading and "all types"; any workbench facet's heading and values; the
"type not recorded" source group; the download and export actions and their unavailable, licence and file-format states;
print-only lines (for example a "printed from" line); any reporting-intent choices; a reading-time line, only if you keep
one; the column headings of each chart's fallback table and the dimension headings of the VIS-PROVIDER-OBSERVABILITY
matrix (the contracts name them in English prose only); and the bilingual form of that matrix's dated cells and its
`>9` count, which are English free text today (`ESCALATE_TO_MASTER`).

**Placeholders are for development only.** While a label is pending, render its request key in a visibly marked
placeholder (for example `⟦NCC:compare-this-record⟧`) and never invented wording. Before D7 acceptance every label the
reference site shows is in the Master and regenerated into `interface_copy.json` — the steward adds requested labels in
batches, so ask early — or the optional feature that needs it stays unshipped (hidden in the reference site and listed
as an exception in `design/09_CODE_HANDOFF.md`). The accepted site contains no placeholder and no invented copy.

**Micro-interactions** are designed, not left to defaults: menu opening and closing, focus, hover, tap, copy and cite
confirmations, opening a source, the language switch, filter states, drawers, tooltips (never the only way to reach
information), confirmations, errors, table overflow, and Escape closing what it opened and returning focus. The whole
should feel calm and exact.

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
- The prohibited inference, under "What not to conclude / ما لا يُستنتج" (`UI-READING-DO-NOT-INFER`), is visible, not
  buried.
- Then "Trace the evidence / تتبّع الأدلة" (`UI-READING-TRACE-H`: the bound records and sources) and "Related readings /
  قراءات ذات صلة". The trace offers "Test comparability of this Reading's records"
  (`UI-READING-TEST-COMPARABILITY-OF-THIS-READING`) only when at least two of the Reading's records are in the comparable
  set, and opens Compare with up to four of them.
- Home shows **one** Featured Reading, Explore **one** "Go deeper", a domain page **at most two**; an Evidence Record lists
  the Readings that use it; a Measurement priority says where its gap is examined. No carousels, no ten-card walls.
- A domain page shows the first N of its Page Spec's `governed_measurement_priorities`, in order, where N is its
  `measurement_limit` (inventory `presentation_contract`), each linking to `/measurement/#MA-00x`.

Readings data: `site-src/content/content/readings.json`, `reading_sections.json`; each Reading's Page Spec carries its
bindings.

---

## 12. Visuals

Read `handoff/VISUAL_DESIGN_CONTRACT.md` and `site-src/content/visuals/visual_design_contracts.json` before any chart.
Tier counts are in `tier_counts`; the tier of every visual is in the inventory.

- **SIGNATURE** — design first; full data contracts. **CORE_ANALYTICAL** — standard truthful forms; full data contracts
  (the three POS visuals are one small multiple). **SUPPORTING** — no data contract: render the governed text (title,
  question, alt text, period, population, prohibited inference) and, optionally, a non-quantitative diagram built only
  from those governed words and the `UI-VIS-*` grammar labels — no plotted value, axis or scale. To plot values, ask for
  the visual to be promoted (`ESCALATE_TO_MASTER`). **TABLE_TEXT_FIRST** — never drawn as a chart; render the governed
  ordered text or table. **RETIRE_FROM_DESIGN** — never drawn.
- **IDs and where a visual lives.** An Evidence Record whose ID starts `VIS-` is a verification record (sources,
  period, population, boundary). Where a governed visual has the same ID, that record page is the visual's canonical
  route (`governed.canonical_route`, the link in its detached frame): draw the visual there in full, following its tier,
  and on the routes in `governed.public_routes` as the Page Specs bind it. A `VIS-` record without a visual contract has
  no chart. VIS-CAPITAL-CONTEXT is RETIRE_FROM_DESIGN: never drawn; its record stays a public Evidence Record.
- **TABLE_TEXT_FIRST without rows.** Where a rationale describes a table (for example VIS-MFI-DIVERGENCE) but the
  contract resolves no rows, render the governed text only and request the rows (`ESCALATE_TO_MASTER`); never build the
  table from a reference file.
- **Markers on one value.** WITHHELD takes precedence: the value is not shown, whatever other marker it carries.
- **Several visuals on one domain page.** A domain route's Page Spec binds one to five visuals
  (`allowed_visual_contract_ids`); the presentation contract places at most one in the first screen. Draw every other
  bound visual in the page's depth, beside the section that discusses it, in its tier's form (TABLE_TEXT_FIRST as text,
  SUPPORTING without plotted values). `/reforms/` places none first: VIS-PAYMENT-RAILS belongs beside the section on the
  payment-infrastructure reform. The DISAGREEMENT note of the POS charts is the method text of their Evidence Records.
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
  visual. Do not invent a chart because numbers are present. The chronology is context, never a causal chain. The 36
  contracts are analytical problems, not chart requests: decide the strongest form for each and record why.
- **Interaction in a visual** may reveal a value's unit, population, calculation base, period, definition, evidence
  state, source, boundary or what remains unproven — only from governed fields. Hover is never the only way in: the
  same information is reachable by focus, keyboard and touch, and readable in the static fallback. Diagrams reflow; a
  complex visual always has its accessible equivalent.

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
  for example «سجل الدليل», «المجتمع الذي ينطبق عليه الرقم», «قاعدة الاحتساب», «حداثة الأدلة», «توقيت القياس»
  (`preferred_public_arabic_terms` in `handoff/IMPLEMENTATION_MANIFEST.json`), «مستمر» for durable use, «التحويلات» for
  remittances as a flow and «الحوالة / الحوالات» for individual transfers (F5 §3), «البنك المركزي اليمني – عدن» at first
  mention. They matter when you request a label; you never author public copy.
- No English-only visual metadata may disappear in Arabic, and no internal-control vocabulary may appear in either.
- **Test in Arabic, not only view it:** native hierarchy, RTL flow, mixed Arabic and Latin, numerals, source names,
  tables, charts and legends, inputs, search, citation, exports and print, mobile, line length, punctuation and the
  language switch — each at the widths of §0, with the longest Arabic strings the corpus holds.
- **Dates** follow the governed form: day, month name, year, Western digits — "26 September 2026", «26 سبتمبر 2026».
  Arabic month names are يناير فبراير مارس أبريل مايو يونيو يوليو أغسطس سبتمبر أكتوبر نوفمبر ديسمبر (as in
  `date_words` in `scripts/yfie/content.py`, `MONTHS`); do not use a locale library's month names, which vary by region.

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
that way: self-hosted fonts from `vendor/fonts/`, loaded efficiently — only the weights you use, the critical faces
preloaded, a deliberate `font-display`, IBM's own pre-split Latin subsets where they help (not vendored yet: request them
in `design/ESCALATIONS.md` and the steward adds them with provenance) — and no self-made subset
unless the owner approves one (`vendor/fonts/README.md`); no decorative images; SVG or CSS for diagrams; charts drawn from local data; no
client framework weight a static page does not need. Specify the logo's rendered sizes so Code can export derivatives.
No "green" claim, badge or comparison anywhere. Accessibility, Arabic quality, security and evidence integrity outrank
marginal byte savings.

Performance is part of usability for a reader on a slow or expensive connection: static-first, progressive
enhancement, the core evidence (answer, scope, boundary, record, source) readable before any script runs, and no
animation library carried for effect. A public note on the site's own footprint is optional; if you propose one, it
follows `docs/SUSTAINABILITY_METHOD.md`, separates measured, modelled, assumed and unknown, carries no carbon figure
before the post-deployment measurement, and its words are requested as governed copy.

---

## 16. Social / Open Graph system

Every page already emits `og:title`, `og:description`, `og:type`, `og:locale` and a `summary` card from its governed title
and description (`scripts/discovery.py`), with no image. Design the **social-image system**: templates that cover all
eleven page families in both languages (families may share a template; at least Home, Domain Answer, Evidence Record,
Reading, Measurement and Reference / Trust need their own), using only governed text (title,
scope/period line, the governed boundary where a figure appears), the logo at a specified size and the canonical link.
A shared image that shows a number must carry its period, population and boundary. Code generates the images at build
time and adds `og:image` only then.

---

## 17. Discovery (keep what F6 established)

One native `<title>` and meta description per page (governed, unique per language); one `<h1>`; self-canonical;
reciprocal `hreflang` for `en`, `ar` and `x-default` (the root); pre-release `robots.txt`; JSON-LD `WebSite`,
`BreadcrumbList` and `Article` (Readings) with governed fields only — no author, dates, image or `Dataset`. Your
templates must keep these head elements and keep the breadcrumb visible where it is today. Contract:
`docs/DEPLOYMENT.md`, "Discovery (F6)"; checks: validator F6-G01…G05.

---

## 18. Security and privacy constraints on the design

The design must work under a strict Content-Security-Policy: no inline executable script (data goes in JSON blocks), no
inline style attributes, no inline event handlers, no external script, stylesheet, font, image or frame, no form. No
analytics, tracking, cookies or accounts; one functional preference (`yfie-lang`). Links to original sources open with
`rel="noopener noreferrer"`. Render data only through escaping. Contract: `docs/DEPLOYMENT.md`, "Security and privacy
expectations for Code"; checks: F6-G05.

---

## 19. Deliverables — repository-backed, no screenshot-only handoff

Work inside this repository. Create `design/` (leave `design/architecture/`: programme diagrams — three generated by
`scripts/architecture_diagrams.py`, and the Design-to-Code flow, hand-maintained to match §20):

| File | Content |
|---|---|
| `design/00_DESIGN_README.md` | What the package is; how to build and preview the reference site; whether an approved visual board or mockup was supplied (D0); the dependency map; the **decision log** — one dated entry per material decision (not for cosmetic tweaks), with: ID and gate; the problem; the evidence and context (routes, contracts, states); the alternatives considered; the direction chosen and why; its Arabic, responsive and accessibility implications; what Code must implement; any known compromise and its design-debt or open-item ID |
| `design/COVERAGE.csv` | The **coverage ledger**, seeded at D0 from the inventory and updated at every gate: one row per route × language × width (320, 390, 640, 1440) and per hard, verification and technical state — columns `route, page_family, language, width, state, gate, status, checks, code_handoff, evidence, note`. `status` climbs `NOT_STARTED` → `REVIEWED` (this route's content, contracts and states read — a family template applied is not a review) → `DESIGNED` (the system applied to this route) → `BUILT` (rendered in the reference site) → `VERIFIED` (every applicable check passed, with evidence) → `ACCEPTED` (at D7). `checks` lists the checks passed, from `rtl`, `responsive`, `interaction`, `hard_state`, `a11y`, `print`, `content` (governed content complete, no placeholder); `code_handoff` is `YES` when `design/09_CODE_HANDOFF.md` covers the row's family, components and states |
| `design/DESIGN_DEBT.md` | The **design-debt register**: every deliberate temporary compromise, so none disappears silently — ID; the temporary decision; why; the surfaces affected; the user impact; the intended behaviour; the Code action; priority; and whether it blocks D7 acceptance, blocks public release, or neither. Entries are closed, never deleted |
| `design/01_FOUNDATIONS.md` | The D1 design theses (what each proposed, screenshots of the stress trio in both languages, how each did against the acceptance criteria, why one was chosen); then principles, evidence-state grammar, type, grid, space, colour, iconography, motion — with rationale |
| `design/02_TOKENS.json` | Machine-readable tokens (colour, type scale per language, space, radius, elevation, motion, breakpoints, z-index) |
| `design/03_COMPONENT_CATALOG.md` | Every component: anatomy, inputs (governed fields), states, RTL/LTR, responsive, accessibility |
| `design/04_PAGE_FAMILY_COMPOSITIONS.md` | Deterministic module order and composition rules for all 11 families, first-screen contract per family |
| `design/05_RESPONSIVE_RTL_LTR.md` | Breakpoints, reflow, Arabic composition rules, bidi isolation |
| `design/06_VISUAL_TABLE_SYSTEM.md` | Every visual family and table pattern against its contract; detached frame; fallbacks; print and export forms |
| `design/07_INTERACTION_ACCESSIBILITY.md` | Every tool's states and keyboard paths; focus management; announcements; WCAG outcome mapping |
| `design/08_ASSET_MAP.md` | Logo placements and sizes, fonts and subsets, icons, social-image templates |
| `design/09_CODE_HANDOFF.md` | The Design-to-Code mapping required by `handoff/DESIGN_TO_CODE_CONTRACT.md` |
| `design/10_ACCEPTANCE_CHECKLIST.md` | `handoff/DESIGN_ACCEPTANCE_CRITERIA.md` filled in with evidence (screenshots, test output, notes) |
| `design/ESCALATIONS.md` | Every `ESCALATE_TO_MASTER` and `NEEDS_CONTROLLED_CONTENT` item |
| `design/reference/` | **The runnable reference implementation** (below) |

**Four layers — keep them apart.** (A) The governed content: the Master and its projections in `site-src/content/**`,
never altered by design. (B) The current reference build: `dist/`, made by `scripts/build.py`, previewed with
`python3 -m http.server 4173 --directory dist` — a behavioural baseline you may challenge visually, never semantically.
(C) Your accepted design implementation: `design/reference/`, built to `design/reference/out/` — the design exists when it
is there, not when it exists in a canvas or a screenshot. (D) Claude Code's production runtime, which hardens (C) after
acceptance and replaces (B).

**The reference implementation** renders **every route in both languages** (the same 288 documents as `dist/`) from
`site-src/content/**` — never from a copied or hand-written content model — with every tool working on local data, at
every width, with every state reachable.

- **Where.** Its source lives in `design/reference/` with one documented build command that writes the site to
  `design/reference/out/` (git-ignored). It does not write to `dist/` and does not change `scripts/build.py`,
  `site-src/app.js` or the pre-design baseline stylesheet: those stay the baseline, and every repository gate keeps running on `dist/`
  unchanged (gate P3-G02 — "the baseline draws no chart" — applies to `dist/` only; your charts live in your output).
  Replacing the baseline renderer is Code's job after acceptance. Any stack is fine (a static generator, a React static
  pre-render); choose what gives Code the best implementation-grade source.
- **How it is tested.** The browser suites and the invariance check take the site directory from `YFIE_SITE_DIR`:
  `YFIE_SITE_DIR=design/reference/out python3 scripts/tests/test_public_tools.py`, the same for
  `audit/tranche_c/checks/viewport_acceptance.py` and `audit/tranche_c/checks/bilingual_invariance.py` (0 differing page
  pairs). Keep the hooks they use — they are the test contract Code inherits: the IDs `main`, `global-search`,
  `search-dialog`, `search-results`, `utility-status`, `compare-a`…`compare-d`, `source-<SOURCE-ID>`; the attributes
  `data-search-open`, `data-search-empty`, `data-menu`, `data-lang`, `data-cite`, `data-source-filter`,
  `data-source-filter-status`, `data-source-no-results`, `data-source-record`, `data-source-cite`,
  `data-source-link-error`, `data-compare-url-error`, `data-compare-verdict`, `data-correction-record`,
  `data-correction-origin`, `data-correction-link`, `data-correction-mail`, `data-correction-error`; the classes
  `search-hit`, `compare-table`, `compare-state`, `evidence-cite-button`, `source-locator`; the JSON blocks `yfie-ui`,
  `yfie-compare`, `yfie-compare-dimensions`, `yfie-record-ids`, and the meta tag `yfie-citation`; the skip link as the
  first focusable element with class exactly `skip`; a native `<dialog id="search-dialog">` with its input
  `global-search-dialog`; `<select>` elements for the Compare slots; the search index at `/static-data/search_index.json`;
  one `<h1>`, `alt` on every image and `dir` on every page; the class `empty` for the search failure state; status regions
  with `role="status"` and `aria-live`, link and input errors with `role="alert"`. The two test files are the authority:
  read them before D1.
  The suites are not edited by Design: keep every hook. CI does not build your reference implementation, so paste each
  suite's output into `design/10_ACCEPTANCE_CHECKLIST.md`.
- **Evidence files.** Commit evidence as PNG screenshots and text. Never commit a PDF, XLSX, DOCX or ZIP (gate F6-G07
  fails on any but the Master): keep print-to-PDF checks in the ignored `design/reference/out/` or outside the
  repository, and commit a PNG of each printed page instead.
- **What else it keeps.** The discovery head (§17), the JSON data blocks, the strict-CSP constraints (§18), and a print
  stylesheet (§10).
- **A hostable static site.** `design/reference/out/` is reproducible from one command and self-contained: the English
  and Arabic HTML of every route, the root entry and the bilingual 404; CSS; JavaScript only where a tool needs it;
  the approved assets (the canonical logo) and the fonts with their licence; the search index and the page data blocks;
  the discovery head; working language switching and internal navigation; the no-JavaScript fallbacks. Anyone can open
  it with `python3 -m http.server 4173 --directory design/reference/out` — no design tool, account or proprietary
  workspace is needed to see the product. Hostable is not released: public release stays a separate acceptance.
- **Completion.** D7 acceptance requires this runnable, fully populated bilingual reference site: all 288 documents,
  every tool, every state, both languages, every width, no placeholder. A homepage, representative screens,
  screenshots, a moodboard, a design-tool prototype, a component catalogue or a partial system is not completion. A
  design source without the site — however implementation-grade — is an incomplete hand-back: say so plainly in
  `design/00_DESIGN_README.md`; it is not accepted as complete.

Maintain `design/09_CODE_HANDOFF.md` **as you work**, not at the end: tokens, components, states, routes, content
bindings, visual contracts, responsive rules, accessibility behaviour and every exception.

---

## 20. Work plan — gates, one pull request each

Do not jump into visual production. Each gate enters only when the one before it has exited, and each leaves a runnable,
committed state.

| Gate | Enters when | Work and durable output | Exits when (evidence in the pull request) |
|---|---|---|---|
| D0 Orientation | The first line of `handoff/README_FIRST.md` reads DESIGN HANDOFF READY and the §8 commands of that file pass on your clone | Read-in (§3); dependency map from the inventory; the statement on supplied boards or mockups; `design/COVERAGE.csv` seeded with every row `NOT_STARTED`; the decision log, `design/DESIGN_DEBT.md`, `design/ESCALATIONS.md` and `design/09_CODE_HANDOFF.md` opened; a plan for D1–D7. No polished screens yet | The records exist and are committed; the plan names the D1 theses to be tested; escalations so far are listed |
| D1 Theses and grammar | D0 exited | Two or three materially different design theses, each rendered on the stress trio — Home, `/evidence/CLM-003/`, `/readings/same-year-different-number/` — in English and Arabic at 390 and 1440 px with real content, judged against the acceptance criteria and the four review tests (§7); one chosen with recorded reasons (`design/01_FOUNDATIONS.md`); then foundations, tokens, evidence-state grammar, shell and type in both languages, proved on the trio | The chosen system holds on the trio at all four widths in both languages, by keyboard, with the hard states the trio carries; decision-log entries for the choice. Nothing is propagated to other routes before this gate exits |
| D2 Hardest families | D1 exited | Explore, `/people/`, `/access/`, `/payments/`, `/remittances/`, `/reforms/`, the Evidence index and the record set of §9.1, Compare, `/data/` | Each hard-state case of §9.2 on these routes proved with evidence; ledger rows `VERIFIED` or their gaps explained |
| D3 Synthesis and reference | D2 exited | Readings index and every Reading, Measurement, Methodology, About and trust, corrections and report journey, 404 (§9.4) | The same, for these families; the Home cold-reader test (§9.4) run and recorded |
| D4 Complete binding | D3 exited | Every route in both languages through family rules; no bespoke drift | All 288 documents render from `design/reference/out/`; `test_public_tools.py`, `viewport_acceptance.py` and `bilingual_invariance.py` pass against it (§19); every ledger row at least `BUILT` |
| D5 Interaction and accessibility | D4 exited | Search, workbench, Compare, sources, Cite, language, report, download and export patterns; micro-interactions (§10); keyboard, focus, zoom, reduced motion, forced colours, image-off, mobile | Every tool state and journey (§9.3) proved in both languages by keyboard; `design/07_INTERACTION_ACCESSIBILITY.md` complete |
| D6 Visuals, social and print | D5 exited | Signature and core visuals, table-first renderings, detached frames, social-image templates, print styles, Reading print/PDF layout, contextual export frames | Every visual against its contract with fallback and frame; print previews of every family in both languages; the screenshot-misuse and portable-evidence tests recorded |
| D7 Acceptance and Code handoff | D6 exited | The runnable, fully populated bilingual reference site (§19); every label governed or its feature unshipped; the **last-10-percent audit** — search and zero results, Contact, Corrections and evidence challenge, source and external links, citation, the language switch, mobile tables, long Arabic strings, focus, inputs, privacy, rights, unavailable downloads, print, reduced motion, 404, the footer, every trust surface and every hard state; `design/10_ACCEPTANCE_CHECKLIST.md` complete; `design/09_CODE_HANDOFF.md` final | Every acceptance line has evidence; the coverage ledger `ACCEPTED` for every row or each gap explained; no open design debt blocks D7; all gates green; the Code recipient test (§0) passes |

**Every gate, start and end.** Start by re-reading the records listed in §0 ("The repository is your memory"). Before the
pull request: add the gate's decision-log entries; update the coverage ledger for every route and state touched, the
design-debt register, the escalations and `design/09_CODE_HANDOFF.md`; record what became more understandable or
truthful, what complexity was added and what could be removed; run the repository gates (`CONTRIBUTING.md` §5, on
every pull request) and the gate's own tests (the reference-site suites from D4 on; before D4, screenshots and targeted
checks of the routes built); apply the Code recipient test; commit, push and leave the tree clean.

**Stop conditions.** Do not move on — record the reason in the decision log and fix it, or escalate it — when: a gate's
exit evidence is missing; a repository gate fails; a hard state on the gate's routes does not hold; the stress trio
stops holding after a change; a shipped feature needs a label that is not yet governed (design it, keep it unshipped,
list it); a truth defect blocks a surface (`ESCALATE_TO_MASTER`, then design the honest current state); or the Code
recipient test fails.

---

## 21. Git protocol

Canonical repository: GitHub `CausewayGrp/Financial-inclusion-`, branch `main`. Branch `design/<gate>-<slug>`; one pull
request per gate; merge only when **Verify** is green. Never force-push; never rewrite `main` or a `checkpoint/*` tag;
never edit `authority/`, `site-src/content/`, `dist/`, `audit/` or `audit/PUBLIC_LITERAL_CLOSURE.json` (outputs the
scripts regenerate are not edits). Commit with Conventional Commits; regenerate `FINAL_REPOSITORY_MANIFEST.json` and
`SHA256SUMS.txt` before each commit (`design/**` is already classified).

Without push access to the canonical repository, work in a local clone (or, from the handoff archive, run
`git init -q && git add -A && git commit -qm "import handoff"` first) and deliver each gate as a git bundle
(`git bundle create design-<gate>.bundle <base>..HEAD`) or a patch series (`git format-patch <base>`); the steward lands
it on a `design/` branch through the same gates.

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
20. produce the runnable, fully populated bilingual reference site that Code can execute without guessing (§19); an
    implementation-grade design source without it is an incomplete hand-back and does not satisfy this item;
21. build and maintain a Design-to-Code contract as you work (§19, `handoff/DESIGN_TO_CODE_CONTRACT.md`);
22. finish with a Code handoff that maps tokens, components, states, routes, content bindings, visual contracts,
    responsive rules, accessibility behaviour and exceptions (§19).

Also required, beyond the twenty-two: competing theses tested at D1 before propagation (§20); the kernel, the loop and
the gate-start re-read (§0); the decision log, the coverage ledger and the design-debt register kept at every gate
(§19); print and portable evidence (§10); the audience lenses and the family outcomes (§9.3, §9.4); the four review tests
(§7); the last-10-percent audit at D7 (§20).

---

## 23. Never

- Invent, round, normalise, convert or "tidy" a number, date, label, author, title, licence or source.
- Print the withheld CLM-044 value, name a source without a public locator, or republish a third-party document.
- Merge the two parts of a boundary ("does not establish" · "limits of the measure") or print the internal delimiter.
- Show an internal ID, enum, field name or repository term as prose (stable IDs as citation references are fine).
- Turn missing into zero, a listing into operation, a target into a result, a sequence into a cause.
- Add analytics, tracking, a font CDN, an external script or a form.
- Ship a placeholder or an invented label in the accepted site, or enable a download of CauseWay content before the
  owner's licence decision.
- Treat a board, mockup or palette that is not in the repository as binding.
- Use an image whose provenance and rights are not established, or recolour or invert the logo for any theme.
- Animate for effect: count-up numbers, decorative parallax, motion that explains nothing.
- Let a decision live only in a canvas, a screenshot or a conversation.
- Claim WCAG conformance, legal review, rights clearance, native-language certification, security guarantees or public
  release readiness.

When the checklist in `handoff/DESIGN_ACCEPTANCE_CRITERIA.md` is complete with evidence and every gate is green, the
Design package is ready for acceptance and for Claude Code (`handoff/CLAUDE_CODE_MASTER_PROMPT.md`).
