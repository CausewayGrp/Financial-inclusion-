# Open-items disposition (Part B B16)

**Status, 3 October 2026.** Every item still open in `design/ESCALATIONS.md` and `FINAL_OPEN_ITEMS_REGISTER.md`, and in
the records those two point to (`audit/release_candidate/B12_TEXT_FIRST_DISPOSITIONS.md`,
`audit/release_candidate/LINK_CHECK.md`, `design/DESIGN_DEBT.md`), has one dated disposition here:

- **DONE**: closed by a commit in this pull request, named.
- **RELEASE**: what remains at release, and who does it (`docs/RELEASE_RUNBOOK.md`).
- **POST-LAUNCH**: not needed for a link-and-citation launch (owner decision OWN-04), with the reason.
- **REJECTED**: decided, with the closed decision or rule it rests on.

B16 also disposes of the items Owner Addendum 2 sends here: its rejected list, its "judge, then decide" items, its
improvements and lessons. It adds the escalations raised by the product challenge (B15) and the red team's blocks.

**How it was built.** A read-only extraction at `c055abc` walked both files and every record they cite. An item was
taken as open unless a later line in its own record said it was closed, done, resolved, applied or superseded. That
gave 126 open and 58 already closed. Each open item was then checked against the repository at the head of this pull
request, and updated for what B15, RC-15 and RC-16 changed. Every item's own record gains a dated line pointing here
(append-only; nothing is rewritten). Nothing here declares PUBLIC RELEASE READY.
