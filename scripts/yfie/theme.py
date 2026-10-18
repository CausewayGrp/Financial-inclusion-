# -*- coding: utf-8 -*-
"""The reference stylesheet as one string (written to out/assets/yfie.css by the build). Extracted once from the
converged D1 composer (design/exploration/d1_canvas/boards/t4.py, version 5) and maintained here from now on.
Tokens are the :root custom properties at the top; the Lock (design/01_FOUNDATIONS.md §4) governs what they carry."""

FONT_FACES = """@font-face{font-family:'IBM Plex Sans';font-style:normal;font-weight:400;font-display:swap;src:url('/assets/fonts/ibm-plex-sans/IBMPlexSans-Regular.woff2') format('woff2')}
@font-face{font-family:'IBM Plex Sans';font-style:normal;font-weight:500;font-display:swap;src:url('/assets/fonts/ibm-plex-sans/IBMPlexSans-Medium.woff2') format('woff2')}
@font-face{font-family:'IBM Plex Sans';font-style:normal;font-weight:600;font-display:swap;src:url('/assets/fonts/ibm-plex-sans/IBMPlexSans-SemiBold.woff2') format('woff2')}
@font-face{font-family:'IBM Plex Sans Arabic';font-style:normal;font-weight:400;font-display:swap;src:url('/assets/fonts/ibm-plex-sans-arabic/IBMPlexSansArabic-Regular.woff2') format('woff2')}
@font-face{font-family:'IBM Plex Sans Arabic';font-style:normal;font-weight:500;font-display:swap;src:url('/assets/fonts/ibm-plex-sans-arabic/IBMPlexSansArabic-Medium.woff2') format('woff2')}
@font-face{font-family:'IBM Plex Sans Arabic';font-style:normal;font-weight:600;font-display:swap;src:url('/assets/fonts/ibm-plex-sans-arabic/IBMPlexSansArabic-SemiBold.woff2') format('woff2')}
@font-face{font-family:'Noto Naskh Arabic';font-style:normal;font-weight:600;font-display:swap;src:url('/assets/fonts/noto-naskh-arabic/NotoNaskhArabic-SemiBold-subset.woff2') format('woff2')}
@font-face{font-family:'IBM Plex Serif';font-style:normal;font-weight:600;font-display:swap;src:url('/assets/fonts/ibm-plex-serif/IBMPlexSerif-SemiBold-Latin1.woff2') format('woff2')}"""

CSS = r"""/* Yemen Financial Inclusion Evidence — reference stylesheet (D1, direction T4 · Instrument). Generated once from the converged composer, then maintained here. No inline style anywhere in the site. */
:root{--paper:#F7F5F0;--white:#FFFFFF;--plaster:#FFFFFF;--ink:#17212B;--ink-2:#3D4954;--mute:#646F79;--rule:#D8DDE2;--rule-2:#AEB7BF;--ochre:#7A5A1D;--ochre-line:#B8975A;--counter:#005A44;
--green-700:#005A44;--green-900:#0C3B2E;--sage-600:#5F7357;--sage-400:#8A9A82;--sage-100:#E7ECE4;--brass-700:#7A5A1D;--brass-300:#B8975A;--gold-300:#D6B86A;
--hub-people:#EEF1F7;--hub-access:#FBF3EA;--hub-payments:#FBF5E8;--hub-remittances:#F3F0EA;--hub-providers:#F1EFF5;--hub-finance:#F6F3EC;--hub-firms:#F1F4EE;--hub-reforms:#EEF3F1;
--r-card:16px;--r-inner:12px;--r-btn:10px;--r-pill:999px;--gutter:16px;--sect:22px;--pad-card:20px;
--ico-search:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='black' stroke-width='2' stroke-linecap='round'%3E%3Ccircle cx='11' cy='11' r='7'/%3E%3Cpath d='M20 20l-3.5-3.5'/%3E%3C/svg%3E");
--ico-menu:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='black' stroke-width='2' stroke-linecap='round'%3E%3Cpath d='M4 7h16M4 12h16M4 17h16'/%3E%3C/svg%3E");
--ico-arrow:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='black' stroke-width='2.2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M19 12H5'/%3E%3Cpath d='M11 6l-6 6 6 6'/%3E%3C/svg%3E");
--fs-body:16px;--lh-body:1.6;--fs-display:28px;--lh-display:1.2;--fs-home:36px;--lh-home:1.15;--fs-h2:22px;--lh-h2:1.25;--fs-h2-home:26px;--fs-q:17px;--lh-q:1.4;--fs-st:16.5px;--lh-st:1.6;--fs-bnd:16px;--lh-bnd:1.7;--fs-clock:13px;--lh-clock:1.5;--fs-rubric:12px;--fs-src:14.5px;--lh-src:1.55;--fs-nav:15px;--fs-read:17px;--lh-read:1.7;--measure:64ch;--font:'IBM Plex Sans',sans-serif;--font-display:'IBM Plex Serif','IBM Plex Sans',serif;--font-fig:'IBM Plex Serif','IBM Plex Sans',serif}
html[dir=rtl]{--fs-body:16px;--lh-body:1.75;--fs-display:28px;--lh-display:1.5;--fs-home:38px;--lh-home:1.35;--fs-h2:22px;--lh-h2:1.5;--fs-h2-home:28px;--fs-q:17px;--lh-q:1.6;--fs-st:16.5px;--lh-st:1.8;--fs-bnd:16px;--lh-bnd:1.85;--fs-clock:13px;--lh-clock:1.6;--fs-rubric:12px;--fs-src:15px;--lh-src:1.7;--fs-nav:15.5px;--fs-read:17.5px;--lh-read:1.9;--measure:34em;--font:'IBM Plex Sans Arabic',sans-serif;--font-display:'Noto Naskh Arabic','IBM Plex Sans Arabic',sans-serif;--font-fig:'IBM Plex Sans Arabic',sans-serif}
/* OD-1018 (18 October 2026, the owner's canvas "Yemen FI Evidence Home"): the canvas's type scale, radii, spacing,
   header, footer, buttons, search field, eyebrows, cards and bands replace A · Register's styling, edited in place in the
   blocks below and marked "Canvas". Colour: every canvas colour is its nearest shipped token (CIEDE2000; a band takes
   the nearest token that differs from its ground); the eight hub tints are the only new tokens — Home's topic cards and
   each domain's masthead band, never data, never meaning. Type: one display face per edition for titles and section
   headings (Noto Naskh Arabic 600, IBM Plex Serif 600), loaded only by its own edition; figures in Western tabular
   digits from a face the page already loads (--font-fig). Home carries the canvas scale; every other family the
   interior scale one step below it (--fs-display and --fs-h2 against --fs-home and --fs-h2-home). */
html{background:var(--paper);color:var(--ink);font-family:var(--font);font-size:var(--fs-body);line-height:var(--lh-body);font-variant-numeric:tabular-nums}
body{margin:0}
a{color:inherit;text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:.16em;text-decoration-color:var(--rule-2)}
h1,h2,h3,h4{margin:0;font-weight:600}
b,strong,th{font-weight:600}   /* emphasis is the semibold role; the browser's bold decides nothing (D6) */
/* Canvas: titles and section headings in the edition's display face; eyebrow headings (h2.rubric) stay in the body face */
h1,h2:not(.rubric){font-family:var(--font-display);font-weight:600;color:var(--green-900)}
h1{font-size:var(--fs-display);line-height:var(--lh-display);text-wrap:balance}[dir=ltr] h1{letter-spacing:-.01em}
/* G2: a long governed title (the renderer marks one over 56 characters) steps the display down a fifth, so no H1 runs
   past three lines at 1440 or four at 390; the wording is never shortened */
h1.long{font-size:calc(var(--fs-display) * .8)}
.nw{white-space:nowrap}
h2{font-size:var(--fs-h2);line-height:var(--lh-h2)}
h3{font-size:17px;line-height:1.4}
.mt8{margin-top:8px}.mt10{margin-top:10px}.mt12{margin-top:12px}.mt16{margin-top:16px}.mt18{margin-top:18px}
.first-obj{border-top:0;padding-top:0}
.clocks{display:flex;flex-wrap:wrap;gap:10px 32px;margin-top:6px}
p{margin:0 0 .85em}p:last-child{margin-bottom:0}
.tbtn{background:none;border:0;padding:0;font:inherit;color:inherit;text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:.16em;text-decoration-color:var(--rule-2);cursor:pointer}
.rubric{display:block;font-size:var(--fs-rubric);line-height:1.4;font-weight:600;color:var(--brass-700);margin:0}
[dir=ltr] .rubric{text-transform:uppercase;letter-spacing:.12em}   /* Canvas eyebrow; Arabic keeps no tracking (joins) */
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
/* R-05: the language switch and the menu are links; they keep the box the buttons had (44 px including padding and border) */
.controls a.tbtn{display:inline-flex;align-items:center;box-sizing:border-box}
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
.vlist li{display:flex;flex-wrap:wrap;gap:2px 10px;align-items:baseline}.vlist .when,.vlist .rref{color:var(--mute);font-size:var(--fs-clock);line-height:var(--lh-clock)}
.record-line{display:flex;flex-wrap:wrap;gap:4px 18px;margin:8px 0 2px}.record-line .clock{margin:0}
.mlist li{padding:4px 0}
details.fig-data>summary{cursor:pointer;list-style:none;font-size:var(--fs-clock);line-height:var(--lh-clock);font-weight:600;color:var(--ink-2);padding:8px 0}
details.fig-data>summary::-webkit-details-marker{display:none}details.fig-data>summary::before{content:"+ ";color:var(--ochre)}details.fig-data[open]>summary::before{content:"− "}
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
dialog.search{border:1px solid var(--sage-100);border-radius:var(--r-card);padding:0;max-width:min(680px,92vw);width:100%;background:var(--paper);color:var(--ink)}
dialog.search::backdrop{background:rgba(23,33,43,.55)}
.search-panel{padding:18px 20px 22px;display:flex;flex-direction:column;gap:12px}
.search-head{display:flex;justify-content:space-between;align-items:baseline;gap:16px}
.search-head strong{font-size:var(--fs-q)}
/* Canvas search field: a white pill under a soft shadow; its boundary keeps --sage-600 (3:1 against the paper, where the
   canvas's pale rule would not reach it) */
.search-input{width:100%;box-sizing:border-box;min-height:52px;padding:12px 22px;border:1.5px solid var(--sage-600);border-radius:var(--r-pill);background:var(--white);font-size:var(--fs-body);box-shadow:0 6px 24px color-mix(in srgb,var(--green-900) 6%,transparent)}
.search-input:focus-visible{outline-offset:0}
.search-status{font-size:var(--fs-clock);color:var(--ink-2);min-height:1.4em}
/* Inline figure emphasis (RC-18 4.1, RC-1115): its own class, inline type only — never the .fig figure frame. */
b.fnum{font-weight:700;font-size:1.08em;font-variant-numeric:lining-nums tabular-nums;font-family:var(--font-fig)}   /* Canvas: Western tabular digits from a face the page already loads */
.cite-preview{flex-basis:100%;border-top:1px solid var(--rule);padding-top:8px}.cite-preview .cite-h{margin:0;font-size:var(--fs-clock);font-weight:600;color:var(--ink-2)}.cite-preview .cite-text{margin:4px 0 0;font-size:var(--fs-src);color:var(--ink-2);overflow-wrap:anywhere}.cite-preview .cite-text bdi.url,.cite-preview .cite-text bdi[data-cite-url]{display:inline-block;max-width:100%;vertical-align:top;white-space:normal;overflow-wrap:anywhere}.cite-long{margin-top:6px}.cite-long summary{cursor:pointer;font-size:var(--fs-clock);color:var(--ink-2)}.cite-long .tbtn{margin-top:6px}
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
.bar .nav,.controls,dialog,.noscript,.skip,.strip,.spine .index,.inst .groups,.util .actions,.fig .foot button,.fig .foot .rep,.cite-format,[data-report-nojs],.hero-art,.home-search{display:none!important}   /* OD-1018: Home's illustration and search control are screen-only */
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
:root{--gutter:32px;--sect:40px;--pad-card:28px;--fs-body:17px;--fs-display:38px;--lh-display:1.15;--fs-home:52px;--fs-h2:28px;--lh-h2:1.2;--fs-h2-home:34px;--fs-q:19px;--fs-st:19px;--lh-st:1.65;--fs-bnd:17px;--fs-clock:14px;--lh-clock:1.55;--fs-src:15px;--fs-read:18px}
html[dir=rtl]{--fs-body:17px;--fs-display:38px;--lh-display:1.45;--fs-home:50px;--lh-home:1.3;--fs-h2:28px;--lh-h2:1.45;--fs-h2-home:34px;--fs-q:19px;--fs-st:19px;--lh-st:1.8;--fs-bnd:17px;--fs-clock:14px;--fs-rubric:13px;--fs-src:15.5px;--fs-read:19px}
.brand{flex-shrink:0}
.brand img{width:48px;height:48px}.brand-name{font-size:14px;max-width:none}.brand-pub{font-size:12.5px}
.nav{display:flex;flex-wrap:wrap;gap:4px 28px;font-size:var(--fs-nav);font-weight:500;align-items:baseline}
.nav a{text-decoration:none;padding:6px 0;border-bottom:2px solid transparent;color:var(--ink)}
.nav a[aria-current=page]{border-bottom-color:var(--green-700);color:var(--green-700)}
.nav .group{display:inline-flex;gap:14px;align-items:baseline}
.nav .group{border-inline-start:1px solid var(--rule-2);padding-inline-start:18px}.nav .glabel{color:var(--ink-2);font-size:12px;font-weight:600;padding:6px 0;line-height:calc(var(--fs-nav) * 1.4)}
[dir=ltr] .nav .glabel{text-transform:uppercase;letter-spacing:.08em}
.controls{gap:12px}
.controls .cite,.controls .report{display:inline;color:var(--ink-2)}
.controls .menu{display:none}
.controls a.menu{display:none}
.nav .m-only{display:none}
.page{padding:32px 32px 56px;display:grid;grid-template-columns:minmax(0,1fr) 236px;column-gap:48px;row-gap:0;align-items:start}
.page>.obj{grid-column:1;min-width:0}
.spine:not(.foot-spine){display:flex}
/* G2: the rail is lighter and narrower — no rule beside it, smaller rows, the numerals muted and tabular */
.spine{grid-column:2;grid-row:1 / span 20;position:sticky;top:20px;margin-top:0;padding:4px 0 0;border-top:0;max-height:calc(100vh - 40px);overflow:auto}
.spine h3{font-size:11px;margin-bottom:6px}
.spine li{font-size:13.5px;line-height:1.4;border-top:0}
.spine li a,.spine .index li a{padding:5px 0}
.spine .index .n{min-width:1.9em;color:var(--green-700);font-weight:500}
.spine .index li a{margin-inline-start:0}   /* G3 review: the numerals no longer hang into a padding the lighter rail does not have */
.spine .edges li{border-top:1px solid var(--rule)}
.spine .edges li:first-child{border-top:0}
.spine .index{display:block}
.strip{display:none}
.foot-spine{display:none}
.essay section{padding:8px 0 30px}
h1{max-width:28ch}
.inst-in{display:grid;grid-template-columns:repeat(12,minmax(0,1fr));gap:32px}
}
@media (min-width:1200px){
:root{--fs-home:64px;--lh-home:1.1;--fs-h2-home:38px;--fs-q:20px}
html[dir=rtl]{--fs-home:62px;--lh-home:1.3;--fs-h2-home:38px;--fs-q:20px}
.page{grid-template-columns:minmax(0,1fr) 300px;column-gap:48px}
/* Canvas: a section's eyebrow and heading over 4 of 12 columns, its body over 8 (the canvas questions and caution rows) */
.qa{display:grid;grid-template-columns:minmax(0,4fr) minmax(0,8fr);gap:10px 32px}
.qa>:first-child{grid-column:1}
.qa>:not(:first-child){grid-column:2}
.qa.compare>:not(:first-child){grid-column:1 / -1}
.qa .rubric{padding-top:4px}
.compact{display:grid;grid-template-columns:minmax(0,4fr) minmax(0,8fr);gap:4px 32px;padding:16px 0}
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
.groups a,details.more>summary,details.more .rlist a,details.fold .rlist a,.topics .rlist a,.mlist a{display:inline-block;padding:3px 0;min-height:24px}
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
/* the phone head: the governed statement, whole, at the canvas lead size, and a tighter head rhythm, so the first
   figure group's heading enters the first screen (DEBT-015; the statement is never shortened or split) */
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
/* ---- Canvas screen layer (OD-1018, 18 October 2026): the owner's canvas "Yemen FI Evidence Home" on every family. It
   replaces, in place, the V1 integration's screen layer (9 October 2026) and A · Register's G2 styling (the register
   head, the plate-less figure, the ruled boundary and unit); the information hierarchy, the order rules and the evidence
   unit's composition are unchanged. Screen only, so the D6 print system above is unchanged; no copy, hook or behaviour
   changes. Colour carries no meaning that shape, rule or label does not already carry. ---- */
@media screen{
html{font-synthesis:none}
/* reflow: a long unbroken string in governed prose (a URL, an identifier) wraps instead of widening the page at 320 px */
.obj p,.obj li,.obj dd{overflow-wrap:break-word}
body{background:var(--paper)}
a{text-decoration-color:var(--sage-400)}
a:hover{text-decoration-thickness:2px;text-decoration-color:currentColor}
.body a,.small a,div.open a,.actions a,.rlist a,.crumb a,.src .acts a,.src .source-url,.fig .foot a,.gets a,.hublist a,.chain a,.evs.keyed a,.ctx a,.correction-origin a,details.deps a,.compare-record-actions a,.search-see-all a{color:var(--green-700)}
.q a{color:var(--green-900);text-decoration-color:var(--brass-300)}.q a:hover{color:var(--green-700)}
button:disabled,.tbtn:disabled{color:var(--ink-2);cursor:not-allowed;text-decoration:none}
:focus-visible{outline-color:var(--green-700)}
/* Canvas header: one paper row (64 px on a phone, 84 px wide) on a hairline; icon marks are masks in the text colour */
.bar{background:var(--paper);border-bottom:1px solid var(--sage-100)}
.bar-in{max-width:1376px;padding:10px var(--gutter);min-height:64px;box-sizing:border-box;gap:12px}
.brand{gap:10px}
.brand-pub{color:var(--brass-700)}
.brand-name{color:var(--green-900)}
.controls{gap:8px;font-weight:600}
.controls .tbtn,.controls a{color:var(--ink)}
.controls .lang{border:0;padding:0 6px;color:var(--mute)}
.controls .menu{padding:0 12px;gap:8px;border:1px solid var(--sage-100);border-radius:var(--r-btn);background:var(--white);color:var(--green-900)}
.controls [data-search-open]::before,.controls .menu::before{content:"";flex:0 0 auto;width:20px;height:20px;background:currentColor;-webkit-mask:var(--ico) center/contain no-repeat;mask:var(--ico) center/contain no-repeat}
.controls [data-search-open]{display:inline-flex;align-items:center;gap:8px;padding:0 8px;border-radius:var(--r-btn);--ico:var(--ico-search)}
.controls .menu{--ico:var(--ico-menu)}
@media (max-width:399px){.controls [data-search-open]::before,.controls .menu::before{display:none}.controls .menu{padding:0 8px}.controls [data-search-open]{padding:0 4px}}   /* 320 px: the labels, not the marks */
/* Canvas page: a 1376 px container, 16 px gutters on a phone; sections parted by space, not rules */
.page{max-width:1376px;padding:20px var(--gutter) 40px;box-sizing:border-box}
.obj.page-obj{gap:var(--sect);border-top:0;padding-top:0}
.obj .head{gap:10px}
.qa{row-gap:10px;padding-top:0;border-top:0}
.qa .rubric{color:var(--brass-700)}
.rubric .n{color:var(--green-700);font-variant-numeric:tabular-nums}
/* lists stay lists: rule-separated rows, never a card grid */
.compact{padding:16px 0}
.compact .q{font-size:var(--fs-q);line-height:var(--lh-q);font-weight:600}
.compact .open{font-weight:600}
.objs{border-top-color:var(--rule)}
/* the record line reads as a figure card's foot: the clocks side by side under a hairline, brass labels */
.record-line{gap:8px 28px;margin:6px 0 2px;padding-top:12px;border-top:1px solid var(--sage-100)}
.record-line .clock .k{color:var(--brass-700);font-size:var(--fs-rubric)}
/* Canvas figure cards (OD-1018 D4, Home): a paced group and the record bound to it, one white card each, three across on
   a wide screen; the group's figures emphasised in place, the record as the card's foot */
.paced .sent{margin:0}
.paced .sent.lead{margin-bottom:18px;color:var(--ink-2)}
.paced .sent.res{font-weight:400;border-top:0;padding-top:0;margin-top:18px;color:var(--ink-2)}
.fcards{display:grid;grid-template-columns:minmax(0,1fr);gap:14px}
.fcard{display:flex;flex-direction:column;gap:12px;background:var(--white);border:1px solid var(--sage-100);border-radius:var(--r-card);padding:var(--pad-card)}
.fcard .sent{font-size:var(--fs-src);line-height:1.75;color:var(--ink);max-width:none}
.paced .compact.bound,[dir=rtl] .paced .compact.bound{margin:auto 0 0;padding:12px 0 0;border:0;border-top:1px solid var(--sage-100);gap:4px}
.paced .compact.bound .clock .k{color:var(--brass-700);font-size:var(--fs-rubric)}
.paced .compact.bound .clock .v{font-size:var(--fs-clock);font-weight:500}
.paced .compact.bound .q{font-size:var(--fs-src);font-weight:600;color:var(--green-900)}
.paced .compact.bound .small{font-size:var(--fs-clock);line-height:var(--lh-clock)}
/* Canvas link with an arrow (the evidence link, the next action), the arrow in the reading direction */
.actions a,.compact .open>a:first-child{display:inline-flex;align-items:center;gap:8px;color:var(--green-700);text-decoration-color:var(--brass-300);text-decoration-thickness:1px}
.actions a::after,.compact .open>a:first-child::after{content:"";flex:0 0 auto;width:16px;height:16px;background:currentColor;-webkit-mask:var(--ico-arrow) center/contain no-repeat;mask:var(--ico-arrow) center/contain no-repeat}
[dir=ltr] .actions a::after,[dir=ltr] .compact .open>a:first-child::after{transform:scaleX(-1)}
/* Canvas question cards: one white card per question, two across on a wide screen; the ordinal as the card's eyebrow */
.qlist{display:grid;grid-template-columns:minmax(0,1fr);gap:10px}
.qlist li{position:relative;display:flex;flex-direction:column;gap:6px;padding:16px;background:var(--white);border:1px solid var(--sage-100);border-radius:var(--r-inner)}
.qlist li::before{font-size:var(--fs-rubric);line-height:1.2;padding-top:0;color:var(--brass-700);font-variant-numeric:tabular-nums}
.qlist .q{font-size:var(--fs-q);line-height:var(--lh-q);font-weight:600}
.qlist .q a{color:var(--green-900);text-decoration:none}
.qlist .q a::after{content:"";position:absolute;inset:0;border-radius:var(--r-inner)}
.qlist li:hover{border-color:var(--brass-300)}.qlist .q a:hover{text-decoration:underline;text-decoration-color:var(--brass-300)}
.qlist .gets{margin-top:2px}
/* Canvas evidence card (OD-1018 D5): every figure is the canvas figure card, its foot (period, boundary, source,
   verification link) under a hairline; the frame's contract and contents are unchanged */
.fig{background:var(--white);border:1px solid var(--sage-100);border-radius:var(--r-card);padding:18px 14px 14px;margin:16px 0 4px}
.fig .fig-t{color:var(--green-900)}
.fig .foot{margin-top:14px;padding-top:12px;border-top:1px solid var(--sage-100)}
.fig .foot .b{color:var(--ink)}
/* Canvas caution band: every "what this does not establish" block — the --sage-100 fill (the nearest token that differs
   from the paper ground), a --gold-300 rule, the warning mark drawn in the band's own ::before; the boundary in the ink */
.bnd{background:var(--sage-100);border:1px solid var(--gold-300);border-radius:var(--r-card);padding:var(--pad-card);margin-top:0;color:var(--ink)}
.bnd::before{content:"";display:block;width:40px;height:40px;box-sizing:border-box;border:1px solid var(--gold-300);border-radius:50%;margin-bottom:12px;background:linear-gradient(var(--brass-700),var(--brass-700)) 50% 38%/2px 10px no-repeat,radial-gradient(circle at 50% 70%,var(--brass-700) 0 1.6px,transparent 2.2px),var(--white)}
.bnd p{font-weight:400;color:var(--ink)}
.bnd h2{color:var(--green-900)}
.bnd h3{margin-top:14px}
/* Canvas footer: the deep-green field; the brand block first on the screen (it holds no control, so the visual order
   changes no focus order), the link groups in columns, the edition and the legal lines across */
.inst{background:var(--green-900);color:var(--sage-100);border-top:0;margin-top:48px}
.inst-in{max-width:1376px;padding:36px var(--gutter) 28px;box-sizing:border-box;gap:24px}
.inst .trust h3,.inst .groups strong{font-weight:600;color:var(--gold-300)}
[dir=ltr] .inst .trust h3,[dir=ltr] .inst .groups strong{letter-spacing:.12em}
.inst .trust nav{gap:4px 20px;font-size:var(--fs-src)}
.inst .groups{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px}
.inst .groups div{gap:4px}
.inst .id{order:-1;flex-direction:column;align-items:flex-start;gap:14px;line-height:1.8;color:var(--sage-100)}
.inst .id img{background:var(--white);padding:8px 12px;border-radius:var(--r-btn)}
.inst .id p{margin:0;max-width:44ch}
.inst .fine{border-top-color:var(--sage-600);color:var(--sage-100)}
.inst .fine+.fine{border-top:0;padding-top:0}
/* header states */
.nav a:hover,.controls .tbtn:hover,.controls a:hover{color:var(--green-700)}
.controls [data-search-open]:hover,.controls .lang:hover{background:var(--sage-100)}
.controls .menu:hover{border-color:var(--green-700)}
.nav.open{border-bottom:1px solid var(--sage-100)}
.nav.open .glabel{color:var(--brass-700)}
/* page head: eyebrow, title, the brass rule, the statement in the secondary ink, the calls to action, the quiet tools */
.head .rubric{color:var(--brass-700)}
.head .st{font-weight:400;color:var(--ink-2)}
.head .st b{color:var(--ink)}
/* Canvas calls to action: one filled, one outlined at 1.5 px, 10 px corners, 48 px tall, the arrow in the reading direction */
.head .actions,.head-rule .actions{margin-top:6px;gap:10px 12px}
.head .actions a,.head-rule .actions a{min-height:48px;box-sizing:border-box;padding:0 22px;border:1.5px solid var(--green-700);border-radius:var(--r-btn);color:var(--green-700);background:transparent;text-decoration:none;font-size:var(--fs-src);font-weight:600;gap:10px}
.head .actions a:first-child,.head-rule .actions a:first-child{background:var(--green-700);color:var(--white)}
.head .actions a:hover,.head-rule .actions a:hover{background:var(--green-900);border-color:var(--green-900);color:var(--white)}
/* the brass rule under every page title (DL-V2-011's anchor, now the canvas's): 48 x 3 px; Home's 72 x 3 px */
.head h1::after{content:"";display:block;width:48px;height:3px;background:var(--brass-300);margin-top:14px}
@media (max-width:599px){.head h1::after{margin-top:10px}}
/* the page's own tools at its foot: outlined buttons, no arrow */
.util .actions{gap:8px 10px}
.util .actions>.tbtn,.util .actions>a{display:inline-flex;align-items:center;min-height:40px;box-sizing:border-box;padding:0 14px;border:1.5px solid var(--green-700);border-radius:var(--r-btn);background:var(--white);color:var(--green-700);text-decoration:none;font-size:var(--fs-src);font-weight:600}
.util .actions>a::after{content:none}
.util .actions>.tbtn:hover,.util .actions>a:hover{background:var(--sage-100)}
/* chart marks: primary marks in the deep green; axes, labels and the not-comparable marks unchanged */
svg .bar,.mark.a{fill:var(--green-900)}.lane-svg .span,.mark.b,.path{stroke:var(--green-900)}
/* breadcrumbs: green and underlined, so a link never differs from its text by colour alone (1.4.1) */
.crumb a{text-decoration:underline;text-decoration-color:var(--sage-400)}
.obj,.spine,.prow{border-top-color:var(--green-900)}
/* group headings inside long lists: an eyebrow over the rows (Questions), a hairline over the group (/data/, Measurement) */
.cluster h3{border-top:0;padding-top:0;margin-top:22px;margin-bottom:10px;color:var(--brass-700)}
h3.grp,details.grp summary,.obj.prio:first-child{border-top:1px solid var(--rule-2)}
h3.grp,details.grp>summary{color:var(--green-900)}
.spine h3,.cat h3,.kv dt,.prow .dim{color:var(--brass-700)}
.strip a .n,.spine .index .n{color:var(--green-700)}
/* key figures: the value in the primary green, from the figure face, never boxed (RC-1115) */
.paced .sent b.fnum,.qa.first .st b.fnum{color:var(--green-700);font-size:1.15em}
.paced .fcard .sent b.fnum{font-size:1.4em;line-height:1.1}
.compact .clock .k{font-weight:500}
.obj-card .v,.prow .n{color:var(--green-700)}
/* Canvas caution band, the Compare variant; the verdict is a white card */
.compare-boundaries{background:var(--sage-100);border:1px solid var(--gold-300);border-radius:var(--r-card);padding:var(--pad-card);color:var(--ink)}
.compare-verdict{background:var(--white);border:1px solid var(--sage-100);border-radius:var(--r-card);padding:var(--pad-card);color:var(--ink)}
.compare-verdict h3{color:var(--green-900)}.compare-verdict p{font-weight:400}
.bnd .rubric,.compare-verdict .eyebrow{color:var(--brass-700)}
.bnd .rubric .n,.bnd .ref,.bnd .clock .k,.bnd .count,.compare-boundaries .count{color:var(--ink-2)}
[data-compare-verdict=same-record]{background:var(--white);border:1px dashed var(--rule-2)}
.prow .lim{border-top-color:var(--brass-700)}
/* figures: the evidence card; a small multiple is a column of cards */
.multiple{gap:16px}.multiple .fig,.multiple .fig:first-child{margin-top:0;border-top-width:1px}
/* tables: ruled, not filled */
.rvtab{background:var(--white)}
.rvtab thead th,.compare-table thead th{background:none;border-top:2px solid var(--green-900);border-bottom:1px solid var(--rule-2);color:var(--ink)}
.rvtab th.rg{background:none;border-top-color:var(--green-900)}
.inventory dd{color:var(--green-900)}
/* tools: the search field and the filter bar in the canvas form */
.search-input:focus-visible{outline-offset:2px}
.source-facets:not([hidden]){background:var(--sage-100);padding:16px 18px 18px;max-width:none;border-radius:var(--r-inner)}
.source-facets .facet>span{font-size:var(--fs-clock);font-weight:600;color:var(--ink)}
.source-facets select,.slot select,.search-type{background:var(--white);border:1.5px solid var(--sage-600);border-radius:var(--r-btn);padding:8px 12px;color:var(--ink)}
.chip{background:var(--white);border-color:var(--sage-400);border-radius:var(--r-pill);padding:3px 12px;color:var(--green-900)}
.chip:hover{background:var(--sage-100);border-color:var(--green-700)}
details.more summary::before,details.hub summary::before,details.grp summary::before,details.deps summary::before{color:var(--green-700);font-weight:600}
/* 2.5.8: the dependency disclosures of /data/ measured 22 px with close neighbours; the D2 minimum, applied where it was missed */
details.deps>summary{padding:3px 0;min-height:24px;box-sizing:border-box}
details.more summary:hover,details.hub summary:hover,details.grp summary:hover,details.deps summary:hover{color:var(--green-700)}
.hublist li,.gap,.pull{border-inline-start-color:var(--brass-300)}
.mks .mk,.compare-state{border-inline-start-color:var(--green-700)}
.search-results a:hover h4,.search-results a:hover{color:var(--green-700)}
.cite-preview{border-top-color:var(--rule)}
/* the footer's links and focus on the deep-green field; the canonical logo on a white tile, never on the dark field */
.inst a{color:var(--paper);text-decoration-color:var(--sage-400)}
.inst a:hover{color:var(--gold-300);text-decoration-color:var(--gold-300)}
.inst :focus-visible{outline-color:var(--gold-300)}
/* the social and export frames share the deep-green structure rule; a card's title takes the edition's display face */
body.social-doc main{border-top-color:var(--green-900)}
body.export-doc .exp{border-top-color:var(--green-900)}
.soc-title{font-family:var(--font-display);color:var(--green-900)}

/* ---- Canvas Home (OD-1018 D4): the hero, the search band, the topic cards, the figure cards, the bands ---- */
.obj.page-obj:has(> #topics) h1{font-size:var(--fs-home);line-height:var(--lh-home)}
.obj.page-obj:has(> #topics) .head h1::after{width:72px}
.obj.page-obj:has(> #topics) .qa:not(.fold-sec) h2:not(.rubric){font-size:var(--fs-h2-home)}
.hero-art{display:none}
.hero-art svg{display:block;width:100%;height:auto;max-width:640px;margin-inline:auto}
.hero-art .ha-dot{fill:var(--rule-2)}.hero-art .ha-dotg{fill:var(--brass-300)}.hero-art .ha-ground{fill:var(--sage-100)}
.hero-art .ha-p4,.hero-art .ha-p2{fill:var(--white);stroke:var(--sage-100);stroke-width:1.5}.hero-art .ha-p3{fill:var(--paper);stroke:var(--sage-100);stroke-width:1.5}
.hero-art .ha-p1{fill:var(--white);stroke:var(--brass-300);stroke-width:2}
.hero-art .ha-fill{fill:url(#ha-dots)}.hero-art .ha-fillg{fill:url(#ha-dotsg);opacity:.9}
.hero-art .ha-l1{stroke:var(--brass-300);stroke-width:1.5}.hero-art .ha-l2{stroke:var(--brass-700);stroke-width:1.5;stroke-dasharray:2 4}
.hero-art .ha-ng{fill:var(--brass-300)}.hero-art .ha-np{fill:var(--green-700)}
/* the search band: a field-shaped control that opens the existing search; the go mark drawn in its own end cap */
.home-search{display:flex;justify-content:center}
.hsearch{display:flex;align-items:center;gap:12px;width:100%;max-width:760px;min-height:56px;box-sizing:border-box;padding-block:6px;padding-inline:18px 6px;border:1.5px solid var(--sage-600);border-radius:var(--r-pill);
background:radial-gradient(circle at calc(100% - 28px) 50%,var(--green-700) 0 21.5px,transparent 22px),var(--white);box-shadow:0 6px 24px color-mix(in srgb,var(--green-900) 6%,transparent);color:var(--mute);font:inherit;font-size:var(--fs-body);text-align:start;cursor:pointer}
[dir=rtl] .hsearch{background:radial-gradient(circle at 28px 50%,var(--green-700) 0 21.5px,transparent 22px),var(--white)}
.hsearch>span{flex:1 1 auto;min-width:0}
.hsearch::before{content:"";flex:0 0 auto;width:22px;height:22px;background:var(--mute);-webkit-mask:var(--ico-search) center/contain no-repeat;mask:var(--ico-search) center/contain no-repeat}
.hsearch::after{content:"";flex:0 0 auto;width:44px;height:44px;background:var(--white);-webkit-mask:var(--ico-arrow) center/20px no-repeat;mask:var(--ico-arrow) center/20px no-repeat}
[dir=ltr] .hsearch::after{transform:scaleX(-1)}
.hsearch:hover{border-color:var(--green-700)}
/* the phone's first screen: the band one step tighter, so the first figure card's value stays inside it */
@media (max-width:599px){.hsearch{min-height:50px;padding-block:3px;font-size:var(--fs-src);line-height:1.4}.paced .sent.lead{margin-bottom:12px}.fcard{padding-top:16px}}
/* the topic cards: the governed name, the governed short thesis, one stroke icon; the hub tint decorates, never means */
.qa.topics{display:flex;flex-direction:column;gap:16px;background:var(--white);border:1px solid var(--sage-100);border-radius:var(--r-card);padding:var(--pad-card)}
.topics ul.rlist{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px;list-style:none;padding:0;margin:0}
.topics ul.rlist li{position:relative;display:flex;flex-direction:column;gap:8px;min-height:150px;box-sizing:border-box;padding:16px 14px;border:1px solid var(--sage-100);border-radius:var(--r-inner)}
.topics ul.rlist li:hover{border-color:var(--brass-300)}
.topics ul.rlist a{font-size:var(--fs-q);line-height:1.35;font-weight:600;color:var(--green-900);text-decoration:none;padding:0;min-height:0}
.topics ul.rlist a::after{content:"";position:absolute;inset:0;border-radius:var(--r-inner)}
.topics ul.rlist a:hover{text-decoration:underline;text-decoration-color:var(--brass-300)}
.topics .tthesis{margin:0;font-size:var(--fs-clock);line-height:1.6;color:var(--ink-2)}
.ticon{width:26px;height:26px;flex:0 0 auto;fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
[data-hub=people]{--hub:var(--hub-people)}[data-hub=access]{--hub:var(--hub-access)}[data-hub=payments]{--hub:var(--hub-payments)}[data-hub=remittances]{--hub:var(--hub-remittances)}
[data-hub=providers]{--hub:var(--hub-providers)}[data-hub=finance]{--hub:var(--hub-finance)}[data-hub=firms]{--hub:var(--hub-firms)}[data-hub=reforms]{--hub:var(--hub-reforms)}
.topics ul.rlist li[data-hub]{background:var(--hub)}
[data-hub=people] .ticon,[data-hub=providers] .ticon,[data-hub=reforms] .ticon{color:var(--ink-2)}
[data-hub=access] .ticon,[data-hub=payments] .ticon,[data-hub=finance] .ticon{color:var(--brass-700)}
[data-hub=remittances] .ticon,[data-hub=firms] .ticon{color:var(--green-700)}
/* Home's folded sections 07 and 08 as the canvas's gaps card and verify band */
#topics~#s7{background:var(--white);border:1px solid var(--sage-100);border-radius:var(--r-card);padding:4px var(--pad-card) 8px}
#topics~#s7 details.fold,#topics~#s8 details.fold{border-top:0;margin-top:0}
#topics~#s7 details.fold>summary,#topics~#s8 details.fold>summary{border-bottom:0}

/* ---- Canvas verify band (OD-1018 D5): every source and verification block ---- */
#topics~#s8,.qa#verify,.qa#q6,[data-reading-verify],.qa#sources{background:var(--sage-100);border-radius:var(--r-card);padding:var(--pad-card)}
#topics~#s8{padding-block:4px 8px}
:is(#topics~#s8,#verify,#q6,#trace,#sources) .rubric{color:var(--green-700)}
:is(#topics~#s8,#verify,#q6,#trace,#sources) :is(.clock .k,.rref,.rights,.when,.count,.ref,.meta){color:var(--ink-2)}   /* --mute on --sage-100 is 4.28 : 1; --ink-2 is 7.68 : 1 */
:is(#verify,#q6,#trace,#sources) .src,:is(#verify,#q6,#trace,#sources) .compact{border-top-color:var(--rule-2)}

/* ---- Canvas reading panel (OD-1018 D5): a featured Reading (Home, the Readings index) and every Reading's head ---- */
:is(#sf,#featured,#deeper) .compact.first-obj,.obj.page-obj:has(> .essay)>.head{background:var(--green-900);color:var(--paper);border:0;border-radius:var(--r-card);padding:var(--pad-card)}
:is(#sf,#featured,#deeper) .compact.first-obj{display:flex;flex-direction:column;gap:12px}
:is(#sf,#featured,#deeper) .compact .clock .k,.obj.page-obj:has(> .essay)>.head :is(.rubric,.clock .k){color:var(--gold-300)}
:is(#sf,#featured,#deeper) .compact .clock .v,.obj.page-obj:has(> .essay)>.head .clock .v{color:var(--paper)}
:is(#sf,#featured,#deeper) .compact .q{font-family:var(--font-display);font-size:var(--fs-h2);line-height:var(--lh-h2)}
:is(#sf,#featured,#deeper) .compact .q a,.obj.page-obj:has(> .essay)>.head a{color:var(--paper);text-decoration-color:var(--gold-300)}
:is(#sf,#featured,#deeper) .compact :is(.st,.small),.obj.page-obj:has(> .essay)>.head :is(.q,.crumb,.page-tools>.tbtn,.page-tools>a){color:var(--sage-100)}
:is(#sf,#featured,#deeper) .compact .st p{color:var(--sage-100)}
:is(#sf,#featured,#deeper) .compact .open a{color:var(--gold-300);text-decoration-color:var(--gold-300)}
.obj.page-obj:has(> .essay)>.head h1{color:var(--paper)}
.obj.page-obj:has(> .essay)>.head h1::after{background:var(--gold-300)}
.obj.page-obj:has(> .essay)>.head .st{color:var(--paper)}
.obj.page-obj:has(> .essay)>.head :focus-visible,:is(#sf,#featured,#deeper) .compact.first-obj :focus-visible{outline-color:var(--gold-300)}
/* the Readings index: the list stays a ruled list, on one white card */
#all>ol.objs{background:var(--white);border:1px solid var(--sage-100);border-radius:var(--r-card);padding:4px var(--pad-card);margin:0}

/* ---- Canvas domain masthead (OD-1018 D3): the head on its hub's tint ---- */
.obj.page-obj[data-hub]>.head{background:var(--hub);border-radius:var(--r-card);padding:var(--pad-card)}
}
@media screen and (min-width:900px){
.nav a{white-space:nowrap}
.nav .group:not(.m-only){display:inline-grid;grid-template-columns:auto auto;column-gap:16px;align-items:baseline}
.nav .group:not(.m-only) .glabel{grid-column:1 / -1;padding:0;font-size:11px;line-height:1.2;color:var(--brass-700)}
.controls .cite,.controls .report{font-size:13.5px}
.controls .report{display:inline-flex;align-items:center;min-height:44px}
.nav{align-items:last baseline}
.spine{border-inline-start-color:var(--rule)}
.spine .index a{border-inline-start:2px solid transparent;margin-inline-start:-21px;padding-inline-start:19px}
.spine .index a:hover{color:var(--green-700)}
.spine .index a[aria-current]{border-inline-start-color:var(--green-700);color:var(--green-700)}
.topics ul.rlist li{padding:20px 18px}
.ticon{width:30px;height:30px}
.bar-in{min-height:84px;padding:12px 32px;gap:28px}
.page{padding-top:32px;padding-bottom:56px}
.qlist{grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}
.qlist li{padding:22px 22px 18px}
.fig{padding:24px 24px 18px}
/* Canvas footer on a wide screen: brand 4 columns, the policies 2, the site's link groups 6; the edition and the legal
   lines across the width (the base block above makes it a 12-column grid) */
.inst-in{padding:48px 32px 32px}
.inst .id{grid-column:1 / span 4;grid-row:1}
.inst .trust{grid-column:5 / span 2;grid-row:1}
.inst .trust nav{flex-direction:column;flex-wrap:nowrap}
.inst .groups{grid-column:7 / -1;grid-row:1;grid-template-columns:repeat(3,minmax(0,1fr));gap:32px}
.inst .colophon,.inst .fine{grid-column:1 / -1}
}
@media screen and (min-width:1200px){
/* Home on a wide screen: the hero (statement column and illustration), the search band, the topic cards four across,
   the three figure cards, the gaps card beside the verify band */
.obj.page-obj:has(> #topics){display:grid;grid-template-columns:repeat(12,minmax(0,1fr));column-gap:32px;row-gap:var(--sect);align-items:start}
.obj.page-obj:has(> #topics)>*{grid-column:1 / -1;min-width:0}
.obj.page-obj:has(> #topics)>.head{grid-column:1 / span 8;align-self:center}
.obj.page-obj:has(> #topics)>.head h1{max-width:none}
.obj.page-obj:has(> #topics)>.hero-art{display:block;grid-column:9 / -1;align-self:center}
[dir=ltr] .hero-art svg{transform:scaleX(-1)}
.obj.page-obj:has(> #topics)>#s3{display:flex;flex-direction:column;gap:14px}
/* the governed groups differ in length, so the long first card runs beside the other two (markup order kept) */
.fcards{grid-template-columns:repeat(2,minmax(0,1fr));gap:20px;align-items:start}
.fcards>.fcard:first-child{grid-row:span 2}
.topics ul.rlist{grid-template-columns:repeat(4,minmax(0,1fr));gap:16px}
.topics ul.rlist li{min-height:196px}
.obj.page-obj:has(> #topics)>#s7{grid-column:1 / span 7}
.obj.page-obj:has(> #topics)>#s8{grid-column:8 / -1}
/* the caution band's eyebrow and heading over a third of its width, its text beside them (the canvas row) */
.bnd{display:flow-root;padding:28px 32px}
.bnd>.rubric,.bnd>h2{float:inline-start;clear:inline-start;width:calc(33.333% - 24px)}
.bnd::before{float:inline-start;clear:inline-start;width:48px;height:48px}
.bnd>:not(.rubric):not(h2){margin-inline-start:33.333%}
.bnd>.mt8{margin-top:0}
}
@media screen and (min-width:1280px){
.bar-in{flex-wrap:nowrap}
.brand-name{max-width:15ch}
.nav{flex-wrap:nowrap;gap:4px 28px;align-items:center}
}
/* ---- V1 phase 2 (DL-V1-009…012): one disclosure pattern, orientation on a phone, density by width. Screen only;
   every governed region keeps its place, and nothing is hidden that a disclosure does not name. ---- */
@media screen{
/* one disclosure pattern: a named bar with a + / − control; the governed summary is the whole hit area */
/* G2 pass two (DL-V2-001, rules not fills): the named bar is a ruled row, not a white box; the control keeps its box */
details.fold{border-top:1px solid var(--rule);margin-top:4px}
details.fold>summary{display:flex;align-items:center;gap:12px;min-height:48px;box-sizing:border-box;padding:10px 0;cursor:pointer;list-style:none;background:none;border:0;border-bottom:1px solid var(--rule);font-weight:600;font-size:var(--fs-body);line-height:1.35;color:var(--ink)}
details.fold>summary::-webkit-details-marker,details.more>summary::-webkit-details-marker,details.hub>summary::-webkit-details-marker,details.grp>summary::-webkit-details-marker{display:none}
details.fold>summary .count{color:var(--ink-2);font-weight:500}
details.fold>summary:hover{color:var(--green-900)}
details.fold[open]>summary{border-bottom-color:var(--rule-2)}
details.fold>summary::before,details.more>summary::before,details.hub>summary::before,details.grp>summary::before{content:"+";content:"+" / "";flex:0 0 auto;display:inline-flex;align-items:center;justify-content:center;width:22px;height:22px;box-sizing:border-box;border:1.5px solid var(--green-700);border-radius:6px;color:var(--green-700);font-weight:600;font-size:16px;line-height:1;margin-inline-end:10px;vertical-align:-4px;background:var(--white)}
details.fold>summary::before{margin-inline-end:0}
details.fold[open]>summary::before,details.more[open]>summary::before,details.hub[open]>summary::before,details.grp[open]>summary::before{content:"−";content:"−" / "";background:var(--green-700);color:var(--white)}
details.more>summary,details.hub>summary{display:flex;align-items:center;min-height:44px;box-sizing:border-box}
details.more>summary{min-height:48px;padding:10px 0;background:none;border:0;border-top:1px solid var(--rule);border-bottom:1px solid var(--rule);font-size:var(--fs-src)}
details.more>summary:hover,details.more[open]>summary{color:var(--green-900)}
details.more[open]>summary{margin-bottom:6px}
details.grp>summary{display:flex;align-items:center;min-height:48px;box-sizing:border-box}
details.fold>.multiple,details.fold>figure{margin-top:16px}
details.chron-fold>p.small{margin:14px 0 4px}
.qa.fold-sec{display:block}
/* Home's topics block (DL-V2-007, F-15): the eight domain answers in one step — Canvas (OD-1018 D4): the topic cards of
   the canvas layer above replace G2's one-line register */
/* Home's named disclosures (owner decision B-a): the control beside the section's own kicker and heading */
/* B2 T (BRIEF W4 T): the report-an-error form, the citation format control and the Compare reason */
.report-form .rf{display:flex;flex-direction:column;gap:4px;margin:10px 0;font-size:var(--fs-clock);font-weight:600;color:var(--ink-2)}
.report-form input,.report-form textarea,.report-form select{font:inherit;font-size:var(--fs-src);font-weight:400;color:var(--ink);background:var(--white);border:1.5px solid var(--sage-600);border-radius:var(--r-btn);padding:10px 12px;min-height:44px;width:100%;max-width:100%;box-sizing:border-box}
.report-form textarea{min-height:88px;resize:vertical}
.report-form [aria-invalid="true"]{border-width:2px;border-color:var(--ink)}
.report-form .rf-err{font-weight:600;color:var(--ink)}.report-form .rf-err[hidden]{display:none}
.report-form .rf-errors{border:1px solid var(--ink);padding:8px 12px;margin:8px 0;font-weight:600}.report-form .rf-errors[hidden]{display:none}
.report-form .req{color:var(--ink)}.report-form .actions{margin-top:12px}.report-form .button{font:inherit;font-weight:600;background:var(--white);border:1.5px solid var(--green-700);border-radius:var(--r-btn);padding:10px 18px;min-height:44px;cursor:pointer;color:var(--green-700)}
.rf-grid{display:grid;grid-template-columns:1fr;gap:0 16px}@media (min-width:600px){.rf-grid{grid-template-columns:1fr 1fr}}
[data-report-nojs][hidden],[data-report-ref][hidden]{display:none}
.cite-format{margin:8px 0 0}.cite-format select{min-height:40px}
.cite-out{white-space:pre-wrap;word-break:break-word;font:inherit;font-size:var(--fs-src);background:var(--paper);border:1px solid var(--rule);padding:8px 12px;margin:8px 0;direction:ltr;text-align:left}.cite-out[hidden]{display:none}
.compare-reason{margin-top:4px;font-weight:600}
details.home-fold{margin-top:6px}
details.home-fold>summary{display:grid;grid-template-columns:22px minmax(0,1fr);column-gap:12px;row-gap:2px;align-items:center;padding:12px 0}
/* G2 pass two: on a phone Home's figures come before the topics line (G1: the figure-first candidates scored 15 and 12
   of 15 on first-screen comprehension against 12 for topics-first); on a wide screen the register keeps topics first */
@media (min-width:900px){
.obj.page-obj:has(> #topics)>:is(.head,.hero-art,.home-search){order:-2}.obj.page-obj:has(> #topics)>#topics{order:-1}   /* the markup carries the phone order (search, figures, index, topics); only the wide screen reorders */
}
details.home-fold>summary::before{grid-row:1 / span 2;align-self:center}
details.home-fold>summary>.rubric,details.home-fold>summary>h2{grid-column:2;margin:0}
details.home-fold>summary>h2{font-size:var(--fs-h2);line-height:var(--lh-h2)}
details.home-fold>.fold-body{padding:16px 0 4px}
/* the chronology as a dated list: the period as the line's key, the event as its text */
ol.chron>li.compact{padding:14px 0}
ol.chron .clock .v{color:var(--green-900)}
/* phone and small tablet: the in-page index becomes a wrapped row of chips under the head — the same links, in order;
   S10 (17 October 2026, G0-F04): at most six entries, wrapping instead of scrolling sideways, so none is hidden */
@media (max-width:899px){
/* G2 (DL-V2-001, G0-F04 closed: list over strip): the same links as plain numbered rows, nothing clamped */
/* Canvas: the numbered rows on one white card */
.strip{display:block;padding:2px 16px;background:var(--white);border:1px solid var(--sage-100);border-radius:var(--r-inner)}
.strip a{display:flex;gap:10px;align-items:baseline;padding:9px 0;min-height:40px;box-sizing:border-box;background:none;border:0;border-bottom:1px solid var(--rule);border-radius:0;font-size:var(--fs-src);line-height:1.35}
.strip a:last-child{border-bottom:0}
.strip a .n{min-width:1.8em;color:var(--mute)}
.strip a:hover{color:var(--green-700)}
}
/* tablet: bound records, measurement cards and Readings sit two to a row while the page is still one column */
@media (min-width:600px) and (max-width:899px){
.objs{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));column-gap:20px;border-top:0}
.objs>.compact,.objs>.compact:first-child{border-top:1px solid var(--rule)}
ol.objs.chron,.curated .objs,.source-locator-details .objs{display:flex;flex-direction:column}
}
/* the source register on a wide screen: what the source is on the left, what it is for and how to reach it on the right */
@media (min-width:1200px){
.src.card{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.45fr);column-gap:28px;row-gap:4px;align-items:start}
.src.card>h4,.src.card>.kind,.src.card>.rref,.src.card>.rights{grid-column:1}
.src.card>h4{grid-row:1}.src.card>.kind{grid-row:2}.src.card>.rref{grid-row:3}.src.card>.rights{grid-row:4}
.src.card>.small:not(.bnd-line){grid-column:2;grid-row:1 / span 2}
.src.card>.bnd-line{grid-column:2;grid-row:3}
.src.card>.acts{grid-column:2;grid-row:4}
.src.card>details.deps,.src.card>*:not(h4):not(.kind):not(.rref):not(.rights):not(.small):not(.acts):not(details){grid-column:1 / -1}
}
}
/* ---- V1 Phase B (owner decisions of 9 October 2026, B-c): the hubs' governed numerals, the page-tools row under the
   h1, the full phone menu. The numeral is the hub's own attribute (UI-NAV-HUB-0n), printed with empty alternative
   text so a link's accessible name stays its navigation label. ---- */
@media screen{
/* the page's own tools, one quiet row under its title, at every width */
/* G2 (DL-V2-001): the tools are quiet text links, and on a phone they follow the calls to action, so the title,
   the statement and the two actions come first; the record family (no statement) keeps them under the record line */
.page-tools{display:flex;flex-wrap:wrap;gap:2px 18px;margin:4px 0 0}
.page-tools>.tbtn,.page-tools>a{display:inline-flex;align-items:center;min-height:28px;box-sizing:border-box;padding:0;border:0;background:none;color:var(--ink-2);text-decoration:underline;text-decoration-color:var(--sage-400);font-size:var(--fs-clock);font-weight:500;line-height:1.2}
.page-tools>.tbtn:hover,.page-tools>a:hover{color:var(--green-700);text-decoration-color:currentColor}
.head .page-tools+.st,.head .page-tools+p.st{margin-top:8px}
.obj .head:has(> .st)>.page-tools{margin-top:10px}   /* the markup now places the tools last in the head; no visual reorder */
/* the full phone menu: five numbered hubs, the eight domain answers under Explore, trust, language and cite */
.nav.open{max-height:calc(100vh - 72px);max-height:calc(100dvh - 72px);overflow-y:auto;overscroll-behavior:contain}
.nav.open .group.mdoms{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));column-gap:18px;padding:2px 0 8px;padding-inline-start:1.9em;border-bottom:1px solid var(--rule)}
.nav.open .group.mdoms a{border-bottom:0;padding:9px 0;min-height:24px;font-size:.94em;color:var(--ink-2)}
.nav.open .group.mdoms a[aria-current=page]{color:var(--green-700);text-decoration:underline;text-underline-offset:3px}
.nav.open .mlang{display:block;margin-top:6px}
}
@media print{.page-tools{display:none!important}}
/* ---- V1 Phase B (owner decision B-b): the currentness strip and the Evidence Colophon ---- */
@media screen{
.cstrip{border-top:1px solid var(--rule);background:var(--sage-100)}
.cstrip-in{max-width:1440px;margin:0 auto;padding:4px 16px;display:flex;flex-wrap:wrap;align-items:center;gap:2px 10px;font-size:12.5px;line-height:1.4;color:var(--ink-2)}
[dir=rtl] .cstrip-in{font-size:12px}
@media (min-width:600px){.cstrip-in{font-size:var(--fs-clock)}}
.cs-line::before{content:"";display:inline-block;width:7px;height:7px;border-radius:50%;background:var(--green-700);margin-inline-end:8px;vertical-align:.08em}
.cs-sep{display:inline-block;width:1px;height:12px;background:var(--sage-400)}
.cstrip a{display:inline-block;padding:3px 0;min-height:24px;box-sizing:border-box;color:var(--green-900);text-decoration:underline;text-decoration-color:var(--sage-400);text-underline-offset:3px}
.cstrip a:hover{color:var(--green-700);text-decoration-color:currentColor}
.colophon{border-top:1px solid var(--sage-600);padding-top:18px;display:grid;gap:10px}
.colophon h3{font-size:var(--fs-rubric);color:var(--gold-300);margin:0}
[dir=ltr] .colophon h3{text-transform:uppercase;letter-spacing:.1em}
.colophon .col-st{margin:0;max-width:62ch;color:var(--paper);font-size:var(--fs-src)}
.colophon dl{margin:0;display:grid;grid-template-columns:minmax(0,1fr);gap:8px}
.colophon dl>div{display:flex;flex-direction:column;gap:1px}
.colophon dt{font-size:var(--fs-clock);color:var(--sage-100)}
.colophon dd{margin:0;font-weight:600;color:var(--paper)}
.colophon code{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:.95em;letter-spacing:.04em;font-weight:500}
.colophon .col-cite{margin:0}
.colophon .col-cite a{display:inline-block;padding:3px 0;min-height:24px;box-sizing:border-box}
}
@media screen and (max-width:599px){.colophon{gap:8px;padding-top:14px}.colophon dl{grid-template-columns:repeat(2,minmax(0,1fr));column-gap:16px}.colophon dl>div:last-child{grid-column:1 / -1}}
@media screen and (min-width:600px){.colophon dl{grid-template-columns:repeat(3,minmax(0,max-content));column-gap:40px}}
@media screen and (min-width:900px){.colophon{grid-column:1 / -1;grid-template-columns:minmax(0,1.3fr) minmax(0,2fr);column-gap:48px;align-items:start}.colophon h3,.colophon .col-st{grid-column:1}.colophon dl,.colophon .col-cite{grid-column:2}.colophon dl{grid-row:1 / span 2}.cstrip-in{padding-inline:32px}}
@media print{.cstrip,.colophon{display:none!important}}
/* ---- V1 Phase B (owner decision B-b): a curated source's description on demand, "About this source", in the same
   quiet disclosure as the records and Readings that use it; on a wide screen it stays open where supported ---- */
@media screen{
details.about{margin:4px 0 2px}
details.about>summary{cursor:pointer;list-style:none;display:inline-block;padding:3px 0;min-height:24px;box-sizing:border-box;font-size:var(--fs-clock);font-weight:600;color:var(--ink-2)}
details.about>summary::-webkit-details-marker{display:none}
details.about>summary::before{content:"+ ";color:var(--green-700);font-weight:600}
details.about[open]>summary::before{content:"− "}
details.about>summary:hover{color:var(--green-700)}
details.about>p.small{margin:4px 0 2px}
}
@media screen and (min-width:1200px){
.src.card>details.about{grid-column:2;grid-row:1 / span 2;margin:0}
@supports selector(::details-content){
.src.card>details.about>summary{display:none}
.src.card>details.about::details-content{content-visibility:visible;display:block}
.src.card>details.about>p.small{margin:0}
}
}
@media print{details.about>summary{display:none}details.about::details-content{content-visibility:visible;display:block}}
/* ---- V1 Phase B: the search and filter tools. The query field stays in view while results scroll; the query's words
   are marked in each result; a filter that is set looks set. No control, label or hook changes. ---- */
@media screen{
dialog.search{overflow:hidden}
dialog.search .search-panel{box-sizing:border-box;max-height:calc(100vh - 2em - 6px);max-height:calc(100dvh - 2em - 6px)}
dialog.search [data-search-results]{flex:1 1 auto;min-height:0;overflow-y:auto;overscroll-behavior:contain;margin-inline:-6px;padding-inline:6px}
.search-results .search-hit mark,[data-search-results] .search-hit mark{background:var(--sage-100);color:inherit;box-shadow:inset 0 -2px 0 var(--brass-300);padding:0 1px;border-radius:1px}
.search-results .search-hit:hover h4,[data-search-results] .search-hit:hover h4{color:var(--green-700);text-decoration:underline;text-decoration-color:var(--sage-400);text-underline-offset:3px}
.search-results .search-hit:focus-visible{outline-offset:2px}
.source-facets select:has(option:checked:not([value=""])),.search-type:has(option:checked:not([value=""])){border-color:var(--green-700);box-shadow:inset 0 0 0 1px var(--green-700);font-weight:600;color:var(--green-900)}
.source-facets .facet:has(option:checked:not([value=""]))>span{color:var(--green-700)}
.source-facets .facet:has(option:checked:not([value=""]))>span::before{content:"";display:inline-block;width:6px;height:6px;border-radius:50%;background:var(--green-700);margin-inline-end:6px;vertical-align:.1em}
}
@media (forced-colors:active){.search-hit mark{background:Mark;color:MarkText;box-shadow:none}}
"""
