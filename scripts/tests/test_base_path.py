#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The site works under the decided address, and nothing escapes its path (owner decision B2, 3 October 2026).

  python3 scripts/tests/test_base_path.py                # build, sweep, browser, metadata, negative control
  python3 scripts/tests/test_base_path.py --no-browser   # the static parts only (sweep, metadata, negative control)
  python3 scripts/tests/test_base_path.py --site DIR     # check a site already built with the same origin

Builds the site with public_origin https://causewaygrp.com/financial-inclusion-evidence into a temporary directory
(`scripts/build.py --origin … --out …`; site-src/deployment.json and dist/ are not touched) and serves it from a local
HTTP server so that it lives under /financial-inclusion-evidence/, with the host headers of its own `_headers` file
applied by full request path, and a missing page answered by its 404 page with status 404, as Cloudflare Pages does.
Anything requested outside the path gets a bare 404. Then:

(a) Sweep. Every HTML, CSS, JS and JSON file, `_headers`, robots.txt and sitemap.xml: every internal address (an
    attribute, a srcset candidate, a refresh, a CSS url(), a structured-data or JSON value, a runtime string literal, a
    header path pattern, a robots directive, an address printed in text) starts with the base path, or with the full
    origin and the base path, and resolves to a file of the build. Route keys (the `route` of the search index and of
    the Compare data, joined by the runtime to its language prefix) must resolve in both languages.
(b) Browser (Chromium; /opt/pw-browsers/chromium when it exists, or YFIE_CHROMIUM). At 390 and 1440 px, in Arabic and
    English: the root entry, Home, /payments/, /evidence/CLM-001/, /data/, the three-measure Compare and a deep 404
    path; search (a query typed, a result followed), Compare (a record link followed, the link copied), Copy citation,
    Share (the copy fallback, with Web Share absent), print (window.print stubbed) and the language switch with its
    stored preference. Every network request is recorded; the run fails if a same-origin request leaves the base path
    or returns an error status (the deep 404 document itself excepted), or if any request goes to another origin.
(c) Metadata. canonical, hreflang (en, ar, x-default), og:url, og:image, the sitemap and every JSON-LD address start
    with the full origin and the base path, and name the page itself where they should.

Negative controls, in the same run: one root-absolute link (href="/en/about/") is injected into one page of the
temporary build. The sweep must report it, and in the browser following it must be reported as a request that escaped
the path. And an address built by concatenation ('/'+'en'+'/about/') is appended to the runtime: the sweep must report
it, because every slash-leading literal outside the base must be a listed route key at its listed count. If any stays
silent, the gate is worth nothing and the run fails.

Exit 0 = pass; 1 = a fault (or the negative control was not caught); 2 = the browser harness is unavailable.
"""
from __future__ import annotations

import argparse
import html.parser
import http.server
import importlib.util
import json
import mimetypes
import os
import re
import shutil
import socketserver
import subprocess
import sys
import tempfile
import threading
from collections import Counter
from pathlib import Path
from urllib.parse import urljoin, urlsplit

ROOT = Path(__file__).resolve().parents[2]
ORIGIN = "https://causewaygrp.com/financial-inclusion-evidence"
LANGS = ("ar", "en")
NEGATIVE_PAGE = "en/payments/index.html"
NEGATIVE_LINK = '<p><a id="yfie-negative-control" href="/en/about/">about</a></p>'
# The second control: an address the runtime would build by concatenation, which only the counted literal rule sees.
NEGATIVE_JS = ("assets/app.js", ";void function(){if(0)location.href='/'+'en'+'/about/'}();")

# HTML attributes whose value is one address
URL_ATTRS = {"href", "src", "action", "formaction", "poster", "cite", "data", "background", "manifest", "ping", "xlink:href"}
SOCIAL_URL = {"og:url", "og:image", "og:image:url", "og:image:secure_url", "twitter:image"}
CSS_URL = re.compile(r"""url\(\s*(['"]?)([^'")\s]+)\1\s*\)""")
JS_LITERAL = re.compile(r"""(['"`])(/[^'"`\s]*)""")


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


HEADERS = _load("yfie_security_headers", ROOT / "scripts" / "tests" / "test_security_headers.py")   # one _headers reader
BASE_PATH = _load("yfie_base_path", ROOT / "scripts" / "base_path.py")   # the runtime's listed route keys


class Site:
    """The temporary build and the address rules it must keep."""

    def __init__(self, root: Path, origin: str):
        self.root, self.origin = root, origin
        parts = urlsplit(origin)
        self.host = f"{parts.scheme}://{parts.netloc}"
        self.base = parts.path                      # "/financial-inclusion-evidence"
        self.top = {p.name for p in root.iterdir()}  # the build's top-level entries: en, ar, assets, static-data, …

    def file_for(self, path: str) -> Path | None:
        """The file a URL path under the base serves, or None."""
        path = path.split("#", 1)[0].split("?", 1)[0]
        if not (path == self.base + "/" or path.startswith(self.base + "/")):
            return None
        rel = path[len(self.base) + 1:]
        f = self.root / rel
        if rel == "" or rel.endswith("/"):
            f = f / "index.html"
        elif f.is_dir():
            f = f / "index.html"
        return f if f.is_file() else None

    def names_top(self, path: str) -> bool:
        seg = path.lstrip("/").split("/", 1)[0].split("?", 1)[0].split("#", 1)[0]
        return seg in self.top


class Sweep:
    def __init__(self, site: Site):
        self.site, self.problems, self.checked, self.files = site, [], 0, 0

    def fail(self, where: str, why: str):
        self.problems.append(f"{where}: {why}")

    def url(self, where: str, value: str, page_url: str | None = None, must_be_absolute: bool = False):
        """One address: an own-origin or root-absolute address must sit under the base path and resolve."""
        s, v = self.site, value.strip()
        if not v or v.startswith(("#", "mailto:", "tel:", "data:")):
            return
        if v.startswith("//"):
            self.fail(where, f"protocol-relative address {v!r}")
            return
        if v.startswith(("http://", "https://")):
            if urlsplit(v).netloc != urlsplit(s.host).netloc:
                return                                          # another site: an original source
            self.checked += 1
            if not v.startswith(s.origin + "/"):
                self.fail(where, f"own-domain address outside the base path {v!r}")
            elif v.startswith("http://"):
                self.fail(where, f"own-domain address over http {v!r}")
            elif s.file_for(urlsplit(v).path) is None:
                self.fail(where, f"address resolves to no file {v!r}")
            return
        if re.match(r"^[a-z][a-z0-9+.-]*:", v, re.I):
            self.fail(where, f"unexpected scheme {v!r}")
            return
        self.checked += 1
        if must_be_absolute:
            self.fail(where, f"not absolute: {v!r}")
        if v.startswith("/"):
            path = v
        elif page_url:
            path = urlsplit(urljoin(s.host + page_url, v)).path
        else:
            self.fail(where, f"relative address with no page to resolve it against {v!r}")
            return
        if not (path == s.base + "/" or path.startswith(s.base + "/")):
            self.fail(where, f"escapes the base path {v!r}")
        elif s.file_for(path) is None:
            self.fail(where, f"resolves to no file {v!r}")

    def text(self, where: str, text: str):
        """An address printed in text: an own-origin URL must resolve; a root-absolute path naming the build escapes."""
        for m in re.finditer(r"https?://[^\s<>\"'«»()]+", text):
            u = m.group(0).rstrip(".,;:")
            if urlsplit(u).netloc == urlsplit(self.site.host).netloc:
                self.url(where, u)
        for m in re.finditer(r"(?<![\w/.:%-])(/[A-Za-z0-9._-]+)(?:/[^\s<>\"'«»()]*)?", text):
            if self.site.names_top(m.group(1)):
                self.fail(where, f"root-absolute address in text {m.group(0)!r}")

    def json_value(self, where: str, data, lang: str | None, key: str | None = None):
        if isinstance(data, dict):
            for k, v in data.items():
                self.json_value(where, v, lang, k)
        elif isinstance(data, list):
            for v in data:
                self.json_value(where, v, lang, key)
        elif isinstance(data, str):
            if data.startswith(("http://", "https://")):
                self.url(where, data)
            elif data.startswith("/") and key == "route":
                self.route(where, data)
            elif data.startswith("/") and self.site.names_top(data):
                self.url(where, data)               # an address in data: under the base path, or it escapes

    def route(self, where: str, route: str):
        """A route key: the runtime writes `<base>/<lang>` + route (scripts/base_path.py, JS_PATCHES)."""
        self.checked += 1
        if re.match(r"^/(?:en|ar)(?:/|$)", route) or route.startswith(self.site.base + "/"):
            self.fail(where, f"route key carries a prefix the runtime adds itself {route!r}")
            return
        for lang in LANGS:
            if self.site.file_for(f"{self.site.base}/{lang}{route}") is None:
                self.fail(where, f"route key resolves to no page in {lang}: {route!r}")

    def css(self, where: str, text: str, page_url: str):
        for m in CSS_URL.finditer(text):
            self.url(where, m.group(2), page_url)

    def html(self, rel: str, text: str):
        sweep, site = self, self.site
        page_url = site.base + "/" + (rel[:-len("index.html")] if rel.endswith("index.html") else rel)
        lang = rel.split("/", 1)[0] if rel.split("/", 1)[0] in LANGS else None

        class P(html.parser.HTMLParser):
            def __init__(self):
                super().__init__(convert_charrefs=True)
                self.stack: list[tuple[str, dict]] = []

            def handle_starttag(self, tag, attrs):
                a = dict(attrs)
                for name, value in attrs:
                    if value is None:
                        continue
                    w = f"{rel} <{tag} {name}>"
                    if name in URL_ATTRS:
                        sweep.url(w, value, page_url)
                    elif name in ("srcset", "imagesrcset"):
                        for cand in value.split(","):
                            if cand.strip():
                                sweep.url(w, cand.strip().split()[0], page_url)
                    elif name == "style":
                        sweep.css(w, value, page_url)
                    elif tag == "meta" and name == "content":
                        kind = (a.get("property") or a.get("name") or "").lower()
                        if (a.get("http-equiv") or "").lower() == "refresh":
                            m = re.search(r"url=(.+)$", value, re.I)
                            if m:
                                sweep.url(w, m.group(1), page_url)
                        elif kind in SOCIAL_URL:
                            sweep.url(w, value, page_url, must_be_absolute=True)
                        else:
                            sweep.text(w, value)
                    elif value.startswith("/") and not value.startswith("//") or value.startswith(site.host):
                        sweep.url(w, value, page_url)       # any other attribute that holds an address
                    else:
                        sweep.text(w, value)
                if tag not in ("meta", "link", "img", "br", "hr", "input", "source", "wbr", "area", "base", "col", "embed", "param", "track"):
                    self.stack.append((tag, a))

            def handle_endtag(self, tag):
                while self.stack:
                    t, _ = self.stack.pop()
                    if t == tag:
                        break

            def handle_data(self, data):
                tag, a = self.stack[-1] if self.stack else ("", {})
                if tag == "script":
                    kind = a.get("type", "")
                    if kind in ("application/ld+json", "application/json"):
                        try:
                            obj = json.loads(data)
                        except ValueError:
                            sweep.fail(rel, f"unparseable {kind} block {a.get('id', '')}")
                            return
                        sweep.json_value(f"{rel} <script {a.get('id') or kind}>", obj, lang)
                    elif data.strip():
                        sweep.fail(rel, "inline executable script")
                elif tag == "style":
                    sweep.css(f"{rel} <style>", data, page_url)
                else:
                    sweep.text(f"{rel} text", data)

        P().feed(text)

    def run(self):
        s = self.site
        for f in sorted(p for p in s.root.rglob("*") if p.is_file()):
            rel = f.relative_to(s.root).as_posix()
            if f.suffix in (".png", ".woff2", ".txt") and rel != "robots.txt":
                continue
            self.files += 1
            text = f.read_text(encoding="utf-8")
            if f.suffix == ".html":
                self.html(rel, text)
            elif f.suffix == ".css":
                self.css(rel, text, s.base + "/" + rel)
            elif f.suffix == ".js":
                # Every slash-leading literal outside the base is a listed route key, at its listed count
                # (scripts/base_path.py JS_ROUTE_KEYS), so an address built by concatenation or a template is reported
                # here too: '/'+lang+'/about/' adds a sixth '/' and an unlisted '/about/'.
                outside = Counter()
                for m in JS_LITERAL.finditer(text):
                    lit = m.group(2)
                    if lit.startswith(s.base + "/"):
                        self.url(f"{rel} literal", lit)
                    else:
                        self.checked += 1
                        outside[m.group(1) + lit + m.group(1)] += 1
                for lit in sorted((outside - Counter(BASE_PATH.JS_ROUTE_KEYS.get(rel, {}))).elements()):
                    self.fail(f"{rel} literal", f"slash-leading literal outside the base path, not a listed route key {lit!r}")
            elif f.suffix == ".json":
                try:
                    self.json_value(rel, json.loads(text), None)
                except ValueError:
                    self.fail(rel, "unparseable JSON")
            elif rel == "_headers":
                for line in text.splitlines():
                    if line and not line[0].isspace() and not line.startswith("#"):
                        self.checked += 1
                        if not line.startswith(s.base + "/"):
                            self.fail("_headers", f"path pattern outside the base path {line!r}")
            elif rel == "robots.txt":
                for line in text.splitlines():
                    k, _, v = line.partition(":")
                    v = v.strip()
                    if k.strip().lower() in ("allow", "disallow") and v:
                        self.checked += 1
                        if not v.startswith(s.base + "/"):
                            self.fail("robots.txt", f"{k} outside the base path {v!r}")
                    elif k.strip().lower() == "sitemap":
                        self.url("robots.txt Sitemap", v, must_be_absolute=True)
            elif rel == "sitemap.xml":
                for u in re.findall(r'<loc>([^<]+)</loc>|href="([^"]+)"', text):
                    self.url("sitemap.xml", u[0] or u[1], must_be_absolute=True)
            else:
                self.fail(rel, "a file type the sweep does not know; add it to scripts/tests/test_base_path.py")
        return self


def metadata(site: Site) -> list[str]:
    """(c) Every discovery address is absolute, under the base path, and names the page itself where it should."""
    problems = []
    o = site.origin
    specs = json.loads((ROOT / "site-src/content/page_specs.json").read_text(encoding="utf-8"))["page_specs"]
    pages = 0
    for spec in specs:
        route = "/" + str(spec.get("route") or "/").strip("/") + "/"
        route = "/" if route == "//" else route
        for lang in LANGS:
            rel = f"{lang}{route}index.html"
            f = site.root / rel
            if not f.exists():
                problems.append(f"{rel}: missing")
                continue
            pages += 1
            t = f.read_text(encoding="utf-8")
            head = t[:t.find("</head>")]
            canon = re.findall(r'<link rel="canonical" href="([^"]+)">', head)
            if canon != [f"{o}/{lang}{route}"]:
                problems.append(f"{rel}: canonical {canon}")
            alts = dict(re.findall(r'<link rel="alternate" hreflang="([^"]+)" href="([^"]+)">', head))
            if alts != {"en": f"{o}/en{route}", "ar": f"{o}/ar{route}", "x-default": f"{o}/"}:
                problems.append(f"{rel}: hreflang {alts}")
            og = dict(re.findall(r'<meta property="(og:url|og:image)" content="([^"]+)">', head))
            if og.get("og:url") != f"{o}/{lang}{route}":
                problems.append(f"{rel}: og:url {og.get('og:url')!r}")
            if not og.get("og:image", "").startswith(o + "/assets/social/") or site.file_for(urlsplit(og["og:image"]).path) is None:
                problems.append(f"{rel}: og:image {og.get('og:image')!r}")
            for blob in re.findall(r'<script type="application/ld\+json">(.*?)</script>', head):
                def walk(x, k=None):
                    if isinstance(x, dict):
                        for kk, v in x.items():
                            walk(v, kk)
                    elif isinstance(x, list):
                        for v in x:
                            walk(v, k)
                    elif k in ("url", "item", "mainEntityOfPage", "@id") and isinstance(x, str):
                        if not x.startswith(o + "/") or site.file_for(urlsplit(x).path) is None:
                            problems.append(f"{rel}: JSON-LD {k} {x!r}")
                walk(json.loads(blob))
    root = (site.root / "index.html").read_text(encoding="utf-8")
    if f'hreflang="x-default" href="{o}/"' not in root:
        problems.append("index.html: x-default is not the full origin and base path")
    sm = (site.root / "sitemap.xml").read_text(encoding="utf-8")
    locs = re.findall(r"<loc>([^<]+)</loc>", sm)
    if len(locs) != pages or len(set(locs)) != len(locs) or not all(x.startswith(o + "/") for x in locs):
        problems.append(f"sitemap.xml: {len(locs)} locations for {pages} pages, or one outside {o}/")
    if (site.root / "robots.txt").read_text(encoding="utf-8").count(f"Sitemap: {o}/sitemap.xml") != 1:
        problems.append("robots.txt does not name the sitemap at the full origin and base path")
    return problems


# ------------------------------------------------------------------------------------------------ the host
def serve(site: Site):
    rules = HEADERS.parse_headers((site.root / "_headers").read_text(encoding="utf-8"))
    not_found = site.root / "404.html"

    class H(http.server.BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def _send(self, status, body=b"", ctype="text/plain; charset=utf-8", path="", extra=None):
            self.send_response(status)
            self.send_header("Content-Type", ctype)
            self.send_header("Content-Length", str(len(body)))
            for k, v in (extra or {}).items():
                self.send_header(k, v)
            for name, value in HEADERS.headers_for(rules, path).items() if path else ():
                if name == "Content-Security-Policy":   # this local server is plain http (test_security_headers.py)
                    value = "; ".join(d for d in (x.strip() for x in value.split(";")) if d and d != "upgrade-insecure-requests")
                self.send_header(name, value)
            self.end_headers()
            if self.command != "HEAD":
                self.wfile.write(body)

        def do_GET(self):
            path = urlsplit(self.path).path
            if path == site.base:
                return self._send(301, extra={"Location": site.base + "/"})
            if not path.startswith(site.base + "/"):
                return self._send(404, b"outside the base path")      # what the corporate site would answer
            f = site.file_for(path)
            if f is None and (site.root / path[len(site.base) + 1:]).is_dir() and not path.endswith("/"):
                return self._send(301, extra={"Location": path + "/"})
            if f is None:
                return self._send(404, not_found.read_bytes(), "text/html; charset=utf-8", path)
            ctype = {".html": "text/html; charset=utf-8", ".js": "text/javascript; charset=utf-8", ".css": "text/css; charset=utf-8",
                     ".json": "application/json", ".woff2": "font/woff2", ".png": "image/png", ".txt": "text/plain; charset=utf-8",
                     ".xml": "application/xml"}.get(f.suffix) or mimetypes.guess_type(f.name)[0] or "application/octet-stream"
            return self._send(200, f.read_bytes(), ctype, path)

        do_HEAD = do_GET

    class S(socketserver.ThreadingTCPServer):
        daemon_threads = True

        def handle_error(self, request, client_address):
            if not isinstance(sys.exc_info()[1], (BrokenPipeError, ConnectionResetError)):   # a navigation abandons a request
                super().handle_error(request, client_address)

    srv = S(("127.0.0.1", 0), H)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv


class Net:
    """Every request a browser context makes, judged by the rule: same origin, under the base path, no error status."""

    def __init__(self, server: str, base: str):
        self.server, self.base, self.problems, self.count, self.allowed_404 = server, base, [], 0, set()

    def attach(self, ctx):
        ctx.on("request", self.on_request)
        ctx.on("response", self.on_response)
        ctx.on("requestfailed", self.on_failed)

    def on_request(self, req):
        self.count += 1
        u = urlsplit(req.url)
        if u.scheme in ("data", "blob", "about"):
            return
        if f"{u.scheme}://{u.netloc}" != self.server:
            self.problems.append(f"request to another origin: {req.url}")
        elif not u.path.startswith(self.base + "/"):
            self.problems.append(f"request escaped the base path: {req.url}")

    def on_response(self, resp):
        if resp.url.startswith(self.server) and resp.status >= 400 and resp.url not in self.allowed_404:
            self.problems.append(f"HTTP {resp.status}: {resp.url}")

    def on_failed(self, req):
        if req.url.startswith(self.server) and "ERR_ABORTED" not in str(req.failure):
            self.problems.append(f"request failed: {req.url} {req.failure}")


def browser_checks(site: Site, server: str, chromium: str | None) -> tuple[list[str], int, int]:
    from playwright.sync_api import sync_playwright
    B = server + site.base
    o = site.origin
    problems: list[str] = []
    net = Net(server, site.base)
    loads = 0
    favicon: set[str] = set()

    def check(cond, msg):
        if not cond:
            problems.append(msg)

    def visible(page, sel):
        loc = page.locator(f"{sel} >> visible=true").first
        loc.scroll_into_view_if_needed()
        return loc

    def clipboard(page):
        page.wait_for_function("navigator.clipboard.readText().then(t=>t.length>0)", timeout=5000)
        return page.evaluate("navigator.clipboard.readText()")

    def on_console(m, errors):
        if m.type != "error":
            return
        url = m.location.get("url", "")
        if m.text.startswith("Failed to load resource"):
            if url in net.allowed_404:
                return                  # the deep 404 document answers 404 on purpose
            if urlsplit(url).path == "/favicon.ico":
                # No page declares an icon, so the browser itself asks the domain root (outside the base path) for
                # /favicon.ico. No page makes that request (the network rule above sees none); on the release domain
                # causewaygrp.com answers it. Counted and reported, not failed (docs/RELEASE_RUNBOOK.md, "Hosting").
                favicon.add(url)
                return
        errors.append(f"console: {m.text} {url}")

    with sync_playwright() as pw:
        browser = pw.chromium.launch(**({"executable_path": chromium} if chromium else {}))
        for width in (390, 1440):
            for lang in LANGS:
                other = "en" if lang == "ar" else "ar"
                tag = f"[{lang} {width}px]"
                ctx = browser.new_context(viewport={"width": width, "height": 900})
                ctx.grant_permissions(["clipboard-read", "clipboard-write"], origin=server)
                ctx.add_init_script("window.__printed=0;window.print=()=>{window.__printed++;};"
                                    "Object.defineProperty(navigator,'share',{value:undefined,configurable:true});")
                net.attach(ctx)
                page = ctx.new_page()
                errors: list[str] = []
                page.on("pageerror", lambda e: errors.append(f"script error: {e}"))
                page.on("console", lambda m: on_console(m, errors))
                try:
                    # the root entry: a fresh visitor gets Arabic; a stored choice is honoured further down
                    page.goto(B + "/", wait_until="load"); loads += 1
                    page.wait_for_url(f"{B}/ar/", timeout=5000)
                    # Home, a domain page, a record, /data/, Compare
                    for route in ("/", "/payments/", "/evidence/CLM-001/", "/data/"):
                        resp = page.goto(f"{B}/{lang}{route}", wait_until="load"); loads += 1
                        check(resp and resp.status == 200, f"{tag} {route}: HTTP {resp.status if resp else None}")
                        # the host headers' path patterns carry the base path, so the policy still reaches every page
                        check(resp and all(h in resp.headers for h in ("content-security-policy", "x-frame-options", "cache-control")),
                              f"{tag} {route}: the _headers rules did not reach the page under the base path")
                        check(page.evaluate("getComputedStyle(document.body).fontFamily").find("IBM Plex") >= 0,
                              f"{tag} {route}: the stylesheet did not apply")
                        check(page.evaluate("[...document.images].every(i=>i.complete&&i.naturalWidth>0)"), f"{tag} {route}: an image did not load")
                    # search: type a query, follow a result
                    page.goto(f"{B}/{lang}/payments/", wait_until="load"); loads += 1
                    visible(page, "[data-search-open]").click()
                    page.fill("#global-search-dialog", "remittances" if lang == "en" else "التحويلات")
                    page.wait_for_selector("#search-dialog .search-hit", timeout=5000)
                    hrefs = page.evaluate("[...document.querySelectorAll('#search-dialog .search-hit')].map(a=>a.getAttribute('href'))")
                    check(hrefs and all(h.startswith(f"{site.base}/{lang}/") for h in hrefs), f"{tag} search result outside {site.base}/{lang}/: {hrefs[:3]}")
                    first = hrefs[0] if hrefs else ""
                    page.click("#search-dialog .search-hit >> nth=0")
                    page.wait_for_load_state("load"); loads += 1
                    check(urlsplit(page.url).path == urlsplit(server + first).path, f"{tag} search result did not open: {page.url} vs {first}")
                    # a record: Copy citation, Share (the copy fallback), print
                    page.goto(f"{B}/{lang}/evidence/CLM-001/", wait_until="load"); loads += 1
                    want = f"{o}/{lang}/evidence/CLM-001/"
                    visible(page, "section.util [data-cite], .evidence-cite-button").click()
                    text = clipboard(page)
                    check(want in text, f"{tag} citation does not carry {want}: {text[-120:]!r}")
                    page.evaluate("navigator.clipboard.writeText('')")
                    visible(page, "[data-share]").click()
                    text = clipboard(page)
                    check(text.rstrip().endswith(want), f"{tag} share text does not end with {want}: {text[-120:]!r}")
                    visible(page, "[data-print]").click()
                    check(page.evaluate("window.__printed") == 1, f"{tag} print did not call window.print")
                    # Compare: the three measures, a record link followed, the link copied
                    q = "?records=CLM-001,CLM-054,FMIIP-BASELINE-2025-01"
                    page.goto(f"{B}/{lang}/evidence/compare/{q}", wait_until="load"); loads += 1
                    page.wait_for_selector("[data-compare-verdict]", timeout=5000)
                    sel = page.evaluate("['#compare-a','#compare-b','#compare-c','#compare-d'].map(s=>document.querySelector(s).value).filter(Boolean)")
                    check(sel == ["CLM-001", "CLM-054", "FMIIP-BASELINE-2025-01"], f"{tag} Compare selection {sel}")
                    links = page.evaluate("[...document.querySelectorAll('.compare-record-actions a')].map(a=>a.getAttribute('href'))")
                    check(len(links) == 3 and all(h.startswith(f"{site.base}/{lang}/evidence/") for h in links), f"{tag} Compare record links {links}")
                    page.evaluate("navigator.clipboard.writeText('')")
                    visible(page, "[data-compare-copy]").click()
                    text = clipboard(page)
                    check(text == f"{B}/{lang}/evidence/compare/{q}", f"{tag} Compare copied {text!r}")
                    visible(page, ".compare-record-actions a").click()
                    page.wait_for_load_state("load"); loads += 1
                    check(urlsplit(page.url).path == f"{site.base}/{lang}/evidence/CLM-001/", f"{tag} Compare record link opened {page.url}")
                    # a deep 404: its stylesheet, logo and runtime load from the base path, and its links work
                    deep = f"{B}/{lang}/no/such/page/at/depth/"
                    net.allowed_404.add(deep)
                    resp = page.goto(deep, wait_until="load"); loads += 1
                    check(resp and resp.status == 404 and page.locator(".nf").count() == 2, f"{tag} deep 404 did not render the 404 page")
                    check(page.evaluate("getComputedStyle(document.body).fontFamily").find("IBM Plex") >= 0, f"{tag} 404 stylesheet did not apply")
                    check(page.evaluate("[...document.images].every(i=>i.complete&&i.naturalWidth>0)"), f"{tag} 404 logo did not load")
                    page.click(f'section[lang="{lang}"] .actions a >> nth=0')
                    page.wait_for_load_state("load"); loads += 1
                    check(urlsplit(page.url).path == f"{site.base}/{lang}/", f"{tag} 404 home link opened {page.url}")
                    # the language switch keeps the page, and the root entry then honours the stored choice
                    page.goto(f"{B}/{lang}/payments/?x=1#s1", wait_until="load"); loads += 1
                    visible(page, "[data-lang]").click()
                    page.wait_for_url(f"{B}/{other}/payments/?x=1#s1", timeout=5000); loads += 1
                    check(page.evaluate("localStorage.getItem('yfie-lang')") == other, f"{tag} the language choice was not stored")
                    page.goto(B + "/", wait_until="load"); loads += 1
                    page.wait_for_url(f"{B}/{other}/", timeout=5000)
                    # this resource sets no cookie (its /privacy/ page says so); after every tool above, none exists
                    check(ctx.cookies() == [], f"{tag} a cookie was set: {[c['name'] for c in ctx.cookies()]}")
                except Exception as exc:   # a step that cannot run is a failure, named
                    problems.append(f"{tag} {type(exc).__name__}: {str(exc).splitlines()[0][:240]}")
                problems += [f"{tag} {e}" for e in errors]
                ctx.close()
        browser.close()
    if favicon:
        print("    note: the browser's own /favicon.ico request at the domain root (no page declares an icon) was seen and not failed")
    return problems + net.problems, loads, net.count


def negative_control_js(site: Site) -> list[str]:
    """Append a runtime address built by concatenation; the sweep must report it. Returns what stayed silent."""
    rel, code = NEGATIVE_JS
    f = site.root / rel
    original = f.read_text(encoding="utf-8")
    f.write_text(original + code, encoding="utf-8")
    try:
        hits = [p for p in Sweep(site).run().problems if p.startswith(rel) and "'/about/'" in p]
        return [] if hits else ["the sweep did not report the address built by concatenation in " + rel]
    finally:
        f.write_text(original, encoding="utf-8")


def negative_control(site: Site, server: str | None, chromium: str | None) -> list[str]:
    """Inject one root-absolute link; both the sweep and the browser must report it. Returns what stayed silent."""
    f = site.root / NEGATIVE_PAGE
    original = f.read_text(encoding="utf-8")
    broken = re.sub(r'(<main\b[^>]*>)', lambda m: m.group(1) + NEGATIVE_LINK, original, count=1)
    if broken == original:
        return ["the negative control could not inject its link"]
    f.write_text(broken, encoding="utf-8")
    silent = []
    try:
        hits = [p for p in Sweep(site).run().problems if NEGATIVE_PAGE in p and "/en/about/" in p]
        if not hits:
            silent.append("the sweep did not report the injected root-absolute link")
        if server:
            from playwright.sync_api import sync_playwright
            net = Net(server, site.base)
            with sync_playwright() as pw:
                browser = pw.chromium.launch(**({"executable_path": chromium} if chromium else {}))
                ctx = browser.new_context()
                net.attach(ctx)
                page = ctx.new_page()
                page.goto(f"{server}{site.base}/{NEGATIVE_PAGE.replace('index.html', '')}", wait_until="load")
                page.click("#yfie-negative-control")
                page.wait_for_load_state("load")
                browser.close()
            if not any("/en/about/" in p and "escaped the base path" in p for p in net.problems):
                silent.append("the browser did not report the request that left the base path")
    finally:
        f.write_text(original, encoding="utf-8")
    return silent


def chromium_path() -> str | None:
    exe = os.environ.get("YFIE_CHROMIUM")
    if exe:
        return exe
    return "/opt/pw-browsers/chromium" if Path("/opt/pw-browsers/chromium").exists() else None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--origin", default=ORIGIN)
    ap.add_argument("--site", help="a site already built with --origin (default: build one into a temporary directory)")
    ap.add_argument("--no-browser", action="store_true")
    ap.add_argument("--show", type=int, default=60, help="how many problems to print")
    args = ap.parse_args()
    if not urlsplit(args.origin).path:
        print("BASE PATH: FAIL (the origin carries no path; nothing to test)")
        return 1
    tmp = None
    try:
        if args.site:
            root = Path(args.site).resolve()
        else:
            tmp = Path(tempfile.mkdtemp(prefix="yfie-base-path-"))
            root = tmp / "site"
            r = subprocess.run([sys.executable, str(ROOT / "scripts/build.py"), "--origin", args.origin, "--out", str(root)],
                               cwd=ROOT, capture_output=True, text=True, env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
            print(r.stdout.strip() or r.stderr.strip())
            if r.returncode:
                print(r.stderr[-2000:])
                print("BASE PATH: FAIL (the build with the origin failed)")
                return 1
        site = Site(root, args.origin)
        sweep = Sweep(site).run()
        meta = metadata(site)
        print(f"(a) sweep: {sweep.files} files, {sweep.checked} addresses checked, {len(sweep.problems)} problems")
        print(f"(c) metadata: {len(meta)} problems")
        problems = sweep.problems + meta
        server = None
        srv = None
        chromium = chromium_path()
        if not args.no_browser:
            try:
                import playwright.sync_api  # noqa: F401
            except Exception:
                print("HARNESS UNAVAILABLE: python playwright not installed")
                return 2
            srv = serve(site)
            server = f"http://127.0.0.1:{srv.server_address[1]}"
            try:
                found, loads, reqs = browser_checks(site, server, chromium)
                print(f"(b) browser: {loads} page loads at 390 and 1440 px in both languages, {reqs} requests recorded, {len(found)} problems")
                problems += found
            except Exception as exc:
                problems.append(f"browser harness: {type(exc).__name__}: {exc}")
        try:
            silent = negative_control(site, server, chromium) + negative_control_js(site)
        finally:
            if srv:
                srv.shutdown()
        for p in problems[:args.show]:
            print("FAIL", p)
        if len(problems) > args.show:
            print(f"… and {len(problems) - args.show} more")
        print(f"NEGATIVE CONTROLS: {'CAUGHT' if not silent else 'NOT CAUGHT — ' + '; '.join(silent)} "
              f"(href=\"/en/about/\" injected into {NEGATIVE_PAGE}{'' if server else ', sweep only'}; "
              f"'/'+'en'+'/about/' appended to {NEGATIVE_JS[0]}, sweep)")
        ok = not problems and not silent
        print(f"BASE PATH: {'PASS' if ok else 'FAIL'} — {args.origin}/ ")
        return 0 if ok else 1
    finally:
        if tmp:
            shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    raise SystemExit(main())
