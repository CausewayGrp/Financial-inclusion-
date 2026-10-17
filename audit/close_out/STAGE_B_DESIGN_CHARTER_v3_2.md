# Stage B Design Charter v3.2 — operative under OD-1017-01 (17 October 2026)

Committed verbatim from Appendix 1 of the owner's takeover brief of 17 October 2026 (`audit/close_out/TAKEOVER_BRIEF_2026-10-17.md`, PR-C). The seven amendments of 17 October 2026 below prevail over the charter text that follows them. The charter was written on 10–11 October 2026 and not committed until now (finding F-02).

---

Read it with these amendments of 17 October 2026, which prevail:
1. **G1 →** BRIEF W4 order (G1 after S and T).
2. **Hosting is neutral** (Part 6, item 3).
3. **The visual-contract count is 42.**
4. **The 15 October prospective charter's constraints remain** (SB-02, CWR-013 reserved, two-Reading rule, CWR-011
   placement).
5. **"AMENDMENTS_D16_D22.md" in §0 means that file as amended by PR #52**, plus `audit/OWNER_DECISIONS_2026-10-17.md`.
   D19–D22 confer nothing.
6. **"brief W4 G0" in §13** means BRIEF W4 G0, re-run on the final build.
7. **The charter's own line "Commit it as audit/close_out/STAGE_B_DESIGN_CHARTER.md" is superseded.** Its path is
   `audit/close_out/STAGE_B_DESIGN_CHARTER_v3_2.md`, and the 15 October file stays where it is with an appended
   pointer.

```text
STAGE B DESIGN CHARTER — v3.2 — Yemen Financial Inclusion Evidence / أدلة الشمول المالي في اليمن

For Claude Code, Stage B (W4).
- Commit it as audit/close_out/STAGE_B_DESIGN_CHARTER.md.
- v3.2 makes seven amendments to v3.1, marked [v3.2] in place and listed in §15.
- v3.1 superseded v3 and v1. It changes v3 in four places: G1 follows D7 with no owner stop (§10.5); the
  social-card blind spot is spelled out (§12.3); earlier design work enters as challenger evidence (§10.1); and the
  ambition and challenge clause is added (§1).
- v3 superseded v1. It keeps v1's ambition and adopts the structure of the OpenAI review (v2). It corrects four points
  in that review against the repository bytes; §15 lists every change.
- Read it with BRIEF.md (v5) and AMENDMENTS_D16_D22.md. Where this charter cites a structure rule of the brief, it
  writes "brief S3", "brief S10" and so on.

══════════════════════════════════════════════════════════════════════
0. AUTHORITY: THIS CHARTER DECIDES PRESENTATION ONLY
══════════════════════════════════════════════════════════════════════
1. The Production Master decides facts, claims, copy, evidence states, sources, rights and publication. The
   projections follow it.
2. The controlled contracts are in force as they stand:
   - navigation_interaction.json, presentation_priority.json, the page-family and visual contracts, and the
     accessibility contracts.
   - They change only through a path the brief or an owner decision authorises: a Master transaction (D8 through
     04_NAV_UX; brief S11's domain titles through 02_SITE_MAP), or a D14 steward edit inside D14's scope, with every
     gate run.
3. BRIEF.md, the owner decisions and AMENDMENTS direct the work, through those paths.
4. This charter decides presentation choices inside all of the above. It never changes a value, claim, question,
   route, evidence state, source relationship, rights state, the analytical form of a governed visual, or a publication
   state.
5. Any new visible string (a label, a caption, a colophon line, a state word) goes Master-first, in EN and AR.

══════════════════════════════════════════════════════════════════════
1. AMBITION
══════════════════════════════════════════════════════════════════════
Most evidence portals make the number prominent and the conditions for reading it secondary. YFIE does the reverse
without becoming heavy: the answer is clear because its scope, clock, source and limit are clear.

The rhythm every consequential figure keeps:
- Answer: large, confident, uncluttered.
- Clock: visibly attached.
- Scope: immediately understandable.
- Boundary: quiet but impossible to miss.
- Source: always one step away.
- Unknown: designed with as much care as the known.
- Whitespace: it carries the intellectual hierarchy.

The quality test:
- A source institution recognises its evidence as faithfully represented.
- An independent reader finds the scope and the limit unusually easy to verify.
- CauseWay's position comes from restraint, traceability and editorial quality, never from promotional copy.

The test is the pages, not the paperwork. The aim is measurably better pages and journeys, above all Arabic on a
phone; a larger design dossier is not the aim. The site should have the seriousness of an official statistical
product and the clarity of excellent editorial design. It is distinctive because it explains complex evidence better
than conventional interfaces, not because of badges, cards or repeated metadata. Ask of every pattern: without the
CauseWay logo, would this page still show a distinctive way of handling evidence? If a pattern adds a layer instead of
removing one, drop it.

Use your strongest available capabilities where they serve the page: frontend and design skills, real-browser
screenshots read back, data visualisation, an Arabic editor and an accessibility review. Do not multiply agents or
documents for their own sake. Challenge this charter: where the live renderer or the evidence shows a better answer,
take it and record why in one DL-V2 line.

Tone: calm, formal, exact, readable. A public evidence instrument with editorial intelligence. Never a dashboard, a
consultancy site, a template, a data dump or a campaign page.

══════════════════════════════════════════════════════════════════════
2. THREE CLASSES OF DESIGN DECISION
══════════════════════════════════════════════════════════════════════
A. Governed invariants: never redesigned.
   - Copy, values, units, universes and periods.
   - Routes, the question architecture, and the semantics of Search and Compare.
   - Evidence–source relationships, rights and publication states.
   - The analytical form of the visual contracts, and the correction and version behaviour.
   - A defect here is fixed Master-first.
B. Required patterns: implemented wherever the controlled state supports them.
   - SIG-1 the figure grammar; SIG-4 absence; SIG-5 the verdict in Compare; SIG-7 print.
   - Detached-use safety.
   - The visible boundary beside every figure (brief S3).
C. Candidates: they must prove themselves before global use.
   - SIG-2 evidence-class marks; SIG-3 the clock strip; SIG-6 the two clocks.
   - The masthead treatment, the desktop TOC presentation, compact source rows and display-scale changes.
   - A candidate becomes global only after it passes on three page families in G1 or G2. Record the decision as a
     DL-V2 entry, with its evidence.

══════════════════════════════════════════════════════════════════════
3. WORKING PROTOCOL: AGAINST MECHANICAL WORK
══════════════════════════════════════════════════════════════════════
3.1 Intent before styling. Before each page family, write a memo in design/DESIGN_INTEGRATION_V2.md:
- the one thing the page must make obvious;
- the reader's first three questions;
- the current failure, with a screenshot or a measurement;
- the options considered;
- your choice, its class (A, B or C) and its cost;
- what becomes more true, what becomes more complex, and what can be removed.
Think hard at each memo and at the G1 decision. [v3.2] Keep memos short: record material decisions, their evidence and
their trade-offs in DESIGN_INTEGRATION_V2.md; do not write prose for its own sake.

3.2 Build → look → critique → refine.
- Render AR 390 first, then EN 1440.
- Open every screenshot with the Read tool and judge it as an editor would. Metrics confirm judgement; they do not
  replace it.
- Refine Home, one domain page, one dense Evidence Record, /data/ and one Reading, in both languages, until their
  criteria are demonstrated. [v3.2] A pass ends when its criteria are met, not when a set number of reviews is done.

3.3 Arabic first, not English mirrored.
- Judge AR 390 first. English is a sibling composition.
- Never shrink Arabic to match English height. Never force English line breaks onto Arabic.
- Never mirror quantitative axes, and never translate IDs.
- Never rewrite governed Arabic in presentation code.

3.4 Three families before a global rule. Test every rule on Home or Orientation, an Evidence Record, and a dense
reference or data page. If it helps one family and harms another, specialise it.

3.5 The source-owner test. Use five figures. [v3.2] Resolve each from its current Master record when the test runs (value, unit, universe,
period and publication state); the list names the objects, not fixed values:
- 11.9% account ownership;
- the latest POS terminal count;
- the 2024 remittance restatement;
- the bank balance-sheet composition;
- one microfinance panel figure.
For each, check seven things: value; unit; universe; period; the publisher's role; that the limit is visible; that
CauseWay's attribution is kept separate from the source's authority. Any failure blocks visual acceptance.

3.6 Counterfactual deletion: for interface chrome and duplicated explanation only, never for governed content.

══════════════════════════════════════════════════════════════════════
4. PRINCIPLES, EACH WITH A TEST
══════════════════════════════════════════════════════════════════════
P1 Answer, clock, boundary and verification path travel together.
- Test: on AR 390, every domain and record page shows, within its first screen (390×844), the answer, its clock, a
  boundary cue and a visible link to the evidence or source.
- The full source title and the full boundary text may follow below.
- [v3.2] This is the target outcome, never a reason to shrink, clip or compress Arabic. Where a long governed title
  or an accessible size makes the target unreachable, record the page, the measured position and why the composition
  is still the clearest available.
P2 Provenance is visible.
- Test: no consequential figure needs a hover to show its evidence role, period or source path.
P3 Absence has weight.
- Test: nothing missing looks like zero or like a rendering failure. Use the governed state vocabulary.
- In dense tables, use one compact accessible label plus a table note, not a sentence in every cell.
P4 Calm authority.
- Hierarchy comes from type, space, rules and alignment, not from card walls, shadows, gradients, animation or brand
  colour.
- Test: at 25% zoom the reading order is still obvious.
P5 Detached use stays safe.
- Test: a crop, a copied figure, a print or a shared card keeps enough scope and source to prevent material misuse.
P6 Performance is part of design.
- Tests:
  - the existing budget gate (scripts/performance_budget.py) passes;
  - a before/after report covers Home, one domain, CLM-001, /data/ and one Reading, in AR and EN: cold-load bytes and
    the JS, font and image deltas;
  - every persistent byte added names its reader benefit;
  - the first screen renders with system fallbacks and no layout jump.
- No font CDN, decorative imagery, animation framework, icon framework or unnecessary chart library.
- Speed on Yemeni networks is release-stage evidence; W4 claims nothing about it.
P7 Every new pattern earns repetition. A new global component serves a repeated reader job on at least three routes,
unless one governed family uniquely needs it.
P8 Two languages, one truth. The same facts, limits, order of meaning and verification path, in different
compositions where the scripts require it.
P9 Semantic invariance is proven, not promised. The standing gates already prove the text: content parity (no
governed sentence lost, no ungoverned number), the projection check, bilingual invariance and the literal audit. W4
adds what they cannot see (§12).
- [v3.2] They do not prove that EN and AR carry the same certainty and causal limits. Before G3, an Arabic editor and
  an English editor read a sample of high-risk statements side by side, as rendered: CLM-001, a Compare verdict, two
  Reading theses and the two-clocks text on Home. They report any difference in hedging, causality or scope. This is
  a targeted check of the changed presentation, not a second whole-corpus gate.

══════════════════════════════════════════════════════════════════════
5. SIGNATURE PATTERNS (SIG-n, so they cannot be confused with the brief's S-rules)
══════════════════════════════════════════════════════════════════════
SIG-1 Figure grammar (required where a consequential quantitative figure exists). One visual unit made only of
controlled fields:
- value and unit; universe; period; publisher;
- the evidence class, where SIG-2 is accepted;
- one material "does not establish" line;
- the record or source path.
A record with no value (a framing or method rule) keeps its own governed record form and never shows an empty plate.
It must survive copy, print, screenshot and sharing.

SIG-2 Evidence-class marks (candidate; a mapping audit comes first).
- Map every proposed mark to a class that already exists: VIS-EVIDENCE-CLASS-LADDER and the records' governed
  classes. Report the coverage and the records that have no safe mapping.
- No mapping means no mark. Never create a second taxonomy.
- Shape plus word, with accessible text, and never colour alone.
- /methodology/ defines the classes. Link to it once per section, not from every mark.

SIG-3 Clock strip (candidate; a date-coverage audit comes first).
- Observed (fieldwork or reference period) → published (by the source). Use only dates the Master holds.
- Keep "source link last checked" out of the evidence clock. It belongs with the source line, worded as a link check,
  so that it can never read as currentness of the measurement.
- Say "not stated" only where the absence is material.
- Do not force a strip onto a record whose chronology is simple.

SIG-4 Absence (required).
- One structural treatment with explicit words for the absence states.
- [v3.2] Use only states that are publicly eligible and already in the controlled vocabulary. Publication filtering
  comes first: the component never reveals the existence or metadata of an internal-only object. "Withheld" and
  "no public locator" appear only where controlled public copy already states them.
- It applies in tables, charts, the subgroup table and the Measurement Agenda.

SIG-5 Comparability verdict (required in Compare; elsewhere only where two figures are actually juxtaposed for
comparison). Use the controlled verdicts only: directly comparable; comparable with qualification; not comparable;
unresolved. Each has a shape, its word and its one controlled reason.

SIG-6 Two clocks (candidate). On Home, where the controlled content already contrasts the people-side evidence
(fieldwork 2022–23) with newer system evidence. In a domain only where that contrast is material. Attach the clocks to
the evidence objects before inventing any visual. Never imply that newer system data update an older measurement of
people.

SIG-7 Print (required). [v3.2: replaces the mandatory evidence-sheet page.]
- Every printed page is intelligible on its own: limits, sources, the page URL and the edition print, and navigation
  does not (brief, Print).
- Records print complete, with nothing cut (D13). The first printed page carries the figure grammar or its
  non-value equivalent, with its boundary.
- A separate evidence-sheet page is used only where testing shows that it helps a dense record, and never where it
  merely duplicates.

SIG-8 Reading page (required where the controlled structure supports it).
- An editorial measure, with figures as governed evidence objects.
- Definitions appear as margin notes on wide screens, and inline on phone, only where definition objects exist.
- No rhetorical pull quotes.
- A "how to use this" block only where the Reading's controlled content supports one.

══════════════════════════════════════════════════════════════════════
6. VISUAL LANGUAGE
══════════════════════════════════════════════════════════════════════
6.1 Palette: the baseline is the shipped V1 system. Do not import another.
- The live tokens (scripts/yfie/theme.py; design/02_TOKENS.json; decision DL-V1-001):
  - surfaces: paper #F7F5F0, white #FFFFFF;
  - one green: green-700 #005A44, also the counter or boundary voice, and green-900 #0C3B2E;
  - sage: 100 #E7ECE4, 400 #8A9A82, 600 #5F7357;
  - brass and ochre: brass-300 #B8975A, which is also the ochre line, brass-700 #7A5A1D, gold-300 #D6B86A;
  - ink #17212B, ink-2 #3D4954, mute #646F79;
  - rules: rule #D8DDE2, rule-2 #AEB7BF.
- DL-V1-001 retired the teal #1E5650 and #F5F1E9. They stay retired.
- The palette proposed in the OpenAI review (#13291F, #1C3D32, #C9A24B, #F6F2E9) appears nowhere in the repository.
  It is not used.
- The two layers already exist in V1. Keep them distinct:
  - institutional layer: the canonical logo, the green-900 colophon band and gold-300 group headings;
  - evidence layer: ink, rules, ochre and the green counter voice.
- Semantics:
  - brand gold is never chart data;
  - green never means "good";
  - evidence states are shown by shape and word;
  - there is one interactive accent.
- A token change is a candidate (class C). It needs a DL-V2 entry, a token diff and measured contrast: at least
  4.5:1 for text and 3:1 for UI, on the real surface.
- G1 tests a white surface against the paper surface for figures.

6.2 Type.
- Two faces only: IBM Plex Sans Arabic and IBM Plex Sans.
- Keep the proven Arabic sizes and leading unless browser evidence shows a defect.
- A modular ratio (about 1.2–1.25) is guidance, never a rule that overrides tested role sizes.
- G1 tests the Arabic heading weight at 600 against 700.
- Figure numerals are tabular, with the unit set smaller beside them.
- Small labels are in sentence case.

6.3 Structure.
- An 8-point rhythm; a 12-column desktop grid where useful; one reading column on phone.
- Rules and space before boxes; small radii or none.
- The TOC follows brief S10 (at most six entries; none on pages under six phone screens; the tiers in
  presentation_priority.json). Sticky on desktop only where the page is long and the evidence column is not crowded.
  Phone gets a simpler, non-sticky equivalent.

6.4 Charts: the governed contracts, with their analytical form unchanged.
- Direct labels and units; breaks annotated, never smoothed; no 3D and no gradients.
- Arabic bidi and axis integrity; the limit attached.
- The data table follows brief S3: in a disclosure, and still present in print and in screen-reader order.

6.5 Motion: state changes only, under 200 ms, and reduced motion respected.

══════════════════════════════════════════════════════════════════════
7. PAGE-FAMILY OUTCOMES: the one thing each page must make obvious
══════════════════════════════════════════════════════════════════════
- Home, in ten seconds:
  - the thesis;
  - that different evidence has different clocks;
  - the strongest starting evidence;
  - where to begin.
  Never promise that Home summarises everything known.
- Explore: find the question.
- Domain: the strongest bounded answer, its main limit, the evidence path and the next depth.
- Evidence Record: exactly what the evidence is, what it is not, its source, and its method and reproducibility.
- Compare: whether comparison is legitimate, before any difference is read as meaningful.
- Readings: a bounded argument, with its evidence inspectable.
- Measurement: which missing evidence matters for decisions, and what new measurement would change.
- Sources (/data/): the original document, and its relation to the public evidence, fast.
- Methodology: how evidence is accepted, compared, derived, corrected and bounded.
- Trust pages: CauseWay's role, corrections, accessibility, rights, the footprint and accountability.

══════════════════════════════════════════════════════════════════════
8. CAUSEWAY'S PRESENCE
══════════════════════════════════════════════════════════════════════
- Visible through: the canonical mark, the institutional layer, a disciplined colophon, and stewardship language that
  is already controlled.
- Never through: service offers, client logos, lead-generation language, promotional claims or self-congratulatory
  benchmarking.
- Colophon lines (stewardship, licence, edition, corrections, footprint, funding and independence) must already be
  controlled copy, or go Master-first before use.

══════════════════════════════════════════════════════════════════════
9. DETAIL PASS (every family, AR and EN, before G3)
══════════════════════════════════════════════════════════════════════
- Arabic: «،» «؛» «؟» and «…»; no letter-spacing, justification or hyphenation; never kashida for layout; long
  titles readable.
- Bidi and numbers:
  - Latin names and IDs isolated;
  - Western digits, per the house style;
  - numeric and time axes left to right;
  - ranges and percentages verified.
- Dates follow brief S13: human dates in all reader-facing text and clocks. ISO stays only in machine contexts:
  datetime attributes, BibTeX and RIS exports, IDs and data files.
- Headings: no widows where avoidable.
  - Domain H1s become short theses through brief S11, Master-first.
  - Elsewhere, "at most three phone lines" is a goal, never permission to shrink or rewrite governed copy outside a
    transaction.
- Links: a visible focus ring and link affordance everywhere. External-link wording comes from controlled UI copy.
- Tables: caption, units and alignment; a responsive strategy and an accessible fallback.
- Forms (the error report): labels, hints, inline errors, keyboard use, and a success state in words.
- Portable forms: print, social cards and export frames checked separately in AR and EN; nothing clipped.
- States: the empty, error and loading states of Search, Compare and the filters keep their governed technical voice.

══════════════════════════════════════════════════════════════════════
10. G1: THE DIRECTION CHALLENGE
══════════════════════════════════════════════════════════════════════
10.1 Three candidates, built outside the shipped stylesheet (design/exploration/v2/), each as a token and CSS delta
over V1, with a recorded token diff:
- (a) quiet official-statistical;
- (b) editorial-evidence;
- (c) compact source-first.
They must differ in information hierarchy and reading order, not only in colour or decoration.
- Use earlier work as challenger evidence, not as decisions. That includes the T4 "Instrument" compositions; its
  palette stays retired under DL-V1-001.
- Recover from the older V3 skin prompt only its regression checks: existing components, small visual choices,
  first-screen editorial quality and cross-page consistency. Take them only where W4 does not already cover them.
  Never revive a standalone skin or a separate design track.

10.2 Scope: the high-leverage surfaces only. Do not build Stage B three times.
- Home: the masthead; the thesis; one people-side figure; one infrastructure figure; a boundary; the question entry.
- CLM-001: the first answer; scope and clock; the boundary; source and verification.
- /data/: one curated source; one ordinary source row; the filter shell.
- One domain: payments, unless the visual contracts make another the better stress test.

10.3 Disqualifiers, applied before any scoring. A candidate is out if it:
- changes governed content;
- hides a material boundary;
- changes a visual's analytical form;
- fails AR 390;
- breaks detached use;
- adds unjustified JS;
- worsens performance without reader value;
- weakens source closure.

10.4 Scoring of the survivors, 1–5. Evidence comprehension and Arabic quality weigh more than novelty.
- Three judges: an Arabic first-time phone reader; a sceptical statistician-journalist; a World Bank or IMF data
  professional.
- Criteria: first-screen comprehension; boundary comprehension; provenance; source path; long-text readability;
  Arabic quality; calm and formal tone; implementation simplicity; distinctiveness without decoration.
- Measured columns:
  - phone screens to the first answer and in total, at AR 390, before and after (the owner's main complaint is long,
    heavy phone pages);
  - the byte delta.
- Then run the source-owner test on CLM-001 for each survivor.

10.5 The decision (D7: a recorded, criteria-based choice; the owner can veto, but approval does not block).
- Choose one direction and record it as DL-V2-001: the scorecard with its measured columns, your reasons, what was
  rejected and why, and one honest sentence on what each candidate sacrifices.
- Commit under design/evidence/v2/:
  - AR 390 and EN 1440 screenshots of Home and CLM-001 for all three candidates;
  - the /data/ and domain proofs.
- Link them from the PR so the owner can veto. Then continue to G2 without waiting.
- Roll out only the chosen direction. Delete nothing in design/exploration/v2/: it is lineage.

══════════════════════════════════════════════════════════════════════
11. G2: IMPLEMENT THE WINNER
══════════════════════════════════════════════════════════════════════
Order: shell on the proving pages → Home → domain → Evidence Record → /data/ → Reading → Methodology → propagation to
the remaining families.
- Two refinement passes on each proving family.
- Do not custom-design every route.
- Decide each class-C candidate explicitly: accepted or rejected, with its evidence.

══════════════════════════════════════════════════════════════════════
12. GATES W4 ADDS (the standing gates keep running)
══════════════════════════════════════════════════════════════════════
1. Rendered visibility (new; Playwright; AR and EN; 390 and 1440).
   - Every governed string that content parity finds in the HTML must be visible, or sit inside a native disclosure
     with a descriptive accessible label.
   - The answer, the clock, the scope, the boundary and the verification link are never inside a closed disclosure.
   - No line-clamp, overflow clip or text-overflow truncation on governed text.
   - Intentional screen-reader-only text is allowed only from a listed set, each item with its reason.
   - Add negative controls: one hidden boundary and one clamped paragraph.
   This closes the one gap W4 opens: the stylesheet can hide what the HTML still contains.
2. Drift report (new; cheap): across the W4 range, site-src/content/** and the route list are unchanged except by
   listed transactions. Any unexplained difference is a FAIL.
3. Social cards and portable frames.
   - `scripts/social_images.py --check` hashes only each card's frame HTML, not the stylesheet, fonts or logo it
     loads. A redesign would therefore pass the check while every card still shows the old design.
   - Add a template fingerprint (the frame CSS, the font files and the logo bytes) to INDEX.json, compare it in
     `--check`, and add one negative control.
   - [v3.2] Order: stabilise the design, let the fingerprint mark the stale cards, regenerate them, and check the
     actual AR and EN output, all before G3 acceptance. Do not regenerate on every iteration.
4. The performance before/after report (P6).

══════════════════════════════════════════════════════════════════════
13. DONE FOR STAGE B
══════════════════════════════════════════════════════════════════════
- DL-V2-001 is recorded and one direction is implemented.
- Every family has its memo. The proving pages have had two refinement passes. The Arabic-first detail pass is done.
- The required patterns are implemented wherever the controlled state supports them. Every candidate has an explicit
  accept or reject decision, with the SIG-2 and SIG-3 audits reported.
- [v3.2] G0's six-persona reader-job audit (brief W4 G0) is re-run on the final build. These are simulated
  walkthroughs with browser measurements; human and specialist acceptance stays with the later release gates.
- On AR 390, P1 passes on every domain and record page, or each exception is recorded. Phone screens are reported for each family, before and after.
- Green: content parity, visibility, drift, detached use, the tools and the error form, accessibility (recorded),
  browser, the budget, and every standing gate.
- design/DESIGN_INTEGRATION_V2.md tells the story in one place:
  - decisions and trade-offs;
  - the before/after gallery and the G1 scorecard;
  - what became more true, what became more complex, and what was removed;
  - what remains release-only.
- Never claim accessibility conformance, live performance or release readiness.
- Stage B ends with the stage report. Release dependencies (live host, rights, live testing in Yemen, human
  accessibility review, owner acceptance) are not Stage B blockers, and Stage B is not release approval.

══════════════════════════════════════════════════════════════════════
14. RELEASE BOUNDARY
══════════════════════════════════════════════════════════════════════
Completing Stage B is not release readiness. The live-host, rights, security, correction and named-owner gates of the
runbook still apply.

══════════════════════════════════════════════════════════════════════
15. CHANGE RECORD: v1 → v3, with the OpenAI review (v2) adjudicated against the repository
══════════════════════════════════════════════════════════════════════
Adopted from the review, where v1 was weaker:
- the charter decides presentation only;
- the three classes (A, B, C);
- the faithful-representation test replaces v1's "more carefully than their own releases";
- marks only with a class mapping;
- "checked" taken out of the evidence clock, and "not stated" only where material;
- two clocks made conditional;
- print as page 1 plus the full record: v1's single A4 page contradicted D13;
- the type ratio as guidance;
- G1 reduced to the high-leverage surfaces, with disqualifiers before scoring;
- the performance delta, and the release-stage boundary for live speed;
- compact absence labels in dense tables;
- the SIG-n names, which end the S3 / S-3 ambiguity.

Changed in v3.2 (second owner review, 11 October):
- P1 is a target outcome, with evidenced exceptions.
- SIG-7 requires independently intelligible print; the evidence-sheet page is optional.
- SIG-4 shows only publicly eligible states.
- Source-owner figures are resolved from the Master when the test runs.
- P9 adds a targeted bilingual certainty check.
- The social-card regeneration order is fixed before G3.
- G0's reader-job audit is re-run on the final build.
- Memos and refinement passes end on criteria, not on counts.

Changed in v3.1 (owner review of 11 October):
- G1 no longer stops for the owner. v3's stop conflicted with D7.
- The social-card blind spot is stated in the charter itself.
- T4 and the V3 skin prompt enter as challenger evidence and regression ideas only.
- The ambition and challenge clause is added.

Corrected in the review, from repository bytes:
1. Palette. v1 did not introduce colours: it named the live V1 tokens (theme.py, DL-V1-001). The review's "CauseWay
   shell" colours exist nowhere in the repository. Its "existing evidence palette" revives #1E5650 and #F5F1E9, which
   DL-V1-001 retired. Following it would create the third palette the review warns against.
2. Authority. The review placed the current contracts above the brief, which would block owner-authorised changes
   made through governed paths (D8, D14, brief S11). Its order is replaced by §0.
3. Dates. Brief S13 already scopes the rule: human dates in reader text; ISO in machine fields. The rule stays, as
   the owner asked.
4. Invariance. Content parity, the projection check, bilingual invariance and the literal audit already prove the
   text. The new gate targets the real W4 risk, visibility (§12.1), rather than duplicating them. The review also
   dropped a measurable P1 and phone-length reporting; both are restored.
```
