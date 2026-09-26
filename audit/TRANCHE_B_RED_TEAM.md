# Tranche B red team and independent verification

**Status:** `VERIFIED_BY_CLAUDE_TEAM` · `INDEPENDENT_OPENAI_ACCEPTANCE_REQUIRED`

Red-team and verifier output is analyst input, not approval. The Lead accepted, re-severed or rejected each item on repository bytes. The record below includes the challenges that were rejected and the Lead's own errors.

## 1. Who challenged the work

| Layer | When | Scope |
|---|---|---|
| Specialist waves (10 reports) | Tranche B, before this window | Readings, Measurement, visuals, Arabic, English, search, trust; findings summarised in the continuation handover §6 |
| Red-team panel: 11 personas across 3 agents | Tranche B, before this window | Hostile-but-fair challenge from citizen, journalist, CBY regulator, bank, MFI/MFB, payment provider, exchange/remittance provider, researcher/academic, IFI/DFI professional, humanitarian/donor and source-owner perspectives |
| Lead byte-verification | Previous window and this window | Every load-bearing candidate, checked against `dist/`, projections and the Master |
| Independent verifier 1 | This window | The 432-row spec: current values, number provenance, source bindings, parity, overclaim, structure |
| Independent verifier 2 | This window | 243 rows added in the final pass, plus a 30-row random sample of the terminology sweeps |

## 2. Persona lens → verified defect → disposition

The persona mapping below is the Lead's consolidation of the panel's challenges as recorded in the handover. It is not a verbatim transcript.

| Persona lens | Challenge | Verified? | Disposition |
|---|---|---|---|
| Journalist | "Your OECD numbers for Yemen: where are they in the report?" | **Yes.** The project's own verification record could not confirm 15/100 and 42/100. | LEAD-B08: scores withdrawn; participation stated; PRIMARY_SOURCE_PENDING |
| Journalist / researcher | "You call IMF estimates 'observed history' and splice two documents." | Yes: `HISTORICAL_REPORTED`; two vintages | LEAD-B06 |
| Source owner (World Bank / IMF) | "The 'source verification path' lists sources that are not behind this record." | Yes: 4 contaminations; closure stamped on 108/108 | LEAD-B07: object-level lineage |
| CBY regulator | "Whose list is this? The English drops the authority-scope limit that the Arabic carries." | Yes: CLM-008 parity; unqualified "official CBY roster" | LEAD-M01, LEAD-M02 |
| MFI / MFB | "33.379 → 44 billion reads as growth; the rial lost half its value." | Partly. Nominal and USD differ, **but** the rial valuation basis is not recorded and no price deflator is sourced. | LEAD-B01 re-severed (directive correction A): nominal plus rate context, no USD or real change |
| Bank | "Microfinance is a tiny share of our credit." | The ratio cannot be computed safely (overlap, basis, date) | LEAD-B03: formal credit published separately, **ratio rejected** (directive correction B) |
| Researcher / academic | "Your gaps need standard errors, and the 3.37× ratio needs an interval." | The design-based variance is not available | LEAD-M04: **model SE/CI rejected** (directive correction C); limitations stated |
| IFI / DFI | "Put 11.9%, 3.3 million and 1.44 million on one denominator." | Incompatible universes | LEAD-M10: **denominator rejected** (directive correction D); incompatibility published |
| Payment provider | "Registration is not use, and you do not show the subscriber series." | Yes: Tranche A CHG-0017 | PB-0521, with the series break |
| Exchange / remittance provider | "Our sector is absent from the access page." | Yes (DOM-ACC-01) | PB-0522, using the binding-correction #4 wording |
| Citizen | "Is 11.9% true today? Is 'borrowing was widespread' true today?" | Currentness risk in undated titles | PB-0572–0574; the evidence-clock framing is kept |
| Humanitarian / donor | "Delivery is not persistence, and the G2Px paragraph is missing." | Yes: CWR-010 rendered section lacks it | PB-0360/0361 |
| Source owner (CBY) | "Decision 18/2026 is missing." | The event is verified; names are pending | PB-0518/0519, PRIMARY_SOURCE_PENDING |

## 3. Lead byte-verifications (spot list)

**From the handover §9, re-confirmed where used:**
- "3.3 million active savers" is live on /finance/;
- 792.69 and 1,529.4 appear in `cby_monetary`;
- "1,679" occurs 0 times in dist;
- "observed history" appears ×4;
- «عدن» appears ×2 on AR /providers/;
- `source_dependencies` in the projection is 108/108 empty;
- "9.00" occurs 0 times;
- the a11y flag is `true` on 141/141 with 0 `<svg>`/`<table>`/`<figure>`;
- the FMIIP values are held but unpublished;
- `global_navigation` has no `children`;
- build.py: the strapline is at line 65, `desc` at line 1224, «المنظومة» at line 664.

**New this window:**
- the Master holds 48 bound objects (not 0);
- the Findex "not verified" block sits in the Master (25 r14–35);
- the CWR-010 paragraph exists in 09 but not in the rendered 03;
- 65 «ادعا…» occurrences in 62 cells;
- /measurement/ ships a design instruction;
- 13 VISUAL records publish instructions as summaries, and 12 have placeholder universes;
- 22 and 26 hold titled sub-blocks;
- the search probe finds 0 results for "law" (EN) and «لائحة» (AR).

## 4. Rejected or re-severed — with reasons

| Item | Source of the proposal | Decision | Reason |
|---|---|---|---|
| "FX-deflated −31.7%, sign reversal" | Handover LEAD-B01 | **Rejected** | A USD conversion is not real deflation, and the valuation basis is not recorded |
| "≈2.6% of private credit" | Handover LEAD-B03 | **Rejected** | Overlap risk (12 MFBs on the bank list); stock, date and valuation incompatibilities |
| SE≈2.78, p≈0.16, ratio CI [2.24, 5.08] | Handover LEAD-M04 | **Rejected** | Model-calculated without the design; would manufacture precision |
| Adult-population denominator | Handover LEAD-M10 | **Rejected** | Not source-defined for this purpose; would imply commensurability |
| "Baseline zero → reform has not translated into use"; publishing the FMIIP zeros | Tranche A CHG-0019 | **Rejected** | Binding correction #3. The zeros are construction artefacts or not yet instrumented; non-zero baselines are published instead |
| "Yemen's largest physical cash-access channel" | Tranche A CHG-0020 | **Rejected** | Binding correction #4 |
| "Absence of a functioning formal credit/deposit channel" | Tranche A §4 system view | **Rejected** | Binding correction #5 |
| Narrow /finance/ to microfinance | Tranche A CHG-0015 | **Rejected** | Binding correction #2 |
| MA-011 household remittances | Tranche A CHG-0018 | **Rejected** | Duplicates MA-001; MA-001 extended instead |
| Populate all 8 domains with Readings | Tranche A CHG-0011 / SYS-01 | **Rejected as mechanical** | Per-pair test gives 11 surfaced and 8 contextual links; /providers/ gets none |
| "MA-003 lists income among not established" (contradiction) | Red team | **Re-severed** | MA-003's causal framing is correct; only the measured level gap was missing |
| "Access to finance ranks 6th" | Tranche A (Lead) | **Withdrawn** | An ordinal claim on multi-response data with no base |
| Reorder /remittances/ to lead with the household thread | Tranche A CHG-0018 | **Rejected** | The only household evidence is from 2014; leading with it invites a currentness misreading |
| Broad issuer-only search alias ("CBY" → all) | Search specialist | **Rejected** | Floods results and empties the term of meaning |
| Move FMIIP and status-event blocks to new sheets | My earlier PB-0342/PB-0517 | **Replaced** | The Master's titled-block design is deliberate (31 blocks); a reader rule (PB-0473) replaces sheet moves |

## 5. Independent verification in this window

**Verifier 1 (432-row spec).**
- All 391 located current values were found exactly.
- All 312 new numbers trace to the Master (0 untraceable).
- All 158 source IDs exist.
- No causal claim, rank, CI, denominator or ratio.
- Findings, all fixed:
  - PB-0007 row count (107, not 106);
  - PB-0342 mischaracterised the block (**Lead error**; corrected);
  - PB-0413 count (65/62);
  - household versus adult framing in PB-0302/0303;
  - PB-0362 classification;
  - 22 editorial rows that changed numbers or units (relabelled);
  - two bad cross-references;
  - seven wording families stronger than the Master (OECD "reports", portfolio-composition assertion, borrower direction, "no CIs published", and others). Each was narrowed to what the Master holds.

**Verifier 2 (243 new rows plus a 30-row sweep sample).**
- 216/216 located current values exist.
- 243/243 numbers trace to the Master.
- 30/30 sweep substitutions are correct and grammatical.
- **30 material findings, all fixed:**
  - the 91.84% base now states the no-need exclusion, in both languages (PB-0583/0584/0583A–E);
  - the Arabic multi-response sum direction is corrected («يتجاوز مجموع النسب 100%»; PB-0351/0456);
  - «المعتمدة» becomes «الموثقة» (PB-0550/0551);
  - CBY-Aden now appears in both languages (PB-0580A/0581A/0585A);
  - the 817/1,021 pairing appears in both the evidence record and the visual (PB-0594/0595);
  - the /firms/ and /access/ headings no longer over-generalise (PB-0520/0522);
  - PB-0519 carries the "suspension ≠ permanent cessation" guard and its full fields;
  - PB-0525 counts (12 of 14) and naming rule corrected;
  - PB-0492/0493 current state corrected, and `document_type`/`evidence_role` columns created with the Resource Library vocabulary;
  - PB-0473 block count (31).
- **23 editorial findings, all fixed.** Among them: the design note now targets the existing "Build grammar" block; PB-0518's card state; Arabic twins for PB-0457/0503; CWR-007 tense and wave; the PB-0575 conditional; «عناصر تحليلية»; «البيانات التاريخية»; CLM-031 Arabic phrasing; English summaries rewritten with verbs; the passport fieldwork dates (PB-0577).
- **Classification:** fieldwork-date, authority, base and title changes relabelled from editorial to BOUNDARY_TIGHTENING or IA_LABEL_CHANGE with `semantic=yes`.

**Not independently certified:** native Arabic certification, legal and rights review, and the primary-source transcriptions (OECD/INFE Yemen row, Decision 18 names, the YPCC registered name).
