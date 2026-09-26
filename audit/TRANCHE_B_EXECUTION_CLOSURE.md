# Tranche B — patch execution closure

**Status: TRANCHE B PATCH EXECUTION COMPLETE — READY FOR INDEPENDENT POST-EXECUTION ACCEPTANCE**

This is not DESIGN HANDOFF READY and not PUBLIC RELEASE READY. Tranche C has not been started. External repository copies
are `EXTERNAL_REPOSITORY_SYNC_PENDING`: the Drive file IDs in `authority/AUTHORITY.json` are lineage references and do not
hold these bytes until a controlled replacement is performed and verified. No external repository was changed.

Date: 2026-09-26. Governing directives: the post-Tranche-B acceptance gate (D1) and the controlled canonical execution
directive (D2, which supersedes D1 where they differ).

## 1. Authority state (verify first)

| Item | Value |
|---|---|
| Production Master | `authority/Yemen_Financial_Inclusion_Evidence_Master.xlsx` — SHA-256 `4403a3536e218d537710c12cd0df5340a35c058b35f9f06ef0f401a16b9c6dbd` |
| Entry Master (lineage) | `e69804106e04d093098688f2d01cea51e13191f255d774a090f3e5dd8dec9bc7` (recorded as `drive_recorded_sha256`) |
| Page Specs | `site-src/content/page_specs.json` — SHA-256 `776558e46a3aedaf1c58bbf4c3b32c752cc38b9f305a85c63b042f4292c20635` (entry `ff2b0f55…`) |
| Patch specification | `audit/MASTER_FIRST_PATCH_SPEC.csv` — SHA-256 `f31ebd49fe6c38cfa4cd81e1bbbd230791df45234778f9c2c9c43c71b1c8e9c7`; 1,001 rows, 395 roots; built twice in independent processes from the Stage-0 Master (`b010b60d…`) with identical bytes |
| Generator | `yfi-projection-generator` 1.2.0; manifest `scripts/projection/projection_manifest.json` SHA-256 `e0c6f5d3cde07bbddc00e4ae3bdf9ace6bce3f5fa5172e1a91a2d3e59232057a` |
| Build | 284 HTML documents from 141 Page Specs (route baseline unchanged) |
| Literal closure | 7,521 records, 0 unresolved |
| Validator | `WEBSITE REPOSITORY VALIDATION PASS` (HTML=284, ERRORS=0, WARN=0) |
| Projection check | `PROJECTION CHECK PASS`; generator regression tests 13/13 OK |

Machine-readable pre/post evidence: `audit/tranche_b_execution/PRE_POST_VALIDATION_SUMMARY.json` (all 17 acceptance checks PASS).

## 2. How the execution ran

1. **Entry verification.** Entry Master and Page Specs matched the expected hashes.
2. **Generator rebuilt and baseline-gated** before any patch (`audit/generator_baseline/`): fidelity PASS on the entry Master; the gate exposed an
   authority-integrity defect (AUTH-INT-001: 14_SYSTEM_CHRONOLOGY rows 18–28 were eleven copies of YSC-013) and entry projection drift, each classified.
3. **Stage 0 — AIR-001.** Chronology restored from the manifest-certified projection (exact-value checks; ledger `tranche_b_execution/AIR-001_LEDGER.json`).
4. **Spec determinism gate and acceptance corrections** (OECD, CBY decisions, YPCC, roles, rights, coverage, About label, firms wording, sweeps).
5. **Stages 1–5**, each a transaction run by `audit/tranche_b_execution/run_stage.py`: snapshot → install the staged Master (and any controlled
   file changed in the same commit) → regenerate every projection → rebind control files → build → literal audit → validator → generator `--check`;
   any failure restored the snapshot. Stages 1–4 each rolled back at least once on a real finding (for example the leaked private-file notes, the literal-closure gate and the presentation-tier contract) and were re-run after a Master-first or code fix.

| Stage | Scope | Master SHA-256 after | Result |
|---|---|---|---|
| 0 | AIR-001 authority integrity | `b010b60d…` | COMMITTED |
| 1 | Object-level lineage and verification integrity (PB-0001…0008, PB-0010…0069) | `905a497c…` | COMMITTED |
| 2 | False, misleading and leak defects (P2) + EXF-001 | `4e3d9158…` | COMMITTED |
| 3 | Domain, Reading, Measurement, methodology, coverage, parity + EXF-002 | `3064257b…` | COMMITTED |
| 4 | IA, trust, source discovery, search, visual contracts | `298cd879…` | COMMITTED |
| 5 | Bilingual editorial (ENGLISH-VOICE, ARABIC-CALQUE) and per-cell sweeps PB-0413/0414/0415 | `d0efa8eb…` | COMMITTED |
| 4B | Three discovery aliases found necessary by the post-execution search probe | `4403a353…` | COMMITTED |

## 3. Root dispositions

`audit/MASTER_FIRST_PATCH_EXECUTION_LEDGER.csv` — every spec root has exactly one disposition, with its reason.

| Disposition | Roots |
|---|---|
| APPLIED | 375 |
| HELD | 12 — PB-0160, PB-0161, PB-0322, PB-0345, PB-0374, PB-0470, PB-0471, PB-0520, PB-0521, PB-0522, PB-0525, PB-0614 |
| SUPERSEDED | 7 — PB-0103, PB-0104, PB-0107, PB-0111 (correction A); PB-0425 (correction G); PB-0472 (by EXF-002); PB-0490 (by EXF-001 and correction F) |
| SOURCE_PENDING | 1 — PB-0390P (publisher/issuer population) |
| FAILED | 0 |

Execution items outside the spec (Lead): AIR-001; EXF-001 (non-locator text in 15.primary_url, leaked private file names on 5 routes × 2
languages); EXF-002 (02.full_copy made a derived Master field — 30 cells had diverged from the rendered page and surfaced unrendered text in search);
EXC-0302 (the Findex visual record carries the education level the /people/ section states).

**Why the holds.** Six roots add public numbers that no source-closed record bound to the page carries (the literal-closure rule); adding records
would add routes and extending route bindings is an IA change outside the spec (unresolved queue U-12). PB-0322 would add a route. PB-0374, PB-0470
and PB-0471 need bilingual editorial adjudication or R8.5 architecture (U-13). PB-0525 needs governed Arabic event text (U-13).

Sweeps: executed per cell after the D2 re-adjudication (`tranche_b_execution/STAGE5_SWEEP_ROW_LEDGER.csv`). PB-0414: all 68 non-derived cells revised
by context (هذا الموقع / قاعدة الأدلة / هنا / impersonal), «المنصة» used nowhere; PB-0413: 25 cells applied, one KEEP (QE-011, fact-checking sense), T01 and B01–B03 applied;
PB-0415: 76 applied, one revised (S119: the financial-system "system" kept, re-based on the AIR-001-restored cell); 102 full-copy rows (13 + 44 + 45) superseded by EXF-002.

## 4. Source-lineage truth test

`audit/tranche_b_execution/SOURCE_LINEAGE_TRUTH_TEST.json`. Evidence Records show only exact bound sources, listed member records, or an explicit state.

| 06 lineage_state | Records | Closure state |
|---|---|---|
| BOUND_EXACT | 87 | CLOSED_TO_SOURCE_ID |
| BOUND_PARTIAL | 6 | PARTIALLY_RESOLVED (CLM-017, CLM-039, CLM-045, CLM-046, CLM-056, VIS-PAYMENT-RAILS) |
| COMPOSITE_OF_OBJECTS | 13 | 1 with listed members (CLM-031); 12 COMPOSITE_MEMBERS_NOT_LISTED |
| SOURCE_NOT_YET_BOUND | 1 | VIS-PROVIDER-TIME |
| FRAMING_NO_FACT | 1 | CLM-004 |

All ten Readings are PARTIALLY_RESOLVED because their 08 evidence_bindings still name datasets. Entry state for comparison: the legacy rule
asserted CLOSED_VIA_CONTROLLED_DEPENDENCIES on 108/108 records while 87 carried unresolved tokens and dataset tokens expanded to every source in the
dataset. A lower, truthful closure rate replaces a false 100%.

The nine BOUND_CANDIDATE bindings were checked against Master data; six were revised (VIS-MFI-SPINE adds the 2021 YMN source; VIS-PAYMENT-RAILS is
partial with REF-PAY-001 open; CLM-004 is a framing rule; CLM-020 cites the MF-ORIG rows' sources; CLM-027 and DS-FINDEX-PUBLIC-HISTORY drop the
unused 2014 microdata catalogue), and VIS-FINDEX-OBSERVED-WAVES was corrected likewise. The 24 pre-populated cells without a source ID were
re-adjudicated (`tranche_b_execution/STAGE1_LINEAGE_ADJUDICATION.json`); the truncated Master token `EP-IMF-CBY-REMIT-ME...` was repaired.

## 5. Acceptance items (D2 §13)

| Item | Result |
|---|---|
| Hashes (Master, Page Specs, spec, generator, manifest) | §1 |
| Build / validator / literal closure / projection check | PASS |
| Bilingual parity | Validator AR/EN structural parity PASS; numeric signatures PASS; Arabic rows carry `EXTERNAL_HUMAN_CERTIFICATION_NOT_PERFORMED` |
| Lineage closure counts by state | §4 |
| Search probe (28 terms × 2) | 44 PASS, 12 WEAK, 0 FAIL (entry 25 / 20 / 11); 21 smoke tests pass (12 new, primary route in the top 3) |
| Compare | PASS |
| Rights / download gating | 160/160 `rights_state` = NOT_ASSESSED; locators shown for citation and verification only; no download or reuse offer |
| No authoring copy / internal fields / private-file notes on public pages | PASS |
| Methodology coverage | PB-0611/0612/0613 public; PB-0614 held |
| Remittance vintage break | AR2024 USD 6.245bn vs AR2025 restated USD 3.42bn visible (six-figure precision removed) |
| Provider scope | "Whose list is this?" on /providers/ (PB-0216); 22 issuing_authority column |
| OECD binding | 42/100 and 15/100 published with sample and fieldwork, survey-scoped, no ranking; 29 verification_state set; OECD-YEM-018 added |
| No unsupported inference | Forbidden-wording scan PASS; ranking clauses removed from 29 |
| Route baseline | 284 |
| Stale-hash scan | no current-state file carries a stale hash (`tranche_b_execution/STALE_HASH_SCAN.json`) |

## 6. What changed for a reader

- Evidence Records now say exactly what they rest on: bound sources, member records, or a plain statement that the record is not yet linked or asserts no figure.
- The meta description of every page is a governed, language-correct description (the English internal design question no longer leaks into both editions).
- Primary navigation: Explore · Evidence · Evidence Readings · Data & sources · Method & Measurement (Methodology, Measurement Agenda). A trust
  bar (About «عن الموقع» · Corrections · Rights & reuse · Accessibility · Privacy · Terms · Contact) sits above the header and in the footer.
- Domain pages surface their governed Readings; search normalises Arabic and English, uses governed aliases (discovery only) and shows each
  result's period or document type.
- The OECD/INFE Yemen values, the CBY-Aden provider scope, the methodology coverage / admission / conflict-setting rules and the Arabic
  self-reference are corrected in both languages.

## 7. Re-run

```
python3 scripts/generate_projections.py --check
python3 -m unittest discover -s scripts/projection/tests -t .
python3 scripts/build.py && python3 scripts/audit_public_literals.py && python3 scripts/validate.py
python3 audit/tranche_b_execution/post_execution_acceptance.py
sha256sum -c SHA256SUMS.txt
```

## 8. Not claimed

No native-speaker Arabic certification, legal review of reuse terms, or primary-source verification beyond what the ledger records was performed.
Publisher and issuer values stay empty unless confirmed. The external repository copies were not changed.
