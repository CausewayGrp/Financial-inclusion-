"""Visual check of the opened mobile menu at 320 and 390 px, EN and AR (owner decisions of 3 October 2026, point 3)."""
import http.server, socketserver, threading, functools, json, sys
from pathlib import Path
from playwright.sync_api import sync_playwright

DIST = Path(__file__).resolve().parents[3] / "dist"
OUT = Path(sys.argv[1] if len(sys.argv) > 1 else "/tmp/menu")
OUT.mkdir(parents=True, exist_ok=True)
H = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(DIST))
srv = socketserver.TCPServer(("127.0.0.1", 0), H); port = srv.server_address[1]
threading.Thread(target=srv.serve_forever, daemon=True).start()
res = []
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/opt/pw-browsers/chromium") if Path("/opt/pw-browsers/chromium").exists() else p.chromium.launch()
    for w in (320, 390):
        for lang in ("en", "ar"):
            for route in ("", "evidence/CLM-001/"):
                pg = b.new_page(viewport={"width": w, "height": 844})
                pg.goto(f"http://127.0.0.1:{port}/{lang}/{route}")
                header_h = pg.evaluate("document.querySelector('header.bar').getBoundingClientRect().height")
                pg.click("[data-menu]")
                pg.wait_for_selector("#primary-nav.open")
                info = pg.evaluate("""() => {
                  const n = document.querySelector('#primary-nav');
                  const trust = [...n.querySelectorAll('[data-menu-trust] a')].map(a => [a.textContent.trim(), a.getAttribute('href')]);
                  const cite = n.querySelector('[data-menu-cite]');
                  const r = n.getBoundingClientRect();
                  const over = [...n.querySelectorAll('a,button,span')].filter(e => { const b = e.getBoundingClientRect(); return b.width && (b.left < -1 || b.right > innerWidth + 1); }).length;
                  return {trust, cite: cite ? cite.textContent.trim() : null, cite_visible: !!(cite && cite.offsetParent),
                          menu_h: Math.round(r.height), doc_w: document.documentElement.scrollWidth, vw: innerWidth, overflowing: over};
                }""")
                info.update({"width": w, "lang": lang, "route": "/" + route, "header_h": round(header_h)})
                pg.screenshot(path=str(OUT / f"menu_{lang}_{w}_{route.strip('/').replace('/', '_') or 'home'}.png"), full_page=False)
                res.append(info)
                pg.close()
    b.close()
srv.shutdown()
ok = all(r["trust"] and r["trust"][0][1].endswith("/about/") and len(r["trust"]) == 7 and r["cite_visible"] and r["doc_w"] <= r["vw"] and r["overflowing"] == 0 for r in res)
print(json.dumps(res, ensure_ascii=False, indent=1))
print("MENU CHECK:", "PASS" if ok else "FAIL", f"({len(res)} views)")
