# Responsive, RTL and LTR — the implemented rules

Status: **written at D7 from the reference implementation as built** — `design/reference/yfie/theme.py` (the one
stylesheet: `CSS` + `CSS_D2` + `CSS_D6`), `design/reference/yfie/text.py` (the text layer) and `design/02_TOKENS.json`
(the roles and values). Nothing here is a new decision: every rule names the code that carries it and the check that
asserts it, and the decisions behind the rules are in the decision log (`00_DESIGN_README.md`, DL-D1-006/007,
DL-D2-003, DL-D3-002, DL-D5-003, DL-D6-003/004/005, DL-D7-002). Where this file and the stylesheet ever differ, the
stylesheet is the built truth and this file is corrected. Code implements from this file, `02_TOKENS.json` and the
component catalogue; it does not estimate a value from a screenshot.

## 1. Widths and breakpoints

The reference is composed mobile-first: the base rules are the 320 px composition and each `min-width` block adds one
thing. The four review widths (brief §9) are 320, 390, 640 and 1440 CSS px; 320 stands for 400 % zoom of a 1280 px
window and 640 for 200 % (`07_INTERACTION_ACCESSIBILITY.md` §3).

| Breakpoint | What changes | Stylesheet |
|---|---|---|
| 320 (floor) | One column: head, answers, boundaries, figures, objects, the strip (section index after the first answer), depth, next actions, the foot spine, the institutional band. Page gutter 16 px. Every figure panel fits 288 px; every fallback table fits 256 px in both languages (DEBT-010 closed at D6) | base rules |
| ≥ 480 | Reserved for the provider matrix's cells, two per row (the form is built and waits for its governed labels, DL-D7-001) | `CSS_D6` |
| ≥ 600 | The narrow index (`nav.strip`) in two columns; RV-CWR-001's row labels beside their tracks (`.p1 .row` grid); figure lanes side by side with the not-comparable divider as a vertical double rule; the Compare/record controls grid in two columns; the chain's step inset; the dense value labels of a time series shown (`svg.ts .val.dense`; below 600 the table carries the middle values, DL-D6-005) | `@media (min-width:600px)` ×2 |
| < 640 | The Compare table stacks: every row a block, each cell numbered by a CSS counter in the inline-start gutter, the row header on its own line (`.compare-table` block) | `@media (max-width:639px)` |
| < 600 | The product rubric in the head hidden (the product name stays in the bar) | `@media (max-width:599px)` |
| ≥ 900 | The wide type scale for both languages (§3); the page becomes a two-column grid — the object (max 840 px) and the spine column (280 px, sticky, `top:20px`, `max-height:calc(100vh - 40px)`, scrolls inside) with the index visible; the strip and the foot spine hidden; the product-bar navigation visible in a row with the Method & Measurement group set off by a hairline; the menu button hidden; cite and report shown inline; the institutional band in two columns; `h1` at most 22ch; page gutter 32 px | `@media (min-width:900px)` |
| ≥ 1200 | The rubric column: every answer (`section.qa`) and compact object becomes a 220 px + content grid, the rubric or clock in the first column; the spine 300 px; the priority objects (`.obj.prio`) and figure answers use the same grid | `@media (min-width:1200px)` ×2 |
| 1240 | Maximum page width (`02_TOKENS.json` → `layout`) | base rules |

Asserted: no horizontal page scroll and nothing wider than the viewport outside a scrollable table wrapper on every
one of the 288 documents at 320, 390, 640 and 1440 px in both languages (`check_site.py`, per render); every figure's
fit on both edges at 320, 390 and 600 px (`check_visuals.py`, `fits_*`); the whole Compare stacked form at 320 px with
its inputs labelled and the verdict before the table (`check_acceptance.py`, D7).

## 2. Reflow rules

- **One spine at any width.** From 900 px the side spine (index + edges) beside the object; below 900 px the strip
  after the first answer and the foot spine after the content (DEBT-014, accepted at D5: no runtime is needed to
  collapse a page's own headings). Both are named by the page's `h1` (`aria-labelledby="page-title"`).
- **Tables never scroll the page.** Every table sits in `div.table-wrap[role="region"][aria-label]` with
  `overflow-x:auto`; it is a tab stop (`tabindex="0"`, focus outline offset 6 px) only when declared wide — none is: two
  or three columns fit 256 px in both languages on every drawn contract (`06_VISUAL_TABLE_SYSTEM.md` §4). The Compare
  table stacks instead of scrolling (§1).
- **Figures keep their meaning at every width.** The narrow forms are the contract's, per form (`06_VISUAL_TABLE_SYSTEM.md`
  §3): rows and lanes stack; a bar's label moves above its track; a dense time series prints its first, last, marked
  and state-change values and the table carries the rest; the dated lanes become their dated lists under 600 px; the
  chain is a vertical list at every width. Percentage x-coordinates on SVGs without a `viewBox` keep every label at
  type size at every width (D1 technique); `labels_clear` is asserted by ink boxes at 320, 390, 600 and 1440 px.
- **The menu below 900 px** is a button with `aria-controls` and `aria-expanded`; without JavaScript it stays
  collapsed and every route remains reachable through the institutional band's link groups (`09_CODE_HANDOFF.md`).
- **Long strings.** `h1` is balanced (`text-wrap:balance`) and capped at 22ch from 900 px; the canonical link and
  source URLs wrap anywhere (`.canon`, `.src .source-url`: `overflow-wrap:anywhere`); an identifier breaks only at its
  own hyphens; a Latin proper name inside Arabic text wraps between its words like any phrase (DEBT-017, closed at D7
  on measurement: the longest such run in a display heading, "Global Findex 2021" in an Arabic `h1` at 30 px, is
  271 px in a 288 px column, so an unbreakable rule would hold by 17 px today and overflow at twenty characters — the
  fault the D4 gate caught for unbreakable identifiers). The longest governed title of each language renders at 320 px
  without overflow (`check_acceptance.py`, `longest_title_fits_320`).
- **Print reflows to the paper**, not to a breakpoint: one column, the spine at the foot, objects that fit a page kept
  whole (`06_VISUAL_TABLE_SYSTEM.md` §7; `@media print` in `CSS_D6`).

## 3. Type per language

Two scales, one for each language, each with a narrow and a wide (≥ 900 px) set; the values and every role are in
`02_TOKENS.json` → `type` (custom properties on `:root`, overridden on `[dir=rtl]`). What differs by language is a
decision of the Lock (`01_FOUNDATIONS.md` §4.1), not a mirrored scale:

| Role | Latin narrow / wide | Arabic narrow / wide | Leading (Latin / Arabic) |
|---|---|---|---|
| Display (`h1`) | 32 / 46 px | 30 / 42 px | 1.1 / 1.35 |
| Question, section heading | 20 / 23 px | 21 / 24 px | 1.4 / 1.7 |
| Statement | 19 / 21 px | 20 / 22 px | 1.5 / 1.7 |
| Body | 17 / 17 px | 18 / 18 px | 1.6 / 1.9 |
| Reading body | 18 / 19 px | 19 / 20 px | 1.65 / 1.9 |
| Boundary voice | 18 / 19 px | 19 / 20 px | 1.55 / 1.8 |
| Clock, reference, chart annotation | 13.5 px | 14.5 px | 1.4 / 1.7 |
| Source, citation, small | 14.5 px | 15.5 px | 1.5 / 1.7 |
| Rubric | 12 px, spaced capitals | 14 px, weight and colour, no transform | — |
| Measure | 64ch | 34em | — |

Arabic is larger and more leaded at every role; its rubrics and navigation group labels carry weight and colour where
the Latin ones carry spaced capitals (`[dir=ltr] .nav .glabel`, `[dir=ltr] h1{letter-spacing:-.012em}` — the
transforms and the negative tracking apply to Latin only). The three faces per family (Regular, Medium, SemiBold;
`08_ASSET_MAP.md` §2) are the only weights declared; `b, strong, th` are 600. Numerals are tabular everywhere a value
is set (`font-variant-numeric:tabular-nums`).

## 4. Arabic composition (RTL)

- **Direction is the document's.** `<html lang="ar" dir="rtl">`; nothing is mirrored by script. The stylesheet uses
  logical properties throughout — 43 `inline-start`/`inline-end`/`margin-inline`/`padding-inline`/`inset-inline`
  and `text-align:start` declarations, no physical `left`/`right` or `text-align:left|right` (counted on `theme.py`
  at D7) — so every rule, gutter, counter, border and inset flips with the direction without a second rule.
- **The thirteen `[dir=rtl]` rules** are the Arabic variants that logical properties cannot express: the two type
  scales (§3); the padding side of the paced compact object, the pull quote, the lanes' divider, the spine, the
  chain's steps, the hub list and the Compare table's cells (each a physical padding written for the Arabic side
  because its Latin twin sets the other side); the paced sentence's Arabic size; and the social frame's family label
  and title without transform or tracking.
- **Charts are not mirrored.** Every SVG is `direction="ltr"`, `aria-hidden`, with the time axis and the value axis
  left-to-right in both editions (Lock §4.1; `svg_ltr` asserted per figure). What is Arabic in a figure is its
  text — labels, states, notes, the frame — set in the Arabic scale by the surrounding document; the reading order
  of the frame (rubric, title, question, scope, panels, notes, foot, alternative) is the document order in both
  languages. The dated lanes' event keys and the chain's steps are lists in document order.
- **Numbers, dates and units.** Western digits everywhere (the one formatter: separators on every value, years
  unseparated, precision as governed); dates in words as day, month name, year with the governed Arabic month names
  (`content.date_words`); a governed English time boundary ("observed 2026-09-07") prints as the Master holds it,
  isolated and `lang="en"` (escalated, D6); a count and its unit noun print as governed (the native-editor
  observations of D6 are content, `ESCALATIONS.md`).
- **The product bar and the band** keep their document order: brand, navigation, controls; trust links first in the
  band. The `dir="rtl"` layout places them from the right; the tab order is the reading order (asserted by the
  keyboard walks, `check_journeys.py`).

## 5. Bidi isolation — the text layer (`yfie/text.py`)

After Arabic letters a plain ISO date renders with its parts reversed and a plain numeric range with its ends
swapped; an isolated run never does. One module isolates for every renderer and nothing in it authors a word:

| Rule | Implementation | Where |
|---|---|---|
| An ISO date (`YYYY-MM`, `YYYY-MM-DD`) or a numeric range (`2021–2024`, `2025-03–2026-01`, `15–24`) is an unbroken left-to-right run | `LTR_RUN` (= `NUM_RANGE` \| `ISO_DATE`); `<bdi dir="ltr" class="nw">` | every document, one pass (`isolate_document`) |
| A governed token (an identifier, a value) is isolated; an identifier breaks only at its own hyphens | `bdi()` — `class="nw"` only for a full date or range | renderers, per token |
| Governed text keeps its dates and ranges isolated | `iso()` / `isolate_iso()` | renderers, per string |
| The one pass over the finished document never enters `script`, `style`, `svg`, `title`, `textarea`, `option`, `pre`, `code`, or text already inside a `dir="ltr"` element (an isolate is never nested in an isolate) | `isolate_document` | `render.render`, the neutral files, the export and social frames |
| A free-text English time boundary is isolated and marked English | `visuals.date_token` → `<bdi dir="ltr" lang="en">` | the matrix, the lanes, the chain |
| The credit line is English, isolated | `visuals.credit_line` → `<bdi dir="ltr" lang="en">` | every frame foot |
| The canonical URL is an isolated run that may wrap anywhere | `.canon{unicode-bidi:isolate;overflow-wrap:anywhere}` | frame foot, print provenance |

Asserted: no date or range outside an isolate in any of the 598 documents and frames, with the renderer's own
`LTR_RUN` (`check_visuals.py --phases text`); `iso_dates_isolated` in the browser on every figure and every export
and social frame; the Arabic Compare table's reversed dates are a defect of the baseline runtime, escalated to Code
with its patch (`ESCALATIONS.md`, D6, RUNTIME_DEFECT).

## 6. Zoom, forced colours, reduced motion, no script, print

These are recorded once, in `07_INTERACTION_ACCESSIBILITY.md` §3 (zoom and reflow, forced colours, reduced motion, no
script, no stylesheet) and `06_VISUAL_TABLE_SYSTEM.md` §7 (the print system), and are not restated here. The
stylesheet blocks: `@media (prefers-reduced-motion:reduce)` (no transition, animation or smooth scroll — there is no
motion to remove), three `@media (forced-colors:active)` blocks (every rule, mark, line and label to `CanvasText`,
state never by colour), three `@media print` blocks (the D6 system last). `check_acceptance.py` asserts at D7 that no
element on Home carries a transition or animation under either preference.

## 7. What Code implements

- The breakpoints of §1 as tokens (`02_TOKENS.json` → `layout.breakpoints`) and the mobile-first order of the blocks;
  the two type scales of §3 as custom properties on `:root` and `[dir=rtl]`.
- Logical properties only; the thirteen `[dir=rtl]` rules of §4 where a physical side is unavoidable; no
  language-specific layout beyond them.
- The text layer of §5 as a post-render pass over every finished document (or the same three functions at render
  time), including the runtime-written cells the baseline leaves plain (the Compare defect).
- The tests that cover it: `check_site.py` (every document at the four widths), `check_visuals.py` (every figure at
  320/390/600 and the text phase), `check_acceptance.py` (the stacked Compare, the longest titles, motion),
  `audit/tranche_c/checks/viewport_acceptance.py` (the repository suite at 320/390/640/1440).
