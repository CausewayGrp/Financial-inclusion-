# Accessibility audit — the implemented runtime (EAD-02)

**Status:** AUDIT RECORD — NOT A CONFORMANCE CLAIM. Machine-checkable outcomes only. Screen readers in Arabic and English, and every judgement a person must make, are outstanding (see 'outstanding_for_a_human_auditor'). The Accessibility page states no result.

Measured 2026-09-29 on `639cc3bea395`, with `scripts/accessibility_audit.py`: 24 pages (one per route class, both languages) at 1440 px and 390 px, plus a 320 px reflow pass, reduced motion, images off, and a keyboard walk. The general ruleset is `axe-core@4.10.2` (SHA-256 `b511cd9dec01c76f…`).

## What the general ruleset found

| Rule | Impact | WCAG | Nodes | Pages | What it means |
|---|---|---|---|---|---|
| `landmark-unique` | moderate | best practice | 20 | 20 | Landmarks should have a unique role or role/label/title (i.e. accessible name) combination |
| `empty-table-header` | minor | best practice | 12 | 8 | Table header text should not be empty |

## The contract's outcomes, measured

| Outcome | WCAG | Measured |
|---|---|---|
| Keyboard access | 2.1.1, 2.1.2, 2.4.3 | skip link first and moves focus into `main`; menu and dialog close on Escape and return focus; no keyboard trap |
| Visible focus | 2.4.7, 2.4.11 | `3px` outline, offset `3px`; focused target clear of the sticky bar |
| Target size | 2.5.8 | 3166 measured; 21 under 24 × 24 px, of which 5 meet the criterion's inline exception and 16 its spacing exception — **0** meet neither |
| Reflow | 1.4.4, 1.4.10 | 320 px (400 % of 1280 px): 0 routes overflow in English, 0 in Arabic |
| Names | 4.1.2, 1.3.1, 2.4.6 | 0 interactive elements and 0 landmarks without a name |
| Labels | 3.3.1, 3.3.2 | 0 controls without a label |
| Contrast | 1.4.3 | **0** text/background pairs under the required ratio |
| Text alternatives | 1.1.1, 1.3.1 | 0 images without `alt`; every drawn visual's alternative listed below |
| Reduced motion | 2.3.3 | `scroll-behavior: auto`, 0 animated elements |
| Headings | 1.3.1, 2.4.6 | pages with other than one `h1`: 0; heading-level jumps: 0 |
| Images off | 1.1.1 | main text still 14,757 characters in English, 13,774 in Arabic |

### Landmarks that share a name

A screen-reader user listing landmarks sees these twice with the same name and cannot tell them apart.

| Role | Name |
|---|---|
| nav | Continue from here |
| nav | تابع من هنا |

## Text alternative for every drawn visual

What a reader gets instead of the picture, from the governed contract.

| Visual | Tier | Rows | Alternative (EN / AR characters) | Boundary stated | Fallback form |
|---|---|---|---|---|---|
| `RV-CWR-001` | SIGNATURE | 3 | 957 / 937 | yes | Panel 1: two-row table (publication, reference year, value in USD million, sourc |
| `RV-CWR-004` | CORE_ANALYTICAL | 3 | 1093 / 1022 | yes | Table: lane, date, what is recorded. |
| `RV-CWR-009` | SIGNATURE | 2 | 1591 / 1408 | yes | Ordered list of steps with state, dated events and links. |
| `VIS-FINDEX-GAPS` | CORE_ANALYTICAL | 1 | 1212 / 1052 | yes | Table: group, value (%), note. |
| `VIS-FIRM-CONSTRAINTS` | CORE_ANALYTICAL | 1 | 930 / 795 | yes | Table of all 16 governed items. |
| `VIS-PAYMENT-ANATOMY` | CORE_ANALYTICAL | 1 | 785 / 630 | yes | Table: object, value or withheld state, what it is not. |
| `VIS-PAYMENT-RAILS` | SUPPORTING | 0 | 1778 / 1581 | yes |  |
| `VIS-POS-TERMINALS` | CORE_ANALYTICAL | 1 | 942 / 856 | yes | Table: month, value, note. |
| `VIS-POS-TRANSACTIONS` | CORE_ANALYTICAL | 1 | 1087 / 949 | yes | Table: month, value, note. |
| `VIS-POS-VALUE` | CORE_ANALYTICAL | 1 | 843 / 722 | yes | Table: month, value (YER million) or 'no verified value'. |
| `VIS-PROVIDER-OBSERVABILITY` | SIGNATURE | 5 | 1501 / 1219 | yes | Table with caption, one row per class, scoped headers. |
| `VIS-REMITTANCE-COST` | CORE_ANALYTICAL | 1 | 719 / 661 | yes | Table: corridor, amount, cost (%). |
| `VIS-REMITTANCE-MACRO` | CORE_ANALYTICAL | 1 | 1046 / 929 | yes | Table: year, value, state, source document. |

## What was fixed because of this audit, and what was not

Two findings were failures against outcomes the contract itself states, so they were fixed and remeasured:

- **1.4.3 contrast.** The institutional band's fine print (`--mute` on `--plaster`) measured **4.42:1** where the
  contract requires 4.5:1 — on all 288 pages, in both languages. `--mute` moved two points darker, `#66717B` →
  `#646F79`: 4.56:1 on the band and 5.13:1 on paper. The role is unchanged and the change is imperceptible; it is the
  smallest value that meets the rule the design published.
- **2.5.8 target size.** Of 129 targets under 24 × 24 px, 117 met one of the criterion's own exceptions (inline, or
  24 px spacing). Twelve met neither: the institutional band's group links, the disclosure summaries and the record
  list inside one, all 22–23 px tall with neighbours closer than 24 px. The design already had a rule for exactly this
  (`min-height: 24px` with 3 px padding, applied to hub, source, chronology and dependency links); it was extended to
  the three families it had missed. Now none fails.

Two findings were **not** fixed, because neither is Code's to decide:

- **Landmarks sharing a name** (best practice, 20 occurrences): the page's "Continue from here" section and the
  spine's first edge group carry the same governed title, so a landmark list shows it twice. Which of the two changes,
  and to what, is a composition and naming decision — recorded in `design/ESCALATIONS.md` with three options.
- **An empty table header** (best practice, 12 occurrences): the corner cell of a figure's fallback table. Design
  recorded this at D2 and again at DEBT-013's closure: no unheaded *data* column ships, and the corner-cell label
  stays a preference rather than an authority question. It needs a governed label, which Code does not write.

## What a person still has to do

This record covers what a machine can decide. None of the following is settled by it, and the Accessibility page states no result until they are:

- Screen-reader passes in Arabic and in English (at least one of NVDA/JAWS and VoiceOver), on a record, a Reading, Compare, the source directory and a domain answer: is what is announced the truth the page states?
- Whether every heading describes its section, and whether the reading order a screen reader announces in Arabic matches the order a sighted Arabic reader follows (1.3.2, 2.4.6).
- Whether the text alternative of each drawn visual conveys the same analytical point as the picture, which is a judgement about meaning and not a property of the markup (1.1.1).
- Voice control and switch access; 200 % browser zoom on a real device as well as the 400 % reflow case.
- Forced-colours mode judged by eye: the checks confirm the rules exist, not that the result reads well.
- Whether any technical state could be mistaken for an evidence state by a reader who cannot see the styling.

No WCAG conformance is claimed here, at any level.
