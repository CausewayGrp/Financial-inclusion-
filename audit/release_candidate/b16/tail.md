## Notes on the count

- **Owner decisions of 3 October 2026** (`audit/OWNER_DECISIONS_2026-10-02.md`) settle seven escalations:
  - point 1 (X-ESC-RC8-01) is DONE in RC-17;
  - point 2 (X-ESC-B15-04) is DONE in RC-17;
  - point 3 (X-ESC-B15-01, -02) is DONE in the steward patch;
  - point 4 (X-ESC-B15-03) and point 5 (X-ESC-B15-05) are POST-LAUNCH;
  - point 6 (X-ESC-B15-06, OWN-04, X-ESC-D6-04, X-ESC-ANT-05) is RELEASE, waiting on the licence decision, with
    `public_downloads` false until then;
  - point 7 (X-ESC-B15-07) is REJECTED for this release.
  - The RC-17 adversarial review raised one consequence of point 2, X-ESC-RC17-01 (RELEASE).
- **B12's own count is 17 contracts.** This table lists 19 `X-B12-*` rows because the two drawings
  (VIS-FIRM-FINANCE-PATH, VIS-TARGET-RESULT-STATE), whose tables RC-12 bound, are listed separately. Each row names its
  missing input, from `audit/release_candidate/B12_TEXT_FIRST_DISPOSITIONS.md`.
- **Overlaps.** Some lines are the same underlying work, recorded in more than one place. Each record keeps its line,
  and each line here carries the same disposition:
  - X-ESC-D2-02b = EXT-10 (part) = X-B12-VIS-MFI-DIVERGENCE;
  - X-ESC-D6-06c = X-B12-VIS-INCLUSION-TRANSMISSION;
  - X-ESC-D6-04 = X-ESC-ANT-05 = OWN-04 = X-ESC-B15-06;
  - EXT-04 = ADD2-IMP-6.
- **"Into the roadmap (do not build now)."** Owner Addendum 2's list is recorded in `docs/ROADMAP_V1_1.md` §3 and is not
  counted again here. The ten items are the Findex 2021 weighted subgroup compute, RV-CWR-004 back to 2011,
  international context, the safe-sentence control, inline dated source brackets, versioned Readings, a domain search
  facet, Reading audiences, IOM DTM and VSLA context, and CPMI-IOSCO as a method reference.

## What remains for the owner

The owner merges this pull request, provides the hosting account and domain, decides the content licence, pushes the
release tag and signs the release. The RELEASE rows above are the steps of `docs/RELEASE_RUNBOOK.md` that come with
those acts:

- the public origin and live security headers;
- the currentness re-run at the release date;
- a browser check of the locators that refuse automated requests;
- the owner's release acceptance.

One choice is left that the owner's own decision created (X-ESC-RC17-01). NEG-EW-011's ID is the circular's own item number, so the record identifies the service. The owner can accept that as disclosed, or point the route to CLM-015. If the owner does not choose, the current state, which the owner decided, stands.

Nothing in this record declares DESIGN HANDOFF READY or PUBLIC RELEASE READY.
