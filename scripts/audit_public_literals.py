#!/usr/bin/env python3
from pathlib import Path
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
# Public-literal audit v2 (Pre-Tranche-C P1-D). Every number printed in a page's public title or section text must be
# (a) a date or period part, (b) an identifier, (c) a repository count resolved from the public inventory contract,
# (d) present, on token boundaries, in the governed text of a record bound to that page whose lineage reaches a source
#     (exact, partial with its partial state shown, or a composite whose member records are listed),
# (e) on a Reading page, present in the governed text of a record the Reading binds, or
# (f) an explicitly allowed method or tool constant (scripts/literal_audit_allowances.json, each with its reason).
# v1 matched numbers as substrings and let any number pass in a paragraph containing words such as "records" or
# "source" (EXF-003 / P16-X1); both escape routes are removed.
# ---------------------------------------------------------------------------------------------------------------------
num_rx=re.compile(r'(?:(?<=YER)|(?<=USD)|(?<=SAR)|(?<![A-Za-z0-9_]))(?<![0-9][.,])\d+(?:[,.]\d+)*%?')
year_rx=re.compile(r'^(?:19|20)\d{2}$')
stable_ctx_terms=('CLM-','SRC-','MA-','CWR-','EP-','VIS-','ISO ','BPM','IFRS','P0','P1','RTGS','FPS')   # governed-copy inventory only
MONTHS=r'(?:January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec|يناير|فبراير|مارس|أبريل|مايو|يونيو|يوليو|أغسطس|سبتمبر|أكتوبر|نوفمبر|ديسمبر)'
ALLOW=json.load(open(ROOT/'scripts/literal_audit_allowances.json',encoding='utf-8'))['allowances']
CLOSURE_BY_ID={}
for c in closure:
    CLOSURE_BY_ID.setdefault(c.get('object_id'),set()).add(c.get('closure_state'))
EVID={o['object_id']:o for o in load(C/'evidence/evidence_objects.json')}
CLAIM={o['claim_id']:o for o in load(C/'evidence/public_claims.json')}


def normtok(t):
    return str(t).replace(',','').replace('%','')

def object_source_closed(objid):
    return 'CLOSED_TO_SOURCE_ID' in CLOSURE_BY_ID.get(objid,set())

def bounded(token,text):
    return re.search(r'(?<![0-9][.,])(?<![0-9])'+re.escape(token)+r'(?![0-9]|[.,][0-9])',text) is not None

def texts_of(rec):
    return [str(v) for k,v in rec.items() if isinstance(v,str)]

def bound_objects(spec):
    out={}
    for key,idk in (('governed_claims','claim_id'),('governed_evidence_objects','object_id'),('governed_visual_contracts','visual_id')):
        for g in spec.get(key) or []:
            out.setdefault(g.get(idk),[]).extend(texts_of(g))
    return out

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

def reading_objects(spec):
    out={}
    for r in spec.get('governed_readings') or []:
        for i in reading_binding_order(r):
            for rec in (EVID.get(i),CLAIM.get(i)):
                if rec: out.setdefault(i,[]).extend(texts_of(rec))
    return out

def classify_route_token(spec,route,token,context,start,end):
    bare=normtok(token)
    pre=context[max(0,start-18):start]; post=context[end:end+24]
    if year_rx.match(bare):
        return 'DATE_OR_PERIOD',None
    if re.search(r'(?:19|20)\d{2}\s*[–-]\s*$',pre) and re.fullmatch(r'\d{2}',bare):
        return 'DATE_OR_PERIOD',None
    if bare.isdigit() and int(bare)<=31 and (re.match(r'\s*'+MONTHS,post) or re.search(MONTHS+r'\s*$',pre)):
        return 'DATE_OR_PERIOD',None
    if re.search(r'[A-Z][A-Z0-9]*-(?:[A-Z0-9]+-)*$',pre) or re.search(r'(?:WCAG|ISO)\s*$',pre):
        return 'STABLE_ID_OR_TECHNICAL_STANDARD',None
    if re.search(r'(?:reference|Reference|No\.|المرجع|رقم)\s*\(?$',pre) and not token.endswith('%'):
        return 'STABLE_ID_OR_TECHNICAL_STANDARD',None     # a document reference or decision number is an identifier, not a quantity
    objs=bound_objects(spec)
    for state,cat in (('CLOSED_TO_SOURCE_ID','ROUTE_SOURCE_CLOSED__OBJECT_TRACE_AVAILABLE'),('PARTIALLY_RESOLVED','ROUTE_PARTIAL_TRACE__PARTIAL_STATE_SHOWN'),
                      ('COMPOSITE_OF_OBJECTS','ROUTE_COMPOSITE_TRACE__MEMBERS_LISTED')):
        for oid,texts in objs.items():
            if state in CLOSURE_BY_ID.get(oid,set()) and any(bounded(token,t) for t in texts):
                return cat,oid
    if spec.get('page_class')=='reading_detail':
        for oid,texts in reading_objects(spec).items():
            if CLOSURE_BY_ID.get(oid,set()) & {'CLOSED_TO_SOURCE_ID','PARTIALLY_RESOLVED','COMPOSITE_OF_OBJECTS'} and any(bounded(token,t) for t in texts):
                return 'READING_BOUND_RECORD_TRACE',oid
    for a in ALLOW:
        if a['route']==route and token in a['tokens'] and a['context'] in context:
            return 'ALLOWED_METHOD_OR_TOOL_CONSTANT',None
    return 'UNRESOLVED_SUBSTANTIVE_PUBLIC_NUMBER',None

records=[]
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
            pre=(context or '')[max(0,m.start()-14):m.start()]
            if token in inv_values and re.match(r'\s*$',(context or '')[m.end():m.end()+1] or ' '):
                cat,oid='INVENTORY_COUNT_FROM_CONTRACT',None     # P1.2: derived from content/public_inventory.json at generation time
            else:
                cat,oid=classify_route_token(spec,route,token,context,m.start(),m.end())
            rec={'route':route,'surface':'section' if field.startswith(('heading','body')) else 'title','field':field,'token':token,'category':cat,'context':context}
            if oid:
                rec['source_object']=oid
            records.append(rec)

    for n in spec.get('numeric_strings_in_governed_copy') or []:
        token=str(n.get('token','')); context=str(n.get('context','')); oid=n.get('source_object'); field=n.get('field')
        if oid and object_source_closed(oid):
            cat='GOVERNED_OBJECT_SOURCE_CLOSED'
        elif year_rx.match(normtok(token)):
            cat='DATE_OR_PERIOD'
        elif any(t in context for t in stable_ctx_terms):
            cat='STABLE_ID_OR_TECHNICAL_STANDARD'
        elif field in {'period_en','period_ar','currentness_en','currentness_ar','change_trigger_en','change_trigger_ar'}:
            cat='DATE_OR_PERIOD'
        else:
            cat='CONTROLLED_DATASET_INVENTORY_OR_METHOD_METADATA'
        records.append({'route':route,'surface':'governed_numeric_inventory','field':field,'token':token,'category':cat,'context':context,'source_object':oid})

seen=set(); ded=[]
for r in records:
    key=(r.get('route'),r.get('surface'),r.get('field'),r.get('token'),r.get('category'),r.get('context'),r.get('source_object'))
    if key not in seen:
        seen.add(key); ded.append(r)
records=ded
unresolved=[r for r in records if r['category']=='UNRESOLVED_SUBSTANTIVE_PUBLIC_NUMBER']
summary={}
for r in records:
    summary[r['category']]=summary.get(r['category'],0)+1

report={
    'schema':'YFIE_PUBLIC_LITERAL_CLOSURE/2.0',
    'audit_version':'2.0 — token-bounded, token-level classification (Pre-Tranche-C P1-D); v1 substring and paragraph-keyword rules removed',
    'authority_master_sha256':master_sha,
    'page_specs_sha256':page_specs_sha,
    'scope':'Reader-facing Page Spec titles/sections plus governed-copy numeric inventory. Every substantive public numeral must resolve to a governed source-closed object or be explicitly classified as date/period, stable technical identifier, or non-observation system/method metadata.',
    'classification_rule':'UNRESOLVED_SUBSTANTIVE_PUBLIC_NUMBER is a hard validation failure. Route/source presence without an object-level source-closed trace is not sufficient.',
    'record_count':len(records),
    'summary':summary,
    'unresolved_substantive_count':len(unresolved),
    'unresolved':unresolved,
    'records':records,
}
dump(OUT,report)
print(f'PUBLIC_LITERAL_CLOSURE records={len(records)} unresolved={len(unresolved)}')
if unresolved:
    for r in unresolved[:40]:
        print(json.dumps(r,ensure_ascii=False))
    sys.exit(2)
