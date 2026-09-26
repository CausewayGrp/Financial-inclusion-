# Deployment (reference build)

**Status:** nothing is deployed. The public site is not released (the programme never declares PUBLIC RELEASE READY);
this page states how the *reference* build would be served so that Design and Code inherit correct assumptions.

The repository is canonical on GitHub (`CausewayGrp/Financial-inclusion-`, branch `main`). `dist/` is committed and CI
fails if it differs from a fresh build, so the files a host would serve are exactly the reviewed ones.

## Build and verify

```bash
python3 -m pip install -r requirements.txt
python3 scripts/generate_projections.py --check   # Master → projections, byte for byte
python3 scripts/build.py                          # site-src → dist (288 HTML files)
python3 scripts/audit_public_literals.py          # every public number traced
python3 scripts/validate.py                       # all repository gates
```

## Serve

- Serve **only** the contents of `dist/` as static files. Never serve `authority/`, `audit/`, `site-src/`, `scripts/`,
  `handoff/` or the Production Master; the browser never parses the Master.
- Unknown routes → `dist/404.html` (bilingual, Arabic first). Keep trailing-slash paths (`/en/people/`).
- `/` redirects to `/ar/` unless the reader chose English before (stored preference `yfie-lang`).
- No database, secret or live API is required. Search and Compare read local JSON under `/static-data/`.
- Security headers, caching, image delivery for the master logo and analytics policy are engineering decisions recorded
  in `handoff/ENGINEERING_HANDOFF_EXPECTATIONS.md`; none is configured here.
