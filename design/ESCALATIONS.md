# Escalations

Format (README_FIRST §10):
- `ESCALATE_TO_MASTER — <route/object> — <defect> — <design impact>`
- `NEEDS_CONTROLLED_CONTENT — <route/object> — <field> — <design impact>`

Answered by the steward, Master-first. Items are closed, never deleted.

## Open

None raised at D0. No controlled-truth defect was found during read-in.

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

- Tag `checkpoint/design-handoff-ready` was not found at D0 (2026-09-27); commit `6d954c1` used. Steward to confirm.
  Steward, 2026-09-27: confirmed. `6d954c177b5d35cdad063f3a2cef5a92d33e16d4` is the recorded Design-handoff target (`OPENAI_REENTRY_CHECKPOINT.md` §7); the tag is an owner action (tag pushes are refused to the steward's environment). Working from the commit is correct; nothing changes when the tag appears.
