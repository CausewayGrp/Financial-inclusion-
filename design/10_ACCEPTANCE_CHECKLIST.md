# Acceptance checklist — D7 (28 September 2026)

**Status: D7 MET — FINAL VISUAL ACCEPTANCE RECORDED BY THE OWNER ON 2 OCTOBER 2026** (`audit/OWNER_DECISIONS_2026-10-02.md`, row D7). Every
check is green on the checkpoint tree and every technical line below carries its evidence; with the owner's visual
acceptance recorded, the Design package is accepted and `COVERAGE.csv` writes `ACCEPTED` on its 1,415 verified rows
(the 18 `DESIGNED` rows stay as explained in §K). Recorded by the session meeting condition C2 of
`audit/PR8_INDEPENDENT_ACCEPTANCE.md`; no line below was re-evidenced or changed by it, except the two dated notes
under §F and §K that cite the owner's record. Not PUBLIC RELEASE READY; no WCAG conformance is claimed.
History — 28 September 2026: this line read **D7 TECHNICAL CHECKPOINT COMPLETE — FINAL VISUAL ACCEPTANCE WITHHELD**
(the gate's final visual acceptance was withheld by the owner, §K.4, last paragraph, so nothing here declared D7 met or
the Design package accepted).

`handoff/DESIGN_ACCEPTANCE_CRITERIA.md` completed line by line with evidence, on the checkpoint tree of branch
`claude/dreamy-archimedes-e8qx5v` (from the accepted `main` `0ccdf01`). A line without evidence is not met; every line
below names a test output, a file and line, a PNG under `design/evidence/`, or a note that says what was judged.
Nothing here is a WCAG conformance claim, a native-language certification, a rights clearance or a security guarantee.

**How the evidence was produced.** The reference site was built by `python3 design/reference/build.py`; every gate's
own check (D1–D6) and the D7 check were run on that tree; the three repository suites were run with
`YFIE_SITE_DIR=design/reference/out`, unedited. The outputs are pasted in §L. The D7 check is
`design/reference/check_acceptance.py` (a static phase over every document and frame, a browser phase over the
last-ten-percent surfaces in EN and AR; `--evidence design/evidence/d7` wrote the PNGs named below). Two independent cold
readers (English; Arabic) read the checkpoint tree (§K.4).

## A. Truth and authority

- [x] No file under `authority/`, `site-src/content/`, `dist/`, `audit/` was edited by hand; all gates pass on the final
  commit. — `git diff --stat 0ccdf01..HEAD -- authority site-src/content dist audit` is empty (the D7 pull request
  touches `design/**`, `docs/CHANGELOG.md`, `FINAL_REPOSITORY_MANIFEST.json`, `SHA256SUMS.txt` only — the README is
  untouched by the owner's hold); the
  `CONTRIBUTING.md` §5 gates on the final commit: §L.
- [x] Every number, label, date, source name and sentence of controlled meaning comes from `site-src/content/**`; no
  copied or hand-written content model. — `check_binding.py`: PASS — 39 projections by role (every RENDER and CONTRACT
  projection read by the content path, no REFERENCE or VIA_SPEC projection read anywhere, no copied content shipped
  beyond the runtime's two files); `check_content.py --text`: CONTENT PARITY PASS, 0 differing documents (every
  governed number of every document equals the baseline's); the withheld and no-locator rules below.
- [x] Every new interface label needed was requested as `NEEDS_CONTROLLED_CONTENT`, not authored. — `design/ESCALATIONS.md`
  (D1–D6 requests, each with its design impact; none filled); `check_visuals.py` and `check_acceptance.py`:
  "placeholders on the site: []" / `no_placeholder` on 288 documents and 310 frames.
- [x] No `⟦NCC:…⟧` placeholder and no invented wording; every optional feature whose labels are not governed is
  unshipped and listed. — The provider matrix's six placeholders of D6 are gone: the matrix is unshipped until its
  labels are governed and its contract renders as the text frame (DL-D7-001; `check_visuals.py`: "VIS-PROVIDER-OBSERVABILITY
  waits as a text frame until its labels are governed", `waits_as_text_frame` asserted on both routes × EN/AR); the
  exceptions map: `09_CODE_HANDOFF.md`, D7 table (the matrix, the export control, the social images as frames).
- [x] The withheld CLM-044 value never appears; the nine sources without a public locator are never named or linked;
  no third-party document is bundled or offered. — `check_acceptance.py` static: `withheld_value_never_printed` on
  `/en/evidence/CLM-044/` and `/ar/evidence/CLM-044/`; `no_locator_source_never_named` for each of the nine ids
  (`SRC-CCY-REMIT-ESTIMATE-2025`, `SRC-CCY-SAM-2024`, `SRC-CCY-CASH-DURATION-2026`, `SRC-CCY-ISP-2024`, `SRC-CCY-AMAL-2025`,
  `SRC-CCY-PRESSURE-2026`, `SRC-LIT-ALG-FI-COMPARATIVE`, `SRC-LIT-IND-FI-TEMPLATE-2023`, `SRC-MOPIC-YSEU-2023-080`) on
  every one of the 286 edition pages, in the text and in the data blocks (0 observations); `no_document_offered` and
  `no_download_attribute` on every page; the built site holds only `html`, `css`, `js`, `json` (the search index,
  aliases and per-page bundles), `png` (the canonical mark and the evidence crops of `_review`), `txt`, `woff2`
  (`find design/reference/out -type f`); `check_site.py` per record: `no_usd_value`, `no_source_named`,
  `no_locator_never_named` (CLM-044).
- [x] Evidence Records show the boundary as two labelled parts, part A alone where there is no measurement limitation,
  never the internal delimiter. — `design/reference/yfie/content.py` `boundary_parts` (line 249) splits the governed
  boundary at the governed delimiter into "does not establish" and "limits of the measure" and the record renders each
  under its governed label (`04_PAGE_FAMILY_COMPOSITIONS.md`, Evidence Record); `check_site.py --gate d4` asserts the
  boundary on first load on all 110 records × EN/AR (3,822 hard-state assertions, 0 failed); CLM-003 (both parts) and
  CLM-004 / CLM-015 (part A only) are in `design/evidence/d7/review-record-*.png` and `design/evidence/d2/evidence_CLM-004-*.png`.
- [x] No internal ID, enum, field name or repository term shown as prose; stable IDs as citation references are
  bidi-isolated. — `check_site.py`: `ids_isolated_ltr` on every record; `check_content.py` (governed text only);
  the D5 technical states render in the governed technical voice (`check_journeys.py`, 28 drives); the D3 and D7 cold
  readers report no internal vocabulary (§K.4).

## B. Coverage (both languages; 1440, 640, 390, 320 CSS px)

- [x] Global shell. — `04_PAGE_FAMILY_COMPOSITIONS.md` §1 and `03_COMPONENT_CATALOG.md` §1 (product bar with the
  Method & Measurement group, search, cite, report, language; the institutional band with the trust layer first;
  skip link; breadcrumbs where governed); `check_acceptance.py` static on all 286 edition pages: `skip_link_first`,
  `one_h1`, `language_switch_present`, `footer_trust:<route>` × 7 trust routes (label and link in the page's
  language), `html_lang_dir`; `check_site.py` hooks present per render. PNG: `design/evidence/d7/review-home-{en,ar}-{1440,390}.png`.
- [x] Home · Explore · eight domain routes · Evidence index · the §9.1 record set · Compare · Readings index · the
  Reading stress cases · Sources with the chronology · Measurement · Methodology · About and every trust route ·
  corrections/report journey · 404. — Each is a route row of `design/COVERAGE.csv` (route × EN/AR × 320/390/640/1440,
  `VERIFIED` with its check; `ACCEPTED` is written at acceptance); `check_site.py --gate d2` (Explore, the five hard domains, the Evidence directory,
  CLM-004, CLM-044, Compare, `/data/`), `--gate d3` (Home, the Readings, Measurement, Methodology, About, Contact,
  Corrections, the 404), `--gate d4` (`/firms/`, `/finance/`, `/providers/`, all 110 records); `check_trio.py`
  (Home, CLM-003, the flagship Reading); `check_journeys.py` (the report journey J10). Outputs in §L.
- [x] Every route in the inventory renders in both languages (the same 288 documents as `dist/`), bound through its
  family rules, reviewed on its own ledger row. — `check_binding.py`: 286 edition pages + root + 404, 286 bundles, a
  twin edition for every page; `check_site.py --gate d4`: 904 renders (every record and the three remaining domain
  answers × EN/AR × four widths); the ledger: 1,415 rows `VERIFIED` (`ACCEPTED` at acceptance), 18 catalogue-only rows
  `DESIGNED` with the gap explained (§J).
- [x] The small surfaces. — Footer: `footer_trust` above and `review-home-*-390.png`; search no-match and failed
  index: `check_journeys.py` `search_no_match`, `search_index_unavailable` (announced, technical voice, not an
  evidence gap) and `check_acceptance.py` `search_no_match_announced` with `design/evidence/d7/search-nomatch-{en,ar}-390.png`;
  the language switch on every family: `language_switch_present` × 286 and `language_switch_keeps_route`, the D5
  `language_switch_state` (the comparison kept); citation: the `yfie-citation` meta byte-equal with the baseline on
  every page and the cite control (`test_public_tools.py`); original-source links and the no-public-locator state:
  `source_locator_external_with_cue` on every locator of every page, `check_site.py` `no_locator_state`,
  `some_without_locator`; unavailable downloads: no download anywhere (`no_download_attribute`,
  `no_document_offered`), the export control designed and unshipped (`06_VISUAL_TABLE_SYSTEM.md` §8); print:
  `check_visuals.py --phases print` (133 checks); empty, unknown and error states and every tool message:
  `check_journeys.py` (28 technical-state drives: Compare wrong count, unknown id, malformed, duplicate, a real record
  outside the set; search no match and index unavailable; unknown source deep link, filter with no match; record
  context unknown, malformed, valid; the language switch keeping state; no JavaScript).
- [x] The family outcomes of brief §9.4; the Home cold-reader test at 390 and 1440 px in both languages. — D3: four
  fresh readers, EN/AR × 390/1440, verbatim in `design/evidence/d3/cold_read/*.md`, DL-D3-001/002 (the corrections
  made); D7: two independent cold readers on the checkpoint tree (§K.4). Family outcomes asserted per family by
  `check_site.py` (Home `statement_in_head`, `scannable_first_screen`; Explore `four_clusters_eleven_questions`;
  domain `band_before_primary`, `verify_path_present`; records `seven_questions`, `clock_before_claim`; Readings
  `standfirst_and_clocks`, `closing_section_headed`; `/data/` `all_public_sources`, `curated_28_by_category`;
  Methodology `plain_language`; Measurement `no_ordinal_numbering`; trust `purpose_role_limits_correction`).
- [x] The twelve hard-state cases; the withheld, composite, partial and framing records; every verification state with
  records shown on one; the two without records designed as states. — `check_site.py --gate d2`: 553 hard-state
  assertions on 44 route renders (dense_domain, sparse_unknown, institutional_sequence, vintage_conflict,
  verification_dense, verification_sparse, compare_unlike, source_scale, mobile_rtl; CLM-004 framing, CLM-044
  withheld, CLM-014/CLM-031 composite, CLM-039 partial); `--gate d3`: 252 (reading_longform,
  measurement_nonranking, trust_plain_language); `--gate d4`: 3,822 (every record against its own bundle);
  `SOURCE_NOT_YET_BOUND` and `NO_SOURCE_RECORD` designed with their governed copy, never on an invented record
  (DL-D5-003; ledger rows "(component catalogue)").
- [x] The thirteen journeys succeed by keyboard, mobile and desktop, both languages. — `check_journeys.py`: 52 journey
  walks (13 × EN/AR × mobile/desktop), 52 passed; `design/evidence/d5/J*-end.png`.
- [x] Every technical state reachable and technical, never "no evidence"; every evidence gap looks like evidence. —
  `check_journeys.py`: 28 technical-state drives, 28 passed (`technical_voice`, `not_evidence_gap`,
  `navigation_works` on each); `07_INTERACTION_ACCESSIBILITY.md` §4.

## C. The semantic firewall in the interface

- [x] Each distinction has a visible, non-colour-only treatment; a cropped component carries unit, population, period
  and boundary. — `01_FOUNDATIONS.md` §5 and `03_COMPONENT_CATALOG.md` §3 (the state grammar: mark shape, line style,
  governed label); `check_visuals.py`: `markers_labelled`, `palette_only`, 48 forced-colours and print checks
  (marks and labels survive without colour); every figure's detached frame (`boundary_once_in_foot`,
  `scope_in_frame`); the compact evidence object carries its clock, population and state (`check_site.py`
  `clock_before_claim`).
- [x] No composite score, traffic light, ranked summary or synchronised "current state" panel. — `check_site.py`:
  `no_pills_no_cards`, `no_lifted_number`, `no_manufactured_history`, `no_ordinal_numbering`; VIS-FIRM-CONSTRAINTS drawn
  without ranks (DL-D6-002); no red, amber or green in the palette (`02_TOKENS.json` → `colour`).
- [x] Measurement priorities read as sequencing within the agenda. — `check_site.py --gate d3` on `/measurement/`:
  `priority_label_governed`, `no_ordinal_numbering`, `ten_priorities_deep_linkable`; `design/evidence/d3/measurement-*.png`.
- [x] The chronology reads as context, never as a causal chain. — `check_site.py --gate d2` on `/data/` and `/finance/`:
  `chronology_24`, `chronology_bound`, `events_dated_with_sources`, `no_manufactured_history`; the dated lanes end in
  an OPEN outcome node, no arrow of flow (`06_VISUAL_TABLE_SYSTEM.md` §3).
- [x] Proximity, shared axes, colour, sequence and motion never make unlike things read as one; a repeated figure is
  never independent corroboration. — `check_site.py`: `pos_three_panels_own_axes`, `not_comparable_marked`,
  `reading_linked_not_redrawn`, `ma001_apart`; `06_VISUAL_TABLE_SYSTEM.md` §2 ("never shares an axis, a row or a lane
  between unlike series"); no motion anywhere (§H).

## D. Tools

- [x] Search. — `test_public_tools.py` 25/26 (1 not applicable to the current data) on the reference site: as-you-type,
  Arabic normalisation, ranking, result types, shortcuts, focus, announced results, lazy index; `check_journeys.py`
  `search_no_match`, `search_index_unavailable`; `check_acceptance.py` `search_no_match_announced`,
  `escape_closes_search_returns_focus`; `07_INTERACTION_ACCESSIBILITY.md` §2.
- [x] Compare. — `test_public_tools.py`; `check_journeys.py` (the five Compare technical states; `language_switch_state`
  keeps the comparison); `check_site.py`: `verdict_before_table`, `verdict_in_boundary_voice`, `boundary_before_controls`,
  `compare_entry` on every comparable record's page; `check_acceptance.py`: `compare_320_stacked_labelled_verdict_first`
  (`design/evidence/d7/compare-{en,ar}-320.png`).
- [x] Sources. — `check_site.py --gate d2` on `/data/`: `all_public_sources`, `curated_28_by_category`,
  `every_source_named_or_referenced`, `locators_public`; `check_journeys.py` `source_link_unknown` (announced link
  error), `source_filter_no_match`; filtering by governed category only (`data-source-filter` on governed fields).
- [x] Cite, report an issue, language and download. — Cite: `test_public_tools.py` (copy, announced), the
  `yfie-citation` meta on every page; report: `check_journeys.py` `record_context_*` and `check_acceptance.py`
  `record_context/contact/`, `record_context/corrections/` (`design/evidence/d7/contact-*.png`, `corrections-*.png`)
  — client-side composition into the existing mail action, no form element (`no_form_frame_object` on every
  document), no new address; language: above; download: the pattern with its disabled state designed and unshipped
  (`06_VISUAL_TABLE_SYSTEM.md` §8; `09_CODE_HANDOFF.md`).
- [x] No CauseWay-content download or export before OWN-04; no third-party document; the four kinds of material
  distinct; CauseWay's identity never implies ownership of source data. — §A (no download, no document);
  `/rights/` and `/data/` governed text (`design/evidence/d7/trust-rights-{en,ar}-390.png`); every source card names its
  publisher and the credit line of every frame is the source's (`credit_isolated`).
- [x] Every input has a reason, a visible label, a text error, preserved input, keyboard and touch, RTL, success and
  failure states; a way on from a no-match; external links visibly external without an interstitial;
  micro-interactions designed; Escape closes and returns focus. — `compare_320_stacked_labelled_verdict_first`
  (`select.labels`), the search input's accessible name (`aria-label` in `render.py`), `check_journeys.py`
  (`role="alert"` text errors, preserved input); `search_no_match_announced` (the governed no-match copy offers the way
  on); `source_locator_external_with_cue` on every locator (`target="_blank"`, `rel="noopener noreferrer"`, the
  governed "Open original source ↗" or the "↗" glyph named by its `aria-label`); `escape_closes_search_returns_focus`;
  `07_INTERACTION_ACCESSIBILITY.md` §2.
- [x] The two suites pass against the reference implementation, unedited, hooks kept. — `git diff 0ccdf01..HEAD --
  scripts/tests/test_public_tools.py audit/tranche_c/checks/viewport_acceptance.py` is empty; outputs in §L:
  PUBLIC TOOL TESTS PASS: 25/26 passed, 1 not applicable to the current data · VIEWPORT ACCEPTANCE: 168/168
  page-width checks pass.

## E. Readings

- [x] Title, standfirst and evidence tension first; governed metadata; the essay ends with "What would change this
  reading?"; the prohibited inference visible; at most one signature visual; the trace and related Readings follow. —
  `check_site.py --gate d3` on the ten Readings: `standfirst_and_clocks`, `boundary_before_essay`, `essay_sections`,
  `closing_section_headed`, `at_most_one_figure_after_opening`, `trace_to_records`, `related_one_or_two`;
  `design/evidence/d7/review-reading-{en,ar}-{1440,390}.png`.
- [x] One Featured Reading on Home and on Explore; at most two on a domain page; records list the Readings that use
  them; priorities link where their gap is examined; no carousel or card wall. — `check_site.py`: Home `featured`
  object, `/readings/` `featured_then_all`, domain `readings_at_most_two`, records `used_in_readings`, `/measurement/`
  `gaps_examined_links`; `no_pills_no_cards`.
- [x] A Reading prints — and saves as PDF from the browser — in its document layout in each language. —
  `check_visuals.py --phases print` on `/readings/same-year-different-number/` × EN/AR (chrome hidden, the title on
  page one, every figure whole with its foot, the provenance block last); `design/evidence/d6/print-readings_same-year-different-number-*.png`
  (twelve pages, both languages); `06_VISUAL_TABLE_SYSTEM.md` §7.

## F. Visuals

- [x] SIGNATURE and CORE_ANALYTICAL follow their data contracts; SUPPORTING plots no values; TABLE_TEXT_FIRST and
  RETIRE never drawn. — `check_visuals.py --phases contracts`: 36 contracts × EN/AR on every binding route, 2,812
  assertions, 0 failures (`drawn`, `values_printed`, `withheld_never_printed`, `no_value_plotted`, `never_a_chart`,
  `record_page_has_no_figure`; the waiting matrix `waits_as_text_frame`).
  Note, 2 October 2026: the RETIRE contract VIS-CAPITAL-CONTEXT is never drawn, but this build shows it on `/reforms/` as a
  governed text frame in the depth group — a frame the pre-design baseline did not have (`audit/PR8_INDEPENDENT_ACCEPTANCE.md`
  A5). The owner decided on 2 October 2026 that the RETIRE_FROM_DESIGN tier is excluded from the domain depth frames and
  the frame is removed in the release-candidate pull request; the Evidence Record text stays (`audit/OWNER_DECISIONS_2026-10-02.md`, row A5 / C4).
- [x] Legends and labels only from `UI-VIS-*` and `<field>_label`; colour never the only carrier; no red/amber/green;
  nothing fades with age; breaks, gaps and disagreements drawn. — `markers_labelled`, `palette_only` (the ten palette
  values), the forced-colours checks; `03_COMPONENT_CATALOG.md` §3 (every grammar state's governed label);
  `check_site.py` `break_not_joined`, `missing_month_gap`, `disagreement_marked`, `projection_dashed`.
- [x] Analytical alt text and a table or ordered-text fallback; the detached frame travels with any export; RTL and
  narrow forms per contract. — `alt_text` (the governed alt text, `data-visual-fallback="ordered-text"`,
  `data-image-independent`), `table_with_caption_and_scoped_headers`, `table_columns_named_and_region_named` on every
  drawn contract; 24 export frames checked (foot with boundary, edition and canonical link; the identity line); `fits_320`,
  `fits_390`, `fits_600` on both edges in both languages; `svg_ltr`.
- [x] Anything revealed on interaction comes from governed fields and is reachable by focus, keyboard and touch and in
  the static fallback; hover is never the only way in. — No figure reveals anything on hover: every value, state and
  note is printed in the drawing and in the table (`03_COMPONENT_CATALOG.md` §2); the only interactive elements inside a
  figure are links and the cite control, each a 24 px target (`targets_24px`); `check_journeys.py` keyboard walks.

## F2. Print and portable evidence

- [x] Every page family has a print style; chrome hidden; title, edition, canonical URL and language kept; figures
  printed with period, population, unit and boundary; "What not to conclude" with its claim; charts never split from
  caption and fallback; Arabic prints right to left; no meaning by colour. — `check_visuals.py --phases print`: 133
  checks on the eleven family routes × EN/AR to PDF (PyMuPDF), 0 failures; `--phases degraded`: 48 checks (forced
  colours and print on the twelve drawn contracts); `@media print` in `theme.CSS_D6` (`06_VISUAL_TABLE_SYSTEM.md` §7);
  PNG print previews of Home, CLM-003 and the Reading in both languages: `design/evidence/d6/print-home-*.png`,
  `print-evidence_CLM-003-*.png`, `print-readings_same-year-different-number-*.png` (no PDF committed).
- [x] Contextual chart and table exports carry the full detached frame and ship disabled until OWN-04. —
  `frames.export_document`: 24 frames (twelve drawn contracts × EN/AR; the matrix's joins when it draws) each asserted
  (`check_frames`: the foot's boundary, edition and canonical link, the identity line, no overflow, no script, no inline
  style, no loose date); `design/evidence/d7/review-export-RV-CWR-001-{en,ar}-900.png`; the control unshipped
  (`06_VISUAL_TABLE_SYSTEM.md` §8; `09_CODE_HANDOFF.md`).
- [x] Any fragment that can leave the page keeps provenance and limits. — Print: the provenance block (product ·
  edition · canonical URL · citation) last on every page (`check_visuals.py` print phase); export: above; citation:
  the `yfie-citation` meta and the cite control's text carry title, product, record id, publisher, edition, period and
  population; social frames: 286 checked (`soc-title`, canonical, edition, the mark, no overflow at 1200 × 630).

## G. Arabic and English

- [x] Arabic natively composed (own type scale, line height, rhythm, order). — `05_RESPONSIVE_RTL_LTR.md` §3–§4 (the
  two scales; the thirteen `[dir=rtl]` rules over logical properties; charts unmirrored); `02_TOKENS.json` → `type.arabic`;
  `design/evidence/d7/review-home-ar-{1440,390}.png`, `review-record-ar-*.png`, `review-reading-ar-*.png`; the D6
  Arabic lens and the D7 Arabic cold reader (§K.4).
- [x] Mixed-script runs isolated; digits Western; dates and units in the governed forms. — **Closed 2026-09-28 (DEBT-018, DL-D7-006):** a
  governed signed value in Arabic prose ("+11%") is outside the isolate and renders "%11+" (verified on `/payments/` and
  CLM-003 at the checkpoint; found by the Arabic cold reader); fixed at the resumption. Otherwise `check_visuals.py --phases
  text`: 596 documents and frames scanned, no ISO date or numeric range outside an isolate; `iso_dates_isolated` per
  figure and frame in the browser; `05_RESPONSIVE_RTL_LTR.md` §5; the one formatter (`visuals.num`); the governed
  Arabic month names (`content.date_words`).
- [x] `bilingual_invariance.py` reports 0 differing page pairs. — BILINGUAL NUMERIC INVARIANCE: 0 page pairs with
  differing numbers (143 pairs checked), `YFIE_SITE_DIR=design/reference/out` (§L).
- [x] Dates follow the governed form. — `content.date_words` (day, governed month name, year, Western digits) is the
  only date-in-words path; ISO dates and free-text time boundaries print as the Master holds them, isolated
  (`visuals.date_token`); `check_content.py` parity with the baseline.
- [x] No English-only metadata disappears in Arabic; no internal vocabulary in either language. — Head parity with the
  baseline on every Arabic page (title, description, canonical, hreflang, Open Graph, citation meta, JSON-LD);
  `check_content.py` parity per document; the English governed time boundaries and credit lines print in Arabic
  frames isolated and marked `lang="en"` (escalated as content, `ESCALATIONS.md` D6).
- [x] Arabic tested, not only viewed. — Hierarchy, RTL flow, mixed script, numerals, source names, tables, charts and
  legends: `check_visuals.py` per contract in AR (1,406 of the 2,812 assertions), the D6 Arabic lens (DL-D6-007);
  inputs and search: `check_journeys.py` AR walks and drives, `design/evidence/d7/search-nomatch-ar-390.png`; citation
  and exports: `review-export-RV-CWR-001-ar-900.png`; print: the AR print checks; mobile and the longest strings:
  `design/evidence/d7/longest-title-ar-320.png` (`longest_title_fits_320`), `compare-ar-320.png`; punctuation and the
  language switch: the D6 lens and `language_switch_keeps_route`; the D7 Arabic cold reader (§K.4).

## H. Accessibility outcomes (WCAG 2.2 target — outcomes as tested, no conformance claim)

- [x] Keyboard access and order; no trap. — `check_journeys.py`: 52 walks by keyboard only; `escape_closes_search_returns_focus`;
  the menu closes on Escape and on focus leaving (`07_INTERACTION_ACCESSIBILITY.md` §2).
- [x] Visible focus that sticky UI never obscures. — `check_acceptance.py` `skip_link_first_tab_outlined`
  (`design/evidence/d7/focus-skip-{en,ar}-390.png`): a 3 px double outline in the counter colour, offset 3 px; the only
  sticky element is the side spine from 900 px, capped at `calc(100vh - 40px)` and scrolling inside itself
  (`05_RESPONSIVE_RTL_LTR.md` §1).
- [x] Targets ≥ 24 × 24 CSS px (44 for primary touch controls). — `check_site.py`: every link and button in `#main`
  ≥ 24 px per render (904 + 168 + 168 + 24 renders); `check_visuals.py` `targets_24px` per figure; the product-bar
  controls ≥ 44 px (`02_TOKENS.json` → `space.hit area`).
- [x] Reflow at 320 CSS px and 400 % zoom; tables scroll inside a named, focusable region. — Every one of the 288
  documents at 320 px without horizontal page scroll (`check_site.py`); VIEWPORT ACCEPTANCE 168/168; every table in
  `div.table-wrap[role=region][aria-label]`, focusable only when it can scroll (`table_columns_named_and_region_named`,
  `table_in_named_region`); the Compare table stacks below 640 px (`compare-{en,ar}-320.png`).
- [x] Names, roles, landmarks, one `<h1>` per page; headings describe sections. — `one_h1` on every document;
  `check_site.py`: one h1, skip link first, every in-page navigation named by the page's h1 (`strip_named`), `dir` per
  language; figure names are their governed titles and inner headings sit one level under (`06_VISUAL_TABLE_SYSTEM.md` §2).
- [x] Labelled inputs; text errors; announced status. — `select.labels` on the four Compare slots; the search inputs'
  `aria-label`; `role="alert"` text errors and `role="status"` regions (`check_journeys.py` `announced`;
  `test_public_tools.py` "technical-error and status regions are announced").
- [x] Contrast 4.5:1 (text) and 3:1 (UI, graphics); no meaning by colour alone. — On the token values (WCAG relative
  luminance): ink 16.29:1 on paper and 14.46:1 on plaster; ink-2 9.21 / 8.18; ochre 6.35 / 5.64; counter 8.39 / 7.45;
  mute 4.98 on paper (its role forbids it on plaster, `02_TOKENS.json`). Chart marks, paths, axes, ticks, bars and the
  lanes' spans are ink; the break, the missing gap and the disagreement ring are counter (≥ 7.45:1); the grid and the
  stems (rule-2, 2.03:1) carry no meaning. No red, amber or green; state by shape, line and label (§C, §F).
- [x] Analytical text alternatives for every visual. — `alt_text` asserted on all 36 contracts × EN/AR × every route.
- [x] RTL focus and reading order. — The Arabic half of the 52 journey walks (focus order = reading order); the
  document order is the same in both editions (`05_RESPONSIVE_RTL_LTR.md` §4).
- [x] Reduced motion honoured; nothing needs motion. — `check_acceptance.py` `no_motion_default`, `no_motion_reduced`
  (no element with a transition or animation on Home under either preference); `@media (prefers-reduced-motion:reduce)`
  (`theme.py`, line 207); `02_TOKENS.json` → `motion`: none by design.
- [x] Single-pointer operation; no drag-only interaction. — No drag interaction exists: the tools are links, buttons,
  text inputs and native selects (`03_COMPONENT_CATALOG.md` §4); every path walked by keyboard.
- [x] Forced-colours mode and image-off keep every meaning. — `check_visuals.py --phases degraded`: 48 checks (every
  drawn mark and label takes `CanvasText`); `check_site.py --degraded` renders (20 + 18 + 10 ok; forced colours, no
  stylesheet, images off); no image carries evidence (the only image is the mark, with `alt`).

## I. Identity, performance, discovery, security

- [x] The logo is the canonical file, unmodified, at specified sizes and clear space; no CSS filter, blend or mask;
  derivative sizes listed for Code. — `build.py` copies `site-src/assets/CauseWay_Master_Logo.png` unchanged; no
  `filter`, `mix-blend-mode`, `mask` or `invert` in `theme.py` (grep at D7); `08_ASSET_MAP.md` §1 (placements, sizes,
  clear space, the derivative sizes for EAD-03); `check_frames` `logo` and `ident` (the unaltered file with `alt`).
- [x] IBM Plex Sans and IBM Plex Sans Arabic self-hosted from `vendor/fonts/`, licence shipped, files as shipped; any
  other family member with a rationale; no other typeface. — `check_acceptance.py` `font_file_shipped` × 6,
  `licence_shipped` × 2; `build.py` `copytree` of the two folders unchanged; `08_ASSET_MAP.md` §2 (three faces per
  family, why); `theme.FONT_FACES`.
- [x] No third-party resource; fonts loaded efficiently — only the weights used, the critical faces preloaded, a
  deliberate `font-display`, no self-made subset; no decorative imagery; per-family page weight recorded with the
  method; no green claim. — `no_external_resource` on 598 documents and frames, `no_external_url_in_css`; six faces
  declared with `font-display: swap`; every page preloads Regular and SemiBold of its language (`render.font_preloads`,
  DL-D7-005); no subset made. Page weight of the reference build, measured at D7 as the static bytes a cold load
  fetches (the document + `yfie.css` 48 KB + `app.js` 23 KB + the six font files 411 KB; warm = the document alone;
  the canonical mark, 9.6 MB, is served unaltered by rule on every page — DEBT-016 / EAD-03 — and is not in the
  column) — the method follows `docs/SUSTAINABILITY_METHOD.md` (static bytes, no network); no claim of any kind follows:

  | Family | Route measured | Document EN / AR | Cold load EN / AR (without the mark) |
  |---|---|---|---|
  | Orientation | `/` | 24 / 31 KB | 506 / 514 KB |
  | Question Entry | `/explore/` | 24 / 31 KB | 506 / 513 KB |
  | Domain Answer | `/people/` | 45 / 58 KB | 527 / 540 KB |
  | Evidence Directory | `/evidence/` | 71 / 93 KB | 554 / 576 KB |
  | Evidence Record | `/evidence/CLM-003/` | 25 / 31 KB | 507 / 513 KB |
  | Comparison | `/evidence/compare/` | 43 / 61 KB | 526 / 543 KB |
  | Reading Index | `/readings/` | 18 / 22 KB | 500 / 504 KB |
  | Reading | `/readings/same-year-different-number/` | 43 / 55 KB | 526 / 537 KB |
  | Data & Source | `/data/` | 303 / 361 KB | 785 / 843 KB |
  | Measurement | `/measurement/` | 42 / 58 KB | 525 / 540 KB |
  | Reference / Trust | `/about/` | 16 / 21 KB | 499 / 503 KB |

- [x] Head elements kept: title, description, canonical, hreflang (en, ar, x-default), Open Graph without image,
  JSON-LD as today; social templates cover all eleven families. — `check_acceptance.py`: nine head parts byte-equal
  with `dist/` on every one of the 286 edition pages (`head_equals_baseline:*`), `no_og_image`; DL-D7-002; 286 social
  frames checked, five templates over the eleven families (`08_ASSET_MAP.md` §4).
- [x] Strict-CSP compatible. — `check_acceptance.py` on 288 documents and 310 frames: `script_is_data_or_same_origin`
  (every `<script>` a JSON or JSON-LD data block or `/assets/app.js` / `/assets/lang-redirect.js`), `no_inline_style`,
  `no_inline_handler`, `no_form_frame_object`, `no_external_resource`; `check_visuals.py` `no_inline_style` per figure.
- [x] No image without purpose, provenance and rights decision; no count-up, parallax or motion; the dark-mode decision
  recorded; the logo never inverted or recoloured. — The only image is the canonical mark (`08_ASSET_MAP.md` §1); no
  motion (§H); dark mode not explored, with the reasons (DL-D7-003); no filter or inversion (above; EAD-04 applies to
  the baseline's footer, not to the reference).
- [x] Core evidence readable before any script runs; `design/reference/out/` a self-contained hostable static site. —
  `check_journeys.py` `no_javascript` (the governed note, every answer, record and boundary readable, navigation works);
  `check_acceptance.py` and every check serve the folder with Python's `http.server` exactly as `00_DESIGN_README.md` §1
  documents; the folder holds the HTML of every route, the root entry, the 404, the stylesheet, the runtime, the mark,
  the fonts with their licences, the search index and the page data blocks.

## J. Package and handoff

- [x] `design/00`–`10`, `ESCALATIONS.md`, `COVERAGE.csv`, `DESIGN_DEBT.md` and the runnable `design/reference/` exist;
  `00_DESIGN_README.md` says how to build and preview. — `ls design/`: `00_DESIGN_README.md`, `01_FOUNDATIONS.md`,
  `02_TOKENS.json`, `03_COMPONENT_CATALOG.md`, `04_PAGE_FAMILY_COMPOSITIONS.md`, `05_RESPONSIVE_RTL_LTR.md` (written at
  D7), `06_VISUAL_TABLE_SYSTEM.md`, `07_INTERACTION_ACCESSIBILITY.md`, `08_ASSET_MAP.md`, `09_CODE_HANDOFF.md`,
  `10_ACCEPTANCE_CHECKLIST.md` (this file), `COVERAGE.csv`, `DESIGN_DEBT.md`, `ESCALATIONS.md`, `reference/`,
  `evidence/`, `exploration/`, `architecture/`; `00_DESIGN_README.md` §1 (build: `python3 design/reference/build.py`;
  preview: `python3 -m http.server 4173 --directory design/reference/out`).
- [x] D0 recorded whether a board or mockup was supplied. — `00_DESIGN_README.md` §3 (none in the repository; nothing
  absent treated as binding; DL-D0-002).
- [x] D1 tested two or three materially different theses on the trio in both languages before propagation, recorded
  with the choice. — `01_FOUNDATIONS.md` §1–§3 (T1 Register, T2 Argument, T3 Strata, the second-generation T4
  Instrument; the independent lenses; the convergence, §3.6), DL-D1-005/006; `design/evidence/d1/`.
- [x] The decision log has entries for every gate D0–D7 with the fields of brief §19; the ledger shows every route ×
  language × width and every state `ACCEPTED` with its checks and `code_handoff` `YES`, or explains each gap. —
  `00_DESIGN_README.md` §9: DL-D0-001…003, DL-D1-001…008, DL-D2-001…008, DL-D3-001…005, DL-D4-001…004, DL-D5-001…004,
  DL-D6-001…007, DL-D7-001…005; `COVERAGE.csv`: 1,433 rows — 1,415 `VERIFIED` at the checkpoint (the `ACCEPTED` status with the D7 evidence per row is written only
  when the gate is accepted, which the owner had withheld; written on 2 October 2026 on the owner's recorded acceptance, `audit/OWNER_DECISIONS_2026-10-02.md`), `code_handoff` `YES` on every row; 18 rows `DESIGNED` with the gap explained (the two verification
  states no record carries, `SOURCE_NOT_YET_BOUND` and `NO_SOURCE_RECORD`, and the seven grammar states no governed
  contract row carries — HISTORICAL, PROGRAMME, PARTIAL, UNKNOWN, BREAK_UNIVERSE, TARGET, RESULT — each designed in the
  catalogue with its governed label and never drawn on an invented record or row).
- [x] `DESIGN_DEBT.md` lists every deliberate temporary compromise; none open blocks D7; each open one has its Code
  action in `09_CODE_HANDOFF.md`. — Nineteen entries, closed not deleted. Closed at the D7 checkpoint: DEBT-002,
  DEBT-013, DEBT-017 (DL-D7-001/004) and DEBT-018 (DL-D7-006). Closed at the D7 closure: DEBT-019 (DL-D7-007),
  DEBT-014 and DEBT-015 (DL-D7-009), and DEBT-007 decided as restraint with its reasoning recorded. **Three remain
  open and none blocks D7.** DEBT-011 (`/data/` length) was attempted and reverted at the closure — closing the
  dependency groups cut the page 44 % but put the governed "cite a locator-only source" path behind a disclosure and
  failed the repository's public-tool suite, so the change was reverted rather than a test weakened for it, and the
  measured prize and the constraint are recorded for whoever takes it next (DL-D7-013). The other two are flagged
  "blocks release": DEBT-008 (a
  governed pacing marker for the Home paragraph; Code keeps the `paced_groups` whole-paragraph fallback) and
  DEBT-016, narrowed at the closure to the file weight alone — the publisher is now named in type on every first
  screen in both languages (DL-D7-008), and what remains is the owner's web-weight rendering of the unaltered mark
  (EAD-03), at the derivative sizes specified in `08_ASSET_MAP.md` §1. Each has its Code action in the "Design debt"
  row of the D7 table in `09_CODE_HANDOFF.md`.
- [x] `09_CODE_HANDOFF.md` maps tokens, components, states, routes, content bindings, visual contracts, responsive
  rules, accessibility behaviour and every exception. — The D1–D7 tables (each gate's rows, the newest superseding),
  "Must not be reinterpreted", "Temporary vs intended", "Owner / release items"; with `02_TOKENS.json` (tokens),
  `03_COMPONENT_CATALOG.md` (components, states, tools), `04_PAGE_FAMILY_COMPOSITIONS.md` (routes and bindings),
  `06_VISUAL_TABLE_SYSTEM.md` (contracts, print, export), `05_RESPONSIVE_RTL_LTR.md` (responsive, RTL),
  `07_INTERACTION_ACCESSIBILITY.md` (accessibility, test hooks) — the map `handoff/DESIGN_TO_CODE_CONTRACT.md` §3 requires.
- [x] No consequential decision exists only in an image or an external design file. — Every decision is a
  decision-log entry; the PNGs under `design/evidence/` illustrate and never decide; the D1 canvas is regenerated by
  committed composers (DEBT-004).
- [x] Every open escalation is listed with its design impact; none silently worked around. — `ESCALATIONS.md`: every
  entry carries "Design impact"; the D6 matrix requests are annotated with the D7 state (unshipped, DL-D7-001); the
  D7 process note names the branch.

## K. Review tests and the last 10 percent

- [x] The four review tests applied to Home, a dense Evidence Record, a Reading, a domain answer with a visual, Compare
  and an export frame, in both languages, with the result and any revision recorded. — Surfaces and evidence:
  Home (`design/evidence/d7/review-home-{en,ar}-{1440,390}.png`), `/evidence/CLM-003/` (`review-record-*`),
  `/readings/same-year-different-number/` (`review-reading-*`), `/people/` (`review-domain-*`),
  `/evidence/compare/?records=CLM-001,CLM-010` (`review-compare-*`, `compare-*-320.png`), the RV-CWR-001 export frame
  (`review-export-RV-CWR-001-{en,ar}-900.png`).

  | Test | Result on the six surfaces, EN and AR | Revision |
  |---|---|---|
  | Anti-template | Without the Yemen content and the CauseWay mark nothing sells as a generic NGO, consultancy, SaaS or AI site: no cards, hero, tiles, badges, gradients, stock imagery or dashboard; the identity is the page object with its rule and rubric, the seven governed questions, the boundary voice, the clock-first objects and the detached frame — carried the same way in Arabic on its own scale | none |
  | Source owner | Every figure and record object shows its unit, population, period, evidence state and the source institution's name beside the value; the boundary is printed once in the object's own frame; the credit line is the source's; a source institution seeing the CLM-003 record, the `/people/` figure or the export frame alone reads exactly what its publication reported and no more | none |
  | Screenshot misuse | A crop of any figure keeps its scope line, state labels, boundary and canonical link; the same-year marker sits between the two rows it qualifies so a crop never reads as a fall; the Compare verdict precedes the table and states comparability before any value; the record's headline paragraph carries its scope in the sentence | none |
  | Portable evidence | The export frame carries the identity line, the whole detached frame and the canonical link; the print page ends with the provenance block; the citation names the record, the product, the edition, the period and the population; the social frame carries title, canonical URL and edition | none |

- [x] The last-10-percent audit done after the flagship pages were accepted, each item with evidence. —

  | Item (brief §20, D7) | Evidence |
  |---|---|
  | Search and zero results | `search_no_match_announced` EN/AR; `check_journeys.py` `search_no_match`, `search_index_unavailable`; `design/evidence/d7/search-nomatch-{en,ar}-390.png` |
  | Contact | `record_context/contact/` EN/AR; `design/evidence/d7/contact-{en,ar}-390.png`; `check_site.py --gate d3` `contact_actionable`, `address_actionable` |
  | Corrections and evidence challenge | `record_context/corrections/` EN/AR; `design/evidence/d7/corrections-{en,ar}-390.png`; `check_journeys.py` J10 and `record_context_*`; `check_site.py` `util_record`, `mail_hidden_without_record` |
  | Source and external links | `source_locator_external_with_cue` on every locator of every page; `check_site.py` `locators_public`, `source_cards_as_bundle`; `check_journeys.py` `source_link_unknown` |
  | Citation | `head_equals_baseline:<meta name="yfie-citation"` on every record; `test_public_tools.py` (cite copies and announces) |
  | The language switch | `language_switch_present` × 286; `language_switch_keeps_route` EN/AR; `check_journeys.py` `language_switch_state` |
  | Mobile tables | `compare_320_stacked_labelled_verdict_first` (`compare-{en,ar}-320.png`); `check_visuals.py` `tables_320`, `tables_390` on every drawn contract; no page-wide scroll on any document at 320 px |
  | Long Arabic strings | `longest_title_fits_320` (`/ar/payments/`, 156 characters; `design/evidence/d7/longest-title-ar-320.png`); DEBT-017 measured and closed (DL-D7-004) |
  | Focus | `skip_link_first_tab_outlined` (`focus-skip-{en,ar}-390.png`); `escape_closes_search_returns_focus`; the 52 keyboard walks |
  | Inputs | the four labelled Compare selects; the search inputs' names; `check_journeys.py` text errors and preserved input |
  | Privacy | `/privacy/` renders in both languages (`trust-privacy-{en,ar}-390.png`); no cookie, account, analytics, form or external resource on any document (`no_form_frame_object`, `no_external_resource`); `yfie-lang` the only stored preference |
  | Rights | `/rights/` (`trust-rights-{en,ar}-390.png`); no download or document offered; the credit line on every frame |
  | Unavailable downloads | `no_download_attribute`, `no_document_offered` on every page; the export control unshipped with its designed disabled state (`06_VISUAL_TABLE_SYSTEM.md` §8) |
  | Print | `check_visuals.py --phases print` (133 checks); `--phases degraded` (48); the D6 print PNGs |
  | Reduced motion | `no_motion_default`, `no_motion_reduced` EN/AR |
  | 404 | `not_found_bilingual` (`design/evidence/d7/not-found-neutral-390.png`); `check_site.py --gate d3` (the bilingual 404, degraded render) |
  | The footer | `footer_trust:<route>` × 7 on every page; `review-home-*-390.png` |
  | Every trust surface | `trust_route/<route>` × 8 × EN/AR (`trust-{about,accessibility,contact,corrections,methodology,privacy,rights,terms}-{en,ar}-390.png`); `check_site.py --gate d3` `purpose_role_limits_correction`, `plain_language` |
  | Every hard state | `check_site.py --gate d2` 553, `--gate d3` 252, `--gate d4` 3,822 hard-state assertions, 0 failed |

- [x] The Code recipient test passes on the checkpoint commit. — `00_DESIGN_README.md` (the status: what is met, what is
  temporary, what remains; DL-D7-001…005), `09_CODE_HANDOFF.md` (the D7 table: implemented, waiting, temporary,
  intended, the exceptions, the Code actions per debt, the tests that must pass, the owner and release items),
  `COVERAGE.csv` (every row's status, checks and evidence), `DESIGN_DEBT.md` (open with its Code action), `ESCALATIONS.md`
  (every open request with its design impact). A cold Code recipient reads what is intentional, temporary,
  implemented and remaining, what must not be reinterpreted (`09` "Must not be reinterpreted"), which tests must pass
  (§L, and the check commands in `00` §1) and which owner or release items remain (`09`, `FINAL_OPEN_ITEMS_REGISTER.md`).

### K.4 Independent cold readers on the checkpoint tree

Two fresh agents with no repository or conversation context read the built site as a researcher, a regulator and a
journalist — one the English edition (13 routes and the search), one the Arabic edition (12 routes and the search) —
and reported only material findings; their reports are verbatim in `design/evidence/d7/cold_read/en.md` and `ar.md`.
Every finding was verified on the built pages and adjudicated (a reader's words are the reader's, not a finding of fact):

| Reader · finding | Verified | Adjudication |
|---|---|---|
| EN 1 · `/people/` §02 states no education gap exists while VIS-FINDEX-GAPS plots 19.53 % and a 12.55-point gap | Yes — the governed section text (both editions) against the governed contract rows | Content: `ESCALATE_TO_MASTER` (defect claimed), `ESCALATIONS.md` D7; Design changes nothing governed |
| EN 2 · search shows ten hits without a total ("10 results shown" for 79 matches) | Yes — the baseline runtime caps at ten; the governed status has no "of N" | Runtime + label: `NEEDS_CONTROLLED_CONTENT`; Code item (`09`, D7 table) |
| EN 3 · Explore "04 · Questions to start from" with no questions under it | Yes — section 5 rendered twice (its body is the questions' introduction, D2 rule) | **Closed at the resumption — DEBT-019** (DL-D7-007): section 5 renders once, at the top, as the answer that holds the clusters (its role as the rubric, its governed heading as the `h2`, its body as the clusters' introduction, the interface lead kept for text parity); no second, question-less rendering exists |
| EN 4 · text-only "Another view of the evidence" boxes repeat the section and the boundary | Yes — governed alt text restating the prohibited inference (raised at D3) | Content: restated in `ESCALATIONS.md` D7; the bound contract must appear as a framed object |
| EN 5 · the visible text description and table under a chart print nine values three times | Yes — by design | Not changed: the Lock keeps the text alternative visible (print, no-script and assistive-technology parity); recorded (DL-D7-003) |
| EN 6 · Compare's governed "01 Three measures that cannot be combined" reads as the analysis of the selected pair | Yes — the D2 order (the tool as the first answer) | Content/order: `ESCALATE_TO_MASTER` (observation); the order stands |
| EN 7 · only 13 records comparable, refusal without a reason | Yes — the comparable set is governed; the error copy is the runtime's | `NEEDS_CONTROLLED_CONTENT` (a governed sentence on the comparable set) |
| EN 8 · the canonical URL as the frame's link text; "Cite this page" thinner than "Cite this record", no preview | Yes | Not changed: the canonical URL is the portable-evidence design (D6); the citation templates are the runtime's — Code item |
| EN 9 · `/data/` 50,000 px; "Reuse terms: not assessed" × 151 | Yes | **DEBT-011 stays open**: closing both dependency groups cut the page 44 % (DL-D7-010) but put the governed "cite a locator-only source" path behind a disclosure and failed the repository's public-tool suite, so it was reverted and recorded (DL-D7-013). The reuse line is governed (REL-02) — `ESCALATIONS.md` D7 |
| AR 1 · one value in two magnitudes and notations (1.262 مليار vs 1,262; 317.639) | Yes — governed prose and governed rows | Content: `ESCALATE_TO_MASTER` (observation) |
| AR 2 · the Findex fieldwork window in three date forms | Yes — governed fields (raised at D3) | Content: restated, `ESCALATIONS.md` D7 |
| AR 3 · the text alternative visible; the caveat up to three times per figure; 17,379 px page | Yes — by design (as EN 5; the table caption carries the markers every row shares) | Not changed (the Lock); recorded |
| AR 4 · the withheld H1 2025 transactions figure beside the monthly series, no "why" | Yes | `NEEDS_CONTROLLED_CONTENT` (a governed sentence naming the withheld release) |
| AR 5 · Explore's dangling section; rubric ordinals 01/04 against the index 02/05 | Yes | Both **closed at the resumption — DEBT-019** (DL-D7-007): one rendering of section 5, and a section rubric's ordinal is now its position in the spine index in every family renderer, so the two numberings cannot drift (the same latent mismatch on `/people/`, `/evidence/`, Compare and `/data/` closed by the same rule) |
| AR 6 · Compare Arabic copy: "2 سجلات مختارة", the prompt shown with two loaded, the boundary twice | Yes — the runtime's copy and state | Runtime + governed dual/plural forms: `ESCALATIONS.md` D7; Code item |
| AR 7 · bidi: ISO dates split across lines, ranges mirrored, "+11%" as "%11+" | Partly — the date and range cases are the runtime's Compare cells (the D6 RUNTIME_DEFECT; no loose date or range in the reference's own pages, `check_visuals.py --phases text`); the signed values are the reference's | **DEBT-018**, verified (eight occurrences on `/payments/` and CLM-003), open, blocks the acceptance |
| AR 8 · English credit lines; the raw path as the link text; the self-link on a Reading | Yes | Credit: governed, English only (escalated at D6); the link: by design (D6) |
| AR 9 · Arabic terminology drift across the corpus | Yes — governed text | Content: `ESCALATE_TO_MASTER` (observations) |
| AR 10 · the method disclosure's summary reads as prose; the citation copies without preview; the POS legend says both figures are shown while one is plotted | Yes | The disclosure: visual-review item; the citation: Code item; the legend: `ESCALATE_TO_MASTER` (question) |
| AR 11 · on a phone the 01–07 index sits between the first two answers, so the record seems to end | Yes — the strip after the first answer (D1 Lock; DEBT-014) | Visual-review item for the owner's review; not changed at the checkpoint |
| AR 12 · "reuse terms: not assessed" × 151; "P0 · People" unexplained on Explore | Yes | Content: `ESCALATE_TO_MASTER` (observations) |

Both readers confirmed: CLM-044 shows no value anywhere (page, Compare, search index, meta); every internal link and
anchor resolves (EN 139 links; AR 170 links, 157 anchors); no console errors; no horizontal scroll at 390 px; the
Home fold answers what the product is, why it differs, where to start and that limits are part of it within 30 s;
the Arabic is authored, not machine-translated. Verdicts (both): usable for a researcher and quotable for a
journalist with a fact-check on the escalated years and units; presentable to a regulator internally, not yet polished
for an official audience — the open items above.

### K.5 The closure pass (28 September 2026) — the bar of the closure brief §5, judged on the rendered product

Every line below was measured or read on the built site, not asserted from the records. Where a bar is not fully met
the shortfall is stated with its measurement; a recorded no is worth more than a claim the product does not support.

**The first thirty seconds from a deep link** — three entry pages × two languages × two viewports (12 screens),
measured on what is visible without scrolling (`closure-entry-*.png`):

| | Publisher named | What this is | What it says | What it does not say | Where next |
|---|---|---|---|---|---|
| Evidence Record (CLM-003) 1440 | 12/12 | 12/12 | yes | **indexed, not stated** (the index entry "05 What this evidence does not establish" is on the first screen) | 12 links |
| Evidence Record 390 EN | yes | yes | yes | indexed | 5 links |
| Evidence Record 390 AR | yes | yes | yes | **no — the index entry falls 3 px below the fold at exactly 390 × 844**; in view on any taller phone | 4 links |
| Reading 1440 EN/AR | yes | yes | yes | **stated** (the boundary precedes the essay) | 14 links |
| Reading 390 EN/AR | yes | yes | yes | **stated** | **only the crumb** — the strip follows 136 px (EN) / 188 px (AR) below the fold |
| Domain answer (`/people/`) all four | yes | yes | yes | **stated** | 2–16 links |

The publisher is named on every one of the twelve screens — this is what DEBT-016 was about, and it is met (DL-D7-008).
The two shortfalls are recorded, not fixed: on the Arabic record at exactly 390 × 844 the limit's index entry sits 3 px
below the fold, and on the Reading's phone screen the only forward link is the breadcrumb because the governed boundary
displaces the strip — which is the right priority, since the limit matters more than the navigation.

**Moving through the product.** Every composed page answers "where am I, what is near me, where next" without a
sitemap: the crumb and rubric above the `h1`; the index (beside the object from 900 px, as the strip below it,
DL-D7-009/011, measured at 2–36 % of the scroll on every family); the governed next actions; the edge groups at the
foot. State survives the language switch (`check_journeys.py` `language_switch_state`, the comparison kept). The menu
holds the six governed destinations and holds at 320 px with the Arabic labels (`check_acceptance.py`, longest titles).

**Reading.** Two authored scales, neither borrowed: English body 17 px/1.60, Arabic 18 px/1.90; display 32/30 px on a
phone and 46/42 px from 900 px; the Arabic rubric at its own size and with no letter-spacing; the measure bounded
(`check_site.py` `measure_bounded`, ≤ 720 px). The Arabic lens confirmed the composition is native, not mirrored, and
the prose idiomatic rather than translated; its one reading finding — that the Arabic heading-to-body size step is
weak on a phone where the rail collapses — is recorded below.

**Figures.** On `/payments/` at 320 px in both languages: 5 figures, every drawn one carrying its scope, its boundary
once in its foot, its canonical link and its named fallback table, 0 overflowing, 0 table wrappers scrolling. A figure
cropped out of the page keeps its scope, boundary, canonical link and unit in both languages
(`closure-crop-*.png`); the flagship same-year figure was re-tested against a hostile crop cutting its panel header
and now carries the unit at its axis (DL-D7-011), with the governed same-year marker standing between the two
publication-keyed rows so the crop cannot read as a fall.

**Tables.** Designed, not defaulted: every data column headed by a governed string, the caption carrying title,
period, universe and unit, row labels as `th scope="row"` (the empty corner cell is the conventional one, the recorded
D2 preference), every table in a named `role="region"`, none scrolling at 256 px, and the 4-column comparison
recomposing into stacked numbered blocks at 320 px rather than side-scrolling (confirmed by the phone lens).

**What leaves the page.** The citation copies title · product · record · publisher · edition · period · population
(clipboard read back, walk 2). The export frame stands alone with the publisher, product, edition, the complete
detached frame and the canonical link. Every printed page ends with the provenance block (product · edition ·
canonical URL · citation) and the chrome is gone. The social frames carry the publisher in type (DL-D7-008).

**The details.** Skip link first and visibly focused (3 px double outline); 0 interactive targets under the recorded
24 px minimum on Home; errors in the governed technical voice with empty and unknown states deliberate
(`check_journeys.py`, 28 drives); nothing moves without reason and both motion preferences are honoured.

**The three walks, recorded** (walked on the rendered site; what was clumsy is stated):

1. *A citizen who wants one plain answer and no method* — Arabic, phone. `/ar/` → the governed action "ابدأ بسؤال" →
   `/ar/explore/` → the cluster question "من هم الأقل وصولًا، وأين تظهر الفجوات المقاسة؟" → `/ar/people/`. Three taps.
   The answer is the `h1` and the governed lead states the measure with its clock, its population and its bound inside
   the sentence; no method is required of the reader. Clumsy: nothing in the path; the lead is six sentences and asks
   real attention on a phone (DEBT-015, closed by composition — the figure group now enters the first screen).
2. *A journalist deciding within two minutes whether a figure is safe to quote* — English, desktop, arriving on
   CLM-003. The first screen gives the publisher, the genre, the period, the population and the full governed claim
   including the source's own inconsistency (8.55 % computed against the source graphic's +11 %, both shown). "Cite
   this page" copies a complete attributable citation; the original source opens externally with its cue. The limit is
   named in the index on the first screen and read in one scroll. Clumsy: the cite button's confirmation is the word
   "Copied" in the status region with no preview of what was copied (recorded for Code at the checkpoint, unchanged).
3. *A researcher who needs definition, population, calculation base, method, source and limits, and wants to test
   whether two records may be compared* — English, desktop. `/evidence/` → search "account ownership" → five relevant
   records → CLM-001 → the seven governed questions answer definition, measure, population, currency, limits, source
   and method in order → "Compare evidence" → the comparison returns, for two records of the governed comparable set,
   the verdict **"Not a direct comparison — the recorded definition, population or method differs between these
   records"** with the prohibition against merging them. The product's thesis is delivered as an answer, not a
   failure. Clumsy: the search status region announces nothing on the first query (the runtime caps at ten hits
   without a total — the checkpoint's recorded Code item), and a record outside the comparable set simply cannot be
   selected, which the page does not explain (escalated at the checkpoint).

**The independent lenses.** Three lenses read the built pages — not a description of them — and each wrote its report
into the repository as it went (DEBT-005's rule). Verbatim in `design/evidence/d7/cold_read/`:
`lens-arabic-closure.md`, `lens-cold-record-closure.md`, `lens-phone-closure.md`. Adjudication of everything they
raised that Design owns:

| Lens · finding | Verified | Adjudication |
|---|---|---|
| Cold record · the governed source intro promises "Open the source record here" on records with no source card, denied in the next sentence | Yes — 10 records, 20 documents | **Fixed** (DL-D7-011): the intro prints only where a source card exists; 0 documents remain |
| Cold record · a hostile crop of RV-CWR-001 loses "USD million", leaving two values that could read as a 45 % fall | Partly — the unit is lost; the governed same-year marker between the rows survives every crop that shows both values, so it cannot honestly read as a fall | **Fixed** (DL-D7-011): the unit now prints in the axis row, so a crop carrying the axis carries the unit |
| Phone · the Compare strip sits at 71 % of the scroll, indexing only what the reader has passed | Yes — measured | **Fixed** (DL-D7-011): the strip precedes the tool (8 % EN, 6 % AR) |
| Phone · no sticky in-page navigation at 390 px; the strip is inline | Yes — by design | Not changed: exactly one visible spine at any width is a Lock rule; a collapsed "on this page" control needs a governed label (the standing escalation) |
| Phone · `/data/` is very long on a phone and its curated categories are not in the index | Yes — measured | Recorded, not changed: **DEBT-011 stays open** (DL-D7-013 — closing the groups would have cut 44 % but put a governed citation path behind a disclosure and failed the repository's public-tool suite); paged groups or category jump links each need governed labels — an escalation, not authored copy |
| Phone · in-flow action links 30–33 px against the header's 44 px | Yes — measured | Recorded, not changed: the project's recorded standard is the 24 px minimum, met everywhere and asserted; a 44 px rule for links inside prose is an owner-level choice |
| Phone, cold record, Arabic · the visible text alternative and table read as unhidden accessibility markup | Yes — by design | Not changed: the Lock keeps the text alternative visible for print, no-script and assistive-technology parity (considered and recorded at the checkpoint) |
| Arabic · **BLOCKING** — every section heading on the record is 14 px against 20 px body: a heading 30 % smaller than the prose it introduces, on `/ar/evidence/CLM-003/`, `/ar/explore/` and the Reading's labels | Yes — measured at 390 and 1440 px; the cause is that English marks the same object with uppercase and tracking, which Arabic correctly withholds and nothing replaced | **Fixed** (DL-D7-012): an Arabic rubric that is a section heading is now sized against the prose it heads (20 px against 18 px body), keeping its colour and weight; English unchanged |
| Arabic · heading-to-body contrast weak on a phone; the ochre eyebrow carries more hierarchy than the heading | Yes | Addressed by the same fix; the residual (heading and lead statement now both 20 px, separated by colour and weight) is recorded for the owner's visual review |
| Arabic · **BLOCKING** — the POS-value column mixes "910.688" and "1,262", read as three orders of magnitude apart | **The reading is wrong** — both are YER million and differ by about 1.4×; the notation, not the data, misled the reader | Content, and now the strongest reader evidence in the record: **two independent trained readers in two sessions have misread a governed value by a factor of a thousand from this notation alone** — `ESCALATE_TO_MASTER`, strengthened in `ESCALATIONS.md`. Design will not round, restate or re-unit a governed value |
| Arabic · charts keep a left-to-right value axis and ISO tick labels inside an RTL column | Yes | Not changed: the left-to-right numeric axis is a governed contract rule kept against a D1 finding (DL-D1-006); the ISO ticks are the governed period keys, isolated by the text layer. The mismatch with the Arabic month names in the same figure's prose is recorded for the owner |
| Arabic · the percent sign appears on opposite sides within one comparison ("%8.55" beside "+11%") | Yes — the unsigned value takes the Unicode default in RTL, the signed one is inside the left-to-right isolate DEBT-018 required | Recorded, not changed: each rendering is individually correct, and isolating every percentage in the corpus at the closure would be a corpus-wide typographic change no reader has asked for. For the owner's visual review |
| Arabic · source attributions left in English ("المصدر: Central Bank of Yemen — Aden") while the prose names the same body in Arabic | Yes | Not changed: publisher names are governed in English only and Arabic frames print them as isolated left-to-right runs (the contract's own `language_note`, closed at D2) |
| Arabic · link underlines cut through Arabic descenders and sub-baseline dots | Yes — `text-underline-offset: .16em` | Recorded for the owner's visual review: a larger Arabic-only underline offset is a legitimate refinement; it was not taken at the closure because it moves every link on every Arabic page and no reader reported a legibility failure, only the collision |
| Arabic · the publisher is named only in Latin script; the Arabic name exists only inside the mark at ~8 px | Yes | Recorded: the publisher's Arabic name is not a governed interface string, and Design authors none; raised with EAD-03/OWN-01 |
| Arabic · a `figure` on Home promises a view and delivers only its text description | Yes — VIS-INCLUSION-TRANSMISSION is a TABLE_TEXT_FIRST contract with no rows | Not changed: a contract without rows is never drawn (the tier rule); the frame prints the governed description as its body. The lens's reading — that it looks unfinished — is recorded for the owner |
| Cold record · CLM-039's central comparison carries no values, dates or interface names | Yes — governed text | Content: `NEEDS_CONTROLLED_CONTENT` (`ESCALATIONS.md`, D7 closure) |
| Cold record · question 7's summary reads as internal meta-language | Yes — governed copy | Content: `ESCALATE_TO_MASTER` (observation) |
| Phone · Compare prints two governed sentences twice, 70 px apart | Yes — the governed `alt_text` ends with the governed `prohibited_inference` verbatim | Content: `ESCALATE_TO_MASTER` — Design will not truncate a governed string and the boundary must print in the boundary voice |
| Cold record · CLM-044 reads as deliberate, not broken, and leaks no withheld value in text, attributes, SVG, hidden nodes, forced-open disclosures or JSON-LD | Yes | Confirmed — the withheld state holds |

**Status of this checklist (28 September 2026, closure).** The ticks record the technical evidence; §K.5 records the
closure pass on the rendered product. DEBT-018 (DL-D7-006), DEBT-019 (DL-D7-007), DEBT-016's identification defect
(DL-D7-008), DEBT-014 and DEBT-015 (DL-D7-009), DEBT-011 (DL-D7-010) and DEBT-007 (decided) are closed, and the three
interface defects the closure lenses found are fixed (DL-D7-011). No design debt is flagged "blocks D7". What remains
is the owner's own visual acceptance, which this session does not give itself, and the content and runtime items
escalated to the steward and to Code. **D7 is not declared accepted here, and this is not PUBLIC RELEASE READY.**

## L2. Outputs on the closure tree (pasted, unedited last lines)

```text
python3 scripts/checksums.py --check
CHECKSUM MANIFEST CURRENT: 1211 files
python3 scripts/generate_projections.py --check
PROJECTION CHECK PASS
python3 -m unittest discover -s scripts/projection/tests -t .
OK
python3 scripts/build.py
Built 288 HTML files from 143 controlled page specs.
python3 scripts/audit_public_literals.py
PUBLIC_LITERAL_CLOSURE records=12760 unresolved=0
python3 scripts/validate.py
WEBSITE REPOSITORY VALIDATION PASS
python3 scripts/repository_manifest.py --check
REPOSITORY MANIFEST CURRENT: 1198 files in 21 classes
python3 scripts/tests/test_literal_audit_determinism.py
LITERAL AUDIT DETERMINISM PASS: 8 hash seeds, one SHA-256 9f23830a8d220598b5014992c59d1b0fbe963bc50ee2d7eda948a3d111ec5f85
python3 audit/pre_tranche_c/source_lineage_truth_test.py
SOURCE LINEAGE TRUTH TEST PASS: 8/8
python3 scripts/architecture_diagrams.py --check
ARCHITECTURE DIAGRAMS CURRENT

python3 design/reference/build.py
Built 288 documents with renderer 'accepted' into design/reference/out; 24 export frames and 286 social frames in _export/ and _social/
python3 design/reference/check_content.py --text
CONTENT PARITY: PASS (0 differing documents)
python3 design/reference/check_binding.py
BINDING: PASS — 39 projections by role, 286 edition pages + root + 404, 286 bundles, shipped data ['static-data/search_aliases.json', 'static-data/search_index.json']
python3 design/reference/tokens.py --check
TOKENS CURRENT
python3 design/reference/check_trio.py --degraded
24 renders checked; 0 failed; 12 interaction smoke tests (pointer and keyboard), 12 passed; 6 degraded renders, 6 ok
python3 design/reference/check_site.py --gate d2 --degraded
168 renders checked; 0 failed; 84 smoke tests, 84 passed; 557 hard-state assertions on 44 route renders, 557 passed; 20 degraded renders, 20 ok
python3 design/reference/check_site.py --gate d3 --degraded
168 renders checked; 0 failed; 84 smoke tests, 84 passed; 252 hard-state assertions on 43 route renders, 252 passed; 18 degraded renders, 18 ok
python3 design/reference/check_site.py --gate d4
904 renders checked; 0 failed; 452 smoke tests, 452 passed; 3822 hard-state assertions on 228 route renders, 3822 passed
python3 design/reference/check_journeys.py
52 journey walks (13 journeys × EN/AR × mobile/desktop), 52 passed; 28 technical-state drives, 28 passed
python3 design/reference/check_visuals.py
VISUALS: PASS — 36 contracts × EN/AR on their routes: 2812 contract assertions; 48 forced-colours and print checks on the 12 drawn contracts (VIS-PROVIDER-OBSERVABILITY waits as a text frame until its labels are governed); 24 export frames; 286 social frames; 111 print checks on 11 family routes × EN/AR; 596 documents and frames scanned for loose runs; placeholders on the site: []; 0 failures
python3 design/reference/check_acceptance.py
ACCEPTANCE: PASS — 288 documents and 310 frames checked statically (14248 assertions); 59 browser assertions on the last-ten-percent surfaces in EN and AR; 0 failures

YFIE_SITE_DIR=design/reference/out python3 scripts/tests/test_public_tools.py
PUBLIC TOOL TESTS PASS: 25/26 passed, 1 not applicable to the current data
YFIE_SITE_DIR=design/reference/out python3 audit/tranche_c/checks/viewport_acceptance.py
VIEWPORT ACCEPTANCE: 168/168 page-width checks pass
YFIE_SITE_DIR=design/reference/out python3 audit/tranche_c/checks/bilingual_invariance.py
BILINGUAL NUMERIC INVARIANCE: 0 page pairs with differing numbers (143 pairs checked)
```

The d2 count rises from 553 to 557: two assertions for the `/data/` register (`supporting_open_reference_closed` and
the new `locator_only_source_reachable`, DL-D7-013) and two for `filter_opens_supporting` in both editions.
`test_public_tools.py` at 25/26 is the checkpoint's own figure — it fell to 24/26 under the reverted `/data/` change
and was restored by the revert, not by touching the test (DL-D7-013).

## L. Outputs on the checkpoint tree (pasted, unedited last lines)

```text
python3 design/reference/build.py
Built 288 documents with renderer 'accepted' into design/reference/out; 24 export frames and 286 social frames in _export/ and _social/
python3 design/reference/check_content.py --text
CONTENT PARITY: PASS (0 differing documents)
python3 design/reference/check_binding.py
BINDING: PASS — 39 projections by role, 286 edition pages + root + 404, 286 bundles, shipped data ['static-data/search_aliases.json', 'static-data/search_index.json']
python3 design/reference/tokens.py --check
TOKENS CURRENT
python3 design/reference/check_site.py --gate d2 --degraded
168 renders checked; 0 failed; 84 smoke tests, 84 passed; 553 hard-state assertions on 44 route renders, 553 passed; 20 degraded renders, 20 ok
python3 design/reference/check_site.py --gate d3 --degraded
168 renders checked; 0 failed; 84 smoke tests, 84 passed; 252 hard-state assertions on 43 route renders, 252 passed; 18 degraded renders, 18 ok
python3 design/reference/check_site.py --gate d4
904 renders checked; 0 failed; 452 smoke tests, 452 passed; 3822 hard-state assertions on 228 route renders, 3822 passed
python3 design/reference/check_journeys.py
52 journey walks (13 journeys × EN/AR × mobile/desktop), 52 passed; 28 technical-state drives, 28 passed
python3 design/reference/check_trio.py
24 renders checked; 0 failed; 12 interaction smoke tests (pointer and keyboard), 12 passed
python3 design/reference/check_visuals.py
VISUALS: PASS — 36 contracts × EN/AR on their routes: 2812 contract assertions; 48 forced-colours and print checks on the 12 drawn contracts (VIS-PROVIDER-OBSERVABILITY waits as a text frame until its labels are governed); 24 export frames; 286 social frames; 133 print checks on 11 family routes × EN/AR; 596 documents and frames scanned for loose runs; placeholders on the site: []; 0 failures
python3 design/reference/check_acceptance.py --evidence design/evidence/d7
ACCEPTANCE: PASS — 288 documents and 310 frames checked statically (14248 assertions); 59 browser assertions on the last-ten-percent surfaces in EN and AR; 0 failures
YFIE_SITE_DIR=design/reference/out python3 scripts/tests/test_public_tools.py
PUBLIC TOOL TESTS PASS: 25/26 passed, 1 not applicable to the current data
YFIE_SITE_DIR=design/reference/out python3 audit/tranche_c/checks/viewport_acceptance.py
VIEWPORT ACCEPTANCE: 168/168 page-width checks pass
YFIE_SITE_DIR=design/reference/out python3 audit/tranche_c/checks/bilingual_invariance.py
BILINGUAL NUMERIC INVARIANCE: 0 page pairs with differing numbers (143 pairs checked)
```

The repository gates (`CONTRIBUTING.md` §5) on the final commit, on `dist/` as always:

```text
python3 scripts/checksums.py --check
CHECKSUM MANIFEST CURRENT: 1180 files
python3 scripts/generate_projections.py --check
PROJECTION CHECK PASS
python3 -m unittest discover -s scripts/projection/tests -t .
OK
python3 scripts/build.py && python3 scripts/audit_public_literals.py && git status --porcelain -- dist audit/PUBLIC_LITERAL_CLOSURE.json
dist and closure unchanged by a fresh build
python3 scripts/validate.py
WEBSITE REPOSITORY VALIDATION PASS
python3 scripts/repository_manifest.py --check
REPOSITORY MANIFEST CURRENT: 1180 files in 21 classes
python3 scripts/tests/test_literal_audit_determinism.py
LITERAL AUDIT DETERMINISM PASS: 8 hash seeds, one SHA-256 9f23830a8d220598b5014992c59d1b0fbe963bc50ee2d7eda948a3d111ec5f85
python3 audit/pre_tranche_c/source_lineage_truth_test.py
SOURCE LINEAGE TRUTH TEST PASS: 8/8
python3 scripts/architecture_diagrams.py --check
ARCHITECTURE DIAGRAMS CURRENT
python3 audit/tranche_c/checks/bilingual_invariance.py
BILINGUAL NUMERIC INVARIANCE: 0 page pairs with differing numbers (143 pairs checked)
python3 scripts/tests/test_public_tools.py
PUBLIC TOOL TESTS PASS: 25/26 passed, 1 not applicable to the current data
python3 audit/tranche_c/checks/viewport_acceptance.py
VIEWPORT ACCEPTANCE: 168/168 page-width checks pass
```
