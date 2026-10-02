(function(){
const $=(s,c=document)=>c.querySelector(s), $$=(s,c=document)=>[...c.querySelectorAll(s)];
const prefix=location.pathname.startsWith('/en/')?'/en':'/ar';
const isAr=document.documentElement.lang==='ar';
// R8.5: interface copy is governed in the Master (04, IDs UI-JS-*); the build writes this page's labels as JSON.
const UI=(()=>{try{return JSON.parse(document.getElementById('yfie-ui')?.textContent||'{}');}catch(e){return {};}})();
const T=k=>(k in UI?UI[k]:k);
// F6: page data travels in JSON blocks, never in inline executable scripts (a strict Content-Security-Policy stays possible).
const DATA=id=>{try{return JSON.parse(document.getElementById(id)?.textContent||'null');}catch(e){return null;}};
const TF=(k,o)=>T(k).replace(/\{(\w+)\}/g,(m,n)=>(n in o?String(o[n]):m));
const labelsFrom=table=>Object.fromEntries(Object.entries(table).map(([k,v])=>[k,T(v)]));
const COMPARE_ERROR_UI={"title": "UI-JS-COMPARE-LINK-TITLE", "count": "UI-JS-COMPARE-LINK-COUNT", "malformed": "UI-JS-COMPARE-LINK-MALFORMED", "unknown": "UI-JS-COMPARE-LINK-UNKNOWN", "note": "UI-JS-COMPARE-LINK-NOTE"};
const COMPARE_LABEL_UI={"definition": "UI-JS-COMPARE-DEFINITION", "universe": "UI-JS-COMPARE-UNIVERSE", "period": "UI-JS-COMPARE-PERIOD", "method": "UI-JS-COMPARE-METHOD", "source": "UI-JS-COMPARE-SOURCE", "currentness": "UI-JS-COMPARE-CURRENTNESS", "boundary": "UI-JS-COMPARE-BOUNDARY", "same": "UI-JS-COMPARE-SAME", "different": "UI-JS-COMPARE-DIFFERENT", "missing": "UI-JS-COMPARE-MISSING", "informational": "UI-JS-COMPARE-INFORMATIONAL", "sameRecord": "UI-JS-COMPARE-SAME-RECORD", "notDirect": "UI-JS-COMPARE-NOT-DIRECT", "unresolved": "UI-JS-COMPARE-UNRESOLVED", "qualified": "UI-JS-COMPARE-QUALIFIED", "aligned": "UI-JS-COMPARE-ALIGNED", "sameRecordCopy": "UI-JS-COMPARE-SAME-RECORD-COPY", "notDirectCopy": "UI-JS-COMPARE-NOT-DIRECT-COPY", "unresolvedCopy": "UI-JS-COMPARE-UNRESOLVED-COPY", "qualifiedCopy": "UI-JS-COMPARE-QUALIFIED-COPY", "alignedCopy": "UI-JS-COMPARE-ALIGNED-COPY", "dimension": "UI-JS-COMPARE-DIMENSION", "assessment": "UI-JS-COMPARE-ASSESSMENT", "openRecord": "UI-JS-COMPARE-OPEN-RECORD", "noMerge": "UI-JS-COMPARE-NO-MERGE", "table": "UI-JS-COMPARE-TABLE", "selected": "UI-JS-COMPARE-SELECTED"};
const TYPE_LABEL_UI={"page": "UI-JS-TYPE-PAGE", "question": "UI-JS-TYPE-QUESTION", "evidence": "UI-JS-TYPE-EVIDENCE", "reading": "UI-JS-TYPE-READING", "measurement": "UI-JS-TYPE-MEASUREMENT", "source": "UI-JS-TYPE-SOURCE", "source_locator": "UI-JS-TYPE-SOURCE-LOCATOR"};

function closeMenu(returnFocus=false){
  const n=$('#primary-nav'), b=$('[data-menu]');
  if(n)n.classList.remove('open');
  if(b){b.setAttribute('aria-expanded','false'); if(returnFocus)b.focus();}
}
$$('[data-menu]').forEach(b=>b.addEventListener('click',()=>{
  const n=$('#primary-nav'); if(!n)return;
  const open=n.classList.toggle('open');
  b.setAttribute('aria-expanded',String(open));
  if(open){
    const first=n.querySelector('a[href],button:not([disabled])');
    if(first)requestAnimationFrame(()=>first.focus());
  }
}));
$$('#primary-nav a').forEach(a=>a.addEventListener('click',()=>closeMenu(false)));
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&$('#primary-nav')?.classList.contains('open'))closeMenu(true);});
// TOOL-04: the open menu closes when focus leaves it and its button.
document.addEventListener('focusin',e=>{const n=$('#primary-nav'),b=$('[data-menu]');if(!n?.classList.contains('open'))return;if(n.contains(e.target)||b?.contains(e.target))return;closeMenu(false);});
window.addEventListener('resize',()=>{if(window.innerWidth>960)closeMenu(false);});
document.addEventListener('click',e=>{const n=$('#primary-nav'),b=$('[data-menu]');if(!n?.classList.contains('open'))return;if(n.contains(e.target)||b?.contains(e.target))return;closeMenu(false);});

$$('[data-lang]').forEach(b=>b.addEventListener('click',()=>{
  const target=b.dataset.lang; try{localStorage.setItem('yfie-lang',target);}catch(e){}   // TOOL-07: storage may be blocked
  let p=location.pathname.replace(/^\/(ar|en)/,''); if(!p.startsWith('/'))p='/'+p;
  location.href='/'+target+p+location.search+location.hash;
}));

function announceUtility(message){
  const status=$('#utility-status');
  if(!status)return;
  status.textContent='';
  requestAnimationFrame(()=>{status.textContent=message;});
}
async function copyText(text,button,promptLabel){
  try{
    await navigator.clipboard.writeText(text);
    if(button){const old=button.textContent;button.textContent='✓';setTimeout(()=>button.textContent=old,1400);}
    const copied=$('#utility-status')?.dataset.copiedLabel||T('UI-JS-COPIED');
    announceUtility(copied);
  }
  catch(e){prompt(promptLabel,text);}
}
$$('[data-cite]').forEach(b=>b.addEventListener('click',async()=>{
  const canonical=$('link[rel="canonical"]')?.href||location.href;
  const governed=$('meta[name="yfie-citation"]')?.content?.trim();
  const text=governed ? governed+' '+T('UI-JS-CURRENT-RECORD')+canonical : document.title+' — '+canonical;
  await copyText(text,b,T('UI-JS-COPY-CITATION'));
}));
$$('[data-source-cite]').forEach(b=>b.addEventListener('click',async()=>{
  const text=(b.dataset.sourceCitation||'').trim(); if(!text)return;
  await copyText(text,b,T('UI-JS-COPY-SOURCE-REFERENCE'));
}));

let searchIndexPromise=null;
function loadSearch(){
  if(!searchIndexPromise) searchIndexPromise=fetch('/static-data/search_index.json').then(r=>{if(!r.ok)throw new Error('search index');return r.json();}).then(x=>Array.isArray(x)?x:(x.records||[]));
  return searchIndexPromise;
}
function esc(s){return String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));}
// D6 RUNTIME_DEFECT, escalated to Code (design/ESCALATIONS.md): after Arabic letters a plain ISO date renders with its
// parts reversed ("07-11-2022 إلى 09-01-2023" for 2022-11-07 → 2023-01-09), a plain numeric range with its ends
// swapped and a plain signed value with its sign at the wrong end. Every page isolates those runs in its own text
// layer; anything this file writes into a page must read the same way. The expression is the renderer's own, character
// for character — scripts/yfie/text.py LTR_RUN — and scripts/validate.py fails if the two ever drift apart.
const LTR_RUN=/(?:(?<![\d.,])(?:\d{4}(?:-\d{2}(?:-\d{2})?)?[–-]\d{4}(?:-\d{2}(?:-\d{2})?)?|\d{1,3}–\d{1,3})(?![\d.,]))|(?:(?<![\d-])\d{4}-\d{2}(?:-\d{2})?(?![\d-]))|(?:(?<![\w\u0600-\u06FF-])[+\u2212\u2013-]\d[\d,]*(?:\.\d+)?%?(?![\w]))/g;
function iso(s){return esc(s).replace(LTR_RUN,m=>`<bdi dir="ltr" class="nw">${m}</bdi>`);}
// Tranche C (TOOL-12): Arabic-Indic and Persian digits read as Western digits. Mirrored in scripts/validate.py (_r4norm).
function normalize(s){return String(s||'').toLocaleLowerCase().normalize('NFKD').replace(/[\u0660-\u0669]/g,d=>String(d.charCodeAt(0)-0x0660)).replace(/[\u06F0-\u06F9]/g,d=>String(d.charCodeAt(0)-0x06F0)).replace(/[\u064B-\u065F\u0670]/g,'').replace(/[إأآٱ]/g,'ا').replace(/ى/g,'ي').replace(/ة/g,'ه').replace(/ؤ/g,'و').replace(/ئ/g,'ي');}
// Tranche C (JRN-05): a typed question is reduced to its content words: punctuation, one-letter tokens and a short
// bilingual stop-word list are dropped. Mirrored in scripts/validate.py (_r4tokens).
const STOP=new Set(['what','do','does','we','is','are','the','and','of','in','about','how','which','who','a','an','to','for','on','there','ما','ماذا','هل','في','من','على','عن','و','التي','الذي','هو','هي','كم','كيف']);
function queryTokens(term){return term.replace(/[?,.;:!—–"“”«»()؟،؛'’]/g,' ').split(/\s+/).filter(t=>t.length>1&&!STOP.has(t)).map(queryToken);}
// PB-0491: light query-token normalisation (Arabic definite article; English plural/verb endings). Mirrored in scripts/validate.py.
function queryToken(t){if(/^ال/.test(t)&&t.length>3)return t.slice(2);if(/^[a-z]+$/.test(t)&&t.length>4){if(/ies$/.test(t))return t.slice(0,-3)+'y';if(/ing$/.test(t))return t.slice(0,-3);if(/ed$/.test(t))return t.slice(0,-2);if(/s$/.test(t)&&!/ss$/.test(t))return t.slice(0,-1);}return t;}
const DOMAIN_ROUTES=new Set(['/people/','/firms/','/finance/','/providers/','/payments/','/remittances/','/access/','/reforms/','/measurement/']);
let aliasPromise=null;
function loadAliases(){if(!aliasPromise)aliasPromise=fetch('/static-data/search_aliases.json').then(r=>r.ok?r.json():[]).catch(()=>[]);return aliasPromise;}
function aliasFor(term,aliases){const q=term.split(/\s+/).filter(Boolean).map(queryToken).join(' ');for(const a of aliases){const terms=String((isAr?a.terms_ar:a.terms_en)||'').split(';').concat(String((isAr?a.terms_en:a.terms_ar)||'').split(';')).map(x=>normalize(x.trim()).split(/\s+/).filter(Boolean).map(queryToken).join(' ')).filter(Boolean);if(terms.includes(q))return a;}return null;}
function scoreRecord(x,tokens,phraseTokens,alias){
  const title=normalize(isAr?(x.title_ar||''):(x.title_en||''));const summary=normalize(isAr?(x.summary_ar||''):(x.summary_en||''));const text=normalize(isAr?(x.search_text_ar||''):(x.search_text_en||''));
  const boundary=normalize(isAr?(x.boundary_text_ar||''):(x.boundary_text_en||''));const stable=normalize([x.id,x.source_id,x.object_id,x.claim_id,x.reading_id].filter(Boolean).join(' '));
  let score=0;tokens.forEach(t=>{if(stable===t)score+=12;else if(/[-\d]/.test(t)&&stable.includes(t))score+=7;   // TOOL-10: a word is not matched inside opaque references
    if(title.includes(t))score+=6;if(summary.includes(t))score+=3;if(text.includes(t))score+=1;if(boundary.includes(t))score+=0.5;});
  const route=String(x.route||'');
  if(score>0&&x.type==='page'&&DOMAIN_ROUTES.has(route)&&phraseTokens.length&&phraseTokens.every(t=>title.includes(t)))score+=20;
  if(alias){String(alias.targets||'').split('|').map(v=>v.trim()).forEach(tg=>{if(tg.startsWith('route:')&&x.type==='page'&&route===tg.slice(6))score+=25;if(tg.startsWith('document_type:')&&x.document_type===tg.slice(14))score+=10;});}
  return [score,title];
}
function typeLabel(type){
  const t=String(type||'').toLowerCase();
  const labels=labelsFrom(TYPE_LABEL_UI);
  return labels[t]||'';
}
// TOOL-23: summaries are shortened at a word boundary before escaping, with an ellipsis.
function clip(s,n){s=String(s||'');if(s.length<=n)return s;const cut=s.slice(0,n);const sp=cut.lastIndexOf(' ');return (sp>n*0.6?cut.slice(0,sp):cut).replace(/[\s,;:،؛]+$/,'')+'…';}
function renderHits(hits){
  if(!hits.length) return '<div class="empty" data-search-empty>'+T('UI-JS-SEARCH-NO-RESULT')+'</div>';
  return hits.map(x=>{
    const title=(isAr?(x.title_ar||x.question_ar||x.label_ar):(x.title_en||x.question_en||x.label_en))||x.id||'Evidence';
    const summary=(isAr?(x.summary_ar||''):(x.summary_en||''));
    let route=x.route||x.primary_route||x.public_route||'/evidence/'; route=String(route).replace(/^\/(ar|en)/,''); if(!route.startsWith('/'))route='/'+route;
    const type=typeLabel(x.object_type||x.type||'');
    const meta=(isAr?(x.meta_ar||''):(x.meta_en||''));   // PB-0493(c): period or document kind, in the reader's language (TOOL-10)
    return `<a class="search-hit" href="${prefix}${route}"><div><h4>${iso(title)}</h4>${summary?`<p>${iso(clip(summary,220))}</p>`:''}</div>${type?`<span class="meta">${esc(type)}${meta?' · '+iso(meta):''}</span>`:''}</a>`;
  }).join('');
}
// EAD-06 (handoff §2: "tool state that matters — Compare records, filters, search query — is URL-addressable,
// reloadable and survives a language switch"). Only the page's OWN search writes the URL. The dialog is an overlay
// over whatever page the reader is on, and rewriting that page's address as they type would change what they share.
function writeSearchUrl(term){
  const next=location.pathname+(term?`?q=${encodeURIComponent(term)}`:'')+location.hash;
  if(next!==location.pathname+location.search+location.hash)history.replaceState(null,'',next);
}
function bindSearch(input,box,status,urlState){
  if(!input||!box)return;
  let timer;
  input.addEventListener('input',()=>{
    clearTimeout(timer);
    timer=setTimeout(async()=>{
      const term=normalize(input.value.trim());
      if(urlState)writeSearchUrl(input.value.trim());
      if(term.length<2){box.innerHTML=''; if(status)status.textContent=''; return;}
      if(status)status.textContent=T('UI-JS-SEARCHING');
      try{
        const idx=await loadSearch();
        const aliases=await loadAliases();
        const tokens=queryTokens(term);
        if(!tokens.length){box.innerHTML=renderHits([]);if(status)status.textContent=T('UI-JS-SEARCH-ZERO');return;}
        const alias=aliasFor(term.replace(/[?,.;:!—–"“”«»()؟،؛'’]/g,' ').trim(),aliases);
        const ranked=idx.map(x=>{const [score,title]=scoreRecord(x,tokens,tokens,alias);return [score,x,title];}).filter(([score])=>score>0).sort((a,b)=>b[0]-a[0]);
        const unique=[], seen=new Map();
        ranked.forEach(([score,x,title])=>{
          const route=String(x.route||x.primary_route||x.public_route||'');
          const key=route;   // TOOL-10: one result per destination
          if(!seen.has(key)){seen.set(key,unique.length);unique.push(x);return;}
          const pos=seen.get(key), current=unique[pos];
          const currentType=String(current.type||current.object_type||'');
          const nextType=String(x.type||x.object_type||'');
          if(currentType==='page'&&nextType!=='page')unique[pos]=x;
        });
        const scored=unique.slice(0,10);
        const note=alias&&(isAr?alias.boundary_note_ar:alias.boundary_note_en);
        box.innerHTML=(note?`<p class="search-boundary-note">${esc(note)}</p>`:'')+renderHits(scored);
        if(status)status.textContent=TF(scored.length===1?'UI-JS-SEARCH-RESULT-ONE':'UI-JS-SEARCH-RESULTS',{n:scored.length});   // TOOL-19
      }catch(e){
        box.innerHTML='<div class="empty">'+T('UI-JS-SEARCH-UNAVAILABLE-COPY')+'</div>';
        if(status)status.textContent=T('UI-JS-SEARCH-UNAVAILABLE');
      }
    },100);
  });
}

$$('[data-search-input]').forEach(input=>{
  const scope=input.closest('.search-dialog-panel')||input.parentElement?.parentElement||document;
  const box=$('[data-search-results]',scope)||$('#search-results');
  const status=$('[data-search-status]',scope);
  const urlState=input.hasAttribute('data-search-url-state');
  bindSearch(input,box,status,urlState);
  if(urlState){
    const q=new URLSearchParams(location.search).get('q');
    if(q!==null&&q!==''){input.value=q;input.dispatchEvent(new Event('input'));}
  }
});
const dialog=$('#search-dialog');
let searchOpener=null;
function openSearch(opener=null){
  if(!dialog)return; searchOpener=opener||document.activeElement;
  if(typeof dialog.showModal==='function'){if(!dialog.open)dialog.showModal();} else dialog.setAttribute('open','');
  const input=$('[data-search-input]',dialog); if(input)setTimeout(()=>input.focus(),0);
}
$$('[data-search-open]').forEach(b=>b.addEventListener('click',()=>openSearch(b)));
document.addEventListener('keydown',e=>{
  const tag=(e.target?.tagName||'').toLowerCase(),typing=['input','textarea','select'].includes(tag)||e.target?.isContentEditable;
  if((e.ctrlKey||e.metaKey)&&e.key.toLowerCase()==='k'){e.preventDefault();openSearch();return;}
  if(e.key==='/'&&!typing&&!e.ctrlKey&&!e.metaKey&&!e.altKey){e.preventDefault();openSearch();}
});
$$('[data-search-close]').forEach(b=>b.addEventListener('click',()=>{if(dialog?.open)dialog.close(); else dialog?.removeAttribute('open');}));
if(dialog){
  dialog.addEventListener('click',e=>{if(e.target===dialog){if(dialog.open)dialog.close();else dialog.removeAttribute('open');}});
  dialog.addEventListener('close',()=>{if(searchOpener){searchOpener.focus();searchOpener=null;}});
}

// Data source directory. Search/source locators remain bounded to the controlled source map rendered by the build.
const sourceInput=$('[data-source-filter]');
if(sourceInput){
  const records=$$('[data-source-record]');
  const status=$('[data-source-filter-status]'), noResults=$('[data-source-no-results]'), locatorDetails=$('.source-locator-details');
  const apply=()=>{
    const term=normalize(sourceInput.value.trim()); let shown=0, visibleLocators=0;
    records.forEach(r=>{const ok=!term||normalize(r.dataset.sourceSearch||'').includes(term);r.hidden=!ok;if(ok){shown++;if(r.classList.contains('source-locator'))visibleLocators++;}});
    if(term&&visibleLocators&&locatorDetails)locatorDetails.open=true;
    if(noResults)noResults.hidden=shown!==0;
    if(status)status.textContent=TF(shown===1?'UI-JS-SOURCES-SHOWN-ONE':'UI-JS-SOURCES-SHOWN',{n:shown});   // TOOL-19
  };
  sourceInput.addEventListener('input',apply);
  const requested=new URLSearchParams(location.search).get('source');
  const target=requested?document.getElementById('source-'+requested):null;
  if(requested&&target){
    sourceInput.value=requested; apply();
    const details=target.closest('details'); if(details)details.open=true;
    target.classList.add('source-target');
    setTimeout(()=>{target.scrollIntoView({block:'center'});target.focus({preventScroll:true});},30);
  } else {
    apply();
    if(requested&&status){   // P2.3: an unknown deep link is a link problem, not an empty result about the evidence
      status.setAttribute('role','alert');
      status.dataset.sourceLinkError='unknown';
      status.textContent=T('UI-JS-SOURCE-LINK-UNKNOWN');
    }
  }
}

// Corrections/version entry preserves the originating evidence record without inventing a history event.
const correctionContext=$('[data-correction-context]');
if(correctionContext){
  // P2.3: the originating record survives into Corrections and Contact; a malformed or unknown reference is a technical link error.
  const record=new URLSearchParams(location.search).get('record');
  const known=new Set(DATA('yfie-record-ids')||[]);
  const origin=$('[data-correction-origin]',correctionContext), rid=$('[data-correction-record]',correctionContext), link=$('[data-correction-link]',correctionContext), err=$('[data-correction-error]',correctionContext);
  if(record!==null){
    if(!/^[A-Za-z0-9._+-]+$/.test(record)){ if(err){err.textContent=err.dataset.msgMalformed;err.dataset.correctionError='malformed';err.hidden=false;} }
    else if(!known.has(record)){ if(err){err.textContent=err.dataset.msgUnknown;err.dataset.correctionError='unknown';err.hidden=false;} }
    else if(origin&&rid&&link){
      rid.textContent=record;link.href=`${prefix}/evidence/${encodeURIComponent(record)}/`;origin.hidden=false;
      const mail=$('[data-correction-mail]',correctionContext);
      if(mail){mail.href=`mailto:${mail.dataset.mailAddress}?subject=${encodeURIComponent(mail.dataset.mailSubject+' '+record)}`;mail.hidden=false;}
    }
  }
}

const compareSelects=['#compare-a','#compare-b','#compare-c','#compare-d'].map(s=>$(s)).filter(Boolean), out=$('#compare-output'), compareStatus=$('#compare-status');
if(compareSelects.length>=2&&out){
  const data=DATA('yfie-compare')||[];
  const contractDimensions=Array.isArray(DATA('yfie-compare-dimensions'))?DATA('yfie-compare-dimensions'):[];
  const labels=labelsFrom(COMPARE_LABEL_UI);
  const requiredHard=new Set(['definition','universe','method']);   // Tranche C TOOL-01: only governed per-record fields
  const temporal=new Set(['period','currentness']);
  const dimensions=contractDimensions.filter(f=>['definition','universe','period','method','source','currentness'].includes(f));
  const norm=v=>normalize(String(v||'').trim()).replace(/\s+/g,' ');
  const assessMany=(records,f)=>{
    const vals=records.map(r=>String(r[f]||'').trim());
    if(vals.some(v=>!v))return {state:'missing',label:labels.missing};
    const same=vals.every(v=>norm(v)===norm(vals[0]));
    if(f==='source')return {state:same?'same':'different',label:labels.informational};
    return same?{state:'same',label:labels.same}:{state:'different',label:labels.different};
  };
  const verdict=(records,rows)=>{
    if(new Set(records.map(r=>r.id)).size!==records.length)return {state:'same-record',title:labels.sameRecord,copy:labels.sameRecordCopy};
    if(rows.some(r=>requiredHard.has(r.field)&&r.state==='different'))return {state:'not-direct',title:labels.notDirect,copy:labels.notDirectCopy};
    if(rows.some(r=>requiredHard.has(r.field)&&r.state==='missing'))return {state:'unresolved',title:labels.unresolved,copy:labels.unresolvedCopy};
    if(rows.some(r=>temporal.has(r.field)&&r.state==='different'))return {state:'qualified',title:labels.qualified,copy:labels.qualifiedCopy};
    if(rows.some(r=>temporal.has(r.field)&&r.state==='missing'))return {state:'unresolved',title:labels.unresolved,copy:labels.unresolvedCopy};
    return {state:'aligned',title:labels.aligned,copy:labels.alignedCopy};
  };
  const recordLink=x=>x.route?`<a class="button ghost" href="${prefix}${esc(x.route)}">${esc(labels.openRecord)} — ${iso(x.title)}</a>`:'';
  // P2.1: the comparison is shareable. URL state is ?records=ID,ID[,ID[,ID]] in slot order (each ID percent-encoded,
  // commas literal). The URL always reflects the comparison shown; reload, a copied link or a language switch
  // (which keeps the query) reproduces it. A malformed or unknown link is a technical input error, never an evidence verdict.
  const errorText=labelsFrom(COMPARE_ERROR_UI);
  const validIds=new Set(data.map(x=>x.id));
  const parseRecordsParam=raw=>{
    if(raw===null)return {state:'absent'};
    const parts=raw.split(',');
    if(!raw.trim()||parts.some(p=>!p.trim()))return {state:'error',reason:'malformed'};
    const ids=parts.map(p=>p.trim());
    if(ids.length<2||ids.length>4)return {state:'error',reason:'count'};
    if(ids.some(id=>!/^[A-Za-z0-9._+-]+$/.test(id)))return {state:'error',reason:'malformed'};
    const unknown=ids.filter(id=>!validIds.has(id));
    if(unknown.length)return {state:'error',reason:'unknown',ids:unknown};
    return {state:'ok',ids};
  };
  const serialize=()=>compareSelects.map(sel=>sel.value).filter(Boolean).map(encodeURIComponent).join(',');
  const writeUrl=()=>{
    const q=serialize();
    const next=location.pathname+(q?`?records=${q}`:'')+location.hash;
    if(next!==location.pathname+location.search+location.hash)history.replaceState(null,'',next);
  };
  const showUrlError=r=>{
    const detail=r.reason==='count'?errorText.count:r.reason==='unknown'?errorText.unknown+(r.ids||[]).join(', '):errorText.malformed;
    out.innerHTML=`<div class="compare-url-error" role="alert" data-compare-url-error="${esc(r.reason)}"><h3>${esc(errorText.title)}</h3><p>${esc(detail)}</p><p>${esc(errorText.note)}</p></div>`;
    if(compareStatus)compareStatus.textContent='';
    const cb=$('[data-compare-copy]'); if(cb)cb.disabled=true;   // TOOL-18: never copy a comparison the page is not showing
  };
  const draw=()=>{
    const records=compareSelects.map(sel=>data.find(x=>x.id===sel.value)).filter(Boolean);
    writeUrl();
    const cb=$('[data-compare-copy]'); if(cb)cb.disabled=records.length<2;
    if(records.length<2){out.innerHTML='';return;}
    const rows=dimensions.map(field=>({field,...assessMany(records,field)}));
    const v=verdict(records,rows);
    const head=records.map(x=>`<th scope="col">${iso(x.title)}</th>`).join('');
    const body=rows.map(r=>`<tr data-compare-state="${esc(r.state)}"><th scope="row">${esc(labels[r.field]||r.field)}</th>${records.map(x=>`<td>${iso(x[r.field]||'—')}</td>`).join('')}<td><span class="compare-state">${esc(r.label)}</span></td></tr>`).join('');
    const boundaries=records.some(x=>x.boundary)?`<div class="compare-boundaries">${records.map(x=>`<article><strong>${iso(x.title)}</strong><p>${iso(x.boundary||'—')}</p></article>`).join('')}</div>`:'';
    out.innerHTML=`<section class="compare-verdict" data-compare-verdict="${esc(v.state)}" data-noncolour-semantic="text-label-structure"><div class="eyebrow">${esc(labels.assessment)}</div><h3>${esc(v.title)}</h3><p>${esc(v.copy)}</p><p class="compare-no-merge">${esc(labels.noMerge)}</p></section><div class="table-wrap" tabindex="0" role="region" aria-label="${esc(labels.table)}" data-noncolour-semantic="caption-headers-text-labels"><table class="compare-table"><caption class="sr-only">${esc(labels.table)}</caption><thead><tr><th scope="col">${esc(labels.dimension)}</th>${head}<th scope="col">${esc(labels.assessment)}</th></tr></thead><tbody>${body}</tbody></table></div>${boundaries}<div class="compare-record-actions">${records.map(recordLink).join('')}</div>`;
    if(compareStatus)compareStatus.textContent=`${v.title}. ${TF('UI-JS-COMPARE-SELECTED',{n:records.length})}`;   // RC-3: label-value form ("Records selected: 2")
  };
  compareSelects.forEach(sel=>sel.addEventListener('change',draw));
  const requested=parseRecordsParam(new URLSearchParams(location.search).get('records'));
  if(requested.state==='ok'){
    compareSelects.forEach((sel,i)=>{sel.value=requested.ids[i]||'';});   // duplicates stay selected: the verdict shows them as invalid
    draw();
  }else{
    if(compareSelects[1]?.options.length>1)compareSelects[1].selectedIndex=1;
    if(requested.state==='error')showUrlError(requested); else draw();
  }
  const copyBtn=$('[data-compare-copy]');
  if(copyBtn)copyBtn.addEventListener('click',async()=>{writeUrl();await copyText(location.href,copyBtn,copyBtn.textContent);});
}
})();
