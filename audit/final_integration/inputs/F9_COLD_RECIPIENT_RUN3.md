# F9 cold-recipient run 3 — Claude Design dry run on a clone of main at b3c8e87 (report as delivered; only this title line added)

Repository: `cleanroom3/repo` at `b3c8e87` (branch `main`, clean tree). Production Master
`17db032b…038690b` and Page Specs `d45748…b69aa` match `handoff/README_FIRST.md` §3 byte for byte. Logo `5830163d…` matches.
Status line: `R8.6 FREEZE CANDIDATE — PENDING FINAL CLEAN-ROOM ACCEPTANCE`. That is expected for a dry run, so it is not
reported as a finding.

## Verdict

**No, with qualifications.** Following `README_FIRST.md` → brief → inventory → acceptance → contracts → open-items register, I
could start D0 and work through D1, D3, D4 and D5 without asking anyone anything:

- The authority chain, counts, routes, collections, hard-state data, verification states, technical states and journeys in
  the inventory agree with the JSON and with `dist/`.
- The brief's §2 precedence table correctly resolves every known contract conflict (OWN-07, OWN-08).
- Every §8 command passes. I also confirmed that the test harness runs unchanged against a site placed in
  `design/reference/out`.

I could not finish D2, D6 and D7 without either inventing something or shipping placeholders that the brief does not
anticipate:

- **Missing headings.** The chart text-alternative tables and the SIGNATURE provider matrix need column and dimension
  headings that have no governed labels.
- **Ungoverned values.** The provider matrix prints English-only, non-ISO date values.
- **Passport pointer.** One CORE contract tells Design to take in-frame text from a non-public, English-only Evidence
  Passport.
- **Unplaced visuals.** The domain-page presentation contract places only one of the 1–5 bound visuals on each route (none
  on `/reforms/`), yet the brief requires the others to be drawn there.
- **Snapshot fields.** The Home "evidence snapshot" requires per-signal unit and evidence-state fields that do not exist.
- **Unrendered sections.** Several governed sections (Home §2/§9, Explore §5, each Reading's section 1) are silently not
  rendered by the baseline, and no document says whether they are superseded.

None of these is a hard BLOCKER, because each has a sanctioned `NEEDS_CONTROLLED_CONTENT` / `ESCALATE_TO_MASTER` path.
Each is MATERIAL, because two careful designers would decide differently, or the register's claim that "every string Design
needs is governed" does not hold. One item would become a BLOCKER only if the npm registry is unreachable: the IBM Plex
fonts are not in the repository.

## Findings

| ID | Severity | File : section | Issue | Evidence | Fix |
|---|---|---|---|---|---|
| CR3-01 | MATERIAL (a BLOCKER if the npm registry is unreachable) | `handoff/CLAUDE_DESIGN_MASTER_PROMPT.md` §8 Typography; `FINAL_OPEN_ITEMS_REGISTER.md` EAD-08 | The two required fonts are not in the repository. D1 cannot be completed without registry access, or without asking the steward (the brief's own fallback). | `git ls-files` shows no `.woff`, `.woff2`, `.ttf` or `.otf` file and no Plex package. The brief says "if it is unreachable, ask the steward for the two package files". The pinned `@1.1.0` versions cannot be checked from the repository. | Vendor the two OFL packages (woff2 files plus licence) or a checksum-pinned tarball into the repository (F6-G07 allows woff2). Alternatively, give a governed fallback so D1 can proceed. |
| CR3-02 | MATERIAL | `site-src/content/visuals/visual_design_contracts.json` → every SIGNATURE and CORE `contract.fallback` / `form`; brief §10 (expected-NCC list), §12 (text alternative); `FINAL_OPEN_ITEMS_REGISTER.md` §7 | Brief §12 and acceptance F require a table fallback with scoped headers for every SIGNATURE and CORE chart. The contracts name those columns only in English prose. The SIGNATURE matrix VIS-PROVIDER-OBSERVABILITY also needs five visible dimension headings (its mobile form is "a definition list"). None of these headings exists as a `UI-*` label, and none is in §10's list of expected NCC requests. As a result, 11 of the 12 data-contract charts ship `⟦NCC⟧` headers, or Design invents them. RV-CWR-009 is the exception because it falls back to an ordered list. | Fallback columns named in English only, for example: "publication, reference year, value in USD million, source" (RV-CWR-001); "month, value, note" (VIS-POS-*); "corridor, amount, cost (%)"; "year, value, state, source document"; "object, value or withheld state, what it is not"; "lane, date, what is recorded". Matrix columns: "authority source, dated named universe or count, status events, negative authority, operation evidence". An exact-match search of `interface_copy.json` finds no Unit, Value, Year, Month, Note, Date, Group, Corridor, Amount, Cost, Publication, Reference year, State, Object, Lane or Event label. The register (§7) states: "every string Design needs is governed". | Add bilingual `UI-VIS-COL-*` / `UI-VIS-PRV-DIM-*` labels Master-first and reference them from each contract's `fallback` and `form`. If that is not done, add them to brief §10's list of expected NCC labels and correct the register (§7). |
| CR3-03 | MATERIAL | `visual_design_contracts.json` → VIS-PROVIDER-OBSERVABILITY `objects.universe` / `objects.wallet_counts` `date`, `count`; `display_label_rule` | The SIGNATURE matrix prints a "dated … count" column. The `date` values in two of its objects (`universe` and `wallet_counts`) are English free text or non-ISO, and one count is a string. None of these values has a bilingual label, and the label rule exempts only ISO temporal values. The Arabic frame cannot print them without translation by Design. | `PUC-EXCH-2026-01.date` = "Official 2026 annual roster; later 2026 status events separate"; `PUC-WALLET-2025-01.date` = "2024 Q3 / 2025 H1 / 2025-09-10 / 2026 event states"; `PUC-MFI-2026-01.date` = "observed 2026-09-07"; `WCR-001/002/004.date` = "2024 Q3", "2025 H1", "2026-01-22 event"; `WCR-004.count` = ">9". | Govern these as `*_iso` values plus bilingual `date_label` / `count_label` (Master 11 / controlled input), so that the generator's "printed value without a label" guard covers them. |
| CR3-04 | MATERIAL | `visual_design_contracts.json` → VIS-POS-TERMINALS `contract.annotation`; VIS-POS-TRANSACTIONS `annotation`; brief §2 (REFERENCE role) | The contract says the DISAGREEMENT note text comes "from the passport critical limit (EP-CBY-POS-MONTHLY)". Passports are REFERENCE: never rendered and English-only. The flagged rows carry no second figure, yet `UI-VIS-DISAGREEMENT` says "both are shown". VIS-POS-TRANSACTIONS names no note source at all. Precedence ("the projection is right") conflicts with brief §2 ("never render" passports). | The DISAGREEMENT rows OBS-00060, -00077, -00080 (terminals) and OBS-00078, -00081 (transactions) have no note field. The passport `critical_limit` holds +7.6%, +11% and +4.9% versus the computed changes. The same figures exist in governed bilingual form in the Evidence Records VIS-POS-TERMINALS and VIS-POS-TRANSACTIONS (`summary_*`, `method_*`). | Repoint the annotation, in the controlled input, at the record's `method_*` / `summary_*`, or add bilingual per-row note labels. State the rule in brief §12. |
| CR3-05 | MATERIAL | `site-src/content/presentation_priority.json` → domain `routes[*].primary`; brief §12 ("on the routes in `governed.public_routes` as the Page Specs bind it"), §9.2 (`institutional_sequence`, `mobile_rtl`); `DESIGN_TO_CODE_CONTRACT.md` §2 | The domain-depth contract places at most one visual per route (none on `/reforms/`). The Page Specs bind 13 further non-retired visuals that the brief says to draw on the domain route. No contract gives their tier (primary / supporting / progressive) or first-load status. The hard states on `/payments/` and `/reforms/` depend on them. The baseline shows them only as record links. Design would therefore invent the depth placement, and results would diverge. | Placed: `/people/` VIS-FINDEX-GAPS, `/payments/` VIS-PAYMENT-ANATOMY, `/remittances/` VIS-REMITTANCE-MACRO, `/firms/` VIS-FIRM-CONSTRAINTS, `/finance/` VIS-MFI-DIVERGENCE, `/providers/` VIS-PROVIDER-OBSERVABILITY, `/access/` VIS-ACCESS-EVIDENCE-LAYER, `/reforms/` none. Unplaced but bound: VIS-POS-TERMINALS, -TRANSACTIONS and -VALUE (CORE small multiple), VIS-REMITTANCE-COST (CORE), VIS-E-MONEY-RULE-STACK, VIS-FL-EVIDENCE-LADDER, VIS-PAYMENT-RAILS (named by §9.2 for `/reforms/`), VIS-FCP-REDRESS-PATH, VIS-FIRM-FINANCE-PATH, VIS-FIRM-FINANCE-SEVERITY, VIS-TARGET-RESULT-STATE, VIS-OECD-FCP-TIMELINE. The inventory's `data_at_route` for `/ar/payments/` lists DISAGREEMENT, MISSING and NOMINAL, which only the POS visuals carry. | Add `kind: visual` placements (tier plus `after_primary`) for every bound visual to `presentation_priority.json`, or state one family rule in brief §4 / §12 for bound-but-unplaced visuals. |
| CR3-06 | MATERIAL | Brief §4.1 (Orientation: "a truthful evidence snapshot") and §4.4; `handoff/IMPLEMENTATION_MANIFEST.json` `dashboard_policy` | The snapshot is allowed only if each signal carries its own measure, unit, population, period and evidence state. The fields for this are missing. A compact strip would need number extraction (which the "never shorten" rule forbids), an ungoverned unit, and an evidence-state mapping invented from internal enums. | `evidence_objects.json` has no value, unit or evidence-state field. `public_claims.json` has `evidence_badge` / `claim_type` (for example `PRIMARY_WEIGHTED_SURVEY`, `ADMIN_TREND`), which are internal enums with no `UI-*` label. `presentation_priority.json` (TOOL-01 note) says unit is not governed per record. Only the prose of Home Page Spec §3 carries the three signals. | State in §4.1 that the snapshot is Home §3 plus the bound records' `period_*` / `universe_*` (the baseline's choice). Otherwise, govern a per-record unit and evidence-state label Master-first. |
| CR3-07 | MATERIAL | `page_specs.json` for `/` (§2, §9) and `/explore/` (§5); `content/reading_sections.json` `section_order` 1; `DESIGN_TO_CODE_CONTRACT.md` §2 ("the Page Spec's section order is the content order") | Governed text blocks are silently not rendered, and nothing says they are superseded. (a) Home §2 "Start with the question, not the dataset" and §9 "Questions to start from", and Explore §5 "Questions to start from", are replaced in `dist/` by the `UI-QUESTIONS-*` headings. On Home the question block also moves above §3, whereas Page Spec order would put it last. (b) Every Reading has a `reading_sections.json` section 1, "What the evidence supports" / «ما الذي تسنده الأدلة" (identical to the thesis). It is not in the Page Spec and is not rendered, although `reading_sections.json` is RENDER. Design must choose between duplicate headings or duplicate text on one side and dropping governed text on the other. | A per-section probe of all 286 localised pages against their Page Specs finds only these 3 non-rendered sections (Home §2 and §9, Explore §5) in both languages. `scripts/build.py` `home_special()` and `question_cards()`. Section 1 of CWR-001 to CWR-010 has `copy_en` equal to `thesis_en`. | Record the decision in the inventory (for example `collection.superseded_sections` and a Home module order), or retire the blocks Master-first. Tell Design that Reading section 1 is the standfirst. |
| CR3-08 | MATERIAL | Brief §10 (Evidence workbench: "the baseline has a text filter") and §19 (hook list) | The description misreads the baseline. The `/evidence/` input `#global-search` is the site-wide search (`search_index.json`), not a record filter. The suites require that input to produce `.search-hit` items in `#search-results`, and to show `#search-results .empty` with "could not be loaded" when the index fails. A designer who turns it into the workbench's record filter would fail the suites. The `.empty` class is also missing from the §19 hook list. | `dist/en/evidence/index.html`: `<input id="global-search" data-search-input …>` in `<section id="search">`. `scripts/tests/test_public_tools.py` `t_search_results`, `t_search_failure` (line 192) and `t_announce`. | In §10, say that `/evidence/` keeps the in-page global search and that a record filter is a separate new control. Add `.empty` (and the required `role` / `aria-live` values) to §19. |
| CR3-09 | MATERIAL | `handoff/ROUTE_CONTENT_AND_STATE_INVENTORY.json` `projection_roles` → `visuals/system_relationships.json: RENDER` | The file is classed as a direct render input, but its prose fields `supported_relationship` and `not_supported` exist in English only (26 rows, no `_ar`). The baseline uses only `from` / `to` to build "Related questions". A designer drawing the system view from this file would have no Arabic text. | Its keys are only `link_id`, `from`, `to`, `relationship_type`, `supported_relationship`, `not_supported` and `evidence_refs`. `build.py` `related_questions()` reads only `from` / `to`. | Reclassify it as REFERENCE, or as "structure only: prose not public", or add governed Arabic Master-first. |
| CR3-10 | MATERIAL (low) | `scripts/build.py` `question_href()` (JRN-15); inventory `/explore/` collection | The link from QE-001 (primary_route `/`) targets `/{lang}/#system`, the anchor placed before VIS-INCLUSION-TRANSMISSION on Home. This behaviour lives only in code. The inventory and brief expose only `primary_route`, so Design would link the question to the top of Home. | `dist/en/explore/index.html` contains `href="/en/#system"`. `questions.json` gives QE-001 `primary_route: "/"`. The string "#system" appears nowhere under `handoff/`. | Add the anchor to the inventory (for example `question_links`) or to the brief's Explore / Home family rules. |

## §8 commands (run in a scratch copy, then deleted)

| Command | Result |
|---|---|
| `pip install -r requirements.txt && playwright install chromium` | already satisfied; Chromium launches |
| `scripts/checksums.py --check` | PASS: `CHECKSUM MANIFEST CURRENT: 725 files` |
| `scripts/generate_projections.py --check` | PASS: 39 outputs, 0 differences |
| `scripts/build.py` | `Built 288 HTML files from 143 controlled page specs`; `git status` clean afterwards |
| `scripts/audit_public_literals.py` | `records=12760 unresolved=0` |
| `scripts/validate.py` | `HTML=288 ERRORS=0 WARN=0`, PASS |
| `scripts/tests/test_public_tools.py` | PASS 25/26; 1 SKIP (no comparable record ID contains `+`) |
| `audit/tranche_c/checks/viewport_acceptance.py` | `168/168` pass |
| `audit/tranche_c/checks/bilingual_invariance.py` | `0 page pairs with differing numbers (143 pairs checked)` |

Other CI gates from CONTRIBUTING §5, all passing:

- generator unit tests (21 OK);
- `repository_manifest.py --check` (725 files, 18 classes);
- literal-audit determinism;
- source-lineage truth test (8/8);
- `architecture_diagrams.py --check`;
- `handoff_inventory.py --check`.

Harness check: a copy of `dist/` placed at `design/reference/out` passed `YFIE_SITE_DIR=design/reference/out` for both the
public-tools suite and the invariance check, and it stayed out of the checksum manifest (git-ignored).
