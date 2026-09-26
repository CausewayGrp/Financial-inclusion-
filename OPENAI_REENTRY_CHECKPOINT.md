# OpenAI re-entry checkpoint — Yemen Financial Inclusion Evidence

**Programme:** Final integration to the Design handoff — directive D7 (`audit/directives/`), sessions F0–F9.
**Position (current):** OpenAI accepted the Tranche C checkpoint on 26 September 2026 (recipient verification 31/31) and
supplied the independent ten-Reading package with directive D7. Sessions F0–F5 are closed: the Reading portfolio is
integrated (F2), the Resource Library decisions are made (F3), R8.5 repository subtraction is closed (F4), the whole
public corpus is accepted (F5), the discovery, accessibility, rights and security contract is in place (F6) and the
sustainability baseline is recorded (F7). Sessions F8–F9 (R8.6 handoff freeze; clean-room acceptance) follow.

**Status: PUBLIC CORPUS ACCEPTED — R8.6 IN PROGRESS.**

- R8.4: CLOSED / PASS, Reading prose included (F2). R8.5: CLOSED (F4). R8.6: in progress (F6–F7 closed; F8–F9).
- This is not DESIGN HANDOFF READY and not PUBLIC RELEASE READY.
- The design and implementation prompts in `handoff/` remain **DRAFT — DO NOT EXECUTE YET** until the R8.6 freeze (F8).

**Date:** 2026-09-26.

## 1. Authority state (verify first)

| Item | Value |
|---|---|
| Production Master | `authority/Yemen_Financial_Inclusion_Evidence_Master.xlsx` — SHA-256 `ed3c5796cb0cca0109a0eb56f66d344ab0a5faa550e5235e05d65a6147f33fe1` |
| Page Specs | `site-src/content/page_specs.json` — SHA-256 `2407cb4f9ca67aec60304630690488d04a3b05f9ea1eec03f805de24915cb3ad` |
| Entry state recorded with the Drive IDs (lineage, not current) | Master `e69804106e04d093098688f2d01cea51e13191f255d774a090f3e5dd8dec9bc7`; Page Specs `ff2b0f559cde5fede3fe31d7dfb2539a00921e8b00b816c2863790cd9de49007` |
| Master lineage in D7 | `f0150122…` (entry) → `caabff47…` (RP-F2) → `0e8730c2…` / `69899ae2…` (RL-F3, RL-F3b) → `2a7fd52b…` / `440614d7…` (R85-A, R85-B) → `168a0ad8…` / `ed3c5796…` (RF5, RF5b) |
| Canonical repository | GitHub `CausewayGrp/Financial-inclusion-`, branch `main`. The last reviewed state is the signed tag `checkpoint/tranche-c-complete-reading-hold` |
| External (Drive) copies | `EXTERNAL_REPOSITORY_SYNC_PENDING` — the Drive files were not replaced; they are lineage, not working copies |
| Generator | `scripts/generate_projections.py`; `PROJECTION CHECK PASS`; 21 of 21 unit tests |
| Build | 288 HTML documents from 143 Page Specs (286 localized + root + 404) |
| Public-literal audit | 12,760 records, 0 unresolved; identical bytes under 8 `PYTHONHASHSEED` values |
| Source-lineage truth test | 8 of 8 |
| Validator | `WEBSITE REPOSITORY VALIDATION PASS`, 0 errors, 0 warnings (gates through R85-G09, RP-G06 and F6-G08) |
| Browser behaviour tests | `scripts/tests/test_public_tools.py` — 25 passed, 1 not applicable to the current data |
| Viewport acceptance | `audit/tranche_c/checks/viewport_acceptance.py` — 168 of 168 |
| Bilingual numeric invariance | `audit/tranche_c/checks/bilingual_invariance.py` — 0 page pairs differ (CI fails on any difference) |
| Current counts | `site-src/content/content/public_inventory.json` (derived from the Master; the only source for counts) |

The Master and Page Specs hashes in this file, `README.md`, `authority/AUTHORITY.json`, the Context and the handoff
manifest are rebound by `scripts/rebind_authority.py`; validator gate P4-G04 fails if any of them diverges.

## 2. What happened since Tranche C

Every Master change was a transaction committed through `audit/tranche_b_execution/run_stage.py` (regenerate, rebind,
build, literal audit, diagrams, repository manifest, validate, generator check; rollback on any failure).

- **Evidence Readings (F1, F2).** The independent ten-Reading package was adjudicated against the Master and its sources
  (`audit/READING_PORTFOLIO_FINAL_ADJUDICATION.md`, 60-row change ledger) and integrated Master-first (RP-F2). BIL-05
  closed: every English/Arabic page pair prints the same numbers.
- **F3 Resource Library.** Five bounded decisions: one curated card added, two deferred, two rejected
  (`audit/F3_RESOURCE_DECISIONS.md`).
- **F4 · R8.5.** Public copy moved out of `build.py` and `app.js` into the Master's governed interface copy; one path from
  authority to recipient; `FINAL_REPOSITORY_MANIFEST.json` classifies every tracked file; `audit/INDEX.md`; permanent
  gates R85-G01…G09 (`audit/R8_5_REPOSITORY_SUBTRACTION_CLOSURE.md`).
- **F5 public corpus.** Eleven reviewers read every governed public text in Arabic, English and for parity: 667 findings,
  all 57 material applied, 26 rejected under two house rulings, 3 deferred as source checks; scope qualifiers restored in
  Arabic, firewall errors fixed, three unsupported periods corrected from the records' own sources, control language
  removed, one duplicate source record retired, the chronology put in date order (`audit/F5_PUBLIC_CORPUS_ACCEPTANCE.md`,
  `audit/F5_CORPUS_FINDINGS_LEDGER.csv`).
- **F6 discovery, accessibility, rights, security.** Self-canonical, reciprocal hreflang with `x-default`, pre-release
  `robots.txt`, sitemap derivation for when the owner sets the public origin, JSON-LD with governed fields only; a strict
  Content-Security-Policy is now possible (no inline script or style); eleven WCAG 2.2 outcomes specified for Design and
  Code; gates F6-G01…G08 (`audit/F6_DISCOVERY_ACCESSIBILITY_RIGHTS_SECURITY_ACCEPTANCE.md`, `docs/DEPLOYMENT.md`).
- **F7 sustainability and stewardship.** Measured baseline of the reference build (`audit/SUSTAINABILITY_PRE_DESIGN_BASELINE.json`):
  the 10 MB master logo is 96–99 % of every cold page (release-only derivatives, TOOL-02); without it 0.09–0.45 MB in
  four requests. Method in `docs/SUSTAINABILITY_METHOD.md` (no carbon figure, budget or badge before Design). Non-public
  stewardship note `handoff/SUPPORT_AND_PARTNERSHIP_READINESS.md` (independence covenant, DPG gap assessment).

Tranche C itself is recorded in `audit/TRANCHE_C_FINAL_ACCEPTANCE.md` and `audit/TRANCHE_C_FINDINGS_LEDGER.csv`.
Currentness cut-off: 26 September 2026 (`audit/FINAL_CURRENTNESS_CUTOFF.md`).

## 3. House rulings carried forward

Recorded in `audit/F5_PUBLIC_CORPUS_ACCEPTANCE.md` §3 and binding on later editing: «فريد / الفريدين» for unique counts;
«التحويلات» for remittances as a macro flow and «الحوالة / الحوالات» for individual transfers, their prices, domestic
person-to-person remittances and the exchange-and-remittance sector; "the evidence base holds no …" (missing here is not
non-existent); «أول تعامل مع …» for first contact; «مستمر» for durable use; «قاعدة الاحتساب»; one Arabic name for the
OECD; CBY-Aden's full name at first mention; "edition", not "content version"; Evidence Record and visual twins stay
identical.

## 4. Open items carried forward (not defects of this state)

- **Evidence checks deferred in F5 (text unchanged until the source is read):** YSC-008 — date oil exports stopped
  ("from January 2023" to be checked against IMF Country Report No. 26/80); YSC-014 — unit of two IMF prudential ratios;
  SRC-CBY-ENF-10-2026 — date of Governor's Decision No. 10 of 2026.
- **Release-only dependencies:** TOOL-02 (web-size derivatives of the 10 MB master logo; the logo is never redrawn),
  TOOL-25 (navigation-group presentation, Design-owned), TRUST-09 (CauseWay identity and funding statement needs owner
  input), confirmation that the contact mailbox `office@causewaygrp.com` is monitored, the public origin
  (`site-src/deployment.json`; until it is set the build asks not to be indexed), security headers at the host
  (`docs/DEPLOYMENT.md`).
- **Known evidence frontiers:** CLM-044 value withheld (no public locator or rights assessment); the ~147-firm base
  implied by the 91.84% table; the CBY-Aden ↔ IMF remittance level crosswalk; the causes of the gender gap; reconciled
  current operating-provider status; the magnitude of the 2022 banking restatement.
- **Sessions still open:** F8 (R8.6 handoff freeze: one Design start path, acceptance criteria, design-to-code contract),
  F9 (clean-room recipient test, final open-items register, handoff archive).

## 5. Re-run

```
python3 scripts/checksums.py --check
python3 scripts/generate_projections.py --check
python3 -m unittest discover -s scripts/projection/tests -t .
python3 scripts/build.py && python3 scripts/audit_public_literals.py && python3 scripts/validate.py
python3 scripts/tests/test_literal_audit_determinism.py
python3 audit/pre_tranche_c/source_lineage_truth_test.py
python3 scripts/tests/test_public_tools.py                 # needs Python Playwright + Chromium
python3 audit/tranche_c/checks/viewport_acceptance.py       # needs Python Playwright + Chromium
python3 audit/tranche_c/checks/bilingual_invariance.py
python3 scripts/architecture_diagrams.py --check
python3 scripts/repository_manifest.py --check
```

## 6. Boundaries kept

- One authority. Every content change went into the Master first through the runner. No projection was edited by hand.
- Nothing closed earlier in the programme was reopened without a recorded finding.
- **Not claimed:** native Arabic certification, legal review, WCAG conformance, rights clearance, security guarantees,
  service levels.
- No external repository was changed.
