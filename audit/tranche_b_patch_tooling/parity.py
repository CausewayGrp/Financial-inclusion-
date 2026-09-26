import sys,re,json,collections; sys.path.insert(0,".")
from postpatch import load
AR_DIG=str.maketrans("٠١٢٣٤٥٦٧٨٩","0123456789")
def nums(t):
    t=(t or "").translate(AR_DIG)
    t=re.sub(r"(?<=\d),(?=\d{3})","",t)
    t=re.sub(r"\b(20)(\d\d)\s*[–-]\s*(\d\d)\b", lambda m: f"{m.group(1)}{m.group(2)}–{m.group(1)}{m.group(3)}", t)
    for w,n in (("الأحد عشر","11"),("الاثني عشر","12"),("اثني عشر","12"),("الاثنا عشر","12"),("الـ26","26")): t=t.replace(w,n)
    out=set(re.findall(r"\d+(?:\.\d+)?",t))
    return {x for x in out if not re.fullmatch(r"0?[1-9]|10|0",x)}  # ignore tiny ordinals (1–10)
def pairs(S):
    for sh in ["06_EVIDENCE_OBJECTS","07_PUBLIC_CLAIMS","09_READING_SECTIONS","10_MEASUREMENT_AGENDA","11_VISUAL_LIBRARY","08_READINGS","05_QUESTIONS","02_SITE_MAP"]:
        for r in S[sh]:
            for k in r:
                if k.endswith("_en") and k[:-3]+"_ar" in r:
                    yield sh, r, k[:-3], r.get(k), r.get(k[:-3]+"_ar")
    by=collections.defaultdict(dict)
    for r in S["03_PAGE_SECTIONS"]:
        key=(r["route"],r.get("section_order"))
        if r.get("body_en") is not None or r.get("heading_en") is not None: by[key]["en"]=r
        if r.get("body_ar") is not None or r.get("heading_ar") is not None: by[key]["ar"]=r
    for key,d in by.items():
        if "en" in d and "ar" in d:
            yield "03_PAGE_SECTIONS", d["en"], f"{key[0]}#s{key[1]}", (d["en"].get("heading_en") or "")+" "+(d["en"].get("body_en") or ""), (d["ar"].get("heading_ar") or "")+" "+(d["ar"].get("body_ar") or "")
def run(S):
    mis=[]
    tot=0
    for sh,r,f,en,ar in pairs(S):
        if sh=="02_SITE_MAP" and f=="full_copy": continue
        a,b=nums(en),nums(ar)
        if not a and not b: continue
        tot+=1
        if a!=b: mis.append((sh,r.get("_row"),f,sorted(a-b),sorted(b-a)))
    return tot,mis
if __name__=="__main__":
    import glob,os
    MJ=os.environ.get("YFI_MASTER_JSON", os.path.join(os.path.dirname(os.path.abspath(__file__)),"master"))
    base={os.path.basename(f)[:-5]:json.load(open(f)) for f in glob.glob(MJ+"/*.json") if not f.endswith("_index.json")}
    t0,m0=run(base); t1,m1=run(load())
    print("BEFORE: pairs with numbers",t0,"mismatched",len(m0)); print("AFTER : pairs with numbers",t1,"mismatched",len(m1))
    json.dump({"before":m0,"after":m1},open(os.environ.get("YFI_PARITY_OUT","parity_report.json"),"w"),ensure_ascii=False,indent=0)
    for x in m1: print(x)
