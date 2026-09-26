# Visual contract closure — the 36 governed contracts

**Status:** `VERIFIED_BY_CLAUDE_TEAM` · `SPEC_PENDING_EXECUTION` · `INDEPENDENT_OPENAI_ACCEPTANCE_REQUIRED`

**Result: 10 REFINE · 26 KEEP · 0 MERGE · 0 RETIRE.** Seventeen of the 26 KEEP contracts also receive voice-only editorial rows, which do not change their meaning.

**Reconciliation with the handover.** The handover reported 24 KEEP / 12 REFINE from the specialist wave, with "R1–R17" execution specs. Those specs are not preserved in the handed repository. This closure therefore re-derives every disposition from the Master bytes and the spec rows.
- **REFINE** here means the contract's meaning changes: its unit, universe, period, evidence state, encoding, boundary, or the substance of its detached-use text.
- **Voice-only rewrites** are classed KEEP. Drawing instructions turned into prose with the same meaning fall here.

The two missing REFINE items from the specialist count most plausibly correspond to voice-only rewrites (RV-CWR-002 and 003). Nothing is lost either way: every one of those rows is in the spec.

## 1. Review checklist applied to each contract

The checklist has twelve items:
1. the question answered;
2. data inputs;
3. unit;
4. universe;
5. period;
6. why a visual rather than a sentence;
7. visual family;
8. boundary (prohibited inference);
9. caption;
10. accessible summary, which must stand alone for detached use (screenshot, crop, screen reader);
11. table fallback;
12. RTL and mobile.

**Items 11 and 12 apply to every contract.** Every quantitative contract needs a text-alternative `<table>` under PB-0400 (caption; scoped headers; unit, population and period columns; source line). This is required whether or not Design renders a chart. None renders today (dist has 0 `<svg>`, 0 `<figure>`, 0 `<table>`), so accessibility conformance is `PENDING_DESIGN_IMPLEMENTATION` everywhere. RTL: axes, time lines and ladders mirror; numbers keep LTR digit order; labels come from the governed Arabic fields.

**Binding (PB-0402).** Each governed contract now reaches its own `/evidence/VIS-*/` page, together with its prohibited inferences.

## 2. Dispositions

| # | Visual | Form | Disposition | What changes and why | Patches |
|---|---|---|---|---|---|
| 1 | VIS-REMITTANCE-MACRO | TWO_SERIES_LINE… | **REFINE** | Evidence state becomes "IMF-reported history (staff calculations)", not "observed". The line **breaks** at the 2024→2025 change of document. Title, summary, encoding and form token all change. | PB-0170–0187 |
| 2 | VIS-CAPITAL-CONTEXT | RELATIONSHIP_GRAPH… | **REFINE** | Freshness profile names the two IMF documents instead of "observed/estimate/projection". | PB-0180 |
| 3 | VIS-MFI-DIVERGENCE | THREE_LANE_BOUNDED_ANCHOR | **REFINE** | "Active savers" is quoted and attributed. There is no trend verb ("fell from" becomes "verified anchors record"). Nominal rials across divided monetary areas: no USD or real change. | PB-0143/0144, PB-0451/0452 |
| 4 | VIS-FIRM-CONSTRAINTS | RANKED_HORIZONTAL_BAR → HORIZONTAL_BAR__MULTI_RESPONSE__NO_RANK_NUMBERS | **REFINE** | Multi-response data (the eight items shown sum to 242%) with no base held cannot support an ordinal rank. The multi-response note travels in both summaries. | PB-0453–0458 |
| 5 | VIS-FIRM-FINANCE-SEVERITY | STACKED_BAR | **REFINE** | "Report-specific finance-filtered base" becomes "among the firms in the report's finance-obstacle tabulation, which excludes firms that said they did not need a loan", so the base, including its exclusion, is named in plain language in both languages. | PB-0583, PB-0583A–E |
| 6 | VIS-FINDEX-GAPS | HORIZONTAL_BAR_WITH_GAP_ANNOTATIONS | **REFINE** | The accessible summary now gives the levels (5.44% / 18.35%) and the income gap (about 9.0 points), as the contract's own "show levels first; annotate gender and income gaps" requires. | PB-0304–0308, PB-0463 |
| 7 | VIS-TARGET-RESULT-STATE | TARGET_RESULT_MILESTONE… | **REFINE** | New pairing rule: the 2030 target of 1,021 is never shown without the 817 baseline for January 2025. The Arabic gains the access-point aggregation clause and loses the calque «الكون». | PB-0594/0595, PB-0469 |
| 8 | RV-CWR-006 | READING_DECISION_VISUAL | **REFINE** | Anchors, not divergence (LEAD-B01). The drawing instruction is rewritten. | PB-0137–0139, PB-0435, PB-0444 |
| 9 | RV-CWR-007 | READING_DECISION_VISUAL | **REFINE** | Levels before the gap in both languages. | PB-0436, PB-0445, PB-0449/0450 |
| 10 | RV-CWR-008 | READING_DECISION_VISUAL | **REFINE** | The English gains the seven-governorate scope that the Arabic already states. | PB-0437, PB-0446 |
| 11 | VIS-POS-TERMINALS | LINE_WITH_CONTRADICTION_NOTE | KEEP | Strong contract: it keeps the source's +11% beside the +8.55% implied by the raw totals. Lineage binds to the 11 monthly releases only (PB-0010). | voice PB-0467 |
| 12 | VIS-POS-TRANSACTIONS | LINE_WITH_CONTRADICTION_NOTE | KEEP | As #11 (+4.9% displayed vs about +13.87% implied). | voice PB-0468 |
| 13 | VIS-POS-VALUE | LINE_WITH_EXPLICIT_GAP | KEEP | Nominal YER; the September 2025 gap stays a gap. | AR calque PB-0539 |
| 14 | VIS-PAYMENT-ANATOMY | METRIC_ANATOMY_CARDS | KEEP | Cards, accounts, subscribers, terminals and transactions stay separate objects. | AR calques |
| 15 | VIS-E-MONEY-RULE-STACK | REGULATORY_STACK… | KEEP | Rules are not usage. | voice PB-0460 |
| 16 | VIS-PAYMENT-RAILS | STATE_TIMELINE_WITH_DEPENDENCIES | KEEP | Milestone is not adoption. The YPCC Arabic name is corrected where it appears (PB-0230). | AR calque PB-0550 |
| 17 | VIS-FCP-REDRESS-PATH | TIME_BOUND_RECOURSE_PATH… | KEEP | Path of 10 and 14 business days, with the outcome node open. | voice PB-0462 |
| 18 | VIS-OECD-FCP-TIMELINE | STATE_TIMELINE… | KEEP | States kept separate. It carries no OECD/INFE Yemen score (LEAD-B08 check: 0). | voice PB-0466 |
| 19 | VIS-FL-EVIDENCE-LADDER | EVIDENCE_LADDER_WITH_OUTCOME_GAP | KEEP | The population-capability rung has **no Yemen value** until the OECD/INFE row is transcribed (binding note in PB-0027; the OECD row itself is PRIMARY_SOURCE_PENDING under PB-0108). | voice PB-0464 |
| 20 | VIS-PROVIDER-OBSERVABILITY | OBSERVABILITY_MATRIX… | KEEP | No confidence score. Authority is a dimension of its own. | — |
| 21 | VIS-ACCESS-EVIDENCE-LAYER | LAYERED_MAP_PLUS_GAP_STATE | KEEP (method contract) | Points appear only with a verified source, observation date, operating-status date and permitted resolution. Unobserved geography is "unknown", never zero. **No operating-provider map may be drawn from lists** (§23 forbidden object) until MA-005 evidence exists. | — |
| 22 | VIS-INCLUSION-TRANSMISSION | LAYERED_SYSTEM_MAP… | KEEP | This is the product's system map, with an evidence state on each link and no composite score. It satisfies the addendum's "system + evidence map" candidate (`SIGNATURE_VISUAL_CANDIDATES.md`). | voice PB-0465 |
| 23 | VIS-EVIDENCE-FRESHNESS | EVIDENCE_FRESHNESS_SKYLINE… | KEEP | This is the "evidence clock". | voice PB-0461 |
| 24 | VIS-EVIDENCE-CLASS-LADDER | EVIDENCE_CLASS_LADDER… | KEEP | — | AR calque |
| 25 | VIS-EVIDENCE-GAPS | GAP_MATRIX_AND_TIMELINE | KEEP | Typed gap states, not a score. | AR calque PB-0536 |
| 26 | VIS-MECHANISM-METRIC-BRIDGE | LINKED_MECHANISM_TO_METRIC… | KEEP | Inference badges; qualitative evidence never becomes prevalence. | AR calques |
| 27 | VIS-SOURCE-COMPARISON | SIDE_BY_SIDE_DEFINITION_COMPARE | KEEP | Supports the new "three numbers that cannot be combined" section (PB-0345). | — |
| 28 | VIS-FIRM-FINANCE-PATH | FUNNEL_PLUS_CONDITIONAL_COMPOSITION | KEEP | 31 of 328 firms had a line of credit; 18 valid loan-source responses. It is never drawn as a population funnel. | — |
| 29 | VIS-REMITTANCE-COST | GROUPED_DOT_OR_BAR… | KEEP | Corridor and amount stay explicit (2025 Q3). | voice PB-0459 |
| 30 | RV-CWR-001 | READING_DECISION_VISUAL | KEEP | The summary was already prose; `what_it_shows_en` is rewritten. | PB-0430 |
| 31 | RV-CWR-002 | READING_DECISION_VISUAL | KEEP | Voice only. | PB-0431, PB-0440 |
| 32 | RV-CWR-003 | READING_DECISION_VISUAL | KEEP | Voice only. | PB-0432, PB-0441 |
| 33 | RV-CWR-004 | READING_DECISION_VISUAL | KEEP | Voice only. | PB-0433, PB-0442 |
| 34 | RV-CWR-005 | READING_DECISION_VISUAL | KEEP | Voice only. | PB-0434, PB-0443 |
| 35 | RV-CWR-009 | READING_DECISION_VISUAL | KEEP | Voice only. | PB-0438, PB-0447 |
| 36 | RV-CWR-010 | READING_DECISION_VISUAL | KEEP | Voice only. | PB-0439, PB-0448 |

## 3. The 13 VISUAL-class evidence records with no contract

These are VIS-BORROWING-SOURCES-2014, VIS-DEMAND-VINTAGE-LADDER, VIS-DOMESTIC-REMITTANCE-PATH-2014, VIS-FINDEX-ACCESS-USE, -BARRIERS, -FLOW-CHANNELS, -OBSERVED-WAVES, -RESILIENCE, -SAMPLE-SUPPORT, VIS-MFI-2014-PANEL, -RUPTURE-LENS, -SPINE and VIS-PROVIDER-TIME.

**Decision (PB-0401).** `NO_GOVERNED_CONTRACT__TABLE_ONLY`: no chart renders until a contract is added to 11 through the Master. The record renders text plus its table alternative. The 36 contracts are **not** extended; adding 13 contracts now would multiply surfaces faster than evidence.

**Text corrections on the same records:**
- the public `summary_en` of all 13 was a design instruction and is rewritten (PB-0500–0512);
- 12 `universe_en` placeholders become real universes (PB-0560–0571);
- three English titles gain their year (PB-0572–0574).

## 4. Rules for the Design recipient

1. **No new chart without a contract row in 11_VISUAL_LIBRARY.** "Governed" means the contract exists in the Master.
2. **The accessible summary is part of the evidence**, not decoration. A chart may not ship if its summary would be false when read alone.
3. **Breaks are drawn as breaks:** a vintage break (remittances), a universe break (e-wallet subscribers, PB-0521), a publication gap (POS value, September 2025).
4. **No composite score, rank, league table, conflict heat map or operating-provider map.** Values from different universes never share an axis.
5. **Re-run the S05.2 320–400px and RTL suite, and the table-contract validator, before claiming conformance.**
