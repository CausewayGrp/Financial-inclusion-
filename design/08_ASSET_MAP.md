# Asset map

> STATUS: **D6 — every asset the reference site ships or draws, as built; nothing here is a picture of an intention.**
> Source of truth: `design/reference/build.py` (what is copied into `out/assets/`), `design/reference/yfie/theme.py`
> (`FONT_FACES`, the social and export frame styles), `design/reference/yfie/render.py` (`logo()`), `design/reference/yfie/frames.py`
> (the portable frames). The logo and the fonts are the owner's canonical files, served unchanged (brief §8, EAD-04;
> `vendor/fonts/` with their licence). No icon set, no illustration, no decorative image exists or is planned (brief §7).

## 1. The mark

One file, `site-src/assets/CauseWay_Master_Logo.png` (6 250 × 6 250 px, 10 MB), copied unchanged to `out/assets/` and
drawn by `render.logo(px)` as `<img … alt="CauseWay" width="px" height="px">`. It is never filtered, recoloured,
cropped, masked, inverted or blended (EAD-04; `check_site.py` and `check_visuals.py` assert the unaltered file on every
surface that carries it). The web-weight derivative and any reversed or single-colour version are owner decisions
(EAD-03, OWN-06; DEBT-016) — until they exist every surface loads the master file.

| Surface | Size (CSS px) | Clear space | Neighbour | Where |
|---|---|---|---|---|
| Product bar (every page) | 40 × 40 | 10 px to the product name; the bar's 16 px gutter | the product name (`.brand-name`); the brand link is named `CauseWay — <product name>` | `render.header` |
| Institutional band (every page) | 40 × 40 | 12 px to the strapline | the governed footer strapline | `render.footer` |
| 404 head | 48 × 48 | the head's 8 px gap | the bilingual rubric | `families.not_found` |
| Print (product bar) | 32 pt | as the bar | the product name, unwrapped | `theme` print block |
| Export frame identity line | 32 × 32 | 10 px | product name · edition | `frames.export_document` |
| Social-image template | 72 × 72 | 18 px | product name and the family rubric | `frames.social_document` |

Derivative sizes Code will want when the owner supplies a web-weight rendering (same mark, no crop, no filter): 40, 48,
72 px at 1× and 2× (80, 96, 144 px), and 32 px (64 px) for the export identity line. Nothing else scales the mark.

## 2. Type

IBM Plex Sans (Latin) and IBM Plex Sans Arabic, self-hosted from `vendor/fonts/ibm-plex-sans/` and
`vendor/fonts/ibm-plex-sans-arabic/` (copied unchanged to `out/assets/fonts/`, each folder with its `LICENSE.txt`),
WOFF2 only, `font-display: swap`. No other typeface, no system fallback other than the browser's sans-serif.

| Face | Weights declared (`theme.FONT_FACES`) | Used by |
|---|---|---|
| IBM Plex Sans | Regular 400, Medium 500, SemiBold 600 | body 400; rubrics, clocks, keys and navigation 500–600; headings, values and every emphasis (`b`, `strong`, `th`) 600 |
| IBM Plex Sans Arabic | Regular 400, Medium 500, SemiBold 600 | the same roles on the Arabic scale (`html[dir=rtl]` tokens) |

Three weights, authored. D1 declared six faces; Light 300 and Italic 400 were never used by any rule, and Bold 700
reached the page only through the browser's defaults for `b`, `strong` and `th` — a type role the Lock says defaults
may not decide (`01_FOUNDATIONS.md` §4.1.9). D6 authors emphasis at the semibold role (`b,strong,th{font-weight:600}`)
and declares only the three faces used; the other files stay in `vendor/fonts/` as shipped. No `<link rel="preload">` is emitted: the two faces a first paint needs
(Regular and SemiBold of the page language) are a Code decision at D7's performance pass, with the pre-split Latin
subsets IBM publishes (anticipated escalation, `ESCALATIONS.md`). Type roles and the two scales: `02_TOKENS.json`.

## 3. Icons and glyphs

There is no icon set. Every non-text sign is a glyph of the shipped fonts or an SVG primitive, and each carries a text
label beside it:

| Sign | Meaning | Where | Text beside it |
|---|---|---|---|
| ● ▢ ◎ (SVG circle, square, ring) | one mark per publication or evidence state | RV-CWR-001, the time series, the dot rows | the state key (`UI-VIS-STATE-*`) |
| ■ □ | a chain step the evidence reaches / an open step | RV-CWR-009, VIS-PAYMENT-RAILS, the outcome node of RV-CWR-004 | `UI-VIS-CHAIN-EVIDENCED`, `UI-VIS-CHAIN-OPEN` |
| ‖ | a break between two source documents (never joined) | VIS-REMITTANCE-MACRO note line | `UI-VIS-BREAK-VINTAGE` |
| ┆ | a missing period (never zero) | VIS-POS-VALUE note line | `UI-VIS-MISSING` |
| ◎ | source figures disagree — both shown | the POS panels' note line | `UI-VIS-DISAGREEMENT` + the record's method text |
| ↗ | opens the original source in a new window | every external `a.source-locator` | the link's accessible name (`UI-VIS-SOURCE` + the event label); the visible cue is escalated (D5) |
| → | the governed flow | the rubric `UI-DOM-UNDERSTAND-EXPLORE-VERIFY` | (it is the label) |
| ─ ═ ┄ | hairline, double rule, dashed hairline | body, boundary, technical voice | — |

## 4. Social-image templates (`frames.social_document`; brief §16)

One 1200 × 630 template per family group, filled only with governed text, written by the build as
`out/_social/<route>__<lang>.html` (286 files; an underscore path outside the hostable site) and asserted by
`check_visuals.py` (fits the frame, title, canonical link, edition, the unaltered logo, no script, no inline style).
Code rasterises them at build time and adds `og:image` (1200 × 630) only then; until then every page keeps Open Graph
without image (F6-G01). The governed meta description is not repeated on the image — 284 of the 286 descriptions open
with the page title (`ESCALATIONS.md`, D6 observation) and the platform prints `og:description` beside the image.

| Template | Families | Head | Body | Foot |
|---|---|---|---|---|
| Record | Evidence Record | logo 72 px · product name · family rubric (`UI-EVID-*` family label) | the title (46 px, stepping to 38 / 31 with its length) · `UI-EVID-WHEN-…` + period · `UI-EVID-WHO-…` + universe · `UI-SOURCE-REFERENCE` + the record ID · the boundary (`UI-DOM-WHAT-NOT-TO-CONCLUDE` + `does_not_establish`) in the boundary voice (double rule, counter colour) | canonical link (isolated LTR) · edition |
| Reading | Reading | logo · product · `UI-READING-EYEBROW` | the governed question · the title · `UI-READING-EVIDENCE-PERIOD` + evidence period · the prohibited inference (`UI-VIS-DOES-NOT-ESTABLISH`) | same |
| Domain answer | Domain Answer | logo · product · `UI-ANSWER-CRUMB-LABEL` | the governed question · the title (the answer) · the first-screen figure's prohibited inference where the contract places a figure first (none on `/reforms/`) | same |
| Product | Orientation | logo · product | the title | same |
| Hub | Question Entry, Evidence Directory, Comparison, Reading Index, Data & Source, Measurement, Reference / Trust | logo · product · the flow rubric | the title | same |

Type steps: title 46 / 38 / 31 px by length; the whole frame steps to `dense` (34 / 30 / 26 px) above 330 characters of
governed text and to `xdense` (28 / 25 / 22 px) above 470, so nothing is ever cropped; a boundary is never truncated.
Arabic templates use the Arabic face, right-to-left order, a longer line height and no letter-spacing on the rubric.
No template shows a value without its period, population and boundary: a record's card always carries its dates and
its boundary; a Reading's card its evidence period and its prohibited inference.

## 5. Export frames (`frames.export_document`; brief §10)

`out/_export/<visual>__<lang>.html` — one standalone document per drawn contract and language (26): the identity
line (mark 32 px · product · edition), then the figure with its complete detached frame (title, question, period ·
universe, panels, notes and markers, the prohibited inference, the credit isolated left-to-right, the canonical link,
the edition); the text alternative and the cite control are not part of the export (the frame is the image; the
canonical link leads to the alternative). 800 px wide, paper surface. The export **control** on pages is designed
(`03_COMPONENT_CATALOG.md` §2) and unshipped: its labels and states are not governed (`ESCALATIONS.md`) and every
CauseWay-content download ships disabled until the licence decision (OWN-04). The browser's print and "save as PDF" of
a page are not downloads and are always available (§6).

## 6. Print (no asset)

The print system is the same stylesheet (`theme.CSS_D6`, `@media print`); it adds no file. Every printed page ends with
the print-only provenance block (`render.print_foot`): product · edition · canonical URL, then the citation the cite
action copies (`06_VISUAL_TABLE_SYSTEM.md` §7).

## 7. What `out/assets/` holds

`yfie.css` (FONT_FACES + CSS + CSS_D2 + CSS_D6), `app.js` and `lang-redirect.js` (the baseline runtime, unchanged),
`CauseWay_Master_Logo.png`, `fonts/ibm-plex-sans/` and `fonts/ibm-plex-sans-arabic/` (as vendored, with licences).
`static-data/` holds the two JSON files the runtime fetches. Nothing else is shipped; no third-party resource is loaded.
