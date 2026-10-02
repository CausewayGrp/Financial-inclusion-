# Arabic dates, systemically — sweep, fix and gate (2 October 2026)

The owner's request after RC-5: the Arabic reviewer's blocking finding (ISO dates displayed reversed on `/ar/providers/`)
is a class of defect, not two cells. Every Arabic page was swept for an ISO date, a date or number range, or a numeric
period printed without direction isolation (prose, tables, figure labels, citations, the title, meta content and search
results). Where the brief keeps ISO (tables, data cells, citations), the renderer isolates it left to right so that it
displays in the same order as in English. Running prose follows B2c. A gate with negative controls keeps it so. No
governed word changed; this is a renderer and runtime change only.

## Method

- **Static pages.** Every file under `dist/ar/` (143 documents) was parsed. Each digit-hyphen-digit run (`\d[-‐‑–−]\d`:
  `2026-01-22`, `2014–2024`, `80,000–90,000`, an identifier's dated tail such as `…-2025-01`) was classed by where it
  prints and whether it sits inside a left-to-right isolate: an element with `dir="ltr"` (an SVG drawing:
  `direction="ltr"`), or the Unicode isolates LRI … PDI where markup cannot go. Quarter and half-year labels (`Q3 2025`,
  `2025 H1`) were searched for too; none prints on an Arabic page (the Arabic edition writes «الربع الثالث 2024»).
- **Runtime.** A headless browser ran the Arabic search on 15 queries and the Compare tool on all 20 offered records, in
  groups of three, and read every text node the runtime wrote.
- `aria-label` values are spoken, not printed; they are counted below but are not part of the display defect.

## Found and fixed

Static Arabic pages, before → after (runs; one page can hold several):

| Where it prints | Not isolated before | After | Isolated before → after |
|---|---:|---:|---:|
| Prose (answers, record text, summaries) | 26 | 0 | 829 → 855 |
| Citations (preview and print foot) | 42 | 0 | 564 → 606 |
| Tables and data cells (incl. clocks, date lists, matrix cells) | 8 | 0 | 677 → 685 |
| Figure labels (SVG) | 0 | 0 | 67 → 67 |
| Document title | 2 | 0 | 0 → 2 |
| Meta: description · og:description · og:title · og:image:alt | 16 · 16 · 2 · 2 | 0 | 0 → 36 |
| **Total printed** | **114 runs on 44 pages** | **0** | 2,137 → 2,251 |
| `aria-label` (spoken; not changed) | 62 | 62 | — |

Runtime: **16** text nodes written without isolation (search results and Compare) → **0**.

### Causes, and what was changed

1. **A range at the end of a sentence or clause was never isolated** (`… للفترة 2026–2030.`). The shared expression
   `scripts/yfie/text.py` `NUM_RANGE` refused a range followed by `.` or `,` (meant to protect decimals). It now refuses
   only a following digit or a decimal part. Most of the 26 prose, 42 citation and 8 table runs, and most runtime
   nodes, were this.
2. **A range of thousands was not recognised** (`80,000–90,000`). `NUM_RANGE` now holds it.
3. **A range inside an identifier was split from it** (`SRC-IMF-YEM-AIV-` + an isolated `2025-2026`). `NUM_RANGE` and
   `ISO_DATE` no longer start after a letter, digit or hyphen, so an identifier is never cut.
4. **Identifiers outside a fixed prefix list ran bare in citations** (`FMIIP-BASELINE-2025-01`). The citation isolation
   now uses one identifier expression, `ID_RUN` (any capitalised identifier with a hyphen and a digit).
5. **The runtime wrote identifiers bare** (`سجل مصدر — SRC-CBY-SANAA-C12-2024` in a search result; the Compare
   table's source lists). `site-src/app.js` `iso()` now isolates identifiers with the same `ID_RUN`, breakable (no
   `nw`), after the dates and ranges; its `LTR_RUN` and `ID_RUN` are the renderer's, character for character.
6. **The title and the meta content cannot carry markup.** In a right-to-left document `isolate_document` now wraps each
   identifier, ISO date and range in the title, `description`, `og:title`, `og:description` and `og:image:alt` in the
   Unicode isolates U+2066 … U+2069 (`isolate_head`). The machine fields (`yfie-citation`, `yfie-record-id`, URLs) are
   unchanged.

English pages change only where the same runs are now isolated too (49 pages; no visible difference in a
left-to-right page) and where an identifier with a dated tail is now isolated whole. Ten social images whose frame text
holds such a run were regenerated; the other 276 are byte-identical.

## Running prose (B2c)

B2c (`INSTRUCTIONS.md`, Part B B2 c) writes ISO dates in Arabic running prose as Arabic dates in words, and keeps ISO in
tables, data cells and citations. The RC-5 pass applied it (B2-100: the two ISO dates of UI-VIS-CAT-PRV-LIMIT-EWALLETS;
B2-003 and B2-004: the matrix's period and state cells, after the Arabic review). This sweep found **no ISO date left in
Arabic running prose**. Every full ISO date that still prints is in a place B2c keeps: the date-led chronology and
decision lists (76), the "When was it measured or observed?" clocks (53), citations (30), the governed period line of a
figure's caption and its "Scope and time" line (8; the record's `period_ar` field, ISO in both languages), and one
matrix cell (2). All are isolated.

## Gate and negative controls

- `scripts/validate.py` **RC-DATES**: on every Arabic page, a digit-hyphen-digit run in printed text must sit inside a
  `dir="ltr"` element (SVG: `direction="ltr"`), and in the title, the displayed meta content, `alt`, `title` and
  `placeholder` between LRI and PDI. It also requires the runtime's `ID_RUN` to be the renderer's and `iso()` to apply
  it. The existing S05.3 check still requires the runtime's `LTR_RUN` to be the renderer's.
- `scripts/tests/test_public_tools.py`: *bidi: Arabic search results and Compare print every date, range and
  identifier isolated* (three searches, three comparisons). It fails on the previous runtime (14 runs).
- `scripts/tests/test_gate_negative_controls.py`, three new controls, each caught: a date range un-isolated on
  `/ar/evidence/CLM-024/`; the Unicode isolates removed from `/ar/evidence/CLM-040/`'s title and social card; the
  runtime's identifier isolation removed. The existing drift control was re-pointed at the revised expression.

No conformance with any accessibility or bidi standard is claimed; this records what was measured and changed.
