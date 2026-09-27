# Component catalogue

> STATUS: **seeded at D2 — the objects the hard families use, the figure anatomy and the evidence-state grammar.**
> Each entry answers the contract's questions (`handoff/DESIGN_TO_CODE_CONTRACT.md` §1) as far as the reference
> implementation proves them; tool states and keyboard paths are completed at D5, print and export forms at D6.
> Source of truth: `design/reference/yfie/render.py`, `families.py`, `visuals.py`, `theme.py` (tokens in
> `02_TOKENS.json`). Nothing here authors public text: every label named is a governed `UI-*` ID.

## 1. Objects

| Component | Governed inputs | States | 320 / 390 / 640 / 1440 | Arabic | Name, role, keyboard | Colour off, image off, forced colours | Fallback | Must stay visible |
|---|---|---|---|---|---|---|---|---|
| Page object `article.obj.page-obj` | Page Spec title, sections, bound objects | — | one column; grid with the spine from 900 px; rubric column from 1200 px | own type scale (`html[dir=rtl]` tokens) | landmark `main`; one `h1#page-title` | heavy ink rule at the start (border) | — | the head's clock and the boundary |
| Head | title, lead (heading-less section 1), the governed question (`UI-ANSWER-CRUMB-LABEL` rubric), record clock (`UI-EVID-WHEN-…`), crumb (`breadcrumbs`) | — | `h1` balanced; measure in `ch`/`em` | Arabic `h1` 30/42 px, no letter-spacing | crumb `nav` labelled `UI-CRUMB-BREADCRUMB`; the record ID isolated `bdi` | — | — | clock before claim |
| Answer `section.qa` | section role, heading, body | — | rubric above on narrow; rubric column from 1200 px | rubric weight + colour, no capitals | `h2` per answer with its ordinal in the rubric | hairline rules | — | — |
| Boundary `section.bnd` | a limit section, `does_not_establish`, `measurement_limitation`, a Reading's `prohibited_inference` | parts A and B (record) | full width; never collapsed | same rule and label | `h2` (record question 5; Reading "What not to conclude") | double rule + label + weight (colour is never alone; CanvasText in forced colours) | — | always first-load (`data-evidence-boundary-first-load`) |
| Compact evidence object `article.compact` | record `period`, `title`, `universe`, `summary` (where the page shows it), `does_not_establish`, route; `UI-EVID-OPEN-EVIDENCE-RECORD` | bound (Home), row (directory), verify (domain) | stacked; clock column from 1200 px | clock label/value on own metrics | link on the title and the open action (≥ 24 px) | hairlines | — | the clock |
| Measurement object (compact and full) | `measurement_agenda` fields, `UI-MA-*`, `UI-BLOCK-EVIDENCE-NEEDED`, `UI-MEASUREMENT-EXAMINED-IN` | compact (domain, Explore, hub); full (`/measurement/`, `id` = reference, `tabindex=-1`) | stacked | priority code isolated `bdi` | `h3` title; deep link `#MA-00x` | no ordinal numbering (non-ranking) | — | the missing evidence |
| Reading object | `readings.json` title, thesis, question, evidence period | featured, list, domain | stacked | — | link on title and open action | — | — | the evidence period |
| Source card `article.src` (record, Reading, register) | `source_reference_map` display fields, locator, `UI-SOURCE-*`, `UI-EVID-OPEN-*`, `UI-SRC-REUSE-*` | display-ready · untitled (locator-only: reference + locator, never a title) · curated (category, why it matters, boundary) · with dependents | actions wrap | title `dir=auto`, reference `bdi` | external link `rel=noopener target=_blank` with the governed "↗" label; copy reference `button` | — | — | the reference |
| Chronology object | `system_chronology` period, fact, relevance, does-not-establish, public sources; `UI-CHRONOLOGY-*` | — | stacked | period `bdi` | `li` with `id` = event ID | — | — | what it does not establish (boundary line) |
| Spine `aside.spine` (index + edges) and strip `nav.strip` | the page's own headings; governed edge headings | side (≥ 900 px, sticky, capped) · foot (< 900 px) · strip on the Record | exactly one visible | hairline on the reading-end side | `nav.index[aria-labelledby=page-title]`; each `nav.edges[aria-labelledby]` its `h3`; rows ≥ 40 px | rules only | — | — |
| Product bar, search dialog, institutional band | navigation contract labels; `UI-HEADER-*`, `UI-SEARCH-*`, `UI-FOOTER-*` | menu open/closed (< 900 px), dialog open/closed | as D1 | mirrored | hooks of brief §19 unchanged; dialog labelled by its title | — | — | trust links lead the band |
| Next actions `nav.actions` | `route_next_actions`, `UI-NEXT-*` | — | wrap | — | labelled by its `h2` | — | — | — |

## 2. The figure object `figure.fig` (every visual, every tier)

Anatomy, in order: rubric `UI-DOM-ANALYTICAL-QUESTION` · governed title (`h2`, `h3` inside an answer) · question · scope
(period · universe) · **panels** · in-frame notes (`frame_labels`) · foot: `UI-VIS-DOES-NOT-ESTABLISH` + the prohibited
inference, `UI-VIS-SOURCE` + the credit as an isolated left-to-right run (the contract's `credit.language_note`; omitted
when the contract has none), `UI-VIS-FULL-RECORD` + the canonical link (absolute once the origin is set), cite · **text
alternative** (`.alt[data-visual-fallback=ordered-text]`): `UI-VIS-WHAT-THE-EVIDENCE-SHOWS` + alt text, `UI-DOM-SCOPE-AND-TIME`,
`UI-DOM-WHAT-NOT-TO-CONCLUDE` + the prohibited inference, the contract's table in a focusable `.table-wrap` · `figcaption.sr-only`.
Attributes: `data-visual-id`, `data-visual-fallback`, `data-image-independent`, `data-noncolour-semantic`. SVGs: percentage
x-coordinates, no `viewBox`, `direction="ltr"`, `aria-hidden` (the text alternative is the accessible content), no inline style.

| Form (D2) | Contract(s) | Panels | Value labels | Narrow form |
|---|---|---|---|---|
| Rows on a horizontal zero-based axis (D1) | RV-CWR-001 | publications as rows; two indexed lanes with the not-comparable divider | printed | rows stack; lanes stack |
| Bars with bracket gaps | VIS-FINDEX-GAPS | one bar per governed group from zero; each governed derived gap printed as a bracket line (never a bar) beside its pair; a row prints its own unit where it differs | at the bar end | label above its track (< 600 px) |
| State-keyed time series | VIS-REMITTANCE-MACRO; VIS-POS-TERMINALS / -TRANSACTIONS / -VALUE (a three-panel small multiple, separate value axes) | one line per series; marks by evidence state; break never joined (double rule, note); missing x a labelled dotted gap; disagreement ringed with the record's method text as the note; NOMINAL on the axis title; a key of states with their x-range and source document | every point; on a series of more than eight points on two rows, and below 600 px only the first, last, marked and state-change points (the table carries all) | full width; alternate x labels hidden below 600 px |
| Dot rows | VIS-REMITTANCE-COST | corridor lanes; one row per governed send amount; marks keyed by amount | above the mark | rows stack |
| Object list | VIS-PAYMENT-ANATOMY | one object per governed measurement object: label, value or the WITHHELD label, its governed "is not" line, marker labels; no totals | — | stacked |
| Chain ladder | RV-CWR-009 (full); VIS-PAYMENT-RAILS (SUPPORTING: the same governed event set, no values) | the seven governed steps top to bottom; EVIDENCED steps list their dated events with a locator; OPEN steps carry `UI-VIS-CHAIN-OPEN`; the first open step after the evidenced ones is set in the boundary voice (where evidence stops) | — | native vertical list |
| Text frame | every SUPPORTING and TABLE_TEXT_FIRST contract without a drawing | the governed text alternative only | — | — |

Tables: caption = title — period — universe (— unit); scoped headers; the value column headed by the governed unit
label; other columns unheaded where no governed column label exists (escalated); every value formatted by the one
number rule (precision as governed, thousands separators, years unseparated, isolated left-to-right).

## 3. The evidence-state grammar (`visual_design_contracts.json` → `grammar`; labels `UI-VIS-*`)

| Token | Governed label ID | Mark | Line | Label rule | Drawn (D2) | Status |
|---|---|---|---|---|---|---|
| MEASURED | UI-VIS-STATE-MEASURED | filled | solid | on the panel | VIS-FINDEX-GAPS, VIS-REMITTANCE-COST | VERIFIED |
| REPORTED | UI-VIS-STATE-REPORTED | filled | solid | keyed | RV-CWR-001, VIS-REMITTANCE-MACRO | VERIFIED (D1, D2) |
| ADMINISTRATIVE | UI-VIS-STATE-ADMINISTRATIVE | filled square | solid | on the panel | POS panels, VIS-PAYMENT-ANATOMY | VERIFIED |
| DERIVED | UI-VIS-STATE-DERIVED | bracket or annotation, never a bar | none | value + the governed word | RV-CWR-001, VIS-FINDEX-GAPS | VERIFIED (D1, D2) |
| ESTIMATED | UI-VIS-STATE-ESTIMATED | hollow | none or dotted | keyed | VIS-REMITTANCE-MACRO | VERIFIED |
| PROJECTED | UI-VIS-STATE-PROJECTED | hollow | dashed | keyed | VIS-REMITTANCE-MACRO | VERIFIED |
| BREAK_VINTAGE | UI-VIS-BREAK-VINTAGE | double rule between the points | not joined | note line | VIS-REMITTANCE-MACRO | VERIFIED |
| MISSING | UI-VIS-MISSING | dotted gap | not joined | note line | VIS-POS-VALUE | VERIFIED |
| DISAGREEMENT | UI-VIS-DISAGREEMENT | ring around the mark | — | note line + the record's method text | POS terminals, transactions | VERIFIED |
| NOMINAL | UI-VIS-NOMINAL | — | — | axis title | VIS-POS-VALUE | VERIFIED |
| WITHHELD | UI-VIS-WITHHELD | no value | — | the label in place of the value | VIS-PAYMENT-ANATOMY | VERIFIED |
| NOT_COMPARABLE | UI-VIS-NOT-COMPARABLE | divider / marker label | — | label | RV-CWR-001, VIS-PAYMENT-ANATOMY | VERIFIED (D1, D2) |
| SAME_YEAR_REVISION | UI-VIS-SAME-YEAR-REVISION | — | — | set above the rows | RV-CWR-001 | VERIFIED (D1) |
| HISTORICAL | UI-VIS-STATE-HISTORICAL | as its state, period printed, no fading | — | — | no contract row carries it | DESIGNED |
| PROGRAMME | UI-VIS-STATE-PROGRAMME | outlined mark in a labelled programme frame | none | universe printed | none | DESIGNED |
| PARTIAL | UI-VIS-STATE-PARTIAL | as its state | — | direct label | none | DESIGNED |
| UNKNOWN | UI-VIS-STATE-UNKNOWN | no mark (never zero) | none | direct label | none (the `/access/` frame carries the governed prose) | DESIGNED |
| BREAK_UNIVERSE | UI-VIS-BREAK-UNIVERSE | as BREAK_VINTAGE | not joined | note line | none | DESIGNED |
| TARGET / RESULT | UI-VIS-TARGET / UI-VIS-RESULT | labelled cells of a three-row table | — | labels | none (VIS-TARGET-RESULT-STATE has no rows — escalated) | DESIGNED |
| CHAIN-* | UI-VIS-CHAIN-RULE … OUTCOME, EVIDENCED, OPEN | ■ evidenced / □ open step | rail | step label + state | VIS-PAYMENT-RAILS (RV-CWR-009 at D6) | VERIFIED |

Colour is never the only carrier; nothing fades with age; no red, amber or green anywhere.

## 4. Tools (the baseline runtime `site-src/app.js`, unchanged; states and keyboard paths completed at D5)

| Tool | Components and hooks | D2 state |
|---|---|---|
| Search | product-bar button → `dialog#search-dialog`; the directory's inline `#global-search` with `[data-search-status]` and `#search-results[aria-live]` | rendered; results, no-match, unavailable and Measurement anchors pass `test_public_tools.py` |
| Compare | `select#compare-a…d` with governed labels, `[data-compare-copy]`, `#compare-status`, `#compare-output` (verdict in the boundary voice, table in a named region, boundaries, record links), `yfie-compare`, `yfie-compare-dimensions`; entry from each comparable record (`[data-compare-entry]`) and from a Reading's trace | rendered; URL state, errors, duplicates, language switch pass |
| Source register | `[data-source-filter]`, `[data-source-filter-status]`, `[data-source-no-results]`, `[data-source-record]#source-<ID>[tabindex=-1]`, `.source-locator-details`, `[data-source-cite]` | rendered; deep link, unknown link, no-match pass |
| Cite, report, corrections | `meta[name=yfie-citation]`, `.evidence-cite-button`, `[data-correction-context]` with `yfie-record-ids`, the mail action revealed for a known record | rendered; pass |
| Language switch, menu | `[data-lang]`, `[data-menu]` | as D1 |

## 5. Exceptions (recorded, `09_CODE_HANDOFF.md`)

- The governed source intro (`UI-EVID-OPEN-THE-SOURCE-RECORD-HERE`) is not printed on a framing record (no source to open).
- Chart fallback tables head only the value column (the governed unit label); the other headers wait for governed labels.
- Dense series hide most value labels below 600 px; the table carries every value.
