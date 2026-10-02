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
| Release candidate (2 Oct →) | [`release_candidate/INSTRUCTIONS.md`](release_candidate/INSTRUCTIONS.md) — the owner's release-candidate brief, saved verbatim: Part A (owner decisions, PR #8 acceptance conditions, held-back labels) and Part B (finish, challenge, harden); the transaction scripts, ledgers and run reports of the RC-* transactions and the Part B records live beside it in [`release_candidate/`](release_candidate/) |

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
