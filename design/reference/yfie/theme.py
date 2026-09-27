# -*- coding: utf-8 -*-
"""The reference stylesheet as one string (written to out/assets/yfie.css by the build). Extracted once from the
converged D1 composer (design/exploration/d1_canvas/boards/t4.py, version 5) and maintained here from now on.
Tokens are the :root custom properties at the top; the Lock (design/01_FOUNDATIONS.md §4) governs what they carry."""

FONT_FACES = """@font-face{font-family:'IBM Plex Sans';font-style:normal;font-weight:300;font-display:swap;src:url('/assets/fonts/ibm-plex-sans/IBMPlexSans-Light.woff2') format('woff2')}
@font-face{font-family:'IBM Plex Sans';font-style:normal;font-weight:400;font-display:swap;src:url('/assets/fonts/ibm-plex-sans/IBMPlexSans-Regular.woff2') format('woff2')}
@font-face{font-family:'IBM Plex Sans';font-style:italic;font-weight:400;font-display:swap;src:url('/assets/fonts/ibm-plex-sans/IBMPlexSans-Italic.woff2') format('woff2')}
@font-face{font-family:'IBM Plex Sans';font-style:normal;font-weight:500;font-display:swap;src:url('/assets/fonts/ibm-plex-sans/IBMPlexSans-Medium.woff2') format('woff2')}
@font-face{font-family:'IBM Plex Sans';font-style:normal;font-weight:600;font-display:swap;src:url('/assets/fonts/ibm-plex-sans/IBMPlexSans-SemiBold.woff2') format('woff2')}
@font-face{font-family:'IBM Plex Sans';font-style:normal;font-weight:700;font-display:swap;src:url('/assets/fonts/ibm-plex-sans/IBMPlexSans-Bold.woff2') format('woff2')}
@font-face{font-family:'IBM Plex Sans Arabic';font-style:normal;font-weight:300;font-display:swap;src:url('/assets/fonts/ibm-plex-sans-arabic/IBMPlexSansArabic-Light.woff2') format('woff2')}
@font-face{font-family:'IBM Plex Sans Arabic';font-style:normal;font-weight:400;font-display:swap;src:url('/assets/fonts/ibm-plex-sans-arabic/IBMPlexSansArabic-Regular.woff2') format('woff2')}
@font-face{font-family:'IBM Plex Sans Arabic';font-style:normal;font-weight:500;font-display:swap;src:url('/assets/fonts/ibm-plex-sans-arabic/IBMPlexSansArabic-Medium.woff2') format('woff2')}
@font-face{font-family:'IBM Plex Sans Arabic';font-style:normal;font-weight:600;font-display:swap;src:url('/assets/fonts/ibm-plex-sans-arabic/IBMPlexSansArabic-SemiBold.woff2') format('woff2')}
@font-face{font-family:'IBM Plex Sans Arabic';font-style:normal;font-weight:700;font-display:swap;src:url('/assets/fonts/ibm-plex-sans-arabic/IBMPlexSansArabic-Bold.woff2') format('woff2')}"""

CSS = r"""/* Yemen Financial Inclusion Evidence — reference stylesheet (D1, direction T4 · Instrument). Generated once from the converged composer, then maintained here. No inline style anywhere in the site. */
:root{--paper:#FFFFFF;--plaster:#F5F1E9;--ink:#17212B;--ink-2:#3D4954;--mute:#66717B;--rule:#D8DDE2;--rule-2:#AEB7BF;--ochre:#7A5A1D;--ochre-line:#D6B86A;--counter:#1E5650;
--fs-body:17px;--lh-body:1.6;--fs-display:32px;--lh-display:1.1;--fs-q:20px;--lh-q:1.4;--fs-st:19px;--lh-st:1.5;--fs-bnd:18px;--lh-bnd:1.55;--fs-clock:13.5px;--lh-clock:1.4;--fs-rubric:12px;--fs-src:14.5px;--lh-src:1.5;--fs-nav:15px;--fs-read:18px;--lh-read:1.65;--measure:64ch;--font:'IBM Plex Sans',sans-serif}
html[dir=rtl]{--fs-body:18px;--lh-body:1.9;--fs-display:30px;--lh-display:1.35;--fs-q:21px;--lh-q:1.7;--fs-st:20px;--lh-st:1.7;--fs-bnd:19px;--lh-bnd:1.8;--fs-clock:14.5px;--lh-clock:1.7;--fs-rubric:13px;--fs-src:15.5px;--lh-src:1.75;--fs-nav:16px;--fs-read:19.5px;--lh-read:1.95;--measure:34em;--font:'IBM Plex Sans Arabic',sans-serif}
html{background:var(--paper);color:var(--ink);font-family:var(--font);font-size:var(--fs-body);line-height:var(--lh-body);font-variant-numeric:tabular-nums}
body{margin:0}
a{color:inherit;text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:.16em;text-decoration-color:var(--rule-2)}
h1,h2,h3,h4{margin:0;font-weight:600}
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
.bnd{border-top:3px double var(--counter);padding-top:12px;margin-top:22px;color:var(--counter);max-width:var(--measure)}
.bnd .rubric{color:var(--counter);margin-bottom:8px}
.bnd p{font-size:var(--fs-bnd);line-height:var(--lh-bnd);font-weight:500}
.bnd h2{color:var(--counter)}
/* product bar */
.bar{border-bottom:2px solid var(--ink)}
.bar-in{max-width:1240px;margin:0 auto;padding:10px 16px;display:flex;align-items:center;gap:14px}
.brand{display:flex;align-items:center;gap:10px;text-decoration:none;margin-inline-end:auto}
.brand img{width:40px;height:40px}
.brand-name{font-weight:600;font-size:13px;line-height:1.2;max-width:14ch}
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
.nav.open .group{display:flex;flex-direction:column}
.nav.open .glabel{color:var(--mute);font-size:12px;font-weight:600;padding:10px 0 2px}
[dir=ltr] .nav.open .glabel{text-transform:uppercase;letter-spacing:.08em}
.controls .tbtn,.controls a{min-height:44px}
dialog.search{border:0;padding:0;max-width:min(680px,92vw);width:100%;background:var(--paper);color:var(--ink);border-top:3px solid var(--ink)}
dialog.search::backdrop{background:rgba(23,33,43,.55)}
.search-panel{padding:18px 20px 22px;display:flex;flex-direction:column;gap:12px}
.search-head{display:flex;justify-content:space-between;align-items:baseline;gap:16px}
.search-head strong{font-size:var(--fs-q)}
.search-input{width:100%;padding:12px 14px;border:1px solid var(--rule-2);background:var(--paper);font-size:var(--fs-body)}
.search-input:focus-visible{outline-offset:0}
.search-status{font-size:var(--fs-clock);color:var(--ink-2);min-height:1.4em}
.search-results{display:flex;flex-direction:column;max-height:60vh;overflow:auto}
.search-results a{display:block;padding:10px 0;border-top:1px solid var(--rule);text-decoration:none}
.search-results .empty{color:var(--ink-2)}
.source-target{outline:3px double var(--counter);outline-offset:6px}
@media (prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important;scroll-behavior:auto!important}}
@media (forced-colors:active){.bnd,.between,.obj,.fig,.inst,.spine,.strip a,.compact,.qa{border-color:CanvasText!important}.mark.a{fill:CanvasText}.mark.b{stroke:CanvasText;fill:Canvas}.path,.axis,.tick,.stem,.grid{stroke:CanvasText}.lbl,.val,.unit{fill:CanvasText}.rubric,.clock .k,.clock .v,.lane .base,.between,.bnd,.bnd p,.bnd h2{color:CanvasText}}
@media print{
html{font-size:11pt;line-height:1.45}
.bar .nav,.controls,dialog,.noscript,.skip,.strip,.spine .index,.inst .groups,.util .actions,.fig .foot button{display:none!important}
.page{display:block;padding:0}
.spine{position:static;max-height:none;overflow:visible;border:0;padding:0;margin-top:18pt}
.foot-spine{display:flex!important}
.obj,.qa,.compact,.fig,.src,.bnd{break-inside:avoid}
h1,h2,h3{break-after:avoid}
details.more::details-content{content-visibility:visible;display:block}
details.more summary{display:none}
.src .acts a[href^='http']::after,.fig .foot a.canon::after{content:' (' attr(href) ')';font-size:.85em;color:var(--ink-2)}
.fig{background:none;border-top:1pt solid var(--ink)}
.inst{background:none;border-top:1pt solid var(--ink)}
a{text-decoration:none;color:inherit}
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
.brand img{width:48px;height:48px}.brand-name{font-size:14px}
.nav{display:flex;flex-wrap:wrap;gap:4px 24px;font-size:var(--fs-nav);font-weight:500;align-items:baseline}
.nav a{text-decoration:none;padding:6px 0;border-bottom:2px solid transparent}
.nav a[aria-current=page]{border-bottom-color:var(--ink)}
.nav .group{display:inline-flex;gap:14px;align-items:baseline}
.nav .glabel{color:var(--mute);font-size:12px;font-weight:600}
[dir=ltr] .nav .glabel{text-transform:uppercase;letter-spacing:.08em}
.controls{gap:16px}
.controls .cite,.controls .report{display:inline;color:var(--mute)}
.controls .menu{display:none}
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
.qa .rubric{padding-top:4px}
.compact{display:grid;grid-template-columns:220px minmax(0,1fr);gap:4px 36px;padding:16px 0}
.compact>.clock{grid-column:1;grid-row:1 / span 4}
.compact>:not(.clock){grid-column:2}
.paced .compact.bound{display:flex;flex-direction:column}
}
"""
