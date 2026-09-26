# Claude Tranche B — closure

> **Execution-state correction (Tranche B execution, 2026-09-26).** Acceptance correction H: the Method & Measurement contract in §4 is reduced to semantic requirements (no route change; equal prominence; both destinations discoverable on desktop and mobile; keyboard accessible; no hover-only meaning; RTL; clear active state). The executed build renders the family with both links always visible; the final interaction treatment is left to Claude Design. Execution results: audit/TRANCHE_B_EXECUTION_CLOSURE.md.


**Status:** `TRANCHE B COMPLETE — READY FOR INDEPENDENT REVIEW`

This is not DESIGN HANDOFF READY and not PUBLIC RELEASE READY. Tranche C has not been started.

**Date:** 2026-09-25. **Lead:** Claude Team Lead, the only adjudicator. Specialist and subagent output was treated as analyst input, never as approval.

> The Master→projection generation pipeline is absent from the handed repository and must be recovered or deterministically rebuilt before semantic patch execution.

---

## 1. Authority and repository state (resume protocol, re-run at close)

| Check | Result |
|---|---|
| Production Master `authority/Yemen_Financial_Inclusion_Evidence_Master.xlsx` | `e69804106e04d093098688f2d01cea51e13191f255d774a090f3e5dd8dec9bc7` — **unchanged** |
| Page Specs `site-src/content/page_specs.json` | `ff2b0f559cde5fede3fe31d7dfb2539a00921e8b00b816c2863790cd9de49007` — **unchanged** |
| `python3 scripts/build.py` | 284 HTML files from 141 page specs |
| `python3 scripts/audit_public_literals.py` | 7,309 records, 0 unresolved |
| `python3 scripts/validate.py` | `WEBSITE REPOSITORY VALIDATION PASS` — HTML=284, ERRORS=0, WARN=0 |
| `sha256sum -c SHA256SUMS.txt` | 58/58 OK (no audit file added to the manifest) |

**Semantic edits installed in Tranche B: none.** Everything semantic is a specification. The only executed changes in the programme are still Tranche A's CHG-0001…0006 (a projection re-bind to the already-current Master).

**Supersession note.** Early in this window, before the repository ZIP was uploaded, a file named `audit/CLAUDE_S00_AUTHORITY_AND_ACTIVE_SURFACE.md` was delivered in chat recording "repository absent". That record is **superseded** by the uploaded repository. The repository's own Tranche A S00 file was not overwritten.

## 2. What Tranche B produced

| Artifact | Role |
|---|---|
| `audit/MASTER_FIRST_PATCH_SPEC.csv` | **Core deliverable.** 994 rows, 394 patch roots, 22 required columns. Every semantic row has its before/after. |
| `audit/MASTER_FIRST_PATCH_NARRATIVE.md` | Explains the grouped changes that the CSV alone does not make safe. |
| `audit/TERMINOLOGY_SWEEP_KEEP_REGISTER.csv` | Every «ادعاء», «منظومة» and "the system/product" occurrence that is kept, each with its rule. This closes the sweep counts. |
| `audit/SOURCE_PUBLISHER_PROPOSALS.csv` | Publisher proposals for the 133 source records with a null publisher: 104 proposed, 29 unresolved. |
| `audit/tranche_b_patch_tooling/` | Reproducible tooling: export the Master, rebuild the spec byte-identically, simulate the application. |
| `BILINGUAL_EDITORIAL_CLOSURE.md` · `ARABIC_TERMINOLOGY_AND_STYLE_LEDGER.md` · `ENGLISH_EDITORIAL_CLOSURE.md` | Language maturation and semantic invariance. |
| `READINGS_MEASUREMENT_CLOSURE.md` · `VISUAL_CONTRACT_CLOSURE.md` · `SEARCH_DISCOVERY_CLOSURE.md` · `EVIDENCE_COMPARE_TRUST_CLOSURE.md` | Surface closures. |
| `TRANCHE_B_RED_TEAM.md` · `TRANCHE_B_UNRESOLVED_QUEUE.md` | Challenge record and the short unresolved queue. |
| Addendum: `ECONOMIC_SYSTEM_AND_EVIDENCE_REVIEW.md` · `INDICATOR_COVERAGE_MATRIX.csv` · `METHODOLOGY_COMPLETENESS_CLOSURE.md` · `BENCHMARK_AND_COMPARATOR_POLICY.md` · `SOURCE_NARRATIVE_EXTRACTION.md` · `ECONOMIC_CONTEXT_USAGE_POLICY.md` · `SIGNATURE_VISUAL_CANDIDATES.md` | Completeness tests. Each proposal was classified ADEQUATE / PARTIAL / MATERIAL GAP / NO MATERIAL VALUE. |
| `OPENAI_REENTRY_CHECKPOINT.md` (repository root) | Re-entry state for the independent reviewer. |

## 3. Lead adjudication — final dispositions

"BLOCKER", "MATERIAL" and so on are severities. They are not claims of execution, and every row remains `SPEC_PENDING_EXECUTION`.

### 3.1 Reconciliation with Tranche A — the "no BLOCKER" statement is overturned

Tranche A §5 and `DOMAIN_CORPUS_EDITORIAL_CLOSURE.md` said there was "no BLOCKER misstatement and no false public number". That statement is **overturned**. The Tranche A records are kept as lineage and annotated here, not deleted. Tranche B's byte-level audit of `dist/` found the following:
- unconfirmed OECD/INFE Yemen scores published as fact (LEAD-B08);
- an evidence-state upgrade to "observed history" and a splice of two IMF vintages (LEAD-B06);
- a verification layer that renders route-level source unions as object lineage (LEAD-B07);
- leaked authoring instructions on /finance/, /measurement/ and 13 evidence records (LEAD-B02 and this window);
- the meta description exposing an `*_internal` field in English on Arabic pages (LEAD-B04).

Three Tranche A analytical statements are also withdrawn:
- "access to finance ranks 6th (22%)" — LEAD-M12. It never reached public copy.
- "Yemen's largest physical cash-access channel" — binding correction #4.
- "the same absence of a functioning formal credit/deposit channel" — binding correction #5.

### 3.2 Findings from the handover that were refined or withdrawn after checking the bytes

| Handover finding | Byte-verified correction |
|---|---|
| LEAD-B01 "sign reversal (FX-deflated −31.7%)" | **Withdrawn.** It rested on a USD conversion mislabelled as real deflation, and the rial valuation basis across the divided monetary areas is not recorded (directive correction A). Re-severed from BLOCKER to MATERIAL. |
| LEAD-B03 "≈2.6% of formal private-sector credit" | **Rejected** (directive correction B). There is overlap risk: 12 MFBs are on the same bank list. Valuation, date and coverage also differ. The magnitudes are shown separately. |
| LEAD-M04 "SE≈2.78, p≈0.16, ratio CI [2.24, 5.08]" | **Rejected** (directive correction C). These are model-calculated without the survey design. The survey-design limits are stated instead. |
| LEAD-M10 "publish an adult-population denominator" | **Rejected** (directive correction D). The incompatibility is stated instead. |
| LEAD-B07 "`source_dependencies` empty 108/108" | **Refined.** The Master holds 48 bound objects; the projection drops the field on all 108. 60 objects need object-level binding. |
| LEAD-M11 "block in `findex_baseline.json`" | **Refined.** The block lives in the Master (25_FINDEX_BASELINE r14–35), so it is removed Master-first (PB-0220). |
| CWR-010 "missing G2Px paragraph" | **Refined.** It is an intra-Master defect: the paragraph exists in 09, and the rendered 03 section lacks it (PB-0360/0361). |
| LEAD-M07 "`<table>`=1 in dist" | **Corrected.** The count is 0. The a11y flag is still an over-claim (PB-0400). |
| LEAD-M09 "family resolves to /methodology/" | **Not adopted.** It conflicts with the accepted S01 hard condition (two equal children). See §4. |
| PB-0342 (my earlier "misaligned columns") | **Lead error, corrected.** 31 rows 78–79 carry the block's own title and header. The fix is one schema per sheet. |
| PB-0413 count (my earlier 64/61) | **Corrected to 65 occurrences in 62 cells**, as the independent verifier found. |

### 3.3 New findings in this window (byte-verified)

| Finding | Severity | Patch |
|---|---|---|
| **LEAD-B08.** OECD/INFE Yemen 15/100 and 42/100 published as source-reported; the Master labels unconfirmed rows "Verified Yemen facts" | BLOCKER | PB-0101–0112, PB-0165/0166 |
| /measurement/ ships "Present them as filterable or expandable items…" | MATERIAL (leak) | PB-0514–0516 |
| 13 ungoverned VISUAL-class records publish design instructions as their `summary_en` (Arabic is prose) | MATERIAL (leak + parity) | PB-0500–0512 |
| Reading-visual `what_it_shows_en` and `accessible_summary_en` are drawing instructions (19 fields, rendered) | MATERIAL | PB-0430–0448 |
| RV-CWR-007 leads with the gap, not the levels (binding correction #6) | MATERIAL | PB-0436/0445/0449/0450 |
| VIS-MFI-DIVERGENCE uses a trend verb and contradicts its own last sentence | MATERIAL | PB-0451/0452 |
| VIS-FIRM-CONSTRAINTS is `RANKED_HORIZONTAL_BAR` on multi-response data | MATERIAL | PB-0453–0457 |
| 22_PROVIDERS_DATA holds a second table (status events) under the sheet header | EDITORIAL→MATERIAL for generators | PB-0517 |
| /people/ Arabic title asks a different question from the English title | MATERIAL (parity) | PB-0526 |
| Arabic CLM-031 omits its own thesis; 12 English universes are placeholders; English titles of 2014 records carry no year; the CWR-007 thesis leads with the gap; the Arabic calques «الكون» and «كائن» | MATERIAL / EDITORIAL | PB-0527–0529, 0560–0577, 0590–0595, 0530–0555, 0600–0607 |
| /methodology/ lacks coverage, admission, conflict-setting and uncertainty rules (addendum) | MATERIAL GAP | PB-0611–0614 |
| Tranche A domain decisions not yet specified (firms behaviour, e-wallet series, access, provider structure, status events, Decision 18) | MATERIAL | PB-0517–0525 |
| Independent verifier 2: 30 material and 23 editorial findings on the new rows | all fixed | see `TRANCHE_B_RED_TEAM.md` §5 |

### 3.4 Disposition index

**BLOCKER:**
- LEAD-B08 (OECD scores);
- LEAD-B06 (remittance evidence state and vintages);
- LEAD-B07 (object lineage);
- LEAD-B04 (meta description);
- LEAD-B05 (Arabic strapline and noun);
- LEAD-B02 (leaked instructions).

**MATERIAL:**
- LEAD-B01 (re-severed);
- LEAD-B03;
- LEAD-M01–M13;
- the Tranche A domain decisions carried in (PB-0520–0526, 0517–0519).

**Rejected:** see `TRANCHE_B_RED_TEAM.md §4` and narrative §14.

Every disposition maps to rows in the spec. The narrative gives the map.

## 4. Method & Measurement — interaction contract (LEAD-M09 / PB-0420–0424)

This contract implements the accepted S01 decision without route changes. It is binding on Design as the acceptance test; the visual treatment remains Design's choice.

**Structure:**
- The header has five primary items: Explore · Evidence · Evidence Readings · Data & sources · Method & Measurement.
- There is a persistent Trust affordance: About · Corrections · Rights & reuse · Accessibility · Privacy · Terms · Contact.

**Family label:**
- EN "Method & Measurement"; AR «المنهج والقياس».
- It is **non-interactive text**: not a link, not a button, not a hover trigger, not a popup trigger.
- It never resolves to either child.

**Children:**
- "Methodology" «المنهجية» → `/methodology/`.
- "Measurement Agenda" «أجندة القياس» → `/measurement/`.
- Both are direct links. They are **always visible** at every breakpoint, with no disclosure needed.
- They have **equal visual weight**: same type size, weight, colour and hit area.
- Neither is indented under the other, and neither is styled as secondary.

**Desktop (≥1024px):** the family label with its two children inline beneath it or beside it. Both children stay visible without hover.

**Mobile (320–767px) drawer:**
- The same three elements appear in the same order: label, Methodology, Measurement Agenda.
- Both children are visible on opening the drawer (no nested accordion).
- Each child has a minimum 44×44 CSS px target.

**Keyboard:**
- Tab order: … Data & sources → Methodology → Measurement Agenda → Trust affordance.
- The label receives no focus.
- Visible focus ring on each child. Enter activates.
- No focus trap in the drawer beyond the standard modal pattern (Escape closes it and returns focus to the trigger).

**Screen reader:**
- The label is exposed as a group name (`role="group"` with `aria-labelledby` pointing to the label).
- The children are links in document order.
- No `aria-haspopup` and no `aria-expanded` (there is nothing to expand).

**RTL:** the order mirrors to right-to-left. The Arabic label and children are the governed strings above. The compound labels "Data & sources / البيانات والمصادر" and «المنهج والقياس» must not truncate at 320px.

**Active state:** on `/methodology/` or `/measurement/`, only the matching child shows the current-page state, and the family label shows no current-page state.

**Breadcrumbs:** `/measurement/` → Home › Measurement Agenda, and `/methodology/` → Home › Methodology. There is no breadcrumb node for the family, because it has no route.

**Same-commit rule (PB-0423):**
- `/measurement/` gains `global_navigation`, with prominence `PRIMARY_CHILD`, **in the same commit** that moves About to the Trust group.
- `/about/` leaves the footer group `method_measure` regardless.

**Schema (PB-0424):**
- Nodes are `{route?, label_en, label_ar, children[]}`.
- The validator rejects an interactive node without a route, and a routeless node with fewer than two always-rendered children.

**Acceptance:**
- Re-run the S05.2 320–400px and RTL assertion suite on the new header.
- Both children are reachable in one click or tap from every page.
- There is no hover-only meaning.

**Do not claim mobile or RTL pass until this suite is re-run.**

## 5. Surface sign-offs (Lead)

"Signed" means the review is complete and every accepted change is specified. It does not mean the changes are installed.

| Surface | Sign-off |
|---|---|
| Eight domains | Reviewed. Truth-critical defects are specified. The Tranche A "told nowhere" evidence now has patches for /firms/, /payments/, /access/, /finance/ and /providers/. /remittances/ gets a measurement node via MA-001. /reforms/ gets dated FMIIP baselines. /people/ leads with levels and adds the income gap. |
| 10 Readings | All dispositioned (`READINGS_MEASUREMENT_CLOSURE.md`): 10 KEEP, of which CWR-006 has a thesis rewrite, CWR-007 leads with levels, CWR-001 is de-jargoned and CWR-010 has its paragraph restored. Domain links set by per-pair test. |
| 10 Measurement priorities | All dispositioned: 8 KEEP, MA-001 and MA-003 rewritten, no MA-011. |
| 36 visual contracts | All dispositioned: 26 KEEP (17 with voice-only edits), 10 REFINE, 0 MERGE, 0 RETIRE (`VISUAL_CONTRACT_CLOSURE.md`; reconciled with the handover's 24/12). The 13 ungoverned VISUAL records are table-only until contracted. |
| Signature visual candidates | 6 evaluated: 2 already covered by existing contracts, 1 accepted as prose on /methodology/ (no chart), 3 rejected as duplicates or overclaim risks. Zero new contracts (`SIGNATURE_VISUAL_CANDIDATES.md`). |
| Arabic | Terminology decisions («خلاصة», «المنصة»), CBY-Aden qualification, the YPCC name and calque removal are specified. `EXTERNAL_HUMAN_CERTIFICATION_NOT_PERFORMED`. |
| English | Backend voice, instruction voice and precision are specified. |
| Search | Measured with a 28-term bilingual probe. Fixes are specified (PB-0490–0494). |
| Evidence, Compare, Data & sources, About, Trust | Specified (`EVIDENCE_COMPARE_TRUST_CLOSURE.md`). |
| Methodology and indicator architecture | Tested against the addendum (`METHODOLOGY_COMPLETENESS_CLOSURE.md`, `INDICATOR_COVERAGE_MATRIX.csv`). |

## 6. Validation split

**Current repository validation (executed, green).** See §1. The repository is internally consistent at its unchanged authority. Nothing in this validation says the public corpus is final, because no semantic patch is installed.

**Proposed-patch validation (simulated, not installed).** `audit/tranche_b_patch_tooling/simulate.py` applied every SUBSTR row and every sweep row, in execution order, to an exported copy of the Master:
- 0 builder errors and 0 collisions;
- 272 sweep edits, each with a unique before-text;
- sweep residuals equal the KEEP register exactly (24, 49 and 11);
- 0 residual forbidden strings in rendered or public-bearing fields (20 patterns);
- EN/AR numeric-invariance mismatches fall from 46 to 22 (10 test artefacts and 12 recorded one-language-more-specific fields; `BILINGUAL_EDITORIAL_CLOSURE.md` §2);
- 0 drawing-instruction summaries left in 06 or 11;
- 7 residual strings in one non-rendered derived cell pair (02 r139), resolved by PB-0472.

CELL, NEW, SCHEMA, GENERATOR_RULE and BUILD rows cannot be simulated on text alone. Each states its own post-regeneration test in `validation_required`.

**External certification.** Native-speaker certification of the Arabic, and legal and rights review, were **not performed**.

## 7. Status tokens

| Item | Token |
|---|---|
| Repository build, validation and manifest; S00 re-bind (Tranche A) | `EXECUTED` |
| All 994 patch rows | `VERIFIED_BY_CLAUDE_TEAM` · `SPEC_PENDING_EXECUTION` · `INDEPENDENT_OPENAI_ACCEPTANCE_REQUIRED` |
| OECD/INFE Yemen row; YPCC exact Arabic name; Decision 18/2026 entity names | `PRIMARY_SOURCE_PENDING` (39 rows) |
| Arabic rows needing native certification (243) | `EXTERNAL_HUMAN_CERTIFICATION_NOT_PERFORMED` |

**Final: `TRANCHE B COMPLETE — READY FOR INDEPENDENT REVIEW`.** STOP.
