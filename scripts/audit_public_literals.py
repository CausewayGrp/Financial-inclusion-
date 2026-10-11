#!/usr/bin/env python3
from pathlib import Path
from decimal import Decimal, InvalidOperation
import json, re, hashlib, sys

ROOT=Path(__file__).resolve().parents[1]
C=ROOT/'site-src/content'
AUDIT=ROOT/'audit'
AUDIT.mkdir(exist_ok=True)
OUT=AUDIT/'PUBLIC_LITERAL_CLOSURE.json'
if '--out' in sys.argv:                      # P5.1: the determinism test writes to a temporary file
    OUT=Path(sys.argv[sys.argv.index('--out')+1])
# Determinism (P5.1): every iteration that shapes a record's identity or order runs over a list or an insertion-ordered
# dict derived from the ordered projections. The remaining sets are used for membership tests only.


def load(p):
    return json.load(open(p,encoding='utf-8'))

def dump(p,obj):
    p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding="utf-8", newline="\n")

auth=load(ROOT/'authority/AUTHORITY.json')
master_path=ROOT/auth['production_master']['path'] if not str(auth['production_master']['path']).startswith('authority/') else ROOT/auth['production_master']['path']
# the path above resolves identically for the current authority schema
if not master_path.exists():
    master_path=ROOT/'authority/Yemen_Financial_Inclusion_Evidence_Master.xlsx'
master_sha=hashlib.sha256(master_path.read_bytes()).hexdigest()

bundle=load(C/'page_specs.json')
page_specs_sha=hashlib.sha256((C/'page_specs.json').read_bytes()).hexdigest()
closure=load(C/'sources/public_object_source_closure.json')

# ---------------------------------------------------------------------------------------------------------------------
# Public-literal audit v3 (close-out addendum, 11 October 2026; v2 was Pre-Tranche-C P1-D).
#
# Scope. Every number a reader sees in:
#   S1  a page's public title and its 03 section text;
#   S2  the governed copy of the records, claims and visual contracts bound to the page (its numeric inventory);
#   S3  the Measurement Agenda priorities the page renders (all ten, every public field, on /measurement/; the compact
#       card fields wherever else a priority is shown, including on the Readings bound to it);
#   S4  the Reading fields the page renders outside its sections (title, question, thesis, evidence period and
#       prohibited inference on the Reading's own page; title, thesis and evidence period on cards elsewhere).
# v2 read only S1 and S2 and, in S2, let any number that was not in a source-closed record's own text pass as
# "controlled dataset inventory or method metadata"; that fallback is removed.
#
# A number passes only as
#   (a) a date or period part (a year, a year-range tail, a day beside a month name);
#   (b) an identifier or a document reference (a record ID, a standard, "No. 7", "Table 6", "p. 17");
#   (c) a repository count resolved from the public inventory contract (S1 only, as before);
#   (d) present, on token boundaries, in the governed text of a source-closed record bound to the page, the priority
#       or the Reading — or of a partially resolved record that shows its partial state;
#   (e) for a composite record: present in the governed text of one of its LISTED member records that is itself
#       source-closed, or equal to a value of a governed data row the record's visual contract draws or tabulates,
#       whose source has a public locator (a composite's own text never traces itself);
#   (f) an explicitly allowed method or tool constant, or an inventory count the audit recomputes from the governed
#       data, each with its reason (scripts/literal_audit_allowances.json);
#   (g) listed, with the transaction that closes it, in scripts/literal_audit_open_traces.json — reported as open and
#       valid only for the Master that list names. It is never counted as resolved.
# Anything else is UNRESOLVED_SUBSTANTIVE_PUBLIC_NUMBER, a hard validation failure.
# ---------------------------------------------------------------------------------------------------------------------
num_rx=re.compile(r'(?:(?<=YER)|(?<=USD)|(?<=SAR)|(?<![A-Za-z0-9_]))(?<![0-9][.,])\d+(?:[,.]\d+)*%?')
year_rx=re.compile(r'^(?:19|20)\d{2}$')
MONTHS=r'(?:January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec|يناير|فبراير|مارس|أبريل|مايو|يونيو|يوليو|أغسطس|سبتمبر|أكتوبر|نوفمبر|ديسمبر)'
# a document reference or identifier: a number that names a document, a part of one, a standard or a record
DOCREF=(r'(?:No\.|Nos\.|Number|Issue|Table|Tables|Figure|Fig\.|Annex|Appendix|Article|Articles|Art\.|paragraph|para\.|¶|p\.|pp\.|page|pages'
        r'|Chapter|Section|Volume|Vol\.|sequence|Sequence|reference|Reference|Decision|Circular|Law|Resolution|Box'
        r'|المرجع|رقم|العدد|الأعداد|جدول|الجدول|الشكل|شكل|الملحق|المادة|المواد|الفقرة|ص\.|صفحة|الصفحة|القانون|القرار|التعميم|المنشور|الفصل|القسم|الإطار)')
ALLOWANCES=load(ROOT/'scripts/literal_audit_allowances.json')
ALLOW=ALLOWANCES['allowances']
OBJECT_ALLOW=ALLOWANCES.get('object_allowances') or []
INVENTORY_ALLOW=ALLOWANCES.get('inventory_counts') or []
OPEN=load(ROOT/'scripts/literal_audit_open_traces.json')
CLOSURE_BY_ID={}
CLOSURE_REC={}
for c in closure:
    CLOSURE_BY_ID.setdefault(c.get('object_id'),set()).add(c.get('closure_state'))
    CLOSURE_REC.setdefault(c.get('object_id'),c)
EVID={o['object_id']:o for o in load(C/'evidence/evidence_objects.json')}
CLAIM={o['claim_id']:o for o in load(C/'evidence/public_claims.json')}
VISLIB={o['visual_id']:o for o in load(C/'visuals/visual_library.json')}
SOURCES={s['source_id']:s for s in load(C/'sources/source_library.json')}
MA=[m for m in load(C/'content/measurement_agenda.json')]
MA_BY_ID={m['measurement_id']:m for m in MA}
READINGS={r['reading_id']:r for r in load(C/'content/readings.json')}
MA_FULL=('title','current_evidence','missing_evidence','unlocked_decision','decisions_unlocked','blocked_evidence','dimensions',
         'guardrail','feasibility','priority_basis','what_changes')                 # every public field (/measurement/)
MA_CARD=('title','current_evidence','missing_evidence','unlocked_decision')           # the card shown elsewhere
RD_PAGE=('title','question','thesis','evidence_period','prohibited_inference')         # the Reading's own page
RD_CARD=('title','thesis','evidence_period')                                           # a Reading card elsewhere
problems=[]


def normtok(t):
    return str(t).replace(',','').replace('%','')

def object_source_closed(objid):
    return 'CLOSED_TO_SOURCE_ID' in CLOSURE_BY_ID.get(objid,set())

def bounded(token,text):
    return re.search(r'(?<![0-9][.,])(?<![0-9])'+re.escape(token)+r'(?![0-9]|[.,][0-9])',text) is not None

def texts_of(rec):
    return [str(v) for k,v in rec.items() if isinstance(v,str)]

def governed_texts(oid):
    """The governed copy of a record (06 object, 07 claim or visual contract): its own string fields, never nested
    provenance notes."""
    out=[]
    for rec in (EVID.get(oid),CLAIM.get(oid),VISLIB.get(oid)):
        if rec:
            out.extend(texts_of(rec))
    return out

def governed_field(oid,field,fallback):
    """The text of a record's field as the governed projection holds it (06 object, 07 claim, visual contract): the page
    spec carries a copy, and the audit reads the original."""
    for rec in (EVID.get(oid),CLAIM.get(oid),VISLIB.get(oid)):
        if rec and isinstance(rec.get(field),str):
            return rec[field]
    return fallback

def public_locator(src):
    s=str(src or '')
    if s.startswith(('http://','https://')):
        return True
    return str((SOURCES.get(s) or {}).get('primary_url') or '').startswith(('http://','https://'))

# ---------------------------------------------------------------------------------------------- contract-bound rows
def data_blocks(rel,header_key):
    snap=load(C/rel)
    rows=snap.get('rows') or []
    out=[]
    for i,r in enumerate(rows):
        if not r or r[0]!=header_key:
            continue
        hdr=[str(x) if x is not None else None for x in r]
        for rr in rows[i+1:]:
            if not rr or all(c in (None,'') for c in rr) or rr[0]==header_key:
                break
            out.append({h:(rr[j] if j<len(rr) else None) for j,h in enumerate(hdr) if h})
    return out

def select_rows(spec):
    recs=data_blocks(spec['file'],spec['header_key'])
    key=spec.get('key',spec['header_key'])
    if 'ids' in spec:
        idx={}
        for r in recs:
            idx.setdefault(str(r.get(key)),r)
        return [(i,idx[i]) for i in spec['ids'] if i in idx]
    return [(str(r.get(key)),r) for r in recs if all(re.search(p,str(r.get(f) if r.get(f) is not None else '')) for f,p in spec['where'].items())]

def as_decimal(v):
    if isinstance(v,bool) or v in (None,''):
        return None
    try:
        return Decimal(str(v).replace(',',''))
    except InvalidOperation:
        return None

CONTRACT_ROWS={}
_vdc_in={v['visual_id']:v for v in load(ROOT/'scripts/projection/controlled_inputs/visual_design_contract.json')['visuals']}
for v in load(C/'visuals/visual_design_contracts.json')['visuals']:
    vid=v['visual_id']; rows=[]
    con=v.get('contract') or {}
    for s in con.get('series') or []:
        for x in s.get('values') or []:
            rows.append((x.get('id'),x.get('y'),x.get('source')))
    for o in con.get('objects') or []:
        for x in o.get('records') or []:
            for k,val in x.items():
                if k not in ('id','source','date','x') and as_decimal(val) is not None and not isinstance(val,str):
                    rows.append((x.get('id'),val,x.get('source')))
    table=v.get('table')
    if table:
        objs={}
        for o in (_vdc_in.get(vid,{}).get('table') or {}).get('objects') or []:
            objs[o['id']]=({rid:r for rid,r in select_rows(o['rows'])},o['fields'].get('source'))
        for r in table.get('rows') or []:
            cells=list(r.get('cells') or [])+([r['group']] if r.get('group') else [])
            for cell in cells:
                if 'number' not in cell:
                    continue
                oid,rid,_fld=cell['ref'].split('.',2)
                found,srcf=objs.get(oid,({},None))
                row=found.get(rid)
                rows.append((rid,cell['number'],(row or {}).get(srcf) if srcf else None))
    CONTRACT_ROWS[vid]=rows

def row_trace(vid,token):
    """A token equal to a value of a governed row this contract draws or tabulates (as printed, or rounded to the
    printed decimals), whose source has a public locator."""
    core=token.rstrip('%').replace(',','')
    t=as_decimal(core)
    if t is None:
        return None
    dp=len(core.split('.')[1]) if '.' in core else 0
    for rid,val,src in CONTRACT_ROWS.get(vid) or []:
        d=as_decimal(val)
        if d is None or not public_locator(src):
            continue
        if d==t or (dp>=1 and d.quantize(Decimal(1).scaleb(-dp),rounding='ROUND_HALF_UP')==t):
            return rid
    return None

# ---------------------------------------------------------------------------------------------- one trace function
def trace(oid,token,depth=0):
    """(kind, via) when the token traces through this record, else None. kind: CLOSED, PARTIAL, MEMBER, ROW."""
    states=CLOSURE_BY_ID.get(oid,set())
    texts=governed_texts(oid)
    if 'CLOSED_TO_SOURCE_ID' in states and any(bounded(token,t) for t in texts):
        return 'CLOSED',None
    if 'PARTIALLY_RESOLVED' in states and any(bounded(token,t) for t in texts):
        return 'PARTIAL',None
    if 'COMPOSITE_OF_OBJECTS' in states and depth<2:
        for m in (CLOSURE_REC.get(oid) or {}).get('resolved_via_object_ids') or []:
            if 'CLOSED_TO_SOURCE_ID' in CLOSURE_BY_ID.get(m,set()) and any(bounded(token,t) for t in governed_texts(m)):
                return 'MEMBER',m
        for m in (CLOSURE_REC.get(oid) or {}).get('resolved_via_object_ids') or []:
            r=trace(m,token,depth+1) if 'COMPOSITE_OF_OBJECTS' in CLOSURE_BY_ID.get(m,set()) else None
            if r:
                return 'MEMBER',m
    rid=row_trace(oid,token)
    if rid and states & {'CLOSED_TO_SOURCE_ID','PARTIALLY_RESOLVED','COMPOSITE_OF_OBJECTS'}:
        return 'ROW',rid
    return None

def date_or_identifier(token,context,start,end):
    bare=normtok(token)
    pre=context[max(0,start-24):start]; post=context[end:end+24]
    if token.endswith('%'):
        return None
    if year_rx.match(bare) and ',' not in token:
        return 'DATE_OR_PERIOD'
    if re.search(r'(?:19|20)\d{2}\s*[–/-]\s*$',pre) and re.fullmatch(r'\d{2}',bare):
        return 'DATE_OR_PERIOD'
    if bare.isdigit() and int(bare)<=31 and (re.match(r'\s*'+MONTHS,post) or re.search(MONTHS+r'\s*$',pre)):
        return 'DATE_OR_PERIOD'
    if re.search(r'[A-Z][A-Z0-9]*-(?:[A-Z0-9]+-)*$',pre) or re.search(r'(?:WCAG|ISO|BPM|IFRS|SDG)\s*$',pre):
        return 'STABLE_ID_OR_TECHNICAL_STANDARD'
    if re.search(DOCREF+r'\s*\(?$',pre):
        return 'STABLE_ID_OR_TECHNICAL_STANDARD'     # a document reference or decision number is an identifier, not a quantity
    if re.search(r'(?:SDG|ODD|الهدف)\s*\d+\.$',pre) or re.match(r'\.\d',post) and re.search(r'(?:SDG|indicator|المؤشر)\s*$',pre):
        return 'STABLE_ID_OR_TECHNICAL_STANDARD'
    return None

def allowed(route,obj,token,text):
    for a in ALLOW:
        if a['route']==route and token in a['tokens'] and a['context'] in text:
            return 'ALLOWED_METHOD_OR_TOOL_CONSTANT'
    for a in OBJECT_ALLOW:
        if a['object_id']==obj and token in a['tokens'] and a['context'] in text:
            return 'ALLOWED_METHOD_OR_TOOL_CONSTANT'
    for a in INVENTORY_ALLOW:
        if a['object_id']==obj and token in a['tokens'] and a['context'] in text and a.get('_verified'):
            return 'INVENTORY_COUNT_VERIFIED'
    return None

# inventory counts are recomputed from the governed data; an allowance whose count no longer matches is a failure
for a in INVENTORY_ALLOW:
    rows=select_rows(a['count'])
    if a['count'].get('distinct'):
        n=len({str(r.get(a['count']['distinct'])) for _,r in rows})
    else:
        n=len(rows)
    a['_verified']=all(normtok(t)==str(n) for t in a['tokens'])
    if not a['_verified']:
        problems.append(f"inventory allowance {a['object_id']} {a['tokens']} no longer equals the governed count {n}")

# ---------------------------------------------------------------------------------------------- S1: titles and sections
def bound_objects(spec):
    out={}
    for key,idk in (('governed_claims','claim_id'),('governed_evidence_objects','object_id'),('governed_visual_contracts','visual_id')):
        for g in spec.get(key) or []:
            out.setdefault(g.get(idk),None)
    return list(out)

def reading_binding_order(r):
    """P5.1 canonical rule for the records a Reading binds. The governed binding order is kept: 08 claim_bindings, then
    08 evidence_bindings, then the verification-path claim IDs; each ID is kept at its first occurrence (ordered
    de-duplication, never an unordered set). The first bound record whose governed text carries a literal is the one
    recorded as its source_object, so attribution is a function of the Master alone, not of the process hash seed."""
    ordered=[]
    for i in (r.get('claim_bindings') or []) + (r.get('evidence_bindings') or []) + ((r.get('verification_bindings') or {}).get('claim_ids') or []):
        if i not in ordered:
            ordered.append(i)
    return ordered

def measurement_binding_order(m):
    """A priority's records: 10 evidence_bindings in governed order (close-out addendum item 1); none before CLOSE-6A."""
    ordered=[]
    for i in (m.get('evidence_bindings') or []):
        if i not in ordered:
            ordered.append(i)
    return ordered

def classify_route_token(spec,route,token,context,start,end):
    cat=date_or_identifier(token,context,start,end)
    if cat:
        return cat,None,None
    objs=bound_objects(spec)
    for want,cat in (('CLOSED','ROUTE_SOURCE_CLOSED__OBJECT_TRACE_AVAILABLE'),('PARTIAL','ROUTE_PARTIAL_TRACE__PARTIAL_STATE_SHOWN'),
                     ('MEMBER','COMPOSITE_MEMBER_RECORD_TRACE'),('ROW','CONTRACT_BOUND_ROW_TRACE')):
        for oid in objs:
            r=trace(oid,token)
            if r and r[0]==want:
                return cat,oid,r[1]
    if spec.get('page_class')=='reading_detail':
        for rd in spec.get('governed_readings') or []:
            for oid in reading_binding_order(READINGS.get(rd['reading_id']) or rd):
                r=trace(oid,token)
                if r:
                    return 'READING_BOUND_RECORD_TRACE',oid,r[1]
    a=allowed(route,None,token,context)
    if a:
        return a,None,None
    return 'UNRESOLVED_SUBSTANTIVE_PUBLIC_NUMBER',None,None

def classify_object_token(route,oid,token,context,start,end):
    """S2: a number in the governed copy of a record bound to the page. A source-closed record's own number keeps its
    record trace (gate E2-READ then requires a value state for it there); dates and identifiers come next."""
    r=trace(oid,token)
    if r and r[0]=='CLOSED':
        return 'GOVERNED_OBJECT_SOURCE_CLOSED',None
    cat=date_or_identifier(token,context,start,end)
    if cat:
        return cat,None
    if r:
        return {'PARTIAL':'GOVERNED_OBJECT_PARTIAL_STATE_SHOWN','MEMBER':'COMPOSITE_MEMBER_RECORD_TRACE','ROW':'CONTRACT_BOUND_ROW_TRACE'}[r[0]],r[1]
    a=allowed(route,oid,token,context)
    if a:
        return a,None
    return 'UNRESOLVED_SUBSTANTIVE_PUBLIC_NUMBER',None

def classify_bound_token(route,subject,bound_ids,cat_ok,token,context,start,end):
    """S3 and S4: a number in a priority or a Reading traces only through the records that priority or Reading binds."""
    cat=date_or_identifier(token,context,start,end)
    if cat:
        return cat,None,None
    for oid in bound_ids:
        r=trace(oid,token)
        if r:
            return cat_ok,oid,r[1]
    a=allowed(route,subject,token,context)
    if a:
        return a,None,None
    return 'UNRESOLVED_SUBSTANTIVE_PUBLIC_NUMBER',None,None

def text_value(rec,f,lang):
    v=rec.get(f'{f}_{lang}')
    if isinstance(v,list):
        v=', '.join(str(x) for x in v)
    return v if isinstance(v,str) else ''

records=[]
def add(rec):
    records.append(rec)

for spec in bundle.get('page_specs',[]):
    route=spec.get('route')
    visible=[('title_en',spec.get('title_en'),set()),('title_ar',spec.get('title_ar'),set())]
    for sec in spec.get('sections') or []:
        for field in ['heading_en','body_en','heading_ar','body_ar']:
            if sec.get(field):
                inv={format(int(t['value']),',') for t in (sec.get('resolved_inventory_tokens') or []) if t.get('field')==field}
                visible.append((field,sec[field],inv))
    for field,context,inv_values in visible:
        for m in num_rx.finditer(context or ''):
            token=m.group(0)
            if token in inv_values and re.match(r'\s*$',(context or '')[m.end():m.end()+1] or ' '):
                cat,oid,via='INVENTORY_COUNT_FROM_CONTRACT',None,None     # P1.2: derived from content/public_inventory.json at generation time
            else:
                cat,oid,via=classify_route_token(spec,route,token,context,m.start(),m.end())
            rec={'route':route,'surface':'section' if field.startswith(('heading','body')) else 'title','field':field,'token':token,'category':cat,'context':context}
            if oid:
                rec['source_object']=oid
            if via:
                rec['trace_via']=via
            add(rec)

    # S2: the governed copy of the bound records, each field once, tokenised here (not by the projection's inventory)
    seen_fields=[]
    for n in spec.get('numeric_strings_in_governed_copy') or []:
        k=(n.get('source_object'),n.get('field'),str(n.get('context','')))
        if k not in seen_fields:
            seen_fields.append(k)
    for oid,field,spec_context in seen_fields:
        context=governed_field(oid,field,spec_context)
        for m in num_rx.finditer(context):
            token=m.group(0)
            cat,via=classify_object_token(route,oid,token,context,m.start(),m.end())
            rec={'route':route,'surface':'governed_numeric_inventory','field':field,'token':token,'category':cat,'context':context,'source_object':oid}
            if via:
                rec['trace_via']=via
            add(rec)

    # S3: the Measurement Agenda priorities the page renders
    if route=='/measurement/':
        shown=[(m,MA_FULL) for m in MA]
    else:
        ids=[m.get('measurement_id') for m in spec.get('governed_measurement_priorities') or []]
        page_readings=(spec.get('governed_readings') or []) if spec.get('page_class')=='reading_detail' else []
        for rd in page_readings:
            for x in (READINGS.get(rd['reading_id']) or {}).get('measurement_bindings') or []:
                if x not in ids:
                    ids.append(x)
        shown=[(MA_BY_ID[i],MA_CARD) for i in ids if i in MA_BY_ID]
    for m,fields in shown:
        mid=m['measurement_id']; bound=measurement_binding_order(m)
        for f in fields:
            for lang in ('en','ar'):
                context=text_value(m,f,lang)
                for mm in num_rx.finditer(context):
                    token=mm.group(0)
                    cat,oid,via=classify_bound_token(route,mid,bound,'MEASUREMENT_BOUND_RECORD_TRACE',token,context,mm.start(),mm.end())
                    rec={'route':route,'surface':'measurement_priority','field':f'{f}_{lang}','token':token,'category':cat,'context':context,'source_object':oid,'subject':mid}
                    if via:
                        rec['trace_via']=via
                    add(rec)

    # S4: the Reading fields the page renders outside its 03 sections
    shown=[]
    if spec.get('page_class')=='reading_detail':
        shown += [(READINGS.get(r['reading_id']) or r,RD_PAGE) for r in spec.get('governed_readings') or []]
        shown += [(READINGS.get(r['reading_id']) or r,RD_CARD) for r in spec.get('related_readings') or []]
    else:
        shown += [(READINGS.get(r['reading_id']) or r,RD_CARD) for r in spec.get('governed_readings') or []]
    if spec.get('featured_reading'):
        shown.append((READINGS.get(spec['featured_reading']['reading_id']) or spec['featured_reading'],RD_CARD))
    if route=='/readings/':
        shown += [(r,RD_CARD) for r in READINGS.values()]
    done=[]
    for r,fields in shown:
        rid=r['reading_id']
        if rid in done:
            continue
        done.append(rid)
        bound=reading_binding_order(r)
        for f in fields:
            for lang in ('en','ar'):
                context=text_value(r,f,lang)
                for mm in num_rx.finditer(context):
                    token=mm.group(0)
                    cat,oid,via=classify_bound_token(route,rid,bound,'READING_BOUND_RECORD_TRACE',token,context,mm.start(),mm.end())
                    rec={'route':route,'surface':'reading_record','field':f'{f}_{lang}','token':token,'category':cat,'context':context,'source_object':oid,'subject':rid}
                    if via:
                        rec['trace_via']=via
                    add(rec)

seen=set(); ded=[]
for r in records:
    key=(r.get('route'),r.get('surface'),r.get('field'),r.get('token'),r.get('category'),r.get('context'),r.get('source_object'),r.get('subject'))
    if key not in seen:
        seen.add(key); ded.append(r)
records=ded

# (g) open traces: listed, pinned to one Master, never counted as resolved; a stale entry is itself a failure
open_entries=OPEN.get('open') or []
if open_entries and OPEN.get('authority_master_sha256')!=master_sha:
    problems.append('scripts/literal_audit_open_traces.json lists open traces for another Master: close them or re-justify the list')
def open_match(e,r):
    """An entry names its record (or priority, or Reading); route "*" is allowed only then. Section numbers name a route."""
    obj=r.get('subject') or r.get('source_object') or ''
    if e['route']=='*' and not e['object']:
        return False
    return (e['route'] in ('*',r.get('route')) and e['surface']==r.get('surface') and e['object']==obj
            and e['field']==r.get('field') and e['token']==r.get('token'))
used=[]
for r in records:
    if r['category']!='UNRESOLVED_SUBSTANTIVE_PUBLIC_NUMBER':
        continue
    for n,e in enumerate(open_entries):
        if open_match(e,r):
            r['category']='OPEN_TRACE_LISTED'
            r['closes_in']=e['closes_in']
            if n not in used:
                used.append(n)
            break
for n,e in enumerate(open_entries):
    if n not in used:
        problems.append(f"stale open trace (no longer printed, or now traced): {e['route']} {e['surface']} {e['object']} {e['field']} {e['token']}")

unresolved=[r for r in records if r['category']=='UNRESOLVED_SUBSTANTIVE_PUBLIC_NUMBER']
open_traces=[r for r in records if r['category']=='OPEN_TRACE_LISTED']
summary={}
for r in records:
    summary[r['category']]=summary.get(r['category'],0)+1
surfaces={}
for r in records:
    surfaces[r['surface']]=surfaces.get(r['surface'],0)+1

report={
    'schema':'YFIE_PUBLIC_LITERAL_CLOSURE/3.0',
    'audit_version':'3.0 — close-out addendum (11 October 2026): Measurement Agenda priorities and Reading fields in scope; '
                    'composite records trace through a listed member or a governed data row; the inventory/method fallback '
                    'is removed. v2.0 (Pre-Tranche-C P1-D) removed v1 substring and paragraph-keyword rules.',
    'authority_master_sha256':master_sha,
    'page_specs_sha256':page_specs_sha,
    'scope':'Every number a reader sees in a page title and its section text (S1), the governed copy of the records, '
            'claims and visual contracts bound to the page (S2), the Measurement Agenda priorities the page renders (S3) '
            'and the Reading fields the page renders outside its sections (S4). Each must resolve to a source-closed '
            'record (directly, through a listed member record or through a governed data row with a public locator) or '
            'be a date, period, identifier, document reference, contract inventory count, recomputed inventory count or '
            'allowed method constant.',
    'classification_rule':'UNRESOLVED_SUBSTANTIVE_PUBLIC_NUMBER is a hard validation failure, and so is any audit problem. '
                          'OPEN_TRACE_LISTED is reported, never resolved, and valid only for the Master its list names. '
                          'Route/source presence without an object-level source-closed trace is not sufficient; a composite '
                          "record's own text never traces itself.",
    'record_count':len(records),
    'surfaces':surfaces,
    'summary':summary,
    'unresolved_substantive_count':len(unresolved),
    'open_trace_count':len(open_traces),
    'audit_problems':problems,
    'unresolved':unresolved,
    'records':records,
}
dump(OUT,report)
print(f'PUBLIC_LITERAL_CLOSURE records={len(records)} unresolved={len(unresolved)} open={len(open_traces)} problems={len(problems)}')
for p in problems:
    print('PROBLEM',p)
if unresolved or problems:
    for r in unresolved:
        print('UNRESOLVED',r['route'],r['surface'],r.get('subject') or r.get('source_object') or '',r['field'],r['token'])
    sys.exit(2)
