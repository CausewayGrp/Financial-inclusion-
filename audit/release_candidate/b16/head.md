# Open-items disposition (Part B B16)

**Status, 3 October 2026.** Every item still open in `design/ESCALATIONS.md` and `FINAL_OPEN_ITEMS_REGISTER.md`, and in
the records those two point to (`audit/release_candidate/B12_TEXT_FIRST_DISPOSITIONS.md`,
`audit/release_candidate/LINK_CHECK.md`, `design/DESIGN_DEBT.md`), has one dated disposition here:

- **DONE**: closed by a commit in this pull request, named.
- **RELEASE**: what remains at release, and who does it (`docs/RELEASE_RUNBOOK.md`).
- **NEXT EDITION** (POST-LAUNCH in the inputs): not needed for a link-and-citation launch (owner decision OWN-04), with the reason and the missing input.
- **REJECTED**: decided, with the closed decision or rule it rests on.

B16 also disposes of the items Owner Addendum 2 sends here: its rejected list, its "judge, then decide" items, its
improvements and lessons. It adds the escalations raised by the product challenge (B15) and the red team's blocks.

**How it was built.** A read-only extraction at `c055abc` walked both files and every record they cite. An item was
taken as open unless a later line in its own record said it was closed, done, resolved, applied or superseded. That
gave 126 open and 58 already closed. Each open item was then checked against the repository at the head of this pull
request, and updated for what B15, RC-15 and RC-16 changed. Every item's own record gains a dated line pointing here
(append-only; nothing is rewritten). Nothing here declares PUBLIC RELEASE READY.

**Finished at the end of pull request #9 (3 October 2026, evening).** The owner note of 11:15 (4.1–4.6, the G0 pass and
section 5's seven topics, one line each), the rejections that review reopened for challenge (maps, same-source
international context, the three waves), and the G0 findings are added. One earlier DONE is corrected:
Dataset structured data was never prepared, so it is NEXT EDITION. Commit placeholders are resolved against the live
ancestry (`make_disposition.py`, COMMITS). The category the earlier pass called POST-LAUNCH is printed as NEXT EDITION,
with its missing input.

**G0 notes (first-reader pass, 3 October 2026).** Home, the eight domains, CLM-002 and /about/ were read at 390 px in
Arabic and 1440 px in English (`audit/release_candidate/checks/g0_shots.py`, 22 views, no horizontal overflow), each
against four readers: a citizen on a phone, a journalist, a supervisor, a researcher.
- The one release defect was the inline-figure box from RC-18. It is fixed in `870d8a5`, and gate RC-1115 and the
  viewport check now hold it.
- Each domain page answers its question in its first screen, with the qualification beside the number.
- /remittances/ is the clearest case of the product's value: the same 2024 year at US$6,245 million and
  US$3,422.16 million is shown as a revision of the same year, not a fall.
- /payments/ follows the analytical form: what we know (561 to 1,651 reported terminals), what changed, what we still
  cannot see (people using them), and what would resolve it (the Measurement Agenda link).
- CWR-005 is bounded: "historical study", "December 2019", "not national prevalence in 2026". It stays as it is.
- Regulation: /reforms/ names the instrument (Governor's Decision No. 4 of 2025), the authority, the date and the
  stage the evidence reaches, and leaves implementation and outcome open.
- Search: 29 of 30 ordinary queries in both languages land right; "ID" is next edition (G0-SEARCH-ID).
- The guided paths checked all resolve in one step: account ownership to the gender gap (through its Reading), POS to
  the payment-system Reading, a remittance figure to the publication-vintage Reading, a firm constraint to the
  denominator Reading, and a programme KPI to the Measurement Agenda.
