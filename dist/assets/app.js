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
// B9 (release candidate): one citation per page, shown in its preview before it is copied; every cite control copies
// exactly the preview's text, with the page's own canonical address written into it.
const canonicalHref=$('link[rel="canonical"]')?.href||location.href;
$$('[data-cite-url]').forEach(e=>{e.textContent=canonicalHref;});
$$('[data-cite]').forEach(b=>b.addEventListener('click',async()=>{
  const preview=$('[data-cite-text]');
  const governed=$('meta[name="yfie-citation"]')?.content?.trim();
  const lines=preview ? [...preview.querySelectorAll('[data-cite-line]')] : [];
  const text=lines.length ? lines.map(l=>l.textContent.replace(/\s+/g,' ').trim()).filter(Boolean).join('\n')
    : preview ? preview.textContent.replace(/\s+/g,' ').trim()
    : (governed ? governed+' '+T('UI-JS-CURRENT-RECORD')+canonicalHref : document.title+' — '+canonicalHref);
  await copyText(text,b,T('UI-JS-COPY-CITATION'));
}));
// RC-15 (B15 e, U1): share a record — its governed title, period, population and what not to conclude, never cut,
// with its link. Web Share where the device offers it; otherwise the same text is copied.
$$('[data-share]').forEach(b=>b.addEventListener('click',async()=>{
  const text=(b.dataset.shareText||'').trim(); if(!text)return;
  if(navigator.share){
    try{await navigator.share({title:document.title,text,url:canonicalHref});return;}
    catch(e){if(e&&e.name==='AbortError')return;}
  }
  await copyText(text+'\n'+canonicalHref,b,T('UI-JS-SHARE-RECORD'));
}));
// RC-15 (B15 d, C-2; OWN-04): the long form of a record's citation is copied as it is previewed
$$('[data-cite-long]').forEach(b=>b.addEventListener('click',async()=>{
  const long=$('[data-cite-long-text]'); if(!long)return;
  await copyText(long.textContent.replace(/\s+/g,' ').trim(),b,T('UI-JS-COPY-LONG-CITATION'));
}));
$$('[data-print]').forEach(b=>b.addEventListener('click',()=>window.print()));
$$('[data-source-cite]').forEach(b=>b.addEventListener('click',async()=>{
  const text=(b.dataset.sourceCitation||'').trim(); if(!text)return;
  await copyText(text,b,T('UI-JS-COPY-SOURCE-REFERENCE'));
}));

let searchIndexPromise=null;
function loadSearch(){
  // B15 (A-1): a failed load is not kept, so the next search tries again (a dropped connection must not break search
  // until the page is reloaded)
  if(!searchIndexPromise) searchIndexPromise=fetch('/static-data/search_index.json').then(r=>{if(!r.ok)throw new Error('search index');return r.json();}).then(x=>Array.isArray(x)?x:(x.records||[])).catch(e=>{searchIndexPromise=null;throw e;});
  return searchIndexPromise;
}
function esc(s){return String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));}
// D6 RUNTIME_DEFECT, escalated to Code (design/ESCALATIONS.md): after Arabic letters a plain ISO date renders with its
// parts reversed ("07-11-2022 إلى 09-01-2023" for 2022-11-07 → 2023-01-09), a plain numeric range with its ends
// swapped and a plain signed value with its sign at the wrong end. Every page isolates those runs in its own text
// layer; anything this file writes into a page must read the same way. The expression is the renderer's own, character
// for character — scripts/yfie/text.py LTR_RUN — and scripts/validate.py fails if the two ever drift apart.
const LTR_RUN=/(?:(?<![A-Za-z0-9_.,-])(?:\d{4}(?:-\d{2}(?:-\d{2})?)?[–-]\d{4}(?:-\d{2}(?:-\d{2})?)?|\d{1,3}(?:,\d{3})+–\d{1,3}(?:,\d{3})+|\d{1,3}–\d{1,3})(?!\d|[.,]\d))|(?:(?<![A-Za-z0-9_-])\d{4}-\d{2}(?:-\d{2})?(?![\d-]))|(?:(?<![\w\u0600-\u06FF-])[+\u2212\u2013-]\d[\d,]*(?:\.\d+)?%?(?![\w]))/g;
const ID_RUN=/(?<![A-Za-z0-9_-])(?=[A-Z][A-Za-z0-9-]*\d)[A-Z][A-Z0-9]*(?:-[A-Za-z0-9]+)+(?![A-Za-z0-9_-])/g;   // identifiers: isolated too, but breakable (scripts/yfie/text.py ID_RUN)
function iso(s){return esc(s).replace(LTR_RUN,m=>`<bdi dir="ltr" class="nw">${m}</bdi>`).split(/(<[^>]+>)/).map((p,k)=>k%2?p:p.replace(ID_RUN,m=>`<bdi dir="ltr">${m}</bdi>`)).join('');}
// Tranche C (TOOL-12): Arabic-Indic and Persian digits read as Western digits. Mirrored in scripts/validate.py (_r4norm).
function normalize(s){return String(s||'').toLocaleLowerCase().normalize('NFKD').replace(/[\u0660-\u0669]/g,d=>String(d.charCodeAt(0)-0x0660)).replace(/[\u06F0-\u06F9]/g,d=>String(d.charCodeAt(0)-0x06F0)).replace(/[\u064B-\u065F\u0670]/g,'').replace(/[إأآٱ]/g,'ا').replace(/ى/g,'ي').replace(/ة/g,'ه').replace(/ؤ/g,'و').replace(/ئ/g,'ي')
  .replace(/(\d)[,\u066C](?=\d{3}(?!\d))/g,'$1').replace(/(\d)\u066B(?=\d)/g,'$1.');}   // B15 (C-5): "6,245" = "6245"; Arabic separators
// Tranche C (JRN-05): a typed question is reduced to its content words: punctuation, one-letter tokens and a short
// bilingual stop-word list are dropped. Mirrored in scripts/validate.py (_r4tokens).
const STOP=new Set(['what','do','does','we','is','are','the','and','of','in','about','how','which','who','a','an','to','for','on','there','ما','ماذا','هل','في','من','على','عن','و','التي','الذي','هو','هي','كم','كيف']);
function queryTokens(term){return term.replace(/[?,;:!—–"“”«»()؟،؛'’]/g,' ').replace(/(?<!\d)\.|\.(?!\d)/g,' ').split(/\s+/).filter(t=>t.length>1&&!STOP.has(t)).map(queryToken);}
// B15 (C-5, A-2): a number matches only as a whole number; a word only from the start of a word (after the Arabic
// proclitics و ف ب ل ك and the article), and a word of three letters or fewer only whole; an identifier still matches
// inside a reference (TOOL-10). Mirrored in scripts/validate.py (_r4re).
const WCH='a-z0-9\u0621-\u064A';
function tokenRe(t){
  const e=t.replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(/^\d+(?:\.\d+)?%?$/.test(t))return new RegExp(`(?<![0-9.,])${e}(?![0-9]|[.,][0-9])`);
  if(/[-\d]/.test(t))return null;
  const ar=/[\u0621-\u064A]/.test(t);
  const pre=ar?'(?:[وفبلك])?(?:ال|لل)?':'';
  const tail=t.length<=3?(ar?`(?:ه|ي|ات)?(?![${WCH}])`:`s?(?![${WCH}])`):'';
  return new RegExp(`(?<![${WCH}])${pre}${e}${tail}`);
}
function hasTok(text,t,re){return re?re.test(text):text.includes(t);}
// PB-0491: light query-token normalisation (Arabic definite article; English plural/verb endings). Mirrored in scripts/validate.py.
function queryToken(t){if(/^ال/.test(t)&&t.length>3)return t.slice(2);if(/^[a-z]+$/.test(t)&&t.length>4){if(/ies$/.test(t))return t.slice(0,-3)+'y';if(/ing$/.test(t))return t.slice(0,-3);if(/ed$/.test(t))return t.slice(0,-2);if(/s$/.test(t)&&!/ss$/.test(t))return t.slice(0,-1);}return t;}
const DOMAIN_ROUTES=new Set(['/people/','/firms/','/finance/','/providers/','/payments/','/remittances/','/access/','/reforms/','/measurement/']);
let aliasPromise=null;
function loadAliases(){if(!aliasPromise)aliasPromise=fetch('/static-data/search_aliases.json').then(r=>{if(!r.ok)throw new Error('aliases');return r.json();}).catch(()=>{aliasPromise=null;return [];});return aliasPromise;}   // B15 (A-1): retried after a failure
function aliasFor(term,aliases){const q=term.split(/\s+/).filter(Boolean).map(queryToken).join(' ');for(const a of aliases){const terms=String((isAr?a.terms_ar:a.terms_en)||'').split(';').concat(String((isAr?a.terms_en:a.terms_ar)||'').split(';')).map(x=>normalize(x.trim()).split(/\s+/).filter(Boolean).map(queryToken).join(' ')).filter(Boolean);if(terms.includes(q))return a;}return null;}
function aliasPhrases(a){return String(a.terms_en||'').split(';').concat(String(a.terms_ar||'').split(';')).map(x=>normalize(x.trim()).split(/\s+/).filter(t=>t.length>1&&!STOP.has(t)).map(queryToken)).filter(p=>p.length);}
function scoreRecord(x,tokens,phraseTokens,alias){
  const title=normalize(isAr?(x.title_ar||''):(x.title_en||''));const summary=normalize(isAr?(x.summary_ar||''):(x.summary_en||''));const text=normalize(isAr?(x.search_text_ar||''):(x.search_text_en||''));
  const boundary=normalize(isAr?(x.boundary_text_ar||''):(x.boundary_text_en||''));const stable=normalize([x.id,x.source_id,x.object_id,x.claim_id,x.reading_id].filter(Boolean).join(' '));
  let score=0;tokens.forEach(t=>{if(stable===t)score+=12;else if(/[-\d]/.test(t)&&stable.includes(t))score+=7;   // TOOL-10: a word is not matched inside opaque references
    const re=tokenRe(t);if(hasTok(title,t,re))score+=6;if(hasTok(summary,t,re))score+=3;if(hasTok(text,t,re))score+=1;if(hasTok(boundary,t,re))score+=0.5;});
  // B15 (A-3): a query that is a governed alias term also finds the group's other terms, ranked below literal hits
  if(alias){aliasPhrases(alias).forEach(ph=>{const all=f=>ph.every(t=>hasTok(f,t,tokenRe(t)));if(all(title))score+=3;else if(all(summary))score+=1.5;else if(all(text))score+=0.5;});}
  const route=String(x.route||'');
  if(score>0&&x.type==='page'&&DOMAIN_ROUTES.has(route)&&phraseTokens.length&&phraseTokens.every(t=>hasTok(title,t,tokenRe(t))))score+=20;
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
  // RC-17 (owner decisions of 3 October 2026, point 2): names from the regulator's lists and enforcement decisions are
  // not in the index; the empty state says so once and points to the original documents on Data & sources
  if(!hits.length) return '<div class="empty" data-search-empty>'+T('UI-JS-SEARCH-NO-RESULT')
    +'<p class="small" data-search-names-note><a href="'+prefix+'/data/#regulatory">'+esc(T('UI-JS-SEARCH-NAMES-NOTE'))+'</a></p></div>';
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
function writeSearchUrl(term,type){
  const qs=new URLSearchParams();if(term)qs.set('q',term);if(term&&type)qs.set('type',type);
  const next=location.pathname+(qs.toString()?`?${qs}`:'')+location.hash;
  if(next!==location.pathname+location.search+location.hash)history.replaceState(null,'',next);
}
// RC-3 / EAD-06: the result-type filter (governed name and no-type state; the option labels are the governed type labels).
function typeFacet(input){
  const sel=document.createElement('select');
  sel.className='search-type';sel.setAttribute('data-search-type','');sel.setAttribute('aria-label',T('UI-JS-SEARCH-TYPE-FACET'));
  sel.innerHTML=`<option value="">${esc(T('UI-JS-SEARCH-TYPE-ALL'))}</option>`+Object.keys(TYPE_LABEL_UI).map(k=>`<option value="${k}">${esc(typeLabel(k))}</option>`).join('');
  input.insertAdjacentElement('afterend',sel);
  return sel;
}
function bindSearch(input,box,status,urlState){
  if(!input||!box)return;
  let timer;
  const facet=typeFacet(input);
  const cap=urlState?Infinity:10;   // the dialog shows ten; the Evidence directory's own search shows every match
  facet.addEventListener('change',()=>input.dispatchEvent(new Event('input')));
  input.addEventListener('input',()=>{
    clearTimeout(timer);
    timer=setTimeout(async()=>{
      const term=normalize(input.value.trim());
      const type=facet.value;
      if(urlState)writeSearchUrl(input.value.trim(),type);
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
        const matching=type?unique.filter(x=>String(x.object_type||x.type||'').toLowerCase()===type):unique;
        const scored=matching.slice(0,cap);
        const note=alias&&(isAr?alias.boundary_note_ar:alias.boundary_note_en);
        // A6 / C7: when fewer hits are shown than match, say so with the true total and carry the query to the Evidence directory (?q=, EAD-06)
        const capped=scored.length<matching.length;
        const seeAll=capped?`<p class="search-see-all"><a href="${prefix}/evidence/?q=${encodeURIComponent(input.value.trim())}&amp;type=evidence">${esc(T('UI-JS-SEARCH-SEE-ALL-EVIDENCE'))}</a></p>`:'';
        box.innerHTML=(note?`<p class="search-boundary-note">${esc(note)}</p>`:'')+renderHits(scored)+seeAll;
        if(status)status.textContent=capped?TF('UI-JS-SEARCH-RESULTS-OF',{n:scored.length,m:matching.length})
          :TF(scored.length===1?'UI-JS-SEARCH-RESULT-ONE':'UI-JS-SEARCH-RESULTS',{n:scored.length});   // TOOL-19
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
    const q=new URLSearchParams(location.search).get('q'), type=new URLSearchParams(location.search).get('type');
    const facet=input.parentElement?.querySelector('[data-search-type]');
    if(facet&&type&&Object.prototype.hasOwnProperty.call(TYPE_LABEL_UI,type))facet.value=type;
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
  // RC-12 (B13 a): filters by document type, publisher, year and the domain page that uses a source, an order by
  // document date, and the whole state in the URL so a filtered list can be shared; the controls appear only here, so
  // without JavaScript the full list is unchanged
  const facetBox=$('[data-source-facets]'), facets=$$('[data-source-facet]'), sortSel=$('[data-source-sort]');
  const facetOk=r=>facets.every(f=>!f.value||(f.dataset.sourceFacet==='domain'?(r.dataset.fDomain||'').split(' ').includes(f.value):r.dataset['f'+f.dataset.sourceFacet[0].toUpperCase()+f.dataset.sourceFacet.slice(1)]===f.value));
  records.forEach((r,i)=>{r.dataset.order=i;});
  const reorder=()=>{const newest=sortSel&&sortSel.value==='newest';
    new Set(records.map(r=>r.parentElement)).forEach(box=>{const kids=records.filter(r=>r.parentElement===box);
      kids.sort((a,b)=>newest?((b.dataset.fDate||'').localeCompare(a.dataset.fDate||'')||(a.dataset.order-b.dataset.order)):(a.dataset.order-b.dataset.order));
      kids.forEach(k=>box.appendChild(k));});};
  const share=()=>{const q=new URLSearchParams(location.search);
    facets.forEach(f=>{if(f.value)q.set(f.dataset.sourceFacet,f.value);else q.delete(f.dataset.sourceFacet);});
    if(sortSel&&sortSel.value)q.set('sort',sortSel.value);else q.delete('sort');
    if(sourceInput.value.trim()&&!q.has('source'))q.set('q',sourceInput.value.trim());else q.delete('q');
    const s=q.toString();history.replaceState(null,'',location.pathname+(s?'?'+s:'')+location.hash);};
  const apply=()=>{
    const term=normalize(sourceInput.value.trim()); let shown=0, visibleLocators=0;
    const filtering=!!term||facets.some(f=>f.value);
    records.forEach(r=>{const ok=(!term||normalize(r.dataset.sourceSearch||'').includes(term))&&facetOk(r);r.hidden=!ok;if(ok){shown++;if(r.classList.contains('source-locator'))visibleLocators++;if(filtering){const d=r.closest('details');if(d)d.open=true;}}});
    $$('[data-source-also]').forEach(r=>{r.hidden=!((!term||normalize(r.dataset.sourceSearch||'').includes(term))&&facetOk(r));});   // B5: a link row, never counted
    if(filtering&&visibleLocators&&locatorDetails&&!locatorDetails.open)locatorDetails.open=true;
    if(noResults)noResults.hidden=shown!==0;
    if(status)status.textContent=TF(shown===1?'UI-JS-SOURCES-SHOWN-ONE':'UI-JS-SOURCES-SHOWN',{n:shown});   // TOOL-19
  };
  sourceInput.addEventListener('input',()=>{apply();share();});
  if(facetBox){
    const params=new URLSearchParams(location.search);
    facets.forEach(f=>{const v=params.get(f.dataset.sourceFacet);if(v&&[...f.options].some(o=>o.value===v))f.value=v;f.addEventListener('change',()=>{apply();share();});});
    if(sortSel){if(params.get('sort')==='newest')sortSel.value='newest';sortSel.addEventListener('change',()=>{reorder();share();});}
    if(params.get('q')&&!params.get('source'))sourceInput.value=params.get('q');
    const clear=$('[data-source-facets-clear]');
    if(clear)clear.addEventListener('click',()=>{facets.forEach(f=>{f.value='';});if(sortSel)sortSel.value='';sourceInput.value='';reorder();apply();share();});
    facetBox.hidden=false; reorder();
  }
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
    const offered=r.reason==='unknown'?`<p data-compare-not-offered>${esc(T('UI-JS-COMPARE-NOT-OFFERED'))}</p>`:'';   // B7
    out.innerHTML=`<div class="compare-url-error" role="alert" data-compare-url-error="${esc(r.reason)}"><h3>${esc(errorText.title)}</h3><p>${esc(detail)}</p><p>${esc(errorText.note)}</p>${offered}</div>`;
    if(compareStatus)compareStatus.textContent='';
    const cb=$('[data-compare-copy]'); if(cb)cb.disabled=true;   // TOOL-18: never copy a comparison the page is not showing
  };
  const draw=()=>{
    const records=compareSelects.map(sel=>data.find(x=>x.id===sel.value)).filter(Boolean);
    writeUrl();
    const cb=$('[data-compare-copy]'); if(cb)cb.disabled=records.length<2;
    const prompt=$('[data-compare-prompt]'); if(prompt)prompt.hidden=records.length>=2;   // G4: the prompt only while fewer than two are selected
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
