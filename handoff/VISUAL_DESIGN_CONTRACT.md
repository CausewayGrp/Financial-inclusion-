# Visual design contract — how Design uses the governed visuals

**Status:** part of the R8.6 Design handoff (start at `handoff/README_FIRST.md`). Tier counts are in `tier_counts` of the JSON; the tier of every visual is also listed in `handoff/ROUTE_CONTENT_AND_STATE_INVENTORY.json`.

**Single source.** `site-src/content/visuals/visual_design_contracts.json` is DERIVED by the projection generator. It is
built from the Production Master and the controlled input `scripts/projection/controlled_inputs/visual_design_contract.json`.
This page explains how to read it. It does not restate its content, so when the two disagree, the JSON is right.

## 1. What the JSON gives you

For each of the 36 governed visuals it gives:
- the design **tier** and the reason for it;
- the governed title and question;
- the prohibited inference;
- the analytical **alt text** in English and Arabic (the governed accessible summary + "Does not establish:" + the
  prohibited inference);
- period and universe in both languages;
- the canonical route.

SIGNATURE and CORE_ANALYTICAL visuals also carry a **data contract**:
- the governed rows, already resolved from the Master, each with its value, unit, period, source, **grammar state** and
  **markers**;
- a governed bilingual **label** for every value the chart prints: `<field>_label` = `{en, ar, ui_id}` on each value or
  record (categories, series, lanes, units, events, provider classes and states). Temporal values (years, ISO months and
  dates, and the `*_iso` form of month-year periods) carry no label; format them by locale;
- missing periods;
- derived differences, already checked against the governed values;
- the drawing rules: form, ordering, transformation, missing, breaks, annotation, mobile, RTL and fallback;
- the governed **credit line**;
- the bilingual **detached caption**;
- any **blockers**.

## 2. Tiers

| Tier | What Design does |
|---|---|
| SIGNATURE | Design these first: RV-CWR-001, RV-CWR-009 and VIS-PROVIDER-OBSERVABILITY. |
| CORE_ANALYTICAL | Draw them in standard forms, using the grammar below. The three POS visuals form one small multiple. |
| SUPPORTING | No data contract. Render the governed text (its alternative is its complete content); optionally add a non-quantitative diagram built only from governed words and `UI-VIS-*` labels — no plotted value, axis or scale. Plotting values needs promotion Master-first. |
| TABLE_TEXT_FIRST | Do not draw a chart; render the governed ordered text or table. Each entry states its promotion condition. |
| RETIRE_FROM_DESIGN | Do not draw VIS-CAPITAL-CONTEXT; its data are governed as context only. |

Counts per tier change when the Master changes; read `tier_counts`.

An Evidence Record whose ID starts `VIS-` is a verification record, not a chart slot: where a visual has the same ID, the
record verifies it; a `VIS-` record without a visual contract is never drawn as a chart. A record can outlive its visual:
VIS-CAPITAL-CONTEXT is RETIRE_FROM_DESIGN as a visual and stays a public Evidence Record.

## 3. Rules that are not negotiable

1. **No new chart without a contract row in Master 11** and a tier in the controlled input. No number, label or
   sentence is authored in Design:
   - legend and state labels come from the governed `UI-VIS-*` interface copy, listed in `grammar_labels` in both
     languages;
   - axis, category, series, lane, unit and event text comes from the value's `<field>_label`;
   - a field marked `encoding_only_fields` (for example the event class that selects a chain step) is never printed.
   If a printed value has no label, the generator stops; ask for a label Master-first rather than writing one.
2. **Colour is never the only carrier.** Every state uses at least two of the following:
   - mark shape or fill;
   - line style;
   - a direct governed label;
   - position.

   No red, amber or green is used. Nothing fades with age.
3. **Breaks, gaps and disagreements are drawn, never repaired:**
   - BREAK_VINTAGE and BREAK_UNIVERSE stop the line.
   - MISSING leaves a labelled gap, never a zero; WITHHELD keeps the slot and shows the governed label instead of the value.
   - DISAGREEMENT puts the same neutral note mark on every flagged period.
   - SAME_YEAR_REVISION puts both values at one position on the axis.
4. **The detached frame travels with the chart.** It carries:
   - the title;
   - period and universe;
   - the credit line;
   - the prohibited inference;
   - any marker present in the data;
   - the canonical link.

   A crop without these is not a supported export. The canonical link in `detached_caption_*` is a site-relative path
   (`/en/evidence/...`); an exported frame prefixes the deployment origin.
5. **RTL.**
   - Numeric time axes run left to right in both languages.
   - Text, legends, panel order and categorical bar labels follow the reading direction.
   - Chains and ladders run top to bottom.
   - Digits are Western. IDs, currency codes and signed percentages are isolated left-to-right runs.
   - No right-pointing arrow glyph goes between numbers in Arabic.
6. **Mobile.** Each contract states its narrow form, proved at 320 and 390 CSS px. Plot areas never scroll horizontally.
7. **The text alternative ships with every chart and stays true if the chart fails to load.** It consists of the alt
   text plus a table or ordered-text fallback with a caption, scoped headers, unit, universe and period.
8. **Blockers stop a release, not a design.**
   - A contract with a blocker may be designed.
   - It may not ship until the blocker is closed Master-first.
   - Open blockers: none. The two P3 blockers were closed Master-first in P5:
     - **RV-CWR-001, panel 2** (indexed paths): the CBY AR2025 values for 2021–2023 are governed rows. The panel binds
       the CBY AR2025 path and the IMF staff-report path, each indexed to its own 2021 value (`derived` entries
       `cby_ar2025_index`, `imf_staff_index`, unit label `UI-VIS-UNIT-INDEX-2021`). The two lanes coincide within
       rounding; draw them as two labelled lanes with distinct marks, never as one series. A growth-gap guard checks the
       governed claim CLM-037.
     - **RV-CWR-009** (credit line of the REF-PAY-001 event): the locator now resolves to the source record of the CBY
       Governor's Decision No. 23 of 2024. The event is a regulatory requirement, not implementation, use or outcome.
   - A panel marked READY is checked by the generator: every series and derived path it binds must resolve.
9. **Lanes are separate series.** A value in a lane (for example VIS-MFI-DIVERGENCE borrowers, savers, portfolio) has
   its own id (`<row>#<lane>`), unit and markers; lanes never share a value axis and anchors are never joined.

## 4. Where it is enforced

- **Generator.** It fails on:
  - any untiered visual;
  - any unresolved row;
  - any value that no longer equals its guard;
  - any grammar label that is not governed interface copy;
  - any printed value without a governed bilingual label.

  The unit tests `test_visual_design_contracts`, `test_visual_design_contract_guards` and `test_visual_display_labels`
  cover this.
- **Validator.**
  - P3-G01: contract completeness.
  - P3-G02: the static baseline draws no graphic.
  - P3-G03: the Arabic scope line matches the English one.
  - P3-G04: no right-pointing arrow between numbers in Arabic.
- **Decisions and reasons.** Recorded in `audit/P3_VISUAL_DESIGN_READINESS.md`.
