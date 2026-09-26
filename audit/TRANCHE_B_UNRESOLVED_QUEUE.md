# Tranche B — unresolved queue (after patch execution)

This queue lists only items that are **genuinely unresolved and material** after the Tranche B execution (2026-09-26).
Every patch root has one disposition in `audit/MASTER_FIRST_PATCH_EXECUTION_LEDGER.csv`; the items below are what remains open.
Closed items are kept at the end with their resolution, so the queue can be audited against the pre-execution version.

## Open

### U-03 — CBY Decision 18/2026 entity names
- **Object:** SRC-CBY-ENF-18-2026 (15, PB-0518 APPLIED) and PSE-015 (22 status events, PB-0519 APPLIED, `NAMES_PRIMARY_SOURCE_PENDING`).
- **State:** the event is verified at cby-ye.com/news/975 (dated 2026-09-24); the page text names no entity; the names are only in the scanned PDF (cby-ye.com/files/6ab52faa3604f.pdf). Press names are not a usable source.
- **Next:** transcribe the names from the signed PDF, then set `entity_subject_state` and extend `datasets_or_use` to DS-PROVIDER-MASTER.
- **External check:** yes. **Blocks Tranche C:** no.

### U-06 — F-06, figures with no unit next to a vintage
- Unchanged. Run the unit check (03/06/07/09 public text: numbers with ≥4 digits not followed by a unit, within 60 characters of "vintage" / «نسخة» / "AR20").
- **Blocks Tranche C:** no.

### U-07 — Source publishers, issuers and rights
- **State:** PB-0390 APPLIED — 15 carries `issuer`, `hosting_platform`, `rights_state` (NOT_ASSESSED on every row), `licence`, `attribution_requirement`, `retrieval_date`, `document_type`, `evidence_roles`. Publisher/issuer population (PB-0390P) is **SOURCE_PENDING**: values are entered only when confirmed from the source itself or authoritative metadata; `SOURCE_PUBLISHER_PROPOSALS.csv` is a resolution aid, not metadata.
- **Rule in force:** a verified public locator may be shown for citation and verification while `rights_state` = NOT_ASSESSED; no download, republication or reuse permission is offered.
- **External check:** legal review of reuse terms is external. **Blocks Tranche C:** no.

### U-08 — Findex subgroup base n and design-based uncertainty
- Unchanged (FSG-0004; PB-0311/0312). Compute unweighted base n and design-based intervals from authorised microdata, reproducing the World Bank values first.

### U-09 — OECD 2026 financial-sector review and the 2023 SFD/SMED primary source
- Unchanged for the OECD 2026 review figures (PB-0165: withheld) and the SFD/SMED 2023 primary object (CLM-053/054/056/057 bound to the secondary sources that report the values).

### U-10 — Certification and re-test
- Native Arabic certification of every Arabic row (`EXTERNAL_HUMAN_CERTIFICATION_NOT_PERFORMED`), including the 68 re-adjudicated self-reference cells and the new interface copy.
- The 320–400px and RTL suite on the new header (navigation family + trust bar) and the domain-page Reading cards.
- The text-alternative table contract (PB-0400) once visuals render.
- **Blocks Tranche C:** no; required before any public-release claim.

### U-11 — Source lineage still open at record level (new)
- **State after Stage 1:** 87 records BOUND_EXACT, 6 BOUND_PARTIAL, 13 COMPOSITE_OF_OBJECTS (1 with listed members, 12 unlisted), 1 SOURCE_NOT_YET_BOUND (VIS-PROVIDER-TIME), 1 FRAMING_NO_FACT (CLM-004).
- **Open inputs:** CLM-017 (CBY payments listing page has no source record), CLM-039 / CLM-045 / CLM-046 / CLM-056 (inputs identified only at dataset level), VIS-PAYMENT-RAILS (REF-PAY-001 locator has no source record); the 12 unlisted composites need member records listed in the Master; all ten Readings are PARTIALLY_RESOLVED because 08 `evidence_bindings` carry dataset-level tokens.
- **Next:** bind the open inputs to exact sources or member records in 06/08; never expand a dataset token.

### U-12 — Numbers that no route-bound record carries (new; literal-closure holds)
- **Roots HELD:** PB-0160/0161 (/finance/ bank credit YER 1,350.4bn, May 2026 — no record binds SRC-CBY-001), PB-0345 (/evidence/compare/ three-numbers section), PB-0520 (/firms/ accounts and working capital — accepted intermediary wording ready), PB-0521 (/payments/ e-wallet subscribers), PB-0522 (/access/ lists and FMIIP baseline), PB-0614 (/methodology/ uncertainty example).
- **Why:** each section states verified Master values, but no source-closed Evidence Record bound to that route carries them; adding records adds routes (baseline 284 fixed) and extending existing records' route bindings is an IA change outside the spec.
- **Next:** decide, per section, between (a) extending existing records (e.g. VIS-FIRM-FINANCE-PATH for the firm metrics, CLM-009/CLM-008/XW-FMIIP-005 on /access/) and binding them to the route, or (b) new records with new routes in a controlled route change. The exact texts are in the spec.

### U-13 — Architecture items held (new)
- **PB-0470** (09 → reading-page sections): 03 and 09 bodies differ in all 80 Reading sections; needs bilingual editorial adjudication before switching. The full-copy part is done (EXF-002).
- **PB-0471** (embedded object blocks generated at build time): R8.5 candidate with PB-0470.
- **PB-0374** (limitations split into measurement limitation and prohibited inference): per-record editorial split of 216 cells.
- **PB-0322** (claim CLM-061, income-group gap): new route; the gap is public on /people/ and in MA-003.
- **PB-0525** (status-event table on /providers/): the 22 block needs governed Arabic event text and Arabic entity names from the source instruments.

### U-14 — Literal-audit heuristic (new finding EXF-003)
- `scripts/audit_public_literals.py` can classify a substantive number as non-substantive when its paragraph contains an inventory keyword ("records", «مصدر», …). Stage 3 used a strict check for new sections (numbers must be carried by a source-closed record bound to the route). A token-level rule should replace the paragraph-level keyword test before release.

### U-15 — Reference data retained for R8.5 (not subtracted)
- `content/page_contracts.json` (duplicate of site_map.json) and the historical audit files are kept; subtraction is an R8.5 decision.

## Closed in execution

| ID | Resolution |
|---|---|
| U-01 | Generator rebuilt (`scripts/generate_projections.py`, manifest `scripts/projection/projection_manifest.json`, generator 1.2.0); baseline gate PASS before any patch; every stage regenerated and passed `--check`. |
| U-02 | OECD/INFE 2023 Yemen values verified (acceptance correction A): literacy 42/100, well-being 15/100, sample 1,000, fieldwork 11 March–1 April 2023, two-question attitude score. Published survey-scoped; no ranking (PB-0101/0102/0105/0106/0108 APPLIED). |
| U-04 | Decisions searched individually: No. 7/2026 = interest rates on deposits (another subject; cby-ye.com/pages/14 → files/69dcac86e3520.pdf); Nos. 8, 12 and 16 of 2026 not publicly located (news pages /news/914–942, 946–963, 970–972 and the document lists checked). A numbering gap is not evidence of a missing provider-status event. |
| U-05 | «الشركة اليمنية للمدفوعات والمقاصة» is the verified public name (PB-0230 APPLIED). |
| AUTH-INT-001 | 14_SYSTEM_CHRONOLOGY rows 17–28 restored from the certified projection (AIR-001, Stage 0). |
| EXF-001 | Eight sources held a note ("USER_PROVIDED_FILE: …") in `primary_url`; moved to `non_public_locator_note`; only http(s) URLs count as public locators in build, search and validation. |
