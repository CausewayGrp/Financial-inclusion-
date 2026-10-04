# The App Platform service image for the DigitalOcean release route (owner decision of 3 October 2026;
# docs/RELEASE_RUNBOOK.md, "Hosting"): nginx serving the published site under its base path, with the header contract
# of `_headers` written as an nginx server block by scripts/hosting_nginx.py. An App Platform static-site component
# cannot send custom response headers, so the site runs as a service.
#
# Built only by .github/workflows/deploy.yml, after every gate, from the staged context build/do/:
#   build/do/default.conf   python3 scripts/hosting_nginx.py --site build/site --out build/do/default.conf
#   build/do/site/          the published site, python3 scripts/build.py --out build/site, without its _headers
# The same block is proved in a real nginx by scripts/tests/test_digitalocean_hosting.py.
# R-17 (independent review of 70398d1): pinned by digest to nginx 1.24.0, the version the gates prove
# (scripts/tests/test_digitalocean_hosting.py runs the block in Ubuntu's nginx 1.24.0, and with --image in this image).
# Move the pin only together with that test: a new nginx can read the same block differently.
FROM nginx:1.24.0-alpine@sha256:77e5d4a6ad906c5d3793764085706577fa705b1dc6f244ea0241c4b5e2155385
ARG BASE=financial-inclusion-evidence
RUN rm -f /etc/nginx/conf.d/default.conf
COPY default.conf /etc/nginx/conf.d/yfie.conf
COPY site/ /usr/share/nginx/html/${BASE}/
EXPOSE 8080
