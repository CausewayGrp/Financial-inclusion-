"""The opened mobile menu's cite control can be scrolled into view (the header is static), Arabic and English, 320 and 390 px.
  python3 audit/release_candidate/checks/reach.py [OUT_DIR]"""
import functools, http.server, socketserver, sys, tempfile, threading
OUT = sys.argv[1] if len(sys.argv) > 1 else tempfile.mkdtemp(prefix="yfie-menu-")
from pathlib import Path
from playwright.sync_api import sync_playwright
from pathlib import Path
DIST=str(Path(__file__).resolve().parents[3] / "dist")
H=functools.partial(http.server.SimpleHTTPRequestHandler,directory=DIST); H.log_message=lambda *a: None
srv=socketserver.ThreadingTCPServer(("127.0.0.1",0),H); port=srv.server_address[1]
threading.Thread(target=srv.serve_forever,daemon=True).start()
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/opt/pw-browsers/chromium")
    for lang,w,h in (("ar",390,844),("en",320,568),("ar",320,568)):
        pg=b.new_page(viewport={"width":w,"height":h})
        pg.goto(f"http://127.0.0.1:{port}/{lang}/evidence/CLM-001/")
        pg.click("[data-menu]"); pg.wait_for_selector("#primary-nav.open")
        pos=pg.evaluate("getComputedStyle(document.querySelector('header.bar')).position")
        pg.locator("[data-menu-cite]").scroll_into_view_if_needed()
        r=pg.evaluate("(()=>{const b=document.querySelector('[data-menu-cite]').getBoundingClientRect();return [Math.round(b.top),Math.round(b.bottom),innerHeight]})()")
        # keyboard: Tab from the menu button reaches the cite control
        print(lang,w,h,"header position:",pos,"cite rect after scroll:",r,"in view:",r[0]>=0 and r[1]<=r[2])
        pg.screenshot(path=f"{OUT}/reach_{lang}_{w}x{h}.png")
        pg.close()
    b.close()
srv.shutdown()
