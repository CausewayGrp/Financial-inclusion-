#!/usr/bin/env python3
from pathlib import Path
from html.parser import HTMLParser
import json,sys,re,html as _html,hashlib
from urllib.parse import urlparse, parse_qs, quote
ROOT=Path(__file__).resolve().parents[1]; DIST=ROOT/'dist'; C=ROOT/'site-src/content'
errors=[]; warns=[]
class P(HTMLParser):
    def __init__(self): super().__init__(); self.links=[]; self.lang=None; self.dir=None
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='html': self.lang=a.get('lang'); self.dir=a.get('dir')
        if tag=='a' and a.get('href'): self.links.append(a['href'])
bundle=json.load(open(C/'page_specs.json',encoding='utf-8')); specs=bundle.get('page_specs',[])
source_refs=json.load(open(C/'sources/source_reference_map.json',encoding='utf-8'))
source_ids={str(r.get('source_id')) for r in source_refs if r.get('source_id')}
source_by_id={str(r.get('source_id')):r for r in source_refs if r.get('source_id')}
def _http(v):
    # One locator rule with build.py: only an http(s) URL is a public original locator.
    v=str(v or '').strip()
    return v if v.lower().startswith(('http://','https://')) else ''
public_source_ids={str(r.get('source_id')) for r in source_refs if r.get('source_id') and (r.get('metadata_state')=='DISPLAY_READY' or _http(r.get('primary_url')))}
no_public_locator_ids=source_ids-public_source_ids
for lang,dirv in [('ar','rtl'),('en','ltr')]:
    for o in specs:
        route=str(o.get('route','/')).strip('/'); f=DIST/lang/route/'index.html'
        if not f.exists(): errors.append('missing '+str(f)); continue
        t=f.read_text(encoding='utf-8'); p=P(); p.feed(t)
        if p.lang!=lang or p.dir!=dirv: errors.append(f'locale/dir mismatch {f}')
        title=o.get('title_'+lang) or ''
        if title and title not in _html.unescape(t): errors.append(f'title missing {o.get("route")} {lang}')
        top=str(o.get('route','/')).strip('/').split('/',1)[0]
        if top in {'explore','evidence','readings','data','methodology','about'} and f'aria-current="page" href="/{lang}/{top}/"' not in t:
            errors.append(f'active navigation missing aria-current {o.get("route")} {lang}')
        for x in ['NOT_STARTED__','governed_claims','governed_evidence_objects','INTERNAL_ONLY','WITHHOLD']:
            if x in t: errors.append(f'backend/control leak {x} in {f}')
        for href in p.links:
            if href.startswith('/ar/') or href.startswith('/en/'):
                rr=href.split('?',1)[0].split('#',1)[0].strip('/'); bits=rr.split('/',1); lf=DIST/bits[0]/(bits[1] if len(bits)>1 else '')/'index.html'
                if not lf.exists(): errors.append(f'broken internal link {href} in {f}')
home=(DIST/'ar/index.html').read_text(encoding='utf-8')
for token in ['11.9%','12.91','561','1,473']:
    if token not in home: errors.append('home semantic token missing '+token)
for f in DIST.rglob('*.html'):
    t=f.read_text(encoding='utf-8')
    for pat in ['YFSI_','YFSI /','YFSI —','BAYAN','مرصد بيان','MASTER_BACKEND','S08','Claude','Replit','Figma','Next.js','Tailwind']:
        if pat in t: errors.append(f'legacy/vendor public leak {pat} in {f}')
    for pat in ['متحكم به','المقام','ساعات الدليل','ساعات أدلة','الحمولة العامة','عنصر متحكم','بوابة النشر','إعادة بناء الاشتقاق','قمع التمويل','قراءات محكومة']:
        if pat in t: errors.append(f'backend Arabic public leak {pat} in {f}')

# Current repository authority and finalization controls.
required_current=[
    ROOT/'authority/AUTHORITY.json',
    ROOT/'authority/CORE_CONSTITUTION.md',
    ROOT/'authority/YFI_CURRENT_PROJECT_CONTEXT.json',
    ROOT/'authority/Yemen_Financial_Inclusion_Evidence_Master.xlsx',
    ROOT/'README.md',
    ROOT/'handoff/IMPLEMENTATION_MANIFEST.json',
    ROOT/'handoff/MASTER_IMPLEMENTATION_PROMPT.md',
    ROOT/'handoff/CLAUDE_DESIGN_MASTER_PROMPT.md',
    ROOT/'handoff/CLAUDE_CODE_MASTER_PROMPT.md',
    ROOT/'design/architecture/README.md',
    ROOT/'design/architecture/YFIE_PUBLIC_SITE_MAP.svg',
    ROOT/'design/architecture/YFIE_FULL_STACK_SYSTEM_ARCHITECTURE.svg',
    ROOT/'design/architecture/YFIE_DESIGN_TO_CODE_FLOW.svg'
]
for req in required_current:
    if not req.exists(): errors.append('missing current control '+str(req))

auth={}; context={}
try:
    auth=json.load(open(ROOT/'authority/AUTHORITY.json',encoding='utf-8'))
    pm=auth.get('production_master') or {}
    master_sha=pm.get('sha256')
    if not master_sha: errors.append('authority Production Master SHA-256 missing')
    master_path=ROOT/'authority'/'Yemen_Financial_Inclusion_Evidence_Master.xlsx'
    if not master_path.exists():
        errors.append('canonical Production Master missing from authority/')
    else:
        actual_master_sha=hashlib.sha256(master_path.read_bytes()).hexdigest()
        if actual_master_sha!=master_sha: errors.append('bundled canonical Production Master hash differs from authority/AUTHORITY.json')
    if any(DIST.rglob('*.xlsx')): errors.append('Production Master/workbook must not be copied into public dist')
except Exception as e: errors.append('authority metadata unreadable '+str(e))

try:
    context=json.load(open(ROOT/'authority/YFI_CURRENT_PROJECT_CONTEXT.json',encoding='utf-8'))
    if context.get('role')!='COMPACT_PROJECTION_NOT_AUTHORITY': errors.append('project Context must declare subordinate projection role')
    cpm=context.get('production_master') or {}; cp=context.get('controlled_projection') or {}
    if cpm.get('sha256')!=master_sha: errors.append('project Context Master hash is stale')
    if (context.get('validation') or {}).get('master_sha256_recorded')!=master_sha: errors.append('project Context validation Master hash is stale')
    actual_page_specs_sha=hashlib.sha256((C/'page_specs.json').read_bytes()).hexdigest()
    if cp.get('page_specs_sha256')!=actual_page_specs_sha: errors.append('project Context Page Specs hash is stale')
    if cp.get('page_specs')!=len(specs): errors.append('project Context Page Spec count mismatch')
    if cp.get('all_page_specs_master_hash_match') is not True or cp.get('page_specs_index_master_hash_match') is not True:
        errors.append('project Context reports incomplete Page Spec authority binding')
except Exception as e: errors.append('project Context unreadable '+str(e))

# Claude Design -> Claude Code handoff remains non-authoritative and is draft until clean-room acceptance.
handoff_required=['README_FIRST.md','CLAUDE_DESIGN_MASTER_PROMPT.md','DESIGN_STARTING_TOKENS.json','DESIGN_TO_CODE_CONTRACT.md','CLAUDE_CODE_MASTER_PROMPT.md','STATIC_RUNTIME_AND_API_CONTRACT.md','IMPLEMENTATION_MANIFEST.json','HANDOFF_ACCEPTANCE_CHECKLIST.md','MASTER_IMPLEMENTATION_PROMPT.md']
for name in handoff_required:
    if not (ROOT/'handoff'/name).exists(): errors.append('missing design/code handoff file '+name)
try:
    him=json.load(open(ROOT/'handoff/IMPLEMENTATION_MANIFEST.json',encoding='utf-8'))
    ha=him.get('authority') or {}; hc=him.get('controlled_counts') or {}; hr=him.get('runtime_contract') or {}; rel=him.get('release_boundaries') or {}
    if ha.get('master_sha256')!=master_sha: errors.append('handoff manifest Master hash is stale')
    if ha.get('page_specs_sha256')!=hashlib.sha256((C/'page_specs.json').read_bytes()).hexdigest(): errors.append('handoff manifest Page Specs hash is stale')
    if hc.get('page_specs')!=len(specs): errors.append('handoff manifest Page Spec count mismatch')
    # Route baseline is derived, not frozen: one page per Page Spec and language, plus the root redirect and 404.
    if hc.get('generated_html_total_including_root_and_404')!=2*len(specs)+2: errors.append('handoff manifest static HTML baseline mismatch')
    if hr.get('mode')!='STATIC_FIRST_FULLY_LOCAL_PUBLIC_RUNTIME' or hr.get('core_runtime_network_dependency_allowed') is not False: errors.append('handoff runtime contract is not local-static-first')
    if rel.get('public_release_approved') is not False: errors.append('handoff must not claim public release approval')
    if 'non-authoritative' not in str(him.get('purpose','')).lower(): errors.append('handoff manifest must declare non-authoritative role')
    navm=him.get('navigation_contract') or {}
    if navm.get('path')!='site-src/content/content/navigation_interaction.json' or navm.get('authority_scope')!='NAVIGATION_AND_INTERACTION_ONLY':
        errors.append('handoff manifest navigation contract missing or invalid')
except Exception as e: errors.append('handoff implementation manifest unreadable '+str(e))

spec_master_hashes={str(o.get('authority_master_sha256')) for o in specs if o.get('authority_master_sha256')}
if master_sha and spec_master_hashes!={str(master_sha)}: errors.append('Page Spec authority hash does not match current Production Master authority')
index_hash=(bundle.get('index') or {}).get('authority_master_sha256')
if master_sha and index_hash!=master_sha: errors.append('Page Specs index authority hash does not match current Production Master authority')
actual_page_specs_sha=hashlib.sha256((C/'page_specs.json').read_bytes()).hexdigest()
# Checksum manifest is strict only after clean-room handoff promotion. During finalization it may lag canonical edits.
try:
    manifest_path=ROOT/'SHA256SUMS.txt'
    if manifest_path.exists():
        malformed=[]
        for raw in manifest_path.read_text(encoding='utf-8').splitlines():
            if raw.strip() and not re.match(r'^[0-9a-f]{64}  .+$',raw): malformed.append(raw[:120])
        if malformed: errors.append('malformed checksum manifest line '+malformed[0])
    if (context.get('release_boundary') or {}).get('live_public_release_approved') is True:
        if not manifest_path.exists(): errors.append('release-approved repository requires SHA256SUMS.txt')
except Exception as e:
    errors.append('checksum manifest unreadable '+str(e))

# R8.1 public-literal closure is a permanent validation dependency.
try:
    pla=json.load(open(ROOT/'audit/PUBLIC_LITERAL_CLOSURE.json',encoding='utf-8'))
    if pla.get('authority_master_sha256')!=master_sha: errors.append('public-literal audit Master hash is stale')
    if pla.get('page_specs_sha256')!=actual_page_specs_sha: errors.append('public-literal audit Page Specs hash is stale')
    if pla.get('unresolved_substantive_count')!=0: errors.append('public-literal audit has unresolved substantive public numbers')
except Exception as e:
    errors.append('public-literal audit missing or unreadable '+str(e))

# Recipient-facing authority hashes must not lag the current controlled state.
try:
    allowed_hashes={str(master_sha),str(actual_page_specs_sha)}
    recipient_hash_files=[ROOT/'README.md',ROOT/'handoff/README_FIRST.md',ROOT/'handoff/MASTER_IMPLEMENTATION_PROMPT.md',ROOT/'handoff/CLAUDE_DESIGN_MASTER_PROMPT.md',ROOT/'handoff/CLAUDE_CODE_MASTER_PROMPT.md',ROOT/'handoff/HANDOFF_ACCEPTANCE_CHECKLIST.md']
    for hp in recipient_hash_files:
        if not hp.exists(): continue
        htxt=hp.read_text(encoding='utf-8')
        for h in re.findall(r'\b[0-9a-f]{64}\b',htxt):
            if h not in allowed_hashes: errors.append(f'stale/unrecognized authority hash in recipient-facing file {hp.relative_to(ROOT)}: {h}')
    root_readme=(ROOT/'README.md').read_text(encoding='utf-8')
    if str(master_sha) not in root_readme or str(actual_page_specs_sha) not in root_readme:
        errors.append('root README does not identify current Master and Page Specs hashes')
except Exception as e:
    errors.append('recipient-facing authority hash validation failed '+str(e))

# Repository authority hygiene: one workbook authority, never a parallel spreadsheet source.
authority_dir=ROOT/'authority'
master_path=authority_dir/'Yemen_Financial_Inclusion_Evidence_Master.xlsx'
if authority_dir.exists():
    authority_files=[p for p in authority_dir.rglob('*') if p.is_file()]
    xlsx=[p for p in authority_files if p.suffix.lower()=='.xlsx']
    if len(xlsx)!=1 or xlsx[0].name!='Yemen_Financial_Inclusion_Evidence_Master.xlsx':
        errors.append('authority/ must contain exactly one canonical Production Master workbook')
# No other canonical workbook may exist elsewhere in the production repository.
repo_xlsx=[]
for p in ROOT.rglob('*.xlsx'):
    rel=p.relative_to(ROOT)
    if rel.parts and rel.parts[0] in {'dist','98_TEMPORARY__NONAUTHORITATIVE'}:
        continue
    repo_xlsx.append(p)
if repo_xlsx!=[master_path]:
    errors.append('canonical repository may contain exactly one .xlsx workbook, at authority/Yemen_Financial_Inclusion_Evidence_Master.xlsx')
# A repository declared hygiene-closed must not carry scratch artifacts into handoff.
temp_dir=ROOT/'98_TEMPORARY__NONAUTHORITATIVE'
temp_files=[p for p in temp_dir.rglob('*') if p.is_file()] if temp_dir.exists() else []
if temp_files:
    errors.append('temporary non-authoritative workspace must be empty in the canonical repository')

# Interaction baseline that the original structural validator did not cover.
css=(ROOT/'site-src/styles.css').read_text(encoding='utf-8')
js=(ROOT/'site-src/app.js').read_text(encoding='utf-8')
for token,label in [('.nav.open','mobile nav open state'),('.utilities .search-btn,.utilities .menu-btn{display:inline-flex}','small-screen search/menu visibility'),(':focus-visible','visible focus'),('.search-dialog','global search dialog')]:
    if token not in css: errors.append('missing '+label)
for token,label in [('aria-expanded','menu aria state'),('data-search-input','search binding'),('showModal','search dialog behavior'),('URLSearchParams','source query parsing'),('data-source-filter','source directory filtering'),('seen=new Map','search duplicate suppression'),("e.key==='Escape'",'escape closes mobile navigation'),("replace(/[إأآٱ]/g,'ا')",'Arabic search normalization'),("e.key.toLowerCase()==='k'",'global keyboard search shortcut')]:
    if token not in js: errors.append('missing '+label)

# Public-search routes must resolve to generated public pages; the index is a public payload.
search_records=[]
try:
    idx=json.load(open(DIST/'static-data/search_index.json',encoding='utf-8'))
    idx=idx if isinstance(idx,list) else idx.get('records',[])
    search_records=idx
    allowed={'page','question','evidence','reading','measurement','source','source_locator'}   # Tranche C JRN-05: governed questions
    for rec in idx:
        typ=rec.get('type') or rec.get('object_type')
        if typ not in allowed: errors.append('unexpected public search type '+str(typ))
        route=str(rec.get('route') or '/').split('?',1)[0].split('#',1)[0].strip('/')
        for lang in ('ar','en'):
            f=DIST/lang/route/'index.html'
            if not f.exists(): errors.append(f'public search route missing {lang}/{route} for {rec.get("id")}')
        if typ in {'source','source_locator'}:
            raw_route=str(rec.get('route') or rec.get('primary_route') or rec.get('public_route') or '')
            qs=parse_qs(urlparse(raw_route).query)
            sid=(qs.get('source') or [None])[0]
            if not sid: errors.append('source search result missing source query '+str(rec.get('id')))
            elif sid not in source_ids: errors.append('source search result references unknown source '+str(sid))
            else:
                for lang in ('ar','en'):
                    data_html=(DIST/lang/'data/index.html').read_text(encoding='utf-8')
                    if f'id="source-{sid}"' not in data_html: errors.append(f'source anchor missing {sid} on {lang} data page')
except Exception as e: errors.append('public search index unreadable '+str(e))

# Data source directory must complete the search journey without leaking internal metadata states.
for lang in ('ar','en'):
    data_file=DIST/lang/'data/index.html'
    if not data_file.exists():
        errors.append('missing Data source directory '+lang)
        continue
    dt=data_file.read_text(encoding='utf-8')
    if dt.count('data-source-record')!=len(public_source_ids): errors.append(f'source directory count mismatch {lang}')
    for sid in public_source_ids:
        if f'id="source-{sid}"' not in dt: errors.append(f'source directory missing {sid} {lang}')
    for sid in no_public_locator_ids:
        if f'id="source-{sid}"' in dt: errors.append(f'no-public-locator source exposed as directory card {sid} {lang}')
    for leak in ['LOCATOR_ONLY','DISPLAY_READY','OBJECT_LEVEL_OR_UNSPECIFIED']:
        if leak in dt: errors.append(f'internal source state leaked {leak} {lang}')

not_found=(DIST/'404.html').read_text(encoding='utf-8') if (DIST/'404.html').exists() else ''
for token in ['الصفحة غير موجودة','Page not found','data-search-open','/ar/explore/','/en/explore/']:
    if token not in not_found: errors.append('404 recovery missing '+token)

# Basic document semantics for generated public pages.
for f in DIST.rglob('*.html'):
    if f == DIST/'index.html':
        continue
    t=f.read_text(encoding='utf-8')
    ids=re.findall(r'\bid="([^"]+)"',t)
    dup_ids={x for x in ids if ids.count(x)>1}
    if dup_ids: errors.append('duplicate DOM id '+','.join(sorted(dup_ids))+' in '+str(f))
    if f != DIST/'404.html' and len(re.findall(r'<h1\b',t))!=1:
        errors.append('generated locale page must have exactly one h1 '+str(f))


# S01 archive review must remain exhaustive and non-authoritative.
try:
    areg=json.load(open(ROOT/'docs/S01_ARCHIVE_DISPOSITION_REGISTER.json',encoding='utf-8'))
    if areg.get('archive_top_level_items_reviewed') != len(areg.get('items',[])):
        warns.append('historical archive disposition count does not match item register')
    if areg.get('archive_top_level_items_reviewed',0) < 70:
        warns.append('historical archive disposition register is incomplete for S01 baseline')
    bad=[x for x in areg.get('items',[]) if not x.get('file') or not x.get('status') or not x.get('reason')]
    if bad: warns.append('historical archive disposition register has incomplete rows')
except Exception as e: warns.append('historical archive disposition register unavailable '+str(e))

try:
    readme=(ROOT/'README.md').read_text(encoding='utf-8')
    if 'single production repository' not in readme.lower() or 'sole semantic' not in readme.lower():
        errors.append('README must state repository and Production Master authority clearly')
except Exception as e: errors.append('README unreadable '+str(e))

# The live working repository is the Drive folder, never a ZIP-as-working-copy.
try:
    program=(ROOT/'docs/POST_BUILD_REVIEW_PROGRAM.md').read_text(encoding='utf-8')
    if 'repository ZIP is updated in place' in program: errors.append('review program still describes ZIP as working repository')
except Exception as e: warns.append('historical review program unavailable '+str(e))

# Empty and duplicate stable-ID cards are implementation defects, not evidence gaps.
for f in DIST.rglob('*.html'):
    t=f.read_text(encoding='utf-8')
    if '<p></p>' in t: errors.append('empty public paragraph/card in '+str(f))
    ids=[]
    for card in re.findall(r'<article class="answer-card[^>]*>.*?</article>',t,flags=re.S):
        m=re.search(r'<span class="badge[^>]*>(.*?)</span>',card,flags=re.S)
        if m: ids.append(re.sub('<.*?>','',m.group(1)).strip())
    dup={x for x in ids if x and ids.count(x)>1}
    if dup: errors.append('duplicate answer-card stable IDs '+','.join(sorted(dup))+' in '+str(f))


# S02 Home / Explore information architecture must be differentiated without losing controlled questions.
for lang in ('ar','en'):
    hf=DIST/lang/'index.html'; ef=DIST/lang/'explore/index.html'
    if hf.exists():
        ht=hf.read_text(encoding='utf-8')
        if 'class="task-card"' in ht: errors.append(f'S02 Home parallel task taxonomy must not reappear {lang}')
        if ht.count('class="question-card compact"') != 4: errors.append(f'S02 Home compact question count mismatch {lang}')
        if 'class="question-cluster"' in ht: errors.append(f'S02 Home must not duplicate full Explore clusters {lang}')
    if ef.exists():
        et=ef.read_text(encoding='utf-8')
        if et.count('class="question-card"') != 11: errors.append(f'S02 Explore must retain all 11 controlled questions {lang}')
        if et.count('class="question-cluster"') != 4: errors.append(f'S02 Explore question grouping mismatch {lang}')
        for qid in [f'QE-{i:03d}' for i in range(1,12)]:
            if qid not in et: errors.append(f'S02 Explore missing controlled question {qid} {lang}')


# S03 Domain Answer presentation contract and cumulative eight-route regression.
# The presentation contract is the single editable source of depth/order/prominence decisions.
try:
    presentation=json.load(open(C/'presentation_priority.json',encoding='utf-8'))
except Exception as e:
    presentation={}
    errors.append('presentation priority contract unreadable '+str(e))

expected_domain_routes={'people','access','firms','finance','payments','remittances','providers','reforms'}
entries=presentation.get('routes',[]) if isinstance(presentation,dict) else []
if presentation.get('authority_scope')!='PRESENTATION_DEPTH_ONLY':
    errors.append('presentation priority contract authority scope invalid')
if 'Domain Answer' not in (presentation.get('populated_families') or []):
    errors.append('presentation priority must include Domain Answer as a populated family')
route_entries={}
for e in entries:
    route=str(e.get('route') or '').strip('/')
    if not route:
        errors.append('presentation priority route missing')
        continue
    if route in route_entries:
        errors.append('duplicate presentation route mapping '+route)
    route_entries[route]=e
if set(route_entries)!=expected_domain_routes:
    errors.append('presentation priority eight-route coverage mismatch: '+str(sorted(set(route_entries)^expected_domain_routes)))

build_src=(ROOT/'scripts/build.py').read_text(encoding='utf-8')
if "PRESENTATION_PRIORITY=load(C/'presentation_priority.json')" not in build_src:
    errors.append('renderer is not consuming presentation priority contract')
if 'DOMAIN_CONFIG' in build_src:
    errors.append('obsolete DOMAIN_CONFIG compatibility layer remains in renderer')
if "'/people/': {" in build_src or "'/providers/': {" in build_src:
    errors.append('hard-coded route presentation decisions remain in renderer')

spec_by_route={str(o.get('route','')).strip('/'):o for o in specs}
detail_routes={}
for o in specs:
    if o.get('page_class')!='evidence_detail':
        continue
    for x in (o.get('governed_claims') or [])+(o.get('governed_evidence_objects') or [])+(o.get('governed_visual_contracts') or []):
        oid=x.get('claim_id') or x.get('evidence_object_id') or x.get('object_id') or x.get('visual_id')
        if oid and o.get('route'):
            detail_routes[str(oid)]=str(o.get('route'))

valid_kinds={'section','visual','route','verification_records','lead','supporting','primary','verify'}
for route,e in route_entries.items():
    if e.get('page_family')!='Domain Answer':
        errors.append('presentation page family mismatch '+route)
    for req in ['primary_user_task','primary_user_question','dominant_analytical_object','primary','supporting','progressive','linked','utility','first_load_exclusions','mobile_priority','always_visible_boundaries','primary_verify_destination']:
        if req not in e:
            errors.append(f'presentation field missing {route} {req}')
    spec=spec_by_route.get(route)
    if not spec:
        errors.append('S03 domain spec missing '+route)
        continue
    all_items=[]
    for tier in ['primary','supporting','progressive','linked','utility','first_load_exclusions','mobile_priority','always_visible_boundaries']:
        items=e.get(tier) or []
        if not isinstance(items,list):
            errors.append(f'presentation tier not list {route} {tier}')
            continue
        all_items.extend((tier,x) for x in items if isinstance(x,dict))
        for x in items:
            if not isinstance(x,dict) or x.get('kind') not in valid_kinds:
                errors.append(f'unknown presentation item kind {route} {tier} {x}')
    section_orders={x.get('section_order') for x in spec.get('sections',[]) if isinstance(x.get('section_order'),int)}
    for tier,x in all_items:
        if x.get('kind')=='section' and x.get('section_order') not in section_orders:
            errors.append(f'presentation section ref missing {route} {tier} {x.get("section_order")}')
    primary_sections=[x['section_order'] for x in e.get('primary',[]) if x.get('kind')=='section']
    progressive_sections=[x['section_order'] for x in e.get('progressive',[]) if x.get('kind')=='section']
    supporting_sections=[x['section_order'] for x in e.get('supporting',[]) if x.get('kind')=='section']
    exclusion_sections=[x['section_order'] for x in e.get('first_load_exclusions',[]) if x.get('kind')=='section']
    boundary_sections=[x['section_order'] for x in e.get('always_visible_boundaries',[]) if x.get('kind')=='section']
    if set(primary_sections)&set(progressive_sections):
        errors.append('presentation primary/progressive overlap '+route)
    # P1.3: band (supporting), primary and progressive tiers are disjoint and together cover every non-lead section,
    # so no section renders twice on a domain page.
    if set(supporting_sections)&(set(primary_sections)|set(progressive_sections)):
        errors.append('P1.3 presentation band section also rendered in primary/progressive '+route)
    expected_nonlead={o for o in section_orders if o!=1}
    if set(primary_sections)|set(progressive_sections)|set(supporting_sections) != expected_nonlead:
        errors.append('presentation section coverage/loss mismatch '+route)
    if set(exclusion_sections)!=set(progressive_sections):
        errors.append('first-load exclusions must equal progressive section set '+route)
    if not set(boundary_sections).issubset(set(supporting_sections)):
        errors.append('always-visible boundary must be in supporting tier '+route)
    visuals=[x for x in e.get('primary',[]) if x.get('kind')=='visual']
    if len(visuals)>1:
        errors.append('more than one primary visual '+route)
    visual_id=visuals[0].get('object_id') if visuals else None
    if visual_id and not any(x.get('visual_id')==visual_id for x in (spec.get('governed_visual_contracts') or [])):
        errors.append(f'S03 selected visual missing from controlled spec {route} {visual_id}')
    verify_ids=[]
    for x in e.get('utility',[]):
        if x.get('kind')=='verification_records':
            verify_ids.extend(str(z) for z in (x.get('object_ids') or []) if z)
    governed_ids=set()
    for x in (spec.get('governed_claims') or [])+(spec.get('governed_evidence_objects') or [])+(spec.get('governed_visual_contracts') or []):
        oid=x.get('claim_id') or x.get('evidence_object_id') or x.get('object_id') or x.get('visual_id')
        if oid: governed_ids.add(str(oid))
    governed_objects={}
    for x in (spec.get('governed_claims') or [])+(spec.get('governed_evidence_objects') or [])+(spec.get('governed_visual_contracts') or []):
        oid=x.get('claim_id') or x.get('evidence_object_id') or x.get('object_id') or x.get('visual_id')
        if oid: governed_objects[str(oid)]=x
    promoted_ids=list(verify_ids)
    if visual_id: promoted_ids.append(str(visual_id))
    for oid in promoted_ids:
        obj=governed_objects.get(oid)
        if not obj:
            errors.append(f'presentation promoted object not governed on route {route} {oid}')
            continue
        raw_public_routes=obj.get('public_routes') or obj.get('public_route_list') or []
        if isinstance(raw_public_routes,str): raw_public_routes=[x.strip() for x in raw_public_routes.split('|') if x.strip()]
        public_routes={str(x).strip('/') for x in raw_public_routes}
        if public_routes and route not in public_routes:
            errors.append(f'presentation promoted object not publication-eligible on route {route} {oid}')
    for oid in verify_ids:
        if oid not in governed_ids:
            errors.append(f'presentation verify object not governed on route {route} {oid}')
        if oid not in detail_routes:
            errors.append(f'presentation verify object lacks public Evidence Record {route} {oid}')
    target=str(e.get('primary_verify_destination') or '')
    target_clean=target.strip('/')
    if target_clean:
        for lang in ('ar','en'):
            if not (DIST/lang/target_clean/'index.html').exists():
                errors.append(f'primary verify destination missing {route} {lang} {target}')
    structural={}
    for lang in ('ar','en'):
        f=DIST/lang/route/'index.html'
        if not f.exists():
            errors.append(f'S03 domain HTML missing {route} {lang}')
            continue
        raw=f.read_text(encoding='utf-8'); text=_html.unescape(raw)
        shape={
            'hero':raw.count('class="hero domain-hero"'),
            'scope':raw.count('class="scope-item '),
            'boundary':raw.count('class="scope-item boundary"'),
            'primary':raw.count('<section class="domain-section'),
            'progressive_wrapper':raw.count('<details class="domain-more">'),
            'progressive':raw.count('class="domain-more-item"'),
            'visual':raw.count('class="domain-visual"'),
            'measure':raw.count('class="measure-next-card"'),
            'verify':raw.count('<section id="verify" class="domain-verify">'),
            'answer_card':raw.count('class="answer-card'),
        }
        expected={
            'hero':1,
            'scope':len(supporting_sections),
            'boundary':1 if boundary_sections else 0,
            'primary':len(primary_sections),
            'progressive_wrapper':1 if progressive_sections else 0,
            'progressive':len(progressive_sections),
            'visual':1 if visual_id else 0,
            'measure':min(int(e.get('measurement_limit') or 0),len(spec.get('governed_measurement_priorities') or [])),
            'verify':1,
            'answer_card':0
        }
        for k,val in expected.items():
            if shape[k]!=val:
                errors.append(f'S03 {k} count mismatch {route} {lang}: expected {val} got {shape[k]}')
        anchors=[raw.find('class="hero domain-hero"'),raw.find('class="domain-scope"'),raw.find('class="domain-core"')]
        if progressive_sections: anchors.append(raw.find('<details class="domain-more">'))
        anchors.append(raw.find('<section id="verify" class="domain-verify">'))
        if any(x<0 for x in anchors) or anchors != sorted(anchors):
            errors.append(f'S03 hierarchy order regression {route} {lang}')
        # Narrative-loss test: every governed reader-facing Page Spec section remains on the route.
        for sec in spec.get('sections',[]):
            body=sec.get(f'body_{lang}')
            for para in [p.strip() for p in str(body or '').split('\n') if p.strip()]:   # one rendered paragraph per authored line
                if para not in text:
                    errors.append(f'S03 controlled section lost {route} {lang} order={sec.get("section_order")}')
                    break
        if visual_id:
            visual=next((x for x in (spec.get('governed_visual_contracts') or []) if x.get('visual_id')==visual_id),None)
            vt=(visual or {}).get(f'title_{lang}') or (visual or {}).get('title') or ''
            if vt and vt not in text:
                errors.append(f'S03 selected visual identity mismatch {route} {lang}')
        for oid in verify_ids:
            if oid not in raw:
                errors.append(f'S03 direct verification record missing {route} {lang} {oid}')
        for dest in (f'/{lang}/evidence/',f'/{lang}/data/',f'/{lang}/methodology/'):
            if dest not in raw:
                errors.append(f'S03 verification destination missing {route} {lang} {dest}')
        # Always-visible safety boundary must render outside progressive disclosure.
        for bo in boundary_sections:
            secs=[s for s in spec.get('sections',[]) if s.get('section_order')==bo and s.get(f'body_{lang}')]
            if secs:
                needle=_first=next((ln.strip() for ln in str(secs[0].get(f'body_{lang}') or '').splitlines() if ln.strip()),'')
                pre=raw.split('<details class="domain-more">',1)[0]
                if needle and needle not in _html.unescape(pre):
                    errors.append(f'always-visible safety boundary not first-load {route} {lang} order={bo}')
        structural[lang]=(shape['scope'],shape['primary'],shape['progressive'],shape['visual'],shape['measure'],shape['verify'])
    if structural.get('ar') and structural.get('en') and structural['ar']!=structural['en']:
        errors.append(f'S03 AR/EN structural parity regression {route}')


# S04.1 Evidence Record family: intentional verification hierarchy and multi-entry discovery journey.
evidence_contract=(presentation.get('family_contracts') or {}).get('Evidence Record') if isinstance(presentation,dict) else None
if not isinstance(evidence_contract,dict):
    errors.append('S04.1 Evidence Record presentation contract missing')
    evidence_contract={}
else:
    if evidence_contract.get('page_family')!='Evidence Record' or evidence_contract.get('page_class')!='evidence_detail':
        errors.append('S04.1 Evidence Record contract family/class invalid')
    expected_contract_fields={
        'primary':{'summary','source_references'},
        'supporting':{'definition','universe','period','currentness','limitations'},
        'progressive':{'method','change_trigger','verification','page_reading_guidance'},
        'linked':{'public_routes','data_source','methodology','evidence_hub'},
        'utility':{'object_id','language','report_issue','citation','reuse','corrections'},
        'first_load_exclusions':{'method','change_trigger','verification','page_reading_guidance'},
        'mobile_priority':{'summary','universe','period','limitations','source_references','public_routes'},
        'always_visible_boundaries':{'limitations'},
    }
    for tier,allowed_fields in expected_contract_fields.items():
        actual=evidence_contract.get(tier)
        if not isinstance(actual,list):
            errors.append(f'S04.1 Evidence Record contract tier not list {tier}')
            continue
        unknown={str(x) for x in actual}-allowed_fields
        if unknown:
            errors.append(f'S04.1 Evidence Record contract contains non-schema/semantic content {tier}: {sorted(unknown)}')
    if evidence_contract.get('primary_verify_destination')!='source_references':
        errors.append('S04.1 Evidence Record contract primary verify destination must be source_references')

# Renderer must consume the same canonical presentation contract instead of defining a second evidence layout config.
for token,label in [
    ("EVIDENCE_PRESENTATION=FAMILY_PRESENTATION.get('Evidence Record')",'Evidence Record contract consumption'),
    ('def evidence_record_page(','Evidence Record renderer'),
    ("_evidence_contract_fields('supporting')",'Evidence Record supporting-field consumption'),
    ("_evidence_contract_fields('progressive')",'Evidence Record progressive-field consumption'),
    ("_evidence_contract_fields('always_visible_boundaries')",'Evidence Record boundary consumption'),
]:
    if token not in build_src: errors.append('missing '+label)
if 'def evidence_detail(' in build_src:
    errors.append('obsolete generic Evidence Record renderer remains')
if "elif cls=='evidence_detail':\n        body=evidence_record_page(spec,lang)" not in build_src:
    errors.append('Evidence Record page dispatch not bound to family renderer')

# Evidence Records are controlled Page Spec routes. Every public route must exist in both languages and bind one public object.
evidence_specs=[o for o in specs if o.get('page_class')=='evidence_detail']
evidence_route_set={str(o.get('route') or '') for o in evidence_specs}
_n_evidence_objects=len(json.load(open(C/'evidence/evidence_objects.json',encoding='utf-8')))
if len(evidence_specs)!=_n_evidence_objects:          # one public Evidence Record page per 06 record (derived, not frozen)
    errors.append(f'S04.1 Evidence Record pages ({len(evidence_specs)}) differ from 06 records ({_n_evidence_objects})')
object_to_spec={}
source_dependents={sid:set() for sid in public_source_ids}
for spec in evidence_specs:
    route=str(spec.get('route') or '')
    objs=spec.get('governed_evidence_objects') or []
    if len(objs)!=1:
        errors.append(f'S04.1 Evidence Record must bind exactly one governed evidence object {route}')
        continue
    obj=objs[0]
    oid=str(obj.get('evidence_object_id') or obj.get('object_id') or '')
    if not oid:
        errors.append(f'S04.1 Evidence Record missing governed object ID {route}')
        continue
    if oid in object_to_spec:
        errors.append(f'S04.1 duplicate Evidence Record object binding {oid}')
    object_to_spec[oid]=spec
    if route.rstrip('/') != f'/evidence/{oid}'.rstrip('/'):
        errors.append(f'S04.1 Evidence Record route/object mismatch {route} {oid}')
    public_routes=obj.get('public_route_list')
    if not isinstance(public_routes,list):
        public_routes=[x.strip() for x in str(obj.get('public_routes') or '').split('|') if x.strip()]
    public_routes=[('/'+str(x).strip('/')+'/') for x in public_routes if str(x).strip('/')]
    for lang in ('ar','en'):
        f=DIST/lang/route.strip('/')/'index.html'
        if not f.exists():
            errors.append(f'S04.1 missing Evidence Record route {route} {lang}')
            continue
        raw=f.read_text(encoding='utf-8'); text=_html.unescape(raw)
        pre=raw.split('<details class="evidence-more">',1)[0]
        pre_text=_html.unescape(pre)
        shape=(
            raw.count('data-evidence-family="Evidence Record"'),
            raw.count('class="evidence-record-summary"'),
            raw.count('class="evidence-fact '),
            raw.count('data-evidence-boundary-first-load'),
            raw.count('class="evidence-source-section"'),
            raw.count('class="evidence-related-section"'),
            raw.count('<details class="evidence-more">'),
            raw.count('class="evidence-utility"'),
        )
        if shape[0]!=1 or shape[1]!=1 or shape[3]!=1 or shape[4]!=1 or shape[5]!=1 or shape[6]!=1 or shape[7]!=1:
            errors.append(f'S04.1 Evidence Record structural family mismatch {route} {lang} {shape}')
        for field in ['title','summary','definition','universe','period','currentness']:
            value=obj.get(f'{field}_{lang}') or obj.get(field) or ''
            value=str(value) if value is not None else ''
            if value and value not in pre_text:
                errors.append(f'S04.1 first-load evidence field missing {route} {lang} {field}')
        # P4.3: the boundary is rendered as its two governed parts (does not establish | limits of the measure); both
        # must be first-load, and the authored delimiter itself is never printed.
        for part in ('does_not_establish','measurement_limitation'):
            value=str(obj.get(f'{part}_{lang}') or '')
            if value and value not in pre_text:
                errors.append(f'S04.1 material boundary hidden behind progressive disclosure {route} {lang} {part}')
        _lim=str(obj.get(f'limitations_{lang}') or '')
        if ' | ' in _lim and _lim in text:
            errors.append(f'P4-G02 boundary printed with its internal delimiter {route} {lang}')
        for field in ['method','change_trigger','verification']:
            if field=='method' and obj.get('visual_contract_state'):
                if (obj.get(f'method_{lang}') or '') and str(obj.get(f'method_{lang}')) in text:
                    errors.append(f'PB-0401 draft encoding note rendered while no governed contract exists {route} {lang}')
                continue
            value=obj.get(f'{field}_{lang}') or obj.get(field) or ''
            value=str(value) if value is not None else ''
            if value and value not in text:
                errors.append(f'S04.1 progressive evidence field missing {route} {lang} {field}')
        # Related interpretation/backtrack links must resolve in-language; Evidence-only objects still return to Evidence Hub.
        related=0
        for pr in public_routes:
            if pr.startswith('/evidence/'):
                continue
            dest=DIST/lang/pr.strip('/')/'index.html'
            if not dest.exists():
                errors.append(f'S04.1 related interpretation target missing {oid} {lang} {pr}')
            elif f'href="/{lang}/{pr.strip("/")}/"' not in raw:
                errors.append(f'S04.1 related interpretation link missing {oid} {lang} {pr}')
            else:
                related+=1
        if not related and f'href="/{lang}/evidence/"' not in raw:
            errors.append(f'S04.1 Evidence-only record lacks Evidence Hub backtrack {oid} {lang}')
        # No backend publication-state labels may appear on a record.
        for leak in ['LOCATOR_ONLY','DISPLAY_READY','NO_PUBLIC_LOCATOR','OBJECT_LEVEL_OR_UNSPECIFIED','rights_display_state','metadata_state']:
            if leak in raw: errors.append(f'S04.1 internal source/publication state leaked {route} {lang} {leak}')
        # Language equivalent must remain at the same Evidence Record route (header JS preserves query/hash globally).
        other='en' if lang=='ar' else 'ar'
        if f'hreflang="{other}" href="/{other}/{route.strip("/")}/"' not in raw:
            errors.append(f'S04.1 Evidence Record language alternate mismatch {route} {lang}')
    # Source references must resolve to controlled source records. Public locators link through Data + original; no-public-locator stays suppressed.
    for ref in spec.get('source_references') or []:
        sid=str(ref.get('source_id') or '').strip()
        if not sid:
            continue
        if sid not in source_by_id:
            errors.append(f'S04.1 Evidence Record source reference unresolved {oid} {sid}')
            continue
        controlled=source_by_id[sid]
        is_public=sid in public_source_ids and bool(_http(controlled.get('primary_url')))
        for lang in ('ar','en'):
            raw=(DIST/lang/route.strip('/')/'index.html').read_text(encoding='utf-8')
            if is_public:
                if f'/data/?source={sid}#source-{sid}' not in raw:
                    errors.append(f'S04.1 Evidence Record source-directory link missing {oid} {lang} {sid}')
                if str(controlled.get('primary_url')) not in _html.unescape(raw):
                    errors.append(f'S04.1 original source locator missing {oid} {lang} {sid}')
            else:
                if sid in raw or str(controlled.get('primary_url') or '') in raw and controlled.get('primary_url'):
                    errors.append(f'S04.1 no-public-locator dependency exposed {oid} {lang} {sid}')
        if is_public:
            source_dependents.setdefault(sid,set()).add(route)

# AR/EN structural parity and search/deep-link discoverability for every Evidence Record.
search_routes={str(r.get('route') or '').split('?',1)[0] for r in search_records if (r.get('type') or r.get('object_type'))=='evidence'}
for oid,spec in object_to_spec.items():
    route=str(spec.get('route') or '')
    if route not in search_routes:
        errors.append(f'S04.1 Evidence Record missing from public search {oid} {route}')
    shapes=[]
    for lang in ('ar','en'):
        raw=(DIST/lang/route.strip('/')/'index.html').read_text(encoding='utf-8')
        shapes.append((raw.count('class="evidence-fact '),raw.count('class="evidence-source-item"'),raw.count('class="evidence-context-link'),raw.count('class="evidence-more-item"')))
    if shapes[0]!=shapes[1]:
        errors.append(f'S04.1 AR/EN Evidence Record structural parity mismatch {oid}: {shapes}')

# Data/source start must expose dependent Evidence Records without rebuilding the S01 source directory.
for lang in ('ar','en'):
    dt=(DIST/lang/'data/index.html').read_text(encoding='utf-8')
    for sid,routes in source_dependents.items():
        if not routes:
            continue
        if f'data-dependent-evidence="{sid}"' not in dt:
            errors.append(f'S04.1 Data/source dependent-evidence disclosure missing {lang} {sid}')
        for route in routes:
            if f'href="/{lang}/{route.strip("/")}/"' not in dt:
                errors.append(f'S04.1 Data/source → Evidence Record link missing {lang} {sid} {route}')
    for sid in no_public_locator_ids:
        if f'data-dependent-evidence="{sid}"' in dt:
            errors.append(f'S04.1 no-public-locator source gained dependent public navigation {lang} {sid}')

# app.js already owns context-preserving language switching and source focus; S04.1 must not regress them.
for token,label in [("location.href='/'+target+p+location.search+location.hash",'same-route language switch'),("new URLSearchParams(location.search).get('source')",'query-aware source focus')]:
    if token not in js: errors.append('S04.1 missing '+label)



# S04.2 Compare + source/citation/rights/corrections/publication closure.
try:
    closure_rows=json.load(open(C/'sources/public_object_source_closure.json',encoding='utf-8'))
except Exception as e:
    closure_rows=[]; errors.append('S04.2 source-reference closure payload unreadable '+str(e))
try:
    passports=json.load(open(C/'evidence/evidence_passports.json',encoding='utf-8'))
except Exception as e:
    passports=[]; errors.append('S04.2 evidence-passport payload unreadable '+str(e))
passport_ids={str(x.get('passport_id')) for x in passports if x.get('passport_id')}
closure_by_key={(str(x.get('object_type')),str(x.get('object_id'))):x for x in closure_rows if x.get('object_type') and x.get('object_id')}

# Comparison uses the same canonical presentation contract and must remain compatibility-first.
comparison_contract=(presentation.get('family_contracts') or {}).get('Comparison') if isinstance(presentation,dict) else None
if 'Comparison' not in (presentation.get('populated_families') or []):
    errors.append('S04.2 Comparison must be a populated canonical presentation family')
if not isinstance(comparison_contract,dict):
    errors.append('S04.2 Comparison presentation contract missing'); comparison_contract={}
else:
    expected_compare={
        'primary':{'selected_records','compatibility_result'},
        'supporting':{'definition','universe','geography','unit','period','method','source_reference','currentness'},
        'progressive':{'limitations','verification'},
        'linked':{'evidence_record','data_source','methodology'},
        'utility':{'language','report_issue'},
        'first_load_exclusions':{'limitations','verification'},
        'mobile_priority':{'compatibility_result','definition','universe','period','method','evidence_record'},
        'always_visible_boundaries':{'compatibility_result'},
    }
    if comparison_contract.get('page_family')!='Comparison' or comparison_contract.get('template_route')!='/evidence/compare':
        errors.append('S04.2 Comparison contract family/route invalid')
    for tier,allowed in expected_compare.items():
        actual=comparison_contract.get(tier)
        if not isinstance(actual,list): errors.append(f'S04.2 Comparison contract tier not list {tier}'); continue
        unknown={str(x) for x in actual}-allowed
        if unknown: errors.append(f'S04.2 Comparison contract contains unsupported/semantic fields {tier}: {sorted(unknown)}')
    if comparison_contract.get('primary_verify_destination')!='evidence_record':
        errors.append('S04.2 Comparison primary verify destination must be evidence_record')

for token,label in [
    ("COMPARISON_PRESENTATION=FAMILY_PRESENTATION.get('Comparison')",'Comparison contract consumption'),
    ("supporting=list(COMPARISON_PRESENTATION.get('supporting')",'contract-driven comparison dimensions'),
    ('window.__COMPARE_DIMENSIONS__','generated contract dimensions'),
    ('data-comparison-family="Comparison"','Comparison family binding'),
    ('id="compare-c"','optional third comparison record'),
    ('id="compare-d"','optional fourth comparison record'),
    ('evidence_citation_context(','detached-use citation context'),
    ('evidence_trace(','source-reference trace renderer'),
    ('source_trust_controls(','source citation/reuse controls'),
    ('corrections_context_block(','correction/version context renderer'),
]:
    if token not in build_src: errors.append('S04.2 missing '+label)
for token,label in [
    ("meta[name=\"yfie-citation\"]",'governed detached citation'),
    ('data-source-cite','source-reference copy behavior'),
    ('window.__COMPARE_DIMENSIONS__','comparison contract consumption in client'),
    # Tranche C TOOL-01: geography and unit are not governed per record, so the hard firewall is definition, universe, method.
    ("requiredHard=new Set(['definition','universe','method'])",'comparison hard-dimension firewall'),
    ('const assessMany=','2–4 record compatibility assessment'),
    ('records.length<2','minimum two-record comparison guard'),
    ("state:'not-direct'",'not-direct comparison state'),
    ("state:'unresolved'",'unresolved comparison state'),
    ("state:'qualified'",'qualified comparison state'),
    ("new URLSearchParams(location.search).get('record')",'correction-origin context'),
]:
    if token not in js: errors.append('S04.2 missing '+label)
for forbidden in ['autoAverage','midpointValue','conversionScalar','preferredNumber']:
    if forbidden in js: errors.append('S04.2 forbidden forced-reconciliation logic present '+forbidden)

compare_spec=next((o for o in specs if o.get('route')=='/evidence/compare/'),None)
if not compare_spec:
    errors.append('S04.2 Compare Page Spec missing')
else:
    governed=[]
    for x in (compare_spec.get('governed_evidence_objects') or [])+(compare_spec.get('governed_claims') or []):
        oid=x.get('evidence_object_id') or x.get('object_id') or x.get('claim_id')
        if oid and str(oid) not in governed: governed.append(str(oid))
    shapes=[]
    for lang in ('ar','en'):
        cf=DIST/lang/'evidence/compare/index.html'
        if not cf.exists(): errors.append(f'S04.2 Compare route missing {lang}'); continue
        raw=cf.read_text(encoding='utf-8')
        if raw.count('data-comparison-family="Comparison"')!=1: errors.append(f'S04.2 Comparison family binding mismatch {lang}')
        if raw.count('data-compare-slot="required"')!=2 or raw.count('data-compare-slot="optional"')!=2:
            errors.append(f'S04.2 Compare must implement controlled 2–4 record selection {lang}')
        if 'class="answer-card' in raw: errors.append(f'S04.2 Compare must not duplicate governed objects as generic cards {lang}')
        m=re.search(r'window\.__COMPARE__=(.*?);window\.__COMPARE_DIMENSIONS__=(.*?);</script>',raw,re.S)
        if not m: errors.append(f'S04.2 Compare controlled payload missing {lang}'); continue
        try:
            payload=json.loads(_html.unescape(m.group(1))); dims=json.loads(_html.unescape(m.group(2)))
        except Exception as e:
            errors.append(f'S04.2 Compare payload unreadable {lang} {e}'); continue
        ids=[str(x.get('id')) for x in payload]
        if ids!=governed: errors.append(f'S04.2 Compare governed-object coverage/order mismatch {lang}')
        if len(ids)!=len(set(ids)): errors.append(f'S04.2 Compare duplicate object IDs {lang}')
        if any('value' in x or 'numeric_value' in x for x in payload): errors.append(f'S04.2 Compare payload must not lead with numeric values {lang}')
        expected_dims=[({'source_reference':'source'}.get(x,x)) for x in (comparison_contract.get('supporting') or [])]
        expected_dims=[x for x in expected_dims if x in {'definition','universe','geography','unit','period','method','source','currentness'}]
        if dims!=expected_dims: errors.append(f'S04.2 Compare renderer/contract dimension drift {lang}')
        for oid in ids:
            if oid not in detail_routes: errors.append(f'S04.2 Compare object lacks Evidence Record {lang} {oid}')
            elif f'"route": "{detail_routes[oid]}"' not in raw and f'"route":"{detail_routes[oid]}"' not in raw:
                errors.append(f'S04.2 Compare object record route missing in payload {lang} {oid}')
        shapes.append((len(payload),tuple(dims),raw.count('data-comparison-contract="Comparison"')))
    if len(shapes)==2 and shapes[0]!=shapes[1]: errors.append('S04.2 Compare AR/EN structural parity mismatch')

# Detached citation must carry enough context to travel with a record; publication filtering applies to citation too.
for oid,spec in object_to_spec.items():
    obj=(spec.get('governed_evidence_objects') or [{}])[0]
    route=str(spec.get('route') or '')
    public_sids=[]
    for ref in spec.get('source_references') or []:
        sid=str(ref.get('source_id') or '').strip()
        if sid in public_source_ids and sid in source_by_id and _http(source_by_id[sid].get('primary_url')): public_sids.append(sid)
    for lang in ('ar','en'):
        raw=(DIST/lang/route.strip('/')/'index.html').read_text(encoding='utf-8')
        mm=re.search(r'<meta name="yfie-citation" content="([^"]*)">',raw)
        if not mm: errors.append(f'S04.2 evidence citation context missing {oid} {lang}'); continue
        cite=_html.unescape(mm.group(1))
        if oid not in cite: errors.append(f'S04.2 citation missing stable record ID {oid} {lang}')
        for field in ['period','universe','does_not_establish','measurement_limitation']:   # P4.3: boundary as its two parts
            val=obj.get(f'{field}_{lang}') or obj.get(field) or ''
            if val and str(val).rstrip('.') not in cite: errors.append(f'S04.2 detached citation lost {field} {oid} {lang}')
        for sid in public_sids:
            if sid not in cite: errors.append(f'S04.2 detached citation missing public source ID {oid} {lang} {sid}')
        for sid in no_public_locator_ids:
            if sid in cite: errors.append(f'S04.2 detached citation leaked no-public-locator source {oid} {lang} {sid}')
        if f'/corrections/?record={quote(oid)}' not in raw: errors.append(f'S04.2 Evidence Record correction route missing {oid} {lang}')
        if 'data-cite' not in raw: errors.append(f'S04.2 Evidence Record cite utility missing {oid} {lang}')
        if 'source-rights-note' not in raw and public_sids: errors.append(f'S04.2 source reuse boundary missing {oid} {lang}')

# Source directory separates citation from redistribution and never exposes rights-state codes or no-public locators.
for lang in ('ar','en'):
    dt=(DIST/lang/'data/index.html').read_text(encoding='utf-8')
    if 'data-source-cite' not in dt: errors.append(f'S04.2 Data/source citation control missing {lang}')
    if 'source-rights-note' not in dt: errors.append(f'S04.2 Data/source reuse boundary missing {lang}')
    for leak in ['OBJECT_LEVEL_OR_UNSPECIFIED','rights_display_state','LOCATOR_ONLY','NO_PUBLIC_LOCATOR']:
        if leak in dt: errors.append(f'S04.2 Data/source internal rights/publication code leaked {lang} {leak}')
    for sid in no_public_locator_ids:
        if sid in dt: errors.append(f'S04.2 no-public-locator source leaked in Data {lang} {sid}')
    if re.search(r'<a[^>]+download(?:=|\s|>)',dt,re.I): errors.append(f'S04.2 uncontrolled source download exposed {lang}')

# Correction/version trail fails closed: no invented history, but originating evidence context is preserved.
for lang in ('ar','en'):
    cr=(DIST/lang/'corrections/index.html').read_text(encoding='utf-8')
    if 'data-correction-context' not in cr or 'data-correction-empty' not in cr:
        errors.append(f'S04.2 correction transparency block missing {lang}')
    if 'data-correction-link' not in cr: errors.append(f'S04.2 correction backtrack binding missing {lang}')
# Source-vintage hard case remains visible on CLM-032.
if 'CLM-032' in object_to_spec:
    sp=object_to_spec['CLM-032']; obj=(sp.get('governed_evidence_objects') or [{}])[0]
    for lang in ('ar','en'):
        raw=(DIST/lang/str(sp.get('route')).strip('/')/'index.html').read_text(encoding='utf-8'); txt=_html.unescape(raw)
        for field in ['currentness','change_trigger','does_not_establish','measurement_limitation']:   # P4.3: the boundary's two parts
            val=obj.get(f'{field}_{lang}') or obj.get(field) or ''
            if val and str(val) not in txt: errors.append(f'S04.2 vintage/correction hard case lost {field} CLM-032 {lang}')

# Source Reference Closure: public object -> governed dependency/passport -> source map -> public Evidence Record/citation.
def _closure(oid,preferred=('evidence_object','public_claim','visual')):
    for typ in preferred:
        r=closure_by_key.get((typ,oid))
        if r and r.get('resolved_source_ids'): return r
    for typ in preferred:
        r=closure_by_key.get((typ,oid))
        if r: return r
    return None
sample_rules={
    'CLM-001':'EP-FINDEX-2022-ACCOUNT','CLM-005':'EP-FIRM-2022','CLM-060':'EP-SMEPS-FINACCESS-KPI',
    'CLM-003':'EP-CBY-POS-MONTHLY','CLM-007':'EP-REMITTANCE-MACRO','CLM-055':'EP-CBY-BANK-ROSTER-2026',
    'CLM-011':'EP-CBY-FCP-REDRESS-2024','CLM-032':'EP-CBY-REMITTANCE-VINTAGE-K04'
}
for oid,pid in sample_rules.items():
    rows=[r for r in closure_rows if str(r.get('object_id'))==oid]
    if not rows: errors.append(f'S04.2 Source Reference Closure missing sample {oid}'); continue
    deps={str(d) for r in rows for d in (r.get('dependency_ids') or [])}
    if pid not in deps: errors.append(f'S04.2 expected evidence-passport dependency missing {oid} {pid}')
    if pid not in passport_ids: errors.append(f'S04.2 evidence-passport object missing {pid}')
    resolved={str(sid) for r in rows for sid in (r.get('resolved_source_ids') or [])}
    if not resolved: errors.append(f'S04.2 Source Reference Closure has no resolved sources {oid}')
    for sid in resolved:
        if sid not in source_by_id: errors.append(f'S04.2 closure resolves unknown source {oid} {sid}')
visual_closure=_closure('VIS-EVIDENCE-CLASS-LADDER',('visual','evidence_object','public_claim'))
# Tranche B Stage 1 (closure rule v2): a derived view carries a governed lineage state; it is never closed by dataset expansion.
if not visual_closure or visual_closure.get('closure_state') not in {'CLOSED_TO_SOURCE_ID','PARTIALLY_RESOLVED','COMPOSITE_OF_OBJECTS','COMPOSITE_MEMBERS_NOT_LISTED','SOURCE_NOT_YET_BOUND','FRAMING_NO_FACT'}:
    errors.append('S04.2 derived/visual Source Reference Closure lacks a governed lineage state VIS-EVIDENCE-CLASS-LADDER')
else:
    for sid in visual_closure.get('resolved_source_ids') or []:
        if str(sid) not in source_by_id: errors.append('S04.2 visual closure resolves unknown source '+str(sid))
# DISPLAY_READY and NO_PUBLIC_LOCATOR hard cases.
rows32=[r for r in closure_rows if str(r.get('object_id'))=='CLM-032']
resolved32={str(sid) for r in rows32 for sid in (r.get('resolved_source_ids') or [])}
if not any((source_by_id.get(sid) or {}).get('metadata_state')=='DISPLAY_READY' for sid in resolved32):
    errors.append('S04.2 CLM-032 hard case lacks DISPLAY_READY source resolution')
# NO_PUBLIC_LOCATOR hard case (Stage 1): CLM-044 is bound to a privately supplied report with no public locator.
# The source stays in the object's closure; no link, file name or locator note may reach the public page.
rows44=[r for r in closure_rows if str(r.get('object_id'))=='CLM-044' and r.get('object_type')=='evidence_object']
resolved44={str(sid) for r in rows44 for sid in (r.get('resolved_source_ids') or [])}
no_locator_sample='SRC-CCY-REMIT-ESTIMATE-2025'
if no_locator_sample not in resolved44: errors.append('S04.2 NO_PUBLIC_LOCATOR hard-case source missing from controlled closure CLM-044')
for lang in ('ar','en'):
    raw44=(DIST/lang/'evidence/CLM-044/index.html').read_text(encoding='utf-8')
    if 'USER_PROVIDED_FILE' in raw44 or 'Remittances in Yemen_Estimates' in raw44: errors.append(f'S04.2 NO_PUBLIC_LOCATOR note leaked on CLM-044 {lang}')

# S-LIN (Tranche B Stage 1): object-level lineage truth. Every Evidence Record carries one governed lineage state;
# its page lists only sources bound to that record; composite pages link member records; no candidate state remains.
LIN_STATES={'BOUND_EXACT','BOUND_PARTIAL','COMPOSITE_OF_OBJECTS','SOURCE_NOT_YET_BOUND','FRAMING_NO_FACT'}
eo_rows=json.load(open(C/'evidence/evidence_objects.json',encoding='utf-8'))
eo_clo={str(r.get('object_id')):r for r in closure_rows if r.get('object_type')=='evidence_object'}
for o in eo_rows:
    oid=str(o.get('object_id'))
    if o.get('lineage_state') not in LIN_STATES: errors.append(f'S-LIN evidence record without governed lineage_state {oid}')
    c=eo_clo.get(oid)
    if not c: errors.append(f'S-LIN closure missing for evidence record {oid}'); continue
    for sid in c.get('resolved_source_ids') or []:
        if sid not in source_by_id: errors.append(f'S-LIN bound source not in library {oid} {sid}')
        if sid not in (o.get('source_dependencies') or []): errors.append(f'S-LIN resolved source not declared in 06 source_dependencies {oid} {sid}')
    spec=object_to_spec.get(oid)
    if spec and spec.get('page_class')=='evidence_detail':
        refs={str(r.get('source_id')) for r in (spec.get('source_references') or [])}
        extra=refs-set(c.get('resolved_source_ids') or [])
        if extra: errors.append(f'S-LIN page spec lists sources not bound to {oid}: {sorted(extra)}')
        for lang in ('ar','en'):
            raw=(DIST/lang/str(spec.get('route')).strip('/')/'index.html').read_text(encoding='utf-8')
            shown=set(re.findall(r'data-evidence-source="([^"]+)"',raw))
            if shown-set(c.get('resolved_source_ids') or []): errors.append(f'S-LIN evidence page shows unbound source {oid} {lang} {sorted(shown-set(c.get("resolved_source_ids") or []))}')
            if c.get('closure_state')!='CLOSED_TO_SOURCE_ID' and 'data-lineage-state="'+str(c.get('closure_state'))+'"' not in raw:
                errors.append(f'S-LIN lineage statement missing {oid} {lang} {c.get("closure_state")}')
if any('BOUND_CANDIDATE' in json.dumps(o) for o in eo_rows): errors.append('S-LIN BOUND_CANDIDATE state remains after execution')

# Publication filtering must hold in Compare, citations, static source payload behavior and deep routes.
for lang in ('ar','en'):
    cmp=(DIST/lang/'evidence/compare/index.html').read_text(encoding='utf-8')
    for leak in ['WITHHOLD','INTERNAL_ONLY','NO_PUBLIC_LOCATOR','OBJECT_LEVEL_OR_UNSPECIFIED']:
        if leak in cmp: errors.append(f'S04.2 publication-state leak in Compare {lang} {leak}')
# A dependency with no public locator must not surface indirectly on any public HTML or search payload.
public_html_text='\n'.join(f.read_text(encoding='utf-8') for f in DIST.rglob('*.html'))
search_payload_text=(DIST/'static-data/search_index.json').read_text(encoding='utf-8')
for sid in no_public_locator_ids:
    if sid in public_html_text: errors.append(f'S04.2 no-public-locator dependency leaked in public HTML {sid}')
    if sid in search_payload_text: errors.append(f'S04.2 no-public-locator dependency leaked in public search payload {sid}')
# S04.3 (Pre-Tranche-C P4, V-D1): nor by the name of its producer. A producer is identified by the source-ID family code
# (SRC-<code>-...) when every source of that family lacks a public locator; known expansions of such codes are listed here.
from collections import defaultdict
_families=defaultdict(set)
for _sid in source_ids:
    _parts=str(_sid).split('-')
    if len(_parts)>2: _families[_parts[1]].add(str(_sid))
_hidden_producers=sorted(k for k,v in _families.items() if v and v<=set(no_public_locator_ids))
_producer_expansions={'CCY':['Cash Consortium of Yemen','ائتلاف النقد']}
_public_plain=_html.unescape(re.sub(r'<[^>]+>',' ',public_html_text))
for _code in _hidden_producers:
    for _tok in [_code]+_producer_expansions.get(_code,[]):
        _pat=r'(?<![A-Za-z0-9-])'+re.escape(_tok)+r'(?![A-Za-z0-9])'
        if re.search(_pat,_public_plain): errors.append(f'S04.3 producer of a source without a public locator is named in public HTML: {_tok}')
        if re.search(_pat,search_payload_text): errors.append(f'S04.3 producer of a source without a public locator is named in the search payload: {_tok}')
# The same holds for the governed payloads a runtime ships ("evidence objects, claims and passports used by the site",
# visual contracts, interface copy, Page Specs) for producers whose material is withheld (those with a recorded name
# expansion). Identifiers such as SRC-<code>-... are internal lineage keys, not names; a public institution cited generically
# as a class of primary source (e.g. "CBY/MOPIC/OECD-INFE primary sources") is not a named withheld source.
for _rel in ('evidence/evidence_passports.json','evidence/evidence_objects.json','visuals/visual_design_contracts.json',
             'content/interface_copy.json','page_specs.json','content/readings.json','content/page_sections.json'):
    _t=(C/_rel).read_text(encoding='utf-8')
    for _code in [c for c in _hidden_producers if c in _producer_expansions]:
        for _tok in [_code]+_producer_expansions.get(_code,[]):
            if re.search(r'(?<![A-Za-z0-9_-])'+re.escape(_tok)+r'(?![A-Za-z0-9_])',_t):
                errors.append(f'S04.3 producer of a source without a public locator is named in the governed payload {_rel}: {_tok}')
# A Reading whose path lists unlisted material must not claim that every source is named without saying so.
_ui={r['ui_id']:r for r in json.load(open(C/'content/interface_copy.json',encoding='utf-8'))}
for _lang in ('ar','en'):
    _plain=_ui['UI-READING-PATH-COMPLETE'][f'label_{_lang}']; _unl=_ui['UI-SOURCE-NO-PUBLIC-LOCATOR'][f'label_{_lang}']
    for _f in (DIST/_lang/'readings').glob('*/index.html'):
        _t=_html.unescape(_f.read_text(encoding='utf-8'))
        if _unl in _t and f'>{_plain}<' in _t:
            errors.append(f'S04.3 Reading path claims complete named sources while a record rests on unlisted material {_f.relative_to(DIST)}')


# S05.1 — Arabic/English semantic + typographic QA.
# These checks validate deterministic invariants only; editorial quality remains a human inspection task.
for spec in specs:
    route=str(spec.get('route') or '/')
    if not spec.get('title_ar') or not spec.get('title_en'):
        errors.append(f'S05.1 bilingual title missing {route}')
    ar_orders={x.get('section_order') for x in (spec.get('sections') or []) if x.get('heading_ar') or x.get('body_ar')}
    en_orders={x.get('section_order') for x in (spec.get('sections') or []) if x.get('heading_en') or x.get('body_en')}
    if ar_orders!=en_orders:
        errors.append(f'S05.1 localized section-order parity mismatch {route}')
    for lang in ('ar','en'):
        f=DIST/lang/route.strip('/')/'index.html'
        if f.exists():
            raw=f.read_text(encoding='utf-8')
            if len(re.findall(r'<h1(?:\s|>)',raw))!=1:
                errors.append(f'S05.1 page must expose exactly one h1 {route} {lang}')

localized_public_fields={
    'governed_claims':['headline','copy','does_not_prove','verification'],
    'governed_evidence_objects':['title','summary','public_summary','what_it_establishes','meaning','period','universe','method','limitations','currentness','verification','does_not_establish','limitation'],
    'governed_visual_contracts':['title','question','what_it_shows','decision_value','prohibited_inference','accessible_summary'],
    'governed_readings':['title','question','thesis','observation','prohibited_inference','recommendation','unknown','measurement_next'],
    'governed_measurement_priorities':['title','current_evidence','missing_evidence','guardrail','unlocked_decision','feasibility','priority_basis','what_changes','recommended_visual'],
}
for spec in specs:
    route=str(spec.get('route') or '/')
    for group,bases in localized_public_fields.items():
        for obj in spec.get(group) or []:
            oid=obj.get('claim_id') or obj.get('evidence_object_id') or obj.get('object_id') or obj.get('visual_id') or obj.get('reading_id') or obj.get('measurement_id') or route
            for base in bases:
                has_en=bool(obj.get(base+'_en')); has_ar=bool(obj.get(base+'_ar'))
                if has_en!=has_ar:
                    errors.append(f'S05.1 one-sided localized public field {route} {oid} {base}')

# Representative numeric signatures prove that material numbers survive both public editions.
s05_numeric_signatures={
    '/':['11.9%','12.91','561','1,473'],
    '/people/':['11.9%','12.91'],
    '/firms/':['22%','50%','46%'],
    '/payments/':['561','1,473'],
    '/providers/':['98','225','106'],
    # Tranche C TC-A (EN-30): the limitation says "more than a quarter" without the redundant "(1/4)".
    '/evidence/CLM-001/':['11.9%','2022-11-07','2023-01-09','23%'],
    '/evidence/CLM-060/':['19%','15%','40%','2024','2021'],
    '/evidence/CLM-032/':['2020','2025'],
    # Tranche B PB-0362/PB-0363 (CWR-001): the restated 2024 value is published at source-appropriate precision (USD 3.42 billion), not six figures.
    # Pre-Tranche-C P4 (V-D1): the residual-model estimate rests only on material without a public locator; its value is withheld (S04.3).
    '/readings/same-year-different-number/':['6.245','3.42','0.0032','33%','1.838'],
}
for _lang in ('ar','en'):
    for _route in ('readings/same-year-different-number','evidence/CLM-044'):
        if re.search(r'(?<![\d.])7\.4(?!\d)',(DIST/_lang/_route/'index.html').read_text(encoding='utf-8')):
            errors.append(f'S04.3 withheld residual-model value printed on /{_route}/ {_lang}')
for route,tokens in s05_numeric_signatures.items():
    for lang in ('ar','en'):
        raw=(DIST/lang/route.strip('/')/'index.html').read_text(encoding='utf-8') if route!='/' else (DIST/lang/'index.html').read_text(encoding='utf-8')
        for token in tokens:
            if token not in raw:
                errors.append(f'S05.1 semantic numeric token missing {route} {lang} {token}')

# Arabic Reading pages must never expose English-only visual implementation metadata.
for spec in specs:
    if spec.get('page_class')!='reading_detail':
        continue
    raw=(DIST/'ar'/str(spec.get('route')).strip('/')/'index.html').read_text(encoding='utf-8')
    for visual in spec.get('governed_visual_contracts') or []:
        for base in ('period','source_period','unit_or_object'):
            ar_value=visual.get(base+'_ar')
            fallback=str(visual.get(base) or '').strip()
            if not ar_value and fallback and re.search(r'[A-Za-z]',fallback) and fallback in _html.unescape(raw):
                errors.append(f'S05.1 English-only visual metadata leaked on Arabic Reading {spec.get("route")} {visual.get("visual_id")} {base}')

# Measurement Agenda domain classification is localized in Arabic rather than exposing English UI labels.
try:
    _measurement= json.load(open(C/'content/measurement_agenda.json',encoding='utf-8'))
    ar_measurement=(DIST/'ar/measurement/index.html').read_text(encoding='utf-8')
    en_measurement=(DIST/'en/measurement/index.html').read_text(encoding='utf-8')
    for m in _measurement:
        raw_domain=str(m.get('domain') or '').strip()
        if raw_domain and (' · '+raw_domain+'</div>') in ar_measurement:
            errors.append(f'S05.1 untranslated Measurement domain on Arabic page {m.get("measurement_id")} {raw_domain}')
        if raw_domain and (' · '+raw_domain+'</div>') not in en_measurement:
            errors.append(f'S05.1 English Measurement domain missing {m.get("measurement_id")} {raw_domain}')
except Exception as e:
    errors.append('S05.1 measurement bilingual QA unreadable '+str(e))

# Mixed-script stable identifiers and language-switch route context are implementation invariants.
if '.stable-id,.source-id{direction:ltr;unicode-bidi:isolate' not in css:
    errors.append('S05.1 stable Latin identifier bidi isolation missing')
for token,label in [
    ("location.pathname.replace(/^\\/(ar|en)/",'language switch equivalent route preservation'),
    ('location.search+location.hash','language switch query/hash preservation'),
    ('measurement_domain_label(','Arabic Measurement domain localization'),
]:
    target=js if token.startswith('location.') else build_src
    if token not in target: errors.append('S05.1 missing '+label)



# S05.2 — constrained interaction, keyboard/reflow and assistive-structure invariants.
# Browser/screen-reader runtime acceptance remains a separate human/runtime proof; these checks protect deterministic structure.
class S052Parser(HTMLParser):
    def __init__(self):
        super().__init__(); self.headings=[]; self.mains=[]; self.details=0; self.summaries=0
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if re.fullmatch(r'h[1-6]',tag): self.headings.append(int(tag[1]))
        if tag=='main': self.mains.append(a.get('id'))
        if tag=='details': self.details+=1
        if tag=='summary': self.summaries+=1

for spec in specs:
    route=str(spec.get('route') or '/').strip('/')
    for lang in ('ar','en'):
        f=DIST/lang/route/'index.html'
        if not f.exists(): continue
        raw=f.read_text(encoding='utf-8'); hp=S052Parser(); hp.feed(raw)
        if hp.mains.count('main')!=1: errors.append(f'S05.2 exactly one main#main required {spec.get("route")} {lang}')
        if 'class="skip" href="#main"' not in raw: errors.append(f'S05.2 skip link missing {spec.get("route")} {lang}')
        if hp.details!=hp.summaries: errors.append(f'S05.2 details/summary structure mismatch {spec.get("route")} {lang}')
        for prev,nxt in zip(hp.headings,hp.headings[1:]):
            if nxt>prev+1: errors.append(f'S05.2 heading-level jump h{prev}->h{nxt} {spec.get("route")} {lang}')
        for token,label in [
            ('id="primary-nav"','primary navigation landmark'),
            ('aria-label="'+('التنقل الرئيسي' if lang=='ar' else 'Primary navigation')+'"','primary navigation accessible name'),
            ('aria-controls="primary-nav"','menu control relationship'),
            ('aria-expanded="false"','menu initial state'),
            ('id="utility-status"','utility status live region'),
            ('class="mobile-nav-utilities"','mobile fallback utilities'),
        ]:
            if token not in raw: errors.append(f'S05.2 missing {label} {spec.get("route")} {lang}')

# Header utilities hidden at small widths must remain reachable inside the opened mobile nav.
for token,label in [
    ('.nav.open .mobile-nav-utilities{display:grid','mobile citation/report utility visibility'),
    ('.mobile-nav-action{display:flex','mobile utility actionable target'),
    ('.table-wrap{overflow:auto;max-width:100%','contained comparison table scrolling'),
    ('.table-wrap[role="region"]:focus-visible','focus indication for scrollable comparison region'),
    ('.sr-only{','visually-hidden accessible text utility'),
]:
    if token not in css: errors.append('S05.2 missing '+label)

for token,label in [
    ("if(open){\n    const first=n.querySelector('a[href],button:not([disabled])');",'menu focus-forward on open'),
    ("if(e.key==='Escape'",'Escape menu close/return path'),
    ("dialog.addEventListener('close'",'search return-focus path'),
    ('announceUtility(copied)','copy-action assistive feedback'),
    ('target.focus({preventScroll:true})','Data/source focused query target'),
    ('data-correction-origin','correction origin behavior'),
    ('<caption class="sr-only">','comparison table caption'),
    ('<th scope="col">','comparison column headers'),
    ('<th scope="row">','comparison row headers'),
    ('class="table-wrap" tabindex="0" role="region" aria-label="${esc(labels.table)}"','named keyboard-scrollable comparison region'),
    ("const compareSelects=['#compare-a','#compare-b','#compare-c','#compare-d']",'2/3/4 record comparison control structure'),
]:
    if token not in js: errors.append('S05.2 missing '+label)

# Compare status is concise; the full result/table must not be a live region.
for lang in ('ar','en'):
    cmp=(DIST/lang/'evidence/compare/index.html').read_text(encoding='utf-8')
    if 'id="compare-status"' not in cmp or 'role="status"' not in cmp or 'aria-live="polite"' not in cmp:
        errors.append(f'S05.2 Compare concise live status missing {lang}')
    if re.search(r'id="compare-output"[^>]*aria-live=',cmp): errors.append(f'S05.2 Compare full output must not be aria-live {lang}')
    if 'data-lang="' not in cmp or 'aria-label="' not in cmp: errors.append(f'S05.2 language switch accessible target missing {lang}')

# Search dialog must be named, keyboard dismissible by native dialog semantics, and return focus through JS.
for lang in ('ar','en'):
    home=(DIST/lang/'index.html').read_text(encoding='utf-8')
    if '<dialog id="search-dialog"' not in home or 'aria-labelledby="search-dialog-title"' not in home:
        errors.append(f'S05.2 named search dialog missing {lang}')
    if 'data-search-close aria-label=' not in home: errors.append(f'S05.2 named search close control missing {lang}')
    if 'data-search-status role="status" aria-live="polite"' not in home: errors.append(f'S05.2 search live status missing {lang}')

# Critical first-load semantic boundaries remain before progressive disclosure on Domain and Evidence families.
for route in ['/people/','/access/','/firms/','/finance/','/payments/','/remittances/','/providers/','/reforms/']:
    for lang in ('ar','en'):
        raw=(DIST/lang/route.strip('/')/'index.html').read_text(encoding='utf-8')
        boundary_positions=[p for p in [raw.find('domain-scope'),raw.find('scope-item boundary')] if p>=0]
        progressive=raw.find('<details class="domain-more"')
        if progressive>=0 and boundary_positions and max(boundary_positions)>progressive:
            errors.append(f'S05.2 Domain safety boundary moved behind progressive disclosure {route} {lang}')
for lang in ('ar','en'):
    sample=DIST/lang/'evidence/CLM-001/index.html'
    if sample.exists():
        raw=sample.read_text(encoding='utf-8')
        b=raw.find('data-evidence-boundary-first-load'); d=raw.find('<details class="evidence-more"')
        if b<0: errors.append(f'S05.2 Evidence first-load boundary missing CLM-001 {lang}')
        elif d>=0 and b>d: errors.append(f'S05.2 Evidence boundary moved behind progressive detail CLM-001 {lang}')


# Historical S00-S06 session controls are audit lineage, not current production acceptance gates.

# S06 concurrency correction: the local MFI shard must preserve the current Master's Q4-2011 within-source conflict,
# not silently restore a clean 2011 year-end portfolio anchor.
try:
    mfi=json.load(open(C/'data/mfi_data.json',encoding='utf-8'))
    r2011=next((r for r in mfi.get('rows',[]) if r and r[0]=='SRC-SFD-Q4-2011-001'),None)
    if not r2011:
        errors.append('S06 current MFI shard missing SRC-SFD-Q4-2011-001')
    else:
        if r2011[1] is not None: errors.append('S06 MFI 2011 conflict row must not expose a settled observation date')
        if r2011[3:6] != [63568,87615,3853]: errors.append('S06 MFI 2011 table values drifted')
        if 'WITHIN_SOURCE_VALUE_CONFLICT' not in str(r2011[11]): errors.append('S06 MFI 2011 portfolio conflict state missing')
        if str(r2011[14])!='HOLD_TIME_SERIES__CONFLICT': errors.append('S06 MFI 2011 time-series hold missing')
        if '4,030' not in str(r2011[17]) or '3,853' not in str(r2011[17]): errors.append('S06 MFI 2011 dual-source-statement note missing')
except Exception as e:
    errors.append('S06 current MFI shard unreadable '+str(e))

# The 2011 conflict is not a current public Page-Spec claim; publication projection must not acquire the competing values by accident.
_ps_text=(C/'page_specs.json').read_text(encoding='utf-8')
for token in ['63,568','87,615','YER 3,853','64,000 active borrowers','YER 4,030m']:
    if token in _ps_text: errors.append('S06 internal 2011 MFI conflict leaked into Page Specs '+token)

# S05.3 — visual/table fallback + non-colour semantics.
# These are deterministic semantic/accessibility structure checks, not aesthetic scores.
visual_contract_ids=set()
for spec in specs:
    for v in spec.get('governed_visual_contracts') or []:
        vid=str(v.get('visual_id') or '')
        if not vid: continue
        visual_contract_ids.add(vid)
        for field in ('title_en','title_ar','question_en','question_ar','accessible_summary_en','accessible_summary_ar','prohibited_inference_en','prohibited_inference_ar'):
            if not str(v.get(field) or '').strip():
                errors.append(f'S05.3 governed visual missing {field} {vid}')

# Every actually rendered governed visual is self-describing when detached from colour/image context.
rendered_visual_instances=0
for spec in specs:
    route=str(spec.get('route') or '/').strip('/')
    governed={str(v.get('visual_id')):v for v in spec.get('governed_visual_contracts') or [] if v.get('visual_id')}
    for lang in ('ar','en'):
        f=DIST/lang/route/'index.html'
        if not f.exists(): continue
        raw=f.read_text(encoding='utf-8')
        ids=re.findall(r'data-visual-id="([^"]+)"',raw)
        rendered_visual_instances+=len(ids)
        for vid in ids:
            if vid not in governed:
                errors.append(f'S05.3 rendered visual is not governed on route {spec.get("route")} {lang} {vid}')
                continue
            v=governed[vid]
            if 'data-visual-fallback="ordered-text"' not in raw:
                errors.append(f'S05.3 visual fallback missing {spec.get("route")} {lang} {vid}')
            if 'data-image-independent="true"' not in raw:
                errors.append(f'S05.3 image-independence marker missing {spec.get("route")} {lang} {vid}')
            if 'data-noncolour-semantic="text-structure-label-position"' not in raw:
                errors.append(f'S05.3 non-colour semantic marker missing {spec.get("route")} {lang} {vid}')
            summary=str(v.get(f'accessible_summary_{lang}') or '')
            if summary and summary not in _html.unescape(raw):
                errors.append(f'S05.3 governed accessible summary missing from rendered fallback {spec.get("route")} {lang} {vid}')
            question=str(v.get(f'question_{lang}') or '')
            if question and question not in _html.unescape(raw):
                errors.append(f'S05.3 governed visual question missing from rendered fallback {spec.get("route")} {lang} {vid}')
            boundary=str(v.get(f'prohibited_inference_{lang}') or '')
            if boundary and boundary not in _html.unescape(raw):
                errors.append(f'S05.3 visual prohibited inference missing {spec.get("route")} {lang} {vid}')

if rendered_visual_instances < 20: # 17 material governed visuals x 2 languages = 34 in the accepted current composition.
    errors.append(f'S05.3 unexpectedly low rendered governed visual coverage {rendered_visual_instances}')

# Home must render the governed system visual through the same accessible fallback contract as other visuals.
for lang in ('ar','en'):
    home=(DIST/lang/'index.html').read_text(encoding='utf-8')
    if 'data-visual-id="VIS-INCLUSION-TRANSMISSION"' not in home:
        errors.append(f'S05.3 Home missing governed VIS-INCLUSION-TRANSMISSION {lang}')
    if 'data-visual-fallback="ordered-text"' not in home or 'data-image-independent="true"' not in home:
        errors.append(f'S05.3 Home governed visual lacks ordered image-independent fallback {lang}')

# Compare is the only public tabular component: its semantics must survive colour loss and narrow layout.
for token,label in [
    ('data-noncolour-semantic="text-label-structure"','explicit non-colour comparison verdict'),
    ('data-noncolour-semantic="caption-headers-text-labels"','explicit non-colour comparison table'),
    ('<caption class="sr-only">','comparison table caption'),
    ('<th scope="col">','comparison column scope'),
    ('<th scope="row">','comparison row scope'),
    ('<span class="compare-state">${esc(r.label)}</span>','text comparison-state label'),
]:
    if token not in js: errors.append('S05.3 missing '+label)

for token,label in [
    ('@media(forced-colors:active)','forced-colours structural fallback'),
    ('.visual-fallback{','visible visual text fallback'),
    ('.visual-context{','structured visual context'),
    ('.compare-state{','text/border comparison state'),
]:
    if token not in css: errors.append('S05.3 missing '+label)

# Public Arabic must not regress to backend denominator terminology during projection reconciliation.
for f in DIST.rglob('*.html'):
    raw=f.read_text(encoding='utf-8')
    for term in ('بمقام محدد','لها مقامات شرطية صغيرة','مقام غير معروف'):
        if term in raw: errors.append(f'S05.3 stale backend Arabic term {term} in {f}')

# R4 — sitemap, route-value and end-to-end journey acceptance.
try:
    nav_contract=json.load(open(C/'content/navigation_interaction.json',encoding='utf-8'))
except Exception as e:
    nav_contract={}
    errors.append('R4 navigation interaction contract unreadable '+str(e))

if nav_contract:
    if nav_contract.get('authority_scope')!='NAVIGATION_AND_INTERACTION_ONLY':
        errors.append('R4 navigation interaction authority scope invalid')
    bind=nav_contract.get('authority_binding') or {}
    if bind.get('master_sha256')!=master_sha:
        errors.append('R4 navigation contract Master hash stale')
    if bind.get('page_specs_sha256')!=actual_page_specs_sha:
        errors.append('R4 navigation contract Page Specs hash stale')
    if bind.get('page_spec_count')!=len(specs):
        errors.append('R4 navigation contract Page Spec count mismatch')
    nav_routes=[str(x.get('route')) for x in nav_contract.get('routes',[]) if x.get('route')]
    controlled_routes=[str(x.get('route')) for x in specs]
    if len(nav_routes)!=len(set(nav_routes)):
        errors.append('R4 navigation route matrix contains duplicates')
    if set(nav_routes)!=set(controlled_routes):
        errors.append('R4 navigation route matrix does not cover exactly the controlled route set')
    family_counts={}
    for x in nav_contract.get('routes',[]):
        fam=str(x.get('page_family') or '')
        family_counts[fam]=family_counts.get(fam,0)+1
        if x.get('deletion_disposition')!='KEEP':
            errors.append('R4 route lacks KEEP deletion disposition '+str(x.get('route')))
        if not x.get('unique_value_role') or not x.get('next_action_policy'):
            errors.append('R4 route lacks unique value/next-action role '+str(x.get('route')))
        if not x.get('depth_role') or not x.get('navigation_prominence'):
            errors.append('R4 route lacks depth/prominence decision '+str(x.get('route')))
        if fam=='Evidence Record' and x.get('navigation_prominence')!='ADDRESSABLE_VERIFICATION':
            errors.append('R4 Evidence Record must remain addressable verification, not global navigation '+str(x.get('route')))
    expected_families={
        'Orientation':1,'Question Entry':1,'Domain Answer':8,'Evidence Directory':1,
        'Evidence Record':len(json.load(open(C/'evidence/evidence_objects.json',encoding='utf-8'))),'Comparison':1,'Reading Index':1,
        'Reading':len(json.load(open(C/'content/readings.json',encoding='utf-8'))),
        'Data & Source':1,'Measurement':1,'Reference / Trust':8
    }
    if family_counts!=expected_families:
        errors.append('R4 page-family matrix count mismatch '+str(family_counts))
    # Tranche B PB-0420…PB-0424: five primary items; Method & Measurement is a family of two routed destinations;
    # About leads the Trust navigation (secondary, always visible) — no route is added or removed.
    gnav=nav_contract.get('global_navigation',[])
    global_routes=set()
    for x in gnav:
        if x.get('route'): global_routes.add(str(x['route']))
        kids=x.get('children') or []
        if not x.get('route') and len([k for k in kids if k.get('route')])<2: errors.append('PB-0424 grouping node without two routed children '+str(x.get('label_en')))
        for k in kids:
            if not k.get('route'): errors.append('PB-0424 navigation child without route '+str(k))
            else: global_routes.add(str(k['route']))
    if global_routes!={'/explore/','/evidence/','/readings/','/data/','/methodology/','/measurement/'}:
        errors.append('R4 global navigation spine mismatch '+str(sorted(global_routes)))
    mm=[x for x in gnav if {'/methodology/','/measurement/'}<= {str(k.get('route')) for k in (x.get('children') or [])}]
    if len(mm)!=1: errors.append('PB-0422 Method & Measurement family must hold both destinations')
    trust_routes=[str(x.get('route')) for x in nav_contract.get('trust_navigation',[])]
    if trust_routes[:1]!=['/about/'] or set(trust_routes)!={'/about/','/corrections/','/rights/','/accessibility/','/privacy/','/terms/','/contact/'}:
        errors.append('PB-0423 trust navigation must lead with About and hold the six trust routes '+str(trust_routes))
    if len(nav_contract.get('journeys') or [])<13:
        errors.append('R4 journey matrix incomplete after payment-rail/humanitarian challenge')

# Header/footer navigation is contract-driven; legal/trust routes must not be hidden search-only pages.
if "NAVIGATION_INTERACTION=load(C/'content/navigation_interaction.json')" not in build_src:
    errors.append('R4 renderer is not consuming navigation interaction contract')
for lang in ('ar','en'):
    home=(DIST/lang/'index.html').read_text(encoding='utf-8')
    for route in ('privacy','rights','terms','accessibility','corrections','contact'):
        if f'href="/{lang}/{route}/"' not in home:
            errors.append(f'R4 footer discovery missing /{route}/ {lang}')
    if home.count('footer-nav-group')!=3:
        errors.append(f'R4 footer grouping mismatch {lang}')

# Deep-link detail routes require first-screen backtracking and Reading-to-Evidence verification.
detail_route_by_id={}
for o in specs:
    if o.get('page_class')!='evidence_detail': continue
    for x in (o.get('governed_claims') or [])+(o.get('governed_evidence_objects') or [])+(o.get('governed_visual_contracts') or []):
        oid=x.get('claim_id') or x.get('evidence_object_id') or x.get('object_id') or x.get('visual_id')
        if oid: detail_route_by_id[str(oid)]=str(o.get('route'))
for o in specs:
    route=str(o.get('route') or '/').strip('/')
    for lang in ('ar','en'):
        f=DIST/lang/route/'index.html'
        if not f.exists(): continue
        raw=f.read_text(encoding='utf-8')
        if o.get('page_class') in {'evidence_detail','reading_detail'} and 'class="breadcrumb"' not in raw:
            errors.append(f'R4 deep-detail breadcrumb missing {o.get("route")} {lang}')
        if o.get('page_class')=='reading_detail':
            if 'data-reading-verify' not in raw:
                errors.append(f'R4 Reading verification bridge missing {o.get("route")} {lang}')
            r=(o.get('governed_readings') or [{}])[0]
            ids=list((r.get('verification_bindings') or {}).get('claim_ids') or r.get('claim_bindings') or [])
            for oid in ids:
                target=detail_route_by_id.get(str(oid))
                if not target:
                    errors.append(f'R4 Reading claim has no Evidence Record route {o.get("route")} {oid}')
                    continue
                expected=f'href="/{lang}/{target.strip("/")}/"'
                if expected not in raw:
                    errors.append(f'R4 Reading missing direct bound Evidence Record link {o.get("route")} {lang} {oid}')

# Every route must be intentionally discoverable: static inbound link or public-search entry.
# Search/deep-link-only Evidence Records are allowed; trust/reference pages are not.
controlled_set=set(str(o.get('route')) for o in specs)
static_inbound={r:set() for r in controlled_set}
for o in specs:
    source=str(o.get('route'))
    f=DIST/'en'/source.strip('/')/'index.html'
    if not f.exists(): continue
    parser=P(); parser.feed(f.read_text(encoding='utf-8'))
    for href in parser.links:
        if not href.startswith('/en/'): continue
        path=urlparse(href).path
        path='/' + path[len('/en/'):].strip('/') + '/'
        if path=='//': path='/'
        if path in controlled_set and path!=source:
            static_inbound[path].add(source)
search_route_set=set()
for rec in search_records:
    route=str(rec.get('route') or rec.get('primary_route') or rec.get('public_route') or '/')
    path=urlparse(route).path
    if not path.endswith('/'): path+='/'
    search_route_set.add(path)
for r in controlled_set:
    if r=='/': continue
    if not static_inbound.get(r) and r not in search_route_set:
        errors.append('R4 undiscoverable controlled route '+r)
for trust in ('/privacy/','/rights/','/terms/'):
    if not static_inbound.get(trust):
        errors.append('R4 trust route remains search-only '+trust)

# Search smoke tests reproduce the browser's current scoring logic closely enough to catch journey regressions.
def _r4norm(value):
    value=str(value or '').casefold()
    value=''.join(str(ord(c)-0x0660) if '\u0660'<=c<='\u0669' else str(ord(c)-0x06F0) if '\u06F0'<=c<='\u06F9' else c for c in value)   # Tranche C TOOL-12
    value=re.sub(r'[\u064B-\u065F\u0670]','',value)
    value=value.replace('إ','ا').replace('أ','ا').replace('آ','ا').replace('ٱ','ا').replace('ى','ي').replace('ة','ه').replace('ؤ','و').replace('ئ','ي')
    return value
def _r4qtok(t):
    # PB-0491 light query-token normalisation, identical to site-src/app.js queryToken().
    if t.startswith('ال') and len(t)>3: return t[2:]
    if re.fullmatch(r'[a-z]+',t) and len(t)>4:
        if t.endswith('ies'): return t[:-3]+'y'
        if t.endswith('ing'): return t[:-3]
        if t.endswith('ed'): return t[:-2]
        if t.endswith('s') and not t.endswith('ss'): return t[:-1]
    return t
_R4_DOMAIN={'/people/','/firms/','/finance/','/providers/','/payments/','/remittances/','/access/','/reforms/','/measurement/'}
try:
    _R4_ALIASES=json.load(open(C/'content/search_aliases.json',encoding='utf-8'))
except Exception as e:
    _R4_ALIASES=[]; errors.append('PB-0492 search aliases projection unreadable '+str(e))
def _r4alias(term,lang):
    q=' '.join(_r4qtok(t) for t in term.split() if t)
    for a in _R4_ALIASES:
        own=a.get('terms_ar' if lang=='ar' else 'terms_en') or ''; other=a.get('terms_en' if lang=='ar' else 'terms_ar') or ''
        terms=[' '.join(_r4qtok(t) for t in _r4norm(x.strip()).split() if t) for x in (own.split(';')+other.split(';'))]
        if q in [t for t in terms if t]: return a
    return None
_R4_STOP={'what','do','does','we','is','are','the','and','of','in','about','how','which','who','a','an','to','for','on','there','ما','ماذا','هل','في','من','على','عن','و','التي','الذي','هو','هي','كم','كيف'}
_R4_PUNCT=re.compile(r'[?,.;:!—–"“”«»()؟،؛\'’]')
def _r4search(query,lang,limit=10):
    # Tranche C (JRN-05/TOOL-10): identical to site-src/app.js queryTokens() and result de-duplication by destination.
    term=_r4norm(query.strip())
    tokens=[_r4qtok(x) for x in re.split(r'\s+',_R4_PUNCT.sub(' ',term)) if len(x)>1 and x not in _R4_STOP]
    alias=_r4alias(_R4_PUNCT.sub(' ',term).strip(),lang)
    ranked=[]
    for x in search_records:
        title=_r4norm(x.get('title_ar' if lang=='ar' else 'title_en') or '')
        summary=_r4norm(x.get('summary_ar' if lang=='ar' else 'summary_en') or '')
        textv=_r4norm(x.get('search_text_ar' if lang=='ar' else 'search_text_en') or '')
        boundary=_r4norm(x.get('boundary_text_ar' if lang=='ar' else 'boundary_text_en') or '')
        stable=_r4norm(' '.join(str(x.get(k) or '') for k in ('id','source_id','object_id','claim_id','reading_id')))
        score=0
        for tok in tokens:
            if stable==tok: score+=12
            elif re.search(r'[-\d]',tok) and tok in stable: score+=7
            if tok in title: score+=6
            if tok in summary: score+=3
            if tok in textv: score+=1
            if tok in boundary: score+=0.5
        xr=str(x.get('route') or '')
        if score>0 and x.get('type')=='page' and xr in _R4_DOMAIN and tokens and all(t in title for t in tokens): score+=20
        if alias:
            for tg in [v.strip() for v in str(alias.get('targets') or '').split('|')]:
                if tg.startswith('route:') and x.get('type')=='page' and xr==tg[6:]: score+=25
                if tg.startswith('document_type:') and x.get('document_type')==tg[14:]: score+=10
        if score>0:
            route=str(x.get('route') or x.get('primary_route') or x.get('public_route') or '/')
            route=urlparse(route).path
            if not route.endswith('/'): route+='/'
            ranked.append((score,route,title,x))
    ranked.sort(key=lambda z:z[0],reverse=True)
    unique=[]; seen=set()
    for score,route,title,x in ranked:
        key=route
        if key in seen: continue
        seen.add(key); unique.append(route)
        if len(unique)>=limit: break
    return unique
for smoke in nav_contract.get('search_smoke_tests',[]) if nav_contract else []:
    for lang,qkey in (('en','query_en'),('ar','query_ar')):
        q=smoke.get(qkey)
        expected=list(smoke.get('expected_routes') or [])
        if not q: continue
        got=_r4search(q,lang)
        if smoke.get('rule')=='PRIMARY_EXPECTED_ROUTE_IN_TOP_3':
            if expected and expected[0] not in got[:3]:
                errors.append(f'PB-0494 search smoke failed (primary route not in top 3) {lang} {q!r}: {got[:5]}')
        elif expected and not set(expected).intersection(got):
            errors.append(f'R4 search smoke failed {lang} {q!r}: {got[:10]}')

# P2.2 canonical search probe (scripts/search_canonical_probe.json): explicit expected destinations with rationale.
try:
    _probe=json.load(open(ROOT/'scripts/search_canonical_probe.json',encoding='utf-8'))
    for it in _probe['intents']:
        for lang,qk in (('en','query_en'),('ar','query_ar')):
            got=_r4search(it[qk],lang)
            ranks=[got.index(e)+1 for e in it['expected'] if e in got]
            best=min(ranks) if ranks else None
            if best is None:
                errors.append(f'P2-G01 search probe FAIL {lang} {it[qk]!r}: none of {it["expected"]} in the top 10 {got[:5]}')
            elif best>3 and not it.get('weak_allowed_reason'):
                errors.append(f'P2-G01 search probe WEAK {lang} {it[qk]!r}: best expected rank {best}; top 3 {got[:3]}')
except Exception as e:
    errors.append('P2-G01 search canonical probe unreadable '+str(e))

# Family-specific meaningful-next-action floor.
for o in specs:
    route=str(o.get('route') or '/').strip('/')
    for lang in ('ar','en'):
        f=DIST/lang/route/'index.html'
        if not f.exists(): continue
        raw=f.read_text(encoding='utf-8')
        cls=o.get('page_class')
        r='/' + route + '/' if route else '/'
        if cls=='evidence_detail' and ('evidence-related-section' not in raw or 'evidence-utility' not in raw):
            errors.append(f'R4 Evidence Record lacks verify/exit actions {o.get("route")} {lang}')
        elif cls=='reading_detail' and 'data-reading-verify' not in raw:
            errors.append(f'R4 Reading lacks verification next action {o.get("route")} {lang}')
        elif r in {'/people/','/access/','/firms/','/finance/','/payments/','/remittances/','/providers/','/reforms/'} and 'class="domain-verify"' not in raw:
            errors.append(f'R4 domain lacks verification next action {r} {lang}')
        elif r in (nav_contract.get('route_next_actions') or {}) and 'class="journey-next"' not in raw:
            errors.append(f'R4 configured route next actions not rendered {r} {lang}')

# ---------------------------------------------------------------------------------------------------------------------
# Pre-Tranche-C P1 gates: template tokens (P1-G01), inventory contract (P1-G02/G03/G04), public-ID policy (P1-G05),
# avoidable repetition on flagship pages (P1-G06).
# ---------------------------------------------------------------------------------------------------------------------
UNRESOLVED_TOKEN=re.compile(r'\{\{[^{}]*\}\}|\{[A-Z][A-Z0-9_]{1,40}\}')
def _p1_main_text(raw,drop_text_alternatives=False,drop_link_lists=False):
    m=re.search(r'<main.*?</main>',raw,flags=re.S)
    t=m.group(0) if m else raw
    t=re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S)
    if drop_link_lists:   # Tranche C: navigation lists repeat record titles and source names by design (records, related questions, chronology sources)
        t=re.sub(r'<details class="all-records">.*?</details>|<section class="related-questions">.*?</section>|<p class="chronology-sources">.*?</p>','',t,flags=re.S)
    if drop_text_alternatives:   # a chart's analytical text alternative is its non-visual equivalent (a different job); P3 governs its presentation
        t=re.sub(r'<div class="visual-fallback".*?</ol></div>','',t,flags=re.S)
    t=re.sub(r'</(p|h[1-6]|li|div|section|summary|dt|dd|tr|article|figcaption)>','\n',t)
    return _html.unescape(re.sub(r'<[^>]+>',' ',t))
# P1-G01: no unresolved template token reaches public HTML (text or attributes), public static data or a Page Spec.
for f in DIST.rglob('*.html'):
    raw=re.sub(r'<script.*?</script>','',f.read_text(encoding='utf-8'),flags=re.S)
    m=UNRESOLVED_TOKEN.search(_html.unescape(raw))
    if m: errors.append(f'P1-G01 unresolved template token {m.group(0)!r} in {f.relative_to(DIST)}')
def _p1_walk(x,where):
    if isinstance(x,str):
        m=UNRESOLVED_TOKEN.search(x)
        if m: errors.append(f'P1-G01 unresolved template token {m.group(0)!r} in {where}')
    elif isinstance(x,dict):
        for v in x.values(): _p1_walk(v,where)
    elif isinstance(x,list):
        for v in x: _p1_walk(v,where)
for f in (DIST/'static-data').glob('*.json'):
    _p1_walk(json.load(open(f,encoding='utf-8')),'static-data/'+f.name)
for o in specs:
    _p1_walk({k:o.get(k) for k in ('title_en','title_ar','meta_description_en','meta_description_ar','full_copy_en','full_copy_ar','sections')},'page spec '+str(o.get('route')))
# P1-G02: the derived inventory contract equals an independent recount of the projections.
INV={}
try:
    _inv=json.load(open(C/'content/public_inventory.json',encoding='utf-8'))
    INV={c['key']:c['value'] for c in _inv['counts']}
    def _n(p): return len(json.load(open(C/p,encoding='utf-8')))
    _srm=json.load(open(C/'sources/source_reference_map.json',encoding='utf-8'))
    _expect={'evidence_records':_n('evidence/evidence_objects.json'),'public_claims':_n('evidence/public_claims.json'),
             'chronology_events':_n('visuals/system_chronology.json'),'sources':_n('sources/source_library.json'),
             'public_locators':sum(1 for s in _srm if str(s.get('primary_url') or '').strip().lower().startswith(('http://','https://'))),
             'curated_resources':sum(1 for s in _srm if s.get('standalone_resource_card_eligible') is True),
             'readings':_n('content/readings.json'),'measurement_priorities':_n('content/measurement_agenda.json'),
             'entry_questions':_n('content/questions.json'),'visual_contracts':_n('visuals/visual_library.json'),
             'evidence_passports':_n('evidence/evidence_passports.json'),'search_records':_n('content/search_index.json'),'page_specs':len(specs)}
    for k,v in _expect.items():
        if INV.get(k)!=v: errors.append(f'P1-G02 public inventory {k}={INV.get(k)} but the projection holds {v}')
    if set(INV)!=set(_expect): errors.append(f'P1-G02 public inventory keys differ from the recount: {sorted(set(INV)^set(_expect))}')
    if _inv.get('authority_master_sha256')!=master_sha: errors.append('P1-G02 public inventory Master hash is stale')
except Exception as e:
    errors.append('P1-G02 public inventory contract unreadable '+str(e))
# P1-G03: every resolved inventory token equals the contract, and the /data/ inventory list shows exactly those values.
for o in specs:
    for s in o.get('sections') or []:
        for t in s.get('resolved_inventory_tokens') or []:
            if INV.get(t.get('key'))!=t.get('value'):
                errors.append(f'P1-G03 resolved inventory token differs from the contract {o.get("route")} {t}')
            if format(int(t.get('value') or 0),',') not in str(s.get(t.get('field')) or ''):
                errors.append(f'P1-G03 resolved inventory value not in section text {o.get("route")} {t}')
_data_spec=next((o for o in specs if o.get('route')=='/data/'),{})
for lang in ('en','ar'):
    want=[t['value'] for s in _data_spec.get('sections') or [] for t in s.get('resolved_inventory_tokens') or [] if t.get('field')==f'body_{lang}']
    f=DIST/lang/'data'/'index.html'
    raw=f.read_text(encoding='utf-8') if f.exists() else ''
    dl=re.search(r'<dl class="inventory-list"[^>]*>(.*?)</dl>',raw,flags=re.S)
    got=[int(x.replace(',','')) for x in re.findall(r'<dd[^>]*>([\d,]+)</dd>',dl.group(1))] if dl else []
    if not want or got!=want:
        errors.append(f'P1-G03 /data/ inventory list {lang} shows {got}, contract tokens give {want}')
# P1-G04: any repository-inventory count phrase in public text must carry the contract value, in digits.
_EN_WORDS='one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty'
_EN_INV=re.compile(r'(?<![\w.,/-])(?!0\d)(\d{1,3}(?:,\d{3})*|'+_EN_WORDS+r')[ \t\u00a0]+(?:(?:public|full|registered|curated|governed|analytical|documented|evidence|entry|source|decision-valued)[ \t\u00a0]+){0,3}'
                   r'(evidence records|source records|readings|chronology events|documented events|public claims|evidence-backed public claims|measurement priorities|measurement items|questions|visual specifications|visual contracts|evidence passports|search records)\b',re.I)
_EN_KEY={'evidence records':'evidence_records','source records':'sources','readings':'readings','chronology events':'chronology_events','documented events':'chronology_events',
         'public claims':'public_claims','evidence-backed public claims':'public_claims','measurement priorities':'measurement_priorities','measurement items':'measurement_priorities',
         'questions':'entry_questions','visual specifications':'visual_contracts','visual contracts':'visual_contracts','evidence passports':'evidence_passports','search records':'search_records'}
_AR_WORDS='عشر|عشرة|أحد عشر|إحدى عشرة|اثنا عشر|اثنتا عشرة|ثلاث|ثلاثة|أربع|أربعة|خمس|خمسة|ست|ستة|سبع|سبعة|ثماني|ثمانية|تسع|تسعة'
_AR_INV=re.compile(r'(?<![\w.,/-])(?!0\d)(\d{1,3}(?:,\d{3})*|'+_AR_WORDS+r')[ \t\u00a0]+(سجلات?\s+(?:تفصيلية\s+عامة\s+)?للأدلة|سجلًا\s+للمصادر|سجلات?\s+(?:ال)?مصادر|سجلًا\s+للأدلة|قراءات|قراءة|حدثًا|أحداث|خلاصة|خلاصات|سؤالًا|أسئلة|أولويات|أولوية)')
_AR_DEF=re.compile(r'(القراءات|الأسئلة|الأولويات|الأحداث|السجلات|الخلاصات)[ \t\u00a0]+(العشر|العشرة|الأحد عشر|الإحدى عشرة|الاثنا عشر|الـ\d+)')
def _ar_key(noun):
    if 'للأدلة' in noun: return 'evidence_records'
    if 'مصادر' in noun: return 'sources'
    for k,v in (('قراء','readings'),('حدث','chronology_events'),('أحداث','chronology_events'),('خلاص','public_claims'),('سؤال','entry_questions'),('أسئلة','entry_questions'),('أولوي','measurement_priorities')):
        if k in noun: return v
    return None
for o in specs:
    if o.get('page_class') in ('evidence_detail','reading_detail'): continue   # record and Reading pages state their own figures, not repository inventory
    route=str(o.get('route') or '/').strip('/')
    for lang in ('en','ar'):
        f=DIST/lang/route/'index.html'
        if not f.exists(): continue
        text=_p1_main_text(f.read_text(encoding='utf-8'))
        if lang=='en':
            for m in _EN_INV.finditer(text):
                num=m.group(1); key=_EN_KEY.get(m.group(2).lower())
                tail=text[m.end():m.end()+40].lower()
                if key=='sources' and tail.startswith(' with a public original locator'): key='public_locators'
                if not num[0].isdigit() or int(num.replace(',',''))!=INV.get(key):
                    errors.append(f'P1-G04 inventory count phrase not from the contract {o.get("route")} en: {m.group(0)!r} (contract {key}={INV.get(key)})')
        else:
            for m in _AR_INV.finditer(text):
                num=m.group(1); key=_ar_key(m.group(2))
                if not num[0].isdigit() or int(num.replace(',',''))!=INV.get(key):
                    errors.append(f'P1-G04 inventory count phrase not from the contract {o.get("route")} ar: {m.group(0)!r} (contract {key}={INV.get(key)})')
            for m in _AR_DEF.finditer(text):
                errors.append(f'P1-G04 inventory count phrase not from the contract {o.get("route")} ar: {m.group(0)!r}')
# P1-G05: public-ID policy (PID-1) — descriptive labels drive links; references are shown only where they aid
# verification or citation, always labelled; no public surface calls a displayed identifier "internal".
_ID_ALLOWED_ROUTES={'/data/'}                                    # source directory: a locator-only source has no other name
for o in specs:
    route_s=str(o.get('route') or '/'); route=route_s.strip('/')
    for lang in ('en','ar'):
        f=DIST/lang/route/'index.html'
        if not f.exists(): continue
        raw=f.read_text(encoding='utf-8')
        main=(re.search(r'<main.*?</main>',raw,flags=re.S) or re.search(r'.*',raw,flags=re.S)).group(0)
        vis=_html.unescape(re.sub(r'<[^>]+>',' ',main))
        if re.search(r'internal (?:ids?|identifiers?)\b',vis,flags=re.I) or re.search(r'المعر[ّ]?فات الداخلية',vis):
            errors.append(f'P1-G05 public copy calls identifiers internal {route_s} {lang}')
        if o.get('page_class') in ('static','operational') and route_s not in _ID_ALLOWED_ROUTES and 'stable-id' in main:
            errors.append(f'P1-G05 decorative stable-ID badge on {route_s} {lang}')
        if re.search(r'<small>\s*(?:CLM|VIS|DS|MA|XW)-',main):
            errors.append(f'P1-G05 identifier used as a link label on {route_s} {lang}')
        for m in re.finditer(r'<span class="record-ref" data-public-ref>(.*?)</span></span>|<span class="record-ref" data-public-ref>(.*?)</bdi></span>',main):
            if 'record-ref-label' not in m.group(0):
                errors.append(f'P1-G05 unlabelled record reference on {route_s} {lang}')
# P1-G06: flagship pages carry no avoidable repetition — no sentence of eight or more words renders twice on the page.
_P1_FLAGSHIP={'/','/explore/','/people/','/finance/','/firms/','/payments/','/remittances/','/providers/','/access/','/reforms/',
              '/methodology/','/measurement/','/about/'}
_SENT=re.compile(r'(?<=[.!?؟])\s+')
for o in specs:
    route_s=str(o.get('route') or '/')
    if route_s not in _P1_FLAGSHIP: continue
    for lang in ('en','ar'):
        f=DIST/lang/route_s.strip('/')/'index.html'
        if not f.exists(): continue
        seen={}
        for line in _p1_main_text(f.read_text(encoding='utf-8'),drop_text_alternatives=True,drop_link_lists=True).split('\n'):
            for sent in _SENT.split(line.strip()):
                norm=re.sub(r'\W+',' ',sent).strip().lower()
                if len(norm.split())<8: continue
                seen[norm]=seen.get(norm,0)+1
        for sent,n in seen.items():
            if n>1: errors.append(f'P1-G06 repeated sentence ×{n} on {route_s} {lang}: {sent[:90]!r}')

# ---------------------------------------------------------------------------------------------------------------------
# Pre-Tranche-C P2 gates: tool contracts (P2-G02) and accessibility baseline (P2-G03). Behaviour is exercised in a
# browser by scripts/tests/test_public_tools.py; these static checks keep the contracts visible without a browser.
# ---------------------------------------------------------------------------------------------------------------------
_measure_ids=[m['measurement_id'] for m in json.load(open(C/'content/measurement_agenda.json',encoding='utf-8'))]
for lang in ('en','ar'):
    mh=(DIST/lang/'measurement'/'index.html').read_text(encoding='utf-8')
    for mid in _measure_ids:
        if f'id="{mid}"' not in mh: errors.append(f'P2-G02 Measurement priority anchor missing {lang} #{mid}')
for rec in search_records:
    if rec.get('type')=='measurement' and '#' not in str(rec.get('route')):
        errors.append(f'P2-G02 Measurement search record does not deep-link to its anchor {rec.get("id")}')
_js=(DIST/'assets'/'app.js').read_text(encoding='utf-8')
for token,label in (("get('records')",'Compare URL state parsing'),('history.replaceState','Compare URL state writing'),('data-compare-url-error','Compare technical input error'),
                    ('__RECORD_IDS__','record-context validation'),('sourceLinkError','source deep-link technical error')):
    if token not in _js: errors.append('P2-G02 missing runtime contract: '+label)
for lang in ('en','ar'):
    cmp=(DIST/lang/'evidence/compare/index.html').read_text(encoding='utf-8')
    if 'data-compare-copy' not in cmp: errors.append(f'P2-G02 Compare share control missing {lang}')
    for r in ('contact','corrections'):
        h=(DIST/lang/r/'index.html').read_text(encoding='utf-8')
        if 'data-correction-origin' not in h or '__RECORD_IDS__' not in h: errors.append(f'P2-G02 record context missing on /{r}/ {lang}')
    if 'data-correction-mail' not in (DIST/lang/'contact'/'index.html').read_text(encoding='utf-8'): errors.append(f'P2-G02 report action missing on /contact/ {lang}')
    dh=(DIST/lang/'data/index.html').read_text(encoding='utf-8')
    if dh.count('class="source-rights-note"')!=1: errors.append(f'P2-G02 /data/ must state the reuse boundary once, got {dh.count(chr(34)+"source-rights-note"+chr(34))} {lang}')
    if dh.count('class="source-rights-state"')<len([s for s in _srm if str(s.get("primary_url") or "").startswith("http")])-1:
        errors.append(f'P2-G02 /data/ source cards lack their reuse-terms state {lang}')
for f in DIST.rglob('*.html'):
    raw=f.read_text(encoding='utf-8'); rel=str(f.relative_to(DIST))
    if re.search(r'''<a\b(?:[^>"']|"[^"]*"|'[^']*')*\sdownload(?=[\s=>/])''',raw): errors.append(f'P2-G02 download offered while reuse terms are not assessed: {rel}')
    for m in re.finditer(r'<div class="eyebrow">([^<]+)</div>\s*<h[1-3][^>]*>([^<]+)</h[1-3]>',raw):
        if m.group(1).strip()==m.group(2).strip(): errors.append(f'P2-G03 label repeated as eyebrow and heading (read twice) {rel}: {m.group(1)[:40]}')
    if '/en/' in '/'+rel and re.search(r'placeholder="[^"]*[\u0600-\u06FF]',raw): errors.append(f'P2-G03 Arabic placeholder on an English page {rel}')
    for cp in re.findall(r'data-source-citation="([^"]*)"',raw):
        parts=cp.split(' · ')
        if len(parts)!=len(set(parts)): errors.append(f'P2-G02 citation repeats a part as if it were a title {rel}: {cp[:80]}')
    for t in re.findall(r'<table\b.*?</table>',raw,flags=re.S):
        if '<caption' not in t: errors.append(f'P2-G03 table without caption {rel}')
        if re.search(r'<th(?![^>]*\bscope=)',t): errors.append(f'P2-G03 table header cell without scope {rel}')
    for d in re.findall(r'<dialog\b[^>]*>',raw):
        if 'aria-labelledby' not in d and 'aria-label' not in d: errors.append(f'P2-G03 dialog without accessible name {rel}')
    if re.search(r'tabindex="[1-9]',raw): errors.append(f'P2-G03 positive tabindex {rel}')
    for img in re.findall(r'<img\b[^>]*>',raw):
        if 'alt=' not in img: errors.append(f'P2-G03 image without alt {rel}')
    for ctl in re.findall(r'<(?:input|select)\b[^>]*>',raw):
        cid=re.search(r'\bid="([^"]+)"',ctl)
        named='aria-label=' in ctl or 'aria-labelledby=' in ctl or (cid and f'for="{cid.group(1)}"' in raw)
        if not named:
            # a control wrapped in its <label> is named by it
            pos=raw.find(ctl); before=raw[max(0,pos-400):pos]
            if before.rfind('<label')<=before.rfind('</label>'): errors.append(f'P2-G03 form control without accessible name {rel}: {ctl[:60]}')
    for b in re.findall(r'<button\b[^>]*>\s*[^<\w\s]{1,2}\s*</button>',raw):
        if 'aria-label' not in b: errors.append(f'P2-G03 icon-only button without accessible name {rel}')
    # The root file is a language redirect with no content; 404 has no repeated navigation before <main>, so there is
    # nothing for a bypass link to bypass, but it must still expose its main landmark.
    if rel=='404.html':
        if 'id="main"' not in raw: errors.append('P2-G03 main landmark missing 404.html')
    elif rel!='index.html' and ('class="skip"' not in raw or 'id="main"' not in raw): errors.append(f'P2-G03 skip link or main target missing {rel}')

# ---------------------------------------------------------------------------------------------------------------------
# Pre-Tranche-C P3 gates: visual design readiness. The derived visual design contracts must tier every governed visual
# and give every SIGNATURE / CORE_ANALYTICAL visual a complete data contract (P3-G01); the static baseline draws no chart
# or decorative graphic (P3-G02); Arabic text alternatives carry the same scope line as English (P3-G03); no arrow glyph
# (U+2192) sits between numbers in Arabic text, where it renders against the reading order (P3-G04).
# ---------------------------------------------------------------------------------------------------------------------
_vdc=json.load(open(C/'visuals/visual_design_contracts.json',encoding='utf-8'))
_vlib=[v['visual_id'] for v in json.load(open(C/'visuals/visual_library.json',encoding='utf-8'))]
if sorted(x['visual_id'] for x in _vdc['visuals'])!=sorted(_vlib) or sum(_vdc['tier_counts'].values())!=len(_vlib):
    errors.append('P3-G01 visual design contracts do not tier exactly the governed visuals')
for _u,_l in _vdc['grammar_labels'].items():
    if not (_l.get('en') and _l.get('ar')): errors.append(f'P3-G01 grammar label without both languages: {_u}')
for _x in _vdc['visuals']:
    _g=_x['governed']
    for _lang in ('en','ar'):
        for _k in ('title','prohibited_inference','alt_text','period','universe'):
            if not _g.get(f'{_k}_{_lang}'): errors.append(f'P3-G01 {_x["visual_id"]} lacks governed {_k}_{_lang}')
    if _x['tier'] in ('SIGNATURE','CORE_ANALYTICAL'):
        _c=_x.get('contract') or {}
        for _k in ('form','ordering','transformation','missing','breaks','annotation','mobile','rtl','fallback'):
            if not _c.get(_k): errors.append(f'P3-G01 {_x["visual_id"]} data contract lacks {_k}')
        if not (_c.get('credit') or {}).get('text'): errors.append(f'P3-G01 {_x["visual_id"]} has no governed credit line')
        if not (_c.get('series') or _c.get('objects')): errors.append(f'P3-G01 {_x["visual_id"]} binds no governed rows')
        for _lang in ('en','ar'):
            if not _x.get(f'detached_caption_{_lang}'): errors.append(f'P3-G01 {_x["visual_id"]} lacks detached_caption_{_lang}')
    elif 'contract' in _x:
        errors.append(f'P3-G01 {_x["visual_id"]} ({_x["tier"]}) carries a data contract it should not')
_charts=[str(f.relative_to(DIST)) for f in DIST.rglob('*.html') if re.search(r'<(svg|canvas)\b',f.read_text(encoding='utf-8'))]
if _charts: errors.append(f'P3-G02 static baseline draws a graphic without a design implementation: {_charts[:5]}')
def _scope_map(raw):
    out={}
    for m in re.finditer(r'data-visual-id="([^"]+)"(.*?)</ol>',raw,flags=re.S):
        out[m.group(1)]=any(a.startswith(('النطاق','Scope')) for a in re.findall(r'<li><strong>([^<]+)</strong>',m.group(2)))
    return out
for f in (DIST/'en').rglob('index.html'):
    af=DIST/'ar'/f.relative_to(DIST/'en')
    if not af.exists(): continue
    en_s,ar_s=_scope_map(f.read_text(encoding='utf-8')),_scope_map(af.read_text(encoding='utf-8'))
    for vid,has in en_s.items():
        if has and not ar_s.get(vid): errors.append(f'P3-G03 Arabic text alternative lacks the scope line English shows: {vid} {af.relative_to(DIST)}')
for f in (DIST/'ar').rglob('*.html'):
    txt=re.sub(r'<[^>]+>',' ',f.read_text(encoding='utf-8'))
    # U+2192 is not mirrored in right-to-left text, so between numbers it points against the reading order; U+2190 reads correctly.
    if re.search(r'\d[\d,.]*\s*\u2192\s*\d',txt): errors.append(f'P3-G04 right-pointing arrow between numbers in Arabic text: {f.relative_to(DIST)}')

# ---------------------------------------------------------------------------------------------------------------------
# Pre-Tranche-C P4 gates: one current-state story. Count statements in current-state documents must equal the derived
# public inventory (P4-G01); the navigation recorded in the compact Context and the handoff manifest must equal the
# navigation contract (P4-G03). Historical lineage files are outside this gate by design.
# ---------------------------------------------------------------------------------------------------------------------
_inv={c['key']:c['value'] for c in json.load(open(C/'content/public_inventory.json',encoding='utf-8'))['counts']}
_ns=len(specs)
_count_rules=[
    (r'(\d[\d,]*)\s+(?:controlled\s+)?Page Specs', _inv['page_specs']),
    (r'(\d[\d,]*)\s+Evidence Record(?:s| detail routes| routes| verification endpoints)\b', _inv['evidence_records']),
    (r'(\d[\d,]*)\s+(?:are\s+)?controlled public claims', _inv['public_claims']),
    (r'(\d[\d,]*)\s+source records', _inv['sources']),
    (r'(\d[\d,]*)\s+(?:expose|with|have)\s+a public original locator', _inv['public_locators']),
    (r'(\d[\d,]*)\s+with public original locators', _inv['public_locators']),
    (r'(\d[\d,]*)\s+curated (?:report/reference|resource) cards', _inv['curated_resources']),
    (r'(\d[\d,]*)\s+(?:local |controlled )?public[- ]search records', _inv['search_records']),
    (r'(\d[\d,]*)\s+(?:documented |dated )?(?:macro-financial / financial-inclusion-system )?chronology events', _inv['chronology_events']),
    (r'(\d[\d,]*)\s+governed visual contracts', _inv['visual_contracts']),
    (r'(\d[\d,]*)\s+(?:analytical |Evidence )?Readings\b', _inv['readings']),
    (r'(\d[\d,]*)\s+Measurement (?:Agenda )?priorities', _inv['measurement_priorities']),
    (r'(\d[\d,]*)\s+Evidence Passports', _inv['evidence_passports']),
    (r'(\d[\d,]*)\s+governed entry questions', _inv['entry_questions']),
    (r'(\d[\d,]*)\s+(?:static HTML documents|baseline static HTML outputs|total static HTML documents)', 2*_ns+2),
    (r'(\d[\d,]*)\s+(?:Arabic/English )?localized route documents', 2*_ns),
]
_current_docs=['README.md','OPENAI_REENTRY_CHECKPOINT.md']+[f'handoff/{x.name}' for x in sorted((ROOT/'handoff').glob('*.md'))]
for _rel in _current_docs:
    _p=ROOT/_rel
    if not _p.exists(): continue
    _t=_p.read_text(encoding='utf-8')
    for _pat,_want in _count_rules:
        for _m in re.finditer(_pat,_t):
            _got=int(_m.group(1).replace(',',''))
            if _got!=_want: errors.append(f'P4-G01 stale count in current-state document {_rel}: "{_m.group(0)}" (current {_want})')
try:
    _nav=json.load(open(C/'content/navigation_interaction.json',encoding='utf-8'))
    def _navnorm(items):
        out=[]
        for x in items:
            rec=(x.get('label_en'),x.get('label_ar'),x.get('route'),tuple((c.get('label_en'),c.get('label_ar'),c.get('route')) for c in x.get('children') or []))
            out.append(rec)
        return out
    _cn=context.get('public_navigation') or {}
    if _navnorm(_cn.get('primary',[]))!=_navnorm(_nav['global_navigation']):
        errors.append('P4-G03 compact Context primary navigation (labels EN/AR, routes, children) differs from the navigation contract')
    if _navnorm(_cn.get('trust',[]))!=_navnorm(_nav.get('trust_navigation',[])):
        errors.append('P4-G03 compact Context trust navigation differs from the navigation contract')
    _hm=json.load(open(ROOT/'handoff/IMPLEMENTATION_MANIFEST.json',encoding='utf-8'))
    _want_hm=[x['label_en']+(' ('+' · '.join(c['label_en'] for c in x['children'])+')' if x.get('children') else '') for x in _nav['global_navigation']]
    if _hm['information_design_contract']['global_primary_navigation']!=_want_hm:
        errors.append('P4-G03 handoff manifest primary navigation differs from the navigation contract')
    if _hm['information_design_contract'].get('trust_navigation')!=[x['label_en'] for x in _nav.get('trust_navigation',[])]:
        errors.append('P4-G03 handoff manifest trust navigation differs from the navigation contract')
    if _hm['navigation_contract']['controlled_route_coverage']!=len(_nav['routes']) or len(_hm.get('routes',[]))!=_ns:
        errors.append('P4-G03 handoff manifest route coverage differs from the controlled routes')
    # every public name of a navigation destination is its navigation label: header, trust bar, footer and breadcrumbs
    _lab={}
    for x in _nav['global_navigation']:
        for y in ([x] if x.get('route') else [])+list(x.get('children') or []): _lab[y['route']]=(y['label_en'],y['label_ar'])
    for x in _nav.get('trust_navigation',[]): _lab[x['route']]=(x['label_en'],x['label_ar'])
    for _lang,_i in (('en',0),('ar',1)):
        for _rel in ('index.html','readings/same-year-different-number/index.html','people/index.html','evidence/CLM-001/index.html'):
            _raw=(DIST/_lang/_rel).read_text(encoding='utf-8')
            for _blk in re.findall(r'<(?:header|footer|nav)\b.*?</(?:header|footer|nav)>',_raw,flags=re.S):
                for _cls,_href,_txt in re.findall(r'<a(?:\s+class="([^"]*)")?[^>]*href="/'+_lang+r'(/[^"#?]*)"[^>]*>([^<]+)</a>',_blk):
                    if re.search(r'action|btn',_cls or ''): continue       # utility actions (e.g. "Report an issue") are verbs, not destination names
                    if _href in _lab and _html.unescape(_txt).strip()!=_lab[_href][_i]:
                        errors.append(f'P4-G03 navigation destination {_href} named "{_txt.strip()}" instead of "{_lab[_href][_i]}" on /{_lang}/{_rel}')
            for _grp in _nav.get('footer_groups',[]):
                if _grp[f'label_{_lang}'] not in _html.unescape(_raw): errors.append(f'P4-G03 footer group label missing /{_lang}/{_rel}: {_grp["label_"+_lang]}')
except Exception as _e:
    errors.append(f'P4-G03 navigation state unreadable {_e}')

# P4-G04: one hash story. README and the checkpoint carry the current Master and Page Specs SHA-256; any other SHA-256 they
# print must be a labelled lineage hash recorded in AUTHORITY.json / the handoff manifest (the Drive-recorded entry state).
try:
    _cur_m=hashlib.sha256((ROOT/'authority/Yemen_Financial_Inclusion_Evidence_Master.xlsx').read_bytes()).hexdigest()
    _cur_p=hashlib.sha256((C/'page_specs.json').read_bytes()).hexdigest()
    _hm=json.load(open(ROOT/'handoff/IMPLEMENTATION_MANIFEST.json',encoding='utf-8'))
    _allowed={_cur_m,_cur_p,(auth.get('production_master') or {}).get('drive_recorded_sha256'),_hm['authority'].get('page_specs_drive_recorded_sha256')}
    for _rel in ('README.md','OPENAI_REENTRY_CHECKPOINT.md'):
        _t=(ROOT/_rel).read_text(encoding='utf-8')
        if _cur_m not in _t or _cur_p not in _t: errors.append(f'P4-G04 {_rel} does not carry the current Master and Page Specs SHA-256')
        for _h in set(re.findall(r'(?<![0-9a-f])[0-9a-f]{64}(?![0-9a-f])',_t))-_allowed:
            errors.append(f'P4-G04 {_rel} prints a SHA-256 that is neither current nor recorded lineage: {_h[:12]}…')
    for _k,_v in (('Context',context.get('production_master',{}).get('sha256')),('handoff manifest',_hm['authority'].get('master_sha256'))):
        if _v!=_cur_m: errors.append(f'P4-G04 {_k} Master SHA-256 is not the current Master')
except Exception as _e:
    errors.append(f'P4-G04 hash story unreadable {_e}')

# P4-G05: the architecture diagrams show the current navigation and counts (scripts/architecture_diagrams.py --check).
try:
    sys.path.insert(0,str(ROOT/'scripts'))
    import architecture_diagrams as _ad
    _want,_diffs=_ad.render(check=True)
    if _diffs: errors.append(f'P4-G05 architecture diagrams are stale (run scripts/architecture_diagrams.py): {_diffs}')
    for _name in _want:
        if not (ROOT/'design/architecture'/_name.replace('.svg','.png')).exists(): errors.append(f'P4-G05 PNG preview missing for {_name}')
except SystemExit as _e:
    errors.append(f'P4-G05 architecture diagrams cannot be derived: {_e}')
except Exception as _e:
    errors.append(f'P4-G05 architecture diagrams unreadable {_e}')

# P2-G03 (P4 re-verification N1/N2): no empty heading element; numbered sections start at 01 and run without gaps.
for _f in DIST.rglob('*.html'):
    _raw=_f.read_text(encoding='utf-8')
    if re.search(r'<h[1-6][^>]*>\s*</h[1-6]>',_raw): errors.append(f'P2-G03 empty heading element {_f.relative_to(DIST)}')
    _nums=[int(x) for x in re.findall(r'<div class="section-number">(\d+)</div>',_raw)]
    if _nums and _nums!=list(range(1,len(_nums)+1)): errors.append(f'P2-G03 section numbering is not 01..n {_f.relative_to(DIST)}: {_nums[:4]}')

# P2-G03 (P4 extension, V-D10): within one section the eyebrow never repeats a heading, adjacent or not.
for _f in DIST.rglob('*.html'):
    _raw=_f.read_text(encoding='utf-8')
    for _sec in re.split(r'<section\b',_raw)[1:]:
        _eb={_html.unescape(x).strip().rstrip('?؟').strip() for x in re.findall(r'<div class="eyebrow">([^<]+)</div>',_sec)}
        _hs={_html.unescape(x).strip().rstrip('?؟').strip() for x in re.findall(r'<h[1-3][^>]*>([^<]+)</h[1-3]>',_sec)}
        for _x in _eb & _hs:
            errors.append(f'P2-G03 eyebrow repeats a heading in the same section {_f.relative_to(DIST)}: {_x[:40]}')

# Tranche C permanent gates (TC-G01..TC-G05).
# TC-G01 one owner, A == prohibited inference: a visual that is also an Evidence Record has one title and one "does not
# establish" text in both languages (06 limitations part A equals 11 prohibited inference; 06 title equals 11 title).
try:
    _tc_eo={r['object_id']:r for r in json.load(open(C/'evidence/evidence_objects.json',encoding='utf-8'))}
    _tc_vl={r['visual_id']:r for r in json.load(open(C/'visuals/visual_library.json',encoding='utf-8'))}
    for _vid,_v in _tc_vl.items():
        _e=_tc_eo.get(_vid)
        if not _e: continue
        for _L in ('en','ar'):
            if (_e.get('title_'+_L) or '').strip()!=(_v.get('title_'+_L) or '').strip():
                errors.append(f'TC-G01 06/11 title differs {_vid} {_L}')
            if (_e.get('does_not_establish_'+_L) or '').strip()!=(_v.get('prohibited_inference_'+_L) or '').strip():
                errors.append(f'TC-G01 06 limitation (part A) differs from 11 prohibited inference {_vid} {_L}')
except Exception as _x:
    errors.append('TC-G01 unreadable '+str(_x))
# TC-G02 one Reading title: the Reading page h1 and <title> carry the 08 title in both languages.
try:
    for _r in json.load(open(C/'content/readings.json',encoding='utf-8')):
        for _L in ('en','ar'):
            _f=DIST/_L/str(_r['route']).strip('/')/'index.html'
            _raw=_f.read_text(encoding='utf-8')
            _h1=re.search(r'<h1[^>]*>(.*?)</h1>',_raw,re.S)
            if not _h1 or _html.unescape(re.sub(r'<[^>]+>','',_h1.group(1))).strip()!=(_r.get('title_'+_L) or '').strip():
                errors.append(f'TC-G02 Reading h1 is not the 08 title {_r["reading_id"]} {_L}')
except Exception as _x:
    errors.append('TC-G02 unreadable '+str(_x))
# R8.5 (26 Sep 2026) one owner for public copy — permanent gates.
#  R85-G01 no bilingual public copy in code: build.py holds no "<Arabic>" if ar else "<English>" pair, app.js no isAr ? '…' : '…'
#  R85-G02 every interface-copy ID the code uses exists in 04, and app.js reads only UI-JS-* IDs the build ships
#  R85-G03 a governed label carries the same {placeholders} in English and Arabic
try:
    _b=(ROOT/'scripts/build.py').read_text(encoding='utf-8'); _j=(ROOT/'site-src/app.js').read_text(encoding='utf-8')
    _pairs=re.findall(r"""(['"])[^'"\n]*[ء-ي][^'"\n]*\1\s+if\s+(?:ar|lang==['"]ar['"])\s+else\s+(['"])""",_b)   # Arabic letters; an Arabic punctuation separator is a locale rule, not copy
    if _pairs: errors.append(f'R85-G01 bilingual public copy held in build.py ({len(_pairs)} pairs); move it to 04 interface copy')
    if re.search(r"isAr\s*\?\s*['\"`]",_j): errors.append('R85-G01 bilingual public copy held in app.js (isAr ? literal); move it to 04 interface copy')
    _ui={r['ui_id']:r for r in json.load(open(C/'content/interface_copy.json',encoding='utf-8'))}
    for _id in sorted(set(re.findall(r"""ui_(?:text|fmt)\(\s*['"](UI-[A-Z0-9-]+)['"]""",_b))|set(re.findall(r"""\b(?:T|TF)\(\s*['"](UI-[A-Z0-9-]+)['"]""",_j))|set(re.findall(r'"(UI-JS-[A-Z0-9-]+)"',_j))):
        if _id not in _ui: errors.append(f'R85-G02 interface copy ID used in code is missing from 04: {_id}')
    for _id in set(re.findall(r'"(UI-[A-Z0-9-]+)"',_j))|set(re.findall(r"""\b(?:T|TF)\(\s*['"](UI-[A-Z0-9-]+)['"]""",_j)):
        if not _id.startswith('UI-JS-'): errors.append(f'R85-G02 app.js reads a label the build does not ship (not UI-JS-*): {_id}')
    for _id,_r in _ui.items():
        if set(re.findall(r'\{(\w+)\}',_r.get('label_en') or ''))!=set(re.findall(r'\{(\w+)\}',_r.get('label_ar') or '')):
            errors.append(f'R85-G03 placeholders differ between English and Arabic in {_id}')
except Exception as _x:
    errors.append('R85-G unreadable '+repr(_x))
# F2 (26 Sep 2026) Evidence Readings family — permanent gates.
#  RP-G01 every Reading ends its essay with "What would change this reading?", then the evidence path, then 1-2 related Readings
#  RP-G02 one signature visual at most on a Reading page; no numbered section template and no Reading card wall
#  RP-G03 exactly one featured Reading, the same on Home, Explore and the Readings index
#  RP-G04 an answer page carries at most two Readings; Evidence Records list the Readings that bind them
#  RP-G05 retired Reading titles and the retired generic section never reappear in content or public HTML
#  RP-G06 every English/Arabic page pair prints the same numbers (bilingual invariance; BIL-05 closed)
try:
    _RP_END={'en':'What would change this reading?','ar':'ما الذي قد يغيّر هذه القراءة؟'}
    _rds=json.load(open(C/'content/readings.json',encoding='utf-8'))
    _feat=[r['reading_id'] for r in _rds if r.get('featured')=='FEATURED']
    if len(_feat)!=1: errors.append(f'RP-G03 exactly one featured Reading required: {_feat}')
    for _r in _rds:
        for _L in ('en','ar'):
            _raw=(DIST/_L/str(_r['route']).strip('/')/'index.html').read_text(encoding='utf-8')
            _secs=re.findall(r'<section class="reading-section"[^>]*>(.*?)</section>',_raw,re.S)
            _h=[_html.unescape(re.sub(r'<[^>]+>','',x)).strip() for x in re.findall(r'<h2>(.*?)</h2>',_secs[-1] if _secs else '')]
            if not _h or _h[0]!=_RP_END[_L]:
                errors.append(f'RP-G01 Reading essay does not end with "{_RP_END[_L]}" {_r["reading_id"]} {_L}')
            _i=[_raw.find(m) for m in ('class="reading-essay"','data-reading-verify','data-reading-related')]
            if min(_i)<0 or _i!=sorted(_i):
                errors.append(f'RP-G01 Reading order must be essay -> evidence path -> related Readings {_r["reading_id"]} {_L}')
            if len(re.findall(r'data-related-reading|class="reading-related-link"',_raw)) not in (1,2):
                errors.append(f'RP-G01 a Reading links one or two related Readings {_r["reading_id"]} {_L}')
            if _raw.count('data-visual-id=')>1:
                errors.append(f'RP-G02 more than one visual on a Reading page {_r["reading_id"]} {_L}')
            if 'class="section-number"' in _raw:
                errors.append(f'RP-G02 numbered section template on a Reading page {_r["reading_id"]} {_L}')
            if _L=='ar' and '→' in re.sub(r'<script.*?</script>','',_raw,flags=re.S).split('class="reading-essay"')[1].split('data-reading-verify')[0]:
                errors.append(f'RP-G02 left-to-right arrow in an Arabic Reading essay {_r["reading_id"]}')
    for _L in ('en','ar'):
        _ids=set()
        for _rel in ('index.html','explore/index.html','readings/index.html'):
            _raw=(DIST/_L/_rel).read_text(encoding='utf-8')
            _f=re.findall(r'data-featured-reading="([^"]+)"',_raw)
            if len(_f)!=1: errors.append(f'RP-G03 one featured Reading expected on /{_L}/{_rel}: {_f}')
            _ids.update(_f)
        if _ids!=set(_feat): errors.append(f'RP-G03 featured Reading differs across Home/Explore/Readings {_L}: {sorted(_ids)} vs {_feat}')
        _idx=(DIST/_L/'readings/index.html').read_text(encoding='utf-8')
        if 'class="reading-card' in _idx: errors.append(f'RP-G02 Readings index renders a card wall {_L}')
        for _f in (DIST/_L).glob('*/index.html'):
            if _f.read_text(encoding='utf-8').count('data-domain-reading=')>2:
                errors.append(f'RP-G04 more than two Readings on {_f.relative_to(DIST)}')
    _bound={}
    for _r in _rds:
        for _x in (_r.get('claim_bindings') or [])+(_r.get('evidence_bindings') or [])+((_r.get('verification_bindings') or {}).get('claim_ids') or []):
            _bound.setdefault(_x,set()).add(_r['reading_id'])
    for _oid,_set in _bound.items():
        for _L in ('en','ar'):
            _f=DIST/_L/'evidence'/_oid/'index.html'
            if _f.exists():
                _raw=_f.read_text(encoding='utf-8')
                if 'data-used-in-readings' not in _raw:
                    errors.append(f'RP-G04 Evidence Record does not list the Readings that use it {_oid} {_L}')
    _RETIRED=['When a balance sheet jumps without the economy necessarily moving','Targets depend on what is being counted',
              'The reform clock is moving faster than the people-side evidence','When digital activity does not yet establish durable inclusion',
              'Borrower counts, savers and nominal portfolio can move differently','A gender gap is measured. Its causes are not.',
              'Finance can be a serious constraint without being the most frequently named business challenge',
              'From rail to result: the missing middle matters','After the transfer, the missing metric is persistence',
              'Evidence turned into decision-relevant analysis','Trace the reading back to evidence','Microfinance is growing. What exactly is growing?']
    _hay=[p for p in list((DIST).rglob('*.html'))+list(C.rglob('*.json')) if p.is_file()]
    for _p in _hay:
        _t=_p.read_text(encoding='utf-8')
        for _s in _RETIRED:
            if _s in _t: errors.append(f'RP-G05 retired Reading copy "{_s[:50]}" in {_p.relative_to(ROOT) if str(_p).startswith(str(ROOT)) else _p}')
    import subprocess as _sp
    _inv=_sp.run([sys.executable,str(ROOT/'audit/tranche_c/checks/bilingual_invariance.py')],capture_output=True,text=True)
    if _inv.returncode!=0: errors.append('RP-G06 bilingual numeric invariance: '+(_inv.stdout.strip().splitlines() or ['?'])[0])
except Exception as _x:
    errors.append('RP-G unreadable '+repr(_x))
# TC-G03 no bare source reference as a name: a source card or record source item with a governed title never shows its ID
# as the title; a locator-only source is named by the governed "Original source" label.
for _L in ('en','ar'):
    for _f in (DIST/_L/'evidence').rglob('index.html'):
        _raw=_f.read_text(encoding='utf-8')
        if re.search(r'<article class="evidence-source-item"[^>]*><strong>SRC-',_raw):
            errors.append(f'TC-G03 source named by its reference {_f.relative_to(DIST)}')
# TC-G04 no generic imperative limitation in public "what not to conclude" fields (EN-07): part A of every record is declarative.
for _oid,_e in (_tc_eo.items() if '_tc_eo' in dir() else []):
    _a=(_e.get('does_not_establish_en') or '').strip()
    if re.match(r'^(Do not|Never|Must)\b',_a):
        errors.append(f'TC-G04 imperative limitation {_oid}')
    if (_e.get('does_not_establish_ar') or '').startswith('لا يجوز'):
        errors.append(f'TC-G04 imperative limitation (AR) {_oid}')
# TC-G05 the unsourced 26 uploaded block and the removed personal name never return to public data.
for _f in (C/'data').glob('*.json'):
    _t=_f.read_text(encoding='utf-8')
    if 'Uploaded 2014–2022 longitudinal inputs' in _t: errors.append(f'TC-G05 unsourced Findex block returned in {_f.name}')
    if 'Iyad' in _t or 'أياد السعدي' in _t: errors.append(f'TC-G05 personal name returned in {_f.name}')

print(f'HTML={len(list(DIST.rglob("*.html")))} ERRORS={len(errors)} WARN={len(warns)}')
if errors:
    for e in errors[:100]: print('FAIL',e)
    sys.exit(1)
print('WEBSITE REPOSITORY VALIDATION PASS')
