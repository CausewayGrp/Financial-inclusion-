# -*- coding: utf-8 -*-
"""The reference stylesheet as one string (written to out/assets/yfie.css by the build). Extracted once from the
converged D1 composer (design/exploration/d1_canvas/boards/t4.py, version 5) and maintained here from now on.
Tokens are the :root custom properties at the top; the Lock (design/01_FOUNDATIONS.md §4) governs what they carry."""

FONT_FACES = """@font-face{font-family:'IBM Plex Sans';font-style:normal;font-weight:400;font-display:swap;src:url('/assets/fonts/ibm-plex-sans/IBMPlexSans-Regular.woff2') format('woff2')}
@font-face{font-family:'IBM Plex Sans';font-style:normal;font-weight:500;font-display:swap;src:url('/assets/fonts/ibm-plex-sans/IBMPlexSans-Medium.woff2') format('woff2')}
@font-face{font-family:'IBM Plex Sans';font-style:normal;font-weight:600;font-display:swap;src:url('/assets/fonts/ibm-plex-sans/IBMPlexSans-SemiBold.woff2') format('woff2')}
@font-face{font-family:'IBM Plex Sans Arabic';font-style:normal;font-weight:400;font-display:swap;src:url('/assets/fonts/ibm-plex-sans-arabic/IBMPlexSansArabic-Regular.woff2') format('woff2')}
@font-face{font-family:'IBM Plex Sans Arabic';font-style:normal;font-weight:500;font-display:swap;src:url('/assets/fonts/ibm-plex-sans-arabic/IBMPlexSansArabic-Medium.woff2') format('woff2')}
@font-face{font-family:'IBM Plex Sans Arabic';font-style:normal;font-weight:600;font-display:swap;src:url('/assets/fonts/ibm-plex-sans-arabic/IBMPlexSansArabic-SemiBold.woff2') format('woff2')}"""

CSS = r"""/* Yemen Financial Inclusion Evidence — reference stylesheet (D1, direction T4 · Instrument). Generated once from the converged composer, then maintained here. No inline style anywhere in the site. */
:root{--paper:#FFFFFF;--plaster:#F5F1E9;--ink:#17212B;--ink-2:#3D4954;--mute:#646F79;--rule:#D8DDE2;--rule-2:#AEB7BF;--ochre:#7A5A1D;--ochre-line:#D6B86A;--counter:#1E5650;
--fs-body:17px;--lh-body:1.6;--fs-display:32px;--lh-display:1.1;--fs-q:20px;--lh-q:1.4;--fs-st:19px;--lh-st:1.5;--fs-bnd:18px;--lh-bnd:1.55;--fs-clock:13.5px;--lh-clock:1.4;--fs-rubric:12px;--fs-src:14.5px;--lh-src:1.5;--fs-nav:15px;--fs-read:18px;--lh-read:1.65;--measure:64ch;--font:'IBM Plex Sans',sans-serif}
html[dir=rtl]{--fs-body:18px;--lh-body:1.9;--fs-display:30px;--lh-display:1.35;--fs-q:21px;--lh-q:1.7;--fs-st:20px;--lh-st:1.7;--fs-bnd:19px;--lh-bnd:1.8;--fs-clock:14.5px;--lh-clock:1.7;--fs-rubric:14px;--fs-src:15.5px;--lh-src:1.75;--fs-nav:16px;--fs-read:19.5px;--lh-read:1.95;--measure:34em;--font:'IBM Plex Sans Arabic',sans-serif}
html{background:var(--paper);color:var(--ink);font-family:var(--font);font-size:var(--fs-body);line-height:var(--lh-body);font-variant-numeric:tabular-nums}
body{margin:0}
a{color:inherit;text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:.16em;text-decoration-color:var(--rule-2)}
h1,h2,h3,h4{margin:0;font-weight:600}
b,strong,th{font-weight:600}   /* emphasis is the semibold role; the browser's bold decides nothing (D6) */
h1{font-size:var(--fs-display);line-height:var(--lh-display);text-wrap:balance}[dir=ltr] h1{letter-spacing:-.012em}
.nw{white-space:nowrap}
h2{font-size:var(--fs-q);line-height:var(--lh-q)}
h3{font-size:17px;line-height:1.4}
.mt8{margin-top:8px}.mt10{margin-top:10px}.mt12{margin-top:12px}.mt16{margin-top:16px}.mt18{margin-top:18px}
.first-obj{border-top:0;padding-top:0}
.clocks{display:flex;flex-wrap:wrap;gap:10px 32px;margin-top:6px}
p{margin:0 0 .85em}p:last-child{margin-bottom:0}
.tbtn{background:none;border:0;padding:0;font:inherit;color:inherit;text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:.16em;text-decoration-color:var(--rule-2);cursor:pointer}
.rubric{display:block;font-size:var(--fs-rubric);line-height:1.4;font-weight:600;color:var(--ochre);margin:0}
[dir=ltr] .rubric{text-transform:uppercase;letter-spacing:.1em}
/* A rubric that IS a section heading must read as one in Arabic. English marks it with uppercase and tracking — two
   devices a script without case cannot use, and which are correctly withheld here — so in Arabic the heading was left
   30 % smaller than the prose it introduces (the D7 Arabic lens, on the record's seven questions at 390 px). In a
   script where size and weight carry the whole hierarchy, a heading is never smaller than its body (DL-D7-012). */
[dir=rtl] h2.rubric,[dir=rtl] h3.rubric{font-size:calc(var(--fs-body) + 2px);line-height:1.5}
.clock{display:flex;flex-direction:column;gap:2px;font-size:var(--fs-clock);line-height:var(--lh-clock)}
.clock .k{font-weight:600;color:var(--mute)}
.clock .v{font-weight:600;color:var(--ink)}
.ref{font-size:var(--fs-clock);line-height:var(--lh-clock);color:var(--mute);font-weight:500}
.ref b{color:var(--ink-2);font-weight:600}
.q{font-size:var(--fs-q);line-height:var(--lh-q);font-weight:400}
.q a{text-decoration-color:var(--ochre-line)}
.st{font-size:var(--fs-st);line-height:var(--lh-st);font-weight:400;max-width:var(--measure)}
.qa.first .st,.head .st{font-weight:500}
.st b{font-weight:600}
.body{max-width:var(--measure)}.body p{color:var(--ink-2)}
.read{font-size:var(--fs-read);line-height:var(--lh-read);max-width:var(--measure)}
.small{font-size:var(--fs-src);line-height:var(--lh-src);color:var(--ink-2)}
.bnd{border-top:3px double var(--counter);padding-top:12px;margin-top:22px;color:var(--counter)}.bnd>p,.bnd>div,.bnd h2,.bnd h3{max-width:var(--measure)}
.bnd .rubric{color:var(--counter);margin-bottom:8px}
.bnd p{font-size:var(--fs-bnd);line-height:var(--lh-bnd);font-weight:500}
.bnd h2{color:var(--counter)}
/* product bar */
.bar{border-bottom:2px solid var(--ink)}
.bar-in{max-width:1240px;margin:0 auto;padding:10px 16px;display:flex;align-items:center;gap:14px}
.brand{display:flex;align-items:center;gap:12px;text-decoration:none;margin-inline-end:auto}
.brand img{width:40px;height:40px}
.brand-text{display:flex;flex-direction:column;gap:2px;min-width:0}
.brand-pub{font-weight:600;font-size:11.5px;line-height:1;letter-spacing:.02em;color:var(--ochre)}
.brand-name{font-weight:600;font-size:13px;line-height:1.25;max-width:22ch}
.nav{display:none}
.controls{display:flex;align-items:center;gap:12px;font-size:14px;font-weight:500;white-space:nowrap}
.controls .tbtn,.controls a{text-decoration:none}
.controls .lang{border:1px solid var(--rule-2);padding:6px 9px}
.controls .cite,.controls .report{display:none}
/* page and object */
.page{max-width:1240px;margin:0 auto;padding:18px 16px 40px;display:flex;flex-direction:column;gap:18px}
.obj{display:flex;flex-direction:column;gap:14px;border-top:3px solid var(--ink);padding-top:16px}
.obj.page-obj{gap:18px}
.obj .head{display:flex;flex-direction:column;gap:8px}
.qa{display:flex;flex-direction:column;gap:6px;padding-top:14px;border-top:1px solid var(--rule)}
.qa .rubric{color:var(--ochre)}
.rubric .n{color:var(--mute);margin-inline-end:.6em}
.qa.first{border-top:0;padding-top:0}
.crumb{font-size:var(--fs-clock);color:var(--mute);margin-bottom:2px}
.crumb a{text-decoration:none}
.strip{display:grid;grid-template-columns:minmax(0,1fr);gap:0;padding:12px 0 4px;border-top:1px solid var(--rule)}
.strip a{display:flex;gap:10px;align-items:baseline;padding:11px 0;font-size:var(--fs-src);line-height:var(--lh-src);text-decoration:none;border-bottom:1px solid var(--rule)}
.strip a .n{color:var(--mute);font-weight:600;min-width:1.6em}
.compact{display:flex;flex-direction:column;gap:6px;padding:14px 0;border-top:1px solid var(--rule)}
.compact:first-child{border-top:0}
.compact .q{font-size:calc(var(--fs-q) - 1px)}
.compact .open{font-size:var(--fs-src);font-weight:500}
.objs{display:flex;flex-direction:column;border-top:1px solid var(--rule-2)}
.objs>.compact:first-child{border-top:0}
.paced p{max-width:var(--measure)}
.paced .sent{display:block;margin:0 0 .45em;font-size:var(--fs-st);line-height:var(--lh-st);font-weight:400}
.paced .sent.res{font-weight:600;border-top:1px solid var(--ochre-line);padding-top:.6em;margin-top:.4em}
.paced .compact.bound{border-top:0;border-inline-start:2px solid var(--ochre-line);padding:4px 0 4px 14px;margin:0 0 20px}
[dir=rtl] .paced .compact.bound{padding:4px 14px 4px 0}
.paced .compact.bound .q{font-size:var(--fs-body)}
.actions{display:flex;flex-wrap:wrap;gap:6px 26px;margin-top:14px;font-weight:600}
.actions a,.actions .tbtn,.open a,.src .acts a,.src .acts .tbtn,.fig .foot a,.fig .foot .tbtn,.small a,.gets a,.edges a,.chip{display:inline-block;padding:3px 0;min-height:24px}
.actions a{text-decoration-color:var(--ochre-line);text-decoration-thickness:2px}
.qlist{list-style:none;margin:0;padding:0;counter-reset:q}
.qlist li{display:grid;grid-template-columns:34px minmax(0,1fr);gap:10px;padding:14px 0;border-top:1px solid var(--rule)}
.qlist li::before{counter-increment:q;content:counter(q,decimal-leading-zero);font-size:var(--fs-clock);font-weight:600;color:var(--mute);padding-top:5px}
.qlist .gets{margin-top:4px}
.src{display:flex;flex-direction:column;gap:6px;padding:14px 0;border-top:1px solid var(--rule)}
.src:first-child{border-top:0;padding-top:0}
.src strong{font-size:var(--fs-body)}
.src .kind,.src .rref{font-size:var(--fs-clock);color:var(--ink-2);font-weight:500}
.src .acts{display:flex;flex-wrap:wrap;gap:6px 18px;font-size:var(--fs-src);font-weight:500}
.src .rights{font-size:var(--fs-clock);color:var(--mute);margin:0}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:6px}
.chip{display:inline-block;border:1px solid var(--rule-2);padding:3px 8px;font-size:var(--fs-clock);text-decoration:none}
details.more summary{cursor:pointer;list-style:none;font-weight:600;font-size:var(--fs-src);color:var(--ink)}
details.more summary::-webkit-details-marker{display:none}
details.more summary::before{content:"+ ";color:var(--ochre)}
details.more[open] summary::before{content:"− "}
details.more .qa{margin-top:10px}
.util{display:flex;flex-direction:column;gap:10px;padding:16px 0 0;border-top:1px solid var(--rule)}
.util .actions{margin-top:0}
/* spine */
.spine{display:flex;flex-direction:column;gap:14px;padding:16px 0 0;margin-top:8px;border-top:3px solid var(--ink)}
.spine h3{font-size:var(--fs-rubric);color:var(--ochre);font-weight:600;margin:0 0 8px}
[dir=ltr] .spine h3{text-transform:uppercase;letter-spacing:.1em}
.spine:not(.foot-spine){display:none}
.foot-spine .index{display:block}
.spine ul{list-style:none;margin:0;padding:0}
.spine li{border-top:1px solid var(--rule-2);font-size:var(--fs-src);line-height:var(--lh-src)}
.spine li a{display:block;padding:9px 0}
.spine li:first-child{border-top:0;padding-top:0}
.spine a{text-decoration:none}
.spine .index li a{display:flex;gap:10px;padding:9px 0}
.spine .index .n{color:var(--mute);font-weight:600;min-width:1.6em}
.spine .index a[aria-current]{font-weight:600}
/* reading */
.pull{margin:22px 0;padding:0 0 0 20px;border-inline-start:2px solid var(--ochre-line);font-size:var(--fs-q);line-height:var(--lh-q);font-weight:500;max-width:var(--measure)}
[dir=rtl] .pull{padding:0 20px 0 0}
.rlist{padding-inline-start:1.2em}
.essay section{padding:6px 0 26px}
.essay section+section{border-top:1px solid var(--rule);padding-top:24px}
.essay h2{margin-bottom:10px}
.fig{background:var(--plaster);padding:18px 16px 16px;margin:20px 0 4px;border-top:3px solid var(--ink)}
.fig .fig-t{font-size:var(--fs-q);line-height:var(--lh-q);margin-bottom:6px;font-weight:600}
.fig .ph{font-size:var(--fs-clock);font-weight:600;color:var(--ink-2);margin:0 0 6px}
.fig .cap{font-size:var(--fs-clock);line-height:var(--lh-clock);color:var(--ink-2);margin:0 0 4px;max-width:70ch}
.panels{display:flex;flex-direction:column;gap:20px;padding-top:12px;border-top:1px solid var(--rule-2);margin-top:12px}
.lane h3{margin:0 0 6px;font-size:var(--fs-clock);line-height:var(--lh-clock);font-weight:600;color:var(--ink)}
.p1{display:flex;flex-direction:column;gap:2px;margin-top:6px}
.p1 .row{display:grid;grid-template-columns:minmax(0,1fr);gap:0}
.p1 .rl{font-size:var(--fs-clock);line-height:var(--lh-clock);font-weight:600;padding-top:8px;text-wrap:balance}
.p1 svg{display:block;overflow:visible;font-family:var(--font)}
.p1 .ax-row{margin-top:2px}
.p1 .ax-unit{font-size:var(--fs-clock);color:var(--ink-2);font-weight:500;align-self:start}
.cap.same{margin:2px 0 4px}.cap.note{margin-top:10px}
.between{border-top:3px double var(--counter);padding-top:8px;margin:10px 0 6px;font-size:var(--fs-clock);font-weight:600;color:var(--counter)}
.lanes{display:flex;flex-direction:column;gap:14px;margin-top:8px}
.lane .base{display:block;font-size:var(--fs-clock);color:var(--ink-2);font-weight:500;margin:-2px 0 4px}
.lanes .between{margin:0}
.alt{margin-top:16px;border-top:1px solid var(--rule-2);padding-top:10px}
.alt-h{font-size:var(--fs-clock);font-weight:600;color:var(--ink-2);margin:0 0 6px}
.fig .foot{display:flex;flex-direction:column;gap:6px;font-size:var(--fs-clock);line-height:var(--lh-clock);color:var(--ink-2);margin-top:12px}
.fig .foot .b{color:var(--counter);font-weight:500;font-size:var(--fs-src)}
svg.rv2{display:block;overflow:visible;font-family:var(--font)}
.lane{min-width:0}
.canon{unicode-bidi:isolate;overflow-wrap:anywhere}
.alt-p{padding-top:8px}
.axis{stroke:var(--ink);stroke-width:1}.grid{stroke:var(--rule-2);stroke-width:1;stroke-dasharray:2 3}.tick{stroke:var(--ink);stroke-width:1}.stem{stroke:var(--rule-2);stroke-width:1}
.lbl{font-size:12px;fill:var(--ink-2);font-weight:500}.lbl.origin{fill:var(--ink);font-weight:600}.unit{font-size:12px;fill:var(--ink-2);font-weight:600}
.val{font-size:12.5px;fill:var(--ink);font-weight:600}.val.small{font-size:11px}
.mark.a{fill:var(--ink)}.mark.b{fill:var(--plaster);stroke:var(--ink);stroke-width:2}
.path{stroke:var(--ink);stroke-width:1.5}
.rvtab{border-collapse:collapse;width:100%;font-size:var(--fs-clock);line-height:var(--lh-clock);margin-top:10px;background:var(--paper)}
.rvtab caption{text-align:start;font-weight:600;color:var(--ink-2);padding:8px 0}
.rvtab th,.rvtab td{text-align:start;padding:7px 8px;border-top:1px solid var(--rule);vertical-align:top}.rvtab td{font-variant-numeric:tabular-nums;white-space:nowrap}
.rvtab thead th{border-top:1px solid var(--ink);font-weight:600}
.rvtab .state{color:var(--mute)}.rvtab .marker{font-weight:600;color:var(--counter)}
/* institutional band */
.inst{background:var(--plaster);border-top:3px solid var(--ink);margin-top:24px}
.inst-in{max-width:1240px;margin:0 auto;padding:28px 16px 20px;display:flex;flex-direction:column;gap:22px}
.inst .trust{display:flex;flex-direction:column;gap:8px}
.inst .trust h3{font-size:var(--fs-rubric);color:var(--ochre)}
[dir=ltr] .inst .trust h3{text-transform:uppercase;letter-spacing:.1em}
.inst .trust nav{display:flex;flex-wrap:wrap;gap:8px 20px;font-size:var(--fs-body);font-weight:500}
.inst .trust a{text-decoration:none}
.inst .groups{display:flex;flex-direction:column;gap:16px;font-size:var(--fs-src)}
.inst .groups div{display:flex;flex-direction:column;gap:5px}
.inst .groups strong{font-size:var(--fs-rubric);color:var(--ochre)}
[dir=ltr] .inst .groups strong{text-transform:uppercase;letter-spacing:.1em}
.inst .groups a{text-decoration:none}
.inst .id{display:flex;gap:12px;align-items:center;font-size:var(--fs-src);color:var(--ink-2)}
.inst .id img{width:40px;height:40px}
.inst .fine{border-top:1px solid var(--rule-2);padding-top:12px;font-size:var(--fs-clock);color:var(--mute)}
/* ---- shell mechanics (brief §19): skip link, focus, screen-reader text, table wrap, menu, search dialog ---- */
.skip{position:absolute;inset-inline-start:16px;top:-200px;padding:12px 16px;background:var(--paper);color:var(--ink);border:3px double var(--counter);z-index:1000;text-decoration:none;font-weight:600}
.skip:focus{top:12px}
:focus-visible{outline:3px double var(--counter);outline-offset:3px}
.sr-only{position:absolute!important;width:1px!important;height:1px!important;padding:0!important;margin:-1px!important;overflow:hidden!important;clip:rect(0,0,0,0)!important;white-space:nowrap!important;border:0!important}
.table-wrap{overflow-x:auto;max-width:100%}
.table-wrap:focus-visible{outline-offset:6px}
.noscript{background:var(--plaster);border-bottom:1px solid var(--rule-2);padding:10px 16px;font-size:var(--fs-src)}
.bar-in{position:relative}
.nav.open{display:flex;flex-direction:column;gap:2px;position:absolute;inset-inline:0;top:100%;background:var(--paper);border-bottom:2px solid var(--ink);padding:12px 16px;z-index:20;font-size:var(--fs-nav);font-weight:500}
.nav.open a{padding:10px 0;text-decoration:none;border-bottom:1px solid var(--rule)}
.nav.open .group{display:flex;flex-direction:column}.nav.open .tbtn.m-only{align-self:flex-start;margin-top:10px}
.nav.open .glabel{color:var(--mute);font-size:12px;font-weight:600;padding:10px 0 2px}
[dir=ltr] .nav.open .glabel{text-transform:uppercase;letter-spacing:.08em}
.controls .tbtn,.controls a{min-height:44px}
dialog.search{border:0;padding:0;max-width:min(680px,92vw);width:100%;background:var(--paper);color:var(--ink);border-top:3px solid var(--ink)}
dialog.search::backdrop{background:rgba(23,33,43,.55)}
.search-panel{padding:18px 20px 22px;display:flex;flex-direction:column;gap:12px}
.search-head{display:flex;justify-content:space-between;align-items:baseline;gap:16px}
.search-head strong{font-size:var(--fs-q)}
.search-input{width:100%;box-sizing:border-box;padding:12px 14px;border:1px solid var(--rule-2);background:var(--paper);font-size:var(--fs-body)}
.search-input:focus-visible{outline-offset:0}
.search-status{font-size:var(--fs-clock);color:var(--ink-2);min-height:1.4em}
.cite-preview{flex-basis:100%;border-top:1px solid var(--rule);padding-top:8px}.cite-preview .cite-h{margin:0;font-size:var(--fs-clock);font-weight:600;color:var(--ink-2)}.cite-preview .cite-text{margin:4px 0 0;font-size:var(--fs-src);color:var(--ink-2);overflow-wrap:anywhere}.cite-preview .cite-text bdi{white-space:normal;overflow-wrap:anywhere}.cite-long{margin-top:6px}.cite-long summary{cursor:pointer;font-size:var(--fs-clock);color:var(--ink-2)}.cite-long .tbtn{margin-top:6px}
.reuse-once{border-inline-start:3px solid var(--rule-2);padding-inline-start:10px}.src-also{margin:8px 0 0;font-size:var(--fs-src)}
@media print{.cite-preview,[data-print]{display:none}}
.search-type{margin-top:6px;padding:6px 10px;border:1px solid var(--rule-2);background:var(--paper);font-size:var(--fs-src);max-width:100%}
.search-results{display:flex;flex-direction:column;max-height:60vh;overflow:auto}
.search-results a{display:block;padding:10px 0;border-top:1px solid var(--rule);text-decoration:none}
.search-results .empty{color:var(--ink-2)}
.source-target{outline:3px double var(--counter);outline-offset:6px}
@media (prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important;scroll-behavior:auto!important}}
@media (forced-colors:active){.bnd,.between,.obj,.fig,.inst,.spine,.strip a,.compact,.qa{border-color:CanvasText!important}.mark.a{fill:CanvasText}.mark.b{stroke:CanvasText;fill:Canvas}.path,.axis,.tick,.stem,.grid{stroke:CanvasText}.lbl,.lbl.origin,.val,.unit{fill:CanvasText}.rubric,.clock .k,.clock .v,.lane .base,.between,.bnd,.bnd p,.bnd h2{color:CanvasText}}
@media print{
/* D1: what the print system of D6 (CSS_D6, the last block of the stylesheet) does not restate */
.bar .nav,.controls,dialog,.noscript,.skip,.strip,.spine .index,.inst .groups,.util .actions,.fig .foot button{display:none!important}
.page{display:block;padding:0}
}
@media (min-width:600px){
.p1 .row{grid-template-columns:minmax(150px,.38fr) minmax(0,1fr);gap:0 16px;align-items:center}
.p1 .rl{padding-top:0}
.lanes{flex-direction:row;gap:20px;align-items:stretch}
.lanes>.lane{flex:1 1 0;min-width:0}
.lanes .between{border-top:0;border-inline-start:3px double var(--counter);padding:0 0 0 12px;align-self:center;max-width:8em;flex:0 0 auto}
[dir=rtl] .lanes .between{padding:0 12px 0 0}
.strip{grid-template-columns:minmax(0,1fr) minmax(0,1fr);column-gap:24px}
}
@media (min-width:900px){
:root{--fs-display:46px;--fs-q:23px;--fs-st:21px;--fs-body:17px;--fs-read:19px;--fs-bnd:19px}
html[dir=rtl]{--fs-display:42px;--fs-q:24px;--fs-st:22px;--fs-body:18px;--fs-read:20px;--fs-bnd:20px}
.bar-in{padding:14px 32px;gap:32px}
.brand{flex-shrink:0}
.brand img{width:48px;height:48px}.brand-name{font-size:14px;max-width:none}.brand-pub{font-size:12.5px}
.nav{display:flex;flex-wrap:wrap;gap:4px 24px;font-size:var(--fs-nav);font-weight:500;align-items:baseline}
.nav a{text-decoration:none;padding:6px 0;border-bottom:2px solid transparent}
.nav a[aria-current=page]{border-bottom-color:var(--ink)}
.nav .group{display:inline-flex;gap:14px;align-items:baseline}
.nav .group{border-inline-start:1px solid var(--rule-2);padding-inline-start:18px}.nav .glabel{color:var(--ink-2);font-size:12px;font-weight:600;padding:6px 0;line-height:calc(var(--fs-nav) * 1.4)}
[dir=ltr] .nav .glabel{text-transform:uppercase;letter-spacing:.08em}
.controls{gap:16px}
.controls .cite,.controls .report{display:inline;color:var(--ink-2)}
.controls .menu{display:none}
.nav .m-only{display:none}
.page{padding:28px 32px 56px;display:grid;grid-template-columns:minmax(0,1fr) 280px;column-gap:40px;row-gap:0;align-items:start}
.page>.obj{grid-column:1;max-width:840px}
.spine:not(.foot-spine){display:flex}
.spine{grid-column:2;grid-row:1 / span 20;position:sticky;top:20px;margin-top:0;padding:0 0 0 20px;border-top:0;border-inline-start:1px solid var(--rule-2);max-height:calc(100vh - 40px);overflow:auto}
[dir=rtl] .spine{padding:0 20px 0 0}
.spine .index{display:block}
.strip{display:none}
.foot-spine{display:none}
.obj.page-obj{gap:22px;padding-top:22px}
.paced .sent{font-size:22px;line-height:1.45}
[dir=rtl] .paced .sent{font-size:23px;line-height:1.7}
.bnd{margin-top:26px;padding-top:14px}
.inst-in{padding:36px 32px 24px;display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,2fr);gap:28px 48px}
.inst .trust{grid-column:1 / -1}
.inst .groups{flex-direction:row;gap:36px}
.inst .fine{grid-column:1 / -1}
.essay section{padding:8px 0 30px}
h1{max-width:22ch}
}
@media (min-width:1200px){
.page{grid-template-columns:minmax(0,1fr) 300px;column-gap:48px}
.qa{display:grid;grid-template-columns:220px minmax(0,1fr);gap:4px 36px;padding-top:16px}
.qa>:first-child{grid-column:1}
.qa>:not(:first-child){grid-column:2}
.qa.compare>:not(:first-child){grid-column:1 / -1}
.qa .rubric{padding-top:4px}
.compact{display:grid;grid-template-columns:220px minmax(0,1fr);gap:4px 36px;padding:16px 0}
.compact>.clock{grid-column:1;grid-row:1 / span 4}
.compact>:not(.clock){grid-column:2}
.paced .compact.bound{display:flex;flex-direction:column}
}
"""

# D2 additions — the same tokens and roles; the families beyond the trio, the D2 figures, the tools' hooks.
CSS_D2 = r"""/* ---- D2: families, figures, tools (same tokens; maintained with CSS above) ---- */
[hidden]{display:none!important}
.chain .source-locator,.hublist a,.src .source-url,.chron a,.deps a,[data-evidence-landscape] a{display:inline-block;padding:3px 0;min-height:24px}
/* 2.5.8, measured at EAD-02: these three sat 1–2 px under the 24 px minimum with neighbours closer than 24 px, so
   neither the inline nor the spacing exception carried them. The rule is the one above, applied where it was missed. */
.groups a,details.more>summary,details.more .rlist a{display:inline-block;padding:3px 0;min-height:24px}
.head .q{font-size:var(--fs-q);line-height:var(--lh-q);color:var(--ink-2);margin:0}
.crumb+.rubric{margin-top:4px}
.unit-l{display:block;font-weight:500;color:var(--ink-2);font-size:var(--fs-rubric);letter-spacing:0;text-transform:none;margin-top:2px}
.pop b,.bnd-line b{font-weight:600}
.bnd-line{color:var(--counter)}
.rref{font-size:var(--fs-clock);color:var(--ink-2);font-weight:500;margin-inline-start:.8em}
.count{color:var(--mute);font-weight:500}
/* question entry */
.clusters-lead{margin-top:26px}
.clusters-lead .q{margin:4px 0 0;max-width:var(--measure)}
.clusters-lead .small{margin-top:6px}
.clusters{display:flex;flex-direction:column;gap:6px;margin-top:10px}
.cluster h3{font-size:var(--fs-rubric);color:var(--ochre);font-weight:600;padding-top:14px;border-top:3px solid var(--ink);margin-top:14px}
[dir=ltr] .cluster h3{text-transform:uppercase;letter-spacing:.1em}
.cluster:first-child h3{margin-top:0}
/* domain answer */
.qa.figs>div:first-child{align-self:start}
.multiple{display:flex;flex-direction:column;gap:0}
.multiple .fig{margin-top:0;border-top-width:1px}
.multiple .fig:first-child{border-top-width:3px;margin-top:20px}
.fig+.fig{margin-top:22px}
details.more .qa h3{font-size:var(--fs-body);font-weight:600;margin-bottom:4px}
/* figures (D2) */
.bar{fill:var(--ink)}
.bars .p1{gap:4px}
.pair{border-top:1px solid var(--rule);margin-top:10px;padding-top:6px}
.gap{margin:6px 0 2px;font-size:var(--fs-clock);line-height:var(--lh-clock);color:var(--ink-2);font-weight:500;padding-inline-start:14px;border-inline-start:2px solid var(--ochre-line)}
.key,.marks{list-style:none;margin:8px 0 0;padding:0;font-size:var(--fs-clock);line-height:var(--lh-clock);color:var(--ink-2);display:flex;flex-direction:column;gap:3px}
.key b,.marks b{color:var(--ink);font-weight:600}
.glyph{display:inline-block;min-width:1.4em;color:var(--ink);font-weight:600}
.marks .brk .glyph,.marks .miss .glyph,.marks .dis .glyph{color:var(--counter)}
.marks .dis-note{padding-inline-start:1.4em;color:var(--ink-2)}
.path.dashed{stroke-dasharray:5 4}
.brk{stroke:var(--counter);stroke-width:1.5}
.miss{stroke:var(--counter);stroke-width:1.5;stroke-dasharray:2 3}
.ring{fill:none;stroke:var(--counter);stroke-width:1.5}
svg.ts .val.dense{display:none}
svg.ts .lbl.alt{display:none}
svg.ts .lbl.alt3{display:none}
svg.ts .lbl.alt2{display:block}
.anatomy{list-style:none;margin:8px 0 0;padding:0;display:flex;flex-direction:column;border-top:1px solid var(--rule-2)}
.obj-card{padding:12px 0;border-top:1px solid var(--rule);display:flex;flex-direction:column;gap:3px}
.obj-card:first-child{border-top:0}
.obj-card .v{font-size:var(--fs-st);font-weight:600;color:var(--ink)}
.obj-card .v .unit-l{display:inline;font-weight:500;margin-inline-start:.5em}
.withheld{color:var(--counter);font-weight:600;font-size:var(--fs-body)}
.isnot{color:var(--counter);font-weight:500;font-size:var(--fs-clock)}
.mks{display:flex;flex-wrap:wrap;gap:6px 14px;font-size:var(--fs-clock);color:var(--ink-2)}
.mks .mk{border-inline-start:2px solid var(--counter);padding-inline-start:8px}
.chain{list-style:none;margin:8px 0 0;padding:0;display:flex;flex-direction:column}
.chain .step{border-inline-start:3px solid var(--ink);padding:10px 0 12px 16px;position:relative}
[dir=rtl] .chain .step{padding:10px 16px 12px 0}
.chain .step.open{border-inline-start:3px dotted var(--rule-2);color:var(--ink-2)}
.chain .step.stop{border-top:3px double var(--counter);margin-top:6px;padding-top:10px}
.chain .step.stop .st-state{color:var(--counter);font-weight:600}
.chain .st-head{display:flex;flex-wrap:wrap;gap:4px 12px;align-items:baseline}
.chain h3{font-size:var(--fs-body);font-weight:600;margin:0}
.chain .st-state{font-size:var(--fs-clock);color:var(--ink-2);font-weight:500}
.chain .evs{list-style:none;margin:6px 0 0;padding:0;display:flex;flex-direction:column;gap:5px;font-size:var(--fs-src);line-height:var(--lh-src)}
.chain .evs li{display:flex;flex-wrap:wrap;gap:2px 12px;align-items:baseline}
.chain .evs .clock{flex-direction:row}
.chain .evs .clock .v{font-weight:600;min-width:6.5em}
.chain .source-locator{text-decoration:none;font-weight:600}
/* evidence directory */
.search-inline{display:flex;flex-direction:column;gap:8px;max-width:var(--measure)}
.source-facets{display:flex;flex-wrap:wrap;gap:8px 16px;margin:12px 0;max-width:var(--measure)}.source-facets[hidden]{display:none}.source-facets .facet{display:flex;flex-direction:column;gap:4px;min-width:0;flex:1 1 140px}.source-facets select{min-height:44px;max-width:100%;font:inherit}.source-facets .tbtn{align-self:flex-end}
.search-inline .search-results{max-height:none}
.search-results .search-hit{display:flex;flex-direction:column;gap:4px;padding:12px 0;border-top:1px solid var(--rule);text-decoration:none}
.search-results .search-hit h4{margin:0;font-size:var(--fs-body);font-weight:600}
.search-results .search-hit p{color:var(--ink-2);font-size:var(--fs-src);margin:0}
.search-results .search-hit .meta{font-size:var(--fs-clock);color:var(--mute);font-weight:500}
.search-results .search-see-all{padding-top:12px;border-top:1px solid var(--rule);font-size:var(--fs-src);font-weight:600}
.search-results .search-boundary-note{font-size:var(--fs-src);color:var(--counter);border-top:3px double var(--counter);padding-top:8px}
.hubs{display:flex;flex-direction:column;border-top:1px solid var(--rule-2)}
details.hub{border-top:1px solid var(--rule)}
details.hub:first-child{border-top:0}
details.hub summary{cursor:pointer;list-style:none;padding:12px 0;font-size:var(--fs-body);font-weight:600;color:var(--ink)}
details.hub summary::-webkit-details-marker{display:none}
details.hub summary::before{content:"+ ";color:var(--ochre)}
details.hub[open] summary::before{content:"− "}
.hublist{list-style:none;margin:0 0 14px;padding:0;display:flex;flex-direction:column}
.hublist li{display:flex;flex-direction:column;gap:2px;padding:9px 0 9px 14px;border-inline-start:2px solid var(--ochre-line);margin-bottom:4px;font-size:var(--fs-src);line-height:var(--lh-src)}
[dir=rtl] .hublist li{padding:9px 14px 9px 0}
.hublist .when{font-size:var(--fs-clock);color:var(--ink-2);font-weight:600}
/* comparison */
.controls-grid{display:grid;grid-template-columns:minmax(0,1fr);gap:12px;margin-top:14px}
.slot{display:flex;flex-direction:column;gap:4px;font-size:var(--fs-clock);font-weight:600;color:var(--ink-2)}
.slot select{font:inherit;font-size:var(--fs-src);color:var(--ink);background:var(--paper);border:1px solid var(--rule-2);padding:10px 12px;min-height:44px;max-width:100%}
.never{margin-top:10px}
.compare-verdict{border-top:3px double var(--counter);padding-top:12px;margin-top:22px;color:var(--counter)}.compare-verdict>*{max-width:var(--measure)}
.compare-verdict .eyebrow{display:block;font-size:var(--fs-rubric);font-weight:600;color:var(--counter);margin-bottom:6px}
[dir=ltr] .compare-verdict .eyebrow{text-transform:uppercase;letter-spacing:.1em}
.compare-verdict h3{font-size:var(--fs-q);line-height:var(--lh-q);color:var(--counter)}
.compare-verdict p{font-size:var(--fs-bnd);line-height:var(--lh-bnd);font-weight:500;margin-top:8px}
.compare-verdict .compare-no-merge{font-size:var(--fs-src);font-weight:500;color:var(--ink-2)}
.compare-table{border-collapse:collapse;width:100%;font-size:var(--fs-src);line-height:var(--lh-src);margin-top:16px}
.compare-table caption{text-align:start;padding:6px 0}
.compare-table th,.compare-table td{text-align:start;vertical-align:top;padding:9px 10px 9px 0;border-top:1px solid var(--rule)}
[dir=rtl] .compare-table th,[dir=rtl] .compare-table td{padding:9px 0 9px 10px}
.compare-table thead th{border-top:1px solid var(--ink);font-weight:600}
.compare-table tbody th{font-weight:600;color:var(--ink-2);white-space:nowrap}
.compare-state{display:inline-block;font-weight:600;color:var(--ink);border-inline-start:2px solid var(--counter);padding-inline-start:8px}
tr[data-compare-state=same] .compare-state{border-color:var(--rule-2)}
.compare-boundaries{display:flex;flex-direction:column;gap:10px;margin-top:18px;border-top:3px double var(--counter);padding-top:12px;color:var(--counter)}
.compare-boundaries article strong{display:block;font-size:var(--fs-src);font-weight:600;color:var(--ink)}
.compare-boundaries article p{font-size:var(--fs-src);font-weight:500}
.compare-record-actions{display:flex;flex-wrap:wrap;gap:6px 24px;margin-top:16px;font-weight:600}
.compare-record-actions .button{display:inline-block;padding:3px 0;min-height:24px;text-decoration-color:var(--ochre-line);text-decoration-thickness:2px}
.compare-url-error{border-top:1px solid var(--rule-2);padding-top:12px;margin-top:18px;color:var(--ink-2)}
.compare-url-error h3{font-size:var(--fs-body);color:var(--ink)}
.compare-url-error p{font-size:var(--fs-src)}
@media (max-width:639px){
.compare-table,.compare-table thead,.compare-table tbody,.compare-table tr,.compare-table th,.compare-table td{display:block}
.compare-table thead tr,.compare-table tbody tr{border-top:1px solid var(--rule-2);padding:8px 0;counter-reset:col}
.compare-table th,.compare-table td{border-top:0;padding:3px 0}
.compare-table thead th:first-child{font-weight:600;color:var(--ink-2)}
.compare-table thead th:not(:first-child),.compare-table tbody td{counter-increment:col;padding-inline-start:2.2em;position:relative}
.compare-table thead th:not(:first-child)::before,.compare-table tbody td::before{content:counter(col);position:absolute;inset-inline-start:0;color:var(--mute);font-weight:600;font-variant-numeric:tabular-nums}
.compare-table thead th:last-child,.compare-table tbody td:last-child{counter-increment:none;padding-inline-start:0}
.compare-table thead th:last-child::before,.compare-table tbody td:last-child::before{content:none}
.compare-table tbody th{white-space:normal;color:var(--ink);padding-bottom:4px}
}
/* data & source */
.grp{margin-top:22px}
h3.grp{font-size:var(--fs-body);font-weight:600;border-top:3px solid var(--ink);padding-top:12px}
details.grp summary{cursor:pointer;list-style:none;font-size:var(--fs-body);font-weight:600;border-top:3px solid var(--ink);padding:12px 0 6px}
details.grp summary::-webkit-details-marker{display:none}
details.grp summary::before{content:"+ ";color:var(--ochre)}
details.grp[open] summary::before{content:"− "}
.curated{display:flex;flex-direction:column;gap:6px}
.cat h3{font-size:var(--fs-rubric);color:var(--ochre);font-weight:600;padding-top:14px;margin-top:10px}
[dir=ltr] .cat h3{text-transform:uppercase;letter-spacing:.1em}
.src.card h4{font-size:var(--fs-body);font-weight:600;margin:0}
.src .source-url{font-size:var(--fs-clock);overflow-wrap:anywhere;text-decoration-color:var(--rule-2)}
.src.source-locator{padding:12px 0}
details.deps summary{cursor:pointer;list-style:none;font-size:var(--fs-clock);font-weight:600;color:var(--ink-2)}
details.deps summary::-webkit-details-marker{display:none}
details.deps summary::before{content:"+ ";color:var(--ochre)}
details.deps[open] summary::before{content:"− "}
details.deps .rlist{font-size:var(--fs-clock);margin:6px 0 0}
.source-target{outline:3px double var(--counter);outline-offset:6px}
.inventory{margin:0;display:flex;flex-direction:column;border-top:1px solid var(--rule-2);max-width:var(--measure)}
.inventory div{display:flex;justify-content:space-between;gap:16px;padding:9px 0;border-top:1px solid var(--rule);font-size:var(--fs-src)}
.inventory div:first-child{border-top:0}
.inventory dt{color:var(--ink-2)}.inventory dd{margin:0;font-weight:600;font-variant-numeric:tabular-nums}
ol.objs.chron{list-style:none;margin:10px 0 0;padding:0}
/* measurement */
.prios{display:flex;flex-direction:column;gap:0}
.obj.prio{border-top:1px solid var(--rule-2);padding-top:14px;gap:10px;margin-top:4px}
.obj.prio:first-child{border-top:3px solid var(--ink)}
.obj.prio h3{font-size:var(--fs-q);line-height:var(--lh-q);font-weight:600}
.obj.prio .body p b{color:var(--ink);font-weight:600}
.kv{margin:8px 0 0;display:flex;flex-direction:column;gap:6px;font-size:var(--fs-src)}
.kv dt{font-weight:600;color:var(--ochre);font-size:var(--fs-rubric)}
[dir=ltr] .kv dt{text-transform:uppercase;letter-spacing:.1em}
.kv dd{margin:0 0 6px}
/* reference / trust: report path */
.ctx .mail{font-weight:600}
.correction-origin{font-size:var(--fs-src)}
.correction-origin strong{margin:0 .4em}
/* not found */
.nf{padding-top:14px;border-top:1px solid var(--rule)}
.nf+.nf{margin-top:8px}
/* forced colours for the D2 marks */
@media (forced-colors:active){.bar{fill:CanvasText}.brk,.miss,.ring{stroke:CanvasText}.chain .step,.chain .step.open,.chain .step.stop,.pair,.gap,.compare-verdict,.compare-boundaries,.compare-state,.mks .mk,.hublist li{border-color:CanvasText!important}.withheld,.isnot,.bnd-line,.compare-verdict,.compare-verdict h3,.compare-verdict p{color:CanvasText}}
@media print{.search-inline,.source-facets,.controls-grid,.never,.compare-record-actions,details.deps,[data-source-filter-status]{display:none!important}details.hub::details-content,details.grp::details-content{content-visibility:visible;display:block}svg.ts .val.dense{display:block}}
@media (min-width:600px){
.controls-grid{grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:12px 20px}
.inventory div{max-width:var(--measure)}
.chain .step{padding-inline-start:20px}
[dir=rtl] .chain .step{padding-inline-start:0;padding-inline-end:20px}
svg.ts .val.dense{display:block}
}
@media (min-width:1200px){
.qa.figs{grid-template-columns:220px minmax(0,1fr)}
.obj.prio{display:grid;grid-template-columns:220px minmax(0,1fr);gap:4px 36px}
.obj.prio>.head{grid-column:1 / -1;display:grid;grid-template-columns:220px minmax(0,1fr);gap:4px 36px}
.obj.prio>.head .clock{grid-column:1}.obj.prio>.head h3{grid-column:2}
.obj.prio>:not(.head){grid-column:2}
}

/* D3 — Home head, text frames, phone masthead */
.head .actions{margin-top:14px}
.fig-text .alt-body{margin-top:8px;border-top:0;padding-top:0}.fig-text .alt-body .body{font-size:var(--fs-body);line-height:var(--lh-body)}
@media (max-width:599px){
.head .rubric.product{display:none}
/* the phone head: the governed statement, whole, one step down the scale, and a tighter head rhythm, so the first
   figure group's heading enters the first screen (DEBT-015; the statement is never shortened or split) */
.head .st{font-size:calc(var(--fs-st) - 2px)}
.obj .head{gap:6px}
.head .actions{margin-top:10px}
}

/* D5 — the technical voice: a dashed hairline, body ink, never the boundary's double rule or counter colour, never the
   plaster surface; used by every announced status, technical error and the no-script note (technical ≠ evidence) */
.compare-url-error,.search-results .empty,[data-search-empty],[data-source-no-results],.search-status:not(:empty),[data-correction-error]:not([hidden]),.noscript{border-top:1px dashed var(--rule-2);padding-top:8px;color:var(--ink-2)}
.compare-url-error{border-top-style:dashed}.noscript{background:var(--paper);border-top-style:dashed}
[data-compare-verdict=same-record]{border-top:1px dashed var(--rule-2);color:var(--ink-2)}[data-compare-verdict=same-record] h3,[data-compare-verdict=same-record] .eyebrow{color:var(--ink)}
.search-status:not(:empty){margin-top:6px}
"""


# D6 additions — the visual system: the frame foot, the matrix, the dated lanes, the bars' note, narrow tables,
# development placeholders; the print system for every family and the Reading document; export and social frames.
CSS_D6 = r"""/* ---- D6: visuals, frames, print (same tokens; maintained with CSS and CSS_D2 above) ---- */
.fig .foot .ed{white-space:nowrap}
.fig .foot .b b{font-weight:600}
.rvtab td{white-space:normal}.rvtab td.num{white-space:nowrap}
@container (max-width:420px){.rvtab th,.rvtab td{padding:6px 5px}}
.rvtab caption span[dir=auto]{unicode-bidi:isolate}
.marker.between-tables{margin:8px 0 0;font-size:var(--fs-clock);font-weight:600;color:var(--counter);border-top:3px double var(--counter);padding-top:6px}
/* the provider matrix */
.matrix{list-style:none;margin:8px 0 0;padding:0;display:flex;flex-direction:column;gap:0}
.prow{border-top:3px solid var(--ink);padding:12px 0 14px}
.prow+.prow{border-top-width:1px;border-top-color:var(--rule-2)}
.prow .cls{font-size:var(--fs-q);line-height:var(--lh-q);font-weight:600;margin:0 0 8px}
.prow .cells{display:grid;grid-template-columns:minmax(0,1fr);gap:10px 18px}
.prow .cell{border-top:1px solid var(--rule);padding-top:6px;min-width:0;font-size:var(--fs-clock);line-height:var(--lh-clock);color:var(--ink-2)}
.prow .dim{display:block;font-size:var(--fs-rubric);font-weight:600;color:var(--ochre);margin-bottom:4px}
[dir=ltr] .prow .dim{text-transform:uppercase;letter-spacing:.1em}
.prow .cl{font-weight:600;color:var(--ink);margin:0 0 4px}
.prow .cl2{margin:4px 0 0;color:var(--ink-2)}
.prow .cnt{margin:0}.prow .n{font-size:var(--fs-st);font-weight:600;color:var(--ink);font-variant-numeric:tabular-nums}
.prow ul{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:4px}
.prow .evl li{padding-inline-start:10px;border-inline-start:2px solid var(--rule-2)}
.prow .evl.ctx li{border-inline-start-style:dotted}
.prow .evl b{color:var(--ink);font-weight:600}
.prow .srcl{display:inline-block;padding:3px 0;min-height:24px;text-decoration-color:var(--rule-2)}
.prow .unk{margin:0;color:var(--ink);font-weight:600;border-inline-start:2px dotted var(--rule-2);padding-inline-start:10px}
.prow .lim{margin:10px 0 0;font-size:var(--fs-src);line-height:var(--lh-src);color:var(--counter);font-weight:500;border-top:3px double var(--counter);padding-top:8px}
.prow .lim b{font-weight:600}
.cap.note.issuer{border-top:1px solid var(--rule-2);padding-top:8px;margin-top:14px}
/* the dated lanes */
.lanes-dated{display:flex;flex-direction:column;gap:10px}
.lanes-dated .lane h3{margin:0 0 2px}
.lanes-dated .between{margin:0;padding-top:6px}
.lane-svg{display:block;overflow:visible;font-family:var(--font)}
.lane-svg .span{stroke:var(--ink);stroke-width:6;stroke-linecap:butt}
.lane-svg .stem.open{stroke-dasharray:2 4}
.lanes-dated .ln{margin:2px 0 0;font-size:var(--fs-clock);line-height:var(--lh-clock);color:var(--ink-2)}
.lanes-dated .ln b{color:var(--ink);font-weight:600}
.lanes-dated .lane.outcome h3{color:var(--counter)}
.lanes-dated .lane.outcome .st-state{color:var(--counter)}
.lanes-dated .lanes-ax{margin-top:2px}
.evs.keyed{list-style:none;margin:6px 0 0;padding:0;display:flex;flex-direction:column;gap:5px;font-size:var(--fs-src);line-height:var(--lh-src)}
.evs.keyed li{display:flex;flex-wrap:wrap;gap:2px 10px;align-items:baseline}
.evs.keyed .k{display:inline-block;min-width:1.4em;font-weight:600;color:var(--mute);font-variant-numeric:tabular-nums}
.evs.keyed .clock{flex-direction:row}.evs.keyed .clock .v{font-weight:600;min-width:6.5em}
.evs.keyed .source-locator{text-decoration:none;font-weight:600}
/* the bars' in-frame note */
.p1.noranks .rl{font-weight:500}
@media (forced-colors:active){.lane-svg .span,.lane-svg .stem{stroke:CanvasText}.prow,.prow .cell,.prow .lim,.prow .unk,.prow .evl li{border-color:CanvasText!important}.prow .n,.prow .cl,.prow .lim,.prow .unk,.lanes-dated .lane.outcome h3{color:CanvasText}}
.fig{container-type:inline-size}
.rvtab.wide{min-width:1080px}
.fig .foot .canon-l{display:inline-block;padding:3px 0;min-height:24px}.fig .foot .canon-p{display:none}@media print{.fig .foot .canon-p{display:inline}.fig .foot .canon-s{display:none}}
.prow .evl .dates{display:block;margin-top:2px;color:var(--ink-2)}
.prow .evl a.dl{text-decoration-color:var(--rule-2);display:inline-block;padding:3px 0;min-height:24px}
@container (min-width:480px){
.prow .cells{grid-template-columns:repeat(2,minmax(0,1fr))}
}
/* ---- D6 forms after the red teams: filled marks, the same-year marker, aligned lanes, state labels on the panel, grouped tables ---- */
.mark.dia{transform-box:fill-box;transform-origin:center;transform:rotate(45deg)}
.p1 .between.same{margin:2px 0 8px;padding-top:6px}
.lanes .lane{display:flex;flex-direction:column}.lanes .lane>svg.rv2{margin-top:auto}
.lanes .lane .ph{margin:2px 0 4px}
svg.ts .lbl.st{font-size:11px;font-weight:600;fill:var(--ink-2)}
@container (max-width:480px){svg.ts .lbl.st{display:none}svg.ts .lbl.alt2{display:none}svg.ts .lbl,svg.ts .val{font-size:10.5px}}
@container (min-width:700px){svg.ts .lbl.alt{display:block}}
.obj-card .rubric{text-transform:none;letter-spacing:0}
.obj-card .cl2{margin:0;font-size:var(--fs-clock);line-height:var(--lh-clock);color:var(--ink-2)}
.chain .evs li{display:grid;grid-template-columns:auto minmax(0,1fr);gap:2px 12px;align-items:baseline}
.evs.keyed li{display:grid;grid-template-columns:1.4em auto minmax(0,1fr);gap:2px 10px;align-items:baseline}
.chain .source-locator,.evs.keyed .source-locator,.prow .source-locator{display:inline-block;min-width:24px;min-height:24px;line-height:24px;text-align:center;padding:0}
.prow .counts .srcl{display:block}
@container (max-width:599px){.lanes-dated .lane-svg,.lanes-dated .lanes-ax{display:none}}
.lanes-dated .lane .st-state{display:block;font-size:var(--fs-clock);font-weight:600;color:var(--counter);margin:0 0 4px}
.rvtab th.rg{text-align:start;font-weight:600;color:var(--ink);background:var(--plaster);border-top:2px solid var(--ink)}
.rvtab tbody th[scope=row]{min-width:7em}
.lanes-dated .ln a{display:inline-block;min-height:24px;line-height:24px}
.rvtab tbody+tbody th.rg{border-top:2px solid var(--ink)}
body.export-doc .exp{border-top:3px solid var(--ink);padding-top:12px}
body.export-doc .fig .foot{border-bottom:1px solid var(--ink);padding-bottom:12px}
/* ---- the print-only identity and citation block (shown by the print system only) ---- */
.print-foot{display:none}
/* ---- export and social frames (standalone documents written by the build to out/_export and out/_social) ---- */
body.export-doc{background:var(--paper);margin:0}
body.export-doc main{width:800px;max-width:100%;padding:24px 28px 20px;margin:0;box-sizing:border-box}
body.export-doc .fig{margin:0}
body.export-doc .fig .foot button{display:none}
body.export-doc .fig .alt{display:none}
body.export-doc .exp-id{display:flex;align-items:center;gap:10px;font-size:var(--fs-clock);line-height:var(--lh-clock);color:var(--ink-2);margin:0 0 12px}
body.export-doc .exp-id img{width:32px;height:32px}
body.export-doc .exp-id b{color:var(--ink);font-weight:600}
body.social-doc{background:var(--paper);margin:0;width:1200px;height:630px;overflow:hidden}
body.social-doc main{box-sizing:border-box;width:1200px;height:630px;padding:44px 56px 40px;display:flex;flex-direction:column;border-top:10px solid var(--ink)}
.soc-head{display:flex;align-items:center;gap:18px;font-size:22px;line-height:1.25;font-weight:600;color:var(--ink)}
.soc-head img{width:72px;height:72px;flex:0 0 auto}
.soc-head .soc-pub{display:block;font-size:14px;font-weight:600;color:var(--ochre);letter-spacing:.02em;margin-bottom:2px}
.soc-head .soc-fam{display:block;font-size:15px;font-weight:600;color:var(--ochre);letter-spacing:.1em;text-transform:uppercase;margin-top:2px}
[dir=rtl] .soc-head .soc-fam{letter-spacing:0;text-transform:none}
.soc-body{flex:1 1 auto;display:flex;flex-direction:column;justify-content:center;gap:14px;min-height:0;padding:16px 0}
.soc-q{font-size:24px;line-height:1.35;color:var(--ink-2);margin:0;font-weight:400}
.soc-title{font-size:46px;line-height:1.15;font-weight:600;margin:0;max-width:none;text-wrap:balance;letter-spacing:-.012em}
[dir=rtl] .soc-title{letter-spacing:0;line-height:1.4}
.soc-title.long{font-size:38px}.soc-title.xlong{font-size:31px}
.soc-clock{font-size:22px;line-height:1.4;color:var(--ink);margin:0;font-weight:500}
.soc-desc{font-size:22px;line-height:1.45;color:var(--ink-2);margin:0;font-weight:400}
.soc-desc.long{font-size:19px}
.soc-clock .k{color:var(--mute);font-weight:600;margin-inline-end:.6em}
.soc-bnd{border-top:3px double var(--counter);padding-top:10px;color:var(--counter);font-size:22px;line-height:1.4;font-weight:500;margin:0}
.soc-bnd.long{font-size:20px}
.soc-bnd b{font-weight:600}
.soc-foot{display:flex;justify-content:space-between;gap:24px;align-items:baseline;font-size:17px;line-height:1.4;color:var(--ink-2);border-top:1px solid var(--rule-2);padding-top:14px}
.soc-foot .canon{font-variant-numeric:tabular-nums}
.soc-foot .ed{white-space:nowrap;font-weight:600;color:var(--ink)}
body.social-doc.dense .soc-title{font-size:32px}body.social-doc.dense .soc-title.long{font-size:28px}body.social-doc.dense .soc-title.xlong{font-size:25px}
body.social-doc.dense .soc-q{font-size:18px}body.social-doc.dense .soc-clock{font-size:20px}body.social-doc.dense .soc-desc,body.social-doc.dense .soc-bnd{font-size:20px}
body.social-doc.dense .soc-body{gap:10px;padding:10px 0}
body.social-doc.xdense .soc-title{font-size:26px}body.social-doc.xdense .soc-title.long{font-size:24px}body.social-doc.xdense .soc-title.xlong{font-size:22px}
body.social-doc.xdense .soc-q{font-size:17px}body.social-doc.xdense .soc-clock{font-size:20px;line-height:1.3}body.social-doc.xdense .soc-desc,body.social-doc.xdense .soc-bnd{font-size:20px;line-height:1.3}
body.social-doc.xdense .soc-body{gap:8px;padding:8px 0}
body.export-doc .cite-sep{display:none}
/* ---- the print system (D6): every family; the Reading as a document ---- */
@media print{
@page{margin:16mm 14mm}
html{font-size:10.5pt;line-height:1.45}
body{color:#000}
.bar{border-bottom:1pt solid #000}
.bar-in{padding:0 0 8pt;gap:12pt}
.brand img{width:32pt;height:32pt}
.bar .nav,.controls,dialog,.noscript,.skip,.strip,.spine .index,.inst .groups,.util .actions,.actions,.fig .foot .cite-sep,.chips,.search-inline,.controls-grid,.never,.compare-record-actions,[data-source-filter-status],[data-source-no-results],.open a,.src .acts button,.open,.compare-url-error{display:none!important}
.brand-name{max-width:none;font-size:11pt}
.brand-pub{font-size:8.5pt;color:#000}
.page{display:block;padding:0;max-width:none}
.page>.obj{max-width:none}
.qa,.compact{display:block}
.qa>div:first-child{margin-bottom:4pt}
.obj{border-top:2pt solid #000;padding-top:10pt}
.spine{position:static;max-height:none;overflow:visible;border:0;padding:0;margin-top:16pt}
.foot-spine{display:block!important}
.spine .edges{border-top:1pt solid #000;padding-top:6pt}
.spine .edges ul{display:block}.spine .edges li{display:inline;border:0;padding:0;font-size:9pt}
.spine .edges li::after{content:' · '}
.spine .edges li:last-child::after{content:''}
.spine .edges a{display:inline;padding:0}
/* the page object and its answers are longer than a page: only the objects that fit a page avoid a break inside; a
   figure keeps its head, panels and frame foot together and lets its text alternative break (D6, corrects the D1 rule
   that kept the whole page object together and so began every printout on its second page) */
.obj,.obj.page-obj,.qa{break-inside:auto}
.compact,.src,.obj-card,.prow,.lane,.step,.pair,.head,.fig .fig-t,.fig .cap,.compare-verdict{break-inside:avoid}
.bnd{break-inside:auto}.bnd p,.bnd li{break-inside:avoid}.bnd>h2,.bnd>.rubric,.bnd>h3{break-after:avoid}
.fig{break-inside:auto;background:none;border-top:1pt solid #000;padding:8pt 0 0;margin:12pt 0 4pt}
.fig .rubric,.fig .fig-t,.fig .cap{break-after:avoid}
.fig .panels{break-inside:avoid;break-before:avoid;border-top:1pt solid #000}
.fig .panels:has(.matrix),.fig .panels:has(.chain),.fig .panels:has(.anatomy),.fig .panels:has(.lanes-dated){break-inside:auto}
.fig .foot{break-inside:avoid;break-before:avoid}
.fig .key,.fig .marks,.fig .cap.note{break-before:avoid;break-inside:avoid}
.fig .alt{break-before:auto}
.fig .alt .table-wrap{break-inside:auto;overflow:visible}
.head+section.bnd,.fig .foot .b{break-before:avoid}
.obj p{orphans:3;widows:3}
.qa.figs>div:first-child,.qa .rubric{break-after:avoid}
.qa.figs .fig,.rubric+*{break-before:avoid}
section#search,.search-inline,.source-facets{display:none!important}
.rvtab.wide{min-width:0}
section.bnd+section.bnd{break-before:auto}
.head+*{break-before:avoid}
h1,h2,h3{break-after:avoid}
details::details-content{content-visibility:visible;display:block}
details summary{display:none}
details.more .qa{margin-top:6pt}
.src .acts a[href^='http']::after,.chain .source-locator::after,.evs.keyed .source-locator::after{content:attr(href);display:block;direction:ltr;unicode-bidi:isolate;text-align:start;font-size:.85em;color:#000;font-weight:400;word-break:break-all}
.chain .source-locator,.evs.keyed .source-locator{text-decoration:none}
.inst{background:none;border-top:1pt solid #000;margin-top:16pt}
.inst-in{display:block;padding:8pt 0 0}
.inst .trust,.inst .id{display:none}
.inst .fine{border:0;padding:0;font-size:8.5pt}
a{text-decoration:none;color:inherit}
.rvtab{font-size:8.5pt}
.rvtab thead{display:table-header-group}
.rvtab tr{break-inside:avoid}
.rvtab td{white-space:normal}
svg.ts .val.dense,svg.ts .lbl.alt{display:block}
.mark.a,.bar{fill:#000}.mark.b{stroke:#000;fill:#fff}.path,.axis,.tick,.stem,.grid,.brk,.miss,.ring,.lane-svg .span{stroke:#000}.lbl,.val{fill:#000}
.bnd h2,.bnd .rubric,.bnd-line,.compare-verdict h3,.isnot,.withheld,.st-state,.prow .unk,.gap,.marker,.between{color:#000}
.obj,.qa,.compact,.src,.bnd,.fig,.obj-card,.prow,.prow .cell,.prow .evl li,.prow .unk,.pair,.between,.marker.between-tables,.rvtab th,.rvtab td,.p1 .between,.step,.chain .step{border-color:#000}
.bnd,.between,.fig .foot .b,.prow .lim,.compare-verdict,.lanes-dated .lane.outcome h3{color:#000}
.bnd,.between,.compare-verdict,.prow .lim,.marker.between-tables{border-top:2pt double #000}
.rubric,.spine h3,.prow .dim,.qa .rubric{color:#000}
.print-foot{display:block;margin-top:18pt;border-top:1pt solid #000;padding-top:8pt;font-size:9pt;line-height:1.4;color:#000}
.print-foot p{margin:0 0 3pt}
.print-foot .canon{word-break:break-all}
.print-foot .cite{font-size:8.5pt;color:#000}
.print-foot .cite b{font-weight:600}
/* the Reading as a document: title block, essay at the reading measure, figure with its frame, trace, sources, citation */
.essay section{padding:4pt 0 12pt}
.essay .read{max-width:none}
.essay .st{max-width:none}
.pull{margin:10pt 0;padding-inline-start:12pt;border-inline-start:1.5pt solid #000}
.head .clocks{display:flex;gap:10pt 28pt}
[data-reading-boundary]{break-after:avoid}
#trace,#sources{break-before:auto}
#trace .objs .compact{padding:6pt 0}
}
"""
