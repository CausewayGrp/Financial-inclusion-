# D1 — Theses and foundations

> STATUS: **D1 IN PROGRESS — CONVERGED ON T4 · INSTRUMENT (§3.6, DL-D1-006). §1 holds the thesis hypotheses; §2 the
> exploration and inspection; §3 the critique, adjudication, adversarial tests and the decision; §4 (Design Intent
> Lock) and §5 (foundational grammar) are not yet written.** The decision is accepted within D1 only; it becomes a
> Lock when §4 is written from the rendered reference implementation, and nothing propagates before D1 exits.

Gate: D1 · Branch: `claude/practical-cray-sr26c5` (see the process note in `ESCALATIONS.md`) · Accepted start
`8bf19efad7505792ca22e0a3bda1db31fb85d33c` (`main`, D0 accepted). Authority fingerprints re-verified at gate start:
Production Master `17db032b…038690b`, Page Specs `d4574804…824b69aa`, logo `5830163d…`.

## 0. What D1 starts from

The reference build in `dist/` is a behavioural baseline, not a design (brief §0). Read on the stress trio at 390 and
1440 px in both languages before any thesis was drawn:

- **Home** is a conventional institutional page: oversized hero, two buttons, a 2×2 card grid of questions, then
  alternating tinted bands with a large heading and a paragraph, a `<details>` for the records, three CTA cards and a
  dark footer whose logo is whitened by CSS (EAD-04). With the Yemen content removed it could be any NGO or consultancy
  site: the anti-template test fails. Nothing on the first screen tells a cold reader *why* inclusion is not one number.
- **`/evidence/CLM-003/`** renders the governed fields as labelled cards, a gold boundary note, a source list and a dark
  utility bar. The record's central fact — two totals (1,357 → 1,473), a derived 8.55 % and the source's displayed
  +11 % — exists only as prose. The discrepancy the hard state `verification_dense` must make visible is not visible
  as a discrepancy; it has to be read.
- **`/readings/same-year-different-number/`** is a centred single column with a text-only "visual" (the baseline draws
  no chart, by rule). The argument's key move — two published values for the same year — is never seen.
- **Arabic** is the English layout mirrored: same hierarchy, same proportions, same rhythm, with Tahoma/Arial fallbacks.

None of this is inherited into D1. The D0 names — Register, Argument, Layers — are provocations (D0 DL-D0-003); they
are sharpened here into three product logics that differ in what the reader perceives first, in the mental model of
the evidence system, in how depth and verification work and in how Arabic and mobile are composed.

## 1. Thesis hypotheses (pre-exploration) — three materially different design logics, and a second-generation fourth

Each hypothesis answers the ten questions of the D1 mandate (and, since the owner's challenge, an eleventh: the
grounding hypothesis). They are tested on the same trio with the same governed English and Arabic content; nothing is
shortened, simplified or invented for any of them. T4 was added after the first-generation propositions had been
composed and critiqued by their designer (§2.3); it is tested under the same protocol, not privileged.

### T1 · REGISTER — the evidence record is the organising object; the apparatus is visible

1. **Central idea.** YFIE is a public register of bounded evidence. Every consequential statement is an *entry*, and an
   entry always shows its apparatus: what is measured, for whom, when, by what method, from which source, in which
   state. The apparatus is not chrome added to content; it is the content's typographic skeleton, set in a start-side
   margin column (marginalia) beside the statement it governs.
2. **First perception.** Structure before sentence: the reader sees that every number here comes with conditions
   attached, and that the conditions are set in one consistent notation. Home opens as a register's front matter —
   the product's claim, then the four governed starting questions set as numbered entries with their scope line,
   then the "three figures" section with each figure's clock, population and state as marginalia.
3. **Information hierarchy.** Dominant: the governed statement and its marginal clock/population line. Quiet:
   navigation, utilities, decoration (none). Density is high and controlled; whitespace is vertical rhythm, not
   emptiness. Stable IDs appear as reference marks, never as titles.
4. **Depth model.** Answer → scope → boundary → evidence → source read as columns of one entry (statement · margin ·
   footnotes), not as a scroll. The Evidence Record is one long entry: the figure and its two competing percentages
   are set as a small typographic table in the entry's body; sources are its footnotes with their locators.
5. **Verification model.** Verification is where the eye already is: the margin. Each figure's margin carries source
   reference, period and the state label; "Open source record" and "Open original source" sit at the foot of the
   entry. Cite/report actions are entry-level, not page-level.
6. **Relationship model.** Cross-references in the register's own notation: "used in" and "returns to" lists as
   reference lines at the entry's foot; a Reading's "Trace the evidence" is a numbered concordance of its entries.
7. **Arabic implication.** The margin sits on the reading-start side (right); marginalia are composed in Arabic with
   their own size steps and line height (Plex Sans Arabic needs a taller leading and a larger optical size than the
   Latin at the same nominal size); mixed runs (IDs, `USD million`, `2021 = 100`) are isolated LTR inside the RTL
   margin. Arabic headings are not letter-spaced or condensed; numerals are Western.
8. **Mobile implication.** The margin cannot stay beside the statement below ~640 px. Hypothesis: it becomes a
   *lead-in line* above each statement (clock · population · state) rather than a trailing footnote, so the frame
   is read before the figure. Density is reduced by rhythm, not by hiding limitations.
9. **Principal risk.** Bureaucratic coldness; apparatus that reads as clutter to a citizen reader; a Reading that
   feels like a ledger rather than an essay; margin collapse on mobile turning into a wall of small labels.
10. **Why YFIE.** The product's whole promise is that no number travels without its conditions. A register makes that
    promise structural and screenshot-safe: crop an entry and its margin comes with it.

### T2 · ARGUMENT — reading-first; the proposition leads; evidence discloses in place

1. **Central idea.** YFIE is a set of arguments that show their working. A page is one measured column of prose in
   which ANSWER, SCOPE, BOUNDARY and VERIFY are distinct typographic *registers* of the same text (not boxes beside
   it): the answer in the primary voice; scope and clock as a quieter running line; the boundary as a marked
   counter-voice that interrupts; verification as a footnote apparatus that expands in place.
2. **First perception.** A sentence before a structure: the reader meets the product's thesis as a line of argument
   ("Financial inclusion in Yemen is not one number.") followed immediately by the reason, in prose, in the reader's
   language. Home is an opening argument, not a landing page.
3. **Information hierarchy.** Dominant: the sentence. Secondary: the boundary counter-voice, which must never be
   quieter than the claim it bounds. Quiet: everything that is not the text. Chrome is minimal; the reading measure
   is fixed (about 68–76 characters in English; its Arabic equivalent set independently).
4. **Depth model.** Depth is in place: a figure in prose expands to its record fields under the line where it stands;
   a record's method and verification expand under their headings; nothing navigates away until the reader chooses a
   source. The Evidence Record is a short structured essay with the figure set as a display line inside the prose.
5. **Verification model.** Footnotes that open: each consequential figure carries a mark; the mark opens the source
   line (source title · publisher · locator) in place, keyboard- and tap-operable, never hover-only. The source
   list at the end repeats the same lines.
6. **Relationship model.** Relationships are prose links: "This record is used in …", "Return to the question", and,
   in Readings, the trace as a numbered list of propositions that read as sentences. No rail, no cloud.
7. **Arabic implication.** The Arabic column has its own measure (fewer characters per line at a larger optical
   size), its own heading scale (Arabic display sizes step less steeply than Latin) and its own leading. The
   counter-voice register must be carried by weight and structure, not by italics (Plex Sans Arabic has no italic).
8. **Mobile implication.** A single column survives narrow width almost unchanged; the risk moves to length: the
   Reading at 390 px is long, so section navigation and a persistent "where am I" line are needed; expansions must
   not push the reader far from the line they opened.
9. **Principal risk.** Verification depth buried in disclosures; the Evidence Record losing its professional-object
   quality; a Home that is beautiful to read but slow to orient; and, on mobile, an essay that is simply long.
10. **Why YFIE.** The evidence here is argued, not dashboarded: the same year gives different numbers because of a
    measurement event, and only prose can carry that distinction with its caveats intact.

### T3 · STRATA — the evidence system made spatial; position and connection are what the reader perceives

1. **Central idea.** YFIE is a connected system with depth: every consequential page is a fixed sequence of strata
   (answer → scope → boundary → source), and the reader always knows which stratum they are in and what is one step
   deeper or one step across. A persistent, relevance-limited *evidence trail* shows the few governed relationships
   that matter here (records used, sources bound, Readings, the question it answers) — never everything.
2. **First perception.** Position before sentence: the reader sees a map-like arrangement — the product's claim, the
   four governed questions as entrances into the system, and, visible at once, the shape of a journey (question →
   answer → record → source). Home is the system's threshold.
3. **Information hierarchy.** Dominant: the stratum labels and the current stratum's content; the trail is secondary
   but always present on desktop. Quiet: chrome. State grammar is carried by structure and pattern (position, rule
   weight, marks), not by colour and not by type alone.
4. **Depth model.** Depth is literal: the Evidence Record's strata are stacked in a fixed order with a stratum index
   that stays in view; the Reading has the essay as its centre stratum and its trace as the stratum beneath.
5. **Verification model.** The trail is the verification model: from any stratum the bound sources are one step
   away in the trail, with locators; the source stratum at the foot repeats them in full.
6. **Relationship model.** The trail shows relationships as *edges with a type* (used in, bound to, answers,
   returns to) drawn from the projections' bindings only; adjacency never implies causality, and the trail carries no
   evidence-strength marks (none is governed).
7. **Arabic implication.** Strata order is the same; the trail sits on the reading-end side (left) in Arabic so that
   the reading-start side holds the content, or the trail is composed as a stratum band rather than a side rail.
   Stratum labels are Arabic-first labels with their own type sizes.
8. **Mobile implication.** A side trail cannot exist at 320–390 px. Hypothesis: the trail folds into a compact
   "in this system" strip under the answer stratum and re-expands as the foot stratum; the stratum index becomes a
   sticky one-line position indicator.
9. **Principal risk.** Chrome and rails that outweigh the evidence; a trail that invents relationships by proximity;
   mobile collapse into accordions; a Home that looks like a product tour.
10. **Why YFIE.** The brief's core problem is a reader lost among hundreds of documents on different clocks; a spatial
    system tells the reader where a number sits before they read it.

### T4 · INSTRUMENT — second generation: an instrument that answers the reader's questions and states what it cannot answer

Authored after §2.3 under the owner's design-ceiling review (DL-D1-005). A proposition under the same tests as T1–T3,
not a hybrid of them; challenged, not defended.

1. **Central idea.** YFIE is an instrument, not a publication and not a portal: a reader brings a question about
   Yemen's financial-inclusion evidence and the instrument returns a bounded answer — when, for whom, what it
   establishes, what it does not, where it rests — in one register on every surface. ANSWER → SCOPE → BOUNDARY → VERIFY
   is not a page template; it is the anatomy of every evidence object.
2. **First perception.** Clock before claim: every bound record opens with its clock (period, population, state) set as
   a small labelled reading, then the statement as its governed sentence. A number is never typeset outside its bounded
   object or its sentence — no lifted figures (T1's doubt), no standfirst of bold numbers (T2's doubt). Home opens with
   the product's claim and then *demonstrates* "not one number" by pacing the governed section-3 text sentence by
   sentence, each sentence a block, the governed resolution sentence set apart above a rule.
3. **Information hierarchy.** Dominant: the governed statement and the clock that frames it. Structure: the seven
   governed questions of an Evidence Record — what it establishes, what it measures, whom or what it applies to, how
   current it is, what it does not establish, what it rests on, and what more there is (lineage, verification state,
   where it is used) — are its section structure *and* its index, in the same order on every record, so the instrument
   is learned once. Quiet: chrome; the product bar carries name, search and language only. Decoration: none. Surfaces are
   paper and plaster; rules are hairline, a heavy ink rule at the start of every object, a doubled rule at every
   boundary.
4. **Depth model.** Depth is answered questions, not scrolling: the question strip on mobile and the spine index on
   desktop jump between the seven answers; further detail sits behind a labelled disclosure whose summary says what it
   holds. The Reading keeps its essay whole; its figure is an inset object with the same anatomy (rubric, title, clock
   caption, boundary, credit, canonical link).
5. **Verification model.** A verification spine on every page with one anatomy: what this page rests on (sources with
   reference and locator actions) and where it returns to (the canonical record or the index). On desktop it is a
   plaster column beside the object; on mobile it is the foot of the object, reached from the strip. Trust links lead
   the institutional footer band.
6. **Relationship model.** Bound relationships only, carried by one object grammar: a record's "where it is used" lists
   its Readings; a Reading's trace is a list of compact clock-first objects that open the records; Home's records are
   the same compact objects. The connected system is perceived through repetition, not a diagram.
7. **Arabic implication.** Composed first in Arabic at 390 px: Plex Sans Arabic at a larger nominal size and longer
   leading than the Latin (body 18 px / 1.9 against 17 px / 1.6), the measure in `em` not `ch`, no letter-spacing and
   no capitals (the Latin rubric is spaced small capitals; the Arabic rubric is weight and colour only), clocks and
   references as `bdi`-isolated left-to-right runs, the double boundary rule and the ochre rubric identical in both
   scripts so the instrument reads the same across the language switch.
8. **Mobile implication.** Mobile is the primary composition, not a collapse: one column of objects; the question strip
   is the index; the spine becomes the object's foot; the desktop grid (object plus a 300 px spine) is added from
   900 px. RV-CWR-001 panel 1 sets the publications as rows with a horizontal zero-based value axis, so the two 2024
   values cannot stack as a fall; panel 2 keeps two side-by-side indexed lanes.
9. **Principal risk.** Sameness — one grammar everywhere may flatten the Reading into a form; clock-first order may
   feel bureaucratic to a citizen reader at Home; a plaster spine with ochre rubrics could slide toward the
   documentation-site pattern T3 was faulted for; the seven-question index depends on the governed labels holding in
   every record (tested on CLM-003 only).
10. **Why YFIE.** The product's promise is that a reader can understand what the evidence says and what it cannot say;
    an instrument whose every object answers the same questions in the same order makes that promise legible, portable
    (a crop of any object carries its clock and its boundary) and equal in both languages.
11. **Grounding hypothesis.** Yemen by abstraction only: paper and plaster surfaces, and three roles taken from the
    canonical logo's own colours — ochre for rubrics, navy ink for text, teal-green for the boundary voice — with no
    motif, border, map or image. The grounding is material and chromatic: felt as colour temperature and a discipline
    of rules, never seen as a theme.

### The higher-order question every thesis must answer (owner challenge, 27 September 2026)

YFIE must land, within seconds, as a serious, independent public evidence institution that happens to be digital: not a
campaign, a dashboard, a consultancy site, an NGO portal, a fintech product or a government announcement site. Its
design must communicate intellectual seriousness, editorial confidence, methodological restraint, public usefulness,
independence, traceability, calm authority, openness to challenge, deep familiarity with Yemen and international
product craft — composed, not decorated. Each thesis therefore carries an eleventh field:

11. **Grounding hypothesis.** How the thesis could be recognisably grounded in Yemen through abstraction only —
    materiality, proportion, architectural rhythm, voids and openings, layered depth, restrained texture, subtle
    irregularity, surface tonality, the relation of density to quiet and of structure to craft — never through
    borders, motifs, icons, pattern wallpaper, tourism or nostalgia. A subtle influence may be stronger than an obvious
    one, and the grounding is rejected outright where it costs readability, evidence hierarchy, Arabic quality,
    accessibility, performance or institutional credibility. At least one thesis is kept deliberately image-free and
    evidence-native as the control against which the grounded possibility is compared.

- **T1 Register — the manuscript page.** The Arabic scholarly page has, for centuries, carried a text block (matn)
  with commentary in its margin (ḥāshiya): verification and qualification live beside the statement, in a smaller
  hand, on the reading-start side. T1's marginalia is that logic, not its ornament: text-block proportions, rubricated
  labels (an ochre for labels only, never for meaning), hairline rules, paper white. An Arabic-first reader should
  recognise the structure as native, not translated; an international researcher should read it as an archival
  register. Nothing is drawn from manuscripts; the proportion and the division of labour between text and margin are.
- **T2 Argument — the control.** No visual grounding beyond native Arabic composition, editorial voice and a warm,
  neutral paper. Its claim to be "designed with real understanding of Yemen" rests entirely on how it handles the
  evidence: clocks, vintages, universes and boundaries in prose. If T2 wins, Yemen-grounded materiality has failed to
  earn its place.
- **T3 Strata — built form.** Yemen's tower houses (Sana'a, Shibam, the Hadramawt) are ordered storeys of dense mass
  with regular openings, plaster bands over earth-toned walls, surfaces set back in layers, and a strong relation
  between the dense façade and the open sky. T3's strata are that logic abstracted: stacked surfaces whose heights
  follow content (never a uniform card grid), band-like double rules between layers, a lime-white surface on a warm
  earth-grey ground, openings (the trail's edges) that look from one layer into the system, and deliberate quiet
  between dense layers. No arch, no window shape, no ornament, no photograph.

Tests applied to every thesis before convergence (recorded in §3): the **landing test** (credible, serious, calm,
distinctive and worth investigating within seconds; the 30/90/180-second questions of the mandate §7); the
**distinctiveness test** (Yemen content, logo and product name removed — could it be an NGO template, a consultancy
site, a fintech, a SaaS dashboard or an AI-generated institutional homepage?); the **restraint test** (every texture,
colour, motion or decoration must improve comprehension, hierarchy, verification, orientation, grounding or trust, or
go); the **audience test** (one system for the citizen, journalist, researcher, provider, regulator, source
institution, Arabic-first reader and low-bandwidth mobile reader, without portals); and the **higher standard** (does
YFIE solve its evidence problem more intelligently than comparable products: scope, what evidence does not establish,
unlike numbers, unknowns, answer-to-verification, portability, screenshot safety, Arabic parity, methodology as
understanding, measurement gaps as public knowledge?).

### Cross-cutting component hypothesis — the framed figure

Independently of the thesis, the screenshot-misuse and source-owner tests suggest one shared component: a governed
figure is never set naked. Its frame carries unit, population, period, evidence state and source reference in the
same typographic object, so a crop of the figure is a crop of its conditions. Each thesis composes the frame
differently (as marginalia in T1, as a display line with running scope in T2, as a stratum in T3). The canvas tests
whether the frame reads as apparatus (T1), as prose (T2) or as position (T3) — and whether it becomes a card wall
(brief §7, avoid).

## 2. Exploration protocol (what Claude Design is asked to do with §1)

For each thesis, on the canvas, with the governed content of the trio (English and Arabic), at desktop (1440) and
mobile (390):

- compose Home for the cold reader (30 / 90 / 180 seconds): what the product is, why not one number, where to start;
- compose `/evidence/CLM-003/` so that the two totals, the derived 8.55 % and the source's +11 % coexist visibly,
  the limitation is prominent and a crop of the primary evidence area still carries scope and boundary;
- compose `/readings/same-year-different-number/` as a serious essay with RV-CWR-001 drawn per its contract (panel 1:
  two markers at 2024 keyed by publication, no joining line; panel 2: two side-by-side indexed panels, one per source,
  never one axis), the prohibited inference visible, and "What would change this reading?" as the signature;
- compose Arabic natively at the same time, not afterwards;
- state for each composition what the reader understands first, and what would be misread in a crop.

The critique that follows (independent lenses, §19 of the mandate, plus an informed Yemeni reader asking whether the
product caricatures or condescends) is recorded in §3 with the comparison. Only then is one thesis, a hybrid, or a
better thesis chosen.

### 2.1 Benchmark review — principles, not style

A small, deliberate review of excellent current products across five categories (multilateral evidence
institutions; data and evidence journalism; public-service digital products; serious research publishing; Arabic
and RTL publishing), asking of each what it does exceptionally well — trust, density, methodology, uncertainty, entry
for non-specialists, depth for experts, long-form reading, charts and annotation, calm navigation, source
verification, mobile, seriousness without dullness — and recording "borrow the principle, not the style" and "what
YFIE should do better". Nothing is imitated.

**Result (27 September 2026).** The D1 session's network policy blocks every product site tried (Our World in Data,
GOV.UK Design System, Pew Research Methods, Reuters Graphics, Al Jazeera Arabic, the IMF Yemen country page, and the
two research papers a web search surfaced). Under the owner's benchmark-integrity rule nothing is inferred or
attributed for pages not inspected: **every interface benchmark is NOT INSPECTED.** Two source repositories were
readable (DIRECTLY OBSERVED, repository documentation only, not the rendered product): the GOV.UK Design System
repository describes itself as "One place for service teams to find styles, components and patterns for designing
government services" and states no design principles in its README; the Our World in Data grapher repository states
that all its visualisations draw on "a single database into which all of our data is placed" so that "when we add and
update empirical data the visualizations are all updated" — a data-management principle YFIE already meets through the
Production Master, not a presentation finding. No further research detour is taken: D1's evidence is the governed
content, the Claude Design exploration, the rendered stress tests, Arabic, mobile and evidence integrity. The
principles applied in the propositions below are marked in §3 as EXISTING PROFESSIONAL DESIGN PRINCIPLE or
YFIE-SPECIFIC DESIGN JUDGMENT, never as benchmark findings.

### 2.2 Process note — sequencing correction (27 September 2026)

Before the canvas held any proposition, a thesis-specific renderer for T1 was written in the Design workspace. On the
owner's correction it is classified **PRE-DESIGN / NON-AUTHORITATIVE implementation exploration**, held unused, and
excluded as a source for any artboard: the Design propositions are authored on the canvas first, critiqued as Design
propositions, and only then translated into thesis renderers for the empirical stress tests. The neutral harness
(`design/reference/yfie/content.py`, `neutral.py`) carries no design decision and stays the content source.

Status before any thesis-specific coding resumes:

- CLAUDE DESIGN INVOKED: **YES** — canvas "YFIE D1 Thesis Exploration", https://claude.ai/artifact/XmHAYbp2cwfU9o9eLjNiVx
  (Design Artifact type; the eleven IBM Plex faces and the unmodified master logo uploaded as its assets).
- T1 DESIGN PROPOSITION EXISTS: **YES** — canvas version 2 ("D1 thesis propositions v1"), 12 artboards `T1-*`.
- T2 DESIGN PROPOSITION EXISTS: **YES** — 12 artboards `T2-*`.
- T3 DESIGN PROPOSITION EXISTS: **YES** — 12 artboards `T3-*`.
- T4 DESIGN PROPOSITION EXISTS: **YES** — 12 artboards `T4-*` (second generation, DL-D1-005; status in §2.5).

Each proposition is on the canvas as a self-contained artboard per surface × language × size (Home, `/evidence/CLM-003/`,
`/readings/same-year-different-number/` × English, Arabic × 1440 and 390 px), composed with the governed text inserted
mechanically from the harness bundle (never retyped), the eleven IBM Plex faces and the unmodified logo as canvas
assets, and RV-CWR-001 drawn per its contract in each thesis's own visual language. Plain HTML twins of the same
artboards, rendered in Chromium, provide the images the critique lenses inspect and the crops for the screenshot-misuse
test; those renders are proof, not authority.

### 2.3 Designer's own critique of the propositions (recorded before the independent lenses reported)

- **T1 Register.** The manuscript-margin logic holds in both scripts: in Arabic the margin sits on the reading-start
  side for the right reason and the apparatus on the reading-end side. Defects found and fixed before critique:
  sub-entries re-divided the statement column (now rows on the page grid); the Home lead was set at statement size
  (now a lead size); the seven-link trust line cost two rows on mobile (now hidden on mobile, kept in the footer).
  Open doubt: the record's apparatus lifts "8.55%" and "+11%" out of the governed sentence as large figures with their
  grammar labels. In a crop they dominate, the boundary is outside the crop, and the discrepancy reads louder than the
  governed sentence states it. The manuscript logic suggests the opposite treatment: keep the figures inside the
  sentence and carry the two grammar labels as marginal commentary beside it, with the population field in the
  apparatus so a crop keeps period, population and statement together.
- **T2 Argument.** The calmest landing and the safest primary crop (period, population and reference travel with the
  statement). Defect fixed: the related-readings list fell into the number column. Open doubts: the centred masthead
  and tracked caps read as a quality magazine, which the brief lists under "avoid"; six bold numbers in the standfirst
  make the eye jump and let "+11%" compete with the totals; the Evidence Record is scannable as prose but weak as a
  professional object (a researcher hunts for the denominator inside paragraphs).
- **T3 Strata.** The most scannable record (labelled strata, a definition list for scope, a sticky index) and the
  strongest mobile orientation (the anchor strip). Defects fixed: strata shrank to content width on mobile (flex
  alignment), the trail's row span left an empty ground, chart panels forced the column open at 390 px. Open doubts:
  white surfaces on a warm grey ground with a right-hand index is the commonest pattern of documentation sites and
  government portals, so the distinctiveness test is at risk; the lower Home strata collapse into a uniform box rhythm;
  the built-form grounding is faint (a 3 px band and a double band) — either it must be made to carry meaning
  (density and quiet between layers) or it is decoration; and the "answer" stratum's crop loses the period and
  population, which sit in the neighbouring strata.
- **RV-CWR-001 in all three.** Every contract rule is met (two markers at 2024 keyed by publication, no joining line,
  zero-based value axis; two side-by-side indexed lanes with their own labelled axes, distinct marks, the not-comparable
  divider, the in-frame note, boundary, credit and canonical link; tables with scoped headers). Open doubt: with a
  vertical value axis the two 2024 markers still sit one above the other, which a glance can read as a fall; a form
  with publications as rows and the value on a horizontal zero-based axis may make that misreading impossible while
  staying inside the contract. In Arabic the panel order and legends follow the reading direction and the axes stay
  left-to-right, as required.

### 2.4 Independent lens critique — status (27 September 2026)

Nine lens reviews of the first-generation renders — A senior evidence researcher, B Arabic editorial and RTL director,
C accessibility and cognitive UX, D data-visualisation specialist, E frontend architect, F high-end product-design
critic, G journalist quoting responsibly, H source-institution fairness, I informed Yemeni reader — were launched as
independent reviewers with the rendered boards and the crops. Their reports were lost with the session's context before
any was recorded (DEBT-005). Nothing from them is recorded or assumed anywhere in this file. The lenses are re-run on the
first-generation renders and T4 together; §3 records only what is actually received, lens by lens, adjudicated without
averaging or scoring.

### 2.5 Second-generation pass — T4 · Instrument: status (27 September 2026)

Under the owner's design-ceiling review, T4 (§1) was composed mobile-first from the Arabic 390 px Evidence Record
outward, with the same governed text path as T1–T3 and RV-CWR-001 panel 1 in the rows form (§2.3, last doubt).

- Rendered: 12 boards (Home, `/evidence/CLM-003/`, `/readings/same-year-different-number/` × EN/AR × 1440/390 px);
  no horizontal overflow on any board at either width.
- On the canvas: version 3 of "YFIE D1 Thesis Exploration" holds all 48 boards — rows T1, T2, T3, T4 — regenerated from
  the committed composers (`design/exploration/d1_canvas/`).
- **Native-size inspection done** (`design/exploration/d1_canvas/inspect_widths.py t4`: 320, 360, 390, 430, 768,
  1024, 1280, 1440 px, EN and AR, plus 320 and 1440 at 2× DPI — 60 renders). Defects found and fixed in the composer
  before critique, each a design defect, none a content change:
  1. RV-CWR-001 panel 1 (the signature) was illegible: its SVG scaled down beside a 45 % label column, values unreadable
     at every width. Now: one HTML row per publication (label wraps and mirrors), the value on a horizontal zero-based
     axis drawn with percentage coordinates on an unscaled SVG (text stays at type size at 320 and 1440 px; no inline
     style, so CSP-safe for the reference); values printed above the marks; ticks 0 / 2,000 / 4,000 / 6,000. Panel 2
     lanes redrawn the same way; the panels stack (rows above, lanes side by side from 600 px).
  2. Between 900 and 1200 px the desktop grid (spine column plus a 220 px rubric column) starved the object column —
     Home at 1024 px was 60 % taller than at 768 px. Now: the spine column from 900 px, the rubric column only from
     1200 px; heights fall monotonically with width.
  3. The seven-question strip walled off the first screen on mobile (seven full-width chips before any content; nine
     on Home). Now: the strip follows the first answer on the Record and the boundary on the Reading; Home has no
     strip (its foot spine keeps the index); rubrics carry the same numbers as the index ("01 What does this evidence
     establish?").
  4. SVG value labels were emitted as HTML `<bdi>` inside `<text>` and never rendered (a formatter fault); the canonical
     link inside the Arabic figure broke across lines in mixed direction (now `dir="ltr"`, isolated); the product-bar
     actions wrapped into three lines at 1024–1440 px (now one line each).
  Residual: at 320 px the fallback table inside the closed text alternative is 8–14 px wider than the viewport and
  scrolls within its wrapper (page overflow 0). Canvas version 4 holds the revised T4.
- **Next, in this order:** the lens critique (§2.4) on the first-generation renders and T4 together; the adversarial
  tests (screenshot misuse, source owner, semantic firewall, Arabic-native, 320 px, low bandwidth, no image, genericity)
  on T4 against the strongest first-generation proposition; the convergence question ("what does YFIE now allow a user
  to understand or do that a conventional evidence website does not make nearly as easy?") answered from rendered
  evidence. Only then §3; only after §3 the Lock (§4).
- What T4 must prove, or be improved or replaced: that clock-first objects make currentness and population legible
  without conceptual overhead; that a crop of any object carries its clock and boundary; that the seven-question
  structure is learned once and does not feel bureaucratic; that Arabic reads as authored, not mirrored; that the
  spine does not slide into the documentation-portal pattern; that Home demonstrates "not one number" without becoming
  a dashboard.

### 2.6 Scaling test on paper — does the candidate's grammar reach the fixed sitemap? (27 September 2026)

The sitemap is fixed; the experience is not. Before convergence, each page family was checked against the T4 object
grammar (clock-first object · seven-question structure · boundary voice · verification spine · compact objects). This
is a paper test of reach, not a design of those pages (they belong to D2–D3); it exists so that a chosen direction is
not one that only works on the trio.

| Family | Carried by | Risk to resolve at its gate |
|---|---|---|
| Question Entry (`/explore/`) | the numbered question list of Home's section 9, whole page | none new; intensity lower than Home |
| Domain Answer (8) | one page-object per answer: clock → statement → scope → boundary → verify; bound visuals as figure objects; Measurement cards as compact objects | five visuals on `/payments/` — figures must stack as objects, never a chart wall; the WITHHELD figure is a bounded object with no value (missing ≠ zero) |
| Evidence Directory | compact objects as rows (clock first) with the governed search hooks | 110 rows: the clock line must not become noise — group by state or domain per the governed fields |
| Evidence Record (110) | the seven questions verbatim; records with fewer fields simply have fewer answers | composite / framing / thin records must not look weaker: the object is the same, the answers shorter |
| Comparison | compare slots as compact objects; the compatibility table as a figure object whose boundary row is the boundary voice | four columns at 320 px (EAD-06) — a recomposition, not a shrink |
| Reading index, Readings (10) | Reading page-object as on the trio; figures per contract tier (TABLE_TEXT_FIRST never a chart) | longest Reading — the spine index must stay usable at 40+ headings |
| Data & sources | source cards as compact objects with locator actions; the nine without locator never named | 151 cards: paging or grouping by `resource_category`, not a link wall |
| Measurement Agenda | priority objects (decision constrained / known / unknown / measurement that would change it) | must not read as a ranking; equal weight, no numbering that implies order |
| Trust and service (8), 404, search states | the page-object with the boundary voice unused; calm intensity | technical states must not look like evidence gaps and vice versa |

Conclusion of the paper test: no family requires a second grammar; two require a deliberate recomposition (Compare at
320 px; the Data & sources register). This does not decide convergence; the lens critique and the adversarial tests
do.

## 3. Comparison and convergence (27 September 2026)

### 3.1 How the critique was run

Nine independent reviewers, each given the same brief (`design/exploration/d1_canvas/LENS_BRIEF.md`: the product, the
firewall, the RV-CWR-001 contract, what each proposition claims, where the renders are, a fixed report format, no
scores, "T4 is a candidate, not the answer") and the same rendered evidence: first screens at 1440 and 390 px, whole
pages as tiles, the Record's primary crop and the figure crop for every proposition, and T4 at 320–1440 px. Lenses:
A senior evidence researcher · B Arabic editorial and RTL director · C accessibility and cognitive UX · D data
visualisation · E frontend architect · F high-end product-design critic · G journalist · H source-institution
statistician (CBY-Aden, IMF, World Bank) · I informed bilingual Yemeni professional. Reports are kept at
`design/exploration/d1_canvas/out/review/lens_*.md` (working material); what matters is recorded here.

Two process facts. (1) The T4 figure crops under `inspect/crops/` that five lenses cited for "values vanish at 320/390"
predated the value-label fix (§2.5, item 4); the current build prints every value at every width (verified: ten
`text.val` labels in the figure at 320, 390 and 1440 px, both languages). Those findings are recorded as stale, not
as defects. (2) Two lenses (A, C) checked T1's tile captions against `interface_copy.json`: governed
(UI-VIS-STATE-DERIVED, UI-VIS-DISAGREEMENT), so the T1 finding is about the lifted-figure component, not invented text.

### 3.2 What each proposition established, and what was materially rejected

- **T1 · Register** established the strongest apparatus: clock and ID as start-side marginalia that survive a crop in
  both scripts, a three-column when/what/for-whom register on Home, and the figure's tables inline so a screenshot
  carries the raw levels (A, D, H, I). **Rejected:** the apparatus that lifts "8.55 %" and "+11 %" out of the governed
  sentence as two display figures with grammar captions — every lens named it: the record's largest numerals become
  growth rates without period or object, the derived figure leads with a neutral tag and the source's figure follows
  with a fault tag (H: "the composition CBY-Aden would formally ask to be corrected"), and the phone's first screen
  ends on the tiles (G, C). Also: fixed 200/220 px side columns starve the statement between 900 and 1100 px (E);
  the Arabic margin splits ISO dates mid-token and the Arabic mobile table clips the IMF index column (B, H).
- **T2 · Argument** established the calmest reading and the best one-move quotation on the Record (period, universe,
  ID inside the primary crop) (A, G). **Rejected:** the grammar restyles a magazine masthead and a foundation long-read;
  six bold numerals in light text build a number-first scan path with the bound whispering (A, B, F, I); Plex Light
  on cream fails Arabic on cheap phones and in sunlight (I); values and records hidden behind disclosures; the
  figure's two unlabelled stacked dots read as a fall; the Arabic canonical link corrupts at every width (B, D, H).
- **T3 · Strata** established the clearest verification skeleton and the most scannable record on desktop (labelled
  strata, chips, tables in frame) (A, I). **Rejected:** the idiom — taupe ground, white cards, teal numbered caps, a
  right rail — is the knowledge-hub template a Yemeni reader recognises as "about Yemen, for donors" (I, F); the
  index chips precede the content on every mobile surface (C); the trail does not match the strata on the Reading
  (F); inline `grid-row` spans break strict CSP and flex `order` breaks focus order (E); the mobile tables clip the
  IMF column and, in Arabic, lose digits ("2025" → "25") (B, D, H).
- **T4 · Instrument** established: clock before claim in both scripts and sizes, surviving the crop; no lifted
  numeral — 8.55 % and +11 % stay a sentence, visible, not amplified; panel 1 as labelled rows on a zero-based
  horizontal axis with printed values, the only figure a screenshot cannot turn into a fall; the boundary as one
  second voice on every surface; the Arabic edition the only one that holds at 320 px with link and identifiers
  intact; a grammar that survives 320 px, CSP and the value-label bug without rework and is generated from data (E);
  Home's first screen is the evidence with its clocks, not an about-paragraph (F). Ranked first by all nine lenses,
  for different reasons; none called it finished.

**Rankings by lens (no scores):** A T4 > T1 > T2 > T3 · B T4 > T3 > T2 > T1 · C T4 > T2 > T3 > T1 · D T4 > T1 > T2 >
T3 · E T4 > T2 > T1 > T3 · F T4 > T1 > T2 > T3 · G T4 > T2 > T1 > T3 · H T4 > T2 > T3 > T1 · I T4 > T1 > T2 > T3.

### 3.3 T4 findings and the corrections applied (composer version 5, canvas version 5)

Material design moves, stated before they were made:

1. **Home demonstrates, per figure.** PROBLEM: paced sentence-blocks let "Areas holding about 23 %…" stand alone as a
   fourth figure and detached the coverage caveat from the 11.9 % it bounds (A, G); Home's first screen risked reading
   as six numbers deep (I). CONSTRAINT: the section-3 text is governed and must not be reworded or reordered; the
   records behind the figures are governed objects. HYPOTHESIS: pace the paragraph as *figure groups* (a new group only
   at the governed connectives that introduce another measure) and set each group's bounded record — clock, title,
   population, open — directly under it, so NUMBER + SCOPE + BOUNDARY + VERIFY is one object per figure; the
   resolution sentence stays set apart. PROOF: the 390 px Home first screen now reads figure → its clock and
   population → open record (`fold/T4-home-en-m.png`, `-2.png`); "23 %" sits inside the Findex group. AFFECTED:
   Home only. Escalated: a controlled pacing marker (`ESCALATIONS.md`), because the split points are found by wording.
2. **The figure carries its verification.** PROBLEM: marks were keyed inconsistently across panels (□ = AR 2025 in
   panel 1, ● = AR 2025 lane in panel 2: D, H); the "not comparable" divider sat between the panels, readable as "the
   two annual reports are not comparable" (A, D, H); the lanes' baseline at 95 named the origin only in the header
   (D); raw levels were hidden in a closed disclosure so a crop lacked them (A, D, H, I); the index printed "100.0/118.0"
   against the table's "100/118" (all). CONSTRAINT: contract rules — two lanes never on one axis, NOT_COMPARABLE on
   the lanes' levels, numeric value axes left-to-right in Arabic, text alternative shipped with every chart.
   HYPOTHESIS: one mark per publication in both panels (● AR 2024, □ AR 2025, ◎ IMF); the divider *between* the two
   lanes (vertical double rule on wide screens, a rule between the stacked lanes on phones); baseline at the origin
   100, labelled; each lane's raw 2021 level under its title so the 1.84× level gap sits beside the identical paths;
   the alt text and both tables visible under the frame; one number rule everywhere. PROOF:
   `crops/T4-reading-en-figure.png`, `-ar-`, and `inspect/crops/T4-reading-*-figure@320/390/1440.png`. AFFECTED:
   Reading figure (and the shared table helper — the "6245" fault fixed for all propositions).

Smaller corrections, each from a named finding: index without pills or fill — a numbered hairline list, two columns
from 600 px, a hairline column on desktop (F, C); weight discipline — semibold only for the first answer, the
boundary voice and the resolution (F); the record head cut to breadcrumb, rubric, clock, title (F); the seven questions
and the boundary as `h2` headings (C); axis and caption text in ink-2 at 12 px, not mute on plaster (C); hit areas
≥ 40 px on spine and index links (C); the Reading has no mobile strip — its index is the foot spine (C); the Home index
no longer lists the product name as a section (F, I); order-independent grid rules, the sticky spine capped at the
viewport, no inline styles left in the composer (E); ISO dates isolated as unbroken left-to-right runs (B, I);
balanced titles and row labels (B); "Cite this page" on the figure itself (G). **Kept against a finding, with the
reason:** the value axis stays left-to-right in Arabic (B asked for bars growing from the right) because the governed
contract says so ("numeric time and value axes stay left to right"); pacing by connectives stays for the proposition
and is escalated for the build (E). **Not in the composer, for the reference implementation:** skip link,
`:focus-visible`, labelled in-page navigation (a governed label is needed — `ESCALATIONS.md`), print rules,
absolute canonical URLs in exported frames.

### 3.4 Adversarial tests on T4 (after the corrections)

| Test | Result | Evidence |
|---|---|---|
| Screenshot misuse | Passes on the Record (clock, ID, whole statement in the phone's first screen; no lone number) and on the figure (publication-keyed rows with values; boundary, credit, link in frame). Residual: row labels "…Report 2024 / …Report 2025" can still be narrated as before/after — held off by "Same year, different publication" set above the rows | G, A, D, H; `crops/T4-record-*-primary.png`, `crops/T4-reading-*-figure.png` |
| Source owner | No source number typeset outside its sentence; both CBY-Aden values carry publication and value; credit in frame. Open: the Arabic credit is English (escalated); the IMF lane's state question (escalated) | H |
| Semantic firewall | Restatement ≠ fall (rows); coinciding paths ≠ confirmation (note under the lanes, raw levels beside them); infrastructure ≠ use (POS record's universe and boundary); people ≠ accounts (Findex group bound to its record); missing ≠ zero (no chart invented for the system visual) | A, D, H |
| Arabic-native | Composed with its own metrics; the only proposition whose Arabic survives every width without corrupting a link, clipping a table or splitting a date. Honest limit: "a disciplined mirror", not Arabic-first design — the Lock carries the Arabic rules as MUST PRESERVE | B, I |
| 320 px | No page overflow at any width; the fallback table scrolls inside its wrapper by 8–14 px at 320 px | `inspect_widths.py`, §2.5 |
| Low bandwidth / no image | Meaning and order survive with no stylesheet; identity survives with no image (name, rules) | §2.5 degraded tests |
| Genericity | Stripped of content, logo and name, the residue read as "statistics-office methodology page" with a documentation sidebar and pills (F); the sidebar fill and pills are removed in v5; the signature elements (question-first head, clock-first objects, boundary voice, row-form panel) "are copied from nowhere" (F). Yemen through materiality: none of the four propositions achieves it (F, I) — provisional, below | F, I |

### 3.5 The convergence question

*What does YFIE now allow a user to understand or do that a conventional evidence website does not make nearly as
easy?* Two behaviours, each named as material by several lenses from rendered evidence:

1. **Two published values for one reference year can be read, quoted and screenshotted as a restatement, not a
   fall** — publication-keyed rows on a zero-based axis with printed values, the boundary and credit in frame; the
   first-generation panels (stacked markers keyed by a legend) needed text to argue against the fall reading
   (A, D, F, G, H, I, C).
2. **A number is never met without its clock and its bound**: clock-before-claim objects make a phone screenshot
   self-citing (period, ID, whole statement), and the 8.55 % / +11 % disagreement stays a recorded inconsistency
   inside its sentence rather than a headline (A, C, G, H, I).

Narrower gains: the Arabic edition holds at 320 px with links and identifiers intact (B, I); one figure implementation
serves 320–1440 px without scaling text and without rework under strict CSP (E); Home's first screen is evidence with
its clocks (F). **Not material** (parity with the first generation): finding the source (three entries, one scroll,
in all four); the verification spine as a component (F: "the same footer link strip as T1"); "the seven questions
everywhere" — true of the Record only; Home and the Reading index their own sections (F, G).

### 3.6 Decision

**T4 · Instrument converges as the D1 design direction.** Not because the lenses rank it first, but because the two
behaviours above answer the convergence question with rendered evidence and no first-generation proposition can be
edited into them without becoming T4: T1's lifted apparatus and T2's bold-number scan are the opposite of "no number
outside its bound"; T3's chip-first mobile and card idiom are the opposite of "the answer first". T1's inline tables and
T3's labelled verification chips are not borrowed as a hybrid: the tables are the contract's text alternative made
visible, and the chips already existed in T4's verification voice.

Conditions carried into the Lock (§4) and the reference implementation: the v5 corrections must be verified in real
rendered code and by the Design review, not assumed from the canvas; the three escalations stay open and the
implementation renders governed strings as given; the Arabic rules and the number rule are MUST PRESERVE; the genericity
residue (sidebar, pills) is removed in v5 and re-tested in the implementation.

### 3.7 What remains provisional after convergence

- **Yemen felt, not themed.** No proposition achieved a material grounding (F, I). T4's grounding is by abstraction
  only — paper and plaster, the logo's three colours as roles, a discipline of rules. Whether proportion, rhythm and
  surface can carry Yemen without a theme is an open design question for the implementation and for D2+, recorded as
  DEBT-007; it is not a reason to withhold convergence (the convergence bar is evidence behaviour, not "more Yemen").
- **Arabic-first**, narrowed to "Arabic composed with its own metrics and verified first at 320 px" (B). Eastern
  versus Western digits: Western, because the governed Arabic copy uses Western digits (a rule to state, not a default).
- **Interaction** (search, cite, language, menu, disclosure) is untested on the propositions; it is proven only in
  the reference implementation with the baseline runtime.
- **Print and citation** are not designed in the propositions (§2.5 degraded tests); print basics are part of the
  implementation.
- **Scaling** beyond the trio is a paper test (§2.6) until D2.

## 4. Design Intent Lock

_Not yet written — after §3._

## 5. Foundational grammar

_Not yet written — extracted only from what D1 proves._
