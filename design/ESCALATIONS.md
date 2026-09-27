# Escalations

Format (README_FIRST §10):
- `ESCALATE_TO_MASTER — <route/object> — <defect> — <design impact>`
- `NEEDS_CONTROLLED_CONTENT — <route/object> — <field> — <design impact>`

Answered by the steward, Master-first. Items are closed, never deleted.

## Open

None raised at D0. No controlled-truth defect was found during read-in.

Raised at D1 (27 September 2026), from the independent lens critique of the propositions (`01_FOUNDATIONS.md` §3).
Each was needed by a design actually rendered; none is filled with authored copy.

- `NEEDS_CONTROLLED_CONTENT — RV-CWR-001 (and every visual contract with a credit) — Arabic credit line — the
  projection carries one credit string (`credit.text`, English: "IMF / Yemeni authorities; Central Bank of Yemen —
  Aden; International Monetary Fund"), so the Arabic edition's figure frame prints an English credit while the same
  institutions appear in Arabic in the Sources section. Design renders the governed string as given; the steward
  decides between an Arabic credit string and a rule that credits keep the source's language.`
- `NEEDS_CONTROLLED_CONTENT — Home (`/`) section 3 — pacing boundaries — the candidate direction paces the governed
  "three figures" paragraph as figure groups, each followed by its bounded record; the split points are found by the
  governed connectives ("In the same survey", "Separately", "These are different measures" and their Arabic
  equivalents), which couples the build to wording. If the direction is accepted, a controlled marker (sentence or
  group boundaries on the section body) lets the build pace without parsing prose. Until then the reference
  implementation may pace only by these connectives and must fall back to the unpaced paragraph when they are absent.`
- `ESCALATE_TO_MASTER (question, not a defect claimed) — RV-CWR-001 imf_staff_path — evidence state — the series
  carries state REPORTED while the Reading's prose describes the IMF path as a staff reconstruction with a modelled
  personal-transfers component; the source-institution lens asked whether the lane should carry an estimate state.
  Design impact: if the state changes, the IMF lane and the fallback table carry the state label; the drawing does
  not change otherwise.`

- `NEEDS_CONTROLLED_CONTENT — every page with an in-page index (Record question index, Home and Reading section
  index, the verification spine) — accessible name for the in-page navigation ("on this page" / "contents" in both
  languages) — without it the index and spine are unnamed navigation regions (DEBT-006); Design ships them unnamed
  rather than inventing the label.`

Noted, not escalated (governed formats Design does not reword): the record period label ("Mar-2025–Jan-2026" in
English, "مارس 2025 – يناير 2026" in Arabic) against the prose "March 2025 to January 2026"; ISO dates inside period
strings ("2022-11-07") against the prose "November 2022" — Design isolates them as unbroken left-to-right runs; the
external-link glyph "↗" inside the governed Arabic label "افتح المصدر الأصلي ↗" is not mirrored — a label matter for
the steward if a mirrored glyph is wanted. Two number-format drifts the lenses raised ("6245" beside "3,422.16" in the
fallback table; "118.0" on a chart against "118" in its table) were renderer formatting faults, fixed in the composers
(one formatting rule: thousands separators on every value, years unseparated, precision as governed).

## Anticipated (not yet raised — each will be raised only when a D1+ design actually needs it)

Recorded so no one fills these gaps silently. Source: brief §10, §12, §15.

- External-link accessible cue for original sources (brief §10).
- Result-type facet labels exist (`UI-JS-TYPE-*`); a domain facet needs a governed domain field on search records.
- "Type not recorded" group label for the 9 displayed sources without `document_label` (`/data/`, EAD-07).
- Evidence-workbench facet headings/values (verification state, domain), if a facet is designed.
- Report-issue intent labels, if a richer reporting intent is designed.
- Reuse line and download labels following the licence decision (OWN-04).
- IBM pre-split Latin font subsets (vendoring with provenance).
- Rows for TABLE_TEXT_FIRST contracts whose rationale describes a table but resolves no rows (e.g. VIS-MFI-DIVERGENCE).

## Process notes (not escalations)

- D1 branch name (2026-09-27): D1 is developed and pushed on `claude/practical-cray-sr26c5`, the branch the execution
  environment is permitted to push, instead of the `design/d1-theses` name planned at D0. One gate, one branch, one pull
  request into `main` still holds; the steward may re-home the branch under `design/` at landing if the convention
  matters for history. No design meaning attaches to the name.

- Tag `checkpoint/design-handoff-ready` was not found at D0 (2026-09-27); commit `6d954c1` used. Steward to confirm.
  Steward, 2026-09-27: confirmed. `6d954c177b5d35cdad063f3a2cef5a92d33e16d4` is the recorded Design-handoff target (`OPENAI_REENTRY_CHECKPOINT.md` §7); the tag is an owner action (tag pushes are refused to the steward's environment). Working from the commit is correct; nothing changes when the tag appears.
