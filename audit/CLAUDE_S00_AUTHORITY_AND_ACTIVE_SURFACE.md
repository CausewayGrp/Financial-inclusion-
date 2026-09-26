# CLAUDE S00 — AUTHORITY + ACTIVE-SURFACE ORIENTATION
# إغلاق الجلسة صفر — إثبات المرجعية وخريطة السطح الفعّال

**Session:** S00 (Authority + Active-Surface Orientation)
**Programme:** Claude Final Pre-Design Maturation (hub-and-spoke; Team Lead = this session)
**Date:** 2026-09-25 (Africa/Cairo, UTC+03:00)
**Entry mode:** Cold start. No prior Claude conversation, memory, prior ZIP, prior design or earlier conclusion was trusted. The supplied repository is the only starting point.
**Edit state:** READ-ONLY. No file in the repository was modified during S00. This orientation record is the only file added.

---

## 1. PURPOSE

Understand exactly what is active before touching anything: verify the declared authority against actual bytes, map the repository, classify every active surface, run the available machine checks, and fix the exact next session. No corrections are made in S00.

---

## 2. ENTRY HASHES — VERIFIED AGAINST ACTUAL BYTES

The constitution declared two expected entry hashes. Both were recomputed from the extracted bytes and **match exactly**:

| Object | Path | Expected (constitution) | Actual (recomputed) | Result |
|---|---|---|---|---|
| Production Master | `authority/Yemen_Financial_Inclusion_Evidence_Master.xlsx` | `e69804106e04d093098688f2d01cea51e13191f255d774a090f3e5dd8dec9bc7` | `e69804106e04d093098688f2d01cea51e13191f255d774a090f3e5dd8dec9bc7` | **MATCH** |
| Page Specs | `site-src/content/page_specs.json` | `ff2b0f559cde5fede3fe31d7dfb2539a00921e8b00b816c2863790cd9de49007` | `ff2b0f559cde5fede3fe31d7dfb2539a00921e8b00b816c2863790cd9de49007` | **MATCH** |

No hash restoration was required. The repository is authentic and at the expected authority state.

**Full manifest:** `SHA256SUMS.txt` lists 58 governed files. `sha256sum -c` returned **58/58 OK**. The manifest deliberately covers the governed authority + projection surface and excludes `dist/` (build output), the `docs/` operational layer, the granular `site-src/content/data/*` + some `sources/*` inputs, the `audit/` lineage, and the `design/` PNGs — i.e. the checksum surface is the *governed truth surface*, not the whole tree.

---

## 3. AUTHORITY CHAIN — ONE AUTHORITY, CONFIRMED

The declared authority chain is internally consistent and all cross-references resolve to the **current** Master:

- `authority/AUTHORITY.json` (schema `YFIE_AUTHORITY/2.0`) records Master `e69804…` as sole semantic/evidence/source/rights/product-state/publication-state authority; projections may not overrule it; **master-first correction rule** and **projection rule** (resolve-from-Master-and-regenerate on hash divergence) are stated.
- `authority/CORE_CONSTITUTION.md` — durable rules only (evidence discipline, semantic firewall, UNDERSTAND → EXPLORE → VERIFY, source-reference closure, bilingual co-authority, product boundary, counterfactual deletion test). No mutable state.
- `authority/YFI_CURRENT_PROJECT_CONTEXT.json` (compact projection, `generated_at` 2026-09-25T14:06+03:00) records Master `e69804…`, Page-Specs `ff2b0f…`, `all_page_specs_master_hash_match: true`, `projection_hash_binding: PASS`.
- `README.md` records the same two hashes and the current programme marker.
- **Independent check:** the current Master hash `e69804…` is embedded **142 times** in `page_specs.json` (141 specs + 1 index). The claim `all_page_specs_master_hash_match: true` is therefore verified, not merely asserted.

**Conclusion:** there is exactly one authority (the Production Master `e69804…`) and the entire governed projection surface is bound to it.

---

## 4. CURRENT PRODUCT STATE (as recorded, verified against controlled scale)

Programme marker (README): **R0–R8.3 CLOSED/PASS; R8.4 ACTIVE; R8.4A (Home + Explore + governed-question entry) CLOSED/PASS.** The repository's own next pointer is **R8.4B — provider/regulatory currentness + Resource Library integration** (README + `audit/R8_CONTINUATION_MASTER_HANDOVER_TO_NEXT_WINDOW.md`). This maps directly onto the constitution's Session 02.

Controlled scale (from `YFI_CURRENT_PROJECT_CONTEXT.json`, consistent with README and with the constitution's "expect approximately" figures):

| Object | Count |
|---|---|
| Page Specs | 141 |
| Page sections | 572 |
| Governed entry questions | 11 |
| Evidence objects (records) | 108 |
| Public claims | 59 |
| Evidence Passports | 55 |
| Readings | 10 |
| Measurement priorities | 10 |
| Visual contracts | 36 |
| Search records | 427 |
| Sources | 159 (158 publicly addressable) |
| Curated source/report cards | 26 |

Live public navigation is **Option A**: `Explore · Evidence · Readings · Data · Methodology · About`. Domain routes: `/people/ /firms/ /finance/ /providers/ /payments/ /remittances/ /access/ /reforms/`.

These are inventory facts, not a measure of quality.

---

## 5. ACTIVE-SURFACE CLASSIFICATION

Every top-level surface classified for decision-making authority:

| Surface | Class | Notes |
|---|---|---|
| `authority/*` (Master, AUTHORITY.json, CORE_CONSTITUTION.md, YFI_CURRENT_PROJECT_CONTEXT.json) | **AUTHORITATIVE** | Master is sole authority; the three companions are its durable rules + compact projection. |
| `site-src/content/page_specs.json` | **ACTIVE PROJECTION (controlled)** | 141 specs, bound to current Master. |
| `site-src/content/content/*`, `evidence/*`, `sources/*`, `visuals/*`, `presentation_priority.json` | **ACTIVE PUBLIC PRODUCT INPUT** | Governed projections consumed by build; all manifest-verified. |
| `site-src/content/data/*` | **ACTIVE DATA INPUT (subordinate)** | Granular data projections; mostly outside the checksum surface — treat as regenerable inputs, not independent truth. |
| `site-src/app.js`, `styles.css`, `assets/*` | **ACTIVE IMPLEMENTATION BASELINE** | Proven static behaviour; not semantic authority. |
| `scripts/build.py`, `validate.py`, `audit_public_literals.py` | **ACTIVE BUILD/VALIDATION BASELINE** | Deterministic; see §6. |
| `design/architecture/*` | **ARCHITECTURE AID** | Diagrams; explicitly "not a parallel source of truth." |
| `handoff/*` | **DRAFT HANDOFF — NOT EXECUTABLE AUTHORITY** | README + constitution both forbid treating as final; **carries stale hashes — see §7 BLOCKER**. |
| `docs/*` | **OPERATIONAL / PRIOR-LINEAGE** | Runtime docs + a *prior* post-build session lineage (S00–S06) bound to a **stale** Master; several read as "current" but are not — see §7. |
| `audit/R0…R8.4A*`, `audit/prior-review-records/*` | **AUDIT LINEAGE (non-authoritative, historical)** | Legitimate closure records; may cite older entry hashes as their own historical entry state. |
| `audit/*(1).md` | **UNCONTROLLED DUPLICATE COPIES** | Download artifacts — see §7. |
| `dist/` | **TEMPORARY BUILD OUTPUT** | Not shipped in repo; regenerated by build; excluded from manifest. Rebuilt during S00 for validation only. |

**Files explicitly excluded from decision-making** (they must not be read as current authority): everything in `docs/` bearing a stale hash (§7), the `handoff/` package until re-bound, all `audit/*(1).md` duplicates, and `design/` PNGs.

---

## 6. MACHINE CHECKS RUN IN S00

| Check | Command | Result |
|---|---|---|
| Manifest integrity | `sha256sum -c SHA256SUMS.txt` | **58/58 OK** |
| Public-literal closure | `scripts/audit_public_literals.py` | **PASS** — `records=7309 unresolved=0` |
| Deterministic build | `scripts/build.py` | **PASS** — "Built 284 HTML files from 141 controlled page specs." (284 = 141×2 + root + 404, matches baseline) |
| Full validator | `scripts/validate.py` (post-build) | **FAIL — 8 ERRORS, 0 WARN** (see §7) |

`build.py` was confirmed side-effect-safe before running (no network; writes only to `dist/`, which it recreates). The governed surface was not touched.

---

## 7. KNOWN RISKS (evidence-based, carried into later sessions)

### R-S00-01 · BLOCKER · Repository fails its own validator (stale authority hashes in recipient-facing handoff)
`validate.py` returns 8 errors, all authority-hash staleness in the **recipient-facing `handoff/`** package:
- `handoff manifest Master hash is stale` and `handoff manifest Page Specs hash is stale` (`handoff/IMPLEMENTATION_MANIFEST.json` records Master `054484e8…`, Page-Specs `8e460396…`).
- Stale/unrecognised authority hashes `054484e8…` and `8e460396…` in `handoff/MASTER_IMPLEMENTATION_PROMPT.md`, `handoff/CLAUDE_DESIGN_MASTER_PROMPT.md`, `handoff/CLAUDE_CODE_MASTER_PROMPT.md`.

**Diagnosis:** these are **Generation-A** hashes (the Master/Page-Specs vintage immediately preceding the current `e69804…`/`ff2b0f…`). The Master itself is correct and current; only subordinate recipient projections are stale. **Fix is projection re-binding (master-first compliant), not a semantic Master change.** A green validator is a stated acceptance gate, so this blocks OpenAI acceptance until resolved. → Owner: consistency/currentness fix (constitution S02/S07/S08 machine-check + handoff hardening).

### R-S00-02 · MATERIAL · Stale "current-state" files in docs/ (Generation-B hash)
A distinct earlier vintage — **Generation B**, Master `f94f1f…`, Page-Specs `4e8a0d8f…` — survives only in `docs/`: `HANDOFF_STATE.json`, `REPOSITORY_BUILD_SUMMARY.json`, `PROGRESS_INVENTORY.json`, `REVIEW_LEDGER.json`, `FINAL_RELEASE_VERIFICATION.md`, `CHANGELOG.md`, plus two S06 closure records. Several of these *present as current state* (e.g. `HANDOFF_STATE.json` reports 141 specs but **500** sections, **150** sources, and `current_next_session: HANDOFF_FROZEN` — contradicting the current 572 sections / 159 sources and the live R8.4B pointer). The validator tolerates them (operational, not recipient-facing), but they must not be read as current. → Owner: repository cleanliness/disposition (S08), refresh or quarantine.

**Hash lineage (three generations):** Generation B (`f94f1f…`/`4e8a0d8f…`, in `docs/`) → Generation A (`054484e8…`/`8e460396…`, in `handoff/` + cited as entry state in R8.3/R8.4A audit closures) → **Current** (`e69804…`/`ff2b0f…`, governed surface). Audit closures legitimately cite Generation A as *their* entry hash; that is historical record, not staleness.

### R-S00-03 · EDITORIAL/CLEANLINESS · Duplicate files on the active surface
- `site-src/content/content/page_contracts.json` and `site_map.json` are **byte-identical** (both `b825c8…`, 573 KB, both manifest-governed) — one duplicated projection under two names. Confirm both consumers before any dedup; do not delete blindly.
- `audit/R6_…_CLOSURE(1).md` is byte-identical to its base; `audit/R4_…_CLOSURE(1).md` and `audit/R8_3_…_CLOSURE(1).md` are *divergent* uncontrolled variants of manifested/near-manifested closures. All three `(1)` files are download artifacts. → S08 disposition.

### R-S00-04 · CONTEXT (not this programme's scope) · Release-boundary items already recorded
`docs/HANDOFF_STATE.json` records open release-gate items: canonical Drive folder + Master have "anyone-with-link writer" permission (`R042` permission risk), and a remote-webfont runtime dependency remains. These belong to the R9/live-release gate, not maturation; noted so they are not lost.

### R-S00-05 · CURRENTNESS · Provider/regulatory adjudication pending (R8.4B)
Constitution S02 names CBY Decision 17/2026 (expected present — confirmed: `HANDOFF_STATE` and Master history record "DATED_CBY_DECISION_17_2026_AL_BURAQ_STATUS_EVENT" already ingested) and CBY Decision 18/2026 (to be independently verified from primary CBY material). Decision 18 verification depends on external primary-source retrieval; capability/limits to be stated honestly at S02.

---

## 8. CLOSE CONDITION

One authority state is agreed: **Production Master `e69804…` is sole authority; the full governed projection surface (manifest, 58 files, all page specs) is bound to it; staleness is confined to the non-governed `handoff/` (Generation A, validator-blocking) and `docs/` (Generation B) layers.** No edits were made. S00 is **CLOSED / PASS**.

---

## 9. EXACT NEXT SESSION

Two things are ready to run and are independent of each other:

1. **Fix the validator BLOCKER (R-S00-01)** — re-bind the recipient-facing `handoff/` files and refresh the stale `docs/` current-state files to the current Master `e69804…`/Page-Specs `ff2b0f…`; re-run `build → audit → validate` to green; refresh `SHA256SUMS.txt`. Master-first compliant (no semantic change).
2. **Session 01 — IA decision (READ-ONLY):** Option A (current) vs Option B (Analysis / Sources & Data / Method & Measurement + Trust secondary) vs a defensible Option C, decided against the actual `navigation_interaction.json`, `questions.json` and route set, using the 30 IA criteria and anti-patterns; one defended Team-Lead decision with consequence + migration map.

**Honest scope note for the Team Lead / OpenAI:** several later sessions have genuine capability or irreversibility boundaries that will be labelled as *analysis* rather than *certification* where that is the truthful description — specifically: external verification of post-cutoff 2026 primary sources (CBY Decision 18/2026 and the S02 candidate list); native-Arabic *senior-editor* certification of the full bilingual corpus; and any semantic Production-Master edit + full downstream regeneration. These will not be declared complete unless they are genuinely complete.

*End of S00.*
