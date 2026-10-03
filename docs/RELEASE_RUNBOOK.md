# Release runbook — from "the owner has a hosting account and a domain" to "live"

**Status, 3 October 2026:** prepared, not started. Nothing here has been executed. The site is not released; this
repository never declares PUBLIC RELEASE READY, and only the owner releases it (step 14). Each step names who does it.
Every step except the account, the domain, the licence decision, the release acceptance and the tag is a Claude Code
step; the route on `causewaygrp.com` is CauseWay's web administrator's ("Hosting").

## Deploy and verify (one page)

Written for someone who has never seen this repository. The steps table further down says who decides what; this page
says how to do it and what you should see. `$B` is the address being checked:
`https://causewaygrp.com/financial-inclusion-evidence` once the corporate route exists, or
`https://<app>.ondigitalocean.app/financial-inclusion-evidence` (the App Platform app's own address) before it.

**Before you start**

- Python 3.11, Git and nginx (`apt-get install nginx-light`; the GitHub runner image has it).
- `git clone https://github.com/CausewayGrp/Financial-inclusion-.git && cd Financial-inclusion-`
- `python3 -m pip install -r requirements.txt`, then `python3 -m playwright install chromium` for the browser tests.
- A DigitalOcean account with a Container Registry, and a personal access token with write access to that registry
  and to App Platform, stored as the repository secret `DIGITALOCEAN_ACCESS_TOKEN`; the variables `YFIE_DO_REGISTRY`
  and, after the first deploy has created the app, `YFIE_DO_APP_ID` (step 7).
- The owner's dated lines in `audit/OWNER_DECISIONS_*.md` for steps 2 and 7a (step 13 only at release).
  `site-src/deployment.json` then has `public_origin` set and `licence_text_confirmed: true`. The deploy workflow
  refuses to publish otherwise.

**Build and check**, each command with the last line it must print:

```bash
python3 scripts/checksums.py --check                 # CHECKSUM MANIFEST CURRENT: <n> files
python3 scripts/validate.py                          # WEBSITE REPOSITORY VALIDATION PASS
python3 scripts/build.py --out build/site            # Built <n> HTML files from <n> controlled page specs … under /financial-inclusion-evidence
python3 scripts/tests/test_base_path.py              # BASE PATH: PASS — https://causewaygrp.com/financial-inclusion-evidence/
python3 scripts/tests/test_security_headers.py       # SECURITY HEADERS: PASS — … 0 problems
python3 scripts/tests/test_digitalocean_hosting.py   # DIGITALOCEAN HOSTING: PASS — the nginx block of _headers, … 0 problems
```

**Deploy.** Merge the approved pull request into `main`, or run the "Deploy to DigitalOcean" workflow by hand (GitHub →
Actions → Run workflow). It refuses a null origin or an unconfirmed licence text, runs the gates, builds the site
under its path, sweeps it, proves its nginx block in a real nginx, builds the image
(`site-src/hosting/digitalocean/Dockerfile`), pushes it to the registry tagged with the commit, points the app at it
(`scripts/do_deploy.py`) and waits until App Platform reports the deployment ACTIVE. The first run, with
`YFIE_DO_APP_ID` unset, creates the app and prints its id. Done when the run is green and
`https://<app>.ondigitalocean.app/financial-inclusion-evidence/` opens the Arabic edition.

**The ten-minute check**, after every deploy:

```bash
B=https://causewaygrp.com/financial-inclusion-evidence
for u in / /ar/ /en/ /en/payments/ /ar/evidence/CLM-001/ /assets/app.js /static-data/search_index.json /en/no-such-page/; do
  echo "== $u"; curl -sSI "$B$u" | grep -iE '^(HTTP|set-cookie|x-robots-tag|x-powered-by|content-security-policy|location)'
done
#   every address: HTTP 200 (the last one: 404) and a content-security-policy line;
#   never a set-cookie, x-robots-tag or x-powered-by line, and no location line
curl -sSL -o /dev/null -w '%{http_code} %{num_redirects}\n' "$B"           # 200 1   (the bare address: one redirect to "$B/")
curl -sSI "$B/en/payments" | grep -iE '^(HTTP|location)'                     # 301, location: /financial-inclusion-evidence/en/payments/
#                                                                              (relative: never an ondigitalocean.app host)
curl -s "$B/en/" | grep -c 'name="robots" content="noindex, nofollow"'       # 1 before step 13; 0 after it
curl -sSI "$B/sitemap.xml" | grep -iE '^(HTTP|content-type)'                 # 200 and application/xml
python3 scripts/tests/test_security_headers.py --base "$B"                   # SECURITY HEADERS: PASS — … 0 problems
YFIE_BASE_URL="$B" python3 scripts/tests/test_public_tools.py               # PUBLIC TOOL TESTS PASS: …
```

`test_security_headers.py --base` loads every page and reads every response with all its headers. It fails on any
`Set-Cookie`, `X-Robots-Tag` or `X-Powered-By`, on any cookie the browser holds afterwards, on a missing page that does
not answer 404, and on a bare address that does not answer one permanent redirect to `$B/` (301, from the corporate
route or from nginx itself). Finish by opening `$B/` on a phone: the Arabic edition opens, the language switch works,
and a search for "remittances" finds results.

**Roll back.**

1. DigitalOcean control panel → Apps → the app → Activity → the last good deployment → "Rollback". App Platform keeps
   the recent successful deployments, and the rollback takes effect without a rebuild; nothing else changes.
2. If the corporate route misbehaves, remove `server/middleware/0.financial-inclusion-evidence.ts` from CauseWay's
   frontend and redeploy the corporate site. The path then answers with the corporate site's own 404.
3. In this repository, revert the faulty commit on a branch (`git revert <commit>`). When CI is green, merge it, and
   the next deploy goes out. History is never rewritten.

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

The checks are the ten-minute check of "Deploy and verify", run on the live address in steps 8 to 10.

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
- The deploy workflow builds the published site, sweeps it with the same test, proves its nginx block in a real nginx,
  and ships it as an image that holds the site under `financial-inclusion-evidence/` (route 1).
- Every page declares its icon, the 32 px derivative under `assets/logo/` (RC-18), so browsers no longer ask the domain
  root for `/favicon.ico`, and no request leaves the path.
- The build checks every slash-leading string in the runtime, not only the ones that name a folder of the site. After
  its own rewrites, each such string must be a listed route key, and it must occur exactly as often as listed
  (`JS_ROUTE_KEYS` in `scripts/base_path.py`). Anything else stops the build. This includes an address built by
  concatenation or a template, such as `'/'+lang+'/about/'`. The sweep applies the same rule, and a second negative
  control proves that it does.
- No host has been tested from inside Yemen. Step 10 asks a person with local access to open the live site before the
  owner accepts the release. GitHub Pages is not an option, because it cannot send security headers
  (`docs/DEPLOYMENT.md`).

### Route 1, decided: our own App Platform app, an nginx service, reached through the corporate site

Owner decision of 3 October 2026 (22:36 Aden): production hosting is DigitalOcean, under CauseWay's domain, at
`https://causewaygrp.com/financial-inclusion-evidence/`. It replaces the earlier preference for a Cloudflare Pages
project, which this runbook no longer describes.

```text
reader → causewaygrp.com (DigitalOcean DNS → the corporate Nuxt application on its Droplet)
           └─ /financial-inclusion-evidence/**  → proxy, path unchanged →  https://<app>.ondigitalocean.app/financial-inclusion-evidence/**
                                                                            (App Platform service: nginx, site-src/hosting/digitalocean/)
```

Why this shape, from facts that can be checked:

- **The corporate site does not run on App Platform.** Re-checked on 3 October 2026 at about 19:50 UTC with one
  read-only request: `causewaygrp.com` still resolves to the single DigitalOcean address `206.189.57.121`, and the
  response carries `x-powered-by: Nuxt`, the `session` cookie and the `x-robots-tag`, but no `cf-ray` or
  `server: cloudflare` (App Platform serves through its Cloudflare edge). So our site cannot simply be a component of
  the corporate app at the subpath; the corporate site has to forward the path to a separate deployment.
- **A static-site component cannot send our headers** (route 2 below), so the separate deployment is a *service*: an
  nginx image holding the published site under its path. Its server block is written by `scripts/hosting_nginx.py`
  from the site's own `_headers`, so the header contract stays one file. `scripts/tests/test_digitalocean_hosting.py`
  runs that block in a real nginx in CI and loads every page through `test_security_headers.py --base`, with a
  negative control.

- **Our side (this repository).** The deploy workflow builds the image and deploys it ("Deploy and verify"). The app's
  own address, `https://<app>.ondigitalocean.app/financial-inclusion-evidence/`, is the same site, so steps 9 and 10
  can test it before the proxy exists. App specification: `site-src/hosting/digitalocean/app_spec.json` (one service,
  port 8080, health check on the base path, the smallest instance). It has not yet been run against DigitalOcean; the
  first deploy (step 8) is its test.
- **The corporate side.** A later, separate task in CauseWay's own frontend repository, not part of this pull request.
  The code below is guidance only. It is one server middleware, not `routeRules`. The adversarial verification of
  3 October 2026 ran both in a real Nitro 2.13.4 server in front of a stand-in host, and found that `routeRules`
  cannot do this job:
  - a redirect rule for the bare path also matches the address with its slash, so the release address redirects to
    itself forever;
  - a route-rule proxy cannot remove response headers, so the corporate `session` cookie, `x-robots-tag` and
    `x-powered-by` still reach our responses;
  - the route-rule proxy follows our host's own redirects itself.

  The middleware below did the job in the same test:
  - it removed those three headers;
  - it sent an empty `Cookie` upstream;
  - it passed our host's redirect on with its relative `Location`;
  - it answered the bare path with one 301, without a loop;
  - it left `/financial-inclusion-evidencex` alone.

  ```ts
  // server/middleware/0.financial-inclusion-evidence.ts in CauseWay's frontend repository: guidance, not applied from here.
  // Remove any routeRules entry for /financial-inclusion-evidence.
  import { proxyRequest, sendRedirect } from 'h3'
  const BASE = '/financial-inclusion-evidence'
  const UPSTREAM = 'https://<app>.ondigitalocean.app'
  const STRIP = ['set-cookie', 'x-robots-tag', 'x-powered-by']
  export default defineEventHandler((event) => {
    const path = event.path.split('?')[0]
    if (path !== BASE && !path.startsWith(BASE + '/')) return
    if (path === BASE) return sendRedirect(event, BASE + '/' + event.path.slice(BASE.length), 301)
    return proxyRequest(event, UPSTREAM + event.path, {
      headers: { cookie: '' },                 // the corporate session cookie never reaches our host
      fetchOptions: { redirect: 'manual' },    // our host's redirects reach the reader unchanged
      onResponse(ev) { for (const h of STRIP) ev.node.res.removeHeader(h) },
    })
  })
  ```

  If nginx sits in front of the Nuxt process, the same forward can be set there instead, with the same effect:
  `location /financial-inclusion-evidence/ { proxy_pass https://<app>.ondigitalocean.app; proxy_set_header Host <app>.ondigitalocean.app;
  proxy_ssl_server_name on; proxy_set_header Cookie ""; proxy_hide_header Set-Cookie; proxy_hide_header X-Robots-Tag;
  proxy_hide_header X-Powered-By; }`, plus `location = /financial-inclusion-evidence { return 301 /financial-inclusion-evidence/; }`.

- **Security headers.** nginx sends them from the generated block, on every response under the path (`always`: the
  404 and the redirects too); the middleware passes them through unchanged. The checks of "Deploy and verify" apply
  unchanged. nginx answers a directory without its slash with a 301 whose `Location` is relative
  (`absolute_redirect off`), so the app's own host name never reaches the reader.
- **Cache.** The block sends the `Cache-Control` of `_headers`. App Platform's edge sits in front of the service; the
  ten-minute check reads the `Cache-Control` the reader actually receives, and step 10 records it. If the edge holds a
  page longer than five minutes, a corrected record reaches readers later: record it, and purge the edge cache
  (the app's Settings) after a correction.
- **Nothing corporate added.**
  - The proxy returns our response body unchanged, so no corporate script is written into our pages. That is the
    guarantee. Under this route our policy's `'self'` is `https://causewaygrp.com`, so `script-src 'self'` would also
    allow the corporate site's own scripts (`/_nuxt/…`). It blocks inline scripts, but it does not separate us from
    the corporate site.
  - The web administrator confirms that no service worker is registered with scope `/` on `causewaygrp.com`. A service
    worker at that scope could reach our pages. On 3 October 2026, `/sw.js` answered 404.
  - `headers: { cookie: '' }` replaces the incoming `Cookie` header, so the `session` cookie never reaches our host.
  - nginx sends no `Set-Cookie`. The corporate application sets its `session` cookie and its `x-robots-tag` before
    routing; it does so even on its own 404 for this path. The middleware removes both from our responses, and any
    header the App Platform edge might add of the three. `test_security_headers.py --base` fails if one is still
    there, and it must pass before release.
- **The app's own address.** `<app>.ondigitalocean.app` serves the same pages. They do not compete in search, because
  every page's canonical names `causewaygrp.com` and, until step 13, every page says `noindex, nofollow`.
- **Rollback.** App Platform's Activity tab rolls back to an earlier successful deployment at once; each image is
  also kept in the registry under its commit. The proxy needs no change. If the proxy itself misbehaves, removing the
  middleware file (one commit in the frontend repository) takes the path down; route 3 can then be used.
- **Cost and region.** One service at the smallest instance size, plus the registry. The region is the owner's choice
  (add `"region"` to the app specification, or move the app in the control panel); it is not a release condition.

### Route 2, alternative: the same nginx block on the corporate Droplet, with no proxy

If the corporate Droplet's front server is nginx, and the web administrator prefers it, the published site can be
served from the Droplet itself: copy `build/site` (without `_headers`) to a directory on the Droplet, and include the
generated block's `location` sections in the existing `causewaygrp.com` server, with `root` pointing at the directory
that holds `financial-inclusion-evidence/`. There is then no proxy hop and the corporate application never sees the
path. Conditions: the corporate server must not set `add_header` lines that the included locations would not replace
(nginx inherits none into a location that sets its own, which the block does), and deployment becomes a copy to the
Droplet (an SSH key as a repository secret) instead of an image. It is not the decided route because it couples our
deploys and rollback to the corporate server; the front server is not visible from outside (the response carries no
`server` header).

A DigitalOcean App Platform **static-site** component at the subpath was examined and rejected on 3 October 2026,
from DigitalOcean's documentation: a static-site component cannot send custom response headers (the app
specification has no header field for static sites or ingress rules; only CORS headers can be set), and static sites
are served with App Platform's own `Cache-Control`. `Content-Security-Policy`, `X-Frame-Options`,
`Permissions-Policy` and the other headers of `_headers` could not be sent that way. Sources: DigitalOcean, "How to
Manage Static Sites in App Platform"; "Reference for App Specification"; "How to Configure Edge Settings in App
Platform"; the feature request "Static site headers and routing" on ideas.digitalocean.com. Re-check only if
DigitalOcean ships static-site headers.

### Route 3, fallback: `evidence.causewaygrp.com`, with a 301 from the subpath

- **Origin.** `public_origin` is `https://evidence.causewaygrp.com`, with no path. The base path is then empty, and the
  published site has the same layout as `dist/`; `scripts/hosting_nginx.py` writes the block for the root.
- **DNS and host.** The same App Platform app serves the site under a custom domain: add `evidence.causewaygrp.com`
  in the app's Settings → Domains (App Platform issues the certificate), and, because the domain's DNS is at
  DigitalOcean, let App Platform create the record or add the CNAME it names.
- **The 301.** The corporate application redirects the old path. Use the same middleware form as route 1, so that the
  bare path and the path with a slash are told apart:
  `if (path === BASE || path.startsWith(BASE + '/')) return sendRedirect(event, 'https://evidence.causewaygrp.com' + (event.path.slice(BASE.length) || '/'), 301)`.
- **Security headers.** nginx serves them directly. The corporate application answers only the 301.
- **Nothing corporate added.** Our pages are on another host name. The `session` cookie is host-only (it has no
  `Domain` attribute), so browsers do not send it to `evidence.causewaygrp.com`. The 301 response may carry the
  corporate cookie and robots header, but it has no content.
- **Rollback.** App Platform rollback, as in route 1. Removing the redirect returns the subpath to the corporate site.
- Choose the route before release: changing the origin later changes every canonical address.

### Search engines: a step for the web administrator

Crawlers read `robots.txt` only at the root of a host: `https://causewaygrp.com/robots.txt`. They ignore the
`robots.txt` the build writes under the path. Until release, therefore, every page says it itself: while `pre_release`
is true in `site-src/deployment.json`, every page carries `<meta name="robots" content="noindex, nofollow">`. That
includes the root entry and the 404 (owner decision B3; gate RC-NOINDEX). At release `pre_release` goes false (step
13), and the web administrator does one of these:

- adds `Sitemap: https://causewaygrp.com/financial-inclusion-evidence/sitemap.xml` to the domain's root `robots.txt`,
  and makes sure no `Disallow` rule there covers `/financial-inclusion-evidence/`; or
- submits that sitemap in Google Search Console (and Bing Webmaster Tools) for the `causewaygrp.com` property.

The noindex meta is in the pages only. Before release, the sitemap, the search data and the social images can be
fetched with no noindex signal. They are not pages, the pages that link to them say `noindex, nofollow`, and no
sitemap is named anywhere until step 13, so this is accepted rather than covered by an `X-Robots-Tag` header (which
the route 1 proxy would have to be taught to keep).

Two more facts for the web administrator:

- **HSTS.** Under route 1, a `Strict-Transport-Security` header sent by our pages applies to all of `causewaygrp.com`,
  and with `includeSubDomains` to every subdomain. That is a decision for the whole domain. It is made by the web
  administrator, not by this resource (step 9).
- **Local storage.** The language choice is stored in the browser as `yfie-lang` for the origin. Under route 1 that
  storage belongs to `causewaygrp.com` and is shared with the corporate pages; the key is ours alone.

## Steps

| # | Step | Who | How | Done when |
|---|---|---|---|---|
| 1 | **Account and domain.** A DigitalOcean account (the decided host) with a Container Registry. The domain stays where it is (DigitalOcean DNS): route 1 needs no DNS change, route 3 one record that App Platform names ("Hosting"). | Owner | DigitalOcean control panel | The account and the registry exist |
| 2 | **Licence decision for downloads.** Decide whether the data exports (`scripts/exports.py`) may be published, and under what terms. | Owner | A dated line in `audit/OWNER_DECISIONS_*.md` | The decision is recorded. If it is yes, Claude Code sets `public_downloads: true` in `site-src/deployment.json`, after the codebook's bilingual review, and states the terms on /data/ Master-first |
| 3 | **Origin.** Set `public_origin` in `site-src/deployment.json` to `https://causewaygrp.com/financial-inclusion-evidence` (route 1, the decided address) or `https://evidence.causewaygrp.com` (route 3): no trailing slash. In the same commit, lift RC-B14's condition that `public_origin` is null (it holds owner decision B8 until then). `pre_release` stays true: the pages stay `noindex, nofollow` until step 13. Rebuild: `python3 scripts/social_images.py && python3 scripts/build.py && python3 scripts/audit_public_literals.py`. `dist/` keeps root-relative links for the gates; the published site, `scripts/build.py --out build/site`, carries the path. | Claude Code | One commit | The validator passes; canonical, hreflang, `og:url`, `og:image`, structured data and `sitemap.xml` are absolute and carry the path, and `robots.txt` allows crawling and names the sitemap (`scripts/discovery.py`, F6 gates); for route 1, `python3 scripts/tests/test_base_path.py` passes |
| 4 | **Currentness at the release date.** `python3 scripts/currentness_rerun.py --append`. Anything newer is read in its original and enters the Master by transaction. The edition date (`UI-CONTENT-VERSION`) moves to the release date, Master-first. | Claude Code | `run_stage.py` | The appended result shows no unread NEWER item, and the "check by hand" points have been checked in a browser |
| 5 | **Every gate.** Every step of `.github/workflows/verify.yml`, locally and in CI: checksums, projection check, validator, literal-audit determinism, lineage, diagrams, social images, logo derivatives, bilingual invariance, content parity, exports, public tools, viewport acceptance, security headers, base path, negative controls. | Claude Code | CI on the release commit | CI is green on the commit that will be tagged |
| 6 | **Credentials.** A DigitalOcean personal access token with write access to the registry and to App Platform (no wider scope than the deploy needs). The app itself is created by the first deploy (step 8). | Owner | DigitalOcean control panel → API | The token exists |
| 7 | **Repository settings.** Secret `DIGITALOCEAN_ACCESS_TOKEN`; variables `YFIE_DO_REGISTRY` and `YFIE_DEPLOY_ENABLED=true`; after the first deploy, `YFIE_DO_APP_ID` (the workflow prints it). | Owner (the secret); Claude Code may set the variables where the session has settings access | GitHub → Settings → Secrets and variables → Actions | The deploy workflow is no longer skipped |
| 7a | **Licence text confirmed by counsel.** CauseWay's counsel confirms the CC BY 4.0 text that /rights/ and /terms/ print, in both languages, before the first deploy makes them public at the app's own address. Then `licence_text_confirmed` goes to `true` in `site-src/deployment.json`, in the same commit as the dated line. Until then the deploy workflow refuses to publish, and `YFIE_DEPLOY_ENABLED` stays unset. | Owner, with counsel; Claude Code (the switch) | A dated line in `audit/OWNER_DECISIONS_*.md`; one commit | The confirmation is recorded and the switch is `true` |
| 8 | **Deploy, then route the address.** Merge to `main`, or run "Deploy to DigitalOcean" by hand (workflow_dispatch). The workflow refuses a null origin, runs the gates, proves `dist/` is a fresh build, builds the published site, sweeps it under its path, proves its nginx block in a real nginx, then builds, pushes and deploys the image and waits until it is live. Then the corporate route of "Hosting" is applied in CauseWay's frontend repository: route 1, the middleware with the app's address as `UPSTREAM`; route 3, the custom domain and the 301. | Claude Code (merge on the owner's approval of the PR); the route by CauseWay's web administrator | `.github/workflows/deploy.yml`; the frontend repository | The workflow is green, `https://<app>.ondigitalocean.app/financial-inclusion-evidence/` serves the site, and the ten-minute check of "Deploy and verify" passes on `causewaygrp.com` |
| 9 | **Headers and HTTPS.** Check that HTTPS works on the address. `Strict-Transport-Security` is the domain's decision ("Hosting"): add it under `/*` in `site-src/hosting/_headers` only with the web administrator's agreement, since under route 1 it covers all of `causewaygrp.com` (and every subdomain with `includeSubDomains`); then rebuild and redeploy. Run `python3 scripts/tests/test_security_headers.py --base https://causewaygrp.com/financial-inclusion-evidence`. | Claude Code; HSTS on the web administrator's agreement | One commit; the test against the live host | Every page loads with every security header and no policy violation |
| 10 | **Every page on the live host.** `YFIE_BASE_URL=https://causewaygrp.com/financial-inclusion-evidence python3 scripts/tests/test_public_tools.py` against the live address; the live run bypasses the page policy, which step 9 tests (viewport acceptance runs on the same build in step 5). Remeasure performance with `scripts/performance_budget.py`, adapted to the origin, and record the result beside `release_candidate_b14d` in `docs/SUSTAINABILITY_IMPLEMENTED_RUNTIME.json`. A person opens the site on a phone in Yemen, or on a connection routed there, in Arabic. | Claude Code; the in-country check by a person the owner names | The tests; a dated note | The tests pass, the budget is met or its miss is recorded, and the in-country check is recorded |
| 11 | **Usage counts (optional).** Only cookieless, first-party, aggregate counts with no personal data. The /privacy/ page must say so in both languages, Master-first, *before* activation, as it requires. | Owner decides; Claude Code implements | A Master transaction for /privacy/, then the code | Activated only after the Privacy page is live |
| 12 | **Open items.** Every item in `FINAL_OPEN_ITEMS_REGISTER.md` and `design/ESCALATIONS.md` marked RELEASE is done or re-dispositioned (`audit/release_candidate/OPEN_ITEMS_DISPOSITION.md`). | Claude Code | Dated lines | No RELEASE item is open |
| 13 | **Release acceptance, then indexing.** The owner reviews the live site and the records, and accepts the release. Then Claude Code sets `pre_release` to `false` in `site-src/deployment.json` (one commit: every page loses its `noindex, nofollow` meta, the 404 keeps its own `noindex`), rebuilds and deploys it, and the web administrator names the sitemap in the domain's root `robots.txt` or submits it in Search Console ("Hosting"). The tag (step 14) goes on that commit. | Owner (acceptance); Claude Code (the switch); the web administrator (the sitemap) | A dated, signed acceptance line in `audit/OWNER_DECISIONS_*.md`; one commit | Recorded; the live pages carry no `noindex`; the sitemap is named |
| 14 | **Tag.** The owner pushes the release tag on the accepted commit of `main`. | Owner | `git tag -s v1.0.0 <commit> && git push origin v1.0.0` | The tag exists; the release is the tagged commit |

## Rolling back

The three lines are in "Deploy and verify"; each route's rollback is under "Hosting". For a faulty deployment: App
Platform keeps the recent successful deployments, and "Rollback" in the app's Activity tab restores the previous one
at once (Owner, or Claude Code with control-panel access); the corporate route needs no change. The repository then
reverts the faulty commit on a branch, CI goes green, and a new deploy goes out (Claude Code). History is never
rewritten.

## What this runbook does not do

- It does not decide anything that belongs to the owner: the account, the domain, the licence, the acceptance and the tag.
- It changes nothing outside this repository. The corporate application, the DNS and the domain's `robots.txt` are
  changed by CauseWay's web administrator, in their own repository and accounts.
- It does not claim WCAG conformance, legal review, rights clearance, native-language certification or a security
  guarantee. The header test checks the policy the site sends; it is not a security assessment.
- It does not turn a local measurement into an operational or carbon figure.
