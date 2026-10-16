import sys,json,functools,http.server,threading
from pathlib import Path
from playwright.sync_api import sync_playwright
root=Path(sys.argv[1]); out=Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=True)
class Quiet(http.server.SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
server=http.server.ThreadingHTTPServer(('127.0.0.1',0),functools.partial(Quiet,directory=str(root/'dist')))
threading.Thread(target=server.serve_forever,daemon=True).start()
rows=[]
with sync_playwright() as p:
 b=p.chromium.launch(executable_path="/usr/bin/chromium")
 for lang in ('ar','en'):
  for w in (320,390,768,1024,1440):
   page=b.new_page(viewport={'width':w,'height':844 if w<600 else 1000 if w<1200 else 900},device_scale_factor=1)
   page.goto(f'http://127.0.0.1:{server.server_port}/{lang}/');page.evaluate('document.fonts.ready')
   rows.append({'lang':lang,'width':w,**page.evaluate('''() => ({overflow:document.documentElement.scrollWidth-innerWidth,height:document.documentElement.scrollHeight,fonts:document.fonts.status,sections:[...document.querySelectorAll('main section[id],main .head,.head .actions')].map(e=>({id:e.id||e.className,y:Math.round(e.getBoundingClientRect().y),height:Math.round(e.getBoundingClientRect().height)}))})''')})
   page.screenshot(path=str(out/f'{lang}-{w}-viewport.png'))
   if w in (390,1440):page.screenshot(path=str(out/f'{lang}-{w}-full.png'),full_page=True)
   page.close()
 b.close()
server.shutdown();(out/'metrics.json').write_text(json.dumps(rows,indent=2))
print(json.dumps(rows,indent=1))
