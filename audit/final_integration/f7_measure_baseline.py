# -*- coding: utf-8 -*-
"""F7 pre-Design sustainability baseline: what the reference build in dist/ transfers, per route class.

  python3 audit/final_integration/f7_measure_baseline.py <out.json>

Method (docs/SUSTAINABILITY_METHOD.md): headless Chromium (Playwright) loads one representative page per route class in
each language from a local static server (Python http.server: no compression, no CDN). Chrome DevTools Protocol network
events give, per request, the resource type, the bytes received on the wire (encodedDataLength) and whether it came
from cache. Cold = new browser context, empty cache. Warm = the same page opened again in the same context (the server
answers conditional requests with 304). One interaction is measured too: opening Search and typing a query loads the
local search index.

A second, modelled figure is given for each cold load: the same responses compressed with gzip (level 6), as a
typical static host would send them. It is a model, not a measurement. No carbon figure is computed before Design: the
final pages, images, scripts, fonts, caching and host will change the footprint, and a pre-design estimate would invite
the comparative claims the method forbids.
"""
import functools, gzip, http.server, json, os, socket, sys, threading
from collections import OrderedDict, defaultdict

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DIST = os.path.join(ROOT, "dist")
CLASSES = OrderedDict([
    ("home", "/"), ("explore", "/explore/"), ("domain_answer", "/people/"), ("evidence_index", "/evidence/"),
    ("evidence_record", "/evidence/CLM-001/"), ("compare", "/evidence/compare/"), ("sources_directory", "/data/"),
    ("readings_index", "/readings/"), ("reading", "/readings/same-year-different-number/"), ("methodology", "/methodology/"),
    ("measurement", "/measurement/"), ("trust_about", "/about/"),
])
TYPES = {"Document": "html", "Script": "js", "Stylesheet": "css", "Image": "images", "Font": "fonts", "Fetch": "data",
         "XHR": "data"}


def serve():
    s = socket.socket(); s.bind(("127.0.0.1", 0)); port = s.getsockname()[1]; s.close()

    class Q(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a, **k):
            pass
    h = http.server.ThreadingHTTPServer(("127.0.0.1", port), functools.partial(Q, directory=DIST))
    threading.Thread(target=h.serve_forever, daemon=True).start()
    return h, f"http://127.0.0.1:{port}"


def local_file(url, base):
    p = url[len(base):].split("?")[0].split("#")[0]
    if p.endswith("/"):
        p += "index.html"
    f = os.path.join(DIST, p.lstrip("/"))
    return f if os.path.isfile(f) else None


def record(page, action):
    cdp = page.context.new_cdp_session(page)
    cdp.send("Network.enable")
    reqs = {}
    cdp.on("Network.requestWillBeSent", lambda e: reqs.setdefault(e["requestId"], {"url": e["request"]["url"], "type": e.get("type")}))
    cdp.on("Network.responseReceived", lambda e: reqs.setdefault(e["requestId"], {}).update(
        {"status": e["response"]["status"], "cache": bool(e["response"].get("fromDiskCache") or e["response"].get("fromMemoryCache")),
         "type": e.get("type") or reqs.get(e["requestId"], {}).get("type")}))
    cdp.on("Network.loadingFinished", lambda e: reqs.setdefault(e["requestId"], {}).update({"bytes": e.get("encodedDataLength", 0)}))
    action()
    page.wait_for_load_state("networkidle")
    cdp.detach()
    return [r for r in reqs.values() if r.get("url", "").startswith("http")]


def summarise(rows, base):
    by = defaultdict(lambda: {"requests": 0, "bytes": 0})
    gz = 0
    for r in rows:
        k = TYPES.get(r.get("type"), "other")
        by[k]["requests"] += 1
        by[k]["bytes"] += int(r.get("bytes") or 0)
        f = local_file(r["url"], base)
        if f and r.get("status") == 200:
            data = open(f, "rb").read()
            gz += len(gzip.compress(data, 6)) if not f.endswith(".png") else len(data)
    total_b = sum(v["bytes"] for v in by.values())
    return OrderedDict([("requests", sum(v["requests"] for v in by.values())), ("transferred_bytes", total_b),
                        ("by_type", OrderedDict(sorted(by.items()))), ("modelled_gzip_bytes", gz)])


def main():
    out = sys.argv[1]
    from playwright.sync_api import sync_playwright
    httpd, base = serve()
    res = OrderedDict()
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        for cls, route in CLASSES.items():
            for lang in ("en", "ar"):
                url = f"{base}/{lang}{route}"
                ctx = b.new_context(viewport={"width": 1440, "height": 900})
                page = ctx.new_page()
                cold = record(page, lambda: page.goto(url, wait_until="load"))
                warm = record(page, lambda: page.goto(url, wait_until="load"))
                res[f"{cls}:{lang}"] = OrderedDict([("route", f"/{lang}{route}"), ("cold", summarise(cold, base)),
                                                    ("warm", summarise(warm, base))])
                ctx.close()
        for lang in ("en", "ar"):
            ctx = b.new_context(viewport={"width": 1440, "height": 900})
            page = ctx.new_page()
            page.goto(f"{base}/{lang}/", wait_until="networkidle")

            def search():
                page.keyboard.press("/") if False else page.click("[data-search-open]")
                page.fill("[data-search-input]", "account")
                page.wait_for_timeout(600)
            rows = record(page, search)
            res[f"interaction_search:{lang}"] = OrderedDict([("route", f"/{lang}/ + open Search, type a query"),
                                                             ("incremental", summarise(rows, base))])
            ctx.close()
        b.close()
    httpd.shutdown()
    json.dump(res, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for k, v in res.items():
        c = v.get("cold") or v.get("incremental")
        print(f"{k:28s} req={c['requests']:3d} bytes={c['transferred_bytes']:>10,d}  gz~{c['modelled_gzip_bytes']:>10,d}")


if __name__ == "__main__":
    main()
