# CURRENTNESS AND SOURCE ADJUDICATION (Tranche A · A2)
# تدقيق الحداثة والمصادر

**Session:** Tranche A / A2
**Date:** 2026-09-25 (Africa/Cairo)
**Mode:** Verification + adjudication. External live retrieval was used only for named currentness issues (per the external-research rule). No Production-Master edit was executed — see the Master-ingestion constraint in §4.

---

## 1. CBY DECISION 17/2026 — VERIFY, DO NOT DUPLICATE → ALREADY PRESENT ✓

Decision 17/2026 (Al-Buraq / البراق) is **already ingested** in the governed content and must not be duplicated. Confirmed occurrences: `SRC-CBY-ENF-17-2026` in `source_library.json` (primary_url `https://cby-ye.com/news/973`, `datasets_or_use: DS-PROVIDER-MASTER, DS-PROVIDER-STATUS-EVENTS`, `row_count: 2`, `public_card_state: LOCATOR_ONLY`), plus `providers_data.json`, `page_specs.json` (20 refs), `public_object_source_closure.json` (14), `search_index.json`, `source_reference_map.json`, `master_dataset_catalog.json`. Provider record carries the entity in EN+AR ("Buraq"/"البراق"). **Disposition: KEEP AS IS. No change. No duplication.**

---

## 2. CBY DECISION 18/2026 — PRIMARY EVENT VERIFIED · EXACT NAMES PENDING

**Retrieved from primary CBY source** `https://cby-ye.com/news/975` (CBY-Aden official site) on 2026-09-25:

| Field | Verified value | Evidence class |
|---|---|---|
| Decision number | **No. 18 of 2026** | PRIMARY (CBY site) |
| Issue date | **24 September 2026** | PRIMARY |
| Issuing authority | Governor, Central Bank of Yemen — Aden (A. Ahmad Ahmad Ghalib) | PRIMARY |
| Action (verbatim AR) | «إيقاف التراخيص الممنوحة لشركة ومنشآت للصرافة ووكيل حوالة المخالفين وإغلاق مقراتها» — suspension of licences of a (violating) exchange company, exchange establishments and a remittance agent, and closure of their premises | PRIMARY |
| Scope | 1 exchange company + exchange establishment(s) + 1 remittance agent (as worded) | PRIMARY (aggregate wording) |
| Basis | field-inspection report, Banking Supervision Sector | PRIMARY |
| Exact entity names (AR/EN) | **NOT OBTAINED** — they reside in the linked signed PDF instrument («قرار رقم 18 …»), which the news page does not inline; the page text carries only the aggregate wording | **PRIMARY-SOURCE VERIFICATION PENDING** |

**Disposition: STATUS EVENT.** The dated enforcement event is PRIMARY-verified (mirrors the repo's own convention for enforcement events); the **per-entity names are `PRIMARY-SOURCE VERIFICATION PENDING`** (in the linked PDF; not extracted here). Secondary press names were **not** promoted (the one secondary article retrieved, Yemen Monitor 180277, was in fact about Decision 15/2026, not 18 — a caution against secondary attribution).

**Semantic-firewall guard (must travel with any ingestion):** licence suspension/closure is a dated regulatory action — it does **not** establish permanent operational cessation. Preserve: `licensed/listed ≠ currently authorised ≠ operational ≠ physically open ≠ serving customers`. Do not subtract these entities from an unknown base roster or infer that unaffected providers are active/compliant.

**Required Master ingestion (spec — see §4 for why not executed here):**
- Add source `SRC-CBY-ENF-18-2026`, primary_url `https://cby-ye.com/news/975`, `public_card_state: LOCATOR_ONLY`, linked `DS-PROVIDER-STATUS-EVENTS` (+ `DS-PROVIDER-MASTER` once names are extracted).
- Add a dated status event: Decision 18/2026, effective 2026-09-24, action = LICENCE_SUSPENSION_AND_CLOSURE, `name_evidence_state = PENDING_PRIMARY_PDF`, `public_admission = HOLD_NAME_PENDING_PRIMARY_CONTENT`, authority = CBY-Aden.
- Add to the regulatory chronology as `REG-2026-008` (2026-09-24, SUPERVISORY_ENFORCEMENT).
- **Do NOT** create per-entity provider rows until the PDF names are extracted.
- Follow-up action (editorial queue): extract the signed PDF from `cby-ye.com/news/975` to obtain verbatim AR entity names, then complete the entity rows.

---

## 3. NAMED CURRENT-SOURCE CANDIDATES (constitution §20) — ROLE ADJUDICATION

Each candidate is a "**evaluate, do not automatically promote**" item. Disposition is by evidence ROLE (assessable from the source's nature); the specific 2026 editions post-date the Jan-2026 knowledge cutoff and were **not individually retrieved** in this pass (none is a currentness blocker and none is a candidate to change a public claim — see the North-Star/product-boundary logic below). None is promoted to primary factual evidence.

| # | Candidate | Disposition | Changes what? |
|---|---|---|---|
| 1 | Yemen microfinance supervision paper — **FinDev Gateway, Sept 2026** | **YEMEN ANALYTICAL LITERATURE** (knowledge-platform secondary analysis; not the primary regulator's instrument) | **Resource Library card candidate only.** Any quantitative/provider claim requires upstream primary tracing. **NO PUBLIC CLAIM CHANGE.** |
| 2 | **IFAD — Sending Money Home 2026** | **GLOBAL METHOD REFERENCE / remittances CONTEXT** (modelled global/regional remittance estimates + methodology) | **Resource Library (methods) + optional context** in /remittances. Governed remittance authority remains IMF Article IV external-sector series; IFAD is context, not a replacement. **NO PUBLIC CLAIM CHANGE.** |
| 3 | **CPMI-IOSCO FMI cyber-resilience** material | **GLOBAL METHOD REFERENCE / standard** (payments/FMI standard, not Yemen evidence) | **Resource Library (methods/standards) candidate;** light context for payment-infrastructure (FMIIP/RTGS/FPS) framing. **NO PUBLIC CLAIM CHANGE.** |
| 4 | **Uzbekistan FI indices** (methodology comparator) | **GLOBAL METHOD REFERENCE (comparator)** | **Methodology/Measurement thinking context, low priority.** Apply the deletion test: include only if it demonstrably aids the Measurement Agenda; otherwise omit from the public product. **NO PUBLIC CLAIM CHANGE.** |
| 5 | **WB Joint Food Security Monitor — Yemen, Sept 2026** | **CONTEXT** (food security ≠ financial-inclusion outcome; semantic firewall) | **Resource-Library-only at most;** enters the public narrative only where it materially changes interpretation of an FI question (product-boundary rule). **NO PUBLIC CLAIM CHANGE.** |

**Net A2 corpus effect on public claims: NONE.** Decision 18 adds a dated provider STATUS EVENT (names pending); the five candidates change no public claim and are, at most, Resource-Library/context/method references.

---

## 4. MASTER-INGESTION CONSTRAINT (governs A2 execution and all later tranches)

The repository does **not** contain the Master→projection generator (`build.py` consumes only the JSON projections; `validate.py` only hashes the `.xlsx`; no script parses the workbook). Therefore a faithful **master-first → regenerate** operation **cannot be integrity-executed in this environment**, and the constitution forbids editing projections only ("never correct only a JSON; fix the Master"). Consequently:
- The Decision-18 ingestion above is recorded as a **precise, execution-ready specification** for the pipeline owner (OpenAI), **not executed** into the Master/projections here. Status: **VERIFIED (primary event) / MASTER INGESTION PENDING (generator required) / NAMES PENDING (primary PDF)**.
- This is not a lowering of the work: the verification is complete and the ingestion spec is complete. Only the mechanical Master regeneration is deferred to the environment that holds the generator.

*End of A2 currentness & source adjudication.*
