# D1 — Theses and foundations

> STATUS: **D1 IN PROGRESS — §1 holds thesis HYPOTHESES (T1–T3 first generation, T4 second generation); §2 records
> the exploration so far; §3–§5 are not written.** Nothing in this file is an accepted Design decision until §3
> (comparison and convergence) and §4 (Design Intent Lock) are written after the independent critique, the native-size
> inspection and the rendered stress tests. No thesis is chosen. A hypothesis is a question put to the canvas, not an
> answer.

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
- **Not yet done, in this order:** native-size inspection of T4 in both languages at 320, 360, 390, 430, 768, 1024, 1280
  and 1440 px and at high DPI, with defects fixed in the composer; the lens critique (§2.4) on the first-generation
  renders and T4 together; the adversarial tests (screenshot misuse, source owner, semantic firewall, Arabic-native,
  320 px, low bandwidth, no image, genericity) on T4 against the strongest first-generation proposition; the convergence
  question ("what does YFIE now allow a user to understand or do that a conventional evidence website does not make
  nearly as easy?") answered from rendered evidence. Only then §3; only after §3 the Lock (§4).
- What T4 must prove, or be improved or replaced: that clock-first objects make currentness and population legible
  without conceptual overhead; that a crop of any object carries its clock and boundary; that the seven-question
  structure is learned once and does not feel bureaucratic; that Arabic reads as authored, not mirrored; that the
  spine does not slide into the documentation-portal pattern; that Home demonstrates "not one number" without becoming
  a dashboard.

## 3. Comparison and convergence

_Not yet written — after the canvas exploration, the critique and the rendered stress tests._

## 4. Design Intent Lock

_Not yet written — after §3._

## 5. Foundational grammar

_Not yet written — extracted only from what D1 proves._
