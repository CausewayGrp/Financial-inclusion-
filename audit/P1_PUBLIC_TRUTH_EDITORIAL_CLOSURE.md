# Session P1 — Public truth and editorial integrity: closure

Programme: Pre-Tranche-C maturation (P1–P4). Status of this session: **P1 CLOSED**. Tranche C has not been started. This is
not DESIGN HANDOFF READY and not PUBLIC RELEASE READY.

Every change went Master-first through the transactional runner (`audit/tranche_b_execution/run_stage.py`: snapshot →
install → regenerate → rebind → build → literal audit → validate → generator `--check`, rollback on any failure). Each
transaction's Master ledger and run report are in `audit/pre_tranche_c/runs/`. Findings, with severity, consequences and the
Lead's decision, are in the central ledger `audit/pre_tranche_c/FINDINGS_LEDGER.csv`. Specialist analyses that informed
decisions are filed, as non-authoritative inputs, in `audit/pre_tranche_c/specialist_inputs/`.

## 1. P1.1 — Canonical state re-verified (counts from the projections, not from handoff prose)

| Item | Entry (Tranche B exit) | P1 exit |
|---|---|---|
| Production Master SHA-256 | `4403a353…c6dbd` | `e1f623109871f127ec74a67c912acac344393e811616bc65c34858be57b602d9` |
| Page Specs SHA-256 | `776558e4…20635` | `314a5b4162fe14dd0a3448316e557f4c2355a065ce422c00fcb823b00eda541e` |
| Generator `--check` / tests | PASS / 13 of 13 | PASS / 16 of 16 (3 inventory-contract tests added) |
| Build | 284 HTML from 141 specs | 288 HTML from 143 specs |
| Public-literal audit | v1: 7,521 records, 0 unresolved | **v2**: 8,230 records, 0 unresolved |
| Validator | PASS | PASS (new gates P1-G01…G06, partition rule, derived baselines) |
| Source records | 160 | 159 (duplicate identity retired, P1-C02) |
| Public original locators (http/https) | 151 | 150 |
| Public claims | 59 | 60 (CLM-062) |
| Evidence Records | 108 | 110 (CLM-062, FMIIP-BASELINE-2025-01) |
| Search records | 420 | 423 |
| Chronology events | 24 | 24 |
| Visual contracts | 36 | 36 |
| Readings / Measurement priorities | 10 / 10 | 10 / 10 |

Entry gates were re-run before any change: generator check PASS, tests 13 of 13, build 284, literal audit 0 unresolved,
validator PASS, `sha256sum -c SHA256SUMS.txt` 156 of 156.

Transactions: P1-A `982bd6ae…` (inventory contract, counts, identifiers, duplication) → P1-B `1d0a6cb1…` (lineage, Reading
paths) → P1-C `754daef2…` (held additions) → P1-D `e1f62310…` (chronology, source identity, strict literal audit).

## 2. P1.2 — Public inventory-count contract

**Defect.** `/data/` rendered `{N_CLAIMS}` in both languages (Tranche B spec rows PB-0372/0373 had proposed a placeholder
that nothing resolved) and typed counts that were stale (159 / 158 against 160 / 151). Counts were also typed into Home,
Explore, Measurement and Readings copy and into `build.py`.

**Contract.** `scripts/projection/controlled_inputs/public_inventory_contract.json` declares each count, the projection it
is derived from and the rule. The generator emits `content/public_inventory.json` (DERIVED). Master copy may carry
`{{n:<key>}}`; the generator resolves it in Page Specs, full copy, default meta descriptions and search records, records each
resolution on the section (`resolved_inventory_tokens`), and raises on an unknown key, a key not cleared for public display
or any unresolved template token. Arabic inventory lines use label–value form, so no noun agreement depends on the number.

**Where counts appear now.** Only where a count tells the reader something the page does not already show: the `/data/`
inventory (eight label–value lines, rendered as a definition list) and Home's "View all 11 questions". Decorative counts
("Ten evidence readings…", "Eleven questions…", "The agenda contains ten…", "24 documented events") were removed rather than
templated. The contract proved itself during P1: `/data/` moved to 110 / 60 / 159 / 150 with no copy edit.

**Validation.** P1-G01 no unresolved template token in any public HTML, static data or Page Spec; P1-G02 the contract equals
an independent recount; P1-G03 every resolved token and every `/data/` list value equals the contract; P1-G04 any inventory
count phrase in public text (English or Arabic, digits or number words) must carry the contract value, in digits.

## 3. P1.3 — Duplication audit

| Route (EN / AR exact repeated sentences ≥ 8 words) | Before | After |
|---|---|---|
| /people/ | 11 / 12 | 0 / 0 |
| /finance/, /firms/, /payments/ | 11/11, 9/8, 12/10 | 0/0, 0/1*, 0/0 |
| /remittances/, /providers/, /access/, /reforms/ | 10/9, 7/7, 9/8, 9/7 | 0 / 0 on all |
| /about/ | 1 / 0 | 0 / 0 |
| /, /explore/, /methodology/, /measurement/ | 0 | 0 (one near-duplicate heading fixed on /explore/) |
| /data/ | 15 / 16 | 15 / 17 — per-card source labels; routed to P2.3 (rights presentation) |

\* The Arabic chart text alternative on /firms/ ends with the same sentence as the section. A text alternative is the
chart's non-visual equivalent — a different job — so P1-G06 excludes it; its presentation is a P3 design rule.

Two causes, both fixed at the root. (1) The domain presentation contract placed each band section in a second tier too, so
every boundary rendered twice; tiers now partition the sections (validator rule), the band holds only always-visible
boundaries, each rendered once and in full under its own governed heading, and `/firms/`'s band no longer holds programme
evidence. (2) 03 bodies on `/people/`, `/firms/` and `/finance/` were flattened evidence cards (narrative + claim copy +
summary + chip labels + boundary) that rendered as run-on paragraphs; each was rewritten Master-first to one authored
narrative, keeping every unique fact (3.7% and 6.4% anchors; 1,000 respondents and fieldwork dates; the four-level capability
ladder; USD 54.7 million; the 68.71% / 23.13% split) and aligning `15%` to the source precision `15.0%`. Also fixed: the
Evidence Record hero repeated the summary on every record page; domain visual pills repeated the text alternative's scope;
authored line breaks collapsed into one paragraph everywhere (now one paragraph per line).

## 4. P1.4 — Public identifier policy (PID-1)

Descriptive labels drive every link and card heading. A stable reference is shown only where it aids verification or
citation — the Evidence Record page, the Evidence directory, the Measurement Agenda list (each card anchored at
`#MA-00x`), the Reading verification path and the source directory (where a locator-only source has no other name) — and it
is always labelled «المرجع» / "Reference". No public surface calls an identifier "internal". Removed: the "without needing to
know internal IDs" sentence and ID labels on domain verify links; ID badges on methodology, measurement, explore and Readings
cards; the "immutable ID … release history" wording on `/measurement/`; Reading breadcrumbs now show the Reading's title. The
P0/P1 priority code is kept (governed and explained on `/measurement/`) but relabelled "Priority" instead of "Evidence
sequence". Routes and IDs are unchanged. Gate: P1-G05.

## 5. P1.5 — Source lineage and Reading verification paths

| 06 lineage state | Entry | P1 exit |
|---|---|---|
| BOUND_EXACT | 87 | 92 (CLM-017, CLM-045, DS-QUAL-EVIDENCE closed; CLM-062 and FMIIP-BASELINE-2025-01 new) |
| BOUND_PARTIAL | 6 | 4 (CLM-039, CLM-046, CLM-056, VIS-PAYMENT-RAILS) |
| COMPOSITE — members listed / not listed | 1 / 12 | 4 / 9 |
| SOURCE_NOT_YET_BOUND | 1 | 0 (VIS-PROVIDER-TIME = CLM-009 + CLM-019) |
| FRAMING_NO_FACT | 1 | 1 |

Every closure rests on governed Master evidence (the analyst's evidence was re-checked by the Lead against the Master):
CLM-017's listing page is itself a source record; CLM-045's three named links map row by row (32 QQL-012/013/014) to three
sources; the qualitative register's 20 rows each cite one of 10 sources. CLM-054 printed CBY-Aden market rates without
binding their source — SRC-CBY-001 added. No dataset token was expanded into a source list.

**Readings.** Each Reading now binds the records that carry its propositions and shows the path on its page:
proposition (the governed headline of the record that carries it) → Evidence Record (labelled reference) → that record's
sources, with a path status in governed copy. Result: 9 of 10 Readings close to named sources; **CWR-006 stays partial**
because CLM-056's 91.98% / 82.45% inputs have no governed data row yet (closes after Master-first rows from SRC-SANAA-MF-2020
are verified). The analyst proposed naming locator-less sources by reference; the Lead declined — the publication firewall
(validator S04.1/S04.2) keeps them unnamed — so pages state that such material exists without naming it.

Still open, truthfully shown on each record: CLM-039, CLM-046, CLM-056, VIS-PAYMENT-RAILS (needs a source promotion for
REF-PAY-001) and nine composites whose members are not enumerable from governed text.

## 6. P1.6 — Held additions: final dispositions

| Root | Route | Disposition | How |
|---|---|---|---|
| PB-0521 | /payments/ | APPLIED | CLM-010 extended with the e-wallet subscriber series and its break; bound to /payments/ and /providers/; new section |
| PB-0522 | /access/ | APPLIED | CLM-008 / CLM-009 bound; XW-FMIIP-005 now shows 1,021 only with its 817 baseline (fixes a live breach); new section |
| PB-0345 | /evidence/compare/ | APPLIED | CLM-001 bound; new record FMIIP-BASELINE-2025-01; worked "not comparable" section |
| PB-0520 | /firms/ | APPLIED | New claim CLM-062 (firm financing behaviour, 2022 survey; two omitted working-capital shares added; base caveats) |
| PB-0614 | /methodology/ | APPLIED without numbers | The 15.5% example collided with a raw case share already on the route |
| PB-0160/0161 | /finance/ | REJECTED | A single nominal-rial stock that may not be converted or compared across the valuation change adds little |
| PB-0322 | (CLM-061) | REJECTED | Duplicative of VIS-FINDEX-GAPS and MA-003; CLM-061 not issued |
| PB-0525 | /providers/ | DEFERRED (R8.5) | Needs governed Arabic event text from the source instruments |
| PB-0374 / PB-0470 / PB-0471 | — | → P4.3 / P4.2 | Limitations architecture; Reading-body ownership |

Two new routes (four HTML pages) were added because each is an independently addressable verification object: the FMIIP
baselines were already public on /reforms/ with no record behind them, and the firm-financing evidence is cited on /firms/.

## 7. P1.7 — Chronology restoration assurance

The certified projection AIR-001 restored from (`8d058126…`) was recovered from the Tranche B entry ZIP and archived
(`audit/tranche_b_execution/archive/AIR-001_CERTIFIED_system_chronology_8d058126.json`). **Independent replay: all 24
events equal the certified file field for field, except the one logged governed edit (PB-0415.S119, YSC-020).**

| Event | Result |
|---|---|
| YSC-018, 019, 021, 022, 023 | Verified against the original web source (quoted in `specialist_inputs/P17_chronology_assurance.md`) |
| YSC-016 | Consistent with independent governed CBY exchange-rate data |
| YSC-020 | Synthesis rule; no source to verify |
| YSC-014, 015, 017 | Not verifiable here (IMF Country Report 26/80 unreachable); YSC-014 in tension with another IMF soundness panel and its unit unstated — **open; primary read required before release** |

Fixed: YSC-019 now states that an agreement to deposit is not a deposit or a disbursement; YSC-018 cites the titled record for
its World Bank implementation report (the untitled duplicate identity was retired); the Arabic FMIIP name matches its source
card; YSC-023 calls the IMF document a press release; the chronology catalog row describes the sheet as it stands.

## 8. Strict public-literal audit (v2)

The literal audit is the main public-truth gate. v1 matched numbers as substrings ("26" inside "2026") and passed every
number in a paragraph containing words such as "records" or "source". v2 classifies each number on token boundaries: date or
period part; identifier; contract-derived inventory count; present in a bound record whose lineage reaches a source (exact,
partial with its state shown, or composite with listed members); on a Reading page, present in a record the Reading binds;
or an explicitly allowed tool constant (`scripts/literal_audit_allowances.json`, one entry: Compare's 2–4 records). Before the
switch-over v2 found three live gaps — the /reforms/ FMIIP baselines, the /providers/ wallet counts and the CWR-010
45,460 figure — all closed through governed records.

## 9. Not claimed

No native-speaker Arabic certification, legal review or primary-source verification beyond what is recorded here and in the
P17 input. External repository copies remain `EXTERNAL_REPOSITORY_SYNC_PENDING`.
