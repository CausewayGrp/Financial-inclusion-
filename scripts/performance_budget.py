#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""First-load weight and time per page family, on a throttled mobile profile, in both languages (Part B B14 d).

  python3 scripts/performance_budget.py              # measure and print
  python3 scripts/performance_budget.py --json PATH  # also write the measurement

Serves `dist/` locally the way a static host would under `dist/_headers`: gzip for text files, and the cache rules the
header file declares. It then opens the twelve route classes of `docs/SUSTAINABILITY_METHOD.md` in English and Arabic,
each in a fresh browser context, so every load is cold. The page is 390 × 844 px, and the network is throttled with
the conditions Lighthouse uses for mobile: 150 ms round trip, 1.6 Mbit/s down, 750 kbit/s up, and the CPU slowed four
times.

Recorded per page: requests, bytes transferred (encoded, as on the wire) by type, first contentful paint, largest
contentful paint and the load event. One run per page on one machine. Timings are indicative, byte counts exact for
this build; neither is a measurement of the release host.
"""
from __future__ import annotations

import argparse
import gzip
import http.server
import io
import json
import socketserver
import sys
import threading
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
sys.path.insert(0, str(ROOT / "scripts" / "tests"))
from test_security_headers import headers_for, parse_headers  # noqa: E402

CLASSES = [("home", "/"), ("explore", "/explore/"), ("domain_answer", "/people/"), ("evidence_index", "/evidence/"),
           ("evidence_record", "/evidence/CLM-001/"), ("compare", "/evidence/compare/"), ("sources_directory", "/data/"),
           ("readings_index", "/readings/"), ("reading", "/readings/same-year-different-number/"), ("methodology", "/methodology/"),
           ("measurement", "/measurement/"), ("trust_about", "/about/")]
PROFILE = OrderedDict([("viewport", "390x844"), ("rtt_ms", 150), ("down_kbps", 1638.4), ("up_kbps", 750), ("cpu_slowdown", 4),
                       ("compression", "gzip for text files"), ("cache", "cold: a fresh browser context per page")])
TEXT = (".html", ".css", ".js", ".json", ".svg", ".xml", ".txt")
KIND = {".html": "html", ".css": "css", ".js": "js", ".json": "data", ".woff2": "fonts", ".png": "images", ".svg": "images", ".webp": "images"}


GZIP = True


def serve(rules):
    class H(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *a, **k):
            super().__init__(*a, directory=str(DIST), **k)

        def send_head(self):
            path = self.translate_path(self.path)
            p = Path(path)
            if p.is_dir():
                p = p / "index.html"
            if GZIP and p.suffix in TEXT and p.exists() and "gzip" in (self.headers.get("Accept-Encoding") or ""):
                body = gzip.compress(p.read_bytes(), compresslevel=6, mtime=0)
                self.send_response(200)
                self.send_header("Content-Type", self.guess_type(str(p)))
                self.send_header("Content-Encoding", "gzip")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                return io.BytesIO(body)
            return super().send_head()

        def end_headers(self):
            route = self.path.split("?", 1)[0]
            for name, value in headers_for(rules, route).items():
                if name != "Content-Security-Policy":   # the policy is checked by test_security_headers.py, not here
                    self.send_header(name, value)
            super().end_headers()

        def log_message(self, *a):
            pass

    srv = socketserver.ThreadingTCPServer(("127.0.0.1", 0), H)
    srv.daemon_threads = True
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv


def measure() -> OrderedDict:
    from playwright.sync_api import sync_playwright
    rules = parse_headers((DIST / "_headers").read_text(encoding="utf-8"))
    srv = serve(rules)
    base = f"http://127.0.0.1:{srv.server_address[1]}"
    out = OrderedDict()
    try:
        with sync_playwright() as pw:
            browser = pw.chromium.launch()
            for cls, route in CLASSES:
                for lang in ("en", "ar"):
                    ctx = browser.new_context(viewport={"width": 390, "height": 844}, device_scale_factor=2, is_mobile=True)
                    page = ctx.new_page()
                    cdp = ctx.new_cdp_session(page)
                    cdp.send("Network.enable")
                    cdp.send("Network.emulateNetworkConditions", {"offline": False, "latency": PROFILE["rtt_ms"],
                             "downloadThroughput": PROFILE["down_kbps"] * 1024 / 8, "uploadThroughput": PROFILE["up_kbps"] * 1024 / 8})
                    cdp.send("Emulation.setCPUThrottlingRate", {"rate": PROFILE["cpu_slowdown"]})
                    urls, sizes = {}, {}
                    cdp.on("Network.responseReceived", lambda e: urls.__setitem__(e["requestId"], e["response"]["url"]))
                    cdp.on("Network.loadingFinished", lambda e: sizes.__setitem__(e["requestId"], e["encodedDataLength"]))
                    page.add_init_script("window.__lcp=0;new PerformanceObserver(l=>{for(const e of l.getEntries())window.__lcp=Math.max(window.__lcp,e.startTime)}).observe({type:'largest-contentful-paint',buffered:true});")
                    url = f"{base}/{lang}{route}" if route != "/" else f"{base}/{lang}/"
                    page.goto(url, wait_until="load", timeout=120000)
                    page.wait_for_timeout(500)
                    t = page.evaluate("""() => { const n = performance.getEntriesByType('navigation')[0];
                        const fcp = (performance.getEntriesByName('first-contentful-paint')[0] || {}).startTime || 0;
                        return {fcp_ms: Math.round(fcp), lcp_ms: Math.round(window.__lcp), load_ms: Math.round(n.loadEventEnd)} }""")
                    by = OrderedDict()
                    for rid, n in sizes.items():
                        u = urls.get(rid, "")
                        k = KIND.get(Path(u.split("?", 1)[0]).suffix, "other")
                        b = by.setdefault(k, OrderedDict([("requests", 0), ("bytes", 0)]))
                        b["requests"] += 1
                        b["bytes"] += int(n)
                    # a second visit in the same context: what the cache rules of dist/_headers leave on the wire
                    sizes.clear()
                    page.goto(url, wait_until="load", timeout=120000)
                    page.wait_for_timeout(300)
                    warm = sum(int(n) for n in sizes.values())
                    out[f"{cls}:{lang}"] = OrderedDict([("route", f"/{lang}{route}"), ("requests", sum(x["requests"] for x in by.values())),
                                                        ("transferred_bytes", sum(x["bytes"] for x in by.values())), ("by_type", by)]
                                                       + list(t.items()) + [("warm_transferred_bytes", warm)])
                    ctx.close()
            browser.close()
    finally:
        srv.shutdown()
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", default="")
    ap.add_argument("--no-gzip", action="store_true", help="serve uncompressed (to show what host compression saves)")
    args = ap.parse_args()
    global GZIP
    GZIP = not args.no_gzip
    res = measure()
    print(f"{'page':28} {'req':>4} {'KB':>7} {'FCP ms':>7} {'LCP ms':>7} {'load ms':>8} {'warm KB':>8}")
    for k, v in res.items():
        print(f"{k:28} {v['requests']:>4} {v['transferred_bytes'] / 1024:>7.1f} {v['fcp_ms']:>7} {v['lcp_ms']:>7} {v['load_ms']:>8} {v['warm_transferred_bytes'] / 1024:>8.1f}")
    if args.json:
        prof = OrderedDict(PROFILE, compression="gzip for text files" if GZIP else "none")
        Path(args.json).write_text(json.dumps(OrderedDict([("profile", prof), ("pages", res)]), ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
