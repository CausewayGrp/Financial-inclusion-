# Evidence, Compare, Data & sources, About and Trust — closure

> **Execution-state correction (Tranche B execution, 2026-09-26).** About keeps «عن الموقع» (correction G); the Trust group renders as a trust navigation bar above the header and as the footer group.


**Status:** `VERIFIED_BY_CLAUDE_TEAM` · `SPEC_PENDING_EXECUTION` · `INDEPENDENT_OPENAI_ACCEPTANCE_REQUIRED`

The product's promise is VERIFY. These surfaces are where that promise is kept or broken. The most serious Tranche B defect sat here: the verification layer rendered route-level source unions as if they were object lineage (LEAD-B07).

## 1. Evidence records — readability and verification

| Issue | Evidence | Decision | Patches |
|---|---|---|---|
| **Source trace is a route union, not the record's lineage** | 4 contaminations verified (e.g. CLM-008 showed 13 enforcement decisions); closure stamped on 108/108 with 87 unresolved | Object-level binding. The trace renders only bound sources, or "composite", or "not yet bound". | PB-0001–0006, PB-0010–0069 |
| **"How can I verify it?"** is producer boilerplate on 107/108 records ("…rather than inferring or inventing it") (F-03 / LEAD-M06) | build.py label; Master `verification_*` identical on 107 | A per-record path generated from `lineage_state` and bound sources, using three governed templates. The "inventing" clause is removed. | PB-0007/0007A/0008 |
| `limitations` pipe-merges "what the measure cannot capture" with "what you must not conclude" (F-04) | projection pipes | Split into `measurement_limitation_*` and `prohibited_inference_*`; clauses are moved, not rewritten | PB-0374 |
| Visual records publish drawing instructions as summaries, and English universes are placeholders | 13 records | Reader prose; real universes; titles carry their year | PB-0500–0512, 0560–0574 |
| The source intro line reads «افتح سجل المصدر داخل المنظومة…» on 108 pages | build.py:664 | «افتح سجل المصدر هنا، أو انتقل إلى الرابط الأصلي حين تسمح حالة النشر بذلك.» | PB-0414.B01 |

**Reader test (journalist on deadline).**
- **After execution:** the journalist opens CLM-008 and sees one bound source, the CBY-Aden 2026 bank list, with its link. The boundary reads "listing, not operation, … beyond the scope of the issuing authority" in both languages. They can quote it safely.
- **Before:** they saw 13 enforcement decisions under a claim about banks.

## 2. Compare — compatibility first

| Issue | Decision | Patches |
|---|---|---|
| F-01: the Arabic lists fewer compatibility dimensions than the English | Arabic brought to the same seven: definition, period, population or base, geography, unit, method, evidence type | PB-0370 |
| F-02: "incompatible" is not stated as a valid result | Both languages: "when definitions or populations do not match, 'not comparable' is a valid result" | PB-0370/0371 |
| LEAD-M10: 11.9%, about 3.3 million and 1.44 million sit on different pages, and nothing tells the reader they cannot be combined | New section "Three numbers that cannot be combined" / «ثلاثة أرقام لا يصح الجمع بينها». No population denominator is applied (directive correction D). | PB-0345 |
| Two same-concept sources disagree (wallet counts 7 → 9 → 8) | Already handled well (CLM-010 SOURCE_DISAGREEMENT). **KEEP.** | — |

## 3. Data & sources (`/data/`)

| Issue | Decision | Patches |
|---|---|---|
| Header "Data" and footer "Data & sources" contradict each other | "Data & sources / البيانات والمصادر" everywhere; route unchanged | PB-0421 |
| Four rights promises no field can keep ("Rights travel with the data" and others) | Rewritten to what is true now: terms are assessed for some sources, publisher terms apply otherwise, and inclusion does not mean CauseWay endorses a source. A rights schema is added. | PB-0380–0390 |
| 133 source records have no publisher | Proposals from source-ID family and URL host (104 proposed, 29 unresolved), to be confirmed at execution. `LOCATOR_ONLY` records are surfaced only after this. | PB-0390; `SOURCE_PUBLISHER_PROPOSALS.csv` |
| F-05: the claims count is missing from "What is currently available" | `{N_CLAIMS}` generated from 07 (currently 59; 60 after CLM-061) | PB-0372/0373 |
| F-07: the macro-financial chronology appears on /data/ (s9) and again in /finance/ (s7, s11) | **KEEP both, with distinct roles.** /data/ holds the chronology as a browsable resource. /finance/ keeps one contextual paragraph (s7) and a short introduction to the dated events (s11), with the leaked instruction removed. No further deletion: the /finance/ reader needs the context in place, and removing it fails the deletion test. | PB-0150/0151 |
| Resource Library taxonomy | One governed register with several facets. Document type is kept distinct from evidence role (Tranche A A3, accepted). Search facet as in SEARCH R10. | PB-0493(b) |

## 4. Methodology

The completeness test against the addendum is in `METHODOLOGY_COMPLETENESS_CLOSURE.md`. In summary: the method is sound and short. Four additions are specified there; nothing is rewritten for style.

## 5. About and CauseWay positioning

- **No CauseWay over-claim was found** (Trust specialist; re-checked). /about/ says CauseWay adds structure and synthesis, not a national statistic or a substitute for source institutions.
- **About moves to the Trust group**, which is visible in a trust navigation bar above the header and in the footer. It is not buried (PB-0423). It leaves the footer group `method_measure`.
- **The strapline is governed in the Master (PB-0412):**
  - EN: "Developed and maintained by CauseWay. A public resource linking each claim to its evidence and original source."
  - AR: «طوّرتها وتديرها CauseWay. مورد عام يربط كل خلاصة بدليلها ومصدرها الأصلي.»
- **The Arabic /about/ label.** Acceptance correction G: the label stays **«عن الموقع»**. PB-0425 is SUPERSEDED; PB-0423's Trust group carries «عن الموقع» first.

## 6. Trust surfaces

| Surface | State | Decision |
|---|---|---|
| Meta description | Renders `primary_user_question_internal` (English) on 282 pages, including all Arabic pages (LEAD-B04) | Governed per-language `meta_description_*`; `*_internal` never renders (PB-0410/0411) |
| Corrections | Honest: no release history is invented | Self-referent only (PB-0414.B02) |
| Accessibility claim | `true` on 141/141 with no rendered visual (LEAD-M07) | `PENDING_DESIGN_IMPLEMENTATION` plus the table contract (PB-0400) |
| Privacy | Honest about unverified deployment facts; "the product stores a language preference" | Self-referent only (PB-0415). The subtitle was judged adequate. |
| Footer strapline | Ungoverned, «الادعاء» | Governed (PB-0412) |

## 7. F-01…F-09 disposition

| F | Disposition |
|---|---|
| F-01 | PB-0370 |
| F-02 | PB-0370/0371 |
| F-03 | PB-0007/0008 |
| F-04 | PB-0374 |
| F-05 | PB-0372/0373 |
| F-06 | **Not re-located this window.** Queued (`TRANCHE_B_UNRESOLVED_QUEUE.md` U-06). |
| F-07 | KEEP both, with distinct roles (§3) |
| F-08 | Editorial, absorbed by the sweeps |
| F-09 | Editorial, absorbed by the sweeps |
