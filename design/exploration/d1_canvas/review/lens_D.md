# Lens D — data visualisation (RV-CWR-001; Home "system" text)

Paths are under `out/`. `scratch/…` = my re-renders of the current `out/local/*.html` at 320/390 px (scratchpad only).

## Shared defects (one chart component in all four)

- **MUST-FIX — mark grammar collides across panels.** Panel 1: ● = Annual Report 2024, □ = Annual Report 2025. Panel 2: ● = CBY AR 2025, □ = IMF. The same source changes glyph; a reader who learned the legend reads the IMF lane as AR 2025 (`crops/T1…T4-reading-en-figure.png`, all AR crops).
- **SHOULD-FIX — index origin.** Lanes draw their baseline at 95; the origin 100 is a gridline, named only by the header. T4 even styles "95" as `.lbl.origin` (`local/T4-reading-en-d.html`). Four annual observations are joined by a solid line (continuity the data lacks).
- **SHOULD-FIX — divider referent.** The bundle attaches NOT_COMPARABLE to the two index series (`design/reference/out/_bundle/readings_same-year-different-number__en.json:474–535`); no proposition places the divider between the lanes. T2–T4 use it as a heading over panel 2; T1 puts it between the panels (below).
- **Home "system":** no proposition invents a chart; all four render text (`tiles/T1-home-en-d-3.png`, `T2…-3`, `T3…-3`, `T4…-3`; no `<svg>`/`<canvas>` in any home HTML, EN or AR). T4's `.fig` frame gives it figure chrome without a figure — reads as a placeholder.

## T1 · Register

Establishes: tables inline in the frame, so a screenshot carries the raw levels (2,900.22 vs 1,577.7) that the identical paths hide (`crops/T1-reading-en-figure.png`); Arabic canonical link intact (`crops/T1-reading-ar-figure.png`); panels and lanes stack at 390 (`scratch/T1-en-fig@390`).
MUST-FIX: value labels never render — all ten `<text class="val">` wrap an HTML `<bdi>` inside SVG text (`local/T1-reading-en-d.html`), so panel 1 is two unlabelled marks read against a 2,000-step axis. The vertical "Not directly comparable" divider sits between panel 1 and panel 2, telling the reader the two 2024 values are not comparable — contradicting "Same year, different publication" and the bundle's referent.
SHOULD-FIX: stacked marks in publication order (high ● over low □) read as a drop; fixed-viewBox SVG shrinks at 390 (ticks ≈9 px, in-chart "USD million" ≈7 px, duplicating the header); Arabic legend orphans "2024"/"2025" on a line of their own.
Cold misreading: "remittances fell from about 6,200 to about 3,400".

## T2 · Argument

Establishes: quiet frame, note adjacent to the lanes.
MUST-FIX: same invisible labels (`local/T2-reading-en-d.html`); the table is behind "+ Text description", so the crop carries no number except ticks (`crops/T2-reading-en-figure.png`) — a screenshot can neither be checked nor quoted; the Arabic canonical link is bidi-scrambled across its wrap ("ar/readings/same-year-different-/" … "/number") (`crops/T2-reading-ar-figure.png`).
SHOULD-FIX: "Not directly comparable" tops the right column level with "2024 · USD million", reading as "right panel not comparable with left"; boundary typeset in a half-width column; lanes fill ~70 % of the column at 390 (`scratch/T2-en-fig@390`); Arabic lane headings run together on one baseline.
Cold misreading: the fall, plus "two sources agree".

## T3 · Strata

Establishes: strata rules separate note and boundary; tables inline.
MUST-FIX: at 390 the inset clips the text/table alternative — EN headings cut ("Referen…", "inde…"), IMF column truncated (`tiles/T3-reading-en-m-3.png`, `scratch/T3-en-fig@390`); in Arabic the IMF header loses digits ("2025" shows as "25") (`scratch/T3-ar-fig@390`) — a wrong number on screen. Same invisible labels (`local/T3-reading-en-d.html`). Arabic link scrambled (`crops/T3-reading-ar-figure.png`).
SHOULD-FIX: axis labels in `--mute #5E6874` on the tinted inset are the faintest of the four (`crops/T3-reading-en-figure.png`) and shrink to ≈9 px at 390; duplicate in-chart unit; orphaned legend years in Arabic.
Cold misreading: as T1, with an axis too faint to correct it.

## T4 · Instrument

Establishes: panel 1 as rows on a horizontal zero-based axis, publication label in the row, value printed on the mark — no legend, no axis reading, no stack (`crops/T4-reading-en-figure.png`); fluid SVGs recompose at 320/390 with text held at 11–12.5 px (`scratch/T4-en-fluidfig@320`, `scratch/T4-ar-fluidfig@320`); lane points printed, so the identity 105.74/111.73/118.0 is visible with the note beneath; Arabic link intact (`crops/T4-reading-ar-figure.png`).
MUST-FIX: mark collision (shared).
SHOULD-FIX: "100.0" label stacks on the "100" tick at the origin (`crops/T4-reading-en-figure.png`, @320); precision drift 118.0/100.0 against the table's 118/100; table behind a disclosure, so the crop lacks raw levels; rows in publication order (longer above shorter) still permit a "shrank" narration, held off only by header and caption; in Arabic the zero origin sits on the far side from the row labels (`crops/T4-reading-ar-figure.png`) — a decision to state; `table.rvtab` measures 8 px over at 320 — check with the description open.
Process: `inspect/crops/T4-reading-*-figure@1440/390/320.png` predate the current build (09:07 vs HTML 09:10) and show no printed values; do not judge T4 from them.

## Ranking for this lens

**T4 > T1 > T2 > T3.** T4 is the only proposition whose figure prints a single value and whose panel 1 cannot stack as a fall; its defects are shared or minor. T1 beats T2 because its alternative is visible and its Arabic link survives. T3 is last: its alternative clips and loses a digit.

## Convergence

Material. T4 lets a reader take the two 2024 values as magnitudes from zero, each labelled and numbered in its own row, at any width. In T1 the same act needs legend → glyph → axis, the marks still stack, and the only argument against the fall reading is text.

## Three improvements to T4

1. One glyph per source across the whole figure: AR 2024 ●, AR 2025 □ in both panels, IMF a third shape.
2. Draw the lane baseline at 100 (or emphasise and label the 100 line "2021 = 100", drop the duplicate "100.0"), and print each lane's raw 2021 level under its title so the 1.84× level gap sits beside the identical paths.
3. Make "Not directly comparable" a divider between the lanes (vertical on desktop, a rule between the stacked lanes on mobile) and open the table alternative by default at ≥768 px.

## ESCALATION CANDIDATES

- Table prints "6245" ungrouped beside "3,422.16" (`crops/T1…`, `T3…`; bundle stores `y: 6245`; its alt_text says "US$6,245 million") — a governed formatting rule is needed.
- Precision: figure contract 118.0/100.0 versus table 118/100.
- Credit line appears in Latin only inside the Arabic figure (all AR crops).
- Divider referent: the bundle marks the index series NOT_COMPARABLE; the contract prose does not say where the divider goes; propositions differ.
