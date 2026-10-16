# CI runbook

This runbook documents how to run the fast and full CI locally and how the verify-fast/verify-full split works.

verify-fast (PR gating):
- Linters, small unit tests, smoke browser checks
- Command (local):
  - python -m venv .venv && . .venv/bin/activate
  - pip install -r requirements.txt
  - pytest -m "not integration"

verify-full (main / nightly):
- Full generator, build, full browser acceptance
- Command (local):
  - python -m venv .venv && . .venv/bin/activate
  - pip install -r requirements.txt
  - python3 scripts/generate_projections.py
  - python3 scripts/build_site.py

Caching and Playwright notes:
- Playwright browsers are cached between runs; locally run `npx playwright install` once.
