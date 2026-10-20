# Asset map

> STATUS: **D6 — every asset the reference site ships or draws, as built; nothing here is a picture of an intention.**
> Source of truth: `design/reference/build.py` (what is copied into `out/assets/`), `design/reference/yfie/theme.py`
> (`FONT_FACES`, the social and export frame styles), `design/reference/yfie/render.py` (`logo()`), `design/reference/yfie/frames.py`
> (the portable frames). The logo and the fonts are the owner's canonical files, served unchanged (brief §8, EAD-04;
> `vendor/fonts/` with their licence). No icon set, no illustration, no decorative image exists or is planned (brief §7).
> Since owner decision OD-1018 (18 October 2026, the canvas "Yemen FI Evidence Home"): one display face per edition
> (§2.1) and, on Home only, one illustration and eight topic icons as inline SVG (§3.1); nothing else changed here.

## 1. The mark and the publisher lockup

One file, `site-src/assets/CauseWay_Master_Logo.png` (6 250 × 6 250 px, 10 MB), copied unchanged to `out/assets/` and
drawn by `render.logo(px)` as `<img … alt="CauseWay" width="px" height="px">`. It is never filtered, recoloured,
cropped, masked, inverted or blended (EAD-04; `check_site.py` and `check_visuals.py` assert the unaltered file on every
surface that carries it). The web-weight derivative and any reversed or single-colour version are owner decisions
(EAD-03, OWN-06; DEBT-016) — until they exist every surface loads the master file.

**The lockup (D7, DL-D7-008).** The file's own wordmark and Arabic name sit under 8 px at every interface size and can
never carry the publisher's identity there, so the lockup carries it in type: the mark, then the publisher's name
**CauseWay** set in text (SemiBold, the ochre role — the type echo of the gold wordmark, at AA contrast) above or
beside the governed product name. The name is the publisher's proper name as the repository already prints it
(the governed strapline, the citation lines, the © line); it is not authored interface copy. In Arabic it is an
isolated left-to-right run (`dir="ltr"`), the rule the visual contracts set for publisher names. The in-image wordmark
remains the mark's own detail at interface sizes; the text is the carrier. A reader arriving on any page, either
language, sees the publisher named legibly in the product bar, and on every artifact that leaves the page (export
frame, social frame, print head).

| Surface | Size (CSS px) | Clear space | Lockup | Where |
|---|---|---|---|---|
| Product bar (every page) | 40 × 40 (48 from 900 px) | 12 px to the text block; the bar's 16 px gutter | mark · **CauseWay** (11.5–12.5 px, ochre) over the product name (13–14 px, ink); the brand link is named `CauseWay — <product name>` | `render.header`, `.brand-pub` |
| Institutional band (every page) | 40 × 40 | 12 px to the strapline | mark · the governed footer strapline (which names CauseWay) | `render.footer` |
| 404 head | 48 × 48 | the head's 8 px gap | mark · the bilingual rubric | `families.not_found` |
| Print (product bar) | 32 pt | as the bar | mark · CauseWay (8.5 pt) over the product name, unwrapped | `theme` print block |
| Export frame identity line | 32 × 32 | 10 px | mark · CauseWay (isolated LTR) · **product name** · edition | `frames.export_document` |
| Social-image template | 72 × 72 | 18 px | mark · CauseWay (14 px, ochre) over the product name and the family rubric | `frames.social_document` |

**Derivative sizes Code must export (EAD-03)** when the owner supplies a web-weight rendering (the same complete mark —
no crop, no filter, no recolour): 40, 48 and 72 px at 1× and 2× (80, 96, 144 px), and 32 px (64 px) for the export
identity line — six raster sizes from one master, or one vector/compressed derivative ≤ 50 KB covering all of them.
Nothing else scales the mark, and the lockup above does not change when the derivative arrives; only the file weight
does (DEBT-016's remaining cost — first paint on a phone — closes then).

**Shipped, 2 October 2026** (release candidate G4 item 2; owner decision EAD-03): `scripts/logo_derivatives.py` writes the
eight sizes (32, 40, 48, 64, 72, 80, 96, 144 px) to `site-src/assets/logo/` as pure Lanczos resamples of the unchanged
master and checks them pixel for pixel (`--check`, CI). `render.logo()` serves them with `srcset`/`sizes` on the product bar,
the institutional band and the 404 head; the export identity line uses 32/64. The social-image template keeps the master
file: it renders offline and the 286 governed images stay byte-identical. Measured cold page weight: 10.31–10.71 MB before,
0.30–0.69 MB after (`audit/release_candidate/page_weight/PAGE_WEIGHT_EAD-03.md`).

## 2. Type

IBM Plex Sans (Latin) and IBM Plex Sans Arabic, self-hosted from `vendor/fonts/ibm-plex-sans/` and
`vendor/fonts/ibm-plex-sans-arabic/` (copied unchanged to `out/assets/fonts/`, each folder with its `LICENSE.txt`),
WOFF2 only, `font-display: swap`. No other typeface, no system fallback other than the browser's sans-serif.

| Face | Weights declared (`theme.FONT_FACES`) | Used by |
|---|---|---|
| IBM Plex Sans | Regular 400, Medium 500, SemiBold 600 | body 400; rubrics, clocks, keys and navigation 500–600; headings, values and every emphasis (`b`, `strong`, `th`) 600 |
| IBM Plex Sans Arabic | Regular 400, Medium 500, SemiBold 600 | the same roles on the Arabic scale (`html[dir=rtl]` tokens) |

Three weights, authored. The Arabic rubric is SemiBold 600 like the English one (the Arabic lens read it as lighter
beside tracked capitals; a heavier face is not declared and would be an owner decision). D1 declared six faces; Light 300 and Italic 400 were never used by any rule, and Bold 700
reached the page only through the browser's defaults for `b`, `strong` and `th` — a type role the Lock says defaults
may not decide (`01_FOUNDATIONS.md` §4.1.9). D6 authors emphasis at the semibold role (`b,strong,th{font-weight:600}`)
and declares only the three faces used; the other files stay in `vendor/fonts/` as shipped. D7 (DL-D7-005): every page
preloads the two faces its first paint needs — Regular and SemiBold of the page's language, from the shipped files,
`crossorigin` because fonts are fetched in CORS mode (`render.font_preloads`); Medium and the other language's faces
load on demand with `font-display: swap`. IBM's pre-split Latin subsets stay a Code option (anticipated escalation,
`ESCALATIONS.md`; vendoring needs provenance). Type roles and the two scales: `02_TOKENS.json`.

### 2.1 Display faces (OD-1018 D2, 18 October 2026)

Titles (`h1`), section headings (`h2` that is not an eyebrow) and the featured Reading's title take one display face
per edition, declared in `theme.FONT_FACES` and loaded only by its own edition (`html[dir]` sets `--font-display`):

| Face | File (`vendor/fonts/`, copied to `assets/fonts/`) | Upstream | Licence | Bytes |
|---|---|---|---|---|
| Noto Naskh Arabic SemiBold 600 | `noto-naskh-arabic/NotoNaskhArabic-SemiBold-subset.woff2` | notofonts/arabic release NotoNaskhArabic-v2.021, the unhinted TTF, subset by `scripts/font_subset.py` (Arabic letters, marks, Arabic punctuation and digits; no Latin, no Western digit) | OFL 1.1, no Reserved Font Name | 12,616 |
| IBM Plex Serif SemiBold 600 | `ibm-plex-serif/IBMPlexSerif-SemiBold-Latin1.woff2` | npm `@ibm/plex-serif@2.0.0`, IBM's own Latin-1 split, unchanged | OFL 1.1, Reserved Font Name "Plex" | 24,016 |

Body, controls and figures keep IBM Plex Sans and IBM Plex Sans Arabic; a figure is set in Western tabular digits from a
face the page already loads (`--font-fig`: Plex Serif in English, Plex Sans Arabic in Arabic). Latin inside an Arabic
title falls back to IBM Plex Sans Arabic 600 by design. Each page preloads Regular, SemiBold and its own display face and
loads at most four font files. Hashes and the covered code points: `vendor/fonts/display_coverage.json`; the gate
`scripts/tests/test_display_font_coverage.py` checks every generated heading of both editions against them.

## 3. Icons and glyphs

There is no icon set. Every non-text sign is a glyph of the shipped fonts or an SVG primitive, and each carries a text
label beside it:

| Sign | Meaning | Where | Text beside it |
|---|---|---|---|
| ● ■ ◆ (SVG circle, square, rotated square) | one filled mark per publication or group, the same in every panel | RV-CWR-001, the dot rows, the lanes | the row or lane label |
| ● ■ ○ ○╌ | evidence state: filled reported/measured, filled square administrative, hollow estimate, hollow dashed projection — hollow means "not an observation" and nothing else | the time series | the state key (`UI-VIS-STATE-*`) and, where the state changes, the label on the panel |
| ■ □ | a chain step the evidence reaches / an open step | RV-CWR-009, VIS-PAYMENT-RAILS, the outcome node of RV-CWR-004 | `UI-VIS-CHAIN-EVIDENCED`, `UI-VIS-CHAIN-OPEN` |
| ‖ | a break between two source documents (never joined) | VIS-REMITTANCE-MACRO note line | `UI-VIS-BREAK-VINTAGE` |
| ┆ | a missing period (never zero) | VIS-POS-VALUE note line | `UI-VIS-MISSING` |
| ◎ | source figures disagree — both shown | the POS panels' note line | `UI-VIS-DISAGREEMENT` + the record's method text |
| ↗ | opens the original source in a new window | every external `a.source-locator` | the link's accessible name (`UI-VIS-SOURCE` + the event label); bound to the word before it by a no-break space; the visible cue, and its mirrored form for Arabic, are escalated (D5, D6) |
| → | the governed flow | the rubric `UI-DOM-UNDERSTAND-EXPLORE-VERIFY` | (it is the label) |
| ─ ═ ┄ | hairline, double rule, dashed hairline | body, boundary, technical voice | — |

### 3.1 The Home exception and the interface marks (OD-1018 D4/D5, 18 October 2026)

The owner's exception to directive §5, Home only: the canvas's hero illustration (four stacked dotted planes, a ground
and four connectors; `render.HERO_ART`) and one stroke icon per topic card (`render.HUB_ICONS`, a 24-unit grid at
1.8 stroke) as inline SVG. Provenance: redrawn from the owner's Claude Design canvas "Yemen FI Evidence Home"
(`Main.dc.html`, `Home-AR-Mobile.dc.html`, 18 October 2026) — the canvas's geometry, none of its text, every colour a
stylesheet token through a class (no literal, no style attribute). Both are `aria-hidden` and carry no meaning; the
illustration is shown from 1200 px only (on a phone it would push the first figure card below the first screen). The
gate P3-G02 admits exactly these on the two Home pages and refuses any other graphic outside a governed figure.

The interface's other marks — the search, menu and go/arrow marks, the caution band's warning circle — are stylesheet
masks and gradients in the text colour (`theme.CSS`, `--ico-*`), never markup and never meaning: each sits beside its
own governed label.

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

`out/_export/<visual>__<lang>.html` — one standalone document per drawn contract and language (26 at D6; 24 at D7,
while the provider matrix waits for its six labels and renders as a text frame, DL-D7-001 — `visuals.draws`): the identity
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
`CauseWay_Master_Logo.png`, `fonts/ibm-plex-sans/` and `fonts/ibm-plex-sans-arabic/` (as vendored, with licences),
and since OD-1018 `fonts/noto-naskh-arabic/` and `fonts/ibm-plex-serif/` (§2.1, with their licences).
`static-data/` holds the two JSON files the runtime fetches. Nothing else is shipped; no third-party resource is loaded.
