# Yemen Financial Inclusion Evidence · أدلة الشمول المالي في اليمن

[![Verify](https://github.com/CausewayGrp/Financial-inclusion-/actions/workflows/verify.yml/badge.svg?branch=main)](https://github.com/CausewayGrp/Financial-inclusion-/actions/workflows/verify.yml)

Developed and maintained by CauseWay.

Yemen Financial Inclusion Evidence is a governed bilingual evidence resource. It starts from a consequential question about financial inclusion in Yemen and gives the strongest answer the controlled evidence can support. It then shows what that answer means, what it does not establish, the wider system context that changes its reading, what remains unknown, and what should be measured next. The record, the method and the original source stay attached.

It exists because financial inclusion in Yemen cannot be read from one number, one institution or one moment. The available evidence covers different populations, institutions, units, methods, periods, geographies and publishing authorities. An ordinary dashboard collapses those differences. This resource keeps them visible.

The public path is understand, then explore, then verify. Arabic and English are co-authoritative editions of the same governed evidence. Arabic is not a later translation.

CauseWay stewards the synthesis, the derivation and the corrections process. CauseWay is not the regulator, the official statistical authority, or the publisher of third-party evidence.

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

## Production and release boundary

The repository contains the governed bilingual production implementation; that does not mean the site is publicly
released. The current deployment configuration is pre-release: `public_origin` is unset, `pre_release` is true,
licence text is not yet confirmed, and public downloads are disabled. The deploy workflow is owner-gated and requires
successful verification of the commit it deploys. Only the release owner can authorize release after the operational
checks in [`docs/RELEASE_RUNBOOK.md`](docs/RELEASE_RUNBOOK.md). Repository or interface verification is not release
approval.

| | |
|---|---|
| **Position** | **DESIGN HANDOFF READY** (R8.6 closed and accepted) |

Public release is not approved.

The current actionable release items are maintained in [`FINAL_OPEN_ITEMS_REGISTER.md`](FINAL_OPEN_ITEMS_REGISTER.md);
this README describes the stable system and does not track pull requests or session progress.

## Authority

This is the single production repository. The Production Master is the sole semantic, evidence, source, rights, controlled-product and publication authority:

`authority/Yemen_Financial_Inclusion_Evidence_Master.xlsx`

Master SHA-256: `fdb24bdfeae5c2604e326dd19effb4d79a783d44272f4dc08da2373979893999`

Page Specs SHA-256: `6c1d39df01cc31240f14ddab51f7cd761536a700f0328f7972fcaaee8b51be7b`

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
| [`handoff/`](handoff/) | Design and engineering handoff, subordinate to the Master |

## Public path

Home asks the question. Explore reads people, firms, finance, providers, payments and reforms. Evidence, Evidence Readings, and Data & sources carry the record and the publisher. Methodology and the Measurement Agenda hold method and what should be measured next. Search returns evidence, measurement and source records. Compare tests comparability before it shows values. About, Corrections, and Rights & reuse hold accountability.

![Public path](docs/diagrams/public-path.svg)

Both editions live at `/en/…` and `/ar/…`. `/` opens the reader's chosen edition.

## Engineering workflow

Start from the current `main` and follow [`CONTRIBUTING.md`](CONTRIBUTING.md) before making changes. Use the repository's
Python and browser-test dependencies from `requirements.txt`; the optional local serving command also uses the pinned
`http-server` dependency in `package-lock.json`.

```bash
python3 -m pip install -r requirements.txt
python3 -m playwright install chromium
npm ci
npm run verify
npm run build
npm run serve
```

`npm run verify` checks projection integrity, generator unit tests, Windows portability, a fresh build, public-literal
closure, repository validation, and release parity. The broader CI workflow runs the additional repository, browser,
accessibility, security-header, and negative-control gates. `npm run serve` serves the generated `dist/` locally on
port 4173. The published site is produced from the same renderer by `scripts/build.py --out` when deployment is
owner-authorized; do not deploy a local review build.

`dist/` is generated by `scripts/build.py` and must never be edited by hand. A gate fails if the committed site differs
from a fresh build. After adding, moving, or removing tracked files, regenerate the repository manifest and checksums
as described in [`CONTRIBUTING.md`](CONTRIBUTING.md).

Engineering invariants: change the Master first for any semantic correction; never hand-edit generated output; do not
add a second source of truth; preserve each figure's universe, period, unit and geography; keep Arabic and English
co-authoritative; and do not treat a public URL as redistribution permission. The full change protocol is in
[`CONTRIBUTING.md`](CONTRIBUTING.md), and durable evidence rules are in
[`authority/CORE_CONSTITUTION.md`](authority/CORE_CONSTITUTION.md).

## Where to go next

Methodology, rights and corrections are public pages generated from the Master. Architecture and deployment: [`docs/DEPLOYMENT.md`](docs/DEPLOYMENT.md). Release history and programme audits stay in `audit/` and `docs/CHANGELOG.md`. They are history, not the current front door.
