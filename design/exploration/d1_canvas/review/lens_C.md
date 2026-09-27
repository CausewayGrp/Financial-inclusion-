# LENS C — Accessibility and cognitive UX (WCAG 2.2 AA as target; no conformance claimed)

Paths are under `out/`. Contrast ratios are computed from each board's TOKENS. Headings, landmarks, target boxes and overflow were confirmed on the `out/local` builds in a scratch headless render (nothing written to the repo). Caveats: `inspect/crops/*@320|@390` are a 09:01–09:07 build and disagree with the 09:12 tiles; the working tree also holds uncommitted 09:26–09:29 edits to t4.py/proto_common.py (not this lens's) that already restyle T4's spine and strip, so re-render T4 before acting on its items.

## Shared defects (all four)

- MUST-FIX: the record's governed questions and its boundary are not headings. Outline of `/evidence/CLM-003/`: T1 h1→h2 "Original source"; T2 h1→h3,h3→h2; T3 and T4 h1→h3 (sidebar edges) only. A screen-reader user navigating by headings never meets "What this evidence does not establish" (`fold/T*-record-en-d.png`; spans/labels at t1.py:270–272, t3.py:274–277, t4.py:391–395).
- SHOULD-FIX: no `:focus`/`:focus-visible` rule and no skip link in any board; 18 tab stops precede `<main>` on T1–T3 desktop, 11 on T4.
- SHOULD-FIX: no mobile target reaches 44 px: header text buttons 20–22 px, chips 28–32 px, T2 TOC rows 19 px, T4 spine/edge links 19–22 px (spacing keeps them above the 24 px minimum).
- Figure values sit in `aria-hidden` SVGs; the sr-only figcaption and table carry them (table collapsed in T2/T4: `crops/T2-reading-en-figure.png`).
- Colour never carries a state alone: boundaries are rule + label (+ weight); panel-1 marks differ by shape. No finding.

## T1 · Register

Establishes: the clock precedes the claim in DOM and margin (`fold/T1-record-en-d.png`); ink 16.5:1, mute 5.45:1.
MUST-FIX: "8.55%" and "+11%" are 30 px bare numbers with 13.5 px captions; on mobile "+11%" closes the first screen with its caption cut off (`fold/T1-record-en-m.png`, `crops/T1-record-en-primary.png`). The bound is the small text.
MUST-FIX: figure value labels do not render (0×0 boxes) and axis text scales to 7.5–8.5 px in the index lanes (`crops/T1-reading-en-figure.png`, `tiles/T1-reading-en-m-2.png`); values are readable only from the table.
SHOULD-FIX: clock value in 13.5 px mute; no in-page index on a nine-tile reading (`tiles/T1-reading-en-m-*`); link underlines at 2.16:1.
Misreading: a margin screenshot reads "+11%" as the record's headline growth.

## T2 · Argument

Establishes: lowest vocabulary, one column, 19 px body; numbers bold inside the sentence that bounds them (`crops/T2-record-en-primary.png`); labelled TOC `<nav>`; boundary = label + bar (`fold/T2-reading-en-m.png`).
MUST-FIX: same figure defect — no value labels, axis text 7.9–9.4 px, table behind "+ Text description" (`crops/T2-reading-en-figure.png`).
SHOULD-FIX: statements in weight 300 at 26 px, Arabic included (`fold/T2-record-ar-d.png`); period and universe demoted to a 15 px list under a 26 px claim (`fold/T2-record-en-d.png`); h3 before any h2; product name printed twice on the mobile home (`fold/T2-home-en-m.png`); "Evidence records behind these figures" collapsed (`tiles/T2-home-en-m-2.png`).
Misreading: the light 26 px statement reads as an essay lede, so 8.55% and +11% read as two facts rather than a recorded disagreement.

## T3 · Strata

Establishes: numbered plain-language strata answer→scope→boundary→source (`fold/T3-record-en-d.png`); trail colour 7.7:1; visible tables.
MUST-FIX: on mobile the index chips precede the content on every surface and push the reading's boundary to the second screen (`fold/T3-reading-en-m.png`, `fold/T3-reading-en-m-2.png`, `fold/T3-record-en-m.png`, `fold/T3-home-en-m-2.png`, same in Arabic `fold/T3-record-ar-m.png`). Figure: no value labels, axis 8–10 px (`crops/T3-reading-en-figure.png`).
SHOULD-FIX: strata boundaries at 1.22:1 (surface on ground) and 2.13:1 (band rule) vanish for low vision; the trail is an unlabelled `<aside>`, not a nav; the table scrolls sideways with its caption clipped mid-word and no scroll cue (`tiles/T3-reading-en-m-3.png`); mute on ground 4.63:1 is marginal.
Misreading: first mobile screen = title plus five chips; a cold reader takes the page for a menu.

## T4 · Instrument

Establishes: every number sits in a sentence or labelled object with its clock (`crops/T4-record-en-primary.png`); the figure prints values on the marks and horizontal rows stop the 2024 values stacking (`crops/T4-reading-en-figure.png`; labels confirmed at 320 on the current build); boundary = double rule + label + weight + teal 8.4:1 (`fold/T4-record-en-m-2.png`); 320 px reflow without overflow, Arabic at 18 px/1.9 (`inspect/T4-record-ar-fluid@320.png`); strip after the first answer; ochre rubrics 6.35:1.
MUST-FIX: mute on plaster is 4.42:1 — spine index numerals and figure axis labels (`fold/T4-record-en-d.png`, `crops/T4-reading-en-figure.png`).
SHOULD-FIX: `nav.strip`, `nav.index`, `aside.spine` unlabelled; figure h4/h5 precede the first h2; question and clock precede the h1 in DOM (`fold/T4-reading-en-m.png`); the nine-chip strip separates the boundary from section 01 (`fold/T4-reading-en-m-2.png`); first-visit vocabulary (WHEN/FOR WHOM, double rule, 01–07) is the largest of the four, though identical on every page.
Misreading: none from the primary crop; the panel-1 rows alone carry labels, values and the zero axis.

## Ranking for this lens

T4 > T2 > T3 > T1. Only T4's figure reads without the table, and only T4 keeps every number inside its bound. T2 is the calmest for cognition but demotes bounds and thins the statement. T3 is clear on desktop, obstructive on mobile. T1's margin numbers are the most misusable object in the set.

## Convergence

T4 lets a sighted user read 6,245 / 3,422.16 and the four index values from the figure at 320–1440 px, and never meets a number without its clock; T2, the strongest first-generation proposition, needs the collapsed table or the prose. Material for low-vision and cognitive access. Everything else (headings, landmarks, focus, targets) is parity.

## Three improvements to T4

1. Make questions 01–07 `h2` elements, the boundary included; label the strip and spine navs; add a skip link and a `:focus-visible` outline in the double-rule vocabulary.
2. Stop using mute on plaster: set spine numerals, `.lbl` and `.ax` text in ink-2 or darken `--mute`; raise `.lbl` to 12 px.
3. Put the hit padding on spine and edge `a` elements (≥ 24 px, 44 px on touch) and collapse the mobile strip into one "Jump to" disclosure so chips never separate answers.

## ESCALATION CANDIDATES

- Table alternative prints `6245` while marks and prose print `6,245` / `USD 6.245 billion`; `118` versus `118.0` (`crops/T*-reading-en-figure.png`).
- Period token `Mar-2025–Jan-2026` mixes hyphen and en dash; screen readers voice it as arithmetic (`fold/T*-record-en-d.png`).
- Reading guidance ("How should this record be read?") sits behind a disclosure in all four; confirm it holds no qualification of the headline.
