# Signature visual candidates (addendum §21–22)

**Status:** `VERIFIED_BY_CLAUDE_TEAM` · `INDEPENDENT_OPENAI_ACCEPTANCE_REQUIRED`

## 1. Verdicts

Each of the six candidates was evaluated against the existing 36 contracts on seven criteria:
- unique value;
- evidence availability;
- risk of overclaiming;
- overlap with the existing 36;
- mobile and RTL cost;
- maintenance;
- the deletion test.

The directive prefers refining or merging over adding.

| # | Candidate | Overlap | Evidence | Overclaim risk | Verdict |
|---|---|---|---|---|---|
| 1 | System + evidence map | **VIS-INCLUSION-TRANSMISSION** is exactly this: a layered system map, evidence state per link, no score | Adequate (per-link states) | Medium if links get arrows of effect; controlled by the contract | **ALREADY ADEQUATE. No new visual.** English description corrected (PB-0465). |
| 2 | Evidence clock | **VIS-EVIDENCE-FRESHNESS** (vintage by domain and class) plus **VIS-DEMAND-VINTAGE-LADDER** (per function) | Adequate | Low | **ALREADY ADEQUATE. No new visual.** The clock is named in prose on /methodology/ (PB-0611). The ladder stays table-only until contracted (PB-0401). |
| 3 | Coverage matrix | None among the 36 | Adequate: 34 dimensions, each with a Master basis (`INDICATOR_COVERAGE_MATRIX.csv`) | **High as a chart** (a heat grid reads as a score or league table) | **ACCEPTED AS PROSE, NOT A CHART.** The public form is the /methodology/ coverage section (PB-0611). The full matrix stays a governance instrument for the measurement agenda. A matrix chart is **rejected** (score-like; §23). |
| 4 | Rule/rail → operation → access → use → quality → outcome ladder | **RV-CWR-009** and **VIS-PAYMENT-RAILS** | Upper links only | High if lower nodes are filled | **REJECTED as new.** It duplicates RV-CWR-009, which already leaves unmeasured nodes open. |
| 5 | Transfer → persistent-use pathway | **RV-CWR-010** | Delivery and exposure only (G2Px) | High if persistence is implied | **REJECTED as new.** It duplicates RV-CWR-010; the G2Px paragraph is restored instead (PB-0360/0361). |
| 6 | Financial-needs / function lens | Partly **VIS-DEMAND-VINTAGE-LADDER**, CLM-031 | 2014 values; 2021 variables not computed | **High:** a function wheel would present 2014 behaviour as current | **REJECTED.** Revisit only after MA-001 produces current weighted values. |

**Tally:**
- 2 are covered by existing contracts (#1, #2);
- 1 is accepted in prose form only (#3);
- 3 are rejected (#4, #5, #6).

Zero new visual contracts.

## 2. Visual-semantics contract for Design (addendum §21)

Every visual must encode each evidence state, and each state keeps a distinct treatment across all charts. Colour is never the only carrier; label and pattern must also mark the state.

| State | Meaning | Required treatment |
|---|---|---|
| MEASURED | Observed by the source for its universe | Solid mark; label with date |
| DERIVED | Calculated reproducibly from measured inputs | Solid mark plus "derived" tag; precision equal to the inputs |
| HISTORICAL | Measured, but older than the current clock for its domain | Year label always visible; never joined to current points |
| ADMINISTRATIVE | A count kept by an institution (accounts, terminals, lists) | Unit label names the counted object ("accounts", not "people") |
| PROGRAMME | A programme or project population or target | "Programme universe" badge |
| ESTIMATED | Source estimate, not an observation | Hollow or dashed mark plus "estimate" |
| PROJECTED | Forecast | Dashed line, separated from history |
| PARTIAL | Defined but incomplete (e.g. one side of a pair) | Label "incomplete"; no gap drawn |
| UNKNOWN / NOT MEASURED | No evidence | Neutral hatch plus "not measured". **Never zero.** |

**Cross-cutting encodings:**
- **Evidence clock:** every value shows its observation or fieldwork date.
- **Universe:** every axis or card names its population or counted object.
- **Currentness:** a historical value may never sit on the same line as a current one.
- **Transmission stage:** rule / rail / operation / access / use / quality / outcome.
- **Source role:** primary / status event / secondary (attributed) / context.
- **Measurement gap:** open nodes link to their MA item.
- **Breaks:**
  - vintage breaks (remittances);
  - universe breaks (e-wallet subscribers);
  - publication gaps (POS value, September 2025).

  Each is a visible break in the line, never a splice.
