# Escalations

Format (README_FIRST §10):
- `ESCALATE_TO_MASTER — <route/object> — <defect> — <design impact>`
- `NEEDS_CONTROLLED_CONTENT — <route/object> — <field> — <design impact>`

Answered by the steward, Master-first. Items are closed, never deleted.

## Open

Raised at D1 (27 September 2026), from the independent lens critique of the propositions (`01_FOUNDATIONS.md` §3), and
reconciled at D2 by their true authority (DL-D2-002). Each was needed by a design actually rendered; none is filled with
authored copy.

- `NEEDS_CONTROLLED_CONTENT — Home (`/`) section 3 — pacing boundaries — the candidate direction paces the governed
  "three figures" paragraph as figure groups, each followed by its bounded record; the split points are found by the
  governed connectives ("In the same survey", "Separately", "These are different measures" and their Arabic
  equivalents), which couples the build to wording. If the direction is accepted, a controlled marker (sentence or
  group boundaries on the section body) lets the build pace without parsing prose. Until then the reference
  implementation may pace only by these connectives and must fall back to the unpaced paragraph when they are absent.`
  D2: Master-first (the section body carries no marker in either language); open, non-blocking; DEBT-008.
- `ESCALATE_TO_MASTER (question, not a defect claimed) — RV-CWR-001 imf_staff_path — evidence state — the series
  carries state REPORTED while the Reading's prose describes the IMF path as a staff reconstruction with a modelled
  personal-transfers component; the source-institution lens asked whether the lane should carry an estimate state.
  Design impact: if the state changes, the IMF lane and the fallback table carry the state label; the drawing does
  not change otherwise.` D2: an evidence-authority question; REPORTED rendered as governed; open, non-blocking.

Raised at D2 (27 September 2026), each needed by a design actually rendered:

- `NEEDS_CONTROLLED_CONTENT — every drawn figure's fallback table (VIS-FINDEX-GAPS, VIS-REMITTANCE-MACRO, the POS
  panels, VIS-PAYMENT-ANATOMY, VIS-REMITTANCE-COST, RV-CWR-001, the chain) — column labels for the group / object,
  the evidence state and the note columns (the value column is headed by the governed unit label) — without them the
  tables ship with empty column headers (DEBT-013); Design ships them empty rather than inventing "Group", "State" or
  "Note".`
- `ESCALATE_TO_MASTER (rows requested) — VIS-TARGET-RESULT-STATE (/reforms/ and its record) and VIS-MFI-DIVERGENCE
  (/finance/) — TABLE_TEXT_FIRST contracts whose rationale describes a table (baseline, target and the absent result;
  the divergence table) but whose contract resolves no rows — the governed TARGET and RESULT markers cannot be drawn
  from the alt text; both render as text frames until rows exist. Design impact: with rows, a three-row table with the
  governed markers; without, the text frame stays.`

## Closed at D2 (27 September 2026) — resolved by an authority the repository already holds

- Arabic credit line (`NEEDS_CONTROLLED_CONTENT — RV-CWR-001 and every visual contract with a credit`): the contract
  answers it — every `credit` carries `language_note` "Publisher names are governed in English only (15, 34); Arabic
  frames print them as isolated left-to-right runs". Every frame now prints the governed credit as an isolated
  left-to-right run. No Master change needed.
- Accessible name for in-page navigation (`NEEDS_CONTROLLED_CONTENT — every page with an in-page index`): resolved by
  accessibility practice without new copy — the index and the strip are named by the `h1` of the object they index
  (`aria-labelledby="page-title"`), each edge group by its own governed heading. DEBT-006 closed. A dedicated governed
  label ("on this page") would read better; it is a preference, not an authority question.
- Home section order (for steward confirmation): decided by the brief — §4.5 states the baseline order "is a
  precedent, not a mandate; keep the `#system` anchor". The Lock item stands; nothing to confirm.

## Anticipated (not yet raised — each will be raised only when a D1+ design actually needs it)

Recorded so no one fills these gaps silently. Source: brief §10, §12, §15.

- External-link accessible cue for original sources (brief §10).
- Result-type facet labels exist (`UI-JS-TYPE-*`); a domain facet needs a governed domain field on search records.
- "Type not recorded" group label for the 9 displayed sources without `document_label` (`/data/`, EAD-07).
- Evidence-workbench facet headings/values (verification state, domain), if a facet is designed.
- Report-issue intent labels, if a richer reporting intent is designed.
- Reuse line and download labels following the licence decision (OWN-04).
- IBM pre-split Latin font subsets (vendoring with provenance).
- Rows for the other TABLE_TEXT_FIRST contracts whose rationale describes a table but resolves no rows (raised at D2 for
  VIS-TARGET-RESULT-STATE and VIS-MFI-DIVERGENCE; the rest as their gate reaches them).

## Process notes (not escalations)

- D1 branch name (2026-09-27): D1 is developed and pushed on `claude/practical-cray-sr26c5`, the branch the execution
  environment is permitted to push, instead of the `design/d1-theses` name planned at D0. One gate, one branch, one pull
  request into `main` still holds; the steward may re-home the branch under `design/` at landing if the convention
  matters for history. No design meaning attaches to the name.

- Tag `checkpoint/design-handoff-ready` was not found at D0 (2026-09-27); commit `6d954c1` used. Steward to confirm.
  Steward, 2026-09-27: confirmed. `6d954c177b5d35cdad063f3a2cef5a92d33e16d4` is the recorded Design-handoff target (`OPENAI_REENTRY_CHECKPOINT.md` §7); the tag is an owner action (tag pushes are refused to the steward's environment). Working from the commit is correct; nothing changes when the tag appears.

- D2 branch name (2026-09-27): D2 is developed and pushed on `claude/epic-cori-60fpeb`, created at the exact accepted
  `main` (`851f496`), instead of the `design/d2-hard-families` name planned at D0; the same convention as D1.
