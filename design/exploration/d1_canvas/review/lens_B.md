# Lens B — Arabic editorial / RTL art direction

**Shared facts (all four).** Running-text percentages render `%8.55` and `%11+` (sign at the reading-end of the digits; fold/T1–T4-record-ar-d.png). That is what Arabic bidi produces and what Arabic readers see in every newspaper; not a defect. Arrows in «افهم ← استكشف ← تحقّق» point correctly; breadcrumbs read parent → child («الأدلة / CLM-003»); index numerals sit at reading-start; dates are composed («مارس 2025 – يناير 2026»), not transliterated; no letter-spacing or small-caps mimicry. Western digits throughout — a policy, not a defect, but Yemeni official Arabic often uses Eastern digits: decide, don't default. The figure credit is English on every Arabic figure (§5).

## 1. Per proposition

### T1 · Register
**Establishes:** the manuscript margin mirrors correctly — clock at reading-start, stat block at reading-end (fold/T1-record-ar-d.png); mobile H1 breaks cleanly (fold/T1-home-ar-m.png).
**MUST-FIX:** (a) one number, two forms — stat block `8.55%` / `+11%` LTR against body `%8.55` / `%11+` (crops/T1-record-ar-primary.png); (b) the narrow margin splits a date mid-token: «من ‎2022-11-» / «07 إلى 09-01-2023» (tiles/T1-home-ar-d-2.png; intact in T3/T4); (c) at 390 the figure's text alternative is clipped at the reading-start edge («024», «05.74», «.1.73») — Arabic only, the English fits (tiles/T1-reading-ar-m-4.png vs tiles/T1-reading-en-m-3.png); (d) URL corrupted at wrap on mobile: «ar/readings/same-year-different-/» + «/number» (tiles/T1-reading-ar-m-3.png).
**SHOULD-FIX:** desktop H1 widow «واحدًا.» (fold/T1-home-ar-d.png); «(Global / Findex)» split (tiles/T1-home-ar-d-2.png); ~8 px tick labels (crops/T1-reading-ar-figure.png); reading title splits «رقم / مختلف» on mobile (fold/T1-reading-ar-m.png).
**Misreading:** a screenshot of crops/T1-record-ar-primary.png shows two visual forms of one growth figure; a cold reader assumes two numbers.

### T2 · Argument
**Establishes:** only proposition whose desktop H1 sits on one line (fold/T2-home-ar-d.png); centred chrome hides mirroring; the mobile record reads calmly (fold/T2-record-ar-m.png).
**MUST-FIX:** URL corrupted at every width: «ar/readings/same-year-different-/» + «/number» (crops/T2-reading-ar-figure.png; tiles/T2-reading-ar-m-3.png).
**SHOULD-FIX:** bold Latin digits inside a light Arabic paragraph make 561 / 1,473 / 8.55% the loudest objects on the page — the numbers leave their sentence visually (crops/T2-record-ar-primary.png); mobile H1 strands the preposition «في / اليمن» and widows «واحدًا.» (fold/T2-home-ar-m.png); the two lane titles nearly touch (crops/T2-reading-ar-figure.png); «رقم / مختلف» split (fold/T2-reading-ar-m.png).
**Misreading:** the bold digits read as headline figures, the light Arabic as caption.

### T3 · Strata
**Establishes:** strata order and index numerals mirror properly; question chips keep 01→05 in RTL (fold/T3-record-ar-m.png); dates intact in list columns (tiles/T3-home-ar-d-2.png).
**MUST-FIX:** URL corrupted («ar/readings/same-year-/» + «/different-number», tiles/T3-reading-ar-m-3.png; desktop crops/T3-reading-ar-figure.png); the second alt-table is clipped at reading-start at 390 (tiles/T3-reading-ar-m-4.png).
**SHOULD-FIX:** mobile meta breaks «مارس / 2025 – يناير 2026» and «آخر / مراجعة» (fold/T3-record-ar-m.png, fold/T3-reading-ar-m.png); H1 widow on desktop, «في / اليمن» on mobile (fold/T3-home-ar-d.png, fold/T3-home-ar-m.png).
**Misreading:** a clipped table reads as a table with missing values — layout undermines "missing ≠ zero".

### T4 · Instrument
**Establishes:** URL isolated, wraps cleanly at 1440/390/320 (inspect/crops/T4-reading-ar-figure@320.png); value labels legible at desktop (crops/T4-reading-ar-figure.png); mobile H1 breaks without stranding «في» (fold/T4-home-ar-m.png, inspect/T4-home-ar-fluid@320.png); reading title fits one mobile line (fold/T4-reading-ar-m.png); the seven-question order is identical in spine and body (fold/T4-record-ar-d.png); no overflow 320–430; dates intact in margins (tiles/T4-home-ar-d-2.png).
**MUST-FIX:** (a) panel 1 is mirrored but its axis is not — labels at reading-start (right), zero at reading-end (left), so the eye meets the dot before the baseline (crops/T4-reading-ar-figure.png); Arabic horizontal bars grow from the right; (b) at 390/320 every value label (6,245; 3,422.16; 100.0…118.0) disappears — both languages (inspect/crops/T4-reading-ar-figure@390.png, …en-figure@320.png).
**SHOULD-FIX:** desktop H1 widow «واحدًا.» (fold/T4-home-ar-d.png); dangling dash «– عدن 2024» at line start (crops/T4-reading-ar-figure.png); «(Global / Findex)» split at 768 (inspect/T4-home-ar-fluid@768.png); «↗» not mirrored (tiles/T4-record-ar-d-2.png); «ثلاثة أشياء / مختلفة» widow at 320.
**Misreading:** on inspect/crops/T4-reading-ar-figure@390.png a reader cannot state the two 2024 values without opening the text description.

## 2. Ranking

**T4 > T3 > T2 > T1.** T4 is the only proposition whose Arabic survives every width without corrupting a link, clipping a table or splitting a date; its faults are compositional (axis, widows), not structural. T3 mirrors cleanly but breaks the link and the table. T2 is calm, but light text with bold digits is the wrong idea for Arabic and its link is broken everywhere. T1 has the most Arabic-only breakages. None would convince an Arabic-first senior that Arabic came first: all four are competent mirrors; T4 is the disciplined mirror.

## 3. Convergence

What T4 makes easy that T3 does not: copying a correct canonical link from any Arabic screen; reading the two 2024 values off the figure at desktop; navigating a record by a question number that matches the spine. As Arabic composition: nothing material — the gain is bidi engineering, not Arabic-first design.

## 4. Three improvements (T4)

1. Compose panel 1 for RTL: zero at reading-start, values growing leftward; keep value labels at all widths (in the row, never hover).
2. Line-break contract: nowrap on «– عدن 2024», «(Global Findex)» and date tokens; balanced H1 so «واحدًا.» never stands alone (mobile already breaks it right).
3. One numeric policy in the Arabic contract: isolate every numeric token so `8.55%` has one visual form in stats and prose; mirror the external-link glyph; state the digits decision (Western vs Eastern) as a rule.

## 5. ESCALATION CANDIDATES

- Figure credit in English on Arabic figures — «المصدر: IMF / Yemeni authorities; Central Bank of Yemen — Aden; International Monetary Fund» (crops/T1–T4-reading-ar-figure.png) — while the same sources are Arabic in Sources (tiles/T4-reading-ar-d-5.png).
- Separator drift: table «6245» vs chart «6,245»; table «118» / «100» vs chart «118.0» / «100.0» (tiles/T1-reading-ar-d-2.png, tiles/T1-reading-en-m-3.png, crops/T4-reading-ar-figure.png).
- Period format drift: «07-11-2022 إلى 09-01-2023» in «متى قيس أو رُصد؟» vs «من نوفمبر 2022 إلى يناير 2023» in body (tiles/T4-home-ar-d-2.png); English «Mar-2025–Jan-2026» vs Arabic «مارس 2025 – يناير 2026» (fold/T1-record-en-d.png / -ar-d.png).
