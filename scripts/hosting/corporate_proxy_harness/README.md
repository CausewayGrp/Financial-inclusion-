# Corporate proxy harness (R-09)

A minimal Nitro 2.13.4 server (pinned in `package-lock.json`) that stands in for CauseWay's corporate Nuxt site, so the
forwarding middleware printed in `docs/RELEASE_RUNBOOK.md` ("Route 1") can be tested as written. It is never deployed.

`python3 scripts/tests/test_corporate_proxy.py` copies this folder to a temporary directory, writes the middleware
**extracted from the runbook** (only the `UPSTREAM` constant is replaced, by a local nginx running our own server
block), runs `npm ci` and `nitropack build`, and checks the route end to end. It needs Node.js 20 or later, npm with
registry access, and nginx. It is not part of CI: it installs packages from the npm registry, and the release step it
supports (runbook step 8) happens once, in CauseWay's frontend repository.

What it proves, and what it does not: see the docstring of `scripts/tests/test_corporate_proxy.py`.
