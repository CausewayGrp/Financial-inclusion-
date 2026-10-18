# The Folio proof — change and impact assessment (18 October 2026)

Baseline D: `dist/` as built at the G2 integration head (PR #62, `b5ca7ba6`: A · Register with DL-V2-011 and the
markup-order fix). Proposal T1: the Folio treatment with the display faces, revised once after the independent
critique. T0: the same treatment on the incumbent faces, kept as the no-new-font fallback. Every word, number, link,
boundary and citation is identical (HTML and JavaScript byte-identical, checked by the build); only CSS and font files
differ. Not a release candidate; not deployed; adopted only by an owner decision and its own Stage C transaction.

## 1. What changed, visibly (D → T1)

| Surface | D (accepted G2) | T1 (Folio) |
|---|---|---|
| Title | Plex Sans / Plex Sans Arabic 600, 30/28 px phone, 42/38 desktop; brass-300 anchor 36 × 2 | IBM Plex Serif 600 / Noto Naskh Arabic 600 (subset, no Latin: Latin inside an Arabic title falls back to Plex Sans Arabic 600), 32/33 px phone, 52/52 desktop; brass-700 anchor 56 × 2 |
| Statement | primary ink in G2, secondary ink after DL-V2-011 | secondary ink in English, primary ink in Arabic (the critique: the secondary ink thins Plex Sans Arabic) |
| Section headings | Plex 600 at the question size; rubric numerals muted | the display faces one step up; brass numerals; darker hairlines; more air (desktop gap 22 → 32 px) |
| Home, desktop (≥ 1200 px) | one column at 820 px: head, topics line, three figures, boundary … with the rail | an asymmetric spread at 1360 px: thesis, topics, boundary and starting questions on the start side; the three figures as one evidence register under a firm ink rule beside them, starting a line below the title; the rail stays |
| Home's three figures | ruled unit, no plate | the same unit inside the register (no box after the revision) |
| Record head | title, clocks stacked, tools | title, the clocks as a ruled two-column register with brass labels (one column on phones) |
| Boundary | double counter-green rule | single firm counter-green rule, spaced rubric |
| Masthead and rail | 2 px ink rule; grey rail | 1 px ink rule; brass for the current hub; brass top rule on the rail |
| Calls to action | 2 px radius, 40 px | square, 42 px |

## 2. Measured (the same routes, widths and script for every variant; `metrics_table.md` has every view)

- Home on the desktop is shorter and answers sooner: EN 1440 5.5 → 4.3 screens, the first figure 0.8 → 0.5 screens,
  the first boundary 1.2 → 0.9; AR 1440 5.6 → 4.5, first figure 0.8 → 0.5.
- On the phone the titles are larger and the pages a touch longer: AR 390 Home 8.9 → 9.1 screens, the first figure
  0.8 → 0.9 screens; AR 390 /payments/ title 2 → 3 lines, the first boundary 0.9 → 1.0; EN 390 CLM-001 title 3 → 4 lines.
  No route grows by more than 0.3 screen on a phone; no horizontal overflow at any width; no governed text hidden
  (the phone index is hidden on the desktop by design, as in D).
- Bytes, cold at 390: T0 +1.3 KB per page; T1 +37 KB (AR: the 13 KB Naskh subset and 24 KB Plex Serif Latin-1; EN:
  +24 KB) — AR /data/ 322 → 346 KB (target ≤ 350), 4 font files per edition (limit ≤ 4). No JavaScript, no image.
- Accessibility (proxy, computed): contrast on the paper — brass-700 #7A5A1D 5.8 : 1 (labels and numerals, at 12–14 px
  bold), ink-2 8.5 : 1 (the English statement), the muted ink of the tools 4.7 : 1 (14.5 px, underlined links; above
  4.5 : 1, and the hover state is the green at 7.6 : 1); focus order unchanged (markup identical); the rendered-visibility
  gate's listed sets unchanged. The
  accessibility audit and the rendered-visibility gate are run on the shipped stylesheet only at adoption, in Stage C.

## 3. The independent critique and its disposition (`critique_T1_round1.md`)

| # | Finding | Disposition in the revision |
|---|---|---|
| 1 | Home's evidence register a cramped bordered box (≈ 45 characters), read as a callout | **Fixed**: the frame removed; the register under a firm ink rule; the column widened (1 : 1.25) at 1360 px; the figures' sentences at 19/20 px |
| 2 | Latin inside the Arabic record title in Plex Serif, larger than the Naskh | **Fixed**: the Naskh subset carries no Latin, so Latin falls back to Plex Sans Arabic 600, the matched companion; weight 600 throughout |
| 3 | Phone titles grew to three lines with weak breaks; stacked marks clotted in the bold | **Fixed in part**: display 34/36 → 32/33 px on phones and SemiBold instead of Bold; Home and the Readings back to two lines; /payments/ stays at three lines (its title is 44 characters at 33 px; D's 28 px gave two) |
| 4 | /payments/ first boundary off the phone's first screen | **Reduced**: 1.0 screens (D 0.9; before the revision 1.1); the recorded domain exception (1.0–1.2) holds |
| 5 | The secondary-ink statement too light in Arabic | **Fixed**: primary ink in Arabic, secondary in English |
| 6 | The phone evidence box narrowed the measure | **Fixed** with 1 |
| 7 | Three columns starting on the same line; no single entry point | **Fixed**: the register starts 72 px below the title's top; the thesis leads |
| 8 | The record's section numeral as tall as its question | **Fixed**: the heading rule no longer touches `h2.rubric` |
| 9 | A Reading's title at four lines | **Accepted** (the serif is wider; nothing shortened; 21ch measure) |

The critique's verdict on the faces stands after the revision: the Arabic Naskh reads with more authority than the
sans on the desktop and equal on the phone; the English serif reads better at title and section sizes; neither is
worse. T2 (Amiri) was built and viewed: a classical book voice and a 128 KB file; not taken further.

## 4. Judgement against the owner's criteria

| Criterion | D → T1 |
|---|---|
| Editorial sophistication and a distinctive CauseWay identity | better (the critique: "reads as a publication; D reads as a well-set website") |
| Arabic typographic quality | better on the desktop, equal on the phone after the revision; the one cost is a three-line /payments/ title |
| English typographic quality | better (serif titles and section heads; one Reading title a line longer) |
| Reader comprehension, hierarchy, source visibility | better on the record (the clock register) and on the desktop Home (the thesis leads, the evidence beside it at a reading measure); equal elsewhere; nothing hidden or moved |
| Real accessibility, responsive behaviour, performance | equal on the proxies above; +37 KB per page in T1 (within the budget), +1.3 KB in T0 |
| Reusability across families without architectural change | the treatment is ten CSS blocks over the shipped stylesheet and two font files; the only layout change is Home's desktop spread, written against the existing markup |

## 5. Recommendation

**Adopt T1** (the Folio treatment with the display faces), subject to the owner's review of the rendered pairs, as a
Stage C presentation transaction: the ten blocks folded into `scripts/yfie/theme.py` in place (no parallel stylesheet),
the two font files recorded in `design/08_ASSET_MAP.md` with their provenance and licence, the Naskh subset rebuilt
from the current upstream release, and the standing gates, the rendered-visibility gate, the accessibility audit, the
social-card fingerprint (the frame rules are untouched) and the negative controls run on the shipped build. If the
owner prefers no new font file, **T0** carries the composition on the incumbent faces at +1.3 KB and loses the
display voice the critique singled out. If the owner prefers the current first-screen numbers on the phone over the
dominant title, retain D: the limiting constraint is that a title one step larger costs 0.1 screen on a phone.

The visual pilot is not merged before the owner's review.
