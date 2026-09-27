# Independent critique brief — YFIE D1 design propositions (T1–T4)

You are one independent critique lens on four competing design propositions for the Yemen Financial Inclusion
Evidence product (YFIE), a bilingual (English + Arabic, co-authoritative) public evidence service built by CauseWay. It
helps people understand, compare and verify evidence on financial inclusion in Yemen; it decides nothing for anyone.
Its central proposition: "Financial inclusion in Yemen is not one number" — the evidence runs on different clocks,
populations, methods and institutions, and the product's job is to keep those differences visible.

Every proposition renders exactly the same governed text (never shortened or rewritten) on three stress surfaces:
Home (`/`), the dense Evidence Record `/evidence/CLM-003/` (POS terminals: two totals 1,357 → 1,473, a derived 8.55 %
and the source's own displayed +11 %, with the discrepancy that must stay visible), and the flagship Reading
`/readings/same-year-different-number/` (two official reports give different 2024 remittance values; its signature
visual RV-CWR-001). Judge composition, hierarchy, typography, evidence behaviour, Arabic, mobile, accessibility, the
semantic firewall, misuse resistance and distinctiveness — not the words.

## What must hold (report any breach as a material defect)

- Semantic firewall: people ≠ accounts; access ≠ use; infrastructure ≠ outcome; target ≠ result; licence ≠ operation;
  observed ≠ estimated ≠ projected; missing ≠ zero; chronology ≠ causality; a same-year restatement ≠ a fall;
  two indexed paths coinciding ≠ independent confirmation. Layout must protect these, never blur them.
- RV-CWR-001 (the Reading's figure): panel 1 = two values for reference year 2024 keyed by publication (CBY-Aden Annual
  Report 2024: 6,245; Annual Report 2025: 3,422.16 USD million), no joining line, value axis from zero; panel 2 = two
  side-by-side indexed lanes (2021 = 100; both read 100 → 105.74 → 111.73 → 118.0), one per source, never on one axis;
  the "not directly comparable" divider, the in-frame note, the boundary ("does not establish"), the credit and the
  canonical link must travel with the figure; a text/table alternative must exist.
- No red/amber/green; colour is never the sole carrier of a state; nothing essential may live only in hover.
- No number outside its bounded context; the withheld value of record CLM-044 is never rendered; sources without a
  public locator are never named.
- Logo unaltered; IBM Plex Sans / Plex Sans Arabic only.

## The four propositions (what each claims)

- **T1 · Register** — the evidence record as a manuscript page: a start-side margin column carries each statement's
  clock, population and state as marginalia; high controlled density; the apparatus is the typographic skeleton.
- **T2 · Argument** — reading-first: one measured text column, the proposition leads, evidence discloses in place;
  minimal chrome; calm.
- **T3 · Strata** — the evidence system made spatial: ordered labelled strata (answer → scope → boundary → source)
  with a persistent trail/index; built-form grounding (bands).
- **T4 · Instrument** (second generation) — one mental model: an instrument that answers the reader's questions and
  states what it cannot answer. Clock-first evidence objects (WHEN and FOR WHOM before the claim; numbers never typeset
  outside their object or sentence); the seven governed questions of a record are its structure and its index (same
  order everywhere); the boundary is a second voice (double rule, label, weight, teal); a verification spine on every
  page; the firewall is structural (unlike things never share an axis, row or colour); mobile-first, Arabic composed
  first; panel 1 of RV-CWR-001 as rows on a horizontal zero-based axis so two same-year values cannot stack as a fall.

T4 is a candidate, not the answer; it must not be protected. If a first-generation proposition is stronger for your
lens, say so.

## Where the renders are (all paths under `/home/user/Financial-inclusion-/design/exploration/d1_canvas/out/`)

- `fold/<T>-<surface>-<lang>-<d|m>.png` — first screen at 1440×900 (d) or 390×844 (m); `…-m-2.png` the second
  mobile screen. Start here.
- `tiles/<T>-<surface>-<lang>-<d|m>-<i>.png` — the full page cut into 1,400 px tiles, in order. Read these for the
  whole page; full-page images are too tall to read directly.
- `crops/<T>-record-<lang>-primary.png` — the Record's primary evidence area cropped as a reader would screenshot it;
  `crops/<T>-reading-<lang>-figure.png` — the Reading's figure cropped alone (screenshot-misuse test material).
- `inspect/T4-<surface>-<lang>-fluid@<w>.png` — T4 first screens at 320, 360, 390, 430, 768, 1024, 1280, 1440
  (`…x2` = high-DPI); `inspect/crops/T4-reading-<lang>-figure@<w>.png` — the T4 figure at 1440, 390 and 320.
- Surfaces: `home`, `record`, `reading`; languages `en`, `ar`; T = T1, T2, T3, T4.

Look at both languages and both sizes for every proposition before judging. Cite the file you saw for every finding.

## Report format (write it to the file named in your instructions AND return it in full; ≤ 1,000 words)

1. **Per proposition (T1, T2, T3, T4):** what it establishes for your lens (strengths, with evidence); material
   defects (MUST-FIX vs SHOULD-FIX); the misreading a cold reader could make from a screenshot or a first screen.
2. **Ranking for your lens** with reasons — no numeric scores, no averaging.
3. **The convergence question:** what does T4 allow a user to understand or do that the strongest first-generation
   proposition does not make nearly as easy? Answer honestly; "nothing material" is a valid answer.
4. **Three specific improvements** to the proposition you rank first.
5. **ESCALATION CANDIDATES:** anything that looks like a governed-content defect (wrong number, missing bound,
   contradictory label) rather than a design defect — list separately; do not propose rewording.

Be concrete, adversarial and brief. Do not praise. Do not invent facts you did not see in a render.
