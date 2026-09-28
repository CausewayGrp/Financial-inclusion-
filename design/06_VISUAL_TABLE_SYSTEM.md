# Visual and table system

> STATUS: **D6 — every one of the 36 governed visual contracts rendered in its tier's form on its canonical route and
> on every public route that binds it, in both languages, with its detached frame, its text alternative and its
> fallback table; the portable forms (export frames, social-image templates) and the print system built and asserted.**
> What is asserted is asserted by `design/reference/check_visuals.py` (contract by contract, five phases: contracts,
> degraded, frames, print, text); what is a design decision is recorded here and in the decision log (`00_DESIGN_README.md`,
> DL-D6-*). Source of truth: `design/reference/yfie/visuals.py` (the drawers, the frame, the tables),
> `design/reference/yfie/frames.py` (the portable frames), `design/reference/yfie/theme.py` (`CSS_D6`: the D6 forms,
> the portable frames, the print system), `design/reference/yfie/content.py` (`visual()`: everything a drawer may bind).
> Nothing here authors public text: every word a figure prints is a governed field, a governed `UI-VIS-*` grammar label,
> a URL or the edition; where a label does not exist the feature waits or shows the development placeholder
> (`⟦NCC:key⟧`, brief §10), never invented wording.

## 1. The 36 contracts and the form each takes

The contract (`site-src/content/visuals/visual_design_contracts.json`) decides the tier; the tier decides what may be
drawn; the rows decide what is drawn. A SIGNATURE or CORE_ANALYTICAL contract with resolved rows is drawn in full. A
SUPPORTING contract plots no value: it is the governed text, or a non-quantitative diagram built only from governed
words and grammar labels. A TABLE_TEXT_FIRST contract is never a chart: the governed ordered text, or a table where the
contract resolves rows (none does today — the rows are requested Master-first, `ESCALATIONS.md`). The RETIRE contract
is never drawn and has no figure on its record. The canonical route of a `VIS-` contract is its own record page; the
same figure appears on the public routes the Page Specs bind.

| Contract | Tier | Form (§3) | Canonical route · public route |
|---|---|---|---|
| RV-CWR-001 | SIGNATURE | rows on a zero-based axis + two indexed lanes with the not-comparable divider (D1) | the Reading *Same year, different number* |
| RV-CWR-009 | SIGNATURE | the chain (seven steps, dated events with locators, the POS activity, the first open step in the boundary voice) | the Reading *From rail to result* |
| VIS-PROVIDER-OBSERVABILITY | SIGNATURE | **the provider matrix** (D6; waits at D7 — built, unshipped until its six labels are governed, DL-D7-001: the contract renders as its text frame, §5) | its record · `/providers/` |
| VIS-FINDEX-GAPS | CORE | bars from zero with bracket gaps (D2) | its record · `/people/` |
| VIS-REMITTANCE-MACRO | CORE | state-keyed time series with the vintage break (D2) | its record · `/remittances/` |
| VIS-POS-TERMINALS / -TRANSACTIONS / -VALUE | CORE | the small multiple: three panels, three value axes (D2) | their records · `/payments/` (depth) |
| VIS-REMITTANCE-COST | CORE | dot rows by corridor and send amount (D2) | its record · `/remittances/` |
| VIS-PAYMENT-ANATOMY | CORE | object list, WITHHELD in place of a value (D2) | its record · `/payments/` |
| VIS-FIRM-CONSTRAINTS | CORE | **bars from zero without rank numbers** (D6) | its record · `/firms/` |
| RV-CWR-004 | CORE | **three dated lanes on one time axis** (D6) | the Reading *Reforms newer than people evidence* |
| VIS-PAYMENT-RAILS | SUPPORTING | the chain as a state diagram, no values (D2) | its record · `/reforms/` |
| RV-CWR-002, -003, -005, -006, -007, -008, -010 | SUPPORTING | text frame (§5) | their Readings |
| VIS-E-MONEY-RULE-STACK, VIS-FCP-REDRESS-PATH, VIS-FL-EVIDENCE-LADDER, VIS-EVIDENCE-CLASS-LADDER | SUPPORTING | text frame | their records · the domain or directory page |
| VIS-FIRM-FINANCE-PATH, VIS-FIRM-FINANCE-SEVERITY, VIS-MFI-DIVERGENCE, VIS-TARGET-RESULT-STATE, VIS-INCLUSION-TRANSMISSION, VIS-EVIDENCE-FRESHNESS, VIS-EVIDENCE-GAPS, VIS-OECD-FCP-TIMELINE, VIS-MECHANISM-METRIC-BRIDGE, VIS-ACCESS-EVIDENCE-LAYER | TABLE_TEXT_FIRST | text frame (rows requested where the rationale describes a table) | their records or pages |
| VIS-SOURCE-COMPARISON | TABLE_TEXT_FIRST | the Compare tool itself carries it (its alt text as the standfirst, its prohibited inference as the boundary before the controls, D2/D4); a text frame on its record | its record · `/evidence/compare/` |
| VIS-CAPITAL-CONTEXT | RETIRE | never drawn; its record has no figure; `/reforms/` keeps the baseline's governed text frame for parity | its record · `/reforms/` |

Why the SUPPORTING and TABLE_TEXT_FIRST contracts stay text frames (DL-D6-001): none resolves a row, and none has a
governed vocabulary for the rungs, layers or steps its rationale names (VIS-FL-EVIDENCE-LADDER's three kinds of
evidence, VIS-E-MONEY-RULE-STACK's rules, VIS-INCLUSION-TRANSMISSION's relationships are English prose in
STRUCTURE-role or REFERENCE-role files that the reference may not read). A diagram would have to author its labels.
VIS-PAYMENT-RAILS is the exception because its rationale asks for RV-CWR-009's governed event set and the chain
labels exist (`UI-VIS-CHAIN-*`).

## 2. The detached frame (every figure, every tier)

The frame is what travels: on the page, in the export frame, in print, and — as far as its governed lines go — on the
social card. In order: the rubric (`UI-DOM-ANALYTICAL-QUESTION`) · the governed title (`h2`; `h3` inside an answer) ·
the governed question · the scope line, period · universe · the panels · the in-frame notes (`frame_labels`, the
state key, the marker lines, the record's measurement limitation where the contract carries one) · the foot:
`UI-DOM-WHAT-NOT-TO-CONCLUDE` + the prohibited inference, exactly once per frame; `UI-VIS-SOURCE` + the credit as an
isolated left-to-right run (the contract's `language_note`; omitted where the contract has none); `UI-VIS-FULL-RECORD`
+ the canonical link; the edition (`UI-CONTENT-VERSION`); the cite control (screen only) — each separator bound to the token after it, so no dot
ends a line. Then the text alternative (§4) and the `figcaption`, the governed title (the figure's accessible name; the
alternative is its description). A text frame prints the same foot under its governed description. The figure's inner
headings sit one level under its title.

What the frame never does: print a number outside its governed sentence or row; print a value the contract withholds;
join a break; draw a missing period as zero; share an axis, a row or a lane between unlike series; carry meaning by
colour alone (no red, amber or green anywhere; forced colours asserted). Every SVG is `direction="ltr"`,
`aria-hidden`, percentage-coordinate, without a `viewBox` and without inline style (strict CSP).

## 3. Drawing forms

| Form | Contract(s) | What is drawn | Narrow form (320–599 px) | Never |
|---|---|---|---|---|
| Rows on a zero-based axis; two indexed lanes | RV-CWR-001 | one row per publication with the printed value, the REPORTED state in the panel head and the governed same-year marker between the two rows (the contract puts the break between the two values, so a crop of the rows never reads as a fall); the two indexed paths as separate lanes, each with its own index unit and DERIVED state, the governed not-comparable label between them, each lane's raw 2021 level beside it; one filled mark per publication across panels (● ■ ◆ — hollow is reserved for the state grammar) | rows stack; lanes stack | one axis for the two raw series; a hollow mark |
| Bars from zero with bracket gaps | VIS-FINDEX-GAPS | one bar per governed group; each governed derived gap as a bracket beside its pair (never a bar) | label above its track | a gap drawn as a bar |
| State-keyed time series | VIS-REMITTANCE-MACRO; the POS small multiple | marks by evidence state (filled reported/administrative, hollow estimated/projected, square administrative), a dashed projected segment, the vintage break as a double rule never joined (its note names the period before and the period after, never an arrow), a missing period as a labelled dotted gap, a disagreement ringed with the record's method text, NOMINAL on the axis title, a key of states with their x-range and source document; where the state changes, each state's governed label on the panel above its segment; the plot inset from the axis, the first and last labels starting and ending at their marks, a label beside a break on its own side, every value label on the first of three rows above its mark (12, 26, 40 px) at which its ink keeps clear of every earlier label it could touch — judged on the narrowest panel of each regime, the state labels placed first as obstacles (`place_label`; asserted `labels_clear` at 320, 390, 600 and 1440 px and in every export) | the odd x labels hidden under 700 px of figure width, all but the first, middle and last under 480 px, and the on-panel state labels under 480 px (the key directly under the plot carries them); a series of more than eight points prints its first, last, marked and state-change values — the table carries every value (DL-D6-005) | joining across a break; a shared value axis across panels; an arrow between two numbers |
| Dot rows | VIS-REMITTANCE-COST | corridor lanes; one row per governed send amount; filled marks keyed by amount | rows stack | a line between corridors |
| Object list | VIS-PAYMENT-ANATOMY | one object per governed measurement object: its label as governed (never case-transformed), value or the WITHHELD label, the governed period and state on every card, its governed "is not" line, marker labels | stacked | a total, a share, a combined score |
| The chain | RV-CWR-009 (full), VIS-PAYMENT-RAILS (no values) | seven governed steps top to bottom; evidenced steps list their dated events with a locator; the first open step set in the boundary voice; RV-CWR-009 adds the governed POS activity rows | native vertical list | an arrow of flow; a completion reading |
| **The provider matrix** (D6; waits at D7 — built, unshipped until its six labels are governed, DL-D7-001) | VIS-PROVIDER-OBSERVABILITY | one row per provider class — banks; exchange and remittance providers; e-wallets; non-bank microfinance; and payment-system operators, the contract's known gap, always drawn as UNKNOWN in every dimension with the three institution events as context (its class label a placeholder until governed) — five self-labelled cells in the contract's order — issuing authority or source, dated universe or count, dated status decisions grouped by state with their dates as source-record links (each named by the date it shows, then the record), negative authority, evidence of operation — each cell governed words and dates, never a dot or a bar; the governed time boundaries as the Master holds them ("observed 2026-09-07"), isolated and marked English; a dimension without a governed row prints `UI-VIS-STATE-UNKNOWN` ("Unknown — not zero"); the roster count by category (never a total of providers), the wallet counts listed by date and wording (never one number), the `>9` participant count as governed; each class ends with its governed limit line in the boundary voice; the issuer-scope note (`UI-VIS-ISSUER-SCOPE`) closes the panel | one or two cells per row by container width (≥ 480 px) | a share, a market size, a confidence score; a list read as operation; a class hidden because its label is pending |
| **The dated lanes** (D6) | RV-CWR-004 | three lanes on one left-to-right time axis, padded at both ends so no mark sits on an edge: the people lane as the governed fieldwork span (the ISO dates inside CLM-001's governed period, the whole period printed beneath) with the account-ownership value and its survey state; the infrastructure lane as monthly dated presence with the first and latest governed values labelled (outside the span when it is short); the institutions lane as dated event marks keyed to the list beneath (events closer than 4 % of the axis share one bracketed key), each event with its locator; the outcome as an open node in the chain vocabulary, its state beside the heading; the governed not-comparable label between lanes; no lane has a value axis | under 600 px the strips are hidden and the lanes are their dated lists — the contract's "dated vertical list" | reading the sequence as cause; a value axis; joining the survey point to the infrastructure line |
| **Bars without ranks** (D6) | VIS-FIRM-CONSTRAINTS | horizontal bars from zero in the contract's descending order, the value at the bar's end, no ordinal, the survey state on the panel; the record's governed measurement limitation (multiple responses; the base not held) as the frame's note | label above its track | a rank number; a sum of the bars |
| Text frame | every SUPPORTING and TABLE_TEXT_FIRST contract without a drawing | the governed description as the body; the scope line; one boundary in the foot | — | a diagram with authored labels |

## 4. Tables — the text alternative and its fallback table

Every figure carries `.alt[data-visual-fallback="ordered-text"]`: the heading `UI-VIS-TEXT-ALTERNATIVE`,
`UI-VIS-WHAT-THE-EVIDENCE-SHOWS` + the governed alt text, `UI-DOM-SCOPE-AND-TIME` + period · universe, and — for a
drawn contract — the fallback table inside a focusable region named by the heading and the title
(`div.table-wrap[role=region][aria-label][tabindex=0]`), then `figcaption.sr-only`. A text frame's description is its
visible body (D3).

The table pattern (D6, `visuals.table`, closes DEBT-010 and narrows DEBT-013):

- **Caption** = title — period — universe — the unit, and every qualifier that holds for every row (evidence state,
  source document, a marker every object carries).
- **Columns**: the row header (period, group, object, lane, step, or `UI-VIS-SOURCE` where the rows are publications)
  — its column never narrower than 7 em, so a placeholder heading that may break anywhere cannot squeeze it to one
  word — and the value column headed by the governed unit label; a qualifier that varies between rows (state, marker,
  document, a boundary line) travels in the value's own cell after the middle dot. Every data column is named by a
  governed string — `table()` refuses an unnamed data column; the corner cell above a row-header column may be empty.
  The chain and the lanes head their second column with `UI-VIS-WHAT-THE-EVIDENCE-SHOWS`; the matrix table heads its
  five columns with the same five headings as its panel (placeholders until governed).
- **Cells**: numbers through the one number rule (`plain_num`, isolated left-to-right, unbroken); a value whose unit
  opens with "%" carries the sign inside its isolate ("11.9%", as the prose writes it — separated, the sign lands on
  the wrong side after Arabic letters); an identifier isolated, breaking only at its own hyphens; every ISO date and
  numeric range in any text isolated unbroken by the document pass (`text.isolate_document`); a list inside a cell
  joined by the edition's punctuation (";" and "," / "؛" and "،"); a purely numeric cell is `td.num`; a missing period
  prints its governed marker; a withheld object prints the WITHHELD label; a marker row (`SAME_YEAR_REVISION`) spans
  the table.
- **Row groups** (`grouped_table`): rows that share a unit or a state of their own sit in a `tbody` opened by a
  row-group header — the FINDEX gaps under "Percentage points · Calculated here from published figures" with the pair
  as the row header; the lanes of RV-CWR-004 under their lane labels with the date as the row header.
- **The matrix**: one two-column table per class (the five dimension headings as row headers, the class in the
  caption, the fifth class under its placeholder), the same words as the cells; no table is declared wide.
- **Width**: two or three columns fit 256 px (the column at 320 px) in both languages — every fallback table of the
  drawn contracts (thirteen at D6; twelve draw at D7 while the matrix waits) fits without scrolling, so no region is a tab stop (`tabindex` only when a table is declared
  wide, and none is). `check_visuals.py` fails a table that scrolls without the declaration.
- **Print**: `thead` repeats on every page, rows never break inside.

## 5. Text frames

A SUPPORTING or TABLE_TEXT_FIRST contract without a drawing renders `figure.fig.fig-text`: rubric, title, question,
the governed description as the body (its heading kept in the accessibility tree only, D3), the scope line, the foot
(§2). The Compare page carries VIS-SOURCE-COMPARISON as the tool (its alt text as the standfirst, its prohibited
inference as the boundary before the controls); its record page carries the text frame. VIS-CAPITAL-CONTEXT's record
page has no figure. Rows for the TABLE_TEXT_FIRST contracts whose rationale describes a table are requested
Master-first (`ESCALATIONS.md`, D2 and D6); with rows, VIS-TARGET-RESULT-STATE becomes the three-row table with the
governed TARGET and RESULT markers (designed, `03_COMPONENT_CATALOG.md` §3).

## 6. The evidence-state grammar at D6

`03_COMPONENT_CATALOG.md` §3 is the ledger. D6 draws two more tokens: UNKNOWN (the matrix cell, never zero, never
"none exist") and the full CHAIN-* set with values (RV-CWR-009). PARTIAL is carried by governed prose in the matrix
(network membership, not the whole sector), not as a mark. HISTORICAL, PROGRAMME, BREAK_UNIVERSE, TARGET and RESULT
still have no contract row and stay designed only.

## 7. Print

One stylesheet, `@media print` (`theme.CSS` D1 rules, `CSS_D2`, and the D6 print system that corrects them):

- **Chrome gone**: navigation, controls, dialogs, the skip link, the strip, the side index, the footer link groups, the
  cite buttons. The product bar keeps the mark (32 pt) and the product name, unwrapped. Every external locator prints
  its target on its own left-to-right line under its text (source cards, the chain, the keyed events — inline, a URL
  in an Arabic paragraph continued at the far right of the next line); the canonical link prints as text.
- **Provenance survives** (`render.print_foot`): every page ends with product · edition · canonical URL and the
  citation the cite action copies (the record's governed citation; otherwise title — product — canonical URL). It is
  the last element of the document (inside the footer, after the fine print) and is shown in print only.
- **Page breaks**: the page object and its answers break freely (the D1 rule that kept the whole object together began
  every printout on its second page — corrected at D6, asserted by `check_print`: the title is on page one of every
  family route in both languages); an object that fits a page (compact object, source card, object card, matrix row,
  lane, chain step, pair, head, figure title, caption) avoids a break inside; the head's boundary stays with the head,
  but a boundary after an answer no longer pulls the break into that answer, and a run of boundary sections — the
  domain answer's band — is not one unbreakable chain; a long boundary breaks between its paragraphs, never inside one;
  paragraphs keep three lines together at a break; a figure keeps its head, panels and foot together and lets its text
  alternative break; a depth figure stays with its rubric; a list panel taller than a page (matrix, chain, anatomy,
  dated lanes) breaks between its items; headings and rubrics never end a page; table headers repeat; the search
  block of the directory does not print (its control cannot).
- **Ink**: every mark, bar, line, grid, break rule, gap, ring, rule, border and boundary in black; the paper and plaster
  surfaces dropped; the double rule kept for every boundary; dense value labels restored on the time series. The D1
  print rules that D6 restates are gone: one print system, the last block of the stylesheet.
- **The Reading as a document**: title block (rubric, question, title, thesis, the two clocks), the boundary before
  the essay, the essay at full measure with its figure and frame, the trace, the sources, the citation block.
- **Families**: one route per family is printed to PDF (A4) in both languages by `check_visuals.py --phases print`
  and the first pages rasterised into `design/evidence/d6/print-*.png`.

## 8. Export frames and the export control

`frames.export_document` writes `out/_export/<visual>__<lang>.html` for every contract that draws, in both languages
(thirteen at D6; twelve at D7 — a drawer whose labels wait has no export frame until it draws, `visuals.draws`):
one box under a heavy rule — the identity line (mark 32 px · product · edition) inside it, the figure with its complete
detached frame at 800 px on the paper surface, a closing rule under the foot (a trim above the boundary shows a cut);
no cite control, no text alternative (the canonical link leads to it), no script, no inline style.
Asserted: the frame lines present, no overflow, the identity line, the logo unaltered.

The export **control** (an action in the figure's foot beside cite: image or the governed data table) is designed and
unshipped: its labels and states (unavailable · licence · file format) are not governed (`ESCALATIONS.md`, D6), and
every CauseWay-content download ships disabled until OWN-04. Its frame is the export document above; when it ships,
the control offers exactly that document and the table of §4, never a crop.

## 9. Social-image templates

`08_ASSET_MAP.md` §4: five templates (record, Reading, domain answer, product, hub) built from governed text only; the
286 frames written by the build and asserted to fit 1200 × 630 with title, canonical link, edition and the unaltered
mark. A record's card always carries its dates and its boundary; a Reading's its evidence period and prohibited
inference; a domain answer's the first-screen figure's boundary. The reference site keeps Open Graph without image;
Code adds `og:image` when it rasterises the templates at build time.

## 10. Verification (`design/reference/check_visuals.py`)

Five phases, exit 1 on any failure, record in `out/_review_visuals.json`; run on the final tree of this gate:

- **contracts** — for each of the 36 contracts × EN/AR × every route that binds it: the tier rule on the DOM (drawn
  with every governed value printed and every marker labelled, a WITHHELD value never printed; a SUPPORTING contract
  plots no value; a TABLE_TEXT_FIRST contract is never a chart; the RETIRE contract never drawn); the frame lines
  (title, question, scope, the boundary once, the credit isolated, the canonical link, the edition); the text
  alternative with the governed alt text; for a drawn contract the table with a caption, scoped headers, every data
  column named, in a named region; no inline style; every SVG left-to-right; only the palette's colours; the
  no development placeholder anywhere on the site (D7; at D6 exactly the escalated set, inside the matrix only); no two text labels of a drawing meeting (`labels_clear`, by ink boxes); at
  320 and 390 px (and 600 px for a drawn contract) the figure inside its column on both edges, no page-wide scroll,
  no scrolling plot, no table scrolling unless declared wide. The Compare page is asserted as the tool.
- **degraded** — forced colours (every mark and label takes the system colour) and print (the frame foot stays, the
  cite control goes, the provenance block appears) on the drawn contracts × EN/AR (thirteen at D6, twelve at D7).
- **frames** — every export frame (26) and every social frame (286).
- **print** — one route per family × EN/AR printed to PDF: chrome hidden, the provenance block with canonical URL,
  citation and edition, every figure whole with its boundary, the title on the first page.
- **text** — every built document's `<main>` and every export and social frame scanned statically: no ISO date or
  numeric range outside a `dir="ltr"` isolate (the renderer's own expression, `yfie.text.LTR_RUN`, shared with the
  in-browser checks; SVG, script and style content aside).

Results on the final D6 tree: 36 contracts × EN/AR on every binding route, 2,856 contract assertions; 52 forced-colours
and print checks on the thirteen drawn contracts; 26 export frames; 286 social frames; 133 print checks on the eleven
family routes × EN/AR; 598 documents and frames scanned for loose runs; 0 failures (`00_DESIGN_README.md` DL-D6-006;
`COVERAGE.csv`, the `evidence` column of the D6 rows).
Evidence: `design/evidence/d6/` — figure crops of the thirteen drawn contracts at 1440 px in both languages, the D6
forms at 390 px, export frames of the signature figure and the three D6 forms, the social cards of the eleven family
routes, and the first print pages of every family route in both languages.

Results on the D7 checkpoint tree (the same five phases; the matrix waiting as a text frame, DL-D7-001): 36 contracts ×
EN/AR on every binding route, 2,812 contract assertions (a waiting contract is asserted as a text frame with no chart
and no value, and no placeholder anywhere on the site); 48 forced-colours and print checks on the twelve drawn
contracts; 24 export frames; 286 social frames; 133 print checks on the eleven family routes × EN/AR; 596 documents
and frames scanned for loose runs; 0 failures (`10_ACCEPTANCE_CHECKLIST.md` F, F2; `COVERAGE.csv`, the D7 evidence).

## 11. Red-team record (D6)

Five independent lenses reviewed the built figures, frames and print pages before the final verification run: a
measurement expert with a statistician (semantic firewall), an information-visualisation expert with an editor (form,
legibility, genericity), a native Arabic editor (composition and terminology), a journalist with a hostile source
owner (screenshot misuse, portable evidence), and an accessibility specialist with a frontend engineer (DOM, CSS, print,
code). The Arabic lens read the corrected tree last. Their findings and every disposition are in DL-D6-007; content
and terminology observations are in `ESCALATIONS.md` (D6), never fixed in design; the one runtime defect found (the
Compare table's reversed dates) is recorded there for Code.

## 12. What this gate does not claim

No WCAG conformance, no assistive-technology testing with people, no native-language certification, no rights
clearance for the mark's derivatives, no social image shipped (Code rasterises), no export shipped (OWN-04), and no
number anywhere that is not a governed row.
