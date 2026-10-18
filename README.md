# Yemen Financial Inclusion Evidence · أدلة الشمول المالي في اليمن

[![Verify](https://github.com/CausewayGrp/Financial-inclusion-/actions/workflows/verify.yml/badge.svg?branch=main)](https://github.com/CausewayGrp/Financial-inclusion-/actions/workflows/verify.yml)

Developed and maintained by CauseWay.

**Hosting decision, 16 October 2026:** hosting and the public address are unselected.
The [prospective owner decision](audit/OWNER_DECISIONS_2026-10-16.md) supersedes the 3 October
DigitalOcean selection. Cloudflare retirement is authorized but account-side completion must be
verified separately. Neither provider is required for development or PR acceptance. Deployment is
disabled; the origin remains null and the site remains pre-release. Older hosting instructions below
are historical context, not instructions to activate a provider.

Yemen Financial Inclusion Evidence is a governed bilingual evidence resource. It starts from a consequential question about financial inclusion in Yemen and gives the strongest answer the controlled evidence can support. It then shows what that answer means, what it does not establish, the wider system context that changes its reading, what remains unknown, and what should be measured next. The record, the method and the original source stay attached.

It exists because financial inclusion in Yemen cannot be read from one number, one institution or one moment. The available evidence covers different populations, institutions, units, methods, periods, geographies and publishing authorities. An ordinary dashboard collapses those differences. This resource keeps them visible.

The public path is understand, then explore, then verify. Arabic and English are co-authoritative editions of the same governed evidence. Arabic is not a later translation.

CauseWay stewards the synthesis, the derivation and the corrections process. CauseWay is not the regulator, the official statistical authority, or the publisher of third-party evidence.

## For developers and AI agents: start or resume here

This repository uses one governed Production Master, not interchangeable handoff ZIPs or prompts.
Read [AGENTS.md](AGENTS.md) and [CONTRIBUTING.md](CONTRIBUTING.md), then inspect your checkout with
`python3 scripts/reentry.py --base <previous-task-sha> --pr` (omit `--base` if unknown; use `--offline` if necessary).
This tool reports **Git repository state, not programme or owner authorization**. Unknown status stays UNKNOWN.

The [Core Constitution](authority/CORE_CONSTITUTION.md) states durable principles.
The [Current Project Context](authority/YFI_CURRENT_PROJECT_CONTEXT.json) is a validated subordinate projection of
the sole [Production Master](authority/Yemen_Financial_Inclusion_Evidence_Master.xlsx).
Stage A **content acceptance**, within its stated scope, is recorded by the
[acceptance scope](audit/stage_a_final/ACCEPTANCE_SCOPE_2026-10-15.md) and the
[dated decision on merged PR #49](https://github.com/CausewayGrp/Financial-inclusion-/pull/49#issuecomment-6192247588).
**Stage B authorized 17 October 2026 (OD-1017-01)**, by the [owner decisions of 17 October 2026](audit/OWNER_DECISIONS_2026-10-17.md);
the operative charter is the [Stage B Design Charter v3.2](audit/close_out/STAGE_B_DESIGN_CHARTER_v3_2.md), executed by
Claude Code, the only writing agent, under the [takeover brief](audit/close_out/TAKEOVER_BRIEF_2026-10-17.md). Stage C
follows without a further owner message (OD-1017-02). Missing D19–D22 texts were neutralized on 17 October 2026; they
authorize nothing. Hosting is unselected and there is no public production-release authorization.

## What it is, and what it is not

It is a decision resource for reading financial inclusion evidence. It is not a dashboard, a regulator, an official statistical authority, a general financial-system observatory, a provider directory, a reform tracker, a research blog, or a CauseWay marketing site. Broader financial-system context appears only where it changes the reading of inclusion evidence.

## How the evidence is kept bounded

A number without its universe, period and meaning can be true and still mislead. Every consequential figure stays tied to its population, period, definition, material method, original source, evidence state and limit, and to what it does not establish.

These distinctions are the product, not a footnote:

- People are not accounts.
- Access is not use.
- Infrastructure is not an outcome.
- A target is not a result.
- A programme indicator is not national prevalence.
- A licence or a listing is not operation.
- Missing is not zero.
- The observation date is not the publication date.
- Disagreement is not automatically an error.
- Bounded evidence stays bounded.

Full method: the public Methodology pages, generated from the Master. Rights, citation and corrections: About, Rights & reuse, and Corrections.

External facts stay attributed to their original publishers. CauseWay attribution covers CauseWay synthesis and stewardship only. A public URL is not permission to redistribute. Restricted source files are not republished because they can be found online. Citation, factual use and redistribution are separate permissions.

![Authority flow: Master, derived site, public path](docs/diagrams/authority-flow.svg)

## Current state

| | |
|---|---|
| **Position** | **DESIGN HANDOFF SUPERSEDED** (10 October 2026). `handoff/` is historical. Stage B authorized 17 October 2026 (OD-1017-01); the operative charter is [v3.2](audit/close_out/STAGE_B_DESIGN_CHARTER_v3_2.md) and the [15 October charter](audit/close_out/STAGE_B_DESIGN_CHARTER.md) keeps its constraints. |
| Non-design v1 product | Complete |
| Current phase | **Stage A content accepted within its dated 15 October 2026 scope; Stage B authorized 17 October 2026 (OD-1017-01)**, Stage C to follow (OD-1017-02), both executed under the takeover brief of 17 October 2026 ([`audit/close_out/TAKEOVER_BRIEF_2026-10-17.md`](audit/close_out/TAKEOVER_BRIEF_2026-10-17.md); Claude Code is the only writing agent). Hosting is unselected (16 October 2026) and public production release is not authorized. [`audit/close_out/PROGRESS.md`](audit/close_out/PROGRESS.md) carries the stage state; current engineering/PR status must be checked on GitHub. |
| Post-v1, owner decision | C1 typed difference block; C2 dedicated guarantee route; C3 public contradiction index |
| Reuse rights | Decided: CC BY 4.0 for CauseWay's own content (adopted 3 October 2026, closed 10 October 2026). The owner confirmed the licence text on 10 October 2026 (RIGHTS-FINAL; no legal review is claimed); the rights question is closed permanently |
| Public release ready | No |
| Content | Complete on `main`, 10 October 2026. The annotated tag `checkpoint/2026-10-10-content-complete` marks it, or is the owner's to push ([`docs/HANDOVER_TO_DEVELOPER.md`](docs/HANDOVER_TO_DEVELOPER.md) §9) |
| Stage A (evidence and Arabic) | STAGE A COMPLETE was recorded at `53dccc4d` (11 October 2026). The Stage A addendum followed on 11 October 2026 (#39 to #42: literal audit v3, CLOSE-6A to CLOSE-6C, Reading CWR-012). The final instruction v5 changes are integrated: CLOSE-6D (#43), CLOSE-6E (#44), CLOSE-6F (#45 at `612ec146`, 13 October), and CO-G07/CLOSE-6G with the [addendum report](audit/close_out/STAGE_A_ADDENDUM_REPORT_v5_2026-10-13.md) (#46 at `e46ff9eb`, 14 October 2026). The 15 October final reconciliation and [prospective acceptance scope](audit/stage_a_final/ACCEPTANCE_SCOPE_2026-10-15.md) supersede the remaining material interpretation and edition issues. The dated post-merge acceptance record on the reconciliation PR is the formal Stage A decision; the old report is historical, not retrospective owner approval. Stage B prerequisites and Stage C/release acceptance remain separate. Neither DESIGN HANDOFF READY nor PUBLIC RELEASE READY is claimed |
| Public inventory (17 October 2026) | 151 Page Specs (306 HTML documents), 116 Evidence Records, 60 public claims, 12 Readings, 10 measurement priorities, 31 dated events, 208 source records (193 with a public locator), 522 search records |
| Open pull requests | [Check GitHub's live PR list](https://github.com/CausewayGrp/Financial-inclusion-/pulls). Current branch, PR and CI state must be inspected live; historic close-out decisions remain in `audit/close_out/PROGRESS.md`, not this changing-status field. |

Closed in this product state: governed evidence and content for v1; Used on reaches every source, including those with no domain use recorded; a single valid Compare entry loads the reader's record and still requires two records for a verdict; the 31 dated events of the system chronology are indexed in search, each deep-linking to its own anchor on /finance/ (the analytical rule is not a dated event and is not indexed); the reuse licence for CauseWay's own content (CC BY 4.0, [`audit/OWNER_DECISIONS_2026-10-10.md`](audit/OWNER_DECISIONS_2026-10-10.md)) — a reuse licence is not regulatory licensing, and CauseWay neither holds nor claims the status of a licensed financial institution.

Not closed, and not claimed: design integration; integrated Arabic and English, RTL, mobile, accessibility and browser acceptance after that integration; release-time hosting, security headers, currentness and live checks; final owner release approval. The repository's software code is outside the CC BY 4.0 licence and is not openly licensed: CauseWay reserves all rights in it (owner decision D3, 10 October 2026).

Remaining path: non-design v1 complete, then design / presentation integration, then final integrated QA, then release / cutover, then owner release approval. Release-time steps live in [`docs/RELEASE_RUNBOOK.md`](docs/RELEASE_RUNBOOK.md). Open items live in [`FINAL_OPEN_ITEMS_REGISTER.md`](FINAL_OPEN_ITEMS_REGISTER.md). The content-pass ledger is [`audit/final_content/FINAL_CONTENT_LOG.md`](audit/final_content/FINAL_CONTENT_LOG.md).

## Release boundary — production not authorized

PR #46's Verify and the subsequent Cloudflare Workers build passed **at that time**; that is historical
verification, not evidence of the current temporary preview's live state. Cloudflare Workers has been used for a
**temporary pre-release preview**; its external GitHub build status is not the Production Master's semantic authority,
a substitute for Verify, or permission to release. The DigitalOcean production route selected on 3 October 2026 is
**historical**: hosting and the public address are **unselected** (owner decision of 16 October 2026), and neither host
is a development or billing prerequisite. Do not provision, activate, or deploy any host under ordinary
evidence/design work. The committed `dist/` is the review build, **not proof of a current live deployment**.

**No public production release has been authorized**; the future release gates remain under owner control.
The following are deferred release prerequisites, not instructions to incur hosting costs now:

| Blocker | Owner | Where |
|---|---|---|
| Hosting (future release only, not required for present review): the host and the public origin are unselected ([owner decision of 16 October 2026](audit/OWNER_DECISIONS_2026-10-16.md)); the owner selects them at release, and the earlier DigitalOcean procedure is a historical adapter | CauseWay (owner), then authorized deploy operator | [`docs/RELEASE_RUNBOOK.md`](docs/RELEASE_RUNBOOK.md), "Prospective supersession"; steps 1–14 are the historical adapter |
| Data downloads stay off (`public_downloads: false`), a separate owner decision. The CC BY 4.0 text itself is confirmed by the owner (10 October 2026, RIGHTS-FINAL), so `licence_text_confirmed` is `true` and no longer blocks a deploy | Owner | runbook steps 2 and 7a |
| Seven sources that need a person with a browser | A person | [`docs/HANDOVER_TO_DEVELOPER.md`](docs/HANDOVER_TO_DEVELOPER.md) §3 |
| A phone check of the live site from Yemen, in Arabic | A person in Yemen | handover §4 |
| OpenAI's independent acceptance review | OpenAI | handover §5 |
| The owner's release approval | Owner | runbook step 13 |
| Repository housekeeping this session's access refuses: deleting 16 merged branches, and the checkpoint tag if absent | Owner (or anyone with write access) | handover §9 |

The full list of what a person must still do is [`docs/HANDOVER_TO_DEVELOPER.md`](docs/HANDOVER_TO_DEVELOPER.md);
open evidence items are in [`FINAL_OPEN_ITEMS_REGISTER.md`](FINAL_OPEN_ITEMS_REGISTER.md), in its live view at the top (one state per item; §1–10 are history).

## Authority

This is the single production repository. The Production Master is the sole semantic, evidence, source, rights, controlled-product and publication authority:

`authority/Yemen_Financial_Inclusion_Evidence_Master.xlsx`

Master SHA-256: `03d194a2c402b7d4673c4c4106cab5f1ce9b0f92128e98fc405342889f3e9f9e`

Page Specs SHA-256: `cf8138806a4e43be3947e6e460d9e498f5a854ef0adc3813fe161d1d750be328`

| Layer | Role |
|---|---|
| Production Master | Authority |
| `authority/YFI_CURRENT_PROJECT_CONTEXT.json` | Projection. It does not overrule the Master |
| `site-src/`, `design/`, `scripts/` | Presentation, contracts, and the machines that project and check |
| `dist/` | Generated public site. Do not hand-edit |
| This README | Orientation. Not authority |
| `audit/` | Verification and lineage. Not a second production authority |

If the Master changes, subordinate projections are regenerated. There is no parallel truth.

![Repository layers](docs/diagrams/repository-layers.svg)

## Repository map

| Path | Why a recipient goes there |
|---|---|
| [`authority/`](authority/) | Master, constitution, current-state projection |
| [`site-src/`](site-src/) | Presentation source. Evidence text is projected, not authored here |
| [`scripts/`](scripts/) | Canonical projection, build, checksums and validation |
| [`design/`](design/) | Accepted presentation contracts and tokens |
| [`dist/`](dist/) | Generated site, committed so a public change is reviewable |
| [`audit/`](audit/) | Review and lineage |
| [`docs/RELEASE_RUNBOOK.md`](docs/RELEASE_RUNBOOK.md) | What release still requires |
| [`handoff/`](handoff/) | Superseded (10 October 2026); historical reference only, never executed |

## Public path

Home asks the question. Questions lead to the eight governed domains: People, Firms, Banks and microfinance, Providers, Payments, Remittances, Access and Reforms. Evidence, Readings and Sources carry the record and the publisher. Methodology and Measurement priorities hold method and what should be measured next. Search discovers existing pages, questions, Evidence Records, Readings, measurement priorities, source records and source locators, and dated chronology events that deep-link to their anchors on `/finance/`; it does not validate claims. Compare tests comparability before it shows values. About, Corrections, and Rights and reuse hold accountability.

![Public path](docs/diagrams/public-path.svg)

Both editions live at `/en/…` and `/ar/…`. `/` opens the reader's chosen edition.

## Safe start

Work from `origin/main`, or a branch rebased on it. Every change goes through a pull request with CI green (`CONTRIBUTING.md`).

```bash
python3 scripts/generate_projections.py --check
python3 scripts/social_images.py --check
python3 scripts/build.py
python3 scripts/checksums.py --check
python3 scripts/validate.py
python3 -m http.server 8080 --directory dist
```

`dist/` is produced by `scripts/build.py`. A gate fails if the committed site differs from a fresh build.

Invariants: Master first for any semantic change; never hand-edit generated output; do not add a second source of truth; do not widen a figure beyond its universe, period or geography; keep Arabic and English semantically the same; do not treat a public URL as redistribution permission. Operating rules: [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`authority/CORE_CONSTITUTION.md`](authority/CORE_CONSTITUTION.md).

## Where to go next

Methodology, rights and corrections are public pages generated from the Master. Architecture and deployment: [`docs/DEPLOYMENT.md`](docs/DEPLOYMENT.md). Release history and programme audits stay in `audit/` and `docs/CHANGELOG.md`. They are history, not the current front door.
