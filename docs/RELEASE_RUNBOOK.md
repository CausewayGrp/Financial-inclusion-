# Release runbook — from "the owner has a hosting account and a domain" to "live"

**Status, 3 October 2026:** prepared, not started. Nothing here has been executed. The site is not released; this
repository never declares PUBLIC RELEASE READY, and only the owner releases it (step 14). Each step names who does it.
Every step except the account, the domain, the licence decision, the release acceptance and the tag is a Claude Code
step.

## Hosting: the recommendation

**Cloudflare Pages**, with **Netlify** as the alternative. Both serve `dist/` as static files and read
`dist/_headers`, so the security policy and the cache rules ship with the build.

| Need | Cloudflare Pages | Netlify |
|---|---|---|
| Cost for a static site of this size | Free plan covers it | Free plan covers it |
| Arabic and RTL | Files served byte for byte; nothing is rewritten | The same |
| Custom headers | `_headers` from the publish root | `_headers` from the publish root |
| Custom domain and HTTPS | Yes, certificate issued automatically | Yes, certificate issued automatically |
| Reach | A large anycast network | A global CDN |
| Deploy from CI | `wrangler pages deploy` (`.github/workflows/deploy.yml`) | Netlify CLI (the workflow's last step changes) |

Neither host has been tested from inside Yemen. Step 10 asks a person with local access to open the live site before
the owner accepts the release. GitHub Pages is not recommended, because it cannot send security headers
(`docs/DEPLOYMENT.md`).

## Steps

| # | Step | Who | How | Done when |
|---|---|---|---|---|
| 1 | **Account and domain.** A Cloudflare account; the release domain registered and added to it. | Owner | Cloudflare dashboard | The domain is active in the account |
| 2 | **Licence decision for downloads.** Decide whether the data exports (`scripts/exports.py`) may be published, and under what terms. | Owner | A dated line in `audit/OWNER_DECISIONS_*.md` | The decision is recorded. If it is yes, Claude Code sets `public_downloads: true` in `site-src/deployment.json`, after the codebook's bilingual review, and states the terms on /data/ Master-first |
| 3 | **Origin.** Set `public_origin` in `site-src/deployment.json` to `https://<domain>` (no trailing slash). Rebuild: `python3 scripts/social_images.py && python3 scripts/build.py && python3 scripts/audit_public_literals.py`. | Claude Code | One commit | The validator passes; canonical, hreflang, `og:url`, structured data and `sitemap.xml` are absolute, and `robots.txt` allows crawling and names the sitemap (`scripts/discovery.py`, F6 gates) |
| 4 | **Currentness at the release date.** `python3 scripts/currentness_rerun.py --append`. Anything newer is read in its original and enters the Master by transaction. The edition date (`UI-CONTENT-VERSION`) moves to the release date, Master-first. | Claude Code | `run_stage.py` | The appended result shows no unread NEWER item, and the "check by hand" points have been checked in a browser |
| 5 | **Every gate.** Every step of `.github/workflows/verify.yml`, locally and in CI: checksums, projection check, validator, literal-audit determinism, lineage, diagrams, social images, logo derivatives, bilingual invariance, content parity, exports, public tools, viewport acceptance, security headers, negative controls. | Claude Code | CI on the release commit | CI is green on the commit that will be tagged |
| 6 | **Pages project and credentials.** Create the Cloudflare Pages project for direct uploads. Create an API token limited to "Cloudflare Pages: Edit". | Owner | Cloudflare dashboard | The project name and the token exist |
| 7 | **Repository settings.** Secrets `CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID`; variables `YFIE_CF_PAGES_PROJECT` and `YFIE_DEPLOY_ENABLED=true`. | Owner (the secrets); Claude Code may set the variables where the session has settings access | GitHub → Settings → Secrets and variables → Actions | The deploy workflow is no longer skipped |
| 8 | **Deploy.** Merge to `main`, or run "Deploy" by hand (workflow_dispatch). The workflow refuses a null origin, runs the gates, proves `dist/` is a fresh build, then uploads it. | Claude Code (merge on the owner's approval of the PR) | `.github/workflows/deploy.yml` | The workflow is green and the Pages deployment is live on the domain |
| 9 | **Headers and HTTPS.** Check that HTTPS works on the domain. Then add `Strict-Transport-Security: max-age=31536000; includeSubDomains` under `/*` in `site-src/hosting/_headers`, rebuild and redeploy. Run `python3 scripts/tests/test_security_headers.py --base https://<domain>`. | Claude Code | One commit; the test against the live host | Every page loads with every security header and no policy violation |
| 10 | **Every page on the live host.** `YFIE_BASE_URL=https://<domain> python3 scripts/tests/test_public_tools.py` against the live origin (viewport acceptance runs on the same build in step 5). Remeasure performance with `scripts/performance_budget.py`, adapted to the origin, and record the result beside `release_candidate_b14d` in `docs/SUSTAINABILITY_IMPLEMENTED_RUNTIME.json`. A person opens the site on a phone in Yemen, or on a connection routed there, in Arabic. | Claude Code; the in-country check by a person the owner names | The tests; a dated note | The tests pass, the budget is met or its miss is recorded, and the in-country check is recorded |
| 11 | **Usage counts (optional).** Only cookieless, first-party, aggregate counts with no personal data. The /privacy/ page must say so in both languages, Master-first, *before* activation, as it requires. | Owner decides; Claude Code implements | A Master transaction for /privacy/, then the code | Activated only after the Privacy page is live |
| 12 | **Open items.** Every item in `FINAL_OPEN_ITEMS_REGISTER.md` and `design/ESCALATIONS.md` marked RELEASE is done or re-dispositioned (`audit/release_candidate/OPEN_ITEMS_DISPOSITION.md`). | Claude Code | Dated lines | No RELEASE item is open |
| 13 | **Release acceptance.** The owner reviews the live site and the records, and accepts the release. | Owner | A dated, signed acceptance line in `audit/OWNER_DECISIONS_*.md` | Recorded |
| 14 | **Tag.** The owner pushes the release tag on the accepted commit of `main`. | Owner | `git tag -s v1.0.0 <commit> && git push origin v1.0.0` | The tag exists; the release is the tagged commit |

## Rolling back

Cloudflare Pages keeps every deployment. "Rollback to this deployment" in the dashboard restores the previous one at
once (Owner or Claude Code with dashboard access). The repository then reverts the faulty commit on a branch, CI goes
green, and a new deploy goes out (Claude Code). History is never rewritten.

## What this runbook does not do

- It does not decide anything that belongs to the owner: the account, the domain, the licence, the acceptance and the tag.
- It does not claim WCAG conformance, legal review, rights clearance, native-language certification or a security
  guarantee. The header test checks the policy the site sends; it is not a security assessment.
- It does not turn a local measurement into an operational or carbon figure.
