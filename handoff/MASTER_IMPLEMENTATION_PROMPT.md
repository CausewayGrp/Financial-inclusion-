> STATUS: **DRAFT — DO NOT EXECUTE YET.** Final independent acceptance and clean-room handoff are still in progress. This file will be promoted only after the finalization programme closes.

# FINAL MASTER IMPLEMENTATION PROMPT — CLAUDE DESIGN → CLAUDE CODE

## Read this as an execution brief, not a review programme

You are receiving the complete production repository for **Yemen Financial Inclusion Evidence / أدلة الشمول المالي في اليمن**.

The controlled evidence structure and linking model, public content, route set and bilingual product model are mature enough for final design and implementation. **Do not spend this assignment reopening prior review sessions, reconstructing project history, writing another assessment, or proposing more controls.** Work on the product itself.

Your job is sequential and finite:

1. **Claude Design:** turn the actual governed product into an exceptional, complete, repository-backed design system and page-family composition package.
2. **Claude Code:** after the design package is complete, implement it as the single final React static-pre-render/export runtime.

The success condition is not “a good concept”. It is a repository from which an unfamiliar senior designer and engineer can build the complete public product without chat history, guessing, or redesigning the evidence model.

---

# A. What you are designing

This is not a dashboard and not a brochure. Yemen Financial Inclusion Evidence is a bilingual public evidence resource that helps users understand, compare and verify evidence on financial inclusion in Yemen. It supports decision-making by making evidence scope, limits and sources explicit. It does not make decisions for users or simulate policy outcomes.

It must let a user move cleanly through this chain:

**decision question → strongest defensible answer → evidence scope and timing → what the evidence does not establish → analytical interpretation → unknowns / measurement need → evidence record → original source / citation / reuse boundary.**

The same evidence base must work at different depths for public institutions and regulators, financial institutions, development partners, researchers, journalists, programme practitioners and informed public users. Do not create different facts for different audiences; create different depths of entry into the same evidence system.

### Current production scale

Counts are derived from the Master (`site-src/content/content/public_inventory.json`); re-read them, because they change when the Master changes.

- 143 controlled Page Specs.
- 110 Evidence Record detail routes, of which 60 are controlled public claims.
- 10 Evidence Readings.
- 10 Measurement priorities.
- 36 governed visual contracts, tiered for design in `site-src/content/visuals/visual_design_contracts.json` (see `handoff/VISUAL_DESIGN_CONTRACT.md`).
- 161 source records, of which 152 expose a public original locator.
- 28 curated report/reference cards.
- 24 documented macro-financial / financial-inclusion-system chronology events.
- 436 controlled public-search records.
- 286 localized Arabic/English route documents + root + 404 = 288 baseline static HTML outputs.

These are **complete design inputs**, not a backlog to re-invent.

---

# B. The only truth boundary you need to preserve

The semantic/evidence source of truth is:

`authority/Yemen_Financial_Inclusion_Evidence_Master.xlsx`

Current handoff identity:

`440614d789f662e2e47d95e932968be3c71d2719187bb91c6f546aed30e72f71`

The controlled implementation projection is:

`site-src/content/page_specs.json`

Current handoff identity:

`0425dc85c1662120a2b00a5bb3485b93d4f64f6058d7e2a0ebeb477dedc3e871`

Presentation depth/order is supplied by:

`site-src/content/presentation_priority.json`

Do not rewrite a number, denominator, unit, universe, geography, period, method, evidence state, source state, rights state, limitation, prohibited inference or publication state. If you encounter a true semantic contradiction, flag the exact object as `ESCALATE_TO_MASTER`. If an implementation-required substantive field is genuinely absent, use `NEEDS_CONTROLLED_CONTENT`.

Those are exception paths. **They are not an invitation to stop the design or to produce another review report.** Continue with every other route and component that is fully controlled.

Never collapse these distinctions visually or verbally:

**people ≠ accounts · access ≠ use · infrastructure ≠ outcome · target ≠ result · programme KPI ≠ national prevalence · licence/listing ≠ operation · observed ≠ estimated ≠ projected · missing ≠ zero · chronology ≠ causality · public citation ≠ redistribution permission.**

---

# C. Start with the actual product, not the control history

For Claude Design, read in this order:

1. `handoff/MASTER_IMPLEMENTATION_PROMPT.md` — this file.
2. `site-src/content/page_specs.json` — actual controlled page content and route contracts.
3. `site-src/content/presentation_priority.json` — what belongs first, supporting, progressive and linked.
4. `site-src/content/content/navigation_interaction.json` — navigation and interaction expectations.
5. `site-src/content/visuals/visual_library.json` — governed analytical visual contracts.
6. `site-src/content/content/readings.json` and `reading_sections.json` — editorial/analytical products.
7. `site-src/content/content/measurement_agenda.json` — measurement product.
8. `site-src/content/sources/source_reference_map.json` and `public_object_source_closure.json` — source/citation behavior.
9. `site-src/styles.css`, `site-src/app.js`, `scripts/build.py`, and representative generated pages — **behavioral baseline only, not final visual authority**.
10. `handoff/DESIGN_STARTING_TOKENS.json` — starting brand/design language.

Do **not** spend the design phase reading historical closure reports, archive inventories, old prompts or review ledgers unless an actual controlled object is contradictory and requires lineage to resolve. The product files above are the working material.

---

# D. The present website is a functional evidence baseline — not a visual ceiling

The existing implementation already proves route coverage, evidence binding, search, source navigation, Compare logic, Arabic/English parity, keyboard structure, mobile reflow and visual fallbacks. Preserve those capabilities.

But do not simply “skin” the current output. Treat these current weaknesses as design work to solve:

- the visual system still reads too much like a capable prototype rather than a definitive public institution-grade product;
- repeated alternating section bands can make long routes feel mechanically stacked;
- card repetition can flatten the hierarchy between answer, evidence, boundary, source and next measurement;
- the English typography in the baseline (Arial/Newsreader mixing) is not the intended final system, whose default is IBM Plex;
- the Data/source surface is functionally complete but can become visually overwhelming if hundreds of links are presented with equal weight;
- long Evidence Records need stronger orientation and traceability without becoming a technical form;
- Readings should feel like evidence-led editorial analysis, not another card template;
- sparse routes such as Access must look intentionally sparse, not unfinished;
- dense routes such as People, Finance and Remittances must be compressible without hiding material scope or limitations;
- visuals should feel analytical and bespoke, not decorative chart inserts;
- Home and Explore must feel deliberately different: Home orients and starts tasks; Explore is the complete question map.

The current CSS and generated HTML are therefore **regression references for behavior and semantics, not instructions to preserve layout, typography or card treatment**.

---

# E. Visual direction

Create a design CauseWay can credibly present to central-bank leadership, senior development partners, researchers and the public without the product feeling bureaucratic or generic.

The character should be:

**calm · exact · editorial · analytical · premium · contemporary · bilingual by construction · low-bandwidth aware · evidence-first.**

Avoid:

- NGO-portal aesthetics;
- SaaS dashboard tropes;
- generic consultancy landing pages;
- news-portal density;
- oversized decorative KPI tiles without scope;
- ubiquitous rounded cards;
- excessive gradients, glass effects or animation;
- “data theatre” that makes the product look more certain than the evidence.

### Brand and design expression

Use the supplied CauseWay identity asset:

`site-src/assets/CauseWay_Master_Logo.png`

Do not redraw it, approximate it or replace it.

The CauseWay-aligned ink/teal/gold/mint/sand palette is a **proven starting reference, not a design prison**. Claude Design owns the final palette, grid, spatial rhythm, component anatomy, interaction and motion system, provided that the result is materially stronger, coherent with CauseWay, locally packageable, accessible and equally successful in Arabic and English. Typography: IBM Plex Sans (English) and IBM Plex Sans Arabic (Arabic) are the default final type system. A departure is allowed only with a written rationale in the design package showing a system that is materially stronger, locally packageable, accessible and equally successful in Arabic and English; a second display face needs the same rationale. Do not introduce a font simply for novelty.

Stable IDs, Latin source codes and URLs must remain bidi-safe. Do not inherit accidental Arial/Newsreader mixing. Do not introduce a second display face or a novel palette simply for novelty; every departure from the baseline should earn its place in the complete system.

The product should rely on typography, spatial hierarchy, line, annotation and structure before colour. Meaning must survive grayscale and forced colours.

### Composition

Use a disciplined grid, strong reading measure, generous whitespace and asymmetric editorial composition where useful. Let evidence objects have different visual weights. Not every module needs a border or container. Use cards only where a card is semantically useful.

Create a recognizable visual grammar for:

- strongest answer;
- evidence clock / period / universe;
- boundary / “does not establish”;
- source verification;
- evidence state;
- unresolved or conflicting evidence;
- measurement-next;
- analytical Reading;
- methodological note.

A user should learn the grammar once and then recognize it across the site.

---

# F. Page-family compositions — design all of them as systems

## 1. Home — orientation, not catalogue

The Home page should answer three questions immediately:

**What is this? Why is it useful? Where do I start?**

Preserve the current decision-first logic, but create a stronger visual sequence:

- restrained CauseWay identity / global utilities;
- one decisive bilingual hero proposition;
- a small set of evidence signals that explicitly show that different measures live on different clocks;
- task-first starting points;
- a compact “system view” showing the relationship between people, firms, providers, payment rails, flows, rules and infrastructure without implying causality;
- a small set of direct questions;
- a trust/verification invitation;
- selected Readings as depth, not a news feed.

Do not put the full Explore catalogue on Home.

## 2. Explore — the complete question map

Explore is a decision navigator. Group the 11 controlled questions by user job or evidence need. A user should be able to scan the whole system without opening every domain.

Use meaningful grouping, progressive detail and clear destination cues. The page should feel like an analytical map, not a grid of identical cards.

## 3. Domain Answer pages

The eight domain routes are not generic topic pages. Each is a structured answer to a decision question.

Every domain composition must make the following order legible:

**answer → scope/clock → strongest evidence → analytical visual if useful → material boundary → supporting evidence → unknown → measurement-next → verify.**

Use `presentation_priority.json` to distinguish dense and sparse routes. Never force a sparse domain to look artificially full.

Design exemplars in both languages at 390 and 1440 before applying the system broadly:

- `/people/` — dense representative population evidence and subgroup gaps;
- `/access/` — sparse geography/observability case;
- `/firms/` — survey denominator discipline;
- `/finance/` — multiple finance objects that must not collapse;
- `/payments/` — infrastructure/transactions without adoption inference;
- `/remittances/` — source concepts, vintages, observed/estimate/projection;
- `/providers/` — formal status without operation inference;
- `/reforms/` — rule/implementation/outcome chain.

## 4. Evidence Record family — trust infrastructure

There are 110 Evidence Record routes. This family must be exceptionally strong because it is where a skeptical user verifies a claim.

First viewport should establish:

- what the record says;
- evidence state/type;
- exact population/universe/base;
- period/currentness;
- geography;
- the most material limitation;
- a clear verification/source path.

Then progressively reveal method, derivation, source closure, related interpretation and correction context.

Design at least these hard cases:

- `/evidence/CLM-001/` — representative population measure;
- `/evidence/CLM-032/` — same reference year, different published value;
- `/evidence/MFI-SPINE-2015-Q4/` — within-source contradiction;
- `/evidence/VIS-REMITTANCE-MACRO/` — observed history versus outlook.

Do not make Evidence Records look like database forms.

## 5. Evidence index + Compare

Evidence discovery should support scanning, filtering and verification without exposing internal-only material.

Compare must remain **compatibility-first**. The design should make the verdict on whether records can legitimately be compared more prominent than the numeric values themselves. It must work for two to four records and remain understandable without colour.

Do not invent normalized scores or forced reconciliation.

## 6. Data / source directory

This surface contains a large amount of source and chronology material. It must not render as a 700-link wall.

Design a scalable information-retrieval surface using the controlled data only:

- search and filter first;
- compact, high-information result rows rather than large cards;
- controlled grouping or disclosure for source locators;
- visible source ID / publisher or locator only when controlled;
- dependent Evidence Records reachable from source entries;
- rights/citation boundary in context;
- chronology as a distinct analytical sequence, not mixed into source search.

No virtualization or interaction pattern may make the content inaccessible without JavaScript; the static document must remain meaningful.

## 7. Readings

The 10 Readings are evidence-led analytical essays. Give them a distinct editorial identity while keeping the evidence chain visible.

A Reading should support:

- a strong title/deck;
- a compact “what this reading argues” summary;
- well-paced body sections;
- inline analytical visuals or evidence callouts where governed;
- visible limits/unknowns;
- linked Evidence Records and sources;
- a clean ending that returns to decision or measurement implications.

Design exemplar:

`/readings/gender-gap-measured-causes-open/`

Do not style Readings as blog posts or news articles.

## 8. Measurement Agenda

This should make evidence gaps actionable. A priority should show:

**decision affected → what is unknown → minimum evidence needed → plausible holder/source → what would change if measured.**

Use visual ranking only when the controlled data supports it. Do not turn the agenda into a synthetic scorecard.

## 9. Methodology / About / operational trust pages

These routes should be calm, readable and intentionally sparse. They are trust infrastructure, not marketing filler.

Accessibility, privacy, rights, corrections, contact and terms pages should share a concise operational family while retaining clear status/action cues.

---

# G. Interaction model

Specify and design, do not leave for Code to invent:

- desktop and mobile navigation;
- language switching that preserves route context;
- search dialog and results states;
- keyboard focus entry/return;
- disclosures and “more detail” behavior;
- source/citation copy feedback;
- Compare selection, verdict and table navigation;
- source-directory filtering and focused source deep links;
- long table scrolling;
- empty/error/loading states where relevant;
- correction/report paths;
- reduced-motion behavior;
- image-off behavior;
- forced-colour/grayscale behavior.

No important meaning may depend on hover, colour, animation or an image being visible.

---

# H. Responsive and bilingual design

Design explicitly for **320, 390/400, 640 and 1440 CSS px**.

Arabic is not a mirrored English layout. For every major component and page family, specify:

- RTL anatomy and alignment;
- reading order;
- keyboard order;
- mixed Arabic/Latin metadata behavior;
- line length and heading wrapping;
- numeric alignment and bidi isolation;
- icon direction only where the icon is directional;
- mobile order when it differs from desktop.

The Arabic edition must feel natively composed and equally premium.

---

# I. Visuals and tables

The repository contains governed analytical visual contracts. Do not treat them as chart requests.

For each public visual, choose the form that best answers the analytical question: chart, annotated comparison, flow, timeline, structured table, small multiple, or textual analytical object.

Every visual must carry:

- analytical question/title;
- evidence scope and clock where material;
- governed analytical summary;
- prohibited inference / boundary;
- image-independent text/table fallback;
- non-colour semantics;
- accessible reading order;
- mobile strategy.

Do not create decorative maps or causality arrows where the evidence does not support them.

---

# J. Performance is part of the design

Assume constrained connections and older devices.

Design for:

- static-first rendering;
- minimal critical CSS/JS;
- local assets;
- no required runtime Drive/database/CMS/API;
- no required font/CDN request in the final implementation;
- no animation framework for effects that CSS can do;
- images only where they add analytical or brand value;
- no heavy charting library unless the final visual set genuinely requires it.

Claude Code must self-host/package the approved final fonts.

---

# K. Required Claude Design repository output

Create exactly one `design/` directory in the current repository. It is the complete implementation specification, not a moodboard.

Required files:

1. `design/00_DESIGN_README.md` — how to use the design package and any Figma linkage.
2. `design/01_FOUNDATIONS.md` — design principles, grid, typography, spacing, colour, line, iconography, elevation and editorial rules.
3. `design/02_TOKENS.json` — final code-consumable tokens.
4. `design/03_COMPONENT_CATALOG.md` — anatomy, variants, states, controlled inputs and accessibility.
5. `design/04_PAGE_FAMILY_COMPOSITIONS.md` — deterministic composition for every page family and exemplar route.
6. `design/05_RESPONSIVE_RTL_LTR.md` — breakpoints, reflow and directional behavior.
7. `design/06_VISUAL_TABLE_SYSTEM.md` — visual grammar, table grammar, analytical annotation and fallbacks.
8. `design/07_INTERACTION_ACCESSIBILITY.md` — keyboard/focus/search/menu/disclosure/Compare/error/empty/reduced-motion/forced-colour behavior.
9. `design/08_ASSET_MAP.md` — exact use of CauseWay identity and any additional permitted assets.
10. `design/09_CODE_HANDOFF.md` — component-to-content-field mapping, implementation order and no-guess instructions for Claude Code.
11. `design/10_ACCEPTANCE_CHECKLIST.md` — practical design-completeness checks.

If Figma is used, Figma is a visual artifact, not the only specification. Every consequential decision must exist in these repository files.

### Design completion rule

Do not stop at a homepage concept. The design phase is complete only when the system is reusable across all Page Specs and the difficult route exemplars above have been designed in Arabic and English across required widths.

Do not return a list of recommendations as the final design output. **Write the design package.**

---

# L. Claude Code — only after the design package is complete

After the complete `design/` package exists, Claude Code reads:

- `design/09_CODE_HANDOFF.md`;
- `handoff/CLAUDE_CODE_MASTER_PROMPT.md`;
- the controlled page/content payloads;
- the final tokens/components/interactions from `design/`.

Implement one final React static-prerender/export application. Do not preserve the Python renderer as a second production runtime once parity is proven.

The final implementation must preserve:

- all controlled routes in both languages;
- deep-link static output;
- local bilingual search;
- Evidence Record and source journeys;
- compatibility-first Compare;
- publication filtering;
- visible evidence boundaries;
- image-independent visual meaning;
- keyboard and focus behavior;
- static-first low-bandwidth operation.

No `.xlsx` may enter the public build. The browser must not parse the Production Master.

---

# M. Final quality bar

The finished product should make a first-time user think **“I understand what this evidence says, what it does not say, and where it came from”** before they notice the system's complexity.

A specialist should be able to challenge the evidence without fighting the interface.

A senior designer should see a coherent visual language rather than a template.

A senior engineer should be able to implement it without interpreting screenshots or asking what the designer meant.

An Arabic user should receive a product composed for Arabic, not an English product flipped horizontally.

CauseWay should be able to present the result as a serious public evidence institution, not as a prototype or an AI-generated website.

**Start with the actual product. Build the complete design system. Do not reopen old review work. Do not invent truth. Do not stop at recommendations.**
