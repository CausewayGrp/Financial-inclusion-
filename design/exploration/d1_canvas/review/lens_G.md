# LENS G — Journalist: quoting and screenshotting under deadline

Method: for each proposition, the headline a hurried reader would write from the Record and figure crops alone, whether the crop contains the stopper (period, universe, bound, source), and whether the layout makes the safe quotation the easy one.

## 1. Per proposition

### T1 · Register
- **Record crop** (crops/T1-record-en-primary.png, -ar-): headline "POS terminals up 11 %". The right column typesets "+11 %" and "8.55 %" as lone stat blocks; the stopper ("Source figures disagree — both are shown") is 11 px under the number. Period and ID CLM-003 are in the margin; universe ("not established") and source are not in the crop. On the phone the two stat blocks land as standalone tiles at the foot of the first screen (fold/T1-record-en-m.png) — the easiest lift in the set. **MUST-FIX.**
- **Figure crop** (crops/T1-reading-en-figure.png, -ar-): panel 1 stacks 6,245 over 3,422 on one x-tick, no value labels → "Remittances fell 45 %". The stopper is present but below the panel in small regular type; the adjacent "Not directly comparable" divider reads as qualifying the two 2024 points. Link and credit present; figure ID absent.
- **Home** (tiles/T1-home-en-d-2.png): three figures inline in one paragraph; records beneath carry period and universe. No lone number, but a bounded sentence must be cut from a paragraph.
- Misreading: "+11 %" quoted as the product's own figure.

### T2 · Argument
- **Record crop** (crops/T2-record-en-primary.png, -ar-): numbers bold inline; period, universe with "not established" and ID all inside the crop — best record crop for one-move quotation. Source locator absent.
- **Figure crop** (crops/T2-reading-en-figure.png): same stacked panel 1; "Not directly comparable" is a heading over panel 2, not a divider; the bound is regular weight in a narrow column beside empty space. The Arabic link wraps and bidi-scrambles ("ar/readings/same-year-different-/ … /number", crops/T2-reading-ar-figure.png) — unusable from a screenshot. **MUST-FIX.**
- **Home** (tiles/T2-home-en-d-2.png): figures in a light paragraph; the record list with period/universe is collapsed behind "+ Evidence records behind these figures". **SHOULD-FIX.**
- Misreading: "remittances halved 2024→2025" (report years read as data years).

### T3 · Strata
- **Record crop** (crops/T3-record-en-primary.png, -ar-): the statement alone in a box — no title, period, ID, universe or source; nothing to cite. On the phone the index pushes the statement off the first screen mid-sentence at "1,473 imply" (fold/T3-record-en-m.png) → "POS terminals nearly tripled", discrepancy cut off. **MUST-FIX.**
- **Figure crop** (crops/T3-reading-en-figure.png): stacked panel 1 as T1/T2; the bound sits in a narrow band with an empty right half. Arabic link bidi-scrambled (crops/T3-reading-ar-figure.png). On mobile the text-alternative tables overflow, clipping the IMF index column (tiles/T3-reading-en-m-3.png, -4.png). **MUST-FIX.**
- **Home** (tiles/T3-home-en-d-2.png): figures inline; record list with periods visible.
- Misreading: as T1.

### T4 · Instrument
- **Record crop** (crops/T4-record-en-primary.png, -ar-; inspect/crops/T4-record-en-primary@390.png): clock and ID above the title, ID twice (breadcrumb + Reference ID), no lone number; the whole statement fits the phone's first screen (fold/T4-record-en-m.png). Universe and source not in crop (as T1/T3).
- **Figure crop** (crops/T4-reading-en-figure.png, -ar-): panel 1 as labelled rows on a zero-based horizontal axis with values printed (6,245; 3,422.16), "Same year, different publication" directly beneath, double-rule divider, bold full-width bound, one-line link; the Arabic link wraps cleanly at 390/320 (inspect/crops/T4-reading-ar-figure@390.png). Residual risk: row labels "…Report 2024 / …Report 2025" still read as data years → "fell 6,245 to 3,422, 2024 to 2025"; the stoppers are in-crop.
- **MUST-FIX:** the "fluid" build drops every value label at every width (inspect/crops/T4-reading-en-figure@1440.png, @390, @320; AR likewise) while the main build keeps them (crops/T4-reading-en-figure.png, tiles/T4-reading-en-m-2.png). Unlabelled, a phone crop yields "about 6,200 → about 3,400".
- **Home** (fold/T4-home-en-d.png, fold/T4-home-en-m-2.png): each figure is its own sentence-paragraph — one-move copy, records linked beneath. But "Areas holding about 23 % of the population were not surveyed." now stands alone without survey or source → "23 % of Yemen unsurveyed". **SHOULD-FIX.**

### Common to all four
- "Full record" is a site-relative path (/en/readings/…) with no host: untypeable from a screenshot.
- RV-CWR-001 is never rendered; "Cite this record" sits only at the page foot (tiles/T1-record-en-d-2.png … T4-record-en-d-2.png), never on the object.
- The Arabic figure credit is Latin-only (crops/T*-reading-ar-figure.png).

## 2. Ranking for this lens
**T4 > T2 > T1 > T3.** T4 is the only figure whose crop prints both values keyed to publication on a horizontal axis, the only record whose phone screenshot is self-citing (clock, ID, full statement), and the only Arabic link that survives wrapping. T2 has the best record crop for one-move quoting but the stacked figure and a broken Arabic link. T1 hands the reader lone stat blocks. T3 gives a statement-only crop, a mid-sentence phone cut and clipped tables.

**Embed:** T4's figure, main build only; no first-generation panel 1.

## 3. Convergence
Material. T4's horizontal, labelled, publication-keyed panel 1 lets a reader quote two same-year values without reading them as a fall; no stacked x=2024 scatter comes near. Second, clock-and-ID-before-claim makes a phone screenshot carry its own citation. The bold bound and double-rule divider T3 approximates.

## 4. Three improvements to T4
1. Ship one build: direct value labels at every width; retire the fluid variant's unlabelled charts (inspect/crops/T4-reading-en-figure@390.png).
2. Put a copyable citation on the object: absolute URL, record/figure ID and review date beneath the figure and the primary statement, with a copy affordance (the Record offers "Copy source reference" for sources, none for itself: tiles/T4-record-en-d-2.png).
3. Give the dot-plot rows a caption-style "publication" column head in the register of "2024 · USD million", so report years cannot be read as the axis; on Home, attach each figure's period/universe marginalia to its sentence-paragraph, not only to the record list below.

## 5. ESCALATION CANDIDATES (governed content, not design)
- Text-alternative table renders "6245" against the figure's "6,245" (crops/T1-reading-en-figure.png, crops/T3-reading-en-figure.png); table "118" vs T4 label "118.0" (crops/T4-reading-en-figure.png).
- Arabic figure credit rendered in English only, all propositions (crops/T*-reading-ar-figure.png).
- Canonical link string is a relative path with no host, all propositions.
- RV-CWR-001 identifier absent from every render.
- T1 stat caption "Source figures disagree — both are shown" (crops/T1-record-en-primary.png): confirm it is a governed string; it appears in no other proposition.
