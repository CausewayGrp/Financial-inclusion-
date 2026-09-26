#!/usr/bin/env python3
from pathlib import Path
import json, html, shutil, re
from urllib.parse import quote

ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/'site-src'; C=SRC/'content'; DIST=ROOT/'dist'
if DIST.exists(): shutil.rmtree(DIST)
DIST.mkdir(); (DIST/'assets').mkdir(); (DIST/'static-data').mkdir()
for name in ['styles.css','app.js']:
    shutil.copy2(SRC/name,DIST/'assets'/name)
shutil.copy2(SRC/'assets/CauseWay_Master_Logo.png',DIST/'assets/CauseWay_Master_Logo.png')
shutil.copy2(C/'content/search_index.json',DIST/'static-data/search_index.json')
shutil.copy2(C/'content/search_aliases.json',DIST/'static-data/search_aliases.json')   # PB-0492 governed discovery aliases

def load(p): return json.load(open(p,encoding='utf-8'))
def load_specs():
    bundle=load(C/'page_specs.json')
    return bundle.get('page_specs',[])
SPECS=load_specs()
SOURCE_REFS=load(C/'sources/source_reference_map.json')
PUBLIC_SOURCE_CLOSURE=load(C/'sources/public_object_source_closure.json')
# Governed interface copy (04_NAV_UX block 'Governed interface copy'; Tranche B Stage 1).
UI_COPY={str(r.get('ui_id')):r for r in load(C/'content/interface_copy.json')}
def ui_text(ui_id,lang):
    r=UI_COPY.get(ui_id)
    if not r: raise SystemExit(f'governed interface copy missing: {ui_id}')
    return r.get(f'label_{lang}') or ''
def esc(x): return html.escape(str(x or ''), quote=True)
def locv(o,key,lang): return o.get(f'{key}_{lang}') or o.get(key) or ''

# Pre-Tranche-C P1.2: repository inventory counts come from the derived contract, never from typed copy.
INVENTORY={str(c['key']):int(c['value']) for c in load(C/'content/public_inventory.json')['counts']}
_INV_LINE=re.compile(r'^(.+?):\s*(\d{1,3}(?:,\d{3})*)$')

_EMAIL=re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b')

def _linkify(escaped):
    """P2.3: a contact address in governed copy is actionable; the text itself is unchanged."""
    return _EMAIL.sub(lambda m: f'<a href="mailto:{m.group(0)}" dir="ltr">{m.group(0)}</a>', escaped)

def paras(text):
    """A section body renders one paragraph per authored line (a newline in governed copy is a paragraph break)."""
    return ''.join(f'<p>{_linkify(esc(p.strip()))}</p>' for p in str(text or '').split('\n') if p.strip())

def section_body(s,lang):
    """Body of a governed section. A body made only of 'label: count' lines whose counts were resolved from the
    public inventory contract renders as a definition list (the repository inventory on /data/)."""
    b=s.get(f'body_{lang}') or ''
    toks=[t for t in (s.get('resolved_inventory_tokens') or []) if t.get('field')==f'body_{lang}']
    lines=[x.strip() for x in b.split('\n') if x.strip()]
    if toks and lines and all(_INV_LINE.match(x) for x in lines):
        items=''.join(f'<div><dt>{esc(_INV_LINE.match(x).group(1))}</dt><dd dir="ltr">{esc(_INV_LINE.match(x).group(2))}</dd></div>' for x in lines)
        return f'<dl class="inventory-list" data-public-inventory>{items}</dl>'
    return paras(b)

def public_ref(oid,lang):
    """PID-1: a stable record reference is shown only where it aids verification or citation, and always labelled."""
    lab='المرجع' if lang=='ar' else 'Reference'
    return f'<span class="record-ref" data-public-ref><span class="record-ref-label">{lab}</span> <bdi dir="ltr">{esc(oid)}</bdi></span>'

# Public evidence-detail routes are discovered from the controlled Page Specs.
# They are used only for navigation; they never create or reinterpret evidence.
DETAIL_ROUTES={}
for _o in SPECS:
    if _o.get('page_class')!='evidence_detail':
        continue
    _route=_o.get('route')
    for _x in (_o.get('governed_claims') or [])+(_o.get('governed_evidence_objects') or [])+(_o.get('governed_visual_contracts') or []):
        _id=_x.get('claim_id') or _x.get('evidence_object_id') or _x.get('object_id') or _x.get('visual_id')
        if _id and _route:
            DETAIL_ROUTES[str(_id)]=_route

def route_href(route,lang):
    clean=str(route or '/').strip('/')
    return f'/{lang}/' + (clean+'/' if clean else '')

def search_dialog(lang):
    ar=lang=='ar'
    search='بحث' if ar else 'Search'; close='إغلاق' if ar else 'Close'; search_title='ابحث في الأدلة العامة' if ar else 'Search the public evidence'; ph='ابحث في الأسئلة والأدلة والقراءات والمصادر...' if ar else 'Search questions, evidence, readings and sources...'
    status='حالة البحث' if ar else 'Search status'
    return f'<dialog id="search-dialog" class="search-dialog" aria-labelledby="search-dialog-title"><div class="search-dialog-panel"><div class="search-dialog-head"><strong id="search-dialog-title">{search_title}</strong><button class="icon-btn" data-search-close aria-label="{close}">×</button></div><div class="search-shell"><span aria-hidden="true">⌕</span><input id="global-search-dialog" data-search-input class="search-input" placeholder="{ph}" aria-label="{search}"></div><div class="search-status" data-search-status role="status" aria-live="polite" aria-label="{status}"></div><div data-search-results class="search-results"></div></div></dialog>'

def header(lang,route):
    ar=lang=='ar'
    nav=[]
    def _link(item):
        target=str(item.get('route') or '/')
        key=target.strip('/').split('/',1)[0]
        active=bool(key) and route.startswith('/'+key)
        current=' aria-current="page"' if active else ''
        cls=' class="active"' if active else ''
        label=item.get('label_ar') if ar else item.get('label_en')
        return f'<a{cls}{current} href="{route_href(target,lang)}">{esc(label)}</a>', active
    for item in NAVIGATION_INTERACTION.get('global_navigation',[]):
        kids=item.get('children') or []
        if kids:
            # PB-0422/PB-0424: a navigation family shows both destinations at all times (no hover-only meaning);
            # Claude Design may choose the final treatment within these conditions.
            links=[_link(k) for k in kids]
            active=any(a for _,a in links)
            glabel=item.get('label_ar') if ar else item.get('label_en')
            nav.append(f'<span class="nav-group{" active" if active else ""}" role="group" aria-label="{esc(glabel)}"><span class="nav-group-label">{esc(glabel)}</span>{"".join(l for l,_ in links)}</span>')
        else:
            nav.append(_link(item)[0])
    nav=''.join(nav)
    trust_items=NAVIGATION_INTERACTION.get('trust_navigation',[])
    trust_label='روابط الثقة' if ar else 'Trust links'
    trust_nav=(f'<nav class="trust-nav" aria-label="{trust_label}"><div class="trust-nav-inner">'+''.join(_link(t)[0] for t in trust_items)+'</div></nav>') if trust_items else ''
    skip='انتقل إلى المحتوى' if ar else 'Skip to content'; primary='التنقل الرئيسي' if ar else 'Primary navigation'; search='بحث' if ar else 'Search'; brand='أدلة الشمول المالي في اليمن' if ar else 'Yemen Financial Inclusion Evidence'; other='en' if ar else 'ar'; other_label='EN' if ar else 'العربية'; menu='القائمة' if ar else 'Menu'; cite='استشهد بهذه الصفحة' if ar else 'Cite this page'; issue='الإبلاغ عن مشكلة' if ar else 'Report an issue'; switch_label='Switch to English' if ar else 'التبديل إلى العربية'; copied='تم النسخ' if ar else 'Copied'
    mobile_tools=f'<div class="mobile-nav-utilities"><button type="button" class="mobile-nav-action" data-cite aria-label="{cite}">{cite}</button><a class="mobile-nav-action" href="/{lang}/contact/">{issue}</a></div>'
    return f'<a class="skip" href="#main">{skip}</a>{trust_nav}<header class="header"><div class="header-inner"><a class="brand" href="/{lang}/" aria-label="CauseWay — {brand}"><img src="/assets/CauseWay_Master_Logo.png" alt="CauseWay"></a><nav id="primary-nav" class="nav" aria-label="{primary}">{nav}{mobile_tools}</nav><div class="utilities"><button class="icon-btn search-btn" data-search-open aria-label="{search}"><span aria-hidden="true">⌕</span><span class="utility-label">{search}</span></button><button class="icon-btn cite-btn" data-cite aria-label="{cite}">↗</button><a class="icon-btn issue-btn" href="/{lang}/contact/" aria-label="{issue}">!</a><button class="lang-btn" data-lang="{other}" aria-label="{switch_label}" lang="{other}" dir="{"ltr" if other=="en" else "rtl"}">{other_label}</button><button class="icon-btn menu-btn" data-menu aria-label="{menu}" aria-controls="primary-nav" aria-expanded="false">☰</button></div></div><div id="utility-status" class="sr-only" role="status" aria-live="polite" aria-atomic="true" data-copied-label="{copied}"></div></header>{search_dialog(lang)}'

def footer(lang):
    ar=lang=='ar'
    desc=ui_text('UI-FOOTER-STRAPLINE',lang)   # PB-0412: governed Master row (04 'Governed interface copy')
    rights='الأدلة المنشورة تحتفظ بنسبة المصدر الأصلي.' if ar else 'Published evidence remains attributed to the original source.'
    groups=[]
    for group in NAVIGATION_INTERACTION.get('footer_groups',[]):
        glabel=group.get('label_ar') if ar else group.get('label_en')
        links=''.join(
            f'<a href="{route_href(item.get("route"),lang)}">{esc(item.get("label_ar") if ar else item.get("label_en"))}</a>'
            for item in group.get('links',[])
        )
        groups.append(f'<div class="footer-nav-group"><strong>{esc(glabel)}</strong>{links}</div>')
    nav=''.join(groups)
    return f'<footer class="footer"><div class="container"><div class="footer-grid"><div><img src="/assets/CauseWay_Master_Logo.png" alt="CauseWay"><p>{desc}</p></div><nav class="footer-nav" aria-label="{"روابط المنتج والثقة" if ar else "Product and trust links"}">{nav}</nav></div><div class="fine">© 2026 CauseWay · {rights}</div></div></footer>'

def hero(spec,lang):
    ar=lang=='ar'; title=locv(spec,'title',lang); lead=''
    for s in spec.get('sections',[]):
        body=s.get(f'body_{lang}')
        if body:
            if not s.get(f'heading_{lang}'): lead=body.split('\n')[0]   # P4 (V-D12): a headed first section is not repeated as the lead
            break
    lead_html=f'<p class="hero-lead">{esc(lead)}</p>' if lead else ''
    eye='أدلة الشمول المالي في اليمن' if ar else 'Yemen Financial Inclusion Evidence'; start='ابدأ بالسؤال' if ar else 'Start with a question'; verify='تحقق من الأدلة' if ar else 'Verify evidence'; flow='افهم ← استكشف ← تحقّق' if ar else 'Understand → Explore → Verify'; side='يعرض هذا المورد أقوى ما تسمح به الأدلة، مع إبقاء حدود الاستنتاج والمصدر ظاهرين.' if ar else 'This resource presents the strongest defensible answer while keeping scope, limits and source visible.'
    return f'<section class="hero"><div class="hero-inner"><div><div class="eyebrow">{eye}</div><h1>{esc(title)}</h1>{lead_html}<div class="hero-actions"><a class="button primary" href="/{lang}/explore/">{start}</a><a class="button ghost" href="/{lang}/evidence/">{verify}</a></div></div><aside class="hero-side"><strong>{flow}</strong><p>{side}</p></aside></div></section>'


PRESENTATION_PRIORITY=load(C/'presentation_priority.json')
READING_SECTIONS=load(C/'content/reading_sections.json')
NAVIGATION_INTERACTION=load(C/'content/navigation_interaction.json')
if NAVIGATION_INTERACTION.get('authority_scope')!='NAVIGATION_AND_INTERACTION_ONLY':
    raise ValueError('navigation_interaction.json must be NAVIGATION_AND_INTERACTION_ONLY')
ROUTE_NEXT_ACTIONS=NAVIGATION_INTERACTION.get('route_next_actions') or {}
PRESENTATION_ROUTES={
    str(entry.get('route')): entry
    for entry in PRESENTATION_PRIORITY.get('routes',[])
    if entry.get('page_family')=='Domain Answer' and entry.get('route')
}
FAMILY_PRESENTATION=PRESENTATION_PRIORITY.get('family_contracts') or {}
EVIDENCE_PRESENTATION=FAMILY_PRESENTATION.get('Evidence Record') or {}
COMPARISON_PRESENTATION=FAMILY_PRESENTATION.get('Comparison') or {}
SPEC_BY_ROUTE={str(o.get('route')):o for o in SPECS if o.get('route')}
PUBLIC_ROUTE_LABELS={}
for _item in NAVIGATION_INTERACTION.get('global_navigation',[]):
    for _x in ([_item] if _item.get('route') else [])+list(_item.get('children') or []):
        PUBLIC_ROUTE_LABELS[str(_x.get('route'))]=(_x.get('label_ar'),_x.get('label_en'))
for _item in NAVIGATION_INTERACTION.get('trust_navigation',[]):
    PUBLIC_ROUTE_LABELS[str(_item.get('route'))]=(_item.get('label_ar'),_item.get('label_en'))
for _group in NAVIGATION_INTERACTION.get('footer_groups',[]):
    for _item in _group.get('links',[]):
        PUBLIC_ROUTE_LABELS.setdefault(str(_item.get('route')),(_item.get('label_ar'),_item.get('label_en')))

def _nav_label(route,lang):
    # P4 (V-D3): every public name of a navigation destination is the governed navigation label
    ar_,en_=PUBLIC_ROUTE_LABELS[route]
    return ar_ if lang=='ar' else en_
SOURCE_BY_ID={str(r.get('source_id')):r for r in SOURCE_REFS if r.get('source_id')}
# P3: a visual that is also an Evidence Record takes its bilingual period and universe from that record (06), so the
# Arabic text alternative carries the same scope line as the English one.
EVIDENCE_OBJECT_BY_ID={str(r.get('object_id')):r for r in load(C/'evidence/evidence_objects.json')}

def route_action_label(route,lang):
    pair=PUBLIC_ROUTE_LABELS.get(str(route))
    if pair:
        return pair[0] if lang=='ar' else pair[1]
    target=SPEC_BY_ROUTE.get(str(route)) or {}
    return locv(target,'title',lang) or str(route)

def breadcrumb(page_family,current_id,lang,current_title=None):
    cfg=(NAVIGATION_INTERACTION.get('breadcrumbs') or {}).get(page_family) or {}
    parent=cfg.get('parent_route')
    if not parent:
        return ''
    ar=lang=='ar'
    parent_label=cfg.get('parent_label_ar') if ar else cfg.get('parent_label_en')
    aria='مسار الصفحة' if ar else 'Breadcrumb'
    # PID-1: the current item is the page's governed title; an Evidence Record keeps its reference, which aids citation.
    current=(f'<span aria-current="page">{esc(current_title)}</span>' if current_title else
             f'<span aria-current="page" class="stable-id" dir="ltr">{esc(current_id)}</span>')
    return (
        f'<nav class="breadcrumb" aria-label="{aria}">'
        f'<a href="{route_href(parent,lang)}">{esc(parent_label)}</a>'
        f'<span aria-hidden="true">/</span>{current}'
        f'</nav>'
    )

def journey_next(spec,lang):
    route=str(spec.get('route') or '/')
    actions=ROUTE_NEXT_ACTIONS.get(route) or []
    if not actions:
        return ''
    ar=lang=='ar'
    title='تابع من هنا' if ar else 'Continue from here'
    intro='اختر المسار الأقرب لما تريد فعله بعد ذلك.' if ar else 'Choose the next path that matches what you need to do.'
    links=[]
    for target in actions:
        label=route_action_label(target,lang)
        links.append(f'<a class="journey-next-link" href="{route_href(target,lang)}"><span>{esc(label)}</span><span aria-hidden="true">{"←" if ar else "→"}</span></a>')
    return (
        f'<section class="journey-next"><div class="container journey-next-grid">'
        f'<div><h2>{esc(title)}</h2><p>{esc(intro)}</p></div>'
        f'<nav class="journey-next-links" aria-label="{esc(title)}">{"".join(links)}</nav>'
        f'</div></section>'
    )
def public_locator(v):
    # Only an http(s) URL is a public original locator; any other text (e.g. a note about a privately supplied file) is not shown.
    v=str(v or '').strip()
    return v if v.lower().startswith(('http://','https://')) else ''
QUESTIONS=load(C/'content/questions.json')
def _qroute(r):
    r=str(r or '').strip('/')
    return '/'+r+'/' if r else '/'
QUESTION_BY_ROUTE={_qroute(q.get('primary_route')):q for q in QUESTIONS}
READINGS_ALL=load(C/'content/readings.json')
SYSTEM_RELATIONSHIPS=load(C/'visuals/system_relationships.json')
SYSTEM_CHRONOLOGY=load(C/'visuals/system_chronology.json')
def route_question_label(route,lang):
    # Tranche C (JRN-02/07/12): an answer page is named by the governed question it answers, else by its title
    q=QUESTION_BY_ROUTE.get(route)
    if q: return locv(q,'question',lang)
    sp=SPEC_BY_ROUTE.get(route)
    return locv(sp or {},'title',lang)
_CMP_SPEC=SPEC_BY_ROUTE.get('/evidence/compare/') or {}
COMPARE_IDS={str(x.get('evidence_object_id') or x.get('object_id') or x.get('claim_id') or '') for x in (_CMP_SPEC.get('governed_evidence_objects') or [])+(_CMP_SPEC.get('governed_claims') or [])}-{''}
PUBLIC_SOURCE_IDS={sid for sid,r in SOURCE_BY_ID.items() if r.get('metadata_state')=='DISPLAY_READY' or public_locator(r.get('primary_url'))}
SOURCE_CLOSURE_BY_KEY={(str(r.get('object_type')),str(r.get('object_id'))):r for r in PUBLIC_SOURCE_CLOSURE if r.get('object_type') and r.get('object_id')}
SOURCE_DEPENDENTS={}
for _spec in SPECS:
    if _spec.get('page_class')!='evidence_detail':
        continue
    _obj=(_spec.get('governed_evidence_objects') or [{}])[0]
    _oid=str(_obj.get('evidence_object_id') or _obj.get('object_id') or '')
    if not _oid:
        continue
    for _ref in _spec.get('source_references') or []:
        _sid=str(_ref.get('source_id') or '').strip()
        if _sid and _sid in PUBLIC_SOURCE_IDS:
            SOURCE_DEPENDENTS.setdefault(_sid,[]).append({
                'route':_spec.get('route'),
                'object_id':_oid,
                'title_en':locv(_obj,'title','en') or _oid,
                'title_ar':locv(_obj,'title','ar') or _oid,
            })

def _presentation_section_orders(items):
    return [int(x.get('section_order')) for x in (items or []) if x.get('kind')=='section' and isinstance(x.get('section_order'),int)]

def _presentation_visual(items):
    for x in items or []:
        if x.get('kind')=='visual' and x.get('object_id'):
            return str(x.get('object_id')), int(x.get('after_primary') or 2)
    return None, 2

def _presentation_verify_ids(items):
    out=[]
    for x in items or []:
        if x.get('kind')=='verification_records':
            out.extend(str(v) for v in (x.get('object_ids') or []) if v)
    return out

def _localized_section_map(spec, lang):
    rows={}
    for s in spec.get('sections',[]):
        if not (s.get(f'heading_{lang}') or s.get(f'body_{lang}')):
            continue
        rows.setdefault(s.get('section_order'), s)
    return rows

def _first_line(text):
    for line in str(text or '').splitlines():
        line=line.strip()
        if line:
            return line
    return ''

def _domain_labels(lang):
    if lang=='ar':
        return {
            'scope':'النطاق والزمن',
            'boundary':'ما لا يُستنتج',
            'unknown':'ما يزال غير معروف',
            'coverage':'قيد التغطية',
            'visual':'عرض يغيّر الفهم',
            'more':'مزيد من الأدلة والسياق',
            'more_intro':'تفاصيل إضافية من الصفحة نفسها، محفوظة مع حدودها الأصلية.',
            'measure':'ما القياس الذي سيغيّر القرار؟',
            'verify':'تحقق بنفسك',
            'verify_intro':'افتح سجل الدليل الذي تستند إليه كل إجابة، أو انتقل إلى المصادر أو المنهجية.',
            'evidence':'افتح الأدلة',
            'data':_nav_label('/data/','ar'),
            'method':'المنهجية',
            'open_record':'افتح سجل الدليل ←',
            'do_not':'لا يُستنتج:',
            'visual_question':'السؤال التحليلي',
            'text_alternative':'البديل النصي التحليلي',
            'question_flow':'افهم ← استكشف ← تحقّق',
            'reading_rule':'قاعدة القراءة',
            'reading_rule_copy':'يبقى كل رقم جوهري مرتبطًا بوحدته ونطاقه وفترته وحدوده. ولا تعامل الأدلة ذات تواريخ القياس المختلفة كما لو كانت تصف اللحظة نفسها.',
            'start':'استكشف الأسئلة',
            'verify_action':'افتح الأدلة',
        }
    return {
        'scope':'Scope and time',
        'boundary':'What not to conclude',
        'unknown':'What remains unknown',
        'coverage':'Coverage limit',
        'visual':'A view that changes understanding',
        'more':'More evidence and context',
        'more_intro':'Additional controlled detail from this route, preserved with its original boundaries.',
        'measure':'What measurement would change the decision?',
        'verify':'Verify it yourself',
        'verify_intro':'Open the evidence record behind each answer, or go to the sources or the methodology.',
        'evidence':'Open evidence',
        'data':_nav_label('/data/','en'),
        'method':'Methodology',
        'open_record':'Open evidence record →',
        'do_not':'Do not infer:',
        'visual_question':'Analytical question',
        'text_alternative':'Analytical text alternative',
        'question_flow':'Understand → Explore → Verify',
        'reading_rule':'Reading rule',
        'reading_rule_copy':'Every consequential number stays attached to its unit, scope, time and limitation. Evidence measured at different times is never presented as if it described the same moment.',
        'start':'Explore questions',
        'verify_action':'Open evidence',
    }

def answer_question_crumb(spec,lang,labels):
    q=QUESTION_BY_ROUTE.get(str(spec.get('route') or ''))
    if not q:
        return f'<div class="eyebrow">{labels["question_flow"]}</div>'
    return (f'<nav class="answer-crumb eyebrow" aria-label="{esc(ui_text("UI-ANSWER-CRUMB-LABEL",lang))}"><a href="/{lang}/explore/">{esc(_nav_label("/explore/",lang))}</a>'
            f' <span aria-hidden="true">/</span> <span class="answer-question">{esc(locv(q,"question",lang))}</span></nav>')

def domain_hero(spec,lang):
    labels=_domain_labels(lang); rows=_localized_section_map(spec,lang)
    lead=_first_line((rows.get(1) or {}).get(f'body_{lang}'))
    title=locv(spec,'title',lang)
    return (
        f'<section class="hero domain-hero"><div class="hero-inner">'
        f'<div>{answer_question_crumb(spec,lang,labels)}<h1>{esc(title)}</h1><p class="hero-lead">{esc(lead)}</p>'
        f'<div class="hero-actions"><a class="button primary" href="/{lang}/explore/">{labels["start"]}</a>'
        f'<a class="button ghost" href="/{lang}/evidence/">{labels["verify_action"]}</a></div></div>'
        f'<aside class="hero-side"><div class="eyebrow">{labels["reading_rule"]}</div><p>{labels["reading_rule_copy"]}</p></aside>'
        f'</div></section>'
    )

def _band_kind(s):
    role=str(s.get('section_role') or '')
    low=role.lower()
    if 'does not establish' in low or 'لا يثبته' in role:
        return 'boundary'
    if 'know' in low or 'نعرف' in role:
        return 'unknown'
    return 'coverage'

def domain_scope_band(spec,lang,presentation):
    """P1.3: the band holds the page's always-visible boundaries (what the evidence does not establish, what remains
    unknown or the coverage limit). Each band section renders here once, in full, under its own governed heading;
    the presentation contract keeps band, primary and progressive tiers disjoint, so nothing is repeated below."""
    rows=_localized_section_map(spec,lang)
    items=[]
    for order in _presentation_section_orders(presentation.get('supporting')):
        s=rows.get(order) or {}
        if not s.get(f'body_{lang}'):
            continue
        items.append(f'<article class="scope-item {_band_kind(s)}" data-section-order="{order}"><h2 class="scope-label">{esc(s.get(f"heading_{lang}") or "")}</h2>{paras(s.get(f"body_{lang}"))}</article>')
    return f'<section class="domain-scope"><div class="container domain-scope-grid">{"".join(items)}</div></section>'

def _domain_section(lang,s,idx):
    h=s.get(f'heading_{lang}') or ''
    role=s.get('section_role') or ''
    role_low=str(role).lower()
    tone=' domain-boundary' if ('does not establish' in role_low or 'لا يثبته' in str(role)) else ''
    if 'measurement' in role_low or 'القياس' in str(role):
        tone+=' domain-measure'
    return (
        f'<section class="domain-section{tone}"><div class="container domain-reading-grid">'
        f'<div class="domain-section-kicker"><span>{idx:02d}</span><div class="eyebrow">{esc(role)}</div></div>'
        f'<div><h2>{esc(h)}</h2>{paras(s.get(f"body_{lang}"))}</div>'
        f'</div></section>'
    )

def _visual_scope(v,lang):
    """Scope line of a visual's text alternative. A visual that is also an Evidence Record takes its bilingual period
    and universe from that record (06), so both languages carry the same scope (P3). Otherwise English uses the contract's
    period and unit; Arabic shows only native Arabic scope and never English-only implementation metadata."""
    ev=EVIDENCE_OBJECT_BY_ID.get(str(v.get('visual_id')))
    if ev and ev.get(f'period_{lang}'):
        return ev.get(f'period_{lang}') or '', ev.get(f'universe_{lang}') or ''
    if v.get('period_ar'):
        # 11 carries a native Arabic period/universe for visuals without an Evidence Record (P3-D): both languages
        # then state period and universe.
        return (v.get('period_ar'), v.get('universe_ar') or '') if lang=='ar' else (v.get('period') or '', v.get('denominator_universe') or '')
    if lang=='ar':
        raw_period=v.get('source_period_ar') or ''
        if not raw_period:
            candidate=str(v.get('period') or v.get('source_period') or '')
            raw_period=candidate if candidate and not re.search(r'[A-Za-z]',candidate) else ''
        return raw_period, v.get('unit_or_object_ar') or ''
    return (v.get('period_en') or v.get('period') or v.get('source_period_en') or v.get('source_period') or ''), (v.get('unit_or_object_en') or v.get('unit_or_object') or '')

def _visual_fallback(lang,question,summary,prohibit,period='',unit=''):
    ar=lang=='ar'
    label='البديل النصي التحليلي' if ar else 'Analytical text alternative'
    qlabel='السؤال التحليلي' if ar else 'Analytical question'
    slabel='ما يوضحه الدليل' if ar else 'What the evidence shows'
    scope_label='النطاق والزمن' if ar else 'Scope and time'
    boundary_label='ما لا يُستنتج' if ar else 'What not to conclude'
    items=[]
    if question:
        items.append(f'<li><strong>{qlabel}:</strong> {esc(question)}</li>')
    if summary:
        items.append(f'<li><strong>{slabel}:</strong> <span class="visual-summary">{esc(summary)}</span></li>')
    scope=' · '.join(str(x) for x in (period,unit) if x)
    if scope:
        items.append(f'<li><strong>{scope_label}:</strong> {esc(scope)}</li>')
    if prohibit:
        items.append(f'<li><strong>{boundary_label}:</strong> {esc(prohibit)}</li>')
    return (
        f'<div class="visual-fallback" data-visual-fallback="ordered-text" data-image-independent="true" '
        f'data-noncolour-semantic="text-structure-label-position">'
        f'<div class="visual-fallback-label">{label}</div>'
        f'<ol class="visual-fallback-list">{"".join(items)}</ol></div>'
    )

def domain_visual(spec,lang,visual_id):
    labels=_domain_labels(lang)
    v=next((x for x in spec.get('governed_visual_contracts') or [] if x.get('visual_id')==visual_id),None)
    if not v:
        return ''
    title=locv(v,'title',lang)
    question=locv(v,'question',lang)
    summary=locv(v,'accessible_summary',lang) or locv(v,'decision_value',lang) or locv(v,'what_it_shows',lang)
    prohibit=locv(v,'prohibited_inference',lang)
    period,unit=_visual_scope(v,lang)
    oid=str(v.get('visual_id') or '')
    link=f'<a class="text-link" href="{route_href(DETAIL_ROUTES[oid],lang)}">{labels["open_record"]}</a>' if oid in DETAIL_ROUTES else ''
    fallback=_visual_fallback(lang,question,summary,prohibit,period,unit)   # scope and time are stated once, inside the text alternative (P1.3)
    return (
        f'<section class="domain-visual-section"><div class="container">'
        f'<div class="eyebrow">{labels["visual"]}</div>'
        f'<article class="domain-visual" data-visual-id="{esc(oid)}" data-image-independent="true" data-noncolour-semantic="text-structure-label-position"><div><h2>{esc(title)}</h2>{fallback}{link}</div>'
        f'</article>'
        f'</div></section>'
    )

def domain_measurement_next(spec,lang,limit):
    arr=(spec.get('governed_measurement_priorities') or [])[:max(0,int(limit or 0))]
    if not arr:
        return ''
    labels=_domain_labels(lang); cards=[]
    for m in arr:
        missing=locv(m,'missing_evidence',lang)
        unlocked=locv(m,'unlocked_decision',lang)
        unlock_html=f'<div class="measure-unlock">{esc(unlocked)}</div>' if unlocked else ''
        mid=str(m.get('measurement_id') or '')
        mlink=f'<a class="text-link" href="/{lang}/measurement/#{quote(mid)}">{esc(ui_text("UI-MA-OPEN",lang))}</a>' if mid else ''   # JRN-10
        cards.append(
            f'<article class="measure-next-card"><h3>{esc(locv(m,"title",lang))}</h3>'
            f'<p>{esc(missing)}</p>{unlock_html}{mlink}</article>'
        )
    return f'<section class="domain-measure-next"><div class="container"><div class="eyebrow">{labels["measure"]}</div><div class="measure-next-grid">{"".join(cards)}</div></div></section>'

def domain_more(spec,lang,progressive_orders):
    labels=_domain_labels(lang); rows=_localized_section_map(spec,lang)
    extra=[rows[o] for o in progressive_orders if o in rows]
    if not extra:
        return ''
    blocks=[]
    for s in extra:
        h=s.get(f'heading_{lang}') or ''
        role=s.get('section_role') or ''
        blocks.append(f'<article class="domain-more-item"><div class="eyebrow">{esc(role)}</div><h3>{esc(h)}</h3>{paras(s.get(f"body_{lang}"))}</article>')
    return (
        f'<section class="domain-more-section"><div class="container"><details class="domain-more">'
        f'<summary><span>{labels["more"]}</span><small>{labels["more_intro"]}</small></summary>'
        f'<div class="domain-more-list">{"".join(blocks)}</div></details></div></section>'
    )

def all_records_disclosure(spec,lang,label_id='UI-ANSWER-ALL-RECORDS'):
    items=bound_record_links(spec,lang)
    if not items:
        return ''
    return (f'<details class="all-records"><summary>{esc(ui_text(label_id,lang))} (<bdi>{len(items)}</bdi>)</summary>'
            f'<ul class="all-records-list">{"".join(items)}</ul></details>')

def domain_verify(spec,lang,presentation):
    labels=_domain_labels(lang); direct=[]
    wanted=set(_presentation_verify_ids(presentation.get('utility')))
    if wanted:
        candidates=(spec.get('governed_claims') or [])+(spec.get('governed_evidence_objects') or [])+(spec.get('governed_visual_contracts') or [])
        seen=set()
        for o in candidates:
            oid=o.get('claim_id') or o.get('evidence_object_id') or o.get('object_id') or o.get('visual_id')
            if not oid or oid not in wanted or oid in seen or oid not in DETAIL_ROUTES:
                continue
            seen.add(oid)
            title=locv(o,'headline',lang) or locv(o,'title',lang) or oid
            direct.append(f'<a href="{route_href(DETAIL_ROUTES[oid],lang)}"><span>{esc(title)}</span></a>')   # PID-1: descriptive label drives the link
    direct_html=''.join(direct)
    return (
        f'<section id="verify" class="domain-verify"><div class="container domain-verify-grid">'
        f'<div><h2>{labels["verify"]}</h2><p>{labels["verify_intro"]}</p></div>'
        f'<div class="verify-links">{direct_html}<a href="/{lang}/evidence/">{labels["evidence"]}</a>'
        f'<a href="/{lang}/data/">{labels["data"]}</a><a href="/{lang}/methodology/">{labels["method"]}</a>{all_records_disclosure(spec,lang)}</div>'
        f'</div></section>'
    )

def domain_readings(spec,lang):
    # PB-0426: governed Evidence Readings surfaced on a domain page (08 domain_surface_routes, at most two) and
    # related Readings linked from it (08 domain_context_routes). Titles and theses come from 08_READINGS.
    ar=lang=='ar'
    cards=[]
    for r in spec.get('governed_readings') or []:
        route=r.get('route') or ''
        cards.append(f'<article class="domain-reading-card" data-domain-reading="{esc(r.get("reading_id"))}"><div class="eyebrow">{"قراءة أدلة" if ar else "Evidence Reading"}</div>'
                     f'<h3><a href="{route_href(route,lang)}">{esc(locv(r,"title",lang))}</a></h3><p>{esc(locv(r,"thesis",lang))}</p></article>')
    links=''.join(f'<li><a href="{route_href(x.get("route"),lang)}">{esc(locv(x,"title",lang))}</a></li>' for x in spec.get('related_readings') or [])
    if not cards and not links:
        return ''
    head='قراءات الأدلة المرتبطة بهذه الصفحة' if ar else 'Evidence Readings on this question'
    rel=f'<div class="related-readings"><strong>{"قراءات ذات صلة" if ar else "Related readings"}</strong><ul>{links}</ul></div>' if links else ''
    return f'<section class="section domain-readings"><div class="container"><h2>{head}</h2><div class="domain-reading-grid">{"".join(cards)}</div>{rel}</div></section>'

def domain_page(spec,lang):
    presentation=PRESENTATION_ROUTES[spec.get('route')]
    rows=_localized_section_map(spec,lang)
    body=domain_hero(spec,lang)
    body+=domain_scope_band(spec,lang,presentation)
    primary_orders=_presentation_section_orders(presentation.get('primary'))
    progressive_orders=_presentation_section_orders(presentation.get('progressive'))
    visual_id,visual_after=_presentation_visual(presentation.get('primary'))
    primary=[rows[o] for o in primary_orders if o in rows]
    if primary:
        body+=f'<div class="domain-core" data-domain-family="{esc(presentation.get("presentation_family") or "domain-answer")}">'
        for idx,s in enumerate(primary,1):
            body+=_domain_section(lang,s,idx)
            if idx==visual_after and visual_id:
                body+=domain_visual(spec,lang,visual_id)
        body+='</div>'
    body+=domain_more(spec,lang,progressive_orders)
    if spec.get('route')=='/finance/':
        body+=chronology_block(lang)          # JRN-09: the chronology the page promises
    body+=domain_readings(spec,lang)
    body+=related_questions(spec,lang)       # JRN-12
    body+=domain_measurement_next(spec,lang,presentation.get('measurement_limit',0))
    body+=domain_verify(spec,lang,presentation)
    return body

def bound_record_links(spec,lang):
    # JRN-03: every record bound to a page, reachable from it (title-labelled; the reference is shown as such)
    items=[]; seen=set()
    for o in (spec.get('governed_claims') or [])+(spec.get('governed_evidence_objects') or [])+(spec.get('governed_visual_contracts') or []):
        oid=str(o.get('claim_id') or o.get('evidence_object_id') or o.get('object_id') or o.get('visual_id') or '')
        if not oid or oid in seen or oid not in DETAIL_ROUTES: continue
        seen.add(oid)
        ev=EVIDENCE_OBJECT_BY_ID.get(oid) or {}
        title=locv(ev,'title',lang) or locv(o,'headline',lang) or locv(o,'title',lang) or oid
        items.append(f'<li><a class="text-link" href="{route_href(DETAIL_ROUTES[oid],lang)}">{esc(title)}</a></li>')
    return items

def related_questions(spec,lang):
    route=str(spec.get('route') or '')
    targets=[]
    for r in SYSTEM_RELATIONSHIPS:
        a=_qroute(r.get('from')); t=_qroute(r.get('to'))
        if a==route and t!=route and t in SPEC_BY_ROUTE and t not in targets:
            targets.append(t)
    if not targets:
        return ''
    links=''.join(f'<li><a class="text-link" href="{route_href(t,lang)}">{esc(route_question_label(t,lang))}</a></li>' for t in targets)
    return (f'<section class="related-questions"><div class="container"><h2>{esc(ui_text("UI-RELATED-QUESTIONS",lang))}</h2>'
            f'<p>{esc(ui_text("UI-RELATED-QUESTIONS-NOTE",lang))}</p><ul class="related-question-list">{links}</ul></div></section>')

def chronology_block(lang):
    ar=lang=='ar'; items=[]
    for e in SYSTEM_CHRONOLOGY:
        fact=locv(e,'fact',lang); imp=locv(e,'fi_relevance',lang) or locv(e,'system_implication',lang); dne=locv(e,'does_not_establish',lang)
        if not fact: continue
        names=[]
        for sid in [x.strip() for x in str(e.get('source_ids') or '').split('|') if x.strip()]:
            s0=SOURCE_BY_ID.get(sid) or {}
            if sid in PUBLIC_SOURCE_IDS and public_locator(s0.get('primary_url')):
                t=(s0.get('display_title_ar') if ar else s0.get('display_title')) if s0.get('metadata_state')=='DISPLAY_READY' else ''
                label=esc(t) if t else '<bdi dir="ltr">'+esc(sid)+'</bdi>'
                names.append(f'<a class="text-link" href="/{lang}/data/?source={quote(sid)}#source-{quote(sid)}">{label}</a>')
        src=f'<p class="chronology-sources"><strong>{esc(ui_text("UI-CHRONOLOGY-SOURCES",lang))}</strong> {" · ".join(names)}</p>' if names else ''
        imp_html=f'<p><strong>{esc(ui_text("UI-CHRONOLOGY-RELEVANCE",lang))}</strong> {esc(imp)}</p>' if imp else ''
        dne_html=f'<p class="note"><strong>{esc(ui_text("UI-VIS-DOES-NOT-ESTABLISH",lang))}</strong> {esc(dne)}</p>' if dne else ''
        items.append(f'<li class="chronology-item" id="{esc(e.get("event_id"))}"><div class="chronology-period"><bdi>{esc(locv(e,"period",lang))}</bdi></div><div><p>{esc(fact)}</p>{imp_html}{dne_html}{src}</div></li>')
    if not items:
        return ''
    return (f'<section id="chronology" class="section chronology"><div class="container"><h2>{esc(ui_text("UI-CHRONOLOGY-H",lang))}</h2>'
            f'<p>{esc(ui_text("UI-CHRONOLOGY-INTRO",lang))}</p><ol class="chronology-list">{"".join(items)}</ol></div></section>')

def sections(spec,lang,exclude_orders=None):
    exclude_orders=set(exclude_orders or [])
    rows=[]; seen=set()
    for s in spec.get('sections',[]):
        if s.get('section_order') in exclude_orders: continue
        h=s.get(f'heading_{lang}'); b=s.get(f'body_{lang}')
        if not (h or b): continue
        key=(s.get('section_order'),h,b)
        if key in seen: continue
        seen.add(key); rows.append(s)
    out=[]
    n=0
    for i,s in enumerate(rows):
        h=s.get(f'heading_{lang}') or ''
        if i==0 and not h: continue
        n+=1                                  # P4: numbering counts the sections a reader sees (a heading-less lead is not numbered)
        tone=['','soft','mint','sand'][i%4]; role=s.get('section_role') or ''
        role_html=f'<div class="eyebrow">{esc(role)}</div>' if role else ''
        out.append(f'<section class="section {tone}"><div class="container section-grid"><div><div class="section-number">{n:02d}</div>{role_html}</div><div><h2>{esc(h)}</h2>{section_body(s,lang)}</div></div></section>')
    return ''.join(out)


def question_cards(lang, compact=False):
    qs=load(C/'content/questions.json'); ar=lang=='ar'
    if compact:
        chosen={'QE-002','QE-003','QE-005','QE-011'}
        qs=[q for q in qs if q.get('question_id') in chosen]
        eye='أسئلة شائعة للبدء' if ar else 'Common starting questions'
        title='ابدأ من المسألة التي تريد حسمها' if ar else 'Start from the problem you need to resolve'
        n=INVENTORY['entry_questions']
        more=f'اعرض الأسئلة كلها ({n})' if ar else f'View all {n} questions'
        cards=[]
        for q in qs:
            qid=str(q.get('question_id') or '')
            cards.append(
                f'<a class="question-card compact" data-question-id="{esc(qid)}" href="{question_href(q,lang)}">'
                f'<div><h3>{esc(locv(q,"question",lang))}</h3><p>{esc(locv(q,"user_gets",lang))}</p></div></a>'
            )
        return (
            f'<section class="section mint home-questions"><div class="container"><div class="section-title-row"><div>'
            f'<div class="eyebrow">{eye}</div><h2>{title}</h2></div>'
            f'<a class="text-link" href="/{lang}/explore/">{more} {"←" if ar else "→"}</a></div>'
            f'<div class="question-grid compact-grid">{"".join(cards)}</div></div></section>'
        )

    groups=[
      (('افهم الصورة العامة' if ar else 'Understand the wider picture'), {'QE-001','QE-003'}),
      (('الناس والاستخدام والتدفقات' if ar else 'People, use and flows'), {'QE-002','QE-004','QE-007','QE-009'}),
      (('المنشآت والمؤسسات ومقدمو الخدمات' if ar else 'Firms, institutions and providers'), {'QE-005','QE-006','QE-008'}),
      (('تحقّق وحدد ما ينبغي قياسه' if ar else 'Verify and decide what to measure'), {'QE-010','QE-011'})
    ]
    sections_out=[]
    for gtitle,ids in groups:
        rows=[x for x in qs if x.get('question_id') in ids]
        cards=[]
        for q in rows:
            qid=str(q.get('question_id') or '')
            cards.append(
                f'<a class="question-card" data-question-id="{esc(qid)}" href="{question_href(q,lang)}">'
                f'<div><h3>{esc(locv(q,"question",lang))}</h3><p>{esc(locv(q,"user_gets",lang))}</p></div></a>'
            )
        sections_out.append(
            f'<section class="question-cluster"><div class="question-cluster-head"><h3>{esc(gtitle)}</h3>'
            f'<span class="pill">{len(rows)}</span></div><div class="question-grid">{"".join(cards)}</div></section>'
        )
    eye='أسئلة للدخول إلى الأدلة' if ar else 'Questions into the evidence'
    # P1.3: the page hero already says "start with the question, not the dataset"; the list heading names the task instead.
    title='اعثر على السؤال الأقرب إلى قرارك' if ar else 'Find the question closest to your decision'
    intro=(
        'يحافظ كل مسار على الفترة، والمجتمع أو قاعدة الاحتساب، وحدود الاستنتاج، والمصدر.'
        if ar else
        'Every route keeps period, population or calculation base, inference limits and source visible.'
    )
    return (
        f'<section class="section mint explore-questions"><div class="container"><div class="eyebrow">{eye}</div>'
        f'<h2>{title}</h2><p class="section-intro">{intro}</p>{"".join(sections_out)}</div></section>'
    )

def _home_section(spec,lang,order,tone=''):
    row=next((s for s in spec.get('sections',[]) if s.get('section_order')==order and (s.get(f'heading_{lang}') or s.get(f'body_{lang}'))),None)
    if not row:
        return ''
    h=row.get(f'heading_{lang}') or ''
    b=row.get(f'body_{lang}') or ''
    role=row.get('section_role') or ''
    role_html=f'<div class="eyebrow">{esc(role)}</div>' if role else ''
    return (
        f'<section class="section {tone}"><div class="container section-grid"><div>{role_html}</div>'
        f'<div><h2>{esc(h)}</h2>{section_body(row,lang)}</div></div></section>'
    )

def question_href(q,lang):
    """JRN-15: a question whose answer page is Home opens at the part of Home that answers it."""
    r=str(q.get("primary_route") or "/")
    return route_href(r,lang)+("#system" if r.strip("/")=="" else "")

def home_special(spec,lang):
    # Question-first entry is the public organizing logic. Facts and visual semantics
    # are rendered from the governed Page Spec rather than duplicated in build.py.
    out=[question_cards(lang,compact=True)]
    out.append(_home_section(spec,lang,3,''))
    figs=all_records_disclosure(spec,lang,'UI-HOME-FIGURES-EVIDENCE')
    if figs: out.append(f'<section class="section home-figures-evidence"><div class="container">{figs}</div></section>')
    out.append(_home_section(spec,lang,4,'sand'))
    out.append(_home_section(spec,lang,5,'soft'))
    out.append(_home_section(spec,lang,6,''))
    out.append('<div id="system" tabindex="-1"></div>'+domain_visual(spec,lang,'VIS-INCLUSION-TRANSMISSION'))   # JRN-15: the system question lands here
    out.append(_home_section(spec,lang,7,'mint'))
    out.append(_home_section(spec,lang,8,''))
    return ''.join(out)

def home_ctas(lang):
    ar=lang=='ar'
    items=[
      ('/readings/',_nav_label('/readings/',lang),'تحليل متعدد المصادر يبقى مربوطًا بالخلاصات والأدلة.' if ar else 'Cross-source analysis that stays bound to claims and evidence.'),
      ('/measurement/',_nav_label('/measurement/',lang),'ما الذي لا نعرفه بعد، وما القياس الذي سيجعل القرار أقوى.' if ar else 'What remains unknown and what measurement would strengthen the decision.'),
      ('/data/',_nav_label('/data/',lang),'اعثر على المصادر الأصلية التي تستند إليها الأدلة، بعناوينها وجهاتها الناشرة وروابطها.' if ar else 'Find the original sources behind the evidence, with their titles, publishers and links.')
    ]
    cards=''.join(f'<a class="reading-card" href="{route_href(r,lang)}"><span class="badge teal">{i+1:02d}</span><h3>{esc(t)}</h3><p>{esc(d)}</p></a>' for i,(r,t,d) in enumerate(items))
    return f'<section class="section"><div class="container"><div class="reading-grid home-cta-grid">{cards}</div></div></section>'

def reading_cards(lang):
    arr=load(C/'content/readings.json'); ar=lang=='ar'; cards=[]
    for r in arr:
        label='قراءة مرتبطة بالأدلة ←' if ar else 'Evidence-bound reading →'
        cards.append(f'<a class="reading-card" href="{route_href(r["route"],lang)}"><h3>{esc(locv(r,"title",lang))}</h3><p>{esc(locv(r,"question",lang))}</p><div class="meta">{label}</div></a>')
    return f'<section class="section"><div class="container"><div class="reading-grid">{"".join(cards)}</div></div></section>'

AR_MEASUREMENT_DOMAIN_TERMS={
    'People':'الأفراد',
    'Payments':'المدفوعات',
    'Equity':'الإنصاف',
    'Firms':'المنشآت',
    'MSME':'المنشآت الصغرى والصغيرة والمتوسطة',
    'Providers':'مقدمو الخدمات',
    'Geography':'الجغرافيا',
    'Consumer protection':'حماية المستهلك',
    'Quality':'الجودة',
    'Identity':'الهوية',
    'Digital access':'الوصول الرقمي',
    'Credit infrastructure':'البنية التحتية للائتمان',
    'Social protection':'الحماية الاجتماعية',
    'Reforms':'الإصلاحات',
}
def measurement_domain_label(domain,lang):
    raw=str(domain or '').strip()
    if lang!='ar' or not raw:
        return raw
    return ' / '.join(AR_MEASUREMENT_DOMAIN_TERMS.get(part.strip(),part.strip()) for part in raw.split('/'))

def measurement_more(m,lang):
    rows=[]
    for f,uid in (('guardrail','UI-MA-GUARDRAIL'),('feasibility','UI-MA-FEASIBILITY'),('priority_basis','UI-MA-BASIS'),('what_changes','UI-MA-CHANGES')):
        v=locv(m,f,lang)
        if v: rows.append(f'<dt>{esc(ui_text(uid,lang))}</dt><dd>{esc(v)}</dd>')
    return f'<details class="measurement-more"><summary>{esc(ui_text("UI-MA-MORE",lang))}</summary><dl>{"".join(rows)}</dl></details>' if rows else ''

def measurement_cards(lang):
    arr=load(C/'content/measurement_agenda.json'); ar=lang=='ar'; cards=[]
    for m in arr:
        k1='ما نعرفه:' if ar else 'Current evidence:'; k2='ما ينقص:' if ar else 'Missing evidence:'; k3='ما الذي سيصبح القرار فيه أقوى:' if ar else 'Decision unlocked:'
        domain=measurement_domain_label(m.get('domain'),lang)
        mid=str(m.get('measurement_id') or '')
        cards.append(f'<article class="measurement-card" id="{esc(mid)}" tabindex="-1"><div class="priority">{("الأولوية" if ar else "Priority")}: <bdi dir="ltr">{esc(m.get("priority"))}</bdi> · {esc(domain)}</div><h3>{esc(locv(m,"title",lang))}</h3><p><strong>{k1}</strong> {esc(locv(m,"current_evidence",lang))}</p><p><strong>{k2}</strong> {esc(locv(m,"missing_evidence",lang))}</p><p><strong>{k3}</strong> {esc(locv(m,"unlocked_decision",lang))}</p><div class="meta-row">{public_ref(mid,lang)}</div>{measurement_more(m,lang)}</article>')
    return f'<section class="section"><div class="container"><div class="measurement-grid">{"".join(cards)}</div></div></section>'

def sources_block(spec,lang):
    # Reader-facing source blocks obey the same publication filter as Evidence Records and Data.
    # A source dependency with no public locator is not exposed merely because it exists in the Page Spec.
    rows=_public_source_rows(spec)
    if not rows: return ''
    ar=lang=='ar'; out=[]
    for sid,source,url in rows:
        # Locator-only sources have no governed title; the reference is already shown above the link, so the link is
        # named for its action instead of repeating the reference.
        title=(source.get('display_title_ar') if ar else source.get('display_title')) or ('افتح المصدر الأصلي ↗' if ar else 'Open original source ↗')
        pub=source_kind_line(source,lang)
        link=f'<a href="{esc(url)}" rel="noopener noreferrer" target="_blank">{esc(title)}</a>'
        data_href=f'/{lang}/data/?source={quote(sid)}#source-{quote(sid)}'
        data_label='سجل المصدر' if ar else 'Source record'
        trust=source_trust_controls(source,lang)
        out.append(f'<div class="source-card"><div class="source-id" dir="ltr">{esc(sid)}</div><strong dir="auto">{link}</strong><div class="meta" dir="auto">{esc(pub)}</div><a class="text-link" href="{esc(data_href)}">{data_label}</a>{trust}</div>')
    label='المصادر' if ar else 'Sources'
    return f'<aside class="answer-card sticky-aside"><div class="eyebrow">{label}</div>{"".join(out)}</aside>'

def render_visual(v,lang):
    ar=lang=='ar'; title=locv(v,'title',lang); question=locv(v,'question',lang); summary=locv(v,'accessible_summary',lang) or locv(v,'what_it_shows',lang); prohibit=locv(v,'prohibited_inference',lang)
    # Never expose English-only implementation metadata on an Arabic public visual.
    # Where a visual has a native localized scope/unit it may be shown; otherwise the governed
    # localized accessible summary carries the material scope without inventing a translation.
    period,unit=_visual_scope(v,lang)
    meta=''.join(f'<span class="pill">{esc(x)}</span>' for x in (period,unit) if x)
    meta_html=f'<div class="meta-row">{meta}</div>' if meta else ''
    fallback=_visual_fallback(lang,question,summary,prohibit,period,unit)
    return f'<article class="visual" data-visual-id="{esc(v.get("visual_id"))}" data-image-independent="true" data-noncolour-semantic="text-structure-label-position"><div class="visual-head"><div><h3>{esc(title)}</h3></div></div>{fallback}{meta_html}</article>'

def governed_block_groups(spec,lang,rt):
    records=governed_blocks({'governed_claims':spec.get('governed_claims'),'governed_evidence_objects':spec.get('governed_evidence_objects')},lang,show_ref=(rt=='/evidence'))
    visuals=governed_blocks({'governed_visual_contracts':spec.get('governed_visual_contracts')},lang)
    measures=governed_blocks({'governed_measurement_priorities':spec.get('governed_measurement_priorities')},lang)
    rec_h={'/measurement':'UI-MEASURE-REVEALING-RECORDS','/evidence':'UI-HUB-START-HERE'}.get(rt,'UI-RELATED-RECORDS')
    ma_h='UI-EXPLORE-CANNOT-ANSWER' if rt=='/explore' else 'UI-RELATED-MEASUREMENT'
    return [(h,g) for h,g in ((ui_text(rec_h,lang),records),('',visuals),(ui_text(ma_h,lang),measures)) if g]

def evidence_hub_index(lang):
    # JRN-17: the hub lists every public record, grouped by the answer page it serves (labelled with its question)
    groups={}; order=[]
    for oid,route in sorted(DETAIL_ROUTES.items()):
        if not route.startswith('/evidence/') or oid not in EVIDENCE_OBJECT_BY_ID: continue
        ev=EVIDENCE_OBJECT_BY_ID[oid]
        home=next((r for r in _object_public_routes(ev) if r in QUESTION_BY_ROUTE and r!='/evidence/'),'')
        if home not in groups: groups[home]=[]; order.append(home)
        groups[home].append(f'<li><a class="text-link" href="{route_href(route,lang)}">{esc(locv(ev,"title",lang) or oid)}</a></li>')
    order.sort(key=lambda r:(r=='', str(QUESTION_BY_ROUTE.get(r,{}).get('question_id') or 'ZZ')))
    blocks=''.join(f'<details class="hub-group"><summary>{esc(route_question_label(r,lang) if r else ui_text("UI-HUB-OTHER",lang))} (<bdi>{len(groups[r])}</bdi>)</summary><ul>{"".join(groups[r])}</ul></details>' for r in order)
    return f'<section class="section hub-index"><div class="container"><h2>{esc(ui_text("UI-HUB-ALL-RECORDS",lang))}</h2>{blocks}</div></section>'

def governed_blocks(spec,lang,show_ref=False):
    # PID-1: cards lead with the governed headline. A labelled record reference is shown only in the Evidence
    # directory (show_ref), where readers look up a record cited elsewhere by its reference.
    ar=lang=='ar'; out=[]; seen=set()
    open_label='افتح سجل الدليل ←' if ar else 'Open evidence record →'
    for c in spec.get('governed_claims') or []:
        oid=str(c.get('claim_id') or '')
        if not oid or oid in seen: continue
        seen.add(oid)
        label='لا يثبت:' if ar else 'Does not establish:'
        title=locv(c,'headline',lang); copy=locv(c,'copy',lang); boundary=locv(c,'does_not_prove',lang)
        if not (title or copy or boundary): continue
        note=f'<div class="note"><strong>{label}</strong> {esc(boundary)}</div>' if boundary else ''
        link=f'<div class="card-actions"><a class="text-link" href="{route_href(DETAIL_ROUTES[oid],lang)}">{open_label}</a></div>' if oid in DETAIL_ROUTES else ''
        ref=f'<div class="meta-row">{public_ref(oid,lang)}</div>' if show_ref else ''
        out.append(f'<article class="answer-card"><h3>{esc(title)}</h3><p>{esc(copy)}</p>{note}{link}{ref}</article>')
    for e in spec.get('governed_evidence_objects') or []:
        oid=str(e.get('evidence_object_id') or e.get('object_id') or '')
        if not oid or oid in seen: continue
        title=locv(e,'title',lang) or oid
        desc=locv(e,'summary',lang) or locv(e,'public_summary',lang) or locv(e,'what_it_establishes',lang) or locv(e,'meaning',lang)
        boundary=_boundary_parts(e,lang)[0] or locv(e,'limitation',lang)
        if not (desc or boundary):
            continue
        seen.add(oid)
        note=f'<div class="note">{esc(boundary)}</div>' if boundary else ''
        link=f'<div class="card-actions"><a class="text-link" href="{route_href(DETAIL_ROUTES[oid],lang)}">{open_label}</a></div>' if oid in DETAIL_ROUTES else ''
        ref=f'<div class="meta-row">{public_ref(oid,lang)}</div>' if show_ref else ''
        out.append(f'<article class="answer-card"><h3>{esc(title)}</h3><p>{esc(desc)}</p>{note}{link}{ref}</article>')
    for v in spec.get('governed_visual_contracts') or []:
        oid=str(v.get('visual_id') or '')
        if oid and oid not in seen:
            seen.add(oid); out.append(render_visual(v,lang))
    for m in spec.get('governed_measurement_priorities') or []:
        oid=str(m.get('measurement_id') or '')
        if not oid or oid in seen: continue
        seen.add(oid)
        need='الدليل المطلوب:' if ar else 'Evidence needed:'
        mlink=f'<div class="card-actions"><a class="text-link" href="/{lang}/measurement/#{quote(oid)}">{esc(ui_text("UI-MA-OPEN",lang))}</a></div>'
        out.append(f'<article class="answer-card boundary"><h3>{esc(locv(m,"title",lang))}</h3><p>{esc(locv(m,"current_evidence",lang))}</p><p><strong>{need}</strong> {esc(locv(m,"missing_evidence",lang))}</p>{mlink}</article>')
    return ''.join(out)

def _evidence_labels(lang):
    if lang=='ar':
        return {
            'family':'سجل الدليل',
            'establishes':'ما الذي يثبته هذا الدليل؟',
            'measures':'ما الذي يقيسه؟',
            'applies':'على من أو ماذا ينطبق؟',
            'period':'متى قيس أو رُصد؟',
            'currentness':'حداثة الدليل',
            'boundary':'ما لا يُستنتج',
            'source':'المصدر الأصلي والتحقق',
            'source_intro':'افتح سجل المصدر هنا، أو انتقل إلى الرابط الأصلي حين تسمح حالة النشر بذلك.',
            'open_original':'افتح المصدر الأصلي ↗',
            'open_source_record':'افتح سجل المصدر',
            'no_public_locator':'لا يتوافر رابط عام مستقل لهذا الاعتماد ضمن حالة النشر الحالية.',
            'no_source_record':'لا يرتبط هذا السجل حاليًا بمسار عام مستقل إلى مصدر أصلي؛ استخدم المنهج وطريقة التحقق أدناه.',
            'related':'عد إلى التفسير',
            'related_intro':'ارجع إلى السؤال أو الصفحة التي تستخدم هذا الدليل في سياقه التحليلي.',
            'evidence_hub':_nav_label('/evidence/','ar'),
            'data':'البيانات والمصادر',
            'methodology':'المنهجية',
            'more':'المنهج وطريقة التحقق',
            'more_intro':'تفاصيل إضافية تساعد على إعادة إنتاج القراءة أو تحديها من دون تغيير معنى الدليل.',
            'method':'كيف أُنتج؟',
            'change_trigger':'متى يتغير هذا السجل؟',
            'verification':'كيف أتحقق منه؟',
            'reading_guidance':'كيف يُقرأ هذا السجل؟',
            'reference':'المعرّف المرجعي',
            'report':'أبلغ عن مشكلة',
            'source_dependents':'سجلات أدلة تستخدم هذا المصدر',
            'open_record':'افتح سجل الدليل',
            'citation':'استشهد بهذا السجل',
            'reuse':'الاستشهاد وإعادة الاستخدام',
            'reuse_note':'الاستشهاد بالدليل لا يعني تلقائيًا امتلاك حق إعادة نشر ملف المصدر أو جدوله أو رسمه. افحص المصدر الأصلي وشروطه قبل إعادة توزيع مادته.',
            'trace':'مسار التحقق من المصدر',
            'trace_intro':'يبقى معرّف السجل مرتبطًا بالمصادر الأصلية التي تسمح حالة النشر بعرضها. ولا تُستكمل البيانات الوصفية الناقصة بالافتراض.',
            'history':'التصحيحات وسجل الإصدارات',
            'source_citation':'انسخ مرجع المصدر',
            'source_reuse_unknown':'لا يثبت سجل المصدر هذا إذنًا بإعادة نشر الملف أو الجدول أو الرسم الأصلي. تحقّق من شروط المصدر قبل إعادة التوزيع.',
        }
    return {
        'family':'Evidence record',
        'establishes':'What does this evidence establish?',
        'measures':'What does it measure?',
        'applies':'Who or what does it apply to?',
        'period':'When was it measured or observed?',
        'currentness':'How current is it?',
        'boundary':'What not to conclude',
        'source':'Original source and verification',
        'source_intro':'Open the source record here, or follow the original locator when publication state allows it.',
        'open_original':'Open original source ↗',
        'open_source_record':'Open source record',
        'no_public_locator':'No standalone public locator is available for this dependency in the current publication state.',
        'no_source_record':'This record currently has no standalone public path to an original source; use the method and verification detail below.',
        'related':'Return to interpretation',
        'related_intro':'Return to the question or page that uses this evidence in its analytical context.',
        'evidence_hub':_nav_label('/evidence/','en'),
        'data':'Data & sources',
        'methodology':'Methodology',
        'more':'Method and verification detail',
        'more_intro':'Additional detail for reproducing or challenging the reading without changing the evidence meaning.',
        'method':'How was it produced?',
        'change_trigger':'When does this record change?',
        'verification':'How can I verify it?',
        'reading_guidance':'How should this record be read?',
        'reference':'Reference ID',
        'report':'Report an issue',
        'source_dependents':'Evidence records using this source',
        'open_record':'Open evidence record',
        'citation':'Cite this record',
        'reuse':'Citation and reuse',
        'reuse_note':'Citing the evidence does not automatically grant permission to republish an original source file, table or chart. Check the original source and its terms before redistributing source material.',
        'trace':'Source verification path',
        'trace_intro':'The stable record ID stays linked to original sources that the publication state permits this product to expose. Missing bibliography is not filled by assumption.',
        'history':'Corrections & release history',
        'source_citation':'Copy source reference',
        'source_reuse_unknown':'This source record does not establish permission to republish the original file, table or chart. Check source-specific terms before redistribution.',
    }

def _evidence_object(spec):
    arr=spec.get('governed_evidence_objects') or []
    return arr[0] if arr else {}

def _evidence_contract_fields(tier):
    return [str(x) for x in (EVIDENCE_PRESENTATION.get(tier) or []) if x]

def _object_public_routes(obj):
    routes=obj.get('public_route_list')
    if isinstance(routes,list):
        raw=routes
    else:
        raw=str(obj.get('public_routes') or '').split('|')
    out=[]
    for route in raw:
        route=str(route or '').strip()
        if not route:
            continue
        if not route.startswith('/'):
            route='/'+route
        if not route.endswith('/'):
            route+='/'
        if route not in out:
            out.append(route)
    return out

def _public_source_rows(spec):
    out=[]
    seen=set()
    for ref in spec.get('source_references') or []:
        sid=str(ref.get('source_id') or '').strip()
        if not sid or sid in seen:
            continue
        seen.add(sid)
        controlled=SOURCE_BY_ID.get(sid) or ref
        url=public_locator(controlled.get('primary_url') or ref.get('primary_url'))
        if sid in PUBLIC_SOURCE_IDS and url:
            out.append((sid,controlled,url))
    return out

def _closure_for_object(oid):
    # PB-0004: an Evidence Record shows only its own object-level lineage; no cross-type fallback.
    return SOURCE_CLOSURE_BY_KEY.get(('evidence_object',str(oid or ''))) or {}

# Lineage state -> governed statement shown instead of (or beside) source cards (PB-0004/PB-0006/PB-0008).
def _lineage_statement(closure):
    state=closure.get('closure_state')
    return {'PARTIALLY_RESOLVED':'UI-VERIFY-PARTIAL','COMPOSITE_OF_OBJECTS':'UI-VERIFY-COMPOSITE',
            'COMPOSITE_MEMBERS_NOT_LISTED':'UI-VERIFY-COMPOSITE-UNLISTED','SOURCE_NOT_YET_BOUND':'UI-EVID-UNBOUND',
            'FRAMING_NO_FACT':'UI-EVID-FRAMING'}.get(state)

def _boundary_parts(obj,lang):
    """P4.3: part A (what the evidence does not establish) and part B (the limit of the measure, when recorded).
    The generator derives both from 06 limitations_* split at its authored delimiter; objects that are not 06 records
    fall back to their single boundary field as part A."""
    a=locv(obj,'does_not_establish',lang)
    b=obj.get(f'measurement_limitation_{lang}') or ''
    if not a:
        raw=locv(obj,'limitations',lang)
        a,b=(raw.split(' | ',1)+[''])[:2] if ' | ' in raw else (raw,'')
    return a.strip(),b.strip()

def _cite_clause(label,value,sep=': '):
    v=str(value or '').strip().rstrip('.').rstrip('؛').strip()
    return f'{label}{sep}{v}.' if v else ''

def evidence_citation_context(spec,obj,lang):
    """Tranche C (TOOL-14/JRN-19/VER-07): a citation names the resource, the author, the content version and the original
    sources by title, carries the record's scope and limit, and never doubles punctuation."""
    oid=str(obj.get('evidence_object_id') or obj.get('object_id') or '')
    title=(locv(obj,'title',lang) or locv(spec,'title',lang) or oid).strip().rstrip('.')
    period=locv(obj,'period',lang)
    universe=locv(obj,'universe',lang)
    limitation,measure_limit=_boundary_parts(obj,lang)
    closure=_closure_for_object(oid)
    bound=closure.get('closure_state') in ('CLOSED_TO_SOURCE_ID','PARTIALLY_RESOLVED')
    own=set(closure.get('resolved_source_ids') or [])
    source_ids=[sid for sid,_,_ in _public_source_rows(spec) if sid in own] if bound else []
    ar=lang=='ar'
    names=[]
    for sid in source_ids:
        s0=SOURCE_BY_ID.get(sid) or {}
        t=(s0.get('display_title_ar') if ar else s0.get('display_title')) if s0.get('metadata_state')=='DISPLAY_READY' else ''
        pub=(s0.get('publisher_ar') if ar else None) or s0.get('publisher') or ''
        ref=f'{pub}؛ {sid}' if ar and pub else (f'{pub}; {sid}' if pub else sid)
        names.append(f'{t} ({ref})' if t else (f'مرجع المصدر {sid}' if ar else f'source reference {sid}'))
    product=ui_text('UI-PRODUCT-NAME',lang); version=ui_text('UI-CONTENT-VERSION',lang)
    if ar:
        parts=[f'{title}.', f'{product}، سجل الدليل {oid}. CauseWay. {version}.',
               _cite_clause('الفترة',period), _cite_clause('المجتمع أو قاعدة الاحتساب',universe),
               _cite_clause('ما لا يُستنتج',limitation), _cite_clause(ui_text('UI-EVID-MEASUREMENT-LIMITS','ar'),measure_limit),
               _cite_clause('المصادر الأصلية','؛ '.join(names)),
               'وتبقى الجهات الناشرة الأصلية المرجع لمادتها.']
    else:
        parts=[f'{title}.', f'{product}, Evidence Record {oid}. CauseWay. {version}.',
               _cite_clause('Period',period), _cite_clause('Population or base',universe),
               _cite_clause('What not to conclude',limitation), _cite_clause(ui_text('UI-EVID-MEASUREMENT-LIMITS','en'),measure_limit),
               _cite_clause('Original sources','; '.join(names)),
               'Original publishers remain authoritative for their material.']
    return ' '.join(p for p in parts if p)

def evidence_trace(spec,obj,lang):
    labels=_evidence_labels(lang)
    oid=str(obj.get('evidence_object_id') or obj.get('object_id') or '')
    closure=_closure_for_object(oid)
    resolved=[str(x) for x in (closure.get('resolved_source_ids') or []) if str(x) in SOURCE_BY_ID]
    visible=[sid for sid in resolved if sid in PUBLIC_SOURCE_IDS and public_locator(SOURCE_BY_ID[sid].get('primary_url'))]
    if not visible:
        return ''
    rows=[]
    for sid in visible:
        data_href=f'/{lang}/data/?source={quote(sid)}#source-{quote(sid)}'
        rows.append(f'<a class="evidence-trace-step" href="{esc(data_href)}"><span class="source-id" dir="ltr">{esc(sid)}</span></a>')
    return (
        f'<section class="evidence-trace-section" data-source-reference-closure="{esc(oid)}"><div class="container evidence-trace-grid">'
        f'<div><h2>{labels["trace"]}</h2><p>{labels["trace_intro"]}</p></div>'
        f'<div class="evidence-trace-steps"><div class="evidence-trace-record"><strong class="stable-id" dir="ltr">{esc(oid)}</strong></div><span aria-hidden="true">{"←" if lang=="ar" else "→"}</span>{"".join(rows)}</div>'
        f'</div></section>'
    )

def source_kind_line(source,lang):
    """Publisher, kind of document and document date in the reader's language (Tranche C TC-B; governed 15 fields)."""
    ar=lang=='ar'
    pub=(source.get('publisher_ar') if ar else None) or source.get('publisher') or ''
    kind=(source.get('document_label_ar') if ar else source.get('document_label')) or ''
    date=source_date_text(source.get('document_date'),lang)
    return ' · '.join(x for x in [str(pub),str(kind),date] if x)

_MONTHS_EN=['January','February','March','April','May','June','July','August','September','October','November','December']
_MONTHS_AR=['يناير','فبراير','مارس','أبريل','مايو','يونيو','يوليو','أغسطس','سبتمبر','أكتوبر','نوفمبر','ديسمبر']
def source_date_text(value,lang):
    # ISO date, year-month or year from 15 document_date, written out in the reader's language; digits stay Western.
    v=str(value or '').strip()
    m=re.fullmatch(r'(\d{4})(?:-(\d{2}))?(?:-(\d{2}))?',v)
    if not m: return v
    y,mo,d=m.groups(); months=_MONTHS_AR if lang=='ar' else _MONTHS_EN
    if not mo: return y
    name=months[int(mo)-1]
    return f'{int(d)} {name} {y}' if d else f'{name} {y}'

def source_trust_controls(source,lang,compact=False):
    # P2.3: rights govern redistribution, never truthful outbound citation. On the source directory each card shows its
    # own reuse-terms state (a governed per-source state); the explanation is given once for the whole directory.
    labels=_evidence_labels(lang)
    sid=str(source.get('source_id') or '')
    url=public_locator(source.get('primary_url'))
    ar=lang=='ar'
    # A locator-only source has no governed title: cite it by reference and locator, never by repeating the reference
    # as if it were a title, and never by inventing bibliography (source_reference_map citation_behavior).
    display=(source.get('display_title_ar') if ar else source.get('display_title')) or ''
    cite_payload=' · '.join(x for x in [display,sid,url] if x)
    note=''
    if source.get('rights_display_state')=='OBJECT_LEVEL_OR_UNSPECIFIED':
        if compact:
            state=('شروط إعادة الاستخدام: غير مقيّمة' if ar else 'Reuse terms: not assessed') if source.get('rights_state')=='NOT_ASSESSED' else ('شروط إعادة الاستخدام: غير محددة' if ar else 'Reuse terms: not stated')
            note=f'<p class="source-rights-state" data-rights-state="{esc(source.get("rights_state") or "")}">{esc(state)}</p>'
        else:
            note=f'<p class="source-rights-note">{esc(labels["source_reuse_unknown"])}</p>'
    button=f'<button type="button" class="text-button" data-source-cite data-source-citation="{esc(cite_payload)}">{labels["source_citation"]}</button>' if url else ''
    return f'<div class="source-trust-controls">{button}{note}</div>'

def _evidence_field_card(label,value,kind=''):
    if not value:
        return ''
    return f'<article class="evidence-fact {kind}"><div class="evidence-fact-label">{esc(label)}</div><p>{esc(value)}</p></article>'

def evidence_record_hero(spec,obj,lang):
    labels=_evidence_labels(lang)
    oid=str(obj.get('evidence_object_id') or obj.get('object_id') or '')
    title=locv(obj,'title',lang) or locv(spec,'title',lang) or oid
    summary=locv(obj,'summary',lang)
    section1=next((x for x in spec.get('sections',[]) if x.get('section_order')==1 and x.get(f'body_{lang}')),None)
    lead=(section1 or {}).get(f'body_{lang}') or summary
    # P1.3: the summary is stated once, under "What does this evidence establish?"; a lead identical to it is not repeated.
    same=' '.join(str(lead or '').split())==' '.join(str(summary or '').split())
    lead_html='' if same else f'<p class="evidence-record-lead">{esc(lead)}</p>'
    crumbs=breadcrumb('Evidence Record',oid,lang)
    return (
        f'<section class="evidence-record-hero" data-evidence-family="Evidence Record" data-evidence-contract="Evidence Record">'
        f'<div class="container">{crumbs}<div class="evidence-record-hero-grid"><div><div class="eyebrow">{labels["family"]}</div>'
        f'<h1>{esc(title)}</h1>{lead_html}</div>'
        f'<aside class="evidence-record-summary"><div class="eyebrow">{labels["establishes"]}</div><p>{esc(summary)}</p></aside>'
        f'</div></div></section>'
    )

def evidence_scope_band(obj,lang):
    labels=_evidence_labels(lang)
    supporting=set(_evidence_contract_fields('supporting'))
    cards=[]
    if 'definition' in supporting:
        cards.append(_evidence_field_card(labels['measures'],locv(obj,'definition',lang),'definition'))
    if 'universe' in supporting:
        cards.append(_evidence_field_card(labels['applies'],locv(obj,'universe',lang),'universe'))
    if 'period' in supporting:
        cards.append(_evidence_field_card(labels['period'],locv(obj,'period',lang),'period'))
    if 'currentness' in supporting:
        cards.append(_evidence_field_card(labels['currentness'],locv(obj,'currentness',lang),'currentness'))
    return f'<section class="evidence-scope-band"><div class="container evidence-scope-grid">{"".join(cards)}</div></section>'

def evidence_boundary(obj,lang):
    labels=_evidence_labels(lang)
    required=set(_evidence_contract_fields('always_visible_boundaries'))
    if 'limitations' not in required:
        return ''
    limitation,measure_limit=_boundary_parts(obj,lang)
    if not limitation:
        return ''
    # P4.3: the two ideas stay separately understandable: A always, B when recorded, each under its governed label.
    part_b=(f'<div class="evidence-boundary-part" data-boundary-part="measurement-limits"><div class="eyebrow">{esc(ui_text("UI-EVID-MEASUREMENT-LIMITS",lang))}</div>'
            f'<p>{esc(measure_limit)}</p></div>') if measure_limit else ''
    return (f'<section class="evidence-boundary-band" data-evidence-boundary-first-load><div class="container"><div class="evidence-boundary-card">'
            f'<div class="evidence-boundary-part" data-boundary-part="does-not-establish"><div class="eyebrow">{esc(ui_text("UI-EVID-DOES-NOT-ESTABLISH",lang))}</div><p>{esc(limitation)}</p></div>'
            f'{part_b}</div></div></section>')

def evidence_sources(spec,lang):
    labels=_evidence_labels(lang); ar=lang=='ar'; cards=[]; suppressed_count=0
    for ref in spec.get('source_references') or []:
        sid=str(ref.get('source_id') or '').strip()
        if not sid:
            continue
        controlled=SOURCE_BY_ID.get(sid) or ref
        url=public_locator(controlled.get('primary_url') or ref.get('primary_url'))
        state=controlled.get('metadata_state') or ref.get('metadata_state')
        if sid not in PUBLIC_SOURCE_IDS or not url:
            suppressed_count+=1
            continue
        data_href=f'/{lang}/data/?source={quote(sid)}#source-{quote(sid)}'
        if state=='DISPLAY_READY':
            title=(controlled.get('display_title_ar') if ar else controlled.get('display_title')) or sid
            publisher=source_kind_line(controlled,lang)
            meta=f'<div class="meta" dir="auto">{esc(publisher)}</div>' if publisher else ''
            head=f'<strong dir="auto">{esc(title)}</strong>{meta}'
        else:
            # Tranche C TRUST-01: a source without a governed title is never named by its reference; the reference is shown as such.
            head=f'<strong>{esc(ui_text("UI-SOURCE-UNTITLED",lang))}</strong><div class="meta">{esc(ui_text("UI-SOURCE-REFERENCE",lang))} <bdi dir="ltr">{esc(sid)}</bdi></div>'
        cards.append(
            f'<article class="evidence-source-item" data-evidence-source="{esc(sid)}">{head}'
            f'<div class="evidence-source-actions"><a class="text-link" href="{esc(data_href)}">{labels["open_source_record"]}</a>'
            f'<a class="text-link" href="{esc(url)}" rel="noopener noreferrer" target="_blank">{labels["open_original"]}</a></div>'
            f'{source_trust_controls(controlled,lang)}</article>'
        )
    closure=_closure_for_object(spec.get('instance_id'))
    statement=_lineage_statement(closure)
    # P15-F2: a bound source without a public locator is never silently dropped; it is named by reference.
    bound_ids=[str(x) for x in (closure.get('resolved_source_ids') or [])]
    no_locator=[sid for sid in bound_ids if not public_locator((SOURCE_BY_ID.get(sid) or {}).get('primary_url'))]
    if cards and no_locator:          # stated, never named: the publication firewall keeps locator-less sources off public pages
        cards.append(f'<div class="evidence-source-note" data-evidence-sources-without-locator><p>{esc(ui_text("UI-EVID-SOURCES-WITHOUT-LOCATOR",lang))}</p></div>')
    members=[m for m in (closure.get('resolved_via_object_ids') or []) if m in DETAIL_ROUTES]
    if members:
        def _mtitle(m):
            ms=SPEC_BY_ROUTE.get(DETAIL_ROUTES[m]) or {}
            return locv(ms,'title',lang) or m
        links=''.join(f'<li><a class="text-link" href="{route_href(DETAIL_ROUTES[m],lang)}">{esc(_mtitle(m))}</a> {public_ref(m,lang)}</li>' for m in members)
        cards.append(f'<article class="evidence-source-item" data-evidence-members><strong>{esc(ui_text("UI-EVID-MEMBERS-HEADING",lang))}</strong><ul class="evidence-member-list">{links}</ul></article>')
    if statement:
        cards.append(f'<div class="evidence-lineage-statement" data-lineage-state="{esc(closure.get("closure_state"))}"><p>{esc(ui_text(statement,lang))}</p></div>')
    elif not cards:
        message=labels['no_public_locator'] if suppressed_count else labels['no_source_record']
        cards.append(f'<div class="empty evidence-source-empty" data-evidence-source-unavailable>{esc(message)}</div>')
    return (
        f'<section id="source" class="evidence-source-section"><div class="container evidence-source-grid">'
        f'<div><h2>{labels["source"]}</h2><p>{labels["source_intro"]}</p></div>'
        f'<div class="evidence-source-list">{"".join(cards)}</div></div></section>'
    )

def evidence_related(obj,lang):
    labels=_evidence_labels(lang); links=[]
    oid=str(obj.get('object_id') or obj.get('evidence_object_id') or '')
    for route in _object_public_routes(obj):
        if route.startswith('/evidence/'):
            continue
        title=route_question_label(route,lang)
        if title:
            links.append(f'<a class="evidence-context-link" href="{route_href(route,lang)}"><span>{esc(title)}</span></a>')
    for r in READINGS_ALL:                      # Readings that rely on this record (JRN-02)
        binds=set(str(x) for x in (r.get('claim_bindings') or [])+(r.get('evidence_bindings') or []))
        if oid in binds and r.get('route'):
            links.append(f'<a class="evidence-context-link" href="{route_href(r["route"],lang)}"><span>{esc(locv(r,"title",lang))}</span></a>')
    links.append(f'<a class="evidence-context-link utility" href="/{lang}/evidence/">{labels["evidence_hub"]}</a>')
    links.append(f'<a class="evidence-context-link utility" href="/{lang}/data/">{labels["data"]}</a>')
    links.append(f'<a class="evidence-context-link utility" href="/{lang}/methodology/">{labels["methodology"]}</a>')
    return (
        f'<section class="evidence-related-section"><div class="container evidence-related-grid">'
        f'<div><h2>{labels["related"]}</h2><p>{labels["related_intro"]}</p></div>'
        f'<nav class="evidence-context-links" aria-label="{esc(labels["related"])}">{"".join(links)}</nav></div></section>'
    )

def evidence_progressive(spec,obj,lang):
    labels=_evidence_labels(lang); allowed=set(_evidence_contract_fields('progressive')); blocks=[]
    mapping=[('method','method'),('change_trigger','change_trigger'),('verification','verification')]
    for key,label_key in mapping:
        if key not in allowed:
            continue
        value=locv(obj,key,lang)
        if key=='method' and obj.get('visual_contract_state'):
            continue          # PB-0401: draft encoding notes are not rendered while no governed contract exists
        if key=='verification':
            st=_lineage_statement(_closure_for_object(obj.get('evidence_object_id') or obj.get('object_id')))
            if st and value==ui_text(st,lang):
                continue          # already shown in the source section (Stage 1)
        if value:
            blocks.append(f'<article class="evidence-more-item"><h3>{labels[label_key]}</h3><p>{esc(value)}</p></article>')
    if 'page_reading_guidance' in allowed:
        s2=next((x for x in spec.get('sections',[]) if x.get('section_order')==2 and x.get(f'body_{lang}')),None)
        if s2:
            blocks.append(f'<article class="evidence-more-item"><h3>{labels["reading_guidance"]}</h3><p>{esc(s2.get(f"body_{lang}"))}</p></article>')
    if not blocks:
        return ''
    return (
        f'<section class="evidence-more-section"><div class="container"><details class="evidence-more">'
        f'<summary><span>{labels["more"]}</span><small>{labels["more_intro"]}</small></summary>'
        f'<div class="evidence-more-list">{"".join(blocks)}</div></details></div></section>'
    )

def evidence_utility(spec,obj,lang):
    labels=_evidence_labels(lang); oid=str(obj.get('evidence_object_id') or obj.get('object_id') or '')
    if not oid:
        return ''
    utility=set(_evidence_contract_fields('utility'))
    actions=[]
    if 'citation' in utility:
        actions.append(f'<button type="button" class="button ghost evidence-cite-button" data-cite>{labels["citation"]}</button>')
    if 'reuse' in utility:
        actions.append(f'<a class="button ghost" href="/{lang}/rights/">{labels["reuse"]}</a>')   # TOOL-21: citation and reuse guidance, not the top of Data
    if 'corrections' in utility:
        actions.append(f'<a class="button ghost" href="/{lang}/corrections/?record={quote(oid)}">{labels["history"]}</a>')
    if 'report_issue' in utility:
        actions.append(f'<a class="button ghost" href="/{lang}/contact/?record={quote(oid)}">{labels["report"]}</a>')
    return (
        f'<section class="evidence-utility" data-record-id="{esc(oid)}"><div class="container">'
        f'<div class="evidence-utility-inner"><div><span>{labels["reference"]}</span><strong class="stable-id" dir="ltr">{esc(oid)}</strong></div>'
        f'<div class="evidence-utility-actions">{"".join(actions)}</div></div>'
        f'<p class="evidence-reuse-note">{esc(labels["reuse_note"])}</p>'
        f'</div></section>'
    )

def evidence_record_page(spec,lang):
    obj=_evidence_object(spec)
    if not obj:
        return ''
    body=evidence_record_hero(spec,obj,lang)
    body+=evidence_scope_band(obj,lang)
    body+=evidence_boundary(obj,lang)
    body+=evidence_sources(spec,lang)
    body+=evidence_trace(spec,obj,lang)
    body+=evidence_related(obj,lang)
    body+=evidence_progressive(spec,obj,lang)
    body+=evidence_utility(spec,obj,lang)
    return body

def compare_block(lang):
    ar=lang=='ar'
    spec=next((o for o in SPECS if o.get('route')=='/evidence/compare/'),{})
    claims={}
    for x in spec.get('governed_claims') or []:
        oid=str(x.get('claim_id') or x.get('object_id') or '')
        if oid: claims[oid]=x
    evidence={}
    order=[]
    for x in spec.get('governed_evidence_objects') or []:
        oid=str(x.get('evidence_object_id') or x.get('object_id') or '')
        if oid and oid not in order: order.append(oid)
        if oid: evidence[oid]=x
    for oid in claims:
        if oid not in order: order.append(oid)
    records=[]
    for oid in order:
        ev=evidence.get(oid) or {}
        cl=claims.get(oid) or {}
        title=locv(ev,'title',lang) or locv(cl,'headline',lang) or oid
        detail_route=DETAIL_ROUTES.get(oid) or ''
        detail_spec=SPEC_BY_ROUTE.get(detail_route) or {}
        src_ids=[sid for sid,_,_ in _public_source_rows(detail_spec)]
        source_label=', '.join(src_ids)
        _a,_b=_boundary_parts(ev,lang)
        boundary=(f'{_a} — {ui_text("UI-EVID-MEASUREMENT-LIMITS",lang)}: {_b}' if _b else _a) or locv(cl,'does_not_prove',lang)
        records.append({
            'id':oid,
            'title':title,
            'type':ev.get('object_class') or cl.get('claim_type') or '',
            'definition':locv(ev,'definition',lang),
            'period':locv(ev,'period',lang),
            'universe':locv(ev,'universe',lang),
            'method':locv(ev,'method',lang),
            'source':source_label,
            'currentness':locv(ev,'currentness',lang),
            'boundary':boundary,
            'verification':locv(ev,'verification',lang),
            'route':detail_route,
        })
    opts=''.join(f'<option value="{esc(x["id"])}">{esc(x["title"])}</option>' for x in records)
    optional_label='— سجل اختياري —' if ar else '— Optional record —'
    optional_opts=f'<option value="">{optional_label}</option>'+opts
    supporting=list(COMPARISON_PRESENTATION.get('supporting') or [])
    field_map={'source_reference':'source'}
    dimensions=[field_map.get(x,x) for x in supporting if field_map.get(x,x) in {'definition','universe','geography','unit','period','method','source','currentness'}]
    data=json.dumps(records,ensure_ascii=False).replace('</','<\\/')
    dim_data=json.dumps(dimensions,ensure_ascii=False).replace('</','<\\/')
    vis=(spec.get('governed_visual_contracts') or [{}])[0]
    summary=locv(vis,'accessible_summary',lang) or locv(vis,'decision_value',lang)
    prohibit=locv(vis,'prohibited_inference',lang)
    note=f'<div class="note"><strong>{"لا يُستنتج:" if ar else "Do not infer:"}</strong> {esc(prohibit)}</div>' if prohibit else ''
    title='هل يمكن مقارنة هذين السجلين مباشرة؟' if ar else 'Can these records actually be compared?'
    intro='ابدأ بمشروعية المقارنة، لا بالأرقام.' if ar else 'Start with comparison legitimacy, not the numbers.'
    a_lab='السجل الأول' if ar else 'First record'
    b_lab='السجل الثاني' if ar else 'Second record'
    c_lab='السجل الثالث — اختياري' if ar else 'Third record — optional'
    d_lab='السجل الرابع — اختياري' if ar else 'Fourth record — optional'
    never='لا متوسطات تلقائية · لا رقم مفضل · لا معامل تحويل مخترع' if ar else 'No auto-average · no preferred number · no invented conversion scalar'
    return (
        f'<section class="compare-lab" data-comparison-family="Comparison" data-comparison-contract="Comparison"><div class="container">'
        f'<div class="compare-intro"><div><div class="eyebrow">{esc(intro)}</div><h2>{esc(title)}</h2><p>{esc(summary)}</p></div><span class="badge gold">{esc(never)}</span></div>{note}'
        f'<div class="compare-controls"><label><span>{a_lab}</span><select id="compare-a" data-compare-slot="required" class="search-shell">{opts}</select></label>'
        f'<label><span>{b_lab}</span><select id="compare-b" data-compare-slot="required" class="search-shell">{opts}</select></label>'
        f'<label><span>{c_lab}</span><select id="compare-c" data-compare-slot="optional" class="search-shell">{optional_opts}</select></label>'
        f'<label><span>{d_lab}</span><select id="compare-d" data-compare-slot="optional" class="search-shell">{optional_opts}</select></label></div>'
        f'<div class="compare-share"><button type="button" class="button ghost" data-compare-copy>{"انسخ رابط هذه المقارنة" if ar else "Copy link to this comparison"}</button></div>'
        f'<div id="compare-status" class="sr-only" role="status" aria-live="polite" aria-atomic="true"></div><div id="compare-output"></div><script>window.__COMPARE__={data};window.__COMPARE_DIMENSIONS__={dim_data};</script>'
        f'</div></section>'
    )

def source_dependents(sid,lang):
    labels=_evidence_labels(lang); rows=[]; seen=set()
    for dep in SOURCE_DEPENDENTS.get(str(sid),[]):
        route=dep.get('route'); oid=dep.get('object_id')
        if not route or not oid or route in seen:
            continue
        seen.add(route)
        title=dep.get('title_ar') if lang=='ar' else dep.get('title_en')
        rows.append(f'<a href="{route_href(route,lang)}"><span>{esc(title or oid)}</span></a>')
    if not rows:
        return ''
    return (
        f'<details class="source-evidence-links" data-dependent-evidence="{esc(sid)}">'
        f'<summary>{labels["source_dependents"]} <span class="pill">{len(rows)}</span></summary>'
        f'<div class="source-evidence-link-list">{"".join(rows)}</div></details>'
    )

def source_directory(lang):
    ar=lang=='ar'
    title='دليل المصادر والتحقق' if ar else 'Source directory and verification'
    intro=('تُعرض هنا فقط معلومات المصدر التي تسمح بها السجلات المعتمدة. وتُفصل المراجع التي تسند أدلة عامة حالية عن المراجع المتاحة للتحقق أو السياق حتى لا يبدو مجرد وجود رابط وكأنه استخدام تحليلي أو دليل على نتيجة.' if ar else 'Only source information permitted by the controlled records is shown here. Sources that currently support public evidence are separated from reference locators available for verification or context, so the existence of a link is never mistaken for analytical use or an observed result.')
    ready_label='تقارير ومراجع منتقاة' if ar else 'Curated reports and references'
    supporting_label='مصادر تسند أدلة عامة حالية' if ar else 'Sources supporting current public evidence'
    reference_label='مراجع أصلية إضافية للتحقق والسياق' if ar else 'Additional original references for verification and context'
    supporting_intro=('هذه المصادر مرتبطة مباشرة بسجل دليل عام واحد على الأقل. افتح الروابط المرتبطة لمعرفة موضع استخدامها وحدودها.' if ar else 'These sources are linked directly to at least one current public Evidence Record. Open the dependent records to see exactly where and how they are used.')
    reference_intro=('هذه المراجع متاحة للتحقق أو المنهج أو السياق، لكنها لا تسند حاليًا سجل دليل عام. وجودها في الدليل لا يرقّيها إلى نتيجة أو خلاصة.' if ar else 'These references are available for verification, method or context but do not currently support a public Evidence Record. Their presence in the directory does not promote them into an evidence finding or claim.')
    search_label='ابحث عن مصدر بعنوانه أو مرجعه' if ar else 'Find a source by title or reference'
    ph='مثال: SRC-CBY…' if ar else 'e.g. SRC-CBY…'
    open_label='افتح المصدر الأصلي ↗' if ar else 'Open original source ↗'
    boundary_label='لا يثبت:' if ar else 'Does not establish:'
    ready=[]; supporting_locator=[]; reference_locator=[]
    for r in SOURCE_REFS:
        sid=str(r.get('source_id') or '').strip()
        if not sid: continue
        url=public_locator(r.get('primary_url'))
        state=r.get('metadata_state')
        search_terms=' '.join([sid, str(r.get('display_title') or ''), str(r.get('display_title_ar') or ''), str(r.get('publisher') or ''), str(r.get('publisher_ar') or ''), str(r.get('document_label') or ''), str(r.get('document_label_ar') or ''), str(r.get('document_type') or ''), url])   # TOOL-13
        trust=source_trust_controls(r,lang,compact=True)
        dependents=SOURCE_DEPENDENTS.get(sid,[])
        if state=='DISPLAY_READY' and not r.get('standalone_resource_card_eligible'):
            # Tranche C TC-B: a citation card (governed title, publisher, kind and date; no curated summary) sits in the
            # locator groups, named by its title rather than its reference.
            if not url:
                continue
            ctitle=(r.get('display_title_ar') if ar else r.get('display_title')) or sid
            kind=source_kind_line(r,lang)
            url_html=f'<a class="text-link source-link" href="{esc(url)}" rel="noopener noreferrer" target="_blank">{open_label}</a>'
            card=(f'<div id="source-{esc(sid)}" class="source-locator source-citation" data-source-record data-source-search="{esc(search_terms)}" tabindex="-1">'
                  f'<strong class="source-citation-title" dir="auto">{esc(ctitle)}</strong><div class="meta" dir="auto">{esc(kind)}</div>'
                  f'<span class="source-id" dir="ltr">{esc(sid)}</span>{url_html}{trust}{source_dependents(sid,lang)}</div>')
            (supporting_locator if dependents else reference_locator).append(card)
        elif state=='DISPLAY_READY':
            rtitle=(r.get('display_title_ar') if ar else r.get('display_title')) or sid
            cat=(r.get('resource_category_ar') if ar else r.get('resource_category')) or ''
            why=(r.get('why_it_matters_ar') if ar else r.get('why_it_matters')) or ''
            boundary=(r.get('does_not_establish_ar') if ar else r.get('does_not_establish')) or ''
            meta=' · '.join(x for x in [source_kind_line(r,lang),str(cat)] if x)
            url_html=f'<a class="text-link source-link" href="{esc(url)}" rel="noopener noreferrer" target="_blank">{open_label}</a>' if url else ''
            boundary_html=f'<div class="note"><strong>{boundary_label}</strong> {esc(boundary)}</div>' if boundary else ''
            why_html=f'<p>{esc(why)}</p>' if why else ''
            ready.append(f'<article id="source-{esc(sid)}" class="source-card" data-source-record data-source-search="{esc(search_terms)}" tabindex="-1"><div class="source-card-head"><bdi class="badge teal stable-id" dir="ltr">{esc(sid)}</bdi></div><h3 dir="auto">{esc(rtitle)}</h3><div class="meta" dir="auto">{esc(meta)}</div>{why_html}{boundary_html}{url_html}{trust}{source_dependents(sid,lang)}</article>')
        else:
            if not url:
                continue
            url_html=f'<a class="source-url" dir="ltr" href="{esc(url)}" rel="noopener noreferrer" target="_blank">{esc(url)}</a>'
            card=f'<div id="source-{esc(sid)}" class="source-locator" data-source-record data-source-search="{esc(search_terms)}" tabindex="-1"><span class="source-id" dir="ltr">{esc(sid)}</span>{url_html}{trust}{source_dependents(sid,lang)}</div>'
            if dependents:
                supporting_locator.append(card)
            else:
                reference_locator.append(card)
    no_results='لا توجد مصادر مطابقة لهذا البحث. ولا يعني ذلك غياب الأدلة عن الموضوع؛ جرّب معرّفًا أو عنوانًا آخر.' if ar else 'No sources match this search. This does not mean there is no evidence on the topic; try another reference or title.'
    rights_note=('يمكن الاستشهاد بكل مصدر هنا وفتحه في موقعه الأصلي. ويبيّن كل بطاقة حالة شروط إعادة استخدام مصدرها؛ وحيث لم تُقيَّم الشروط، لا يعرض هذا الموقع ملفات المصدر للتنزيل أو إعادة النشر، فتحقّق من شروط كل مصدر قبل إعادة توزيع مادته.'
                 if ar else
                 "Every source here can be cited and opened at its original location. Each card shows its source's reuse-terms state; where terms have not been assessed, this resource offers no source file for download or republication, so check each source's own terms before redistributing its material.")
    supporting_block=(
        f'<details class="source-locator-details source-supporting-details" open><summary>{supporting_label} <span class="pill">{len(supporting_locator)}</span></summary>'
        f'<p class="source-group-intro">{esc(supporting_intro)}</p><div class="source-locator-list">{"".join(supporting_locator)}</div></details>'
    )
    reference_block=(
        f'<details class="source-locator-details source-reference-details"><summary>{reference_label} <span class="pill">{len(reference_locator)}</span></summary>'
        f'<p class="source-group-intro">{esc(reference_intro)}</p><div class="source-locator-list">{"".join(reference_locator)}</div></details>'
    )
    return f'<section id="source-directory" class="section source-directory"><div class="container"><h2>{esc(title)}</h2><p class="source-intro">{esc(intro)}</p><p class="source-rights-note">{esc(rights_note)}</p><div class="source-filter search-shell"><span aria-hidden="true">⌕</span><input data-source-filter class="search-input" type="search" placeholder="{esc(ph)}" aria-label="{esc(search_label)}"></div><div class="source-filter-status" data-source-filter-status role="status" aria-live="polite"></div><h3 class="source-group-title">{ready_label}</h3><div class="source-ready-grid">{"".join(ready)}</div>{supporting_block}{reference_block}<div class="empty source-no-results" data-source-no-results hidden>{no_results}</div></div></section>'

def record_context_origin(lang,mode):
    # P2.3: a correction or report link keeps its originating record. A malformed or unknown reference is a technical
    # link error, stated as such (never as a finding about the evidence).
    ar=lang=='ar'
    current=('السجل الذي تبلّغ عنه' if ar else 'Record you are reporting on') if mode=='contact' else ('السجل الذي جئت منه' if ar else 'Record you came from')
    open_label='افتح السجل العام الحالي' if ar else 'Open the current public record'
    bad=('مرجع السجل في هذا الرابط غير صالح. هذه مشكلة في الرابط، وليست معلومة عن الأدلة.' if ar else 'The record reference in this link is not valid. This is a problem with the link, not information about the evidence.')
    unknown=('يشير هذا الرابط إلى مرجع لا يطابق أي سجل عام حالي. تحقّق من المرجع أو ابحث عن السجل؛ هذه مشكلة في الرابط، وليست معلومة عن الأدلة.' if ar else 'This link names a reference that matches no current public record. Check the reference or search for the record; this is a problem with the link, not information about the evidence.')
    ids=json.dumps(sorted(DETAIL_ROUTES)).replace('</','<\\/')
    return (
        f'<div class="correction-origin" data-correction-origin hidden><span>{esc(current)}</span><strong data-correction-record dir="ltr"></strong>'
        f'<a class="text-link" data-correction-link href="#">{esc(open_label)}</a></div>'
        f'<div class="correction-link-error" data-correction-error hidden role="alert" data-msg-malformed="{esc(bad)}" data-msg-unknown="{esc(unknown)}"></div>'
        f'<script>window.__RECORD_IDS__={ids};</script>'
    )

def _governed_contact_address():
    """The report channel is the address governed in the /contact Page Spec (Master copy); never typed in code."""
    spec=next((x for x in SPECS if x.get('template_route')=='/contact'),None) or {}
    found={m for sec in (spec.get('sections') or []) for k in ('body_en','body_ar') for m in _EMAIL.findall(str(sec.get(k) or ''))}
    if len(found)!=1:
        raise SystemExit(f'/contact must govern exactly one contact address, found {sorted(found)}')
    return found.pop()

CONTACT_ADDRESS=_governed_contact_address()

def contact_context_block(lang):
    # When a record reference arrives from a Report-issue link, offer one action that carries it into the message
    # subject (the governed copy asks for the product name in the subject). The runtime reveals it only for a known record.
    ar=lang=='ar'
    label='اكتب إلينا بشأن هذا السجل' if ar else 'Write to us about this record'
    subject='Yemen Financial Inclusion Evidence — '+('المرجع' if ar else 'Reference')
    mail=f'<a class="button primary" data-correction-mail hidden href="mailto:{esc(CONTACT_ADDRESS)}" data-mail-address="{esc(CONTACT_ADDRESS)}" data-mail-subject="{esc(subject)}">{esc(label)}</a>'
    return f'<section class="correction-context" data-correction-context data-context-mode="contact"><div class="container">{record_context_origin(lang,"contact")}{mail}</div></section>'

def corrections_context_block(lang):
    ar=lang=='ar'
    title='السجل الحالي ومسار التصحيح' if ar else 'Current record and correction path'
    intro=('لا ينشئ هذا الموقع سجل إصدارات أو تصحيحات افتراضيًا. تظهر واقعة التصحيح فقط عندما تكون معتمدة للنشر؛ ويظل المعرّف الثابت هو نقطة الرجوع إلى السجل العام الحالي.' if ar else 'This resource does not manufacture a release or correction history. A correction event appears only when it is governed for publication; the stable record ID remains the route back to the current public record.')
    current='السجل الذي جئت منه' if ar else 'Record you came from'
    open_label='افتح السجل العام الحالي' if ar else 'Open the current public record'
    empty='لا توجد في مواصفة هذه الصفحة حاليًا وقائع تصحيح جوهرية مستقلة معتمدة للنشر؛ لذلك لا تُنشئ الواجهة تاريخًا اصطناعيًا.' if ar else 'This page currently has no separately governed material-correction events to publish, so the interface does not invent a synthetic history.'
    return (
        f'<section class="correction-context" data-correction-context><div class="container correction-grid">'
        f'<div><h2>{esc(title)}</h2><p>{esc(intro)}</p></div>'
        f'<div><div class="empty" data-correction-empty>{esc(empty)}</div>{record_context_origin(lang,"corrections")}</div>'
        f'</div></section>'
    )

def generic(spec,lang):
    rt=spec.get('template_route'); extras=''
    if rt=='/explore': extras=question_cards(lang)
    elif rt=='/readings': extras=reading_cards(lang)
    elif rt=='/measurement': extras=measurement_cards(lang)
    elif rt=='/evidence':
        ar=lang=='ar'; ph='ابحث في الخلاصات والأدلة والقراءات…' if ar else 'Search claims, evidence, readings...'; label='بحث' if ar else 'Search'; comp='مقارنة الأدلة' if ar else 'Compare evidence'
        extras=f'<section id="search" class="section mint"><div class="container"><div class="search-shell"><span aria-hidden="true">⌕</span><input id="global-search" data-search-input class="search-input" placeholder="{ph}" aria-label="{label}"></div><div id="search-results" data-search-results class="search-results" aria-live="polite"></div><div class="hero-actions"><a class="button ghost" href="/{lang}/evidence/compare/">{comp}</a></div></div></section>'
    elif rt=='/evidence/compare': extras=compare_block(lang)
    elif rt=='/data': extras=source_directory(lang)
    elif rt=='/corrections': extras=corrections_context_block(lang)
    elif rt=='/contact': extras=contact_context_block(lang)
    # Comparison already consumes its governed public object set through the compatibility-first selector.
    # Re-rendering those objects as generic cards would duplicate the governed array and defeat intentional depth.
    if rt!='/evidence/compare':
        for heading,g in governed_block_groups(spec,lang,rt):
            h=f'<h2 class="block-heading">{esc(heading)}</h2>' if heading else ''
            extras+=f'<section class="section"><div class="container">{h}<div class="card-grid">{g}</div></div></section>'
    if rt=='/evidence': extras+=evidence_hub_index(lang)      # JRN-17
    if rt=='/data': extras+=chronology_block(lang)            # JRN-09
    extras+=journey_next(spec,lang)
    prose=sections(spec,lang,exclude_orders={5} if rt=='/explore' else None)
    return prose+extras

def _closure(object_type,oid):
    return next((c for c in PUBLIC_SOURCE_CLOSURE if c.get('object_type')==object_type and c.get('object_id')==oid),{})

def reading_verification_links(spec,lang):
    """P1.5: the Reading's verification path — each proposition the Reading relies on (the governed headline of the
    Evidence Record that carries it) -> the Evidence Record -> that record's bound sources, with the path's state."""
    ar=lang=='ar'
    r=(spec.get('governed_readings') or [{}])[0]
    bindings=r.get('verification_bindings') or {}
    ids=list(bindings.get('claim_ids') or r.get('claim_bindings') or [])
    steps=[]
    seen=set()
    unlisted=0
    path_ids=[]
    for oid in ids:
        oid=str(oid)
        route=DETAIL_ROUTES.get(oid)
        if not route or route in seen:
            continue
        path_ids.append(oid)
        seen.add(route)
        ds=SPEC_BY_ROUTE.get(route) or {}
        claim=next((c for c in ds.get('governed_claims') or [] if c.get('claim_id')==oid),{})
        obj=(ds.get('governed_evidence_objects') or [{}])[0]
        proposition=locv(claim,'headline',lang) or locv(obj,'title',lang) or locv(ds,'title',lang) or oid
        clo=_closure('evidence_object',oid)
        state=clo.get('closure_state')
        flag=''
        if state=='PARTIALLY_RESOLVED':
            flag=f'<span class="path-state" data-path-state="partial">{esc(ui_text("UI-READING-PATH-RECORD-PARTIAL",lang))}</span>'
        elif state in ('COMPOSITE_OF_OBJECTS','COMPOSITE_MEMBERS_NOT_LISTED'):
            flag=f'<span class="path-state" data-path-state="composite">{esc(ui_text("UI-READING-PATH-RECORD-COMPOSITE",lang))}</span>'
        srcs=[]; hidden=0
        for sid in clo.get('resolved_source_ids') or []:
            src=SOURCE_BY_ID.get(sid) or {}
            name=(src.get('display_title_ar') if ar else src.get('display_title')) if src.get('metadata_state')=='DISPLAY_READY' else ''
            if public_locator(src.get('primary_url')) and sid in PUBLIC_SOURCE_IDS:
                label=esc(name) if name else f'<bdi dir="ltr">{esc(sid)}</bdi>'
                srcs.append(f'<li><a class="text-link" href="/{lang}/data/?source={quote(sid)}#source-{quote(sid)}">{label}</a></li>')
            else:
                hidden+=1           # never named on a public page (publication firewall)
        if hidden:
            unlisted+=1
            srcs.append(f'<li class="path-state">{esc(ui_text("UI-SOURCE-NO-PUBLIC-LOCATOR",lang))}</li>')
        src_html=f'<ul class="reading-path-sources">{"".join(srcs)}</ul>' if srcs else ''
        steps.append(
            f'<li class="reading-path-step" data-path-record="{esc(oid)}"><a class="reading-verify-card" href="{route_href(route,lang)}"><strong>{esc(proposition)}</strong></a>'
            f' {public_ref(oid,lang)}{flag}{src_html}</li>'
        )
    if not steps:
        return ''
    title='تحقّق من هذه القراءة' if ar else 'Verify this reading'
    rstate=_closure('reading',str(r.get('reading_id') or '')).get('closure_state')
    if rstate=='CLOSED_TO_SOURCE_ID':
        status_id='UI-READING-PATH-COMPLETE-UNLISTED' if unlisted else 'UI-READING-PATH-COMPLETE'   # P4 (V-D1)
    else:
        status_id='UI-READING-PATH-PARTIAL'
    compare=''
    # Tranche C (TOOL-08/JRN-11): the comparison opens with this Reading's own records, and is offered only when at least
    # two of them are in the governed Compare set.
    cmp_ids=[x for x in path_ids if x in COMPARE_IDS][:4]
    if len(cmp_ids)>=2:
        compare_label='اختبر قابلية المقارنة بين سجلات هذه القراءة' if ar else "Test comparability of this Reading's records"
        compare=f'<a class="button ghost" href="/{lang}/evidence/compare/?records={",".join(quote(x) for x in cmp_ids)}">{esc(compare_label)}</a>'
    back=[]
    for rt_ in list(r.get('domain_context_routes') or [])+list(r.get('domain_surface_routes') or []):
        q=_qroute(rt_)
        if q in SPEC_BY_ROUTE and q not in back: back.append(q)
    back_html=(f'<div class="reading-return"><h3>{esc(ui_text("UI-READING-RETURN",lang))}</h3><ul>'+''.join(f'<li><a class="text-link" href="{route_href(q,lang)}">{esc(route_question_label(q,lang))}</a></li>' for q in back)+'</ul></div>') if back else ''
    return (
        f'<section class="reading-verify" data-reading-verify data-reading-path-state="{esc(rstate)}"><div class="container reading-verify-grid">'
        f'<div><h2>{esc(title)}</h2><p>{esc(ui_text("UI-READING-PATH-INTRO",lang))}</p>'
        f'<p class="reading-path-status">{esc(ui_text(status_id,lang))}</p>{compare}{back_html}</div>'
        f'<ol class="reading-path">{"".join(steps)}</ol></div></section>'
    )

def reading_detail(spec,lang):
    ar=lang=='ar'; r=(spec.get('governed_readings') or [{}])[0]; thesis=locv(r,'thesis',lang); question=locv(r,'question',lang); prohibit=locv(r,'prohibited_inference',lang); qlab='السؤال' if ar else 'Question'; tlab='الخلاصة المقيدة بالأدلة' if ar else 'Bounded thesis'; plab='لا يُستنتج:' if ar else 'Do not infer:'; note=f'<div class="note" style="margin-top:1rem"><strong>{plab}</strong> {esc(prohibit)}</div>' if prohibit else ''
    rid=str(r.get('reading_id') or '')
    # P4 (R10): the thesis card is labelled by the governed section-1 title of the Reading index (09), not a hard-coded label
    s1=next((x for x in READING_SECTIONS if x.get('reading_id')==rid and int(float(x.get('section_order') or 0))==1),None)
    if s1 and s1.get(f'title_{lang}'): tlab=s1[f'title_{lang}']
    # P4 (V-D12): when the Reading's own "does not establish" section already carries the prohibited inference (decided on the
    # English owner text so both editions behave alike), the lead card does not repeat it
    pi_en=str(r.get('prohibited_inference_en') or '')
    if pi_en and any(pi_en in str(x.get('body_en') or '') for x in spec.get('sections',[])):
        note=''
    crumbs=breadcrumb('Reading',rid,lang,current_title=locv(r,'title',lang) or rid)
    lead=f'<section class="section sand"><div class="container">{crumbs}<div class="eyebrow">{qlab}</div><h2>{esc(question)}</h2><div class="answer-card"><h3>{tlab}</h3><p>{esc(thesis)}</p></div>{note}</div></section>'
    verify=reading_verification_links(spec,lang)
    return lead+sections(spec,lang)+verify+f'<section class="section"><div class="container evidence-detail"><div class="card-grid" style="grid-template-columns:1fr">{governed_blocks(spec,lang)}</div>{sources_block(spec,lang)}</div></section>'

def _meta_clip(text,n=160):
    t=re.sub(r'\s+',' ',str(text or '')).strip()
    if len(t)<=n: return t
    cut=t[:n]; sp=cut.rfind(' ')
    return (cut[:sp] if sp>n*0.6 else cut).rstrip(' ,;:،؛')+'…'

def page_meta_description(spec,lang,title):
    """EN-11: the description never repeats the title; records and Readings lead with their governed summary or thesis."""
    governed=locv(spec,'meta_description',lang)
    if governed and governed.strip()!=str(title).strip():
        return governed
    cls=spec.get('page_class')
    if cls=='evidence_detail':
        obj=_evidence_object(spec) or {}
        if locv(obj,'summary',lang): return _meta_clip(locv(obj,'summary',lang))
    if cls=='reading_detail':
        r=(spec.get('governed_readings') or [{}])[0]
        if locv(r,'thesis',lang): return _meta_clip(locv(r,'thesis',lang))
    for x in spec.get('sections') or []:
        body=x.get(f'body_{lang}')
        if body: return _meta_clip(body)
    return title

def page(spec,lang):
    route=spec.get('route','/'); ar=lang=='ar'; direction='rtl' if ar else 'ltr'; cls=spec.get('page_class')
    if route in PRESENTATION_ROUTES:
        body=domain_page(spec,lang)
    elif cls=='evidence_detail':
        body=evidence_record_page(spec,lang)
    else:
        body=hero(spec,lang)
        if route=='/': body+=home_special(spec,lang)+home_ctas(lang)
        elif cls=='reading_detail': body+=reading_detail(spec,lang)
        else: body+=generic(spec,lang)
    other='en' if ar else 'ar'; product=ui_text('UI-PRODUCT-NAME',lang); title=locv(spec,'title',lang); desc=page_meta_description(spec,lang,title)   # PB-0410: never a *_internal field
    citation_meta=''
    if cls=='evidence_detail':
        obj=_evidence_object(spec)
        if obj:
            citation_meta=f'<meta name="yfie-citation" content="{esc(evidence_citation_context(spec,obj,lang))}"><meta name="yfie-record-id" content="{esc(obj.get("object_id") or obj.get("evidence_object_id") or "")}">'
    return f'<!doctype html><html lang="{lang}" dir="{direction}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#082d4f"><title>{esc(title)} — {product}</title><meta name="description" content="{esc(desc)}">{citation_meta}<link rel="stylesheet" href="/assets/styles.css"><link rel="alternate" hreflang="{other}" href="{route_href(route,other)}"><link rel="canonical" href="{route_href(route,lang)}"></head><body><noscript><div class="noscript-note">{esc(ui_text("UI-NOSCRIPT-NOTE",lang))}</div></noscript>{header(lang,route)}<main id="main" class="main">{body}</main>{footer(lang)}<script src="/assets/app.js" defer></script></body></html>'


files=SPECS
for spec in files:
    route=str(spec.get('route','/')).strip('/')
    for lang in ('ar','en'):
        d=DIST/lang/route; d.mkdir(parents=True,exist_ok=True); (d/'index.html').write_text(page(spec,lang),encoding='utf-8')
(DIST/'index.html').write_text('<!doctype html><meta charset="utf-8"><title>Yemen Financial Inclusion Evidence</title><script>let l="ar";try{const s=localStorage.getItem("yfie-lang");if(s==="en"||s==="ar")l=s;}catch(e){}location.replace("/"+l+"/");</script><noscript><meta http-equiv="refresh" content="0;url=/ar/"></noscript>',encoding='utf-8')
(DIST/'404.html').write_text(f'''<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#082d4f"><title>الصفحة غير موجودة — Yemen Financial Inclusion Evidence</title><link rel="stylesheet" href="/assets/styles.css"></head><body><main id="main" class="not-found"><div class="not-found-panel"><img src="/assets/CauseWay_Master_Logo.png" alt="CauseWay"><div class="eyebrow">404 · الصفحة غير موجودة / Page not found</div><div class="not-found-grid"><section lang="ar" dir="rtl"><h1>تعذر العثور على هذا المسار</h1><p>قد يكون الرابط قديمًا أو غير متاح ضمن المسارات العامة الحالية. ابدأ من الصفحة الرئيسية، أو استكشف الأسئلة، أو ابحث في الأدلة المنشورة.</p><div class="hero-actions"><a class="button primary" href="/ar/">الرئيسية</a><a class="button ghost" href="/ar/explore/">استكشف</a><a class="button ghost" href="/ar/evidence/">الأدلة</a><button class="button ghost" data-search-open>البحث (بالعربية والإنجليزية)</button></div></section><section lang="en" dir="ltr"><h2>We could not find this route</h2><p>The link may be old or unavailable in the current public route set. Start from Home, explore the questions, or search the published evidence.</p><div class="hero-actions"><a class="button primary" href="/en/">Home</a><a class="button ghost" href="/en/explore/">Explore</a><a class="button ghost" href="/en/evidence/">Evidence</a><button class="button ghost" data-search-open>Search (Arabic and English)</button></div></section></div></div></main>{search_dialog('ar')}<script src="/assets/app.js" defer></script></body></html>''',encoding='utf-8')
print(f'Built {len(files)*2+2} HTML files from {len(files)} controlled page specs.')
