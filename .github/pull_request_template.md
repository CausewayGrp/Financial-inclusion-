## What and why

<!-- The demonstrated problem, and what becomes more truthful, understandable, verifiable or usable. -->

## Owner layer

<!-- Tick one. Content, evidence, source, rights and status changes belong to the Master. -->
- [ ] Production Master (transaction through `audit/tranche_b_execution/run_stage.py`)
- [ ] Generator or build code (`scripts/`)
- [ ] Runtime (`site-src/app.js`, `site-src/styles.css`)
- [ ] Handoff or Design package (`handoff/`, `design/`)
- [ ] Repository, CI or documentation only

## Master transaction (if any)

| Field | Value |
|---|---|
| Transaction | <!-- e.g. TC-J --> |
| Master before → after | <!-- first 12 hex of each --> |
| Run report | <!-- audit/…/runs/…_RUN_REPORT.json --> |
| Findings closed | <!-- ledger IDs --> |

## Checks

- [ ] No projection under `site-src/content/`, no file in `dist/` and no audit closure was edited by hand.
- [ ] English and Arabic changed together; numbers, units, periods and limits are the same in both editions.
- [ ] `python3 scripts/checksums.py` was run and `SHA256SUMS.txt` is committed with the change.
- [ ] `docs/CHANGELOG.md` has an entry; README, checkpoint and Context agree if the programme state changed.
- [ ] No new public number without a bound, source-traced record; no source named without a public locator.
- [ ] Nothing declares DESIGN HANDOFF READY or PUBLIC RELEASE READY outside the R8.6 Definition of Done.
