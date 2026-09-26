# RESOURCE LIBRARY MODEL (Tranche A · A3)
# نموذج مكتبة المصادر

**Session:** Tranche A / A3
**Date:** 2026-09-25 (Africa/Cairo)
**Mode:** Model decision + discoverability test. Facet/field additions are semantic projection changes → specified here, not executed (generator constraint, see A2 §4).

---

## 1. DECISION: ONE REGISTER, MANY VIEWS — KEEP THE SINGLE LIBRARY, ADD DISCOVERY FACETS

The product already has the correct shape: **one governed source register**, not multiple archives/corners:
- `source_library.json` — **159 source records** (26 `FULL_PUBLIC_CARD` curated cards + 133 `LOCATOR_ONLY` provenance locators), each bilingual with `why_it_matters` and — a strong asset to keep — `does_not_establish`.
- `master_dataset_catalog.json` — **211 datasets** with `domain`, `period_min/max`, source counts and `analytical_role`.
- Surfaced publicly at `/data/` ("Data & sources" per the A1 decision), whose current sections already cover catalogue contents, availability caveats, rights-travel, "what you may not find", "open the evidence record before reuse", the macro-financial chronology, and "Reports, methods and implementation references" (the 26 cards).

**KEEP AS IS:** the single-register model, the curated-card layer, the bilingual `why_it_matters`/`does_not_establish` pattern, the evidence-record-before-reuse discipline, the source-vs-evidence separation. **Do NOT** build separate "corners" per document type — that would fragment one truth. The goal is discoverability, not a bigger archive (deletion test applies).

**The gap is discovery FACETS/VIEWS over the one register, plus surfacing the regulatory-instrument layer** (below).

---

## 2. DISCOVERABILITY TEST — the 7 governed user queries

| # | User query | Current result | Verdict |
|---|---|---|---|
| 1 | Every relevant CBY exchange/remittance enforcement **decision in 2026** | 13 (→15 incl. Decisions 17 & pending-18) exist as `SRC-CBY-ENF-*` sources but **all `LOCATOR_ONLY`**, reachable only behind `/providers` status events — no library view lists them as a filterable set | **FAIL** — needs an issuer+type+date view |
| 2 | The **original source behind a POS figure** | search "POS terminals" → `/payments` + `/evidence/CLM-003` → source-reference closure → `source_library` locator | **PASS** |
| 3 | Yemen **financial-literacy measurement** | OECD/INFE source present (publisher OECD; "measurement standards" category card); findable by publisher/search but no clean topic facet, and not in the search smoke set | **PARTIAL** |
| 4 | **Consumer-protection rules** | CBY FCP 2023 present but `LOCATOR_ONLY` (law/instruction layer); reachable via `/reforms`, not via a library facet | **PARTIAL/FAIL** |
| 5 | **Remittance methodology** | IMF/RPW + "Global/regional measurement standards and methods" cards; findable by category/publisher | **PASS** |
| 6 | **Firm-finance datasets** | dataset catalogue has a `domain` field (firm finance); 211 datasets filterable | **PASS** |
| 7 | Analytical sources that are **context, not factual authority** | encoded in `does_not_establish` + category text ("…context", "…diagnostics"), but no clean **evidence-role** filter | **PARTIAL** |

Three of seven fail or half-fail, all for the same root cause: **the regulatory-instrument layer (decisions, laws, instructions) is not a discoverable, faceted set**, and there is no **evidence-role** or **document-type** facet.

---

## 3. REQUIRED MODEL ADDITIONS (spec for pipeline owner — Master/projection change)

Layer these **facets/views over the single register** (no new routes, no new corners):
1. **Issuer / authority** — CBY-Aden, World Bank, IMF, OECD, UNDP, KfW, CGAP, BIS/CPMI, Sana'a Center, … (already in `publisher` for the 26 cards; extend to the regulatory-instrument records).
2. **Document type** — law · regulation · decision/enforcement · instruction/circular · survey · dataset · official statistic · report/research · method/standard · provider-status instrument · consumer-protection material · financial-capability material.
3. **Evidence role** — primary factual evidence · status event · Yemen analytical literature · global method reference · context. (Promote `does_not_establish` into a first-class role signal.)
4. **Topic / domain**, **date / currentness**, **rights / publication state**, **related domain / related claim / evidence**.
5. **Surface the `LOCATOR_ONLY` regulatory instruments** (CBY Decisions 1–18/2026, laws, bank lists) into the discoverable library layer with at least issuer + document-type + date + status, **without** promoting them to full curated cards. This makes queries 1 and 4 succeed. Never infer legal status from silence.

For legal/regulatory instruments specifically, expose: issuer · instrument type · instrument number · issue date · effective date (if established) · entities affected · status/action · related instrument · original locator · verification date · rights · product impact.

**Acceptance test:** a user can answer all 7 governed queries above via facets **without** knowing repository/backend taxonomy.

**Honest status:** model = **DECIDED / VERIFIED BY CLAUDE TEAM**; facet/field build = **SPEC — PENDING MASTER-PROJECTION EXECUTION** (generator required); search-facet alignment = **Tranche B**.

*End of A3 Resource Library model.*
