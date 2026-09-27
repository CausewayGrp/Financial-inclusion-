import functools, http.server, socket, threading, os, sys
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out'))
from playwright.sync_api import sync_playwright
os.makedirs('fold', exist_ok=True)
s=socket.socket(); s.bind(('127.0.0.1',0)); port=s.getsockname()[1]; s.close()
class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self,*a,**k): pass
h=http.server.ThreadingHTTPServer(('127.0.0.1',port), functools.partial(Q, directory='local'))
threading.Thread(target=h.serve_forever, daemon=True).start()
names=[f for f in sorted(os.listdir('local')) if f.endswith('.html')]
with sync_playwright() as p:
    b=p.chromium.launch()
    for f in names:
        m=f.endswith('-m.html'); w,hh=(390,844) if m else (1440,900)
        ctx=b.new_context(viewport={'width':w,'height':hh}); pg=ctx.new_page()
        pg.goto(f'http://127.0.0.1:{port}/{f}', wait_until='load'); pg.wait_for_timeout(120)
        pg.screenshot(path=f'fold/{f[:-5]}.png')
        if m:
            pg.evaluate('window.scrollTo(0,844)'); pg.wait_for_timeout(80); pg.screenshot(path=f'fold/{f[:-5]}-2.png')
        ctx.close()
    b.close()
h.shutdown(); print('fold shots:', len(names))
