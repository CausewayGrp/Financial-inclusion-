import json,glob,os,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from pdefs_p2 import P2
from pdefs_p3 import P3
from pdefs_p4 import P4
def load(extra=()):
    sheets={os.path.basename(f)[:-5]:json.load(open(f)) for f in sorted(glob.glob(os.environ.get("YFI_MASTER_JSON", os.path.dirname(os.path.abspath(__file__))+"/master")+"/*.json")) if not f.endswith("_index.json")}
    for d in sorted([d for d in list(P2)+list(P3)+list(P4)+list(extra) if d["op"]=="SUBSTR"],key=lambda d:d["pid"]):
        for sh,recs in sheets.items():
            if d.get("sheets") and sh not in d["sheets"]: continue
            for r in recs:
                if d.get("rows") and (sh,r["_row"]) not in d["rows"]: continue
                for k,v in list(r.items()):
                    if k=="_row" or not isinstance(v,str): continue
                    if d.get("fields") and k not in d["fields"]: continue
                    if d["old"] in v: r[k]=v.replace(d["old"],d["new"])
    return sheets
