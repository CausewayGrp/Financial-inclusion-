# Session P3 — Visual design readiness: closure

Programme: Pre-Tranche-C maturation (P1–P4). This session's status: **P3 CLOSED**.
- Tranche C has not been started.
- This is not DESIGN HANDOFF READY and not PUBLIC RELEASE READY.
- The static baseline draws no chart.

**Method.**
- Two specialist analyses ran in parallel, read-only: a data-binding audit of all 36 contracts against the current Master
  (J/B), and a red team of the signature candidates (K, with E and H lenses). They are filed as non-authoritative inputs
  in `audit/pre_tranche_c/specialist_inputs/P3_*`.
- The Lead adjudicated every finding. Truth corrections went into the Master first through the transactional runner.
- Findings P3-F01…F13 and P3-G01 are in `audit/pre_tranche_c/FINDINGS_LEDGER.csv`.
- The design-facing guide is `handoff/VISUAL_DESIGN_CONTRACT.md`.

## 1. State at P3 exit

| Item | P2 exit | P3 exit |
|---|---|---|
| Production Master SHA-256 | `6456add9…47672` | `49cbfe3326e3825714bb47ae7752d4b4b4b8c8e5d45be74a466a77691d3c6286` |
| Page Specs SHA-256 | `96618693…1834` | `8c142f2ec278110fad0216a9fcc5ea8cb9aadfe086bbf6b42a5ea7abe6de0c73` |
| Generator outputs / tests | 39 / 16 of 16 | 40 (new DERIVED `visuals/visual_design_contracts.json`) / 18 of 18 |
| Build / literal audit | 288 HTML / 8,230, 0 unresolved | 288 HTML / 8,296, 0 unresolved |
| Validator | PASS | PASS (new gates P3-G01…G04) |
| Browser behaviour tests | 26 of 26 | 26 of 26 |
| Master structure | 11 has 23 columns | 11 has 25 columns (`period_ar`, `universe_ar` appended; contract updated) |

**Transactions** (ledgers and run reports are in `audit/pre_tranche_c/runs/P3*`):

| Transaction | Master SHA-256 | Cells | Content |
|---|---|---|---|
| P3-A | `ead90829…` | 175 | Contract truth corrections |
| P3-B | `334f801a…` | 35 | Grammar vocabulary, remittance vintage rows, unit on YSC-013 |
| P3-C | `ed85f47b…` | 10 | Two grammar labels, RV-CWR-001 title, six publishers |
| P3-D | `49cbfe33…` | 26 | Arabic scope for twelve visuals |
| P3-E | — | — | Code, contract and test commit; Master unchanged |

## 2. Tiering of all 36 contracts

**Counts:** 3 SIGNATURE, 12 CORE_ANALYTICAL, 12 SUPPORTING, 8 TABLE_TEXT_FIRST, 1 RETIRE_FROM_DESIGN.

The full rationale per visual is in the controlled input and the derived JSON.

| Visual | Tier | Decisive reason |
|---|---|---|
| RV-CWR-001 | SIGNATURE | Stops the likeliest false headline, a same-year restatement read as a 45% collapse. Panel 1 is drawable now; panel 2 is blocked (§5). |
| RV-CWR-009 | SIGNATURE | The rule-to-result chain. It is state-only, drawable, vertical and mobile-native. |
| VIS-PROVIDER-OBSERVABILITY | SIGNATURE | Shows whose list, of what date, and what it proves, with no score. The issuing authority is inside the frame. |
| VIS-FINDEX-GAPS | CORE | Standard bars; the value is the discipline of the frame. |
| VIS-REMITTANCE-MACRO | CORE | Three evidence states and a document break; the scope is now stated (P3-F03). |
| VIS-POS-TERMINALS / -TRANSACTIONS / -VALUE | CORE | One three-panel small multiple. Every flagged month gets the same neutral mark. |
| VIS-PAYMENT-ANATOMY | CORE | Card-first. No totals and no population denominator. Two unvalidated values are withheld. |
| VIS-REMITTANCE-COST | CORE | Small and decision-useful; the send amount is an explicit axis. |
| VIS-FIRM-FINANCE-PATH | CORE | The base is printed at every stage (328 → 31 → 18). |
| VIS-FIRM-CONSTRAINTS | CORE | Multi-response bars with no rank numbers and the base stated as not held. |
| VIS-MFI-DIVERGENCE | CORE | Three lanes of unconnected anchors. RV-CWR-006 reuses it. |
| VIS-TARGET-RESULT-STATE | CORE | The target is always paired with the baseline. The result is UNKNOWN. There is no progress bar. |
| RV-CWR-004 | CORE | The drawable instance of the "evidence clock": asynchronous dated lanes ending in an open outcome node. |
| VIS-E-MONEY-RULE-STACK, VIS-FCP-REDRESS-PATH, VIS-FL-EVIDENCE-LADDER, VIS-EVIDENCE-CLASS-LADDER, VIS-PAYMENT-RAILS | SUPPORTING | State figures whose text already carries the content. VIS-PAYMENT-RAILS should reuse the RV-CWR-009 event set. |
| RV-CWR-002, 003, 005, 006, 007, 008, 010 | SUPPORTING | Reading visuals. Either their values are not held as rows (002, 005, 008 are PARTIAL) or they reuse a core contract (003, 006, 007). |
| VIS-INCLUSION-TRANSMISSION | TABLE_TEXT_FIRST | Not drawable truthfully (§3). |
| VIS-EVIDENCE-FRESHNESS | TABLE_TEXT_FIRST | Not drawable: there are no structured dates. The promotion condition is stated (§3). |
| VIS-EVIDENCE-GAPS | TABLE_TEXT_FIRST | Gap types are not a governed field. |
| VIS-SOURCE-COMPARISON | TABLE_TEXT_FIRST | Already implemented as the Compare tool. |
| VIS-FIRM-FINANCE-SEVERITY | TABLE_TEXT_FIRST | Two percentages in a filtered base; a bar invites a prevalence reading. |
| VIS-OECD-FCP-TIMELINE | TABLE_TEXT_FIRST | State list; it overlaps the redress path on the same page. |
| VIS-MECHANISM-METRIC-BRIDGE | TABLE_TEXT_FIRST | The Master uses 16 relationship types where the contract names 4. |
| VIS-ACCESS-EVIDENCE-LAYER | TABLE_TEXT_FIRST | No map may be drawn from lists until MA-005 evidence exists. |
| VIS-CAPITAL-CONTEXT | RETIRE_FROM_DESIGN | Its data are governed HUMANITARIAN_CONTEXT_ONLY / "backend/context only". |

## 3. Signature candidates tested

| Candidate | Result | Evidence |
|---|---|---|
| VIS-INCLUSION-TRANSMISSION | **Failed; now TABLE_TEXT_FIRST** | See below. |
| VIS-EVIDENCE-FRESHNESS | **Failed (not drawable); now TABLE_TEXT_FIRST** | See below. |
| VIS-PROVIDER-OBSERVABILITY | **Kept SIGNATURE** | See below. |
| VIS-FINDEX-GAPS | **CORE** | Drawable and truthful, but a standard form. Its period framing was wrong and is fixed (P3-F02). |
| Remittance vintage/break (VIS-REMITTANCE-MACRO, RV-CWR-001) | **RV-CWR-001 SIGNATURE; MACRO CORE** | RV-CWR-001 is the more distinctive and decision-critical, and its values are now rows (P3-F11). MACRO's scope was missing from its frame (P3-F03). |
| Payments contradiction/gap (the POS three) | **CORE, as a small multiple** | Making the source's percentage mismatch the headline reads as a gotcha against the source, so every flagged month gets the same neutral mark instead. The endpoint framing hid the July 2025 high (P3-F04). |

**VIS-INCLUSION-TRANSMISSION.** Sheet 13 holds relationship statements, not evidenced links:
- 21 of 26 links carry no reference;
- no link carries an evidence strength;
- SL-011…021 are measurement, placement and navigation links, not system relationships.

The contract promised "the evidence state marked on each link", which the data cannot deliver. The contract is corrected
(P3-F07) and the visual is rendered as the ordered list SL-001…010 and SL-022…026. Home keeps its governed position, since
R8.4A is not reopened.

**VIS-EVIDENCE-FRESHNESS.** It cannot be drawn from the current Master:
- periods are free text (97 strings);
- there are no separate observation, fieldwork, publication or retrieval dates;
- retrieval dates are held for 1 of 159 sources.

The contract text is kept as a statement of intent. The data promotion needed is stated in `promotion_requires`.

**VIS-PROVIDER-OBSERVABILITY.**
- Every dimension binds to governed rows in 22.
- Missing dimensions are UNKNOWN, meaning "none held", not "none exist".
- CBY-Aden scope is in the frame (UI-VIS-ISSUER-SCOPE).
- Known gap: there is no provider-universe row for payment-system operators, so that row is UNKNOWN with dated institution events as context.

The red team proposed RV-CWR-009 as the Home signature. The Lead decision is: **not adopted in P3**. Home's governed binding
belongs to the closed R8.4A. RV-CWR-009 is designed as a signature on its Reading, and moving it to Home is a governed
change for Design to propose, Master-first.

## 4. Semantic visual grammar

The machine-readable grammar is in the derived JSON (`grammar`, `grammar_labels`). All 33 labels are governed
bilingual interface copy (`UI-VIS-*` in Master 04).

**Evidence states.** The directive's nine states, plus REPORTED for official statistics that are neither a survey
measure nor an administrative count (the IMF reported history, the SFD tables):

| State | Carrier |
|---|---|
| MEASURED | Filled mark, solid line, direct label on first use |
| REPORTED | Filled mark, solid line |
| ADMINISTRATIVE | Filled square mark, solid line |
| DERIVED | Bracket or difference annotation, never a bar of its own |
| HISTORICAL | Period printed on the mark; no fading |
| PROGRAMME | Outlined mark inside a labelled programme frame |
| ESTIMATED | Hollow mark |
| PROJECTED | Hollow mark, dashed line |
| PARTIAL | Half-filled mark with the universe printed beside it |
| UNKNOWN | Empty cell carrying the word; never a zero-height bar |

**Structure markers:**

| Marker | How it is drawn |
|---|---|
| BREAK_VINTAGE | The line stops; a labelled gap names both documents |
| BREAK_UNIVERSE | The line stops at a labelled rule |
| SAME_YEAR_REVISION | Both values at one axis position |
| MISSING | Labelled gap; never interpolated, never zero |
| DISAGREEMENT | Neutral † on **every** flagged period, both figures in the note |
| TARGET | Outlined marker; no progress bar unless compatibility is governed as direct |
| RESULT | Filled marker, or UNKNOWN |
| NOT_COMPARABLE | Separate panels or axes with the label between them |
| NOMINAL | On the axis title |

**Chain.** The chain runs rule → implementation → operation → access → use → quality → outcome, top to bottom in both
languages. Each step is EVIDENCED or OPEN, and OPEN is labelled "not yet measured — not a failure".

Lead decision: **activity counts (transactions, values) evidence OPERATION, not USE**. USE needs a person- or firm-level
measure. This closes the red team's open question on where transactions sit.

**Carriers.** Colour is never the only carrier. There is no red, amber or green, and nothing fades by age.

**RTL decision (Lead).** Numeric time axes run **left to right in both languages**. Text, legends, panel order and
categorical bars follow the reading direction. This supersedes the line "axes, time lines and ladders mirror" in
`audit/VISUAL_CONTRACT_CLOSURE.md` (Tranche B), which is historical and not rewritten. The reason is that bilingual crops
circulate side by side, and a mirrored rising line reads as a fall. This is a design rule to be tested with Arabic
readers; it is not a claim about Arabic convention.

## 5. Data contracts (SIGNATURE and CORE)

Every data contract resolves its rows from the Master at generation time, with guards. It gives each value a grammar state
and markers, and records the missing periods. Derived differences are checked against the governed values (12.91 and 9.0
percentage points). Each contract also carries:
- the drawing rules: form, ordering, transformation, missing, breaks, annotation, mobile, RTL and fallback;
- the governed credit line;
- the bilingual detached caption;
- blockers.

The validator (P3-G01) requires every field.

**Examples of what the guards now enforce:**
- the POS value series has exactly one governed gap (2025-09);
- the IMF line breaks exactly at RMO-IMF-2025-REV;
- the POS transaction count (58,512) and the payment accounts (5,202,019) are **withheld**, because their governed
  caveat requires a methodology note before public use;
- the 2030 access-point target (1,021) cannot resolve without its January 2025 baseline (817).

**Open blockers** (a visual may be designed but not released while one is open):
1. **RV-CWR-001, panel 2** (indexed paths, 2021=100): the CBY AR2025 values for 2021–2023 are not held. Closing it needs
   a primary read of SRC-CBY-AR2025-BOP. If panel 2 is not drawn, the accessible summary must be amended Master-first,
   because it describes both panels.
2. **RV-CWR-009**: the REF-PAY-001 event's locator has no source record. This is the same gap as VIS-PAYMENT-RAILS'
   BOUND_PARTIAL lineage.

**Language note.** Publisher names are governed in English only (15, 34). Arabic frames print them as isolated
left-to-right runs. Arabic publisher names belong to the corpus-metadata work (P2-F10).

## 6. Truth corrections made Master-first

| Finding | Correction |
|---|---|
| P3-F01 | Four contracts carried another visual's evidence_strength or freshness_profile. VIS-CAPITAL-CONTEXT had the remittance-vintage text (Tranche B PB-0180 landed on the wrong row), VIS-FIRM-CONSTRAINTS had "2025-Q3", VIS-FIRM-FINANCE-SEVERITY had the Findex caveat, and VIS-FCP-REDRESS-PATH had "2021→…". Each is reset from its own period or source class. |
| P3-F02 | VIS-FINDEX-GAPS: "2022 observation" collapsed the reporting year, study wave and fieldwork. It is aligned to CLM-001's governed period, universe and currentness. The title no longer says "who is being left behind" (present tense) or «الوصول» (access for ownership). |
| P3-F03 | IMF remittance series: its universe now states the IMF analytical scope for IRG areas (from CLM-036/042). "Observed 2018–2024" becomes "reported history (staff calculations)" in CLM-007, EP-REMITTANCE-MACRO and the visual. The currentness no longer says "bounded to 2018–2030" (projections are not current evidence). |
| P3-F04 | POS titles: "Footprint Pulse" implied reach, "Usage Pulse" implied people, and the value series now says "nominal". The transactions summary names the July 2025 high (27,187). |
| P3-F05 | Arrows between numbers in Arabic text were replaced with words. |
| P3-F06 | Research-tool artefacts ("web ref turn…") were removed from 20 governed source locators. |
| P3-F07 | The system-map contract now describes what the data support. SL-019 and SL-022…026 now reference registered objects. |
| P3-F08 | RV-CWR-006 asserted divergence against its own thesis, and RV-CWR-001 said "baselines". Both titles are corrected. |
| P3-F09 | "Manipulation" is removed from the boundary copy about a named official source (CLM-034, /remittances/). The method-scrutiny boundary is kept. |
| P3-F10 | 56 provider dates were stored as untyped Excel serials and are written as the ISO dates they encode. |
| P3-F11 | The two CBY vintage values for 2024 are promoted from governed prose into data rows, and the unit is added to YSC-013. |
| P3-F12 | Six CBY sources cited by RV-CWR-009 events receive the publisher the Master already uses for cby-ye.com documents. No other bibliography is added. |
| P3-F13 | Arabic period and universe are added for the twelve visuals without an Evidence Record. The Arabic text alternative now carries the same scope line as English on all 18 rendered visuals (it did on 6). |
| P3-G01 | 33 governed grammar labels, EN/AR (31 in P3-B, 2 in P3-C). |

## 7. Adjudication of specialist recommendations not adopted

| Recommendation | Lead decision | Reason |
|---|---|---|
| Merge duplicate reform events (REF-PAY-006/010, 007/013) in 31 | **Deferred** | The data contract deduplicates by date and source item. A Master merge touches lineage and closure and is not needed for truth. |
| Drop the "2021 baseline" node from VIS-OECD-FCP-TIMELINE | **Deferred** | It may be OECD 2021 context rather than an error; that needs a source check. The visual is TABLE_TEXT_FIRST meanwhile. |
| Relabel 33 DA-023/024 and XW-FMIIP-005 | **Deferred** | These are analytics hygiene. No SIGNATURE or CORE contract binds them. |
| Apply the cby-ye.com publisher to all 51 CBY-hosted sources | **Deferred to P2-F10** | Only the six a signature needs were done. The same rule can be applied in the corpus-metadata work. |
| Label the IMF 2018–2024 values "staff calculations" in frame | **Adopted** | Via P3-F03 and the REPORTED state. |

## 8. What P3 did not do

- **No chart was drawn and no SVG was added.** P3-G02 enforces this.
- **No accessibility conformance is claimed.**
- **No Arabic text was certified by an external native editor.** The Arabic added in P3 (33 labels, 24 scope strings and
  the corrected titles) is Lead-authored in the product's register.
- **No primary source was re-read.** Every correction derives from other governed Master fields.

**Next session: P4** covers canonical handoff alignment, the Reading ownership rule, the limitations architecture,
design-prompt drift, hygiene, the acceptance matrix and packaging.

---

## Erratum (added in P4; the text above is unchanged)

- **§3, VIS-INCLUSION-TRANSMISSION.** "the visual is rendered as the ordered list SL-001…010 and SL-022…026" describes
  what Design renders. The static baseline shows the governed text alternative only; it does not print the SL list. The
  controlled-input rationale now says so, and the Master summary no longer describes a map (P4-D, finding V-D7).
- **Chart labels.** P3 left category, series, lane, unit, event and state values without governed Arabic labels. P4-E adds
  101 governed labels and a generator rule that stops on an unlabelled printed value (finding V-D5).
- **VIS-MFI-DIVERGENCE.** The lane values now carry their own id, unit and markers (finding V-D6).

See `audit/P4_CANONICAL_HANDOFF_ALIGNMENT.md` §7.
