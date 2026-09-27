# Lens H — source-institution statistician (CBY-Aden · IMF · World Bank/Findex)

Paths are under `/home/user/Financial-inclusion-/design/exploration/d1_canvas/out/`. Governed text is identical across T1–T4; only composition is judged. Checked in `local/*.html`: every "Open original source ↗" resolves to a cby-ye.com or imf.org PDF and "Open source record" to `/en/data/?source=…`, so the path is honest in all four.

## 1. Per proposition

**T1 · Register**
- Establishes: the table alternative is open under the figure, so a screenshot carries 6245 / 3,422.16 and both index columns (`crops/T1-reading-en-figure.png`); source chips sit in a dedicated "Source verification path" column (`tiles/T1-record-en-d-2.png`).
- MUST-FIX: the sidebar typesets "8.55% — Calculated here from published figures" above "+11% — Source figures disagree — both are shown" (`crops/T1-record-en-primary.png`, `fold/T1-record-en-m.png`; AR "أرقام المصدر غير متسقة", `crops/T1-record-ar-primary.png`). The derived figure leads with a neutral tag; the Bank's displayed figure follows with a fault tag. This is the composition CBY-Aden would formally ask to be corrected. The labels exist only in T1's HTML (`local/T1-record-*.html`).
- MUST-FIX: AR mobile clips the IMF index column at the page edge: 105.74 renders as "05.74", 111.73 as "1.73" (`tiles/T1-reading-ar-m-4.png`) — wrong numbers attributed to the IMF.
- SHOULD-FIX: panel-1 legend binds ● = Annual Report 2024, □ = Annual Report 2025; panel 2 reuses ● for CBY AR 2025 and □ for the IMF (`crops/T1-reading-en-figure.png`). Axis labels ≈7 px (`tiles/T1-reading-en-d-2.png`).
- Misreading: "the source got +11% wrong; 8.55% is the correction."

**T2 · Argument**
- Establishes: all six numbers bold at parity inside the sentence (`crops/T2-record-en-primary.png`, `crops/T2-record-ar-primary.png`); credit and canonical link travel with the figure (`crops/T2-reading-en-figure.png`).
- SHOULD-FIX: the figure prints no value and the table is collapsed behind "+ Text description of this view", so a screenshot shows two unlabeled dots stacked vertically at 2024 (`crops/T2-reading-en-figure.png`, `tiles/T2-reading-en-m-3.png`).
- SHOULD-FIX: the AR canonical link wraps as "ar/readings/same-year-different-/" + "/number", an unusable path (`crops/T2-reading-ar-figure.png`).
- Same mark reuse as T1.
- Misreading: higher dot, lower dot, same year → "remittances fell".

**T3 · Strata**
- Establishes: "Not directly comparable" heads the index band, i.e. sits on its true referent (`crops/T3-reading-en-figure.png`); table open under the figure.
- MUST-FIX: on mobile both tables overflow and are cut; the IMF index column and the captions are lost (`tiles/T3-reading-en-m-3.png`, `tiles/T3-reading-en-m-4.png`; AR `tiles/T3-reading-ar-m-4.png`).
- SHOULD-FIX: axis tick labels are near-invisible light grey while the product's commentary is full-contrast (`crops/T3-reading-en-figure.png`): the source's scale looks weaker than the commentary. AR link wrap as T2 (`crops/T3-reading-ar-figure.png`).
- Misreading: an IMF column with no index values reads as "the IMF has no comparable series".

**T4 · Instrument**
- Establishes: 8.55% and +11% appear only inside the governed sentence, no callouts (`crops/T4-record-en-primary.png`, `inspect/crops/T4-record-ar-primary@390.png`); panel 1 as horizontal rows from zero with "6,245" and "3,422.16" printed beside their publication (`inspect/crops/T4-reading-en-figure@1440.png`, `crops/T4-reading-ar-figure.png`), so a restatement cannot read as a fall; AR link wraps legibly (`inspect/crops/T4-reading-ar-figure@390.png`); "06 Original source and verification" is one tap from the index on mobile (`fold/T4-record-en-m.png`, `tiles/T4-record-ar-m-3.png`).
- SHOULD-FIX: at 390 and 320 the row values and lane labels vanish although present in the markup (`inspect/crops/T4-reading-en-figure@390.png`, `…en-figure@320.png`, `…ar-figure@320.png`; `local/T4-reading-en-m.html` carries two `class="val"`). With the text description collapsed, a mobile screenshot carries no published value.
- SHOULD-FIX: mark reuse as above; the CBY AR 2025 value is □ in panel 1 and ● in panel 2.
- SHOULD-FIX: "Not directly comparable" sits on the divider between panel 1 and panel 2 (`crops/T4-reading-en-figure.png`), readable as "the two annual reports are not comparable".
- Misreading (mobile): two unvalued rows of different length → "one report is bigger", magnitude unknown.

**Correction requests by institution.** CBY-Aden: T1's callout pairing; the Arabic credit line (all four). IMF: double naming in the credit and no estimate state on its lane (§5). World Bank/Findex: none — the Findex figures appear only inline with their vintage and coverage caveat in every proposition (`fold/T4-home-en-d.png`, `tiles/T1-home-en-d-2.png`, `tiles/T3-home-ar-d-2.png`).

## 2. Ranking

T4 > T2 > T3 > T1. T4 is the only proposition in which no source number is typeset outside its sentence and the two CBY-Aden values carry publication and value together. T2 is clean but shows no values. T3 clips the IMF's numbers on mobile. T1 is last: its callout pairing is the one composition a source would contest, and it also clips the IMF index in Arabic.

## 3. Convergence

On desktop T4 lets a reader verify the restatement from the figure alone — publication, value, zero axis, credit in one frame — without opening the table (`inspect/crops/T4-reading-en-figure@1440.png`); T2 cannot (`crops/T2-reading-en-figure.png`). As rendered on mobile the advantage disappears (values missing), so it is material only above roughly 430 px.

## 4. Three improvements to T4

1. Make row values and lane labels render at 320–430 (they are in the DOM), or fold the value into the row label ("CBY-Aden Annual Report 2024 · 6,245"); open the text description by default on the Reading.
2. One mark per series across both panels: □ for Annual Report 2025 in panel 1 and its lane, a third mark for the IMF lane; carry each lane's state ("reported" / "staff reconstruction") in its title.
3. Attach "Not directly comparable" to the pair of lanes (a spanning label above both lane titles) instead of the divider under panel 1.

## 5. ESCALATION CANDIDATES (content, not design)

- AR credit line rendered in English in all four (`crops/T1-…T4-reading-ar-figure.png`); the IMF is named twice ("IMF / Yemeni authorities" and "International Monetary Fund").
- Table value "6245" lacks the thousands separator used for 3,422.16 and 2,900.22 (all four); T4's hidden description writes "US$6,245 million" (`local/T4-reading-en-d.html`).
- Index precision: table "100"/"118" against "105.74"/"111.73"; T4 lane labels "100.0"/"118.0" (`inspect/crops/T4-reading-en-figure@1440.png` vs `crops/T1-reading-en-figure.png`).
- IMF values carry no observed/estimated state in lanes or table although the Reading describes a reconstruction with a modelled personal-transfers component (`tiles/T1-reading-en-d-3.png`); CBY values carry "Reported by the source".
- T1-only labels "Source figures disagree — both are shown" / "أرقام المصدر غير متسقة — يُعرض الرقمان": absent from T2–T4; EN "disagree" ≠ AR "inconsistent".
