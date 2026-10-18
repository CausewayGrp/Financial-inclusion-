# Accessibility audit — the implemented runtime (EAD-02)

**Status:** AUDIT RECORD — NOT A CONFORMANCE CLAIM. Machine-checkable outcomes only. Screen readers in Arabic and English, and every judgement a person must make, are outstanding (see 'outstanding_for_a_human_auditor'). The Accessibility page states no result.

Measured 2026-10-18 on `5ee0758137a0`, with `scripts/accessibility_audit.py`: 24 pages (12 routes in both languages, one per route class) at 1440 px and 390 px, plus a 320 px reflow pass, reduced motion, images off, and a keyboard walk. The general ruleset is `C:\Users\MAHERF~1\AppData\Local\Temp\axe\node_modules\axe-core\axe.min.js` (SHA-256 `b511cd9dec01c76f…`).

## What the general ruleset found

Nothing.

## The contract's outcomes, measured

| Outcome | WCAG | Measured |
|---|---|---|
| Keyboard access | 2.1.1, 2.1.2, 2.4.3 | skip link first and moves focus into `main`; menu and dialog close on Escape and return focus; no keyboard trap |
| Visible focus | 2.4.7, 2.4.11 | `3px` outline, offset `3px`; focused target clear of the sticky bar |
| Target size | 2.5.8 | 5126 measured; 30 under 24 × 24 px, of which 29 meet the criterion's inline exception and 1 its spacing exception — **0** meet neither |
| Reflow | 1.4.4, 1.4.10 | 320 px (400 % of 1280 px): 0 routes overflow in English, 0 in Arabic |
| Names | 4.1.2, 1.3.1, 2.4.6 | 0 interactive elements and 0 landmarks without a name |
| Labels | 3.3.1, 3.3.2 | 0 controls without a label |
| Contrast | 1.4.3 | **0** text/background pairs under the required ratio |
| Text alternatives | 1.1.1, 1.3.1 | 0 images without `alt`; every drawn visual's alternative listed below |
| Reduced motion | 2.3.3 | `scroll-behavior: auto`, 0 animated elements |
| Headings | 1.3.1, 2.4.6 | pages with other than one `h1`: 0; heading-level jumps: 0 |
| Images off | 1.1.1 | main text still 17,461 characters in English, 16,257 in Arabic |

## Text alternative for every drawn visual

What a reader gets instead of the picture, from the governed contract.

| Visual | Tier | Rows | Alternative (EN / AR characters) | Boundary stated | Fallback form |
|---|---|---|---|---|---|
| `RV-CWR-001` | SIGNATURE | 3 | 957 / 936 | yes | Panel 1: two-row table (publication, reference year, value in USD million, sourc |
| `RV-CWR-004` | CORE_ANALYTICAL | 3 | 1086 / 1018 | yes | Table: lane, date, what is recorded. |
| `RV-CWR-009` | SIGNATURE | 2 | 1620 / 1463 | yes | Ordered list of steps with state, dated events and links. |
| `VIS-FINDEX-GAPS` | CORE_ANALYTICAL | 1 | 1322 / 1118 | yes | Table: group, value (%), note. |
| `VIS-FIRM-CONSTRAINTS` | CORE_ANALYTICAL | 1 | 1140 / 993 | yes | Table of all 16 governed items. |
| `VIS-PAYMENT-ANATOMY` | CORE_ANALYTICAL | 2 | 1322 / 1080 | yes | One table per panel: object, value or withheld state, what it is not. |
| `VIS-PAYMENT-RAILS` | SUPPORTING | 0 | 2152 / 1893 | yes |  |
| `VIS-POS-TERMINALS` | CORE_ANALYTICAL | 1 | 1252 / 1145 | yes | Table: month, value, note. |
| `VIS-POS-TRANSACTIONS` | CORE_ANALYTICAL | 1 | 1313 / 1154 | yes | Table: month, value, note. |
| `VIS-POS-VALUE` | CORE_ANALYTICAL | 1 | 1216 / 1061 | yes | Table: month, value (YER million) or 'no verified value'. |
| `VIS-PROVIDER-OBSERVABILITY` | SIGNATURE | 5 | 1499 / 1221 | yes | Table with caption, one row per class, scoped headers. |
| `VIS-REMITTANCE-COST` | CORE_ANALYTICAL | 2 | 1534 / 1458 | yes | Table: corridor, amount, cost (%); a second table: year, average cost (%). |
| `VIS-REMITTANCE-MACRO` | CORE_ANALYTICAL | 1 | 1106 / 950 | yes | Table: year, value, state, source document. |
| `VIS-YER-MARKET-RATE` | CORE_ANALYTICAL | 1 | 675 / 577 | yes | Table: month, average market rate (rials per US dollar). |

## What a person still has to do

This record covers what a machine can decide. None of the following is settled by it, and the Accessibility page states no result until they are:

- Screen-reader passes in Arabic and in English (at least one of NVDA/JAWS and VoiceOver), on a record, a Reading, Compare, the source directory and a domain answer: is what is announced the truth the page states?
- Whether every heading describes its section, and whether the reading order a screen reader announces in Arabic matches the order a sighted Arabic reader follows (1.3.2, 2.4.6).
- Whether the text alternative of each drawn visual conveys the same analytical point as the picture, which is a judgement about meaning and not a property of the markup (1.1.1).
- Voice control and switch access; 200 % browser zoom on a real device as well as the 400 % reflow case.
- Forced-colours mode judged by eye: the checks confirm the rules exist, not that the result reads well.
- Whether any technical state could be mistaken for an evidence state by a reader who cannot see the styling.

No WCAG conformance is claimed here, at any level.
