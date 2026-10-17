# Owner decision — 16 October 2026: hosting neutrality and bounded integration

Source: the owner's “CauseWay | YFIE — one-window integration directive” in this session.

Hosting is now undecided. Neither Cloudflare nor DigitalOcean is required for development,
PR acceptance or current release preparation. This prospectively supersedes the hosting selection
of 3 October 2026; it does not deny that decision or rewrite its historical record.
The public origin stays null, pre-release stays true, and public downloads stay false.
No deployment, public release, purchase of capacity or corporate-site change is authorized.

The owner authorizes: finish PR #50; a distinct hosting-neutral PR with a separately justified
Master-first privacy correction; then update and finish existing homepage PR #51. Normal merges
require complete checks on the final commit and substantive scope review. The narrow homepage
pilot does not authorize general Stage B. Unresolved runner or review conditions block merging.

Cloudflare retirement is authorized only for the verified temporary YFIE project after checking
custom-domain/DNS and service dependencies. Disable its automatic builds, disconnect its repository
integration, and retire its preview endpoint. Account deletion and unrelated services are excluded.
Repository changes alone do not establish account-side retirement.

## Privacy correction justification

Master fields: `03_PAGE_SECTIONS`, `/privacy/`, sections 3 and 4, `body_en` and `body_ar`;
only these four cells change. The present copy asserts DigitalOcean App
Platform hosting and an active corporate proxy/cookie route. Those assertions cannot stand after
the hosting decision is withdrawn. The exact old/new bilingual cell values and consumer impact
are recorded by `audit/hosting_neutral/privacy_transaction.py` and its ledger. The new text states
the undecided host/address and unconfirmed logging/processor/retention details; it preserves the
runtime's no-cookie statement without asserting a live corporate route. No evidence claim,
measurement, source binding, licence or publication flag is changed.

## Coverage and external receipt

Required Verify retains build, projections, evidence/source/rights gates, bilingual parity,
browser tools, viewport, no-JS, security headers and base-path tests. The portable HTTP contract
test replaces the host adapter's required response-contract coverage: status codes, relative
redirects, MIME, cache/security headers, no cookies, and missing-header rejection. The existing
nginx/image tests remain available in an optional manual compatibility workflow, without deployment.
`_headers` remains the portable policy input. The historical deploy workflow and CLI are disabled.

Live inspection: main `19384b27`; #50 `29075c47`; #51 `fa2be0b7`, both Draft. The GitHub connector
rejects check annotation and Actions-permission endpoints; direct authenticated CLI access to
the annotation endpoint is Forbidden. Branch protection returns “Resource not accessible by
integration”; rulesets return a plan/visibility 403. Neither response diagnoses Actions billing.
No startup condition change is established and no retry is authorized by that evidence.

External check identified: `Workers Builds: financial-inclusion`, account identifier
`6b293e8e1499a6b25221638ba21970d1`, build `86f66561-eeab-4204-a8fc-729489e89224` on #50's head.
These are check metadata, not verified account access. This session has no Cloudflare account
connector or credentials. Build trigger, installation permissions, logs, custom domains/DNS,
live endpoint identity and dependencies remain UNVERIFIED; retirement remains BLOCKED.
No check enforcement or account setting was changed. Owner/admin access is needed to inspect
the Actions rejection annotation and permitted runner configuration, and Cloudflare access is
needed to verify dependencies and perform retirement. Do not infer a billing cause.

### Refreshed receipt — 17 October 2026

The preceding access results describe the initial inspection, not the final GitHub state.
PR #50 subsequently completed Verify run 38946392754, all nine jobs on head `29075c47`,
and merged as `274583df`. PR #51 advanced to `64dca58b` with successful run 38972997743.
This branch preserves its implementation in `18ed4f3f` and merges current main normally.
Separate PR #52 records the owner's prospective neutralization of missing D19–D22;
this hosting change does not duplicate or override that authority work.

Independent integrity review found and resolved a stale privacy-column assumption,
a deployment job-name edge case, and omitted portable response cases. The corrected transaction
changes exactly four privacy body cells and passed regeneration, validation and idempotence.
Both deployment fault controls were caught. The portable HTTP browser sweep passed all
306 pages and rejected a missing required header. No human participant testing is claimed.
Local browser is Debian Chromium 154.0.8037.57, substituted for Playwright's pinned download;
GitHub browser acceptance remains necessary. Cloudflare account access remains unavailable.
