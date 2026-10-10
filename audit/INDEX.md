# Audit index

The audit folder is the programme's memory. **Nothing here is semantic authority** — the Production Master is — and
only the first two groups describe the current state. Every file in `audit/` is classified in
`FINAL_REPOSITORY_MANIFEST.json` (`CURRENT_PROGRAMME_RECORD`, `STANDING_POLICY`, `AUDIT_HISTORY`, and the generated
`audit/PUBLIC_LITERAL_CLOSURE.json`); the validator fails if a top-level file here is missing from this index.

## 1. Current programme — final integration to the Design handoff (directive D7, 26 September 2026)

| Session | Record |
|---|---|
| Directive | [`directives/D7_FINAL_INTEGRATION_TO_DESIGN_HANDOFF_2026-09-26.md`](directives/D7_FINAL_INTEGRATION_TO_DESIGN_HANDOFF_2026-09-26.md) (verbatim; index in [`directives/README.md`](directives/README.md)) |
| Post-F9 correction (27 Sep) | Directive [`directives/D8_POST_F9_CORRECTION_2026-09-27.txt`](directives/D8_POST_F9_CORRECTION_2026-09-27.txt) (verbatim); record: the addendum to [`FINAL_CLEAN_ROOM_ACCEPTANCE.md`](FINAL_CLEAN_ROOM_ACCEPTANCE.md) |
| Design-enablement control pass (27 Sep) | Directive [`directives/D9_DESIGN_ENABLEMENT_CONTROL_PASS_2026-09-27.txt`](directives/D9_DESIGN_ENABLEMENT_CONTROL_PASS_2026-09-27.txt) (verbatim); record: the second addendum to [`FINAL_CLEAN_ROOM_ACCEPTANCE.md`](FINAL_CLEAN_ROOM_ACCEPTANCE.md) |
| F1–F2 Readings | [`READING_PORTFOLIO_FINAL_ADJUDICATION.md`](READING_PORTFOLIO_FINAL_ADJUDICATION.md), [`READING_PORTFOLIO_CHANGE_LEDGER.csv`](READING_PORTFOLIO_CHANGE_LEDGER.csv); transaction and run reports in [`reading_integration/`](reading_integration/) |
| F3 Resource Library | [`F3_RESOURCE_DECISIONS.md`](F3_RESOURCE_DECISIONS.md) |
| F4 R8.5 subtraction | [`R8_5_REPOSITORY_SUBTRACTION_CLOSURE.md`](R8_5_REPOSITORY_SUBTRACTION_CLOSURE.md), [`R8_5_SUBTRACTION_LEDGER.csv`](R8_5_SUBTRACTION_LEDGER.csv) |
| F5 public corpus | [`F5_PUBLIC_CORPUS_ACCEPTANCE.md`](F5_PUBLIC_CORPUS_ACCEPTANCE.md), [`F5_CORPUS_FINDINGS_LEDGER.csv`](F5_CORPUS_FINDINGS_LEDGER.csv) (every review finding with the Lead decision) |
| F6 SEO, accessibility, rights, security | [`F6_DISCOVERY_ACCESSIBILITY_RIGHTS_SECURITY_ACCEPTANCE.md`](F6_DISCOVERY_ACCESSIBILITY_RIGHTS_SECURITY_ACCEPTANCE.md) |
| F7 sustainability and stewardship | [`SUSTAINABILITY_PRE_DESIGN_BASELINE.json`](SUSTAINABILITY_PRE_DESIGN_BASELINE.json) (measured with `final_integration/f7_measure_baseline.py`); method in `docs/SUSTAINABILITY_METHOD.md`; non-public stewardship note `handoff/SUPPORT_AND_PARTNERSHIP_READINESS.md` |
| F8 R8.6 freeze | [`R8_6_DESIGN_HANDOFF_FREEZE_CLOSURE.md`](R8_6_DESIGN_HANDOFF_FREEZE_CLOSURE.md) |
| F9 clean-room acceptance | [`FINAL_CLEAN_ROOM_ACCEPTANCE.md`](FINAL_CLEAN_ROOM_ACCEPTANCE.md); open items in `FINAL_OPEN_ITEMS_REGISTER.md` (repository root) |
| Transactions F3–F9 | [`final_integration/`](final_integration/) — scripts, inputs, Master ledgers and run reports |
| Independent acceptance of pull request #8 (2 Oct) | [`PR8_INDEPENDENT_ACCEPTANCE.md`](PR8_INDEPENDENT_ACCEPTANCE.md) — the production runtime (EAD-01…EAD-11) verified and adjudicated; verdict MERGE AFTER CONDITIONS; fixes nothing |
| Owner decisions (2 Oct) | [`OWNER_DECISIONS_2026-10-02.md`](OWNER_DECISIONS_2026-10-02.md) — the owner's decisions of 2 October 2026: OWN-01…OWN-05, the publisher name, EAD-03, D7 final visual acceptance, and the dispositions of the acceptance findings A3 / C3, A5 / C4 and A4 / C6; recorded, not applied |
| Owner decisions (9 Oct) | [`OWNER_DECISIONS_2026-10-09.md`](OWNER_DECISIONS_2026-10-09.md) — the owner's decisions of 9 October 2026: pull request #15 (V1) approved and merged with a merge commit; Phase B steward changes (Home Orientation tier, the interface-label transaction, the navigation contract); fonts; the rights choice left open; pull request #13 held |
| Records reconciliation (2 Oct) | [`RECORDS_RECONCILIATION_2026-10-02.md`](RECORDS_RECONCILIATION_2026-10-02.md) — release candidate G5: the after-merge record fixes of pull request #8 (C8, C9) and the listed minor items, one row each (finding, action, files); C1–C5 confirmed still holding |
| Release candidate (2 Oct →) | [`release_candidate/INSTRUCTIONS.md`](release_candidate/INSTRUCTIONS.md) — the owner's release-candidate brief, saved verbatim: Part A (owner decisions, PR #8 acceptance conditions, held-back labels) and Part B (finish, challenge, harden); the transaction scripts, ledgers and run reports of the RC-* transactions and the Part B records live beside it in [`release_candidate/`](release_candidate/) |
| Owner Addendum 2 (2 Oct) | [`release_candidate/INSTRUCTIONS_ADDENDUM_2026-10-02.md`](release_candidate/INSTRUCTIONS_ADDENDUM_2026-10-02.md) — the owner's second addendum to the release-candidate brief, saved verbatim from its BEGIN to its END marker: the public value rule, the red team, release defects A1 (VIS-PAYMENT-RAILS) and A2 (the "law" search boundary), improvements 1–11, lessons from comparable products, the currentness and enrichment sweep, the roadmap items and the rejected list |
| Arabic dates, systemically (2 Oct) | [`release_candidate/ARABIC_DATE_ISOLATION_SWEEP.md`](release_candidate/ARABIC_DATE_ISOLATION_SWEEP.md) — the owner's request after RC-5: every Arabic page swept for dates, ranges and identifiers printed without left-to-right isolation (114 runs on 44 pages and 16 runtime text nodes found, all fixed in the renderer and runtime), B2c confirmed for running prose, and the RC-DATES gate with its negative controls |
| Original-source verification (3 Oct →) | [`release_candidate/ORIGINAL_SOURCE_VERIFICATION.md`](release_candidate/ORIGINAL_SOURCE_VERIFICATION.md) — every number and fact re-read in its original once the originals could be read (owner's update of 3 October 2026): Part A items 3 and 6 on Path A, the currentness and enrichment sweep, and the first-screen and drawn-figure numbers before B15; matches recorded as well as corrections |
| Editorial passes B2 and B3 (2 Oct) | [`release_candidate/ARABIC_EDITORIAL_LEDGER.md`](release_candidate/ARABIC_EDITORIAL_LEDGER.md) and [`release_candidate/ENGLISH_EDITORIAL_LEDGER.md`](release_candidate/ENGLISH_EDITORIAL_LEDGER.md) — every change of the Arabic and English editorial passes (transaction RC-5), one row each with FROM, TO and reason, and the independent review before commit |
| Edition 2, the value lane (4 Oct →) | [`edition_2/EDITION_2_LOG.md`](edition_2/EDITION_2_LOG.md) — the owner's edition-2 brief in summary, the ranking of candidates a–f with the public value check, each decision in one line, and the batches; the transaction scripts, ledgers and run reports of the E2-* transactions live beside it in [`edition_2/`](edition_2/) |
| Measurement linkage B6 (3 Oct) | [`release_candidate/MEASUREMENT_LINKS.md`](release_candidate/MEASUREMENT_LINKS.md) — each Reading linked to the Measurement Agenda priorities whose stated purpose supplies the evidence it says is missing, every link quoting both sides in both languages; the gaps the agenda does not cover; the reachability of each priority; `decisions_unlocked` and `blocked_evidence` shown on /measurement/ (RC-9) |
| Text-first visuals B12 (3 Oct) | [`release_candidate/B12_TEXT_FIRST_DISPOSITIONS.md`](release_candidate/B12_TEXT_FIRST_DISPOSITIONS.md) — each of the 23 visual contracts that rendered only as text frames: the two bound to their designed table from governed rows in RC-12 (gate RC-B12), the four complete as designed, and the missing input named for each of the other seventeen; with one finding beyond B12 (origin tables the dataset catalog names but the Master does not hold). |
| Link check B13d (3 Oct) | [`release_candidate/LINK_CHECK.md`](release_candidate/LINK_CHECK.md) — every one of the 156 public original locators requested on 3 October 2026, with its outcome; locators moved to the publisher's current address only after the document was read and matched, otherwise to the web.archive.org copy of the original address (labelled on the site); counts by outcome and what stays open. |
| Reverse traces (3 Oct) | [`release_candidate/REVERSE_TRACES.md`](release_candidate/REVERSE_TRACES.md) — the six reverse traces Owner Addendum 2 asks for before B16 (Home headline claims, VIS-FINDEX-GAPS, VIS-POS-VALUE, RV-CWR-001, the /reforms/ chain, one IMF-attributed chronology event): public object → record → source → locator, each locator requested; six of six unbroken. |
| Product challenge B15 (3 Oct) | [`release_candidate/PRODUCT_CHALLENGE.md`](release_candidate/PRODUCT_CHALLENGE.md) — the independent panel (five lenses, ten users), every finding ranked by value with the red team's verdict and what happened to it (built, blocked, escalated, roadmap), the game-changer answers, and the two reviews of RC-15; the roadmap carries the rest (`docs/ROADMAP_V1_1.md` §3). |
| Final content pass (4 Oct →) | [`final_content/FINAL_CONTENT_LOG.md`](final_content/FINAL_CONTENT_LOG.md) — the owner's final content pass and hand-back: the Findex margins of error derived from the microdata supplied with that message, the source and locator work, the tool audit, the three items built under the steward contract exception, the record corrections and the home-page presentation pilot; the transaction scripts, Master ledgers and run reports of the FC-* transactions live beside it in [`final_content/`](final_content/) |
| Design integration V1, Phase B (9 Oct →) | [`design_integration/PHASE_B_LOG.md`](design_integration/PHASE_B_LOG.md) — the steward changes of the owner's decisions of 9 October 2026 (B-a, B-b, B-c): the interface-label transaction V1B-1, its script, Master ledger and run report in [`design_integration/`](design_integration/), and the navigation-contract change |
| Open-items disposition B16 (3 Oct) | [`release_candidate/OPEN_ITEMS_DISPOSITION.md`](release_candidate/OPEN_ITEMS_DISPOSITION.md) — every open item of the escalations, the register and the records they cite, the owner note of 11:15 (4.1–4.6, section 5) and the reopened rejections, each DONE, RELEASE, NEXT EDITION or REJECTED with its reason; the G0 notes |
| Owner decisions (10 Oct) | [`OWNER_DECISIONS_2026-10-10.md`](OWNER_DECISIONS_2026-10-10.md) — the owner's decision of 10 October 2026: rights decided and closed (CC BY 4.0 for CauseWay's own content stands, as adopted on 3 October 2026; the 9 October "no licence" message was about regulatory licensing, which CauseWay neither holds nor claims), the release step "counsel confirms the CC BY 4.0 text" unchanged, the software code outside the licence and undecided, and the steward designation for the public naming and terminology change; recorded, not applied |
| Public naming and terminology (10 Oct) | [`naming/NAMING_DECISIONS_2026-10-10.md`](naming/NAMING_DECISIONS_2026-10-10.md) — the owner brief's Part B: the label table with a reason per label, the glossary rules and their counts, the terminology register, the rights presentation, and the independent review; the transactions NB-1 and NB-2, their Master ledgers and run reports, and the remittance substitution list live beside it in [`naming/`](naming/) |
| Legacy-audit follow-through (10 Oct) | [`legacy_followthrough/`](legacy_followthrough/) — the owner brief "Legacy-audit follow-through" with the owner's corrections: transaction LA-A (corrections to our own copy), the source verification record [`SOURCE_VERIFICATION_2026-10-10.md`](legacy_followthrough/SOURCE_VERIFICATION_2026-10-10.md), the Master ledgers and run reports in `runs/` |

Records named above that do not exist yet are written by the session that owns them; until then the session is open.

## 2. Standing policies (still binding)

| Record | Rule |
|---|---|
| [`FINAL_CURRENTNESS_CUTOFF.md`](FINAL_CURRENTNESS_CUTOFF.md) | Currentness cut-off 26 September 2026 |
| [`ARABIC_TERMINOLOGY_AND_STYLE_LEDGER.md`](ARABIC_TERMINOLOGY_AND_STYLE_LEDGER.md) | Arabic terminology and style |
| [`BENCHMARK_AND_COMPARATOR_POLICY.md`](BENCHMARK_AND_COMPARATOR_POLICY.md) | How external benchmarks and comparators may be used |
| [`ECONOMIC_CONTEXT_USAGE_POLICY.md`](ECONOMIC_CONTEXT_USAGE_POLICY.md) | How economic and conflict context may be used |
| [`tranche_c/DRAFTING_RULES.md`](tranche_c/DRAFTING_RULES.md) | Drafting rules for governed copy |

## 3. History (lineage — accurate when written, not current)

| Stage | Records |
|---|---|
| Tranche C (whole-product adversarial acceptance; accepted by OpenAI 26 Sep 2026) | `TRANCHE_C_FINAL_ACCEPTANCE.md`, `TRANCHE_C_FINDINGS_LEDGER.csv`, `tranche_c/` |
| Pre-Tranche-C maturation P1–P5 | `P1_PUBLIC_TRUTH_EDITORIAL_CLOSURE.md`, `P2_TOOL_DISCOVERY_CLOSURE.md`, `P3_VISUAL_DESIGN_READINESS.md`, `P4_CANONICAL_HANDOFF_ALIGNMENT.md`, `P5_INDEPENDENT_ACCEPTANCE_CORRECTIONS.md`, `PRE_TRANCHE_C_ACCEPTANCE_MATRIX.csv`, `pre_tranche_c/` |
| Tranche B (Master-first patch) | `CLAUDE_TRANCHE_B_CLOSURE.md`, `TRANCHE_B_EXECUTION_CLOSURE.md`, `TRANCHE_B_RED_TEAM.md`, `TRANCHE_B_UNRESOLVED_QUEUE.md`, `MASTER_FIRST_PATCH_NARRATIVE.md`, `MASTER_FIRST_PATCH_SPEC.csv`, `MASTER_FIRST_PATCH_EXECUTION_LEDGER.csv`, `SOURCE_PUBLISHER_PROPOSALS.csv`, `TERMINOLOGY_SWEEP_KEEP_REGISTER.csv`, `CLAUDE_TRANCHE_B_CONTINUATION_HANDOVER_TO_NEXT_WINDOW.md`, `tranche_b_execution/`, `tranche_b_patch_tooling/`, `generator_baseline/` |
| Tranche A (authority, IA, currentness, resource model, domains) | `CLAUDE_S00_AUTHORITY_AND_ACTIVE_SURFACE.md`, `CLAUDE_S01_IA_DECISION.md`, `CLAUDE_TRANCHE_A_HANDBACK.md`, `CURRENTNESS_AND_SOURCE_ADJUDICATION.md`, `RESOURCE_LIBRARY_CLOSURE.md`, `DOMAIN_CORPUS_EDITORIAL_CLOSURE.md`, `CLAUDE_FIELD_LEVEL_CHANGE_LEDGER.csv` |
| Addenda (Tranche A/B) | `BILINGUAL_EDITORIAL_CLOSURE.md`, `ENGLISH_EDITORIAL_CLOSURE.md`, `EVIDENCE_COMPARE_TRUST_CLOSURE.md`, `ECONOMIC_SYSTEM_AND_EVIDENCE_REVIEW.md`, `METHODOLOGY_COMPLETENESS_CLOSURE.md`, `READINGS_MEASUREMENT_CLOSURE.md`, `SEARCH_DISCOVERY_CLOSURE.md`, `SIGNATURE_VISUAL_CANDIDATES.md`, `SOURCE_NARRATIVE_EXTRACTION.md`, `VISUAL_CONTRACT_CLOSURE.md`, `INDICATOR_COVERAGE_MATRIX.csv` |
| R-programme R0–R8.4A | `R0_CANONICAL_RECONCILIATION_CLOSURE.md`, `R1_PUBLIC_VOICE_2B_CLOSURE.md`, `R2_READINGS_MEASUREMENT_CLOSURE.md`, `R3_METHOD_TRUST_LEGAL_OPERATIONAL_CLOSURE.md`, `R4_SITEMAP_END_TO_END_JOURNEYS_CLOSURE.md`, `R5_EVIDENCE_UTILIZATION_AND_RESOURCE_LIBRARY_CLOSURE.md`, `R6_INFORMATION_DESIGN_AND_TECHNICAL_ARCHITECTURE_CLOSURE.md`, `R7_NATIVE_BILINGUAL_EDITORIAL_INVARIANCE_CLOSURE.md`, `R8_1_PUBLIC_TRUTH_SOURCE_REFERENCE_CLOSURE.md`, `R8_2_LITERATURE_LEGACY_NARRATIVE_RECOVERY_CLOSURE.md`, `R8_3_INTELLECTUAL_PRODUCT_CLOSURE.md`, `R8_4A_HOME_EXPLORE_ENTRY_JOURNEY_CLOSURE.md`, `R8_CONTINUATION_MASTER_HANDOVER_TO_NEXT_WINDOW.md`, `SESSION_01_PRODUCT_IDENTITY_CAUSEWAY_ROLE_PUBLIC_VALUE_CLOSURE.md`, `FINALIZATION_PROGRAM.md` |
| Superseded drafts | `prior-review-records/` (see its README) |
| Earlier programme directives | `directives/D0…D6` |
| Post-build sessions S00–S06 (Sept 2026) | `docs/S0*_*.md`, `docs/*.json` other than current documents — each marked `HISTORICAL_LINEAGE` |

Continuation handovers (`CLAUDE_TRANCHE_B_CONTINUATION_…`, `R8_CONTINUATION_MASTER_HANDOVER_…`) are kept as lineage and
must not be executed: the current instructions are the repository's `README.md`, `AGENTS.md` and `handoff/README_FIRST.md`.

## 4. Generated

`PUBLIC_LITERAL_CLOSURE.json` — written by `scripts/audit_public_literals.py` on every build; never edited by hand.
