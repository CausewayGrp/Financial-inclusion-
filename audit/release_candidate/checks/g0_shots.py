"""G0 presentation pass (owner instructions of 3 October 2026, 09:50): Home, the eight domain pages, one Evidence Record
and /about/, at 390 px in Arabic and at 1440 px in English; full-page screenshots plus the first screen, and a text dump
of each first screen for the readers."""
import functools, http.server, json, socketserver, sys, threading
from pathlib import Path
from playwright.sync_api import sync_playwright

DIST = Path(__file__).resolve().parents[3] / "dist"
OUT = Path(sys.argv[1] if len(sys.argv) > 1 else "/tmp/g0")
OUT.mkdir(parents=True, exist_ok=True)
ROUTES = ["", "people/", "payments/", "remittances/", "finance/", "firms/", "providers/", "reforms/", "access/",
          "evidence/CLM-002/", "about/"]
H = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(DIST))
H.log_message = lambda *a: None
srv = socketserver.ThreadingTCPServer(("127.0.0.1", 0), H); port = srv.server_address[1]
threading.Thread(target=srv.serve_forever, daemon=True).start()
res = []
with sync_playwright() as p:
    exe = "/opt/pw-browsers/chromium"
    b = p.chromium.launch(executable_path=exe) if Path(exe).exists() else p.chromium.launch()
    for lang, w, h in (("ar", 390, 844), ("en", 1440, 900)):
        for r in ROUTES:
            pg = b.new_page(viewport={"width": w, "height": h})
            pg.goto(f"http://127.0.0.1:{port}/{lang}/{r}", wait_until="networkidle")
            slug = (r.strip("/").replace("/", "_") or "home")
            pg.screenshot(path=str(OUT / f"{lang}_{w}_{slug}_first.png"))
            pg.screenshot(path=str(OUT / f"{lang}_{w}_{slug}_full.png"), full_page=True)
            first = pg.evaluate("""() => { const out=[]; const H=innerHeight;
              for (const e of document.querySelectorAll('main h1, main h2, main h3, main p, main li, main a.btn, main figure figcaption')) {
                const r=e.getBoundingClientRect(); if (r.top < H && r.bottom > 0 && e.offsetParent) out.push(e.tagName+': '+e.innerText.trim().slice(0,300)); }
              return out; }""")
            over = pg.evaluate("document.documentElement.scrollWidth > innerWidth")
            hgt = pg.evaluate("document.documentElement.scrollHeight")
            res.append({"lang": lang, "width": w, "route": "/" + r, "first_screen": first, "overflow_x": over, "page_height": hgt})
            pg.close()
    b.close()
srv.shutdown()
(OUT / "first_screens.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
print("G0 SHOTS:", len(res), "views →", OUT)
