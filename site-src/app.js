(function(){
const $=(s,c=document)=>c.querySelector(s), $$=(s,c=document)=>[...c.querySelectorAll(s)];
const prefix=location.pathname.startsWith('/en/')?'/en':'/ar';
const isAr=document.documentElement.lang==='ar';

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
    const copied=$('#utility-status')?.dataset.copiedLabel||(isAr?'تم النسخ':'Copied');
    announceUtility(copied);
  }
  catch(e){prompt(promptLabel,text);}
}
$$('[data-cite]').forEach(b=>b.addEventListener('click',async()=>{
  const canonical=$('link[rel="canonical"]')?.href||location.href;
  const governed=$('meta[name="yfie-citation"]')?.content?.trim();
  const text=governed ? governed+' '+(isAr?'الرابط الحالي: ':'Current record: ')+canonical : document.title+' — '+canonical;
  await copyText(text,b,isAr?'انسخ الاستشهاد':'Copy citation');
}));
$$('[data-source-cite]').forEach(b=>b.addEventListener('click',async()=>{
  const text=(b.dataset.sourceCitation||'').trim(); if(!text)return;
  await copyText(text,b,isAr?'انسخ مرجع المصدر':'Copy source reference');
}));

let searchIndexPromise=null;
function loadSearch(){
  if(!searchIndexPromise) searchIndexPromise=fetch('/static-data/search_index.json').then(r=>{if(!r.ok)throw new Error('search index');return r.json();}).then(x=>Array.isArray(x)?x:(x.records||[]));
  return searchIndexPromise;
}
function esc(s){return String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));}
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
  const labels=isAr?{page:'صفحة',question:'سؤال',evidence:'سجل دليل',reading:'قراءة',measurement:'أولوية قياس',source:'مصدر',source_locator:'مرجع مصدر'}:{page:'Page',question:'Question',evidence:'Evidence record',reading:'Reading',measurement:'Measurement priority',source:'Source',source_locator:'Source reference'};
  return labels[t]||'';
}
// TOOL-23: summaries are shortened at a word boundary before escaping, with an ellipsis.
function clip(s,n){s=String(s||'');if(s.length<=n)return s;const cut=s.slice(0,n);const sp=cut.lastIndexOf(' ');return (sp>n*0.6?cut.slice(0,sp):cut).replace(/[\s,;:،؛]+$/,'')+'…';}
function renderHits(hits){
  if(!hits.length) return '<div class="empty" data-search-empty>'+(isAr?'لا توجد نتيجة تطابق هذا البحث. ولا يعني ذلك غياب الأدلة عن الموضوع؛ جرّب كلمات أخرى أو ابدأ من الأسئلة.':'No result matches this search. This does not mean there is no evidence on the topic; try other words or start from the questions.')+'</div>';
  return hits.map(x=>{
    const title=(isAr?(x.title_ar||x.question_ar||x.label_ar):(x.title_en||x.question_en||x.label_en))||x.id||'Evidence';
    const summary=(isAr?(x.summary_ar||''):(x.summary_en||''));
    let route=x.route||x.primary_route||x.public_route||'/evidence/'; route=String(route).replace(/^\/(ar|en)/,''); if(!route.startsWith('/'))route='/'+route;
    const type=typeLabel(x.object_type||x.type||'');
    const meta=(isAr?(x.meta_ar||''):(x.meta_en||''));   // PB-0493(c): period or document kind, in the reader's language (TOOL-10)
    return `<a class="search-hit" href="${prefix}${route}"><div><h4>${esc(title)}</h4>${summary?`<p>${esc(clip(summary,220))}</p>`:''}</div>${type?`<span class="meta">${esc(type)}${meta?' · '+esc(meta):''}</span>`:''}</a>`;
  }).join('');
}
function bindSearch(input,box,status){
  if(!input||!box)return;
  let timer;
  input.addEventListener('input',()=>{
    clearTimeout(timer);
    timer=setTimeout(async()=>{
      const term=normalize(input.value.trim());
      if(term.length<2){box.innerHTML=''; if(status)status.textContent=''; return;}
      if(status)status.textContent=isAr?'جارٍ البحث…':'Searching…';
      try{
        const idx=await loadSearch();
        const aliases=await loadAliases();
        const tokens=queryTokens(term);
        if(!tokens.length){box.innerHTML=renderHits([]);if(status)status.textContent=isAr?'0 نتيجة معروضة':'0 results shown';return;}
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
        if(status)status.textContent=isAr?`عدد النتائج المعروضة: ${scored.length}`:(scored.length===1?'1 result shown':`${scored.length} results shown`);   // TOOL-19
      }catch(e){
        box.innerHTML='<div class="empty">'+(isAr?'تعذر تحميل البحث الآن. يمكنك متابعة التصفح من الأقسام الرئيسية.':'Search could not be loaded. You can continue from the main sections.')+'</div>';
        if(status)status.textContent=isAr?'تعذر تحميل البحث':'Search unavailable';
      }
    },100);
  });
}

$$('[data-search-input]').forEach(input=>{
  const scope=input.closest('.search-dialog-panel')||input.parentElement?.parentElement||document;
  const box=$('[data-search-results]',scope)||$('#search-results');
  const status=$('[data-search-status]',scope);
  bindSearch(input,box,status);
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
    if(status)status.textContent=isAr?`عدد المصادر والمراجع المعروضة: ${shown}`:(shown===1?'1 source or reference shown':`${shown} sources or references shown`);   // TOOL-19
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
      status.textContent=isAr?'لم يُعثر في دليل المصادر على مرجع المصدر الوارد في هذا الرابط. هذه مشكلة في الرابط، وليست معلومة عن الأدلة؛ تُعرض المصادر كلها أدناه.':'The source reference in this link was not found in the source directory. This is a problem with the link, not information about the evidence; all sources are shown below.';
    }
  }
}

// Corrections/version entry preserves the originating evidence record without inventing a history event.
const correctionContext=$('[data-correction-context]');
if(correctionContext){
  // P2.3: the originating record survives into Corrections and Contact; a malformed or unknown reference is a technical link error.
  const record=new URLSearchParams(location.search).get('record');
  const known=new Set(window.__RECORD_IDS__||[]);
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
  const data=window.__COMPARE__||[];
  const contractDimensions=Array.isArray(window.__COMPARE_DIMENSIONS__)?window.__COMPARE_DIMENSIONS__:[];
  const labels=isAr?{
    definition:'التعريف',universe:'المجتمع / قاعدة الاحتساب',period:'الفترة',method:'الطريقة',source:'مرجع المصدر',currentness:'حداثة الدليل',boundary:'ما لا يُستنتج',
    same:'متطابق في الحقول المنظمة',different:'مختلف',missing:'غير متاح للحكم',informational:'للتتبع',sameRecord:'السجل نفسه مكرر',notDirect:'ليست مقارنة مباشرة',unresolved:'لا يمكن إثبات قابلية المقارنة المباشرة',qualified:'مقارنة مؤهلة فقط',aligned:'متوافقة بنيويًا ضمن الحقول المتاحة',
    sameRecordCopy:'اختير سجل الدليل نفسه أكثر من مرة. أزل التكرار قبل الحكم على المقارنة بين أدلة مستقلة.',
    notDirectCopy:'يختلف التعريف أو المجتمع أو الطريقة المسجلة بين هذه السجلات. تعامل معها بوصفها مقاييس مختلفة ما لم تذكر سجلاتها خلاف ذلك، ولا تعرض قيمها على مقياس مشترك.',
    unresolvedCopy:'تنقص حقول لازمة للحكم على المقارنة المباشرة. الغياب لا يعني التوافق؛ لذلك تبقى المقارنة غير محسومة.',
    qualifiedCopy:'تتوافق الحقول البنيوية اللازمة، لكن الفترة أو حداثة الدليل تختلف. استخدم المقارنة مع هذا القيد ظاهرًا.',
    alignedCopy:'يتطابق التعريف والمجتمع والطريقة المسجلة. ولا يثبت ذلك تكافؤ المعنى خارج الحقول المعتمدة المعروضة هنا.',
    dimension:'بُعد المقارنة',assessment:'الحكم',openRecord:'افتح سجل الدليل',noMerge:'لا تُدمج القيم ولا تُنشئ متوسطًا أو رقمًا وسطًا أو معامل تحويل من هذه المقارنة.',table:'تفاصيل مقارنة الأدلة',selected:'سجلات مختارة'
  }:{
    definition:'Definition',universe:'Population / base',period:'Period',method:'Method',source:'Source reference',currentness:'Evidence currency',boundary:'What not to conclude',
    same:'Same controlled fields',different:'Different',missing:'Not available to judge',informational:'Trace only',sameRecord:'Same record selected more than once',notDirect:'Not a direct comparison',unresolved:'Direct comparability cannot be established',qualified:'Qualified comparison only',aligned:'Structurally aligned on available fields',
    sameRecordCopy:'The same Evidence Record is selected more than once. Remove duplicates before judging comparability across independent evidence.',
    notDirectCopy:'The recorded definition, population or method differs between these records. Treat them as different measures unless their records say otherwise, and do not present their values on a common scale.',
    unresolvedCopy:'A field required to judge direct comparability is missing. Missing does not mean compatible, so the comparison remains unresolved.',
    qualifiedCopy:'The required structural fields align, but period or evidence currency differs. Use the comparison only with that qualification visible.',
    alignedCopy:'The recorded definition, population and method match. This does not establish equivalence beyond the governed fields shown here.',
    dimension:'Comparison dimension',assessment:'Assessment',openRecord:'Open Evidence Record',noMerge:'Do not merge values, manufacture a midpoint, average disagreement or infer a conversion scalar from this comparison.',table:'Evidence comparison details',selected:'records selected'
  };
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
  const recordLink=x=>x.route?`<a class="button ghost" href="${prefix}${esc(x.route)}">${esc(labels.openRecord)} — ${esc(x.title)}</a>`:'';
  // P2.1: the comparison is shareable. URL state is ?records=ID,ID[,ID[,ID]] in slot order (each ID percent-encoded,
  // commas literal). The URL always reflects the comparison shown; reload, a copied link or a language switch
  // (which keeps the query) reproduces it. A malformed or unknown link is a technical input error, never an evidence verdict.
  const errorText=isAr?{
    title:'تعذّرت قراءة رابط المقارنة',
    count:'يجب أن يسمّي الرابط من سجلين إلى أربعة سجلات أدلة، مفصولة بفواصل.',
    malformed:'يحتوي الرابط على مرجع سجل غير صالح.',
    unknown:'يسمّي الرابط سجلًا غير متاح للمقارنة هنا: ',
    note:'هذه مشكلة في الرابط، وليست نتيجة عن الأدلة. اختر السجلات أدناه لبدء مقارنة.'
  }:{
    title:'This comparison link could not be read',
    count:'The link must name two to four Evidence Records, separated by commas.',
    malformed:'The link contains a record reference that is not valid.',
    unknown:'The link names a record that is not available for comparison here: ',
    note:'This is a problem with the link, not a finding about the evidence. Choose records below to start a comparison.'
  };
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
    const head=records.map(x=>`<th scope="col">${esc(x.title)}</th>`).join('');
    const body=rows.map(r=>`<tr data-compare-state="${esc(r.state)}"><th scope="row">${esc(labels[r.field]||r.field)}</th>${records.map(x=>`<td>${esc(x[r.field]||'—')}</td>`).join('')}<td><span class="compare-state">${esc(r.label)}</span></td></tr>`).join('');
    const boundaries=records.some(x=>x.boundary)?`<div class="compare-boundaries">${records.map(x=>`<article><strong>${esc(x.title)}</strong><p>${esc(x.boundary||'—')}</p></article>`).join('')}</div>`:'';
    out.innerHTML=`<section class="compare-verdict" data-compare-verdict="${esc(v.state)}" data-noncolour-semantic="text-label-structure"><div class="eyebrow">${esc(labels.assessment)}</div><h3>${esc(v.title)}</h3><p>${esc(v.copy)}</p><p class="compare-no-merge">${esc(labels.noMerge)}</p></section><div class="table-wrap" tabindex="0" role="region" aria-label="${esc(labels.table)}" data-noncolour-semantic="caption-headers-text-labels"><table class="compare-table"><caption class="sr-only">${esc(labels.table)}</caption><thead><tr><th scope="col">${esc(labels.dimension)}</th>${head}<th scope="col">${esc(labels.assessment)}</th></tr></thead><tbody>${body}</tbody></table></div>${boundaries}<div class="compare-record-actions">${records.map(recordLink).join('')}</div>`;
    if(compareStatus)compareStatus.textContent=`${v.title}. ${records.length} ${labels.selected}.`;
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
