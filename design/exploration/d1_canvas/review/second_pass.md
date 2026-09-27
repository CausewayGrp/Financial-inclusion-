# D1 second independent pass — closure of the final review (repository-only)

Reviewed `claude/practical-cray-sr26c5` at `455d4f7` (tree clean; Master `17db032b…`, Page Specs `d4574804…`). Run: build 6 documents; `check_content --text` PASS; `check_trio --shots --degraded --evidence` 24/24 renders, 12/12 smoke tests, 6/6 degraded; `tokens --check` CURRENT; bilingual invariance 0 of 3; `validate.py` PASS; checksums and manifest current. Own probes: Chromium 141 at seven widths 320–1440 px, forced colours light/dark, A4 print, run-level text diff of every `<main>` against `dist/`.

## 1. Item by item

**MUST-FIX**

1. Home visual — CLOSED. render.py:244 calls `figure()`; visuals.py:167–183 frames boundary, scope, credit, link. Probe: `prohibited_inference`, period, universe, alt text and their labels sit inside `figure[data-visual-id=VIS-INCLUSION-TRANSMISSION]` at 390 and 1440, EN and AR; `.foot .b` visible; boundary label "What not to conclude" matches dist.
2. One spine — CLOSED. render.py:151–158, theme.py:117–118, 253, 258. Probe: exactly one `aside.spine` visible at every width; below 900 the foot spine carries the index (Home 8 items, Reading 9); the Record's foot spine has none and its strip is visible; ≥900 the side spine only.
3. 320 px tables — CLOSED. theme.py:165 has no `overflow-wrap`; `.table-wrap` (client 256 px) scrolls, page overflow 0; row headers break at spaces and the hyphen of "CBY-Aden" (5 lines for 4 words), Arabic 7 lines for 8 words — words intact (alt-320 screenshots).
4. STATUS and stub — CLOSED. 01_FOUNDATIONS.md:3–7; the only "not yet written" left is the account of it at :720.
5. 09_CODE_HANDOFF — CLOSED. :5 marks D0 as history; :25–26, :31–32 describe the built state; :49–52 replace "nothing implemented".
6. Tokens — CLOSED. 02_TOKENS.json valid JSON, key fixed (:57); tokens.py generates it from theme.py (:53–87) and `--check` is current.
7. Evidence — CLOSED with one residual. check_trio.py:153–192 writes `_review/degraded/` (24 files) and the evidence set; `design/evidence/d1/` holds 18 PNG, byte-identical to a fresh regeneration; `review/` holds lens_A–I plus final_review.md. Residual: 01_FOUNDATIONS.md:423 still says the reports are "kept at `…/out/review/`" (ignored) — contradicts §6:725–726 and d1_canvas/README.md:31.
8. Forced colours — CLOSED. theme.py:212; probe: `.lbl`/`.val` fill = CanvasText (black on white, white on black), marks and paths stroke CanvasText; forced-dark screenshot legible.

**SHOULD-FIX**

1. Print of `details.more` — CLOSED. theme.py:221–222; print probe: 4/4 paragraphs and h3s visible, summary hidden, Chromium 141 (`::details-content`, recorded as Chromium-only, DL-D1-008).
2. Keyboard path and text parity — CLOSED. check_trio.py:128–147; check_content.py:105–127.
3. F6 attributes — CLOSED. visuals.py:89 (`FIG_ATTRS`), render.py:194 (`data-boundary-part`); counts match dist's single record occurrence.
4. Axes from data — CLOSED but regressive: visuals.py:82–86, 105–106, 124–125; ticks are now 0 / 1,750 / 3,500 / 5,250 (`vmax/4`), where the hard-coded axis read 2,000 / 4,000 / 6,000 (panels-1440 screenshot).
5. Four unrendered strings — CLOSED. render.py:238, 240, 216; each present once in the built pages. Home reorder recorded for the steward, ESCALATIONS.md:38–42.
6. COVERAGE.csv / DEBT-003 — PARTLY. 8 grammar rows VERIFIED (:1199–1232), 32 re-gated D2 with a note; DEBT-003 CLOSED (DESIGN_DEBT.md:10). But the eight VERIFIED rows now carry a corrupt note field, `' drawn per contract D6"'` (fragment and stray quote left by the edit; the 1c0846d rows were clean).
7. PNGs — CLOSED (item 7 above).
8. `.nav` without JS / 24 px targets — PARTLY. No-JS collapse accepted and recorded (09_CODE_HANDOFF.md:50–52). theme.py:92 fixes `.actions`, `.open`, `.src .acts` only: at 390 px the figure-foot "Cite this page" button is 18.9 px, Home's "Open evidence record →" 18 px, "View all 11 questions", "All Evidence Readings" and the trace source links 19 px.
9. Notes — acknowledged in §6:739–743.

## 2. New defects and untrue statements

- COVERAGE.csv:1199–1232 corrupt `note` field, and the 1,750-step ticks (above).
- visuals.py:182 prints the governed label "Source:" followed by nothing on the Home figure, both languages (credit is `None`); dist prints no source line there — an empty public label on the flagship page.
- DEBT-010, §2.5:376, §3.4:511, §4.4:662 say the tables are "50–80 px wider than their wrapper": measured 80 and 48 px (EN), 23 and 73 px (AR). The re-measurement demanded by MUST-FIX 3 is wrong again.
- §4.4:666 "all verified by the same checks": no committed check covers forced colours (check_trio has no forced-colours context) or hit areas; both were verifiable only by hand.
- §6:727 names `.unit`, which matches no element, and credits "the captions" to the rule; captions survive by the UA's forced-colours override, not theme.py:212.
- README.md:20 attributes text parity, keyboard and degraded checks to DL-D1-007; they belong to DL-D1-008. 00_DESIGN_README.md:32 still names the check commands without `--text`/`--degraded`.
- §4.4:672 "`check_content.py --text` now proves text-block parity": the rule (check_content.py:105–122) is one-directional and bundle-scoped — only bundle strings of ≥12 characters that the baseline prints verbatim are checked; baseline text outside the bundle, short labels and template-composed runs are invisible. My run-level diff found no governed sentence lost (CLM-003: 0 of 73 baseline runs missing; Home and the Reading lose only composed "label: value" runs and the baseline's template arrow), so the property holds, but the tool is a proxy, not a proof.
- Print at A4 width hides both spines (theme.py:117, 218): the rule at :217 is dead; spine edges never print. Not claimed.
- Observation: the Reading's foot index sits at 11.6 k of 13.2 k px at 390 px — reached only after the content.

## 3. Cold-developer test

From the repository alone a senior developer can tell what is authoritative (README.md:9–23, AGENTS.md), what is accepted (D0 at `8bf19ef`; README.md:20, 00_DESIGN_README.md:3–13), what is provisional and why (01_FOUNDATIONS.md status line, §4.2, §4.4 residuals, DEBT-006…010), what was rejected (§3.2, DL-D1-006), what is implemented and by whom (09_CODE_HANDOFF.md D1 table, ESCALATIONS.md, DESIGN_DEBT.md), how to build and test (README.md:20; 00_DESIGN_README.md:29–36), what must not be reinterpreted (§4.1, §4.3, 09_CODE_HANDOFF.md:39–45) and what happens next (hand-back on PR #3, owner merge, four escalations). Two things mislead: §3.1:423 points to an ignored path for the lens reports, and §4.4's "verified by the same checks" promises tool coverage that forced colours and hit areas lack.

## 4. Verdict: D1 DESIGN COMPLETE — OWNER MERGE REQUIRED

All eight MUST-FIX items are closed in code and records and reproduce from the committed tools; the six pages carry every governed sentence the baseline prints, numeric and bilingual invariance hold, the Lock items the first review found broken (frame, one spine, readable tables) now hold at every width, and the PNG evidence is byte-identical to the code. What remains is small and Design-owned — a corrupt CSV note, an empty "Source:" label on Home, non-round ticks, a second wrong table measurement, a stale path and three overstated sentences — none breaches the firewall, governed text or a Lock item, and each belongs in the hand-back commit on the pull request before the owner merges. "READY FOR D2" would be the wrong form: the repository's rules put gate exit in the owner's merge, four escalations await the steward, and README.md:20 itself says D2 does not start before that decision.
