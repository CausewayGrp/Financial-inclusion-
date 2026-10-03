#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The corporate forwarding middleware of docs/RELEASE_RUNBOOK.md ("Route 1") does what the runbook says, as written
(R-09, independent review of 70398d1: the earlier test of it in a real Nitro server was not in the repository).

  python3 scripts/tests/test_corporate_proxy.py

Builds the published site for the decided origin into a temporary directory, serves it from a real nginx with our own
server block (scripts/hosting_nginx.py, as in test_digitalocean_hosting.py) as the stand-in for the App Platform app,
and puts in front of it the harness in scripts/hosting/corporate_proxy_harness/: a Nitro 2.13.4 server (pinned by its
package-lock.json) whose own middleware sets the corporate `session` cookie, `x-robots-tag` and `x-powered-by` on every
response before routing, as causewaygrp.com was observed to do. The forwarding middleware is the TypeScript block
printed in the runbook, extracted from it at run time; only its UPSTREAM constant is replaced by the local nginx. Then,
with the reader's browser sending the corporate cookie:

(a) the bare path answers one 301 to the path with its slash, without the corporate headers, and that address
    answers 200 (no loop);
(b) every page, asset and data file under the path, and a missing page (404), arrives with our security headers and
    without Set-Cookie, X-Robots-Tag or X-Powered-By, with the body nginx served;
(c) our directory redirect passes through with its relative Location;
(d) /financial-inclusion-evidencex is not forwarded (the corporate site answers it);
(e) no request reaches the upstream with the corporate cookie (nginx's own access log);
(f) scripts/tests/test_security_headers.py --base <the corporate stand-in>/financial-inclusion-evidence passes: every
    page in a browser, no cookie held afterwards.
(g) Negative control: the same middleware without its header removal must fail (b).

What it does not prove: a header added by a server in front of Nitro (an nginx, a load balancer or a CDN on the
corporate side) is outside the middleware's reach, and so outside this test. Where the corporate headers originate is
the web administrator's check in docs/RELEASE_RUNBOOK.md, step 8; the live `test_security_headers.py --base` run on
causewaygrp.com is the release condition either way. Needs Node.js 20+, npm with registry access, and nginx; not run in
CI (it installs packages from the npm registry).
"""
from __future__ import annotations

import os
import re
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
HARNESS = ROOT / "scripts/hosting/corporate_proxy_harness"
RUNBOOK = ROOT / "docs/RELEASE_RUNBOOK.md"
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "scripts" / "tests"))
import hosting_nginx  # noqa: E402
from test_digitalocean_hosting import MIME  # noqa: E402

COOKIE = "session=reader-browser-cookie"
FORBIDDEN = ("set-cookie", "x-robots-tag", "x-powered-by")
OURS = ("content-security-policy", "x-frame-options", "x-content-type-options", "referrer-policy", "permissions-policy",
        "cross-origin-opener-policy")


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None


def fetch(url: str, cookie: str = COOKIE) -> tuple[int, dict[str, str], bytes]:
    req = urllib.request.Request(url, headers={"Cookie": cookie} if cookie else {})
    try:
        with urllib.request.build_opener(_NoRedirect).open(req, timeout=15) as r:
            return r.status, {k.lower(): v for k, v in r.headers.items()}, r.read()
    except urllib.error.HTTPError as e:
        return e.code, {k.lower(): v for k, v in e.headers.items()}, e.read()


def free_port() -> int:
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def wait(url: str) -> None:
    for _ in range(100):
        try:
            urllib.request.urlopen(url, timeout=2)
            return
        except urllib.error.HTTPError:
            return
        except Exception:
            time.sleep(0.2)
    raise SystemExit(f"nothing answers at {url}")


def runbook_middleware() -> str:
    text = RUNBOOK.read_text(encoding="utf-8")
    blocks = [b for b in re.findall(r"```ts\n(.*?)```", text, re.S) if "proxyRequest" in b]
    if len(blocks) != 1:
        raise SystemExit(f"the runbook holds {len(blocks)} forwarding middleware blocks, expected 1")
    return "\n".join(line[2:] if line.startswith("  ") else line for line in blocks[0].splitlines()) + "\n"


def start_nginx(work: Path, site: Path, block: str) -> tuple[subprocess.Popen, int]:
    port = free_port()
    www = work / "www"
    shutil.copytree(site, www / BASE.strip("/"), ignore=shutil.ignore_patterns("_headers"))
    (work / "logs").mkdir()
    who = "user root;\n" if os.geteuid() == 0 else ""
    conf = work / "nginx.conf"
    conf.write_text(f"""{who}worker_processes 1;
pid {work}/nginx.pid;
error_log {work}/logs/error.log warn;
events {{ worker_connections 256; }}
http {{
    include {MIME};
    default_type application/octet-stream;
    log_format upstream_cookie '$request_uri|$http_cookie';
    access_log {work}/logs/access.log upstream_cookie;
    client_body_temp_path {work}/tmp_body; proxy_temp_path {work}/tmp_proxy; fastcgi_temp_path {work}/tmp_fcgi;
    uwsgi_temp_path {work}/tmp_uwsgi; scgi_temp_path {work}/tmp_scgi;
{block.replace("listen 8080;", f"listen 127.0.0.1:{port};").replace("root /usr/share/nginx/html;", f"root {www};")}
}}
""", encoding="utf-8")
    t = subprocess.run(["nginx", "-t", "-p", str(work), "-c", str(conf)], capture_output=True, text=True)
    if t.returncode:
        raise SystemExit("nginx rejected the generated block:\n" + t.stderr)
    proc = subprocess.Popen(["nginx", "-p", str(work), "-c", str(conf), "-g", "daemon off;"],
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    wait(f"http://127.0.0.1:{port}{BASE}/")
    return proc, port


def build_harness(work: Path, middleware: str) -> Path:
    h = work / "harness"
    shutil.copytree(HARNESS, h, ignore=shutil.ignore_patterns("node_modules", ".output", ".nitro"))
    (h / "server/middleware/0.financial-inclusion-evidence.ts").write_text(middleware, encoding="utf-8")
    for cmd in (["npm", "ci", "--no-audit", "--no-fund", "--loglevel=error"], ["npx", "--no-install", "nitropack", "build"]):
        r = subprocess.run(cmd, cwd=h, capture_output=True, text=True)
        if r.returncode:
            raise SystemExit(f"{' '.join(cmd)} failed:\n{(r.stdout + r.stderr)[-2000:]}")
    return h


def start_nitro(h: Path) -> tuple[subprocess.Popen, int]:
    port = free_port()
    proc = subprocess.Popen(["node", str(h / ".output/server/index.mjs")], cwd=h,
                            env={**os.environ, "PORT": str(port), "HOST": "127.0.0.1", "NITRO_PORT": str(port), "NITRO_HOST": "127.0.0.1"},
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    wait(f"http://127.0.0.1:{port}/")
    return proc, port


def check(front: str, direct: str, log: Path | None) -> list[str]:
    problems = []
    st, h, _ = fetch(front + BASE)
    if st != 301 or h.get("location") != BASE + "/":
        problems.append(f"(a) the bare path answers {st} {h.get('location')!r}, not one 301 to {BASE}/")
    if [k for k in FORBIDDEN if k in h]:
        problems.append(f"(a) the bare path's redirect carries {[k for k in FORBIDDEN if k in h]}")
    st2, _, _ = fetch(front + BASE + "/")
    if st2 != 200:
        problems.append(f"(a) {BASE}/ answers {st2}")
    paths = [("/", 200), ("/ar/", 200), ("/en/", 200), ("/en/payments/", 200), ("/ar/evidence/CLM-001/", 200),
             ("/assets/app.js", 200), ("/assets/yfie.css", 200), ("/static-data/search_index.json", 200),
             ("/sitemap.xml", 200), ("/en/no-such-page/", 404)]
    for p, want in paths:
        st, h, body = fetch(front + BASE + p)
        _, hd, bd = fetch(direct + BASE + p, cookie="")
        if st != want:
            problems.append(f"(b) {p} answers {st}, expected {want}")
        bad = [k for k in FORBIDDEN if k in h]
        if bad:
            problems.append(f"(b) {p} carries {bad}")
        missing = [k for k in OURS if h.get(k) != hd.get(k)]
        if missing:
            problems.append(f"(b) {p} does not carry our {missing}")
        if body != bd:
            problems.append(f"(b) {p} body differs from what nginx served")
    st, h, _ = fetch(front + BASE + "/en/payments")
    if st != 301 or h.get("location") != BASE + "/en/payments/":
        problems.append(f"(c) {BASE}/en/payments answers {st} {h.get('location')!r}, not 301 to a relative {BASE}/en/payments/")
    st, h, body = fetch(front + BASE + "x")
    if st != 404 or b"corporate site" not in body:
        problems.append(f"(d) {BASE}x was forwarded (HTTP {st})")
    if log is not None:
        lines = log.read_text(encoding="utf-8").splitlines() if log.exists() else []
        leaked = [l for l in lines if "session=" in l]
        if not lines or leaked:
            problems.append(f"(e) the upstream saw {len(lines)} requests, {len(leaked)} with the corporate cookie")
    return problems


def main() -> int:
    for tool in ("node", "npm", "npx", "nginx"):
        if not shutil.which(tool):
            print(f"CORPORATE PROXY: FAIL — {tool} is not installed")
            return 1
    problems: list[str] = []
    mw = runbook_middleware()
    if "const UPSTREAM = 'https://<app>.ondigitalocean.app'" not in mw:
        raise SystemExit("the runbook's middleware no longer declares UPSTREAM as expected")
    with tempfile.TemporaryDirectory(prefix="yfie-proxy-") as tmp:
        tmp = Path(tmp)
        site = tmp / "site"
        subprocess.run([sys.executable, str(ROOT / "scripts/build.py"), "--origin", ORIGIN, "--out", str(site)],
                       check=True, capture_output=True, cwd=ROOT)
        block = hosting_nginx.server_block((site / "_headers").read_text(encoding="utf-8"), BASE, local_http=True)
        ngx, nport = start_nginx(tmp / "nginx", site, block)
        direct = f"http://127.0.0.1:{nport}"
        try:
            h = build_harness(tmp / "ok", mw.replace("'https://<app>.ondigitalocean.app'", f"'{direct}'"))
            nitro, port = start_nitro(h)
            front = f"http://127.0.0.1:{port}"
            try:
                (tmp / "nginx/logs/access.log").write_text("", encoding="utf-8")
                problems += check(front, direct, tmp / "nginx/logs/access.log")
                r = subprocess.run([sys.executable, str(ROOT / "scripts/tests/test_security_headers.py"), "--base", front + BASE],
                                   capture_output=True, text=True, cwd=ROOT)
                out = (r.stdout + r.stderr).strip()
                print(out.splitlines()[-1] if out else "(no output)")
                if r.returncode:
                    problems.append("(f) the header test fails through the corporate stand-in:\n" + out[-1500:])
            finally:
                nitro.terminate(); nitro.wait(timeout=10)
            # (g) negative control: the runbook's middleware without its header removal
            broken = mw.replace("onResponse(ev) { for (const h of STRIP) ev.node.res.removeHeader(h) },", "")
            if broken == mw:
                raise SystemExit("negative control: the removal line was not found in the runbook's middleware")
            hb = build_harness(tmp / "broken", broken.replace("'https://<app>.ondigitalocean.app'", f"'{direct}'"))
            nitro, port = start_nitro(hb)
            try:
                caught = [p for p in check(f"http://127.0.0.1:{port}", direct, None) if p.startswith("(b)") and "carries" in p]
                if caught:
                    print("negative control: the middleware without header removal — caught")
                else:
                    problems.append("negative control: (b) passed without the header removal")
            finally:
                nitro.terminate(); nitro.wait(timeout=10)
        finally:
            ngx.terminate(); ngx.wait(timeout=10)
    for p in problems:
        print("FAIL", p)
    print(f"CORPORATE PROXY: {'PASS' if not problems else 'FAIL'} — the runbook's forwarding middleware in Nitro 2.13.4, in front of "
          f"our nginx block, under {BASE}/; {len(problems)} problems")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
