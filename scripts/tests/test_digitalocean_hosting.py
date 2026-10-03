#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The DigitalOcean release route serves the header contract (owner decision of 3 October 2026: production hosting is
DigitalOcean, at https://causewaygrp.com/financial-inclusion-evidence/).

  python3 scripts/tests/test_digitalocean_hosting.py               # build, serve in nginx, header test, negative control
  python3 scripts/tests/test_digitalocean_hosting.py --site DIR    # a site already built with the decided origin

Builds the published site for the decided origin into a temporary directory (`scripts/build.py --origin … --out …`;
site-src/deployment.json and dist/ are not touched), writes its nginx server block with `scripts/hosting_nginx.py` —
the configuration the App Platform image (site-src/hosting/digitalocean/Dockerfile) or a Droplet runs — and serves the
site from a real nginx on a local port. Then:

(a) `scripts/tests/test_security_headers.py --base <local nginx>/financial-inclusion-evidence` must PASS: every page,
    the root entry and the 404 load with every security header and no policy violation; no response carries
    Set-Cookie, X-Robots-Tag or X-Powered-By; a missing page answers 404; the bare address answers one permanent
    redirect to the address with its slash.
(b) The redirects carry a relative Location (no host name of the upstream leaks through the corporate proxy): a
    directory without its slash answers 301 to the same path with it; every Cache-Control value of `_headers` is sent
    for a path it covers; the sitemap is application/xml; an address outside the base path answers 404.
(c) Negative control: the same block with X-Frame-Options removed from the site-wide rule must make (a) FAIL.

Plain HTTP on a local port is the one difference from the live route: the policy is served without
`upgrade-insecure-requests` (`--local-http`), exactly as the local header test serves it. Needs nginx on PATH (the CI
runner image has it; `apt-get install nginx-light` elsewhere) and the browser of the header test.
"""
from __future__ import annotations

import argparse
import os
import shutil
import socket
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ORIGIN = "https://causewaygrp.com/financial-inclusion-evidence"
BASE = "/financial-inclusion-evidence"
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "scripts" / "tests"))
import hosting_nginx  # noqa: E402
from test_security_headers import headers_for, parse_headers  # noqa: E402

MIME = next((p for p in (Path("/etc/nginx/mime.types"), Path("/usr/local/etc/nginx/mime.types")) if p.exists()), None)


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None


def fetch(url: str) -> tuple[int, dict[str, str]]:
    opener = urllib.request.build_opener(_NoRedirect)
    try:
        with opener.open(url, timeout=10) as r:
            return r.status, {k.lower(): v for k, v in r.headers.items()}
    except urllib.error.HTTPError as e:
        return e.code, {k.lower(): v for k, v in e.headers.items()}


def start_nginx(work: Path, site: Path, block: str) -> tuple[subprocess.Popen, int]:
    s = socket.socket(); s.bind(("127.0.0.1", 0)); port = s.getsockname()[1]; s.close()
    www = work / "www"
    if not www.exists():
        www.mkdir(parents=True)
        shutil.copytree(site, www / BASE.strip("/"), ignore=shutil.ignore_patterns("_headers"))
    (work / "logs").mkdir(exist_ok=True)
    conf = work / "nginx.conf"
    who = "user root;\n" if os.geteuid() == 0 else ""   # as root, workers would drop to `nobody` and lose the temp tree
    conf.write_text(f"""{who}worker_processes 1;
pid {work}/nginx.pid;
error_log {work}/logs/error.log warn;
events {{ worker_connections 256; }}
http {{
    include {MIME};
    default_type application/octet-stream;
    access_log off;
    client_body_temp_path {work}/tmp_body; proxy_temp_path {work}/tmp_proxy; fastcgi_temp_path {work}/tmp_fcgi;
    uwsgi_temp_path {work}/tmp_uwsgi; scgi_temp_path {work}/tmp_scgi;
{block.replace("listen 8080;", f"listen 127.0.0.1:{port};").replace("root /usr/share/nginx/html;", f"root {www};")}
}}
""", encoding="utf-8")
    t = subprocess.run(["nginx", "-t", "-p", str(work), "-c", str(conf)], capture_output=True, text=True)
    if t.returncode:
        raise SystemExit("nginx rejected the generated block:\n" + t.stderr)
    proc = subprocess.Popen(["nginx", "-p", str(work), "-c", str(conf), "-g", "daemon off;"],
                            stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
    for _ in range(50):
        try:
            fetch(f"http://127.0.0.1:{port}{BASE}/")
            break
        except OSError:
            time.sleep(0.1)
    return proc, port


def header_test(port: int) -> tuple[int, str]:
    r = subprocess.run([sys.executable, str(ROOT / "scripts/tests/test_security_headers.py"), "--base",
                        f"http://127.0.0.1:{port}{BASE}"], capture_output=True, text=True, cwd=ROOT)
    return r.returncode, (r.stdout + r.stderr).strip()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--site", default="")
    args = ap.parse_args()
    if not shutil.which("nginx") or MIME is None:
        print("DIGITALOCEAN HOSTING: FAIL — nginx (and its mime.types) is not installed")
        return 1
    problems: list[str] = []
    with tempfile.TemporaryDirectory(prefix="yfie-do-") as tmp:
        tmp = Path(tmp)
        site = Path(args.site) if args.site else tmp / "site"
        if not args.site:
            subprocess.run([sys.executable, str(ROOT / "scripts/build.py"), "--origin", ORIGIN, "--out", str(site)],
                           check=True, capture_output=True, cwd=ROOT)
        htext = (site / "_headers").read_text(encoding="utf-8")
        rules = parse_headers(htext)
        block = hosting_nginx.server_block(htext, BASE, local_http=True)

        proc, port = start_nginx(tmp / "run", site, block)
        try:
            rc, out = header_test(port)
            print(out.splitlines()[-1] if out else "(no output)")
            if rc:
                problems.append("the header test fails through nginx:\n" + out[-1500:])
            b = f"http://127.0.0.1:{port}"
            st, h = fetch(b + BASE + "/en/payments")
            if st != 301 or h.get("location") != BASE + "/en/payments/":
                problems.append(f"{BASE}/en/payments answers {st} {h.get('location')!r}, not 301 to a relative {BASE}/en/payments/")
            for path in (BASE + "/", BASE + "/en/payments/", BASE + "/ar/", BASE + "/404.html", BASE + "/assets/app.js",
                         BASE + "/assets/yfie.css", BASE + "/assets/fonts/ibm-plex-sans/IBMPlexSans-Regular.woff2",
                         BASE + "/assets/logo/CauseWay_logo_32.png", BASE + "/static-data/search_index.json",
                         BASE + "/robots.txt", BASE + "/sitemap.xml"):
                st, h = fetch(b + path)
                want = headers_for(rules, path).get("Cache-Control")
                if st != 200 or h.get("cache-control") != want:
                    problems.append(f"{path}: HTTP {st}, Cache-Control {h.get('cache-control')!r}, expected {want!r}")
                if "server" in h and "/" in h["server"]:
                    problems.append(f"{path}: the server header names a version: {h['server']}")
            st, h = fetch(b + BASE + "/sitemap.xml")
            if not h.get("content-type", "").startswith("application/xml"):
                problems.append(f"sitemap.xml is served as {h.get('content-type')!r}")
            st, _ = fetch(b + "/elsewhere/")
            if st != 404:
                problems.append(f"an address outside the base path answers {st}, not 404")
        finally:
            proc.terminate(); proc.wait(timeout=10)

        # (c) negative control: one security header removed from the site-wide rule
        broken = "\n".join(l for l in block.splitlines() if "X-Frame-Options" not in l) + "\n"
        proc, port = start_nginx(tmp / "run", site, broken)
        try:
            rc, out = header_test(port)
            if rc == 0 or "X-Frame-Options" not in out:
                problems.append("negative control: the header test passed with X-Frame-Options removed")
            else:
                print("negative control: X-Frame-Options removed — caught")
        finally:
            proc.terminate(); proc.wait(timeout=10)
    for p in problems:
        print("FAIL", p)
    print(f"DIGITALOCEAN HOSTING: {'PASS' if not problems else 'FAIL'} — the nginx block of _headers, served under {BASE}/; "
          f"{len(problems)} problems")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
