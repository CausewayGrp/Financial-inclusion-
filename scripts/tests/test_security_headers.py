#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Every page loads under the host headers with no policy violation (Part B B14 b, REL-01).

  python3 scripts/tests/test_security_headers.py            # every page in both languages, the root and the 404
  python3 scripts/tests/test_security_headers.py --limit 20 # a quick sample

Serves `dist/` locally with the headers `dist/_headers` declares (the file Cloudflare Pages and Netlify read), then
loads every page in headless Chromium and fails on any Content-Security-Policy violation, any blocked or failed
same-origin request, any script error, and any path the header file covers twice with the same header (both hosts
would join the two values). It also checks that every page receives each security header.

One directive is not applied locally: `upgrade-insecure-requests` would send this plain-HTTP test server's own
requests to HTTPS. It changes no permission and reports no violation, so the policy that is tested is otherwise exact.
This is a local check of the header file; it is not a test of any live host.
"""
from __future__ import annotations

import argparse
import fnmatch
import http.server
import socketserver
import sys
import threading
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DIST = ROOT / "dist"
SECURITY = ("Content-Security-Policy", "X-Content-Type-Options", "Referrer-Policy", "Permissions-Policy",
            "Cross-Origin-Opener-Policy", "X-Frame-Options")


def parse_headers(text: str) -> list[tuple[str, list[tuple[str, str]]]]:
    """The `_headers` format: an unindented path pattern, then indented `Name: value` lines; `#` starts a comment."""
    rules: list[tuple[str, list[tuple[str, str]]]] = []
    for line in text.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if not line[0].isspace():
            rules.append((line.strip(), []))
        else:
            name, _, value = line.strip().partition(":")
            if not rules or not value:
                raise ValueError(f"_headers: a header line outside a path block or without a value: {line!r}")
            rules[-1][1].append((name.strip(), value.strip()))
    return rules


def matches(pattern: str, path: str) -> bool:
    return path == pattern if "*" not in pattern else fnmatch.fnmatchcase(path, pattern)


def headers_for(rules, path: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for pattern, hs in rules:
        if matches(pattern, path):
            for name, value in hs:
                if name in out:
                    raise ValueError(f"_headers: {path} receives {name} from two rules (a host would join them)")
                out[name] = value
    return out


def serve(rules):
    class H(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *a, **k):
            super().__init__(*a, directory=str(DIST), **k)

        def end_headers(self):
            path = self.path.split("?", 1)[0].split("#", 1)[0]
            for name, value in headers_for(rules, path).items():
                if name == "Content-Security-Policy":
                    value = "; ".join(d for d in (x.strip() for x in value.split(";")) if d and d != "upgrade-insecure-requests")
                self.send_header(name, value)
            super().end_headers()

        def log_message(self, *a):
            pass

    srv = socketserver.ThreadingTCPServer(("127.0.0.1", 0), H)
    srv.daemon_threads = True
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()
    hf = DIST / "_headers"
    if not hf.exists():
        print("SECURITY HEADERS: FAIL (dist/_headers missing; run python3 scripts/build.py)")
        return 1
    rules = parse_headers(hf.read_text(encoding="utf-8"))
    pages = ["/", "/404.html"] + sorted("/" + str(p.parent.relative_to(DIST)).replace("\\", "/") + "/"
                                        for p in DIST.glob("*/**/index.html") if p.parent != DIST)
    pages += [p for p in ("/en/", "/ar/") if p not in pages]
    if args.limit:
        pages = pages[:args.limit]
    problems: list[str] = []
    for p in pages + ["/assets/app.js", "/assets/fonts/ibm-plex-sans/IBMPlexSans-Regular.woff2", "/static-data/search_index.json"]:
        try:
            got = headers_for(rules, p)
        except ValueError as ex:
            problems.append(str(ex))
            continue
        if p.endswith("/") or p.endswith(".html"):
            problems += [f"{p}: no {h}" for h in SECURITY if h not in got]
        if "Cache-Control" not in got:
            problems.append(f"{p}: no Cache-Control rule")
    srv = serve(rules)
    base = f"http://127.0.0.1:{srv.server_address[1]}"
    from playwright.sync_api import sync_playwright
    try:
        with sync_playwright() as pw:
            browser = pw.chromium.launch()
            ctx = browser.new_context()
            ctx.add_init_script("window.__csp=[];document.addEventListener('securitypolicyviolation',e=>window.__csp.push(e.violatedDirective+' '+e.blockedURI));")
            page = ctx.new_page()
            errors: list[str] = []
            page.on("pageerror", lambda e: errors.append(f"script error: {e}"))
            page.on("console", lambda m: errors.append(f"console: {m.text}") if m.type == "error" and "Content Security Policy" in m.text else None)
            # a request the browser abandons when the next page starts loading (net::ERR_ABORTED, e.g. a font preload still
            # in flight) is not a failure of either page; a request the policy blocks reports net::ERR_BLOCKED_BY_CSP and
            # still counts (CI run 37092238972 failed on such aborts, attributed to the page that followed)
            page.on("requestfailed", lambda r: errors.append(f"request failed: {r.url} {r.failure}")
                    if r.url.startswith(base) and "ERR_ABORTED" not in str(r.failure) else None)
            for p in pages:
                errors.clear()
                resp = page.goto(base + p, wait_until="load")
                csp = page.evaluate("window.__csp")
                if resp is None or (resp.status != 200 and p != "/404.html"):
                    problems.append(f"{p}: HTTP {resp.status if resp else 'none'}")
                if resp is not None and "content-security-policy" not in {k.lower() for k in resp.headers}:
                    problems.append(f"{p}: the response carries no policy")
                problems += [f"{p}: CSP violation {v}" for v in csp] + [f"{p}: {e}" for e in errors]
            browser.close()
    finally:
        srv.shutdown()
    for x in problems[:40]:
        print("FAIL", x)
    print(f"SECURITY HEADERS: {'PASS' if not problems else 'FAIL'} — {len(pages)} pages loaded under dist/_headers; "
          f"{len(problems)} problems")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
