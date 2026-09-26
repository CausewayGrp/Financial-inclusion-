# Session P2 — Tools, discovery and accessibility baseline: closure

Programme: Pre-Tranche-C maturation (P1–P4). Status of this session: **P2 CLOSED**. Tranche C has not been started. This is
not DESIGN HANDOFF READY and not PUBLIC RELEASE READY. No WCAG conformance is claimed.

Scope was the behaviour of the static baseline's public tools, in both languages. No React was built. The one Master change
(governed search aliases) went Master-first through the transactional runner; the tool changes are interface code whose
output was regenerated, rebuilt, audited and validated by the same runner. Findings with severity, consequences and the
Lead's decision are rows P2-F01…F11 in `audit/pre_tranche_c/FINDINGS_LEDGER.csv` (P1-O01, routed here from P1, is closed).

## 1. State at P2 exit

| Item | P1 exit | P2 exit |
|---|---|---|
| Production Master SHA-256 | `e1f62310…602d9` | `6456add9e419bf2ce9a1e8b72715eb7e0d3a2d9d157deea2dbdbcdee46247672` |
| Page Specs SHA-256 | `314a5b41…1e541e` | `966186933c3018d43de1572546793b1c34b0f79fe04cb971a464045dd4d21834` |
| Build | 288 HTML from 143 specs | 288 HTML from 143 specs |
| Generator `--check` / unit tests | PASS / 16 of 16 | PASS / 16 of 16 |
| Public-literal audit (v2) | 8,230 records, 0 unresolved | 8,230 records, 0 unresolved |
| Validator | PASS | PASS (new gates P2-G01 search probe, P2-G02 tool contracts, P2-G03 accessibility baseline) |
| Browser behaviour tests | none | **26 of 26 PASS** (`scripts/tests/test_public_tools.py`, headless Chromium) |
| Governed search aliases | 17 | 24 |

Transactions: P2-A `6456add9…` (aliases SEARCH-ALIAS-018…024, Master 04) → P2-B, P2-C, P2-D (same Master; interface and
contract changes regenerated, rebuilt and validated; reports in `audit/pre_tranche_c/runs/P2*_RUN_REPORT.json`).

## 2. P2.1 — Compare: shareable URL state

**Defect (P2-F01).** The comparison lived only in the form. Reload, a copied link or a language switch lost it.

**Contract now.** `?records=ID,ID[,ID[,ID]]`, in slot order. Each ID is percent-encoded on its own and commas are literal,
so identifiers containing `+` survive the round trip. The URL always reflects the comparison that is drawn
(`history.replaceState`), so what a reader copies is what they see. A "Copy link to this comparison" /
«انسخ رابط هذه المقارنة» control is on the page. The language switch carries the query.

| Input | Behaviour |
|---|---|
| 2–4 known IDs | Restored into slots in order and drawn |
| 1 or more than 4 IDs | Technical input error (`[data-compare-url-error]`, `role=alert`); no verdict is shown |
| Malformed list (empty items, illegal characters) | Technical input error; no verdict |
| Unknown ID | Technical input error naming the ID; no verdict |
| The same ID twice | Drawn and visibly invalid: `same-record` verdict ("The same evidence record was selected more than once…") |
| Reader then chooses records | The error clears and the URL is rewritten |

Eleven browser tests hold this contract, including the `+` codec and table semantics. A wrong link is always presented as a
problem with the link, never as a finding about the evidence.

## 3. P2.2 — Search: weak intents and the canonical probe

Only intents that graded WEAK were worked on. No ranking weight was changed and no synonym was asserted. Aliases are
discovery aids that route a topic query to the page that explains the topic (PB-0492). The complaints alias carries a
boundary note: the governed rules describe a path and time limits, not how complaints are handled in practice.

| Probe (same browser-scoring mirror, before → after) | Before | After |
|---|---|---|
| Legacy Tranche B 28-term probe (expected = explanatory pages only) | 43 PASS / 13 WEAK | 54 PASS / 2 WEAK |
| Canonical 30-intent probe `scripts/search_canonical_probe.json` | 55 PASS / 5 WEAK | **60 PASS / 0 WEAK / 0 FAIL** |

Rank movement from the aliases: deposits EN 8→1, AR 4→1; SME finance EN 10→1; RTGS EN 4→1, AR 9→2. Consumer protection,
complaints and FMIIP moved their explanatory page into the top three in the legacy probe (EN/AR 7, 5 and 9 → ≤3).

The canonical probe names, for every intent, the destinations that answer it and why. The two remaining legacy WEAK are
Arabic «التحويل النقدي» and «نقاط الوصول». In both, an Evidence Record that carries the answer (CLM-045; XW-FMIIP-005)
ranks first, and the canonical probe lists that record as a correct destination with its rationale. The page was not forced
above the record.

Reproduce with `python3 audit/pre_tranche_c/search_probe_run.py <before_content_dir>`. The result is in
`audit/pre_tranche_c/runs/SEARCH_CANONICAL_PROBE_BEFORE_AFTER.json`. The validator (P2-G01) re-runs the probe through its
own independent mirror of `app.js` scoring and fails on any FAIL, or on any WEAK that lacks a recorded reason.

A related defect was fixed (P2-F03): all ten Measurement search results pointed to the top of `/measurement/`. They now open
the priority's anchor (`/measurement/#MA-00x`). The validator checks that every anchor exists in both languages.

## 4. P2.3 — Tool contract sweep (both languages)

Legend:
- **Complete now** means the behaviour is implemented in the static baseline and exercised by a browser test or a validator
  gate.
- **Design/React requirement** means work that Design or implementation must carry. It is not a gap in truth, and none of it
  is required for the evidence to be read correctly.

| Tool | Complete now | Design/React implementation requirement |
|---|---|---|
| **Search** | Header dialog (button, Ctrl/⌘ K). Focus goes into the input and returns to the opener; Escape closes. Inline search on `/evidence/`. Arabic normalisation (hamza/alef forms, diacritics). 24 governed aliases. Results are labelled by type. No-match copy states that no match ≠ no evidence (P2-F05). An index load failure is a technical state, announced. Measurement results deep-link to anchors. | Group results by object type (question, domain answer, Evidence Record, Reading, Measurement priority, source). Query in the URL (`?q=`) for shareable searches. Arrow-key movement within results. Term highlighting. Any change to scoring must keep `validate.py _r4search` equivalent, or the probe must be re-run. |
| **Evidence discovery** | The `/evidence/` directory lists governed records, each with a labelled Reference (PID-1), plus inline search. Every Evidence Record opens with what it establishes and its boundary first. It shows the source path, Cite and Report issue. | Filters by domain, evidence state and period. The family grouping shown visually. An entry from a record into Compare (P2-F11). |
| **Compare** | See §2. The comparison table has a caption and scoped headers, and every row state has a text label. | A mobile layout for the four-column table. A selection basket. Print. |
| **Data / source filtering** | Text filter across reference, title, publisher and URL. No-match copy. `?source=` opens and focuses the card. An unknown reference is an announced technical error and every source stays visible (P2-F04). Each card shows its reuse-terms state, and the directory states the reuse boundary once (P1-O01 closed). No download is offered while reuse terms are unassessed. | A category filter (laws, CBY decisions, surveys, datasets), with filter state in the URL. **Blocked on metadata, not code:** 133 of 159 sources are LOCATOR_ONLY, with no governed title, issuer or document type. A type filter would have to invent them. Bibliographic promotion must be Master-first (P2-F10, deferred to corpus work). |
| **Cite** | Record Cite copies the governed citation (`yfie-citation`) plus the record's canonical link, in EN and AR. Source Cite copies title · reference · locator; locator-only sources get reference · locator, and the reference is never repeated as a title (P2-F07). The copy is announced in the status region; if the clipboard is refused, a prompt fallback appears. | The page-level "Cite this page" icon uses ↗, which reads as an external link, so Design should give it a cite glyph. Add further citation formats only if they are governed. |
| **Language switch** | Keeps route, query and hash. The label is in the target language, with `lang`/`dir`. The preference is stored locally, as disclosed on Privacy. | — |
| **Corrections / report issue** | Report issue on every Evidence Record → `/contact/?record=ID`. Contact and Corrections keep the originating record, validated against the published set. Malformed or unknown references are technical errors (P2-F06). For a known record, Contact offers a mail action to the governed address with the reference in the subject, as the governed copy instructs. Governed addresses are links. No synthetic correction history is shown. | Publish correction events once any are governed. A form only if a backend and privacy terms exist. |
| **Deep links** | Evidence Records; Readings; `/measurement/#MA-00x`; `/data/?source=…#source-…`; `/evidence/compare/?records=…`; `/contact/?record=…`; `/corrections/?record=…`. All survive a language switch. | If Design restructures a page, keep these anchors or publish a redirect map. No route change is planned. |
| **Technical-error states** | Compare URL errors; unknown source link; malformed or unknown record reference; search index failure; bilingual 404 with search. Each is worded as a link or loading problem, not as information about the evidence. | Offline or partial-load states and error-boundary copy in the implementation, governed in both languages. |

## 5. P2.4 — Accessibility baseline (no conformance claim)

What is checked now:
- **Keyboard.** The skip link is first in tab order and moves focus into `<main>` (tested, AR). The mobile menu reflects
  `aria-expanded`; Escape closes it and returns focus (tested). The search dialog is keyboard-operable with focus in and
  focus return (tested). No positive `tabindex` (gate).
- **Dialog semantics.** Every `<dialog>` has an accessible name (gate).
- **Tables.** Every table has a caption, and every header cell has a scope (gate for built pages). The runtime Compare table
  is tested in the browser. The static pages carry no other data tables.
- **No colour-only meaning.** Every Compare state carries a text label (tested). The static baseline draws no chart
  graphics: every visual contract renders as a text-first summary and fallback list.
- **Names and announcements.**
  - Every image has alt text, every form control has a name, and icon-only buttons have `aria-label` (gates).
  - Technical errors use `role=alert` and search results use `aria-live=polite`; copy confirmations use `role=status`
    (tested).
  - 696 section headers that printed the same label twice (eyebrow and heading, so screen readers announced it twice) now
    print it once (P2-F08, gate).
  - English pages carry no Arabic placeholder (P2-F09, gate).
- **Landmarks.** Every content page has a skip link and a `main` target. The 404 page has its `main` landmark but no
  repeated navigation to bypass. The root file is a language redirect with no content.

What was not done: no screen-reader session, no contrast audit, no zoom or reflow test and no assessment by users with
disabilities. These belong to the implemented design. The public Accessibility statement already says conformance will not
be claimed before those tests.

**Rule carried to P3 and Design.** Every future chart must carry an analytical text alternative, plus a visible table or
ordered-text fallback. These must say what the chart shows and what it does not establish, not only describe its shape.
Meaning must never depend on colour, hover or a pointer.

## 6. Duplication re-check (P1-O01)

Re-scanned after P2 (sentences of six or more words; same method as P1):
- **Domain pages:** 0 exact repeats in English and at most 1 in Arabic.
- **`/data/`:** the rights sentence that was repeated on every card is gone. The remaining exact repeats are:
  - per-card labels ("Evidence records using this source", "Reuse terms: not assessed");
  - collapsed reverse-index link titles (for example, the twelve enforcement-decision sources all point to one record).

  These are navigation, not prose, and are expected in a directory.

## 7. What P2 changed, by file

- **Master 04 (via P2-A).** Aliases SEARCH-ALIAS-018…024.
- **`site-src/app.js`.**
  - Compare URL state and copy.
  - Search empty text.
  - Source deep-link error.
  - Record-context validation and the mail action.
- **`scripts/build.py`.**
  - Compare share control.
  - Compact per-card reuse state and a single directory note.
  - Record context on Contact.
  - Governed-address links and the mail action.
  - Citation payload for locator-only sources.
  - Duplicate eyebrows removed.
  - Localised source-filter placeholder and label.
- **`scripts/projection/…`.** Measurement anchor route template; the generator formats it.
- **`scripts/validate.py`.** Gates P2-G01, P2-G02 and P2-G03.
- **New files.**
  - `scripts/search_canonical_probe.json` (30 intents, with expected destinations and rationale).
  - `scripts/tests/test_public_tools.py` (26 browser tests).
  - `audit/pre_tranche_c/search_probe_run.py`.

## 8. Carried forward

- **P2-F10.** Source bibliographic promotion. This is corpus work and must be Master-first with a primary read. It blocks
  only a type filter on `/data/`.
- **P2-F11.** A Compare entry from a record. This is a Design/React requirement.
- **The Design/React column of §4.** It goes into the P4 handoff alignment as implementation requirements, not as open
  truth defects.

Next session: **P3 — visual design readiness** (tier the 36 visual contracts, semantic visual grammar, data contracts for
signature and core visuals).
