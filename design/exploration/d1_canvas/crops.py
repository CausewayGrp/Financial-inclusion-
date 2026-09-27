import functools, http.server, socket, threading, os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out'))
from playwright.sync_api import sync_playwright
os.makedirs('crops', exist_ok=True)
s=socket.socket(); s.bind(('127.0.0.1',0)); port=s.getsockname()[1]; s.close()
class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self,*a,**k): pass
h=http.server.ThreadingHTTPServer(('127.0.0.1',port), functools.partial(Q, directory='local'))
threading.Thread(target=h.serve_forever, daemon=True).start()
# the primary evidence area of each Record proposition, cropped as a reader would screenshot it
targets={'T1':'.entry.major','T2':'.col > .passage:first-of-type','T3':'#s1'}
with sync_playwright() as p:
    b=p.chromium.launch()
    for key,sel in targets.items():
        for lang in ('en','ar'):
            ctx=b.new_context(viewport={'width':1440,'height':900}); pg=ctx.new_page()
            pg.goto(f'http://127.0.0.1:{port}/{key}-record-{lang}-d.html', wait_until='load'); pg.wait_for_timeout(120)
            el=pg.query_selector(sel)
            el.screenshot(path=f'crops/{key}-record-{lang}-primary.png')
            ctx.close()
    # the figure of each Reading proposition, cropped alone
    fig={'T1':'figure.frame','T2':'figure.figure','T3':'figure.inset'}
    for key,sel in fig.items():
        for lang in ('en','ar'):
            ctx=b.new_context(viewport={'width':1440,'height':900}); pg=ctx.new_page()
            pg.goto(f'http://127.0.0.1:{port}/{key}-reading-{lang}-d.html', wait_until='load'); pg.wait_for_timeout(120)
            pg.query_selector(sel).screenshot(path=f'crops/{key}-reading-{lang}-figure.png')
            ctx.close()
    b.close()
h.shutdown(); print('crops:', sorted(os.listdir('crops')))
