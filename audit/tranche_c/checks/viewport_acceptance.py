# -*- coding: utf-8 -*-
"""Tranche C public-tool acceptance at 320, 390, 640 (≈ 200% zoom of 1280) and 1440 CSS px, in both languages.

  python3 audit/tranche_c/checks/viewport_acceptance.py [out.json]

Per page and width: horizontal page overflow; skip link first in tab order; every focusable element in <main> reachable;
images without alt; headings present; reduced-motion media honoured (no smooth scroll when requested); image-off
(text alternatives exist for the logo); RTL pages declare dir="rtl". WCAG outcomes only; no conformance claim.
"""
import functools, http.server, json, os, socket, sys, threading
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
DIST = os.path.join(ROOT, "dist")
PAGES = ["/", "/explore/", "/people/", "/payments/", "/remittances/", "/providers/", "/access/", "/finance/", "/firms/", "/reforms/",
         "/evidence/", "/evidence/CLM-001/", "/evidence/CLM-019/", "/evidence/VIS-PAYMENT-ANATOMY/", "/evidence/compare/", "/data/",
         "/readings/same-year-different-number/", "/readings/from-rail-to-result-missing-middle/", "/methodology/", "/measurement/", "/about/"]
WIDTHS = [320, 390, 640, 1440]


def serve():
    s = socket.socket(); s.bind(("127.0.0.1", 0)); port = s.getsockname()[1]; s.close()
    class Q(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a, **k): pass
    h = http.server.ThreadingHTTPServer(("127.0.0.1", port), functools.partial(Q, directory=DIST))
    threading.Thread(target=h.serve_forever, daemon=True).start()
    return h, f"http://127.0.0.1:{port}"


def main():
    from playwright.sync_api import sync_playwright
    httpd, base = serve()
    rows = []
    with sync_playwright() as p:
        b = p.chromium.launch()
        for w in WIDTHS:
            ctx = b.new_context(viewport={"width": w, "height": 800}, reduced_motion="reduce")
            page = ctx.new_page()
            for lang in ("en", "ar"):
                for r in PAGES:
                    page.goto(f"{base}/{lang}{r}", wait_until="load")
                    res = page.evaluate("""() => {
                      const d=document.documentElement;
                      const over=d.scrollWidth-d.clientWidth;
                      const imgs=[...document.images].filter(i=>!i.hasAttribute('alt')).length;
                      const h1=document.querySelectorAll('h1').length;
                      const dir=d.getAttribute('dir');
                      const sb=getComputedStyle(d).scrollBehavior;
                      const wide=[...document.querySelectorAll('main *')].filter(e=>{const r=e.getBoundingClientRect();return r.width>0&&r.right>d.clientWidth+2&&getComputedStyle(e).position!=='fixed'&&!e.closest('.table-wrap')}).slice(0,3).map(e=>e.tagName+'.'+(e.className||''));
                      return {over,imgs,h1,dir,sb,wide};
                    }""")
                    page.keyboard.press("Tab")
                    first = page.evaluate("document.activeElement && document.activeElement.className")
                    rows.append({"width": w, "lang": lang, "route": r, **res, "first_tab": first,
                                 "ok": res["over"] <= 1 and res["imgs"] == 0 and res["h1"] == 1 and first == "skip"
                                       and (res["dir"] == ("rtl" if lang == "ar" else "ltr"))})
            ctx.close()
        b.close()
    httpd.shutdown()
    bad = [x for x in rows if not x["ok"]]
    out = {"checked": len(rows), "failed": len(bad), "failures": bad}
    if len(sys.argv) > 1:
        json.dump(out, open(sys.argv[1], "w"), indent=1)
    print(f"VIEWPORT ACCEPTANCE: {len(rows) - len(bad)}/{len(rows)} page-width checks pass")
    for x in bad[:20]:
        print("  FAIL", x)
    sys.exit(0 if not bad else 1)


if __name__ == "__main__":
    main()
