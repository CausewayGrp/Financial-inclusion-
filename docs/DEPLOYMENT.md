# Deployment

**Status:** nothing is deployed. The public site is not released (the programme never declares PUBLIC RELEASE READY);
this page states how the build in `dist/` would be served. It is the header, discovery and privacy contract that the
implementation keeps; it is not a claim of any live security test. Since EAD-01 `dist/` is the production runtime's
output — the accepted design rendered by `scripts/yfie` through `scripts/build.py` — not a pre-design baseline.

The repository is canonical on GitHub (`CausewayGrp/Financial-inclusion-`, branch `main`). `dist/` is committed and CI
fails if it differs from a fresh build, so the files a host would serve are exactly the reviewed ones.

## Build and verify

```bash
python3 -m pip install -r requirements.txt
python3 scripts/generate_projections.py --check   # Master → projections, byte for byte
python3 scripts/social_images.py --check           # the governed social images cover every route and are current
python3 scripts/build.py                          # site-src/content → dist, through scripts/yfie (288 HTML files)
python3 scripts/audit_public_literals.py          # every public number traced
python3 scripts/validate.py                       # all repository gates, including F6-G01…G08 below
```

## Serve

- Serve **only** the contents of `dist/` as static files. Never serve `authority/`, `audit/`, `site-src/`, `scripts/`,
  `handoff/` or the Production Master; the browser never parses the Master.
- Unknown routes → `dist/404.html` (bilingual, Arabic first, `noindex`). Keep trailing-slash paths (`/en/people/`).
- `/` is the neutral entry route and the hreflang `x-default`: `assets/lang-redirect.js` opens the edition the reader
  chose before (stored preference `yfie-lang`), otherwise Arabic; without JavaScript it falls back to `/ar/`.
- No database, secret, account, cookie or live API is required. Search and Compare read local JSON under
  `/static-data/` and JSON blocks in the page. Fonts are served from `/assets/fonts/` on the same origin: the six IBM
  Plex faces the stylesheet declares, with their OFL licence. No font CDN, and no external request of any kind.

## Discovery (F6)

One implementation, `scripts/discovery.py`, used by the build and checked by the validator.

| Item | Contract |
|---|---|
| Public origin | `site-src/deployment.json` → `public_origin`: **null** until the owner fixes the release domain (release-only decision). Never guessed |
| Canonical | Self-canonical in the page's own language |
| hreflang | Every page lists `en`, `ar` and `x-default` (→ `/`); the pair is reciprocal |
| robots.txt | Origin null (now): `Disallow: /` — a pre-release build is not for indexing. Origin set: `Allow: /` and `Sitemap:` |
| sitemap.xml | Written only with an origin: every localized page once (286), each with its three alternates; no `lastmod` (the Master holds no page-level modification date) |
| Titles and descriptions | One native `<title>` and one meta description per page, unique within each language; one `<h1>` |
| Structured data | `WebSite` on Home; `BreadcrumbList` where a breadcrumb is shown (Evidence Records, Readings), with the visible names; `Article` on the ten Readings (headline, description = standfirst, language, publisher CauseWay, part of the resource). No author, dates or `Dataset`: none is governed, and the resource publishes evidence records and a source directory, not datasets |
| Social image | `og:image` is the page's own 1200 × 630 image, rasterised from the design's governed template (EAD-09) and served from `/assets/social/`; root-relative before an origin is set, absolute after, like every other URL here. `og:image:alt` is the page's own title; the card type is `summary_large_image` |
| Search | Local index (`static-data/search_index.json`): page, question, evidence, Reading, Measurement, source and source-locator result types |

When the origin is set the same build makes every canonical, hreflang, sitemap and structured-data URL absolute; nothing
else changes.

## Security and privacy expectations for Code

The reference build is written so that a strict policy works as is: no inline executable script (page data travels in
`<script type="application/json">` blocks), no inline style, no inline event handler, no external script, stylesheet,
font, image or frame, no form (gate F6-G05). The host should send:

| Header | Value |
|---|---|
| `Content-Security-Policy` | `default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:; font-src 'self'; connect-src 'self'; object-src 'none'; base-uri 'self'; form-action 'none'; frame-ancestors 'none'; upgrade-insecure-requests` |
| `Strict-Transport-Security` | `max-age=31536000; includeSubDomains` once HTTPS is confirmed on the release domain |
| `X-Content-Type-Options` | `nosniff` |
| `Referrer-Policy` | `strict-origin-when-cross-origin` |
| `Permissions-Policy` | `camera=(), microphone=(), geolocation=(), payment=(), usb=()` |
| `Cross-Origin-Opener-Policy` | `same-origin` |

### Host configuration, in the repository (B14 b, 3 October 2026)

`site-src/hosting/_headers` holds the headers above, plus cache rules: five minutes, revalidated, for HTML and the
search data; an hour for assets whose names are not fingerprinted; thirty days for the canonical fonts.
`scripts/build.py` copies it unchanged to `dist/_headers`. Cloudflare Pages and Netlify read that file from the publish
root. Its path rules never overlap, because both hosts would join two values of one header.

`Strict-Transport-Security` stays commented out until HTTPS is confirmed on the release domain (`docs/RELEASE_RUNBOOK.md`).

**GitHub Pages cannot set response headers.** It would serve `_headers` as an ordinary file. If GitHub Pages is ever
used, the policy can come only from a `<meta http-equiv="Content-Security-Policy">`. That cannot carry `frame-ancestors`
or the other headers, so it is not the recommended host.

`scripts/tests/test_security_headers.py` serves `dist/` locally under `dist/_headers` and loads every page in headless
Chromium. It fails on any policy violation, failed request or script error. It is a local check of the file and makes no
claim about any live host.

### Data exports, switched off (B14 a, 3 October 2026)

`scripts/exports.py` writes six datasets to `build/exports/`, never to `dist/`: the Evidence Records, the public claims,
the sources, the visual rows, the chronology and the Measurement Agenda. Each comes as CSV and JSON, with a bilingual
codebook and provenance on every row: record ID, source IDs, public locators and the Master's SHA-256.

`scripts/tests/test_exports.py` proves every value against the projections. CI attaches the files as the artefact
`yfie-data-exports`.

Publishing them is one switch: `public_downloads` in `site-src/deployment.json`. It stays `false` until CauseWay's
counsel confirms the CC BY 4.0 text (the owner adopted the licence on 3 October 2026). While it is false, the validator (RC-B14) fails if a download appears in `dist/`.

- **Rendering.** `app.js` builds result and comparison markup from governed JSON and escapes every value (`esc`); Code
  must keep escaping (or Trusted Types) for anything rendered from data, and must not render source text as HTML.
- **External links.** Links to original sources open in a new tab with `rel="noopener noreferrer"`; the site fetches
  nothing from them.
- **Privacy.** One functional preference is stored on the reader's device (`yfie-lang`, the chosen language). There is
  no analytics, tracking, cookie, account or form, and reports go by e-mail to `office@causewaygrp.com`. Adding any
  analytics or telemetry needs an owner decision, an updated Privacy page in both languages and, where required,
  consent — before it ships.
- **Repository hygiene.** No secret or credential pattern in any tracked file (F6-G06); no bundled source document — the
  only tracked office file is the Production Master (F6-G07); every source record states its rights and card state
  (F6-G08). Reuse terms of the original sources have not been assessed (`rights_state: NOT_ASSESSED`); the site links to
  sources and does not republish them.
- **Assets.** The master logo is a 10 MB PNG and is never redrawn, recoloured, filtered, cropped or masked; the
  pre-design baseline's CSS filter on it went with that renderer at EAD-01. Web-size derivatives (EAD-03) need the
  owner's approval, and cache fingerprinting is release-only engineering (TOOL-02). HTML should be served with short
  caching; assets may be cached long only once their file names are fingerprinted.
