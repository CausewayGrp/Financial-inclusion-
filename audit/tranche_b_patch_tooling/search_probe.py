import json,re,sys
from urllib.parse import urlparse
import os
R=os.environ.get("YFI_REPO", os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","..")))
S=json.load(open(f"{R}/dist/static-data/search_index.json")); S=S if isinstance(S,list) else (S.get("records") or S.get("items") or list(S.values())[0])
def norm(v):
    v=str(v or '').casefold(); v=re.sub(r'[ً-ٰٟ]','',v)
    return v.replace('إ','ا').replace('أ','ا').replace('آ','ا').replace('ٱ','ا').replace('ى','ي')
def search(q,lang):
    toks=[x for x in re.split(r'\s+',norm(q.strip())) if x]; ranked=[]
    for x in S:
        t=norm(x.get(f'title_{lang}')); s=norm(x.get(f'summary_{lang}')); tx=norm(x.get(f'search_text_{lang}'))
        st=norm(' '.join(str(x.get(k) or '') for k in ('id','source_id','object_id','claim_id','reading_id')))
        sc=0
        for k in toks:
            if st==k: sc+=12
            elif k in st: sc+=7
            if k in t: sc+=6
            if k in s: sc+=3
            if k in tx: sc+=1
        if sc>0:
            r=urlparse(str(x.get('route') or x.get('primary_route') or x.get('public_route') or '/')).path
            r=r if r.endswith('/') else r+'/'
            ranked.append((sc,r,t))
    ranked.sort(key=lambda z:z[0],reverse=True); out=[]; seen=set()
    for sc,r,t in ranked:
        if (r,t) in seen: continue
        seen.add((r,t)); out.append(r)
        if len(out)>=10: break
    return out
TERMS=[ # (label, en, ar, expected-any routes or prefixes)
 ("account ownership","account ownership","امتلاك الحساب",["/people/","/evidence/CLM-001/"]),
 ("gender gap","gender gap","الفجوة بين الرجال والنساء",["/people/","/readings/gender-gap-measured-causes-open/"]),
 ("income gap","income","الدخل",["/people/"]),
 ("financial literacy","financial literacy","الثقافة المالية",["/people/","/reforms/"]),
 ("microfinance","microfinance","التمويل الأصغر",["/finance/","/readings/microfinance-structural-divergence/"]),
 ("credit","credit","الائتمان",["/finance/","/firms/"]),
 ("deposits","deposits","الودائع",["/finance/"]),
 ("SME finance","SME finance","تمويل المنشآت الصغيرة",["/firms/"]),
 ("POS","POS terminals","نقاط البيع",["/payments/"]),
 ("e-wallet","e-wallet","المحافظ الإلكترونية",["/payments/","/providers/"]),
 ("RTGS","RTGS","التسوية الإجمالية الفورية",["/payments/","/reforms/"]),
 ("remittances","remittances","الحوالات",["/remittances/"]),
 ("remittance cost","remittance cost","تكلفة التحويل",["/remittances/"]),
 ("exchange companies","exchange companies","شركات الصرافة",["/providers/","/access/"]),
 ("licensed banks","licensed banks","البنوك المرخصة",["/providers/"]),
 ("CBY Aden","Aden","عدن",["/providers/","/data/"]),
 ("Sanaa","Sanaa","صنعاء",["/providers/","/data/"]),
 ("CBY decision","decision","قرار",["/data/","/providers/","/reforms/"]),
 ("law","law","قانون",["/data/","/reforms/"]),
 ("regulation","regulation","لائحة",["/data/","/reforms/"]),
 ("consumer protection","consumer protection","حماية المستهلك",["/reforms/"]),
 ("complaints","complaints","الشكاوى",["/reforms/"]),
 ("FMIIP","FMIIP","FMIIP",["/reforms/","/payments/"]),
 ("cash transfer","cash transfer","التحويل النقدي",["/readings/after-transfer-persistence/","/payments/"]),
 ("identity KYC","KYC","اعرف عميلك",["/payments/","/people/","/measurement/"]),
 ("access points","access points","نقاط الوصول",["/access/"]),
 ("exchange rate","exchange rate","سعر الصرف",["/finance/","/data/"]),
 ("measurement agenda","measurement","القياس",["/measurement/"]),
]
res=[]
for lab,en,ar,exp in TERMS:
    row=[lab]
    for lang,q in (("en",en),("ar",ar)):
        got=search(q,lang)
        top3=any(g in exp for g in got[:3]); top10=any(g in exp for g in got[:10])
        row.append("PASS" if top3 else ("WEAK" if top10 else "FAIL")); row.append(got[:5])
    res.append(row)
if __name__=="__main__":
    import collections
    for r in res: print(f"{r[0]:<20} EN {r[1]:<4} {r[2][:4]} | AR {r[3]:<4} {r[4][:4]}")
    print("EN",collections.Counter(r[1] for r in res),"AR",collections.Counter(r[3] for r in res))
    nav=json.load(open(f"{R}/site-src/content/content/navigation_interaction.json"))
    for sm in nav["search_smoke_tests"]:
        for lang,k in (("en","query_en"),("ar","query_ar")):
            got=search(sm[k],lang); exp=set(sm["expected_routes"])
            print("SMOKE",lang,sm[k],"| any:",bool(exp & set(got)),"| all:",exp<=set(got))
