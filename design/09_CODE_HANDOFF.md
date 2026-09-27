# Design → Code handoff (progressive)

Contract: `handoff/DESIGN_TO_CODE_CONTRACT.md`. Updated at every gate end; never back-filled.

## State at D0 (history — superseded by the D1 table below)

| Area | Status | Notes |
|---|---|---|
| Tokens | NOT STARTED | `handoff/DESIGN_STARTING_TOKENS.json` is a hypothesis only; do not implement it |
| Components | NOT STARTED | Candidate component inventory in `00_DESIGN_README.md` §4 — not decisions |
| States | MAPPED, NOT DESIGNED | 9 verification, 20 grammar, 15 technical, 12 hard-state cases — see `COVERAGE.csv` |
| Routes | MAPPED | 288 documents; family per route in `COVERAGE.csv` |
| Content bindings | UNCHANGED | Render only from `site-src/content/**` per inventory `projection_roles` |
| Visual contracts | NOT STARTED | 36 contracts; tiers in `00_DESIGN_README.md` §4 |
| Responsive / RTL | NOT STARTED | Widths 320 / 390 / 640 / 1440 |
| Accessibility | NOT STARTED | WCAG 2.2 AA outcomes as target; no conformance claimed |
| Print / export | NOT STARTED | Downloads ship disabled until OWN-04 |
| Reference implementation | DOES NOT EXIST | DEBT-002 |

## State at D4 (in progress — updated at milestones, not back-filled; rows not listed are as at D3)

| Area | Status | Notes |
|---|---|---|
| Routes | ALL 288 VERIFIED on their rows | every evidence record asserted from its own governed bundle and the three remaining domain answers from their contracts (`check_site.py --gate d4`: 904 renders, 452 smoke tests, 3,822 hard-state assertions, 10 degraded renders); the neutral root entry asserted (`root_checks`); the D5 tool states and journeys and the D6 visuals remain |
| Content bindings | PROVED | `design/reference/check_binding.py`: every RENDER and CONTRACT projection read by `yfie/content.py` (the search index and aliases shipped unchanged for the runtime); no REFERENCE or VIA_SPEC projection read anywhere in the reference; STRUCTURE read for ids and links only; 286 edition pages + root + 404, 286 bundles, no copied content model. `public_claims.json` (VIA_SPEC) is no longer loaded |
| Checks | GATE d4 | `check_site.py --gate d4` (the three domain routes + every record from the built bundles; `--only` for a partial run, never a record); `check_binding.py` |
| Evidence | COMMITTED | `design/evidence/d4/` (42 PNG: the three domain answers at 390 and 1440 px in both languages; one record per verification state outside the §9.1 set; the 404) |

## State at D3 (met at `beecdbb` — the D4 table above supersedes the rows it repeats)

| Area | Status | Notes |
|---|---|---|
| Routes | ALL 288 BUILD; D1–D3 families VERIFIED | The Reading index, the ten Readings, Measurement, Methodology, the eight trust pages and the bilingual 404 are composed and asserted (`check_site.py --gate d3`: 168 renders, 84 smoke tests, 252 hard-state assertions, 18 degraded renders); Home re-verified after the cold-reader test (in gate d3). Remaining: the three domain answers and the records outside §9.1 (D4), the tool states (D5), the visuals still rendered as text frames (D6) |
| Compact evidence object | ONE LINK | `render.compact`: the governed action is the only link; its accessible name is the action then the record's title via `aria-labelledby` over the two ids (`co-a<n>`, `co-t<n>`); the title is text. Directory rows, verify objects and Reading objects keep their own markup (one link each) |
| Figure object | BOUNDARY ONCE | the foot prints `UI-DOM-WHAT-NOT-TO-CONCLUDE` + the prohibited inference once; the text alternative carries what the view shows, scope and the table; a text frame (`figure.fig.fig-text`) shows the description as its body, keeps `h3.alt-h` visually hidden and no `figcaption` (the visible body is the description) |
| Home | HEAD = STATEMENT + ACTIONS | section 1 and the two governed actions in `.head` before the first figure (`.head .rubric.product` hidden under 600 px); the framing record in `#s6`; the spine's first edge lists all four records with the governed count |
| Product bar | GROUP SET OFF | `.nav .group` carries a hairline and its label aligns to the links' baseline; `.controls .cite/.report` in `--ink-2` |
| Arabic tokens | RUBRIC 14 px | `html[dir=rtl] --fs-rubric: 14px` (was 13); `02_TOKENS.json` regenerated |
| Checks | GATE d3 | `check_site.py --gate d3` (routes: Home, `/readings/`, ten Readings, `/measurement/`, `/methodology/`, eight trust routes; `not_found_checks` on the 404); Home assertions `statement_in_head`, `statement_before_first_figure`, `one_link_per_bound_object`, `boundary_once_per_frame`, `records_edge_lists_all`, `double_rule_spans_column`; Reading `measure_bounded` asserts the measure property (narrower than the column, ≤ 720 px) |
| Evidence | COMMITTED | `design/evidence/d3/` (38 PNG: first screens at 390 and 1440 px of nine routes in both languages, the 404 at 320 and 1440 px) and `design/evidence/d3/cold_read/` (four verbatim reader reports) |
| Temporary vs intended | RECORDED | Temporary: the foot spine on phones (DEBT-014); the statement's length on a phone (DEBT-015); the 10 MB mark and the publisher's legibility (DEBT-016, escalated); D2's DEBT-011…013 unchanged. Intended: everything else on this table |

## State at D2 (met at `9c263ac` — the D3 table above supersedes the rows it repeats)

| Area | Status | Notes |
|---|---|---|
| Content path | IMPLEMENTED for every family | `design/reference/yfie/content.py` loads all eleven families (`Content.page(route, lang)` dispatches by the navigation contract's `page_family`): Question Entry (clusters from the handoff inventory's `question_groups`), Domain Answer (order from `presentation_priority.json`), Evidence Directory (the question-grouped register), Evidence Record (now with its own visual and a Compare entry), Comparison (the runtime payload from the governed fields, dimensions from the family contract), Data & Source (curated by `resource_category`, dependency groups from the evidence specs' source references, inventory list, chronology), Reading Index, Measurement, Reference / Trust (report path context), 404, root. `visual()` resolves every `<field>_label` to the page language, carries `frame_labels`, `objects`, `missing_x`, the record's method text and the grammar labels; VIS-PAYMENT-RAILS carries RV-CWR-009's event set |
| Routes | ALL 288 BUILD | `python3 design/reference/build.py` writes every document, the root entry, the 404 and `robots.txt` (`sitemap.xml` once the origin is set). Family → renderer: `render.py` (Orientation, Evidence Record, Reading), `families.py` (the rest). Composition rules: `04_PAGE_FAMILY_COMPOSITIONS.md` |
| Components | CATALOGUE SEEDED | `03_COMPONENT_CATALOG.md`: objects, the figure anatomy, six drawing forms, the evidence-state grammar (what is drawn, what is designed only), the tools' hooks |
| Visual contracts | 8 DRAWN (D1 + D2); the rest as text frames | RV-CWR-001 (D1); VIS-FINDEX-GAPS (bars + bracket gaps); VIS-REMITTANCE-MACRO and the POS small multiple (state-keyed time series: filled/hollow/square marks, dashed projections, break never joined, labelled missing gap, ringed disagreement with the record's method text, NOMINAL on the axis title, a key of states with their source document); VIS-REMITTANCE-COST (dot rows); VIS-PAYMENT-ANATOMY (object list, WITHHELD in place of a value, NOT_COMPARABLE labels); VIS-PAYMENT-RAILS (the chain ladder from RV-CWR-009's governed events, no values). Technique unchanged: percentage-coordinate SVG, no viewBox, `direction="ltr"`, no inline style; every value through `plain_num` (precision as governed); the credit as `<bdi dir="ltr">` |
| Number rule | CORRECTED | `plain_num` never rounds: the shortest exact representation with thousands separators (317.639 stays 317.639); years unseparated; `bdi` isolation in HTML text, never inside SVG `<text>` |
| Headings and landmarks | DECIDED, NAMED | one `h1#page-title` per page; every `nav` named: the index and strip by the `h1` (`aria-labelledby="page-title"`), edge groups by their `h3`, the crumb, primary, trust, footer and next-action navs by governed labels; `check_site.py` fails on any unnamed `nav` |
| Responsive / RTL | VERIFIED on 21 D2 routes | 320/390/640/1440 px in both languages; Compare's table recomposed below 640 px by CSS counters keyed to the governed slot order (runtime untouched); the register and the hub as lists; `[hidden]` honoured |
| Tools | RENDERED, RUNTIME UNCHANGED | `site-src/app.js` copied as is; Search (dialog + the directory's inline input, status and results regions), Compare (four `<select>` slots, copy link, status, output, `yfie-compare`, `yfie-compare-dimensions`; entry from each comparable record and from a Reading's trace), source register (filter, status, no-match, `#source-<ID>` focusable rows, `.source-locator-details`), report path (`[data-correction-context]`, `yfie-record-ids`, the mail action for a known record); `test_public_tools.py` 25/26 on the site |
| Strict CSP | MET | zero `[style]` on all 288 documents; JSON blocks only |
| Print | BASICS on every family | the D1 rules plus: figures kept whole with their boundary; controls, filters and record actions removed; dense value labels restored; hub and register disclosures printed |
| Evidence and checks | COMMITTED | `design/evidence/d2/` (60 PNG: first screens at 390 and 1440 px of eleven routes in both languages, figure crops of the eight D2 figures in both languages); `check_site.py` (168 renders, 84 smoke tests, 157 hard-state assertions, 20 degraded renders); `check_content.py --text` (bundle-scoped numbers, inline-tag-safe text) on 288 documents; `check_trio.py` unchanged; both repository suites and `bilingual_invariance.py` on the site |
| Temporary vs intended | RECORDED | Temporary: the source register's supporting group open and long (DEBT-011); dense value labels hidden below 600 px (DEBT-012); fallback tables with unheaded columns (DEBT-013); the D3 families composed by the family rule only (DEBT-002). Intended: a governed-field filter on the register; a narrow form that prints every value; governed column labels; composition per family at D3 |
| Exceptions | RECORDED | The governed source intro is not printed on a framing record (`check_content.py` `FRAMING_EXCEPTION`); Explore prints section 5's body as the list's introduction and drops its heading (brief §4.5); Home's order as at D1 (brief §4.5); the Reading index, Measurement and trust heads carry the governed flow rubric instead of a family rubric until D3 |

## State at D1 (history — the D2 table above supersedes the rows it repeats)

| Area | Status | Notes |
|---|---|---|
| Content path | IMPLEMENTED (neutral) | `design/reference/yfie/content.py` reads `site-src/content/**` and gives every renderer the same structures (shell, page, evidence record, reading, visual, home); `design/reference/check_content.py` proves parity with `dist/`. Code inherits this path or an equivalent that binds the same projections; no copied content model |
| Test hooks | CARRIED by the reference renderer (and the neutral harness) | `design/reference/yfie/render.py` emits every brief §19 hook: ids `main`, `search-dialog`, `utility-status`, `primary-nav`; `data-search-open/close/input/status/results`, `data-menu`, `data-lang`, `data-cite`, `data-source-cite`, `data-evidence-source`, `data-record-id`, `data-evidence-boundary-first-load`, `data-boundary-part`, `data-reading-boundary/section/verify/related`, `data-path-record/state`, `data-visual-id`, `data-visual-fallback`, `data-image-independent`, `data-noncolour-semantic`; classes `skip` (first focusable), `evidence-cite-button`, `source-locator`, `table-wrap`; JSON block `yfie-ui`; meta `yfie-citation`, `yfie-record-id`; `<dialog id="search-dialog">` with input `global-search-dialog`; one `h1`; `lang` and `dir` on the document (`check_trio.py` asserts them) |
| Tokens | EXTRACTED (D1) | `design/02_TOKENS.json` is generated by `design/reference/tokens.py` from the reference stylesheet's custom properties (`--check` fails when stale); the exploratory values in `design/exploration/d1_canvas/boards/t4.py` are not authoritative |
| Components | GRAMMAR CHOSEN (T4) | Clock-first evidence object (page object and compact object), the seven governed record questions as `h2` structure and index, the boundary as a second voice (double rule + label + weight + colour), a verification spine (index, edges, trust links first in the footer band), figure object with the contract frame and its text alternative visible. Details in `01_FOUNDATIONS.md` §1 (T4), §3.3 |
| Visual contracts | RV-CWR-001 FORM CHOSEN | Panel 1 as one row per publication on a horizontal zero-based axis with printed values; panel 2 as two lanes with the not-comparable divider between them, baseline at the index origin, each lane's raw 2021 level beside it; one mark per publication across panels; alt text and tables visible; numeric value and time axes left-to-right in both languages (governed rule). Technique Code inherits: percentage-coordinate SVG without a viewBox keeps text at type size at every width and needs no inline style under strict CSP; marks that need rotation are not usable with percentage coordinates |
| Number rule | DECIDED | One formatter for every rendered value: thousands separators on all values, years never separated, precision as governed, no trailing ".0"; numeric runs, IDs and ISO dates isolated left-to-right (`bdi`) and unbroken in Arabic; Western digits as in governed copy |
| Headings and landmarks | DECIDED | One `h1`; the Record's seven questions and its boundary are `h2`; the figure title `h2` inside the essay, lane titles `h3`; in-page navigation needs a governed accessible name (escalated) |
| Responsive / RTL | VERIFIED on the trio | 320/390/640/1440 px in both languages with no page overflow (`check_trio.py`); breakpoints 600/900/1200; numeric axes stay LTR in Arabic; IDs, units, index bases and ISO dates isolated with `bdi`; Arabic on its own scale |
| Strict CSP | MET | The reference renderer emits no inline style or script (`check_trio.py` asserts zero `[style]` elements); the canvas artboards' frame styles belong to the canvas only |
| Reference implementation | STRESS TRIO BUILT (D1) | `python3 design/reference/build.py` renders Home, `/evidence/CLM-003/` and `/readings/same-year-different-number/` in both languages from `yfie/render.py` (composition), `yfie/theme.py` (the one stylesheet, written to `assets/yfie.css`) and `yfie/visuals.py` (contract drawings); `check_trio.py` proves 24 renders and 12 interaction smoke tests; parity and bilingual invariance pass. 282 documents remain (DEBT-002) |
| Print | BASICS IMPLEMENTED | In the same stylesheet: controls, dialog, indexes and footer link groups removed; objects, figures and sources kept whole; the record's disclosure content printed (`::details-content`, verified in Chromium); source locators and the canonical link printed after their text; page breaks avoided inside objects (proof: `python3 design/reference/check_trio.py --degraded`, and the committed `design/evidence/d1/*-print.png`) |
| Evidence and checks | COMMITTED | `design/evidence/d1/` (18 PNG: first screens at 390 and 1440 px and printed pages, both languages, written by `check_trio.py --evidence`); `check_trio.py` (renders, hooks, pointer and keyboard smoke tests, degraded states), `check_content.py --text` (numeric and text-block parity), `tokens.py --check`; the nine lens reports and the independent final review under `design/exploration/d1_canvas/review/` |
| Runtime | BASELINE, UNCHANGED | `site-src/app.js` is copied as is; the renderer emits the hooks it binds (search dialog, cite, language, menu, source cite). The menu panel (`#primary-nav.open`) and the dialog are styled in the theme; no other script |
| Temporary vs intended | RECORDED | Temporary: pacing on Home by governed connectives with a whole-paragraph fallback (DEBT-008); in-page navigation unnamed (DEBT-006); the fallback table scrolls at 320 px (DEBT-010). Intended: a controlled pacing marker; a governed accessible name; a narrower table composition at D6 |

## Must not be reinterpreted (already fixed by the brief)

- Test hooks of brief §19 (IDs, `data-*` attributes, classes, JSON blocks, `<dialog id="search-dialog">`, `<select>`
  Compare slots, skip link class `skip`, `role="status"`/`role="alert"` regions).
- Strict CSP: no inline script/style/handlers, no external resources, no form; `yfie-lang` is the only preference.
- Logo never filtered, recoloured or inverted (EAD-04); fonts self-hosted, unchanged, with OFL.
- CLM-044 value never rendered anywhere; the 9 sources without a public locator never named or linked.

## Temporary vs intended

At D0 nothing was implemented. At D2 the "Temporary vs intended" row of the D2 table above is the live statement (the D1 row stands where it is not superseded);
nothing in `dist/` or `site-src/styles.css` is a Design decision. Without JavaScript below 900 px the primary
navigation stays collapsed (the menu button needs the runtime); every route remains reachable through the
institutional band's link groups.

## Owner / release items that remain

OWN-01 identity and funding statement · OWN-04 content licence (gates downloads) · OWN-06 reversed logo · EAD-03 logo
derivatives · REL-01…04. See `FINAL_OPEN_ITEMS_REGISTER.md`.
