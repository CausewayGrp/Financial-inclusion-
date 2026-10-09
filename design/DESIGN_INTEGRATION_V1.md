# V1 design integration — gate record

Status: **V1 PHASE 1 (SCREEN STYLESHEET) AND PHASE 2 (DISCLOSURE AND DENSITY) BUILT — FOR THE OWNER'S VISUAL REVIEW — NOT ACCEPTED.** The D7 package remains
the accepted design (`audit/OWNER_DECISIONS_2026-10-02.md`, row D7). This gate changes the presentation of that
accepted structure; it does not inherit D7's acceptance. Acceptance is the owner's, recorded by the owner in a dated
`audit/OWNER_DECISIONS_*.md` record when it is given. Nothing here declares DESIGN HANDOFF READY anew, PUBLIC RELEASE
READY, or WCAG conformance.

## 1. What the gate implements, and on whose instruction

The owner's message "Design integration v1, and the last records" (9 October 2026, Aden) sets the direction: the
palette and type of its design-system section, the eight references (two type samples, one moodboard, five mockups)
with the take/reject list of that message, rhythm and hierarchy rather than decoration. In the same session the owner
narrowed it, and this gate follows the narrower instruction wherever the two differ:

| Owner instruction (9 October 2026, this session) | Effect here |
|---|---|
| CSS-first and phased; preserve every text, datum, route, link, ID, data hook and behaviour; no file deleted or renamed | Every change is in the stylesheet; all 288 documents are byte-identical |
| The two controlled contracts, the Master, content JSON, `app.js`, tests and gates are not modified | None is modified; what needs them is escalated (`ESCALATIONS.md`, V1) |
| Palette exactly as briefed; `--paper #F7F5F0`, `--white #FFFFFF`; no new colour; no oak, wood or olive motif | §2 |
| A1: Arabic H1/H2 stay at the genuine SemiBold 600; Plex Sans Arabic Bold is not added | Not added |
| No Source Serif 4, no other font file, no modified subset, no synthesised weight | No font added; `font-synthesis:none` on screen |
| No currentness strip, colophon text, page-tools relocation, mobile-menu expansion, new copy or new filter in this phase | None built; each is escalated |
| PR #13 stays open, unchanged and unmerged | Not touched |

Branch: developed on `claude/design-review-constraints-l9au89`, the branch this execution environment may push, created
at `main` `7557866e99c390a6db2fd63ca4a5c63a86ef7e3e`, instead of the `design/integration-v1` name the owner's message
plans — the convention of D1–D7 (`ESCALATIONS.md`, process notes). One gate, one branch, one pull request.

## 2. Decisions

### DL-V1-001 · Palette: one green, warm paper, sage and brass
- Tokens (`scripts/yfie/theme.py` `:root`; generated into `02_TOKENS.json` by `reference/tokens.py`): `--paper #F7F5F0`,
  `--white #FFFFFF`, `--green-700 #005A44`, `--green-900 #0C3B2E`, `--sage-600 #5F7357`, `--sage-400 #8A9A82`,
  `--sage-100 #E7ECE4`, `--brass-700 #7A5A1D`, `--brass-300 #B8975A`, `--gold-300 #D6B86A`; `--ink`, `--ink-2` unchanged.
- The teal `#1E5650` is retired: `--counter` (the boundary voice) takes `#005A44`, so the site has one green.
  `--ochre-line` takes the brass hairline `#B8975A` (the gold is reserved for the deep-green field). `--plaster` (the
  figure surface) takes white, so a figure reads as a plate on the warm paper; `#F5F1E9` leaves the palette.
- Contrast measured against the surface each colour actually sits on: ink 14.95, ink-2 8.46, mute 4.71, brass-700 5.83,
  green-700 7.57 on paper; green-700 6.88, brass-700 5.30, ink-2 7.68 on sage-100; paper 11.47, sage-100 10.42,
  gold-300 6.50 on green-900; white 8.25 on green-700. `--mute` on sage-100 is 4.28, so no mute text is placed on a
  sage panel (the panel rules set ink-2 instead).

### DL-V1-002 · Type: hierarchy from size and weight in the shipped faces
- Latin display 52 px at ≥ 900 px (was 46), tracking −0.02 em; Arabic display 44 px (was 42); Arabic body leading 1.75
  (was 1.9), as the brief specifies. Headings stay at 600 in both scripts; no face, weight or file is added.
- The Latin serif of reference 02 is not implemented: the repository's font rules (`vendor/fonts/README.md`,
  `CONTRIBUTING.md` §2, `handoff/CLAUDE_DESIGN_MASTER_PROMPT.md` typography, `08_ASSET_MAP.md` §2) admit only IBM Plex
  files as shipped. Escalated for an owner decision; the verified provenance and licence of Source Serif 4 4.005R (SIL
  OFL 1.1, Reserved Font Name "Source") are recorded there.

### DL-V1-003 · Chrome
- Product bar on paper with a 2 px green-700 rule; on wide screens (≥ 1280 px) one row: brand, the four hubs, the
  Method & Measurement group with its governed label set above its two items, then Search, Cite, Report and the
  language switch. Below 1280 px the row may wrap, as before. Active hub in green-700.
- Colophon: the institutional band becomes green-900 with paper text and gold-300 group headings; the canonical logo
  sits on a paper tile, never on the dark field; focus on the band is gold-300. Its governed content is unchanged.
- Page tools: the existing cite, print, share and report controls of each page's utility row become one row of quiet
  tool buttons. They stay where they were and the header keeps its own cite and report links (relocation is a
  navigation-contract change, escalated).

### DL-V1-004 · The page head and the key figure
- The head's first call to action is a filled green-700 button and the second an outlined one (Home and the domain
  answers), 44 px high.
- Governed key values already marked as figures (`b.fnum`) in the first answer and the paced Home figures take
  green-700 at 1.22 em; they are never boxed (RC-1115's rule string is untouched).
- Home's three bounded figure records become white cards with a green-700 inline-start rule.

### DL-V1-005 · "What this does not establish" and the boundary family
- `.bnd`, the Compare verdict and its boundaries: a sage-100 panel under a 3 px double brass-700 rule; the boundary voice
  keeps its own colour (`--counter`). The double rule — the non-colour carrier of the boundary — is kept.

### DL-V1-006 · Objects, numerals, figures, tables, tools
- Structure rules of objects, figures, clusters, groups and the provider matrix in green-900; eyebrows in brass-700;
  section numerals (`.rubric .n`, the strip and spine indexes, the question list) in green-700, larger in a rubric.
- Figures: a white plate, 1 px frame, 3 px green-900 top; chart primary marks green-900; axes, labels, dashed and
  dotted marks and the not-comparable double rule unchanged (meaning stays in shape, never colour).
- Tables: heads on sage-100 under a 2 px green-900 rule.
- One filter-bar pattern: the search field and the source facets on sage-100, fields and selects with sage-600 borders
  (5.15:1 on white, above the 3:1 a control boundary needs).
- Disclosure markers, hovers and the active index entry in green-700; the spine index marks the current entry with a
  2 px green-700 rule.
- The social and export frames share the deep-green top rule; the 284 social images are regenerated by
  `scripts/social_images.py` (their frame HTML, and so `INDEX.json`, is unchanged).

### DL-V1-007 · Print unchanged
- The whole skin is inside `@media screen`. The D6 print system is untouched and prints in black on white as accepted.

### DL-V1-008 · Accessibility found by the full audit, fixed in the stylesheet
- Breadcrumb links, once green, differed from their text by colour alone (axe `link-in-text-block`, 1.4.1, on 476
  pages); they are now underlined (`sage-400`), as every other link in text is.
- `/rights/` overflowed at 320 px in both languages because of a long unbroken string in governed prose (present on
  `main` too); paragraphs, list items and definitions in an object now wrap such strings.
- The dependency disclosures of `/data/` measured 22 px with close neighbours (12 targets meeting neither 2.5.8
  exception, present on `main` too); they take the 24 px minimum the D2 rule already gives their siblings.

### DL-V1-009 · Phase 2: disclosure where the renderer owns the depth, with governed labels only
- The owner's mission of 9 October 2026 (content-page redesign with progressive disclosure) authorises renderer and
  HTML changes that keep every governed text, route, ID, hook and contract tier. The section tiers of
  `presentation_priority.json` (primary, always-visible band, the one progressive disclosure) are the steward's and are
  untouched; the validator's S03 and S04.1 shape checks still pass unchanged.
- Domain answers: the depth figures (`#views`, the views beside no first-screen answer, placed by the renderer's own
  `SMALL_MULTIPLES` and the bound visuals) are one disclosure. Its summary is the governed label that used to head them
  (`UI-DOM-A-VIEW-THAT-CHANGES-UNDERSTANDING`) with the number of views; the contract's primary visual stays first-load.
  Every figure keeps its visible text alternative once opened, and prints in full (D6).
- `/data/`: the dated chronology list is one disclosure; its summary is the governed heading already printed there
  (`UI-CHRONOLOGY-H`) with the number of events, and the section heading and body stay first-load. The source register
  is not collapsed: the locator-only path of DEBT-011 stays reachable without opening anything.
- No new public literal (`audit/PUBLIC_LITERAL_CLOSURE.json` unchanged: 14,563 records, 0 unresolved).

### DL-V1-010 · One disclosure pattern
- Every governed disclosure (the new folds, the domain and record `details.more`, the hub, group and dependency
  disclosures) reads the same: a named bar at least 44–48 px high whose whole width is the control, a `+`/`−` box in
  green-700 (decorative; its alternative text is empty), sage-100 when open or hovered, focus as everywhere else. The
  native `details` element keeps keyboard operation, the exposed expanded state and no-JavaScript behaviour.

### DL-V1-011 · Orientation on a phone
- Below 900 px the in-page index (`nav.strip`, the same links in the same order) becomes one horizontally scrolling row
  of chips under the head instead of a vertical list; each label is clamped to two lines in the chip and stays whole in
  the section it opens. The document never scrolls sideways (the row scrolls within itself).

### DL-V1-012 · Density by width
- Tablet (600–899 px, still one column): bound records, measurement cards and Readings sit two to a row.
- Desktop (≥ 1200 px): a source in the register reads as a row — title, publisher, reference and reuse state on the
  left; what it is for, what it does not establish and how to reach it on the right; its dependency disclosures below.
- Desktop keeps the sticky index beside the page; nothing on desktop is collapsed that is open on a phone, and nothing
  is open on a phone that is hidden on desktop (one DOM, one disclosure state for every width).

## 3. Not built in this phase, and why

| Brief item | Blocked by | Where |
|---|---|---|
| Currentness strip; Evidence Colophon lines (single Master, version, fingerprint, next review, copyable citation) | New governed interface copy | `ESCALATIONS.md`, V1 |
| Page-tools row replacing the header's Cite and Report; mobile sheet with hubs, numerals, domains, language | `navigation_interaction.json` (steward) | same |
| Hub numerals 01–05 in navigation, hub pages and breadcrumbs | A governed binding of numeral to hub (navigation contract) | same |
| First two sections open, the rest collapsed; phone-screen targets | `presentation_priority.json` and the renderer; DEBT-011 for `/data/` | same |
| Two-tone display headline | A renderer change that wraps the clause after a governed break (HTML changes) | same |
| "≠" between Home's figure cards | A governed glyph or label | same |
| Latin display serif; Arabic Bold 700 | Font rules (owner); the Arabic cold-page budget (A1) | same |
| Methodology dark rule cards; Explore green rail; Evidence directory facets and Compare tray | Markup and governed facet fields (EAD-07) | same |
| Home's named disclosures ("different moments", "rule to result", "gaps", "challenge") | No Orientation entry in `presentation_priority.json` (steward); a renderer-only tier would be a second contract | `ESCALATIONS.md`, V1 phase 2 |
| `/finance/` chronology as a disclosure | Its heading is `UI-CHRONOLOGY-H` itself; a summary needs a second governed label | same |
| A shorter source row on phones (description on demand) | A governed summary label for the row's detail | same |

## 4. Evidence

- Documents: 288 built, **0 HTML files differ** from `main` (`git status dist` lists only `assets/yfie.css` and the
  social images).
- Phone screens at 390 px (844 px viewport), before → after, Arabic: Home 10.8 → 10.9; CLM-001 8.0 → 7.8; /people/
  16.9 → 17.0; /data/ 77.8 → 75.1; /explore/ 11.8 → 11.9; /evidence/ 27.8 → 27.6; /methodology/ 21.6 → 21.1; the
  Reading "Same year, different number" 18.4 → 18.4; /about/ 6.4 → 6.1. English Home 10.3 → 10.7. A stylesheet pass
  cannot reach the brief's targets; they need the disclosure contract (§3).
- Weight: `yfie.css` 11.7 → 14.1 KB compressed; heaviest cold page (RC-PERF method) 272.6 KB English and 304.1 KB Arabic
  (`/data/`), budget 350 KB; no font added.
- Accessibility (`scripts/accessibility_audit.py --all`, record in `docs/ACCESSIBILITY_AUDIT.md`): 284 pages × 2
  widths; 0 axe rules violated; 0 contrast failures; 2.5.8: 0 targets meeting neither exception; 320 px reflow: 0
  routes overflow. No conformance is claimed.
- Gates: see `ESCALATIONS.md`, V1, and the pull request for the run on the final commit.

## 5. Phase 2 evidence (9 October 2026)

Conditions: Chromium 141.0.7390.37 (Playwright 1.56, `chromium-1194`), the built `dist/` served locally, self-hosted fonts
loaded (`document.fonts.ready`), JavaScript on, every disclosure in its default state; page height ÷ viewport height.
"main" is `7557866`, "P1" is phase 1 (`6f2b10d`), "now" is phase 2.

| Route | 390 × 844 main → P1 → now | 768 × 1024 main → P1 → now | 1440 × 900 main → P1 → now |
|---|---|---|---|
| `/ar/` | 10.8 → 10.9 → 10.5 | 6.4 → 6.4 → 6.1 | 6.5 → 6.6 → 6.6 |
| `/en/` | 10.3 → 10.7 → 10.3 | 5.9 → 6.0 → 5.8 | 6.3 → 6.5 → 6.5 |
| `/ar/people/` | 16.9 → 17.0 → 15.3 | 9.5 → 9.6 → 8.6 | 10.7 → 10.8 → 10.2 |
| `/en/people/` | 15.6 → 15.9 → 14.2 | 8.6 → 8.7 → 7.9 | 9.9 → 10.0 → 9.4 |
| `/ar/data/` | 77.8 → 73.5 → 57.2 | 50.9 → 47.8 → 39.4 | 65.6 → 62.0 → 44.5 |
| `/en/data/` | 72.5 → 71.1 → 55.6 | 45.5 → 44.3 → 36.5 | 59.6 → 58.3 → 42.0 |
| `/ar/payments/` | 30.9 → 31.0 → 19.9 | 18.1 → 18.0 → 11.5 | 20.9 → 20.8 → 13.5 |
| `/ar/firms/` | 20.5 → 20.4 → 16.7 | 11.4 → 11.4 → 9.7 | 13.5 → 13.6 → 11.6 |
| `/ar/finance/` | 31.9 → 31.9 → 31.0 | 17.2 → 17.1 → 16.5 | 25.9 → 25.8 → 25.7 |
| `/ar/evidence/CLM-001/` | 8.0 → 7.8 → 7.5 | 4.6 → 4.5 → 4.4 | 4.4 → 4.4 → 4.4 |

The brief's targets (Home ≤ 5, domains ≤ 6 before the disclosures, `/data/` ≤ 8 phone screens) are not reached and
cannot be inside the present contracts: Home has no disclosure tier, a domain's always-visible band and primary figure
are first-load by contract, and `/data/`'s register must stay open (DEBT-011). The proposals that would reach further
are in `ESCALATIONS.md`, "Raised at V1 phase 2".

