# Release runbook — from "the owner has a hosting account and a domain" to "live"

**Status, 3 October 2026:** prepared, not started. Nothing here has been executed. The site is not released; this
repository never declares PUBLIC RELEASE READY, and only the owner releases it (step 14). Each step names who does it.
Every step except the account, the domain, the licence decision, the release acceptance and the tag is a Claude Code
step; the route on `causewaygrp.com` is CauseWay's web administrator's ("Hosting").

## Hosting

### The address and what the domain looks like today

The release address is **`https://causewaygrp.com/financial-inclusion-evidence/`** (owner decision B1, 3 October 2026):
lowercase and hyphenated. Its root opens the Arabic edition, or the edition the reader chose before; English is under
`/en/`. `public_origin` is not set yet (B8); step 3 sets it.

The owner recorded these facts on 3 October 2026 (B4). Claude Code confirmed them the same day at 07:20 UTC with one
read-only request (`curl -sI https://causewaygrp.com/`) and a DNS lookup. Nothing outside this repository was changed.

| Fact | Observed |
|---|---|
| Name servers | `ns1.digitalocean.com`, `ns2.digitalocean.com`, `ns3.digitalocean.com`: DNS is at DigitalOcean, not Cloudflare |
| Address of `causewaygrp.com` | One A record, `206.189.57.121` |
| Application | `x-powered-by: Nuxt` |
| Cookie | `set-cookie: session=…; Path=/`. The browser sends it back with every request on the domain, including requests for this resource. The header showed no `Domain`, `Secure` or `HttpOnly` attribute |
| Robots header | `x-robots-tag: index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1` |
| Edge | No `cf-ray` or `server: cloudflare` header |

What follows from them:

- DNS is not on Cloudflare, so a Cloudflare Worker route on `causewaygrp.com` is not available as things stand.
- App Platform serves apps through its built-in Cloudflare CDN, whose responses carry `cf-ray` and `server: cloudflare`.
  This response carried neither, and the domain resolves to one DigitalOcean address. That suggests the corporate site
  does not run on App Platform; it is more likely a Droplet. The web administrator confirms it.

### What every route must keep

1. **Our security headers reach the reader.** Every response under the path carries the headers of `_headers`:
   `Content-Security-Policy`, `X-Content-Type-Options`, `Referrer-Policy`, `Permissions-Policy`,
   `Cross-Origin-Opener-Policy`, `X-Frame-Options` and `Cache-Control`.
2. **Nothing of the corporate site is added to our responses.** No `x-robots-tag` (our pages state their own robots
   rule), no script, no cookie and no `Set-Cookie`. The corporate `session` cookie is not passed on to our host.
3. **Rollback is one step.**

The checks, on the live address (steps 8 to 10):

```bash
curl -sI https://causewaygrp.com/financial-inclusion-evidence/en/
#   must show content-security-policy, x-frame-options and the other headers of _headers;
#   must not show set-cookie or x-robots-tag (nor x-powered-by: harmless, but not ours)
curl -sI https://causewaygrp.com/financial-inclusion-evidence/en/payments
#   a redirect whose Location stays on causewaygrp.com, never on pages.dev
python3 scripts/tests/test_security_headers.py --base https://causewaygrp.com/financial-inclusion-evidence
#   every page, every security header, no policy violation (an injected script would be blocked and reported)
```

### How the site is built for the path

- `dist/` is the review build. Its own links stay root-relative, so every gate serves and reads it at a server root, as
  it always has.
- The published site is `python3 scripts/build.py --out build/site`. It moves every link, asset, stylesheet, runtime
  fetch, language prefix, root redirect and `_headers` path pattern under `/financial-inclusion-evidence/`
  (`scripts/base_path.py`). Canonical, hreflang, `og:url`, `og:image`, structured data and the sitemap are absolute from
  the origin, path included.
- `scripts/tests/test_base_path.py` builds the decided origin into a temporary directory and serves it under the path.
  It sweeps every file, drives the public tools at 390 and 1440 px in both languages, and fails on any request that
  leaves the path. It runs in CI on every pull request, with its own negative control.
- The deploy workflow builds the published site, sweeps it with the same test, and uploads a publish root that holds
  the site under `financial-inclusion-evidence/` and `_headers` at the root, where Pages reads it.
- One request does leave the path, and no page makes it: no page declares an icon, so browsers ask the domain root for
  `/favicon.ico`, and `causewaygrp.com` answers it. The test reports it without failing.
- No host has been tested from inside Yemen. Step 10 asks a person with local access to open the live site before the
  owner accepts the release. GitHub Pages is not an option, because it cannot send security headers
  (`docs/DEPLOYMENT.md`); Netlify, the earlier alternative, reads the same `_headers` but is not one of the three routes.

### Route 1, preferred: our own Cloudflare Pages project, reached through the corporate site

```text
reader → causewaygrp.com (DigitalOcean DNS → the corporate Nuxt application)
           └─ /financial-inclusion-evidence/**  → proxy, path unchanged →  https://<project>.pages.dev/financial-inclusion-evidence/**
```

- **Our side (this repository).** The deploy workflow publishes the site as described above. The Pages project's own
  address, `https://<project>.pages.dev/financial-inclusion-evidence/`, is the same site. Steps 9 and 10 can therefore
  test it before the proxy exists.
- **The corporate side.** This is a later, separate task in CauseWay's own frontend repository, not part of this pull
  request. The snippet below is guidance only:

  ```ts
  // nuxt.config.ts in CauseWay's frontend repository: guidance, not applied from here
  export default defineNuxtConfig({
    routeRules: {
      '/financial-inclusion-evidence': { redirect: { to: '/financial-inclusion-evidence/', statusCode: 301 } },
      '/financial-inclusion-evidence/**': {
        proxy: {
          to: 'https://<project>.pages.dev/financial-inclusion-evidence/**',
          headers: { cookie: '' },   // the corporate session cookie is not passed on to our host
        },
      },
    },
  })
  ```

- **Security headers.** Pages sends them from `_headers`. The proxy passes the response headers through. If a reverse
  proxy such as nginx sits in front of the Nuxt process, the same forward can be set there instead; it must keep the
  same three properties, and the checks above apply unchanged.
- **Nothing corporate added.**
  - The proxy returns the Pages response unchanged, so no corporate script enters our pages. Our policy allows only
    our own scripts (`script-src 'self'`), so an injected script would be blocked, and the header test reports it.
  - `headers: { cookie: '' }` replaces the incoming `Cookie` header, so the `session` cookie never reaches our host.
  - Pages sends no `Set-Cookie`.
  - The corporate application adds its `session` cookie and its `x-robots-tag` to the responses it serves. It adds
    them to ours as well if they are set by a middleware or plugin that runs before the route rules. The frontend task
    therefore excludes `/financial-inclusion-evidence/**` from the session and from the robots header. The checks
    above must pass before release.
- **Do not** add a host rule `https://<project>.pages.dev/*` with `X-Robots-Tag: noindex` to `_headers`. The proxy
  fetches from that host, so the header would reach `causewaygrp.com`. The `pages.dev` copy does not compete in search,
  because every page's canonical names `causewaygrp.com`.
- **Rollback.** Pages keeps every deployment, and "Rollback to this deployment" restores the previous one at once. The
  proxy needs no change. If the proxy itself misbehaves, removing the route rule (one commit in the frontend
  repository) takes the path down; route 3 can then be used.

### Route 2, equivalent: a DigitalOcean App Platform static-site component at `/financial-inclusion-evidence`

This route was to be used only if the corporate site runs on App Platform and our security headers can be served.
DigitalOcean's current documentation, read on 3 October 2026, settles the second condition:

- **Headers: no.** A static-site component cannot send custom response headers. The app specification has no header
  field for static sites or ingress rules. Only CORS headers can be configured. Static sites are served with App
  Platform's own `Cache-Control`: 24 hours at the edge and 10 seconds in the browser, unless the edge cache is
  switched off. The public feature request for static-site headers is still open. So `Content-Security-Policy`,
  `X-Frame-Options`, `Permissions-Policy` and the other headers of `_headers` cannot be sent this way.
- **Path prefix.** An ingress rule that matches the prefix `/financial-inclusion-evidence` sends the request to the
  component. By default App Platform trims the matched prefix, so `/financial-inclusion-evidence/en/` reaches the
  component as `/en/`. `preserve_path_prefix: true` keeps it. With the default, the component would serve
  `build/site` as built, with `404.html` as its error document.
- **Rollback** would be App Platform's own: the app's Activity tab can roll back to any of the ten most recent
  successful deployments.
- **Decision.** This route cannot serve our security headers, so the proxy route stands. In any case the corporate site
  does not appear to run on App Platform (see above). Re-check at release only if DigitalOcean ships static-site
  headers.

Sources: DigitalOcean, "How to Manage Static Sites in App Platform" (last verified 13 July 2026); "Reference for App
Specification" (1 September 2026); "How to Configure Edge Settings in App Platform" (29 June 2026); "How to Manage
Deployments in App Platform"; and the feature request "Static site headers and routing" on ideas.digitalocean.com.

### Route 3, fallback: `evidence.causewaygrp.com`, with a 301 from the subpath

- **Origin.** `public_origin` is `https://evidence.causewaygrp.com`, with no path. The base path is then empty, and the
  published site has the same layout as `dist/`.
- **DNS and host.** The same Pages project serves the site at its root. One CNAME, `evidence` → `<project>.pages.dev`,
  goes in DigitalOcean DNS, and the domain is added to the Pages project. Pages accepts a subdomain on outside DNS
  through a CNAME; the apex would need the zone on Cloudflare.
- **The 301.** The corporate application redirects the old path:
  `'/financial-inclusion-evidence/**': { redirect: { to: 'https://evidence.causewaygrp.com/**', statusCode: 301 } }`,
  plus the bare path.
- **Security headers.** Pages serves them from `_headers` directly. The corporate application answers only the 301.
- **Nothing corporate added.** Our pages are on another host name. The `session` cookie is host-only (it has no
  `Domain` attribute), so browsers do not send it to `evidence.causewaygrp.com`. The 301 response may carry the
  corporate cookie and robots header, but it has no content.
- **Rollback.** Pages rollback, as in route 1. Removing the redirect returns the subpath to the corporate site.
- Choose the route before release: changing the origin later changes every canonical address.

### Search engines: a step for the web administrator

Crawlers read `robots.txt` only at the root of a host: `https://causewaygrp.com/robots.txt`. They ignore the
`robots.txt` the build writes under the path. At release, the web administrator does one of these:

- adds `Sitemap: https://causewaygrp.com/financial-inclusion-evidence/sitemap.xml` to the domain's root `robots.txt`,
  and makes sure no `Disallow` rule there covers `/financial-inclusion-evidence/`; or
- submits that sitemap in Google Search Console (and Bing Webmaster Tools) for the `causewaygrp.com` property.

Two more facts for the web administrator:

- **HSTS.** Under route 1, a `Strict-Transport-Security` header sent by our pages applies to all of `causewaygrp.com`,
  and with `includeSubDomains` to every subdomain. That is a decision for the whole domain. It is made by the web
  administrator, not by this resource (step 9).
- **Local storage.** The language choice is stored in the browser as `yfie-lang` for the origin. Under route 1 that
  storage belongs to `causewaygrp.com` and is shared with the corporate pages; the key is ours alone.

## Steps

| # | Step | Who | How | Done when |
|---|---|---|---|---|
| 1 | **Account and domain.** A Cloudflare account for the Pages project. The domain stays where it is (DigitalOcean DNS): route 1 needs no DNS change, route 3 one CNAME ("Hosting"). | Owner | Cloudflare dashboard | The account exists |
| 2 | **Licence decision for downloads.** Decide whether the data exports (`scripts/exports.py`) may be published, and under what terms. | Owner | A dated line in `audit/OWNER_DECISIONS_*.md` | The decision is recorded. If it is yes, Claude Code sets `public_downloads: true` in `site-src/deployment.json`, after the codebook's bilingual review, and states the terms on /data/ Master-first |
| 3 | **Origin.** Set `public_origin` in `site-src/deployment.json` to `https://causewaygrp.com/financial-inclusion-evidence` (route 1, the decided address) or `https://evidence.causewaygrp.com` (route 3): no trailing slash. In the same commit, lift RC-B14's condition that `public_origin` is null (it holds owner decision B8 until then). Rebuild: `python3 scripts/social_images.py && python3 scripts/build.py && python3 scripts/audit_public_literals.py`. `dist/` keeps root-relative links for the gates; the published site, `scripts/build.py --out build/site`, carries the path. | Claude Code | One commit | The validator passes; canonical, hreflang, `og:url`, `og:image`, structured data and `sitemap.xml` are absolute and carry the path, and `robots.txt` allows crawling and names the sitemap (`scripts/discovery.py`, F6 gates); for route 1, `python3 scripts/tests/test_base_path.py` passes |
| 4 | **Currentness at the release date.** `python3 scripts/currentness_rerun.py --append`. Anything newer is read in its original and enters the Master by transaction. The edition date (`UI-CONTENT-VERSION`) moves to the release date, Master-first. | Claude Code | `run_stage.py` | The appended result shows no unread NEWER item, and the "check by hand" points have been checked in a browser |
| 5 | **Every gate.** Every step of `.github/workflows/verify.yml`, locally and in CI: checksums, projection check, validator, literal-audit determinism, lineage, diagrams, social images, logo derivatives, bilingual invariance, content parity, exports, public tools, viewport acceptance, security headers, base path, negative controls. | Claude Code | CI on the release commit | CI is green on the commit that will be tagged |
| 6 | **Pages project and credentials.** Create the Cloudflare Pages project for direct uploads. Create an API token limited to "Cloudflare Pages: Edit". | Owner | Cloudflare dashboard | The project name and the token exist |
| 7 | **Repository settings.** Secrets `CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID`; variables `YFIE_CF_PAGES_PROJECT` and `YFIE_DEPLOY_ENABLED=true`. | Owner (the secrets); Claude Code may set the variables where the session has settings access | GitHub → Settings → Secrets and variables → Actions | The deploy workflow is no longer skipped |
| 8 | **Deploy, then route the address.** Merge to `main`, or run "Deploy" by hand (workflow_dispatch). The workflow refuses a null origin, runs the gates, proves `dist/` is a fresh build, builds the published site, sweeps it under its path, then uploads it. Then the corporate route of "Hosting" is applied in CauseWay's frontend repository: route 1, the proxy and its exclusions; route 3, the CNAME and the 301. | Claude Code (merge on the owner's approval of the PR); the route by CauseWay's web administrator | `.github/workflows/deploy.yml`; the frontend repository | The workflow is green, `https://<project>.pages.dev/financial-inclusion-evidence/` serves the site, and the checks of "What every route must keep" pass on `causewaygrp.com` |
| 9 | **Headers and HTTPS.** Check that HTTPS works on the address. `Strict-Transport-Security` is the domain's decision ("Hosting"): add it under `/*` in `site-src/hosting/_headers` only with the web administrator's agreement, since under route 1 it covers all of `causewaygrp.com` (and every subdomain with `includeSubDomains`); then rebuild and redeploy. Run `python3 scripts/tests/test_security_headers.py --base https://causewaygrp.com/financial-inclusion-evidence`. | Claude Code; HSTS on the web administrator's agreement | One commit; the test against the live host | Every page loads with every security header and no policy violation |
| 10 | **Every page on the live host.** `YFIE_BASE_URL=https://causewaygrp.com/financial-inclusion-evidence python3 scripts/tests/test_public_tools.py` against the live address; the live run bypasses the page policy, which step 9 tests (viewport acceptance runs on the same build in step 5). Remeasure performance with `scripts/performance_budget.py`, adapted to the origin, and record the result beside `release_candidate_b14d` in `docs/SUSTAINABILITY_IMPLEMENTED_RUNTIME.json`. A person opens the site on a phone in Yemen, or on a connection routed there, in Arabic. | Claude Code; the in-country check by a person the owner names | The tests; a dated note | The tests pass, the budget is met or its miss is recorded, and the in-country check is recorded |
| 11 | **Usage counts (optional).** Only cookieless, first-party, aggregate counts with no personal data. The /privacy/ page must say so in both languages, Master-first, *before* activation, as it requires. | Owner decides; Claude Code implements | A Master transaction for /privacy/, then the code | Activated only after the Privacy page is live |
| 12 | **Open items.** Every item in `FINAL_OPEN_ITEMS_REGISTER.md` and `design/ESCALATIONS.md` marked RELEASE is done or re-dispositioned (`audit/release_candidate/OPEN_ITEMS_DISPOSITION.md`). | Claude Code | Dated lines | No RELEASE item is open |
| 13 | **Release acceptance.** The owner reviews the live site and the records, and accepts the release. | Owner | A dated, signed acceptance line in `audit/OWNER_DECISIONS_*.md` | Recorded |
| 14 | **Tag.** The owner pushes the release tag on the accepted commit of `main`. | Owner | `git tag -s v1.0.0 <commit> && git push origin v1.0.0` | The tag exists; the release is the tagged commit |

## Rolling back

Each route's rollback is under "Hosting". For a faulty deployment: Cloudflare Pages keeps every deployment, and
"Rollback to this deployment" in the dashboard restores the previous one at once (Owner or Claude Code with dashboard
access); the corporate route needs no change. The repository then reverts the faulty commit on a branch, CI goes green,
and a new deploy goes out (Claude Code). History is never rewritten.

## What this runbook does not do

- It does not decide anything that belongs to the owner: the account, the domain, the licence, the acceptance and the tag.
- It changes nothing outside this repository. The corporate application, the DNS and the domain's `robots.txt` are
  changed by CauseWay's web administrator, in their own repository and accounts.
- It does not claim WCAG conformance, legal review, rights clearance, native-language certification or a security
  guarantee. The header test checks the policy the site sends; it is not a security assessment.
- It does not turn a local measurement into an operational or carbon figure.
