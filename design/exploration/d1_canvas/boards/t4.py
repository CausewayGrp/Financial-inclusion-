# -*- coding: utf-8 -*-
"""T4 · INSTRUMENT — second-generation Design proposition (canvas).

One mental model: YFIE is an instrument that answers the reader's questions about evidence and states what it cannot
answer. Signature behaviours, all grown from the evidence doctrine (ANSWER → SCOPE → BOUNDARY → VERIFY):
  1. clock-first evidence objects — a bound record is always read as WHEN and FOR WHOM before its claim; a number is
     never typeset outside its bounded object or its governed sentence;
  2. the seven governed questions of an Evidence Record are its structure and its index, in the same order everywhere;
  3. every boundary is a second voice in one register (double rule + label + weight + colour; never colour alone);
  4. a verification spine on every page with the same anatomy (what the page rests on; where it returns to);
  5. unlike things never share an axis, a row or a colour: the firewall is structural.
Composed mobile-first (the Arabic mobile record first); desktop is the same system with a spine column.
Surfaces: paper and plaster; rules: hairline, a heavy ink rule at object starts, a doubled rule at boundaries; the
canonical logo's three colours become three roles — ochre for rubrics, navy ink for text, teal-green for the boundary.
"""
from __future__ import annotations

import re

from common import esc, bdi, paragraphs, reading_blocks, nav_flat, logo, responsive_rules, rv001_data, rv001_panel1_rows_svg, rv001_index_panel_svg, rv001_tables, rv001_frame_lines

CUR = ' aria-current="page"'
NAME = "T4 · Instrument"

TOKENS = """
:root,.root{--paper:#FFFFFF;--plaster:#F5F1E9;--ink:#17212B;--ink-2:#3D4954;--mute:#66717B;--rule:#D8DDE2;--rule-2:#AEB7BF;--ochre:#7A5A1D;--ochre-line:#D6B86A;--counter:#1E5650;
--fs-body:17px;--lh-body:1.6;--fs-display:32px;--lh-display:1.1;--fs-q:20px;--lh-q:1.4;--fs-st:19px;--lh-st:1.5;--fs-bnd:18px;--lh-bnd:1.55;--fs-clock:13.5px;--lh-clock:1.4;--fs-rubric:12px;--fs-src:14.5px;--lh-src:1.5;--fs-nav:15px;--fs-read:18px;--lh-read:1.65;--measure:64ch;--font:'IBM Plex Sans',sans-serif}
html[dir=rtl],[dir=rtl].root{--fs-body:18px;--lh-body:1.9;--fs-display:30px;--lh-display:1.35;--fs-q:21px;--lh-q:1.7;--fs-st:20px;--lh-st:1.7;--fs-bnd:19px;--lh-bnd:1.8;--fs-clock:14.5px;--lh-clock:1.7;--fs-rubric:13px;--fs-src:15.5px;--lh-src:1.75;--fs-nav:16px;--fs-read:19.5px;--lh-read:1.95;--measure:34em;--font:'IBM Plex Sans Arabic',sans-serif}
"""

BASE = TOKENS + """
html,.root{background:var(--paper);color:var(--ink);font-family:var(--font);font-size:var(--fs-body);line-height:var(--lh-body);font-variant-numeric:tabular-nums}
body{margin:0}
a{color:inherit;text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:.16em;text-decoration-color:var(--rule-2)}
h1,h2,h3,h4{margin:0;font-weight:600}
h1{font-size:var(--fs-display);line-height:var(--lh-display)}[dir=ltr] h1{letter-spacing:-.012em}
h2{font-size:var(--fs-q);line-height:var(--lh-q)}
h3{font-size:17px;line-height:1.4}
p{margin:0 0 .85em}p:last-child{margin-bottom:0}
.tbtn{background:none;border:0;padding:0;font:inherit;color:inherit;text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:.16em;text-decoration-color:var(--rule-2);cursor:pointer}
.rubric{display:block;font-size:var(--fs-rubric);line-height:1.4;font-weight:600;color:var(--ochre)}
[dir=ltr] .rubric{text-transform:uppercase;letter-spacing:.1em}
.clock{display:flex;flex-direction:column;gap:2px;font-size:var(--fs-clock);line-height:var(--lh-clock)}
.clock .k{font-weight:600;color:var(--mute)}
.clock .v{font-weight:600;color:var(--ink)}
.ref{font-size:var(--fs-clock);line-height:var(--lh-clock);color:var(--mute);font-weight:500}
.ref b{color:var(--ink-2);font-weight:600}
.q{font-size:var(--fs-q);line-height:var(--lh-q);font-weight:500}
.q a{text-decoration-color:var(--ochre-line)}
.st{font-size:var(--fs-st);line-height:var(--lh-st);font-weight:500;max-width:var(--measure)}
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
.controls{display:flex;align-items:center;gap:12px;font-size:14px;font-weight:500}
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
.qa.first{border-top:0;padding-top:0}
.crumb{font-size:var(--fs-clock);color:var(--mute);margin-bottom:2px}
.crumb a{text-decoration:none}
.strip{display:flex;flex-wrap:wrap;gap:6px;padding:4px 0}
.strip a{display:inline-flex;gap:6px;align-items:baseline;border:1px solid var(--rule-2);padding:6px 10px;font-size:var(--fs-clock);font-weight:500;text-decoration:none;background:var(--paper)}
.strip a .n{color:var(--mute);font-weight:600}
.compact{display:flex;flex-direction:column;gap:6px;padding:14px 0;border-top:1px solid var(--rule)}
.compact:first-child{border-top:0}
.compact .q{font-size:calc(var(--fs-q) - 1px)}
.compact .open{font-size:var(--fs-src);font-weight:500}
.objs{display:flex;flex-direction:column;border-top:1px solid var(--rule-2)}
.objs>.compact:first-child{border-top:0}
.paced p{max-width:var(--measure)}
.paced .sent{display:block;margin:0 0 .45em;font-size:var(--fs-st);line-height:var(--lh-st);font-weight:500}
.paced .sent.res{font-weight:600;border-top:1px solid var(--ochre-line);padding-top:.6em;margin-top:.4em}
.actions{display:flex;flex-wrap:wrap;gap:10px 26px;margin-top:14px;font-weight:600}
.actions a{text-decoration-color:var(--ochre-line);text-decoration-thickness:2px}
.qlist{list-style:none;margin:0;padding:0;counter-reset:q}
.qlist li{display:grid;grid-template-columns:34px minmax(0,1fr);gap:10px;padding:14px 0;border-top:1px solid var(--rule)}
.qlist li::before{counter-increment:q;content:counter(q,decimal-leading-zero);font-size:var(--fs-clock);font-weight:600;color:var(--mute);padding-top:5px}
.qlist .gets{margin-top:4px}
.src{display:flex;flex-direction:column;gap:6px;padding:14px 0;border-top:1px solid var(--rule)}
.src:first-child{border-top:0;padding-top:0}
.src strong{font-size:var(--fs-body)}
.src .kind,.src .rref{font-size:var(--fs-clock);color:var(--mute);font-weight:500}
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
.spine{display:flex;flex-direction:column;gap:14px;background:var(--plaster);padding:16px;margin-top:8px}
.spine h3{font-size:var(--fs-rubric);color:var(--ochre);font-weight:600;margin:0 0 8px}
[dir=ltr] .spine h3{text-transform:uppercase;letter-spacing:.1em}
.spine .index{display:none}
.spine ul{list-style:none;margin:0;padding:0}
.spine li{border-top:1px solid var(--rule-2);padding:7px 0;font-size:var(--fs-src);line-height:var(--lh-src)}
.spine li:first-child{border-top:0;padding-top:0}
.spine a{text-decoration:none}
.spine .index li a{display:flex;gap:10px}
.spine .index .n{color:var(--mute);font-weight:600;min-width:1.6em}
.spine .index a[aria-current]{font-weight:600;border-inline-start:3px solid var(--ochre);padding-inline-start:8px}
/* reading */
.pull{margin:22px 0;padding:0 0 0 20px;border-inline-start:2px solid var(--ochre-line);font-size:var(--fs-q);line-height:var(--lh-q);font-weight:500;max-width:var(--measure)}
[dir=rtl] .pull{padding:0 20px 0 0}
.rlist{padding-inline-start:1.2em}
.essay section{padding:6px 0 26px}
.essay section+section{border-top:1px solid var(--rule);padding-top:24px}
.essay h2{margin-bottom:10px}
.fig{background:var(--plaster);padding:18px 16px 16px;margin:20px 0 4px;border-top:3px solid var(--ink)}
.fig h4{font-size:var(--fs-q);line-height:var(--lh-q);margin-bottom:6px}
.fig .cap{font-size:var(--fs-clock);line-height:var(--lh-clock);color:var(--ink-2);margin:0 0 4px;max-width:70ch}
.panels{display:flex;flex-direction:column;gap:18px;padding-top:12px;border-top:1px solid var(--rule-2);margin-top:12px}
.panel h5{margin:0 0 6px;font-size:var(--fs-clock);font-weight:600;color:var(--ink-2)}
.rows{display:grid;grid-template-columns:minmax(120px,.45fr) minmax(0,1fr);gap:0 12px;align-items:center}
.rows .rl{font-size:var(--fs-clock);line-height:var(--lh-clock);font-weight:600;padding:10px 0}
.between{border-top:3px double var(--counter);padding-top:8px;font-size:var(--fs-clock);font-weight:600;color:var(--counter)}
.lanes{display:flex;flex-direction:column;gap:14px}
.lane h5{color:var(--ink)}
.legend{display:flex;flex-wrap:wrap;gap:8px 18px;font-size:var(--fs-clock);color:var(--ink-2);margin-top:6px}
.legend .k{display:inline-flex;align-items:center;gap:7px}
.legend .sw{display:inline-block;width:11px;height:11px;background:var(--ink)}.legend .sw.c{border-radius:50%}.legend .sw.s{background:var(--plaster);border:2px solid var(--ink)}
.fig .foot{display:flex;flex-direction:column;gap:6px;font-size:var(--fs-clock);line-height:var(--lh-clock);color:var(--ink-2);margin-top:12px}
.fig .foot .b{color:var(--counter);font-weight:500;font-size:var(--fs-src)}
svg.rv1,svg.rv2{max-width:100%;height:auto;font-family:var(--font)}
.axis{stroke:var(--ink);stroke-width:1}.grid{stroke:var(--rule-2);stroke-width:1;stroke-dasharray:2 3}.tick{stroke:var(--ink);stroke-width:1}.stem{stroke:var(--rule-2);stroke-width:1}
.lbl{font-size:11px;fill:var(--mute);font-weight:500}.lbl.origin{fill:var(--ink)}.unit{font-size:11px;fill:var(--ink-2);font-weight:600}
.val{font-size:12.5px;fill:var(--ink);font-weight:600}.val.small{font-size:11px}
.mark.a{fill:var(--ink)}.mark.b{fill:var(--plaster);stroke:var(--ink);stroke-width:2}
.path{stroke:var(--ink);stroke-width:1.5}
.rvtab{border-collapse:collapse;width:100%;font-size:var(--fs-clock);line-height:var(--lh-clock);margin-top:10px;background:var(--paper)}
.rvtab caption{text-align:start;font-weight:600;color:var(--ink-2);padding:8px 0}
.rvtab th,.rvtab td{text-align:start;padding:7px 10px;border-top:1px solid var(--rule);vertical-align:top}
.rvtab thead th{border-top:1px solid var(--ink);font-weight:600}
.rvtab .state{color:var(--mute)}.rvtab .marker{font-weight:600;color:var(--counter)}
details.alt summary{cursor:pointer;font-size:var(--fs-src);font-weight:600;list-style:none;margin-top:12px}
details.alt summary::-webkit-details-marker{display:none}
details.alt summary::before{content:"+ ";color:var(--ochre)}
details.alt[open] summary::before{content:"− "}
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
"""

DESKTOP = """
:root,.root{--fs-display:46px;--fs-q:23px;--fs-st:21px;--fs-body:17px;--fs-read:19px;--fs-bnd:19px}
[dir=rtl],[dir=rtl].root{--fs-display:42px;--fs-q:24px;--fs-st:22px;--fs-body:18px;--fs-read:20px;--fs-bnd:20px}
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
.page{padding:28px 32px 56px;display:grid;grid-template-columns:minmax(0,1fr) 300px;column-gap:48px;row-gap:0;align-items:start}
.page>.obj{grid-column:1;max-width:840px}
.spine{grid-column:2;grid-row:1 / span 20;position:sticky;top:20px;margin-top:0;padding:18px 20px}
.spine .index{display:block}
.strip{display:none}
.foot-spine{display:none}
.obj.page-obj{gap:22px;padding-top:22px}
.qa{display:grid;grid-template-columns:220px minmax(0,1fr);gap:4px 36px;padding-top:16px}
.qa .rubric{padding-top:4px}
.compact{display:grid;grid-template-columns:220px minmax(0,1fr);gap:4px 36px;padding:16px 0}
.compact .clock{grid-row:1 / span 3}
.compact .open{grid-column:2}
.compact .small{grid-column:2}
.compact .q{grid-column:2}
.paced .sent{font-size:22px;line-height:1.45}
[dir=rtl] .paced .sent{font-size:23px;line-height:1.7}
.bnd{margin-top:26px;padding-top:14px}
.panels{flex-direction:row;align-items:flex-start;gap:28px}
.panels>.panel{flex:1 1 0;min-width:0}
.panels>.panel.p2{flex:1.5 1 0}
.between{border-top:0;border-inline-start:3px double var(--counter);padding:0 0 0 14px;align-self:center;max-width:10em}
[dir=rtl] .between{padding:0 14px 0 0}
.lanes{flex-direction:row}
.lanes>.lane{flex:1 1 0;min-width:0}
.inst-in{padding:36px 32px 24px;display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,2fr);gap:28px 48px}
.inst .trust{grid-column:1 / -1}
.inst .groups{flex-direction:row;gap:36px}
.inst .fine{grid-column:1 / -1}
.essay section{padding:8px 0 30px}
h1{max-width:22ch}
"""

CSS = BASE + responsive_rules(DESKTOP, "min-width:900px", "vp-d")


def rubric(t, cls="rubric"):
    return f'<span class="{cls}">{esc(t)}</span>'


def clock(label, value):
    return f'<div class="clock"><span class="k">{esc(label)}</span><span class="v">{value}</span></div>'


def header(shell):
    L = shell["labels"]
    nav = []
    for it in nav_flat(shell):
        if "group" in it:
            kids = "".join(f'<a href="{k["href"]}"{CUR if k["active"] else ""}>{esc(k["label"])}</a>' for k in it["children"])
            nav.append(f'<span class="group"><span class="glabel">{esc(it["group"])}</span>{kids}</span>')
        else:
            nav.append(f'<a href="{it["href"]}"{CUR if it["active"] else ""}>{esc(it["label"])}</a>')
    other = shell["other_lang"]
    return (f'<header class="bar"><div class="bar-in"><a class="brand" href="{shell["home_href"]}">{logo(40)}<span class="brand-name">{esc(shell["product"])}</span></a>'
            f'<nav class="nav" aria-label="{esc(L["primary_nav"])}">{"".join(nav)}</nav>'
            f'<div class="controls"><button type="button" class="tbtn">{esc(L["search"])}</button><button type="button" class="tbtn cite">{esc(L["cite"])}</button><a class="report" href="{shell["contact_href"]}">{esc(L["report"])}</a>'
            f'<button type="button" class="tbtn lang" lang="{other}" dir="{"ltr" if other == "en" else "rtl"}">{esc(L["lang_switch_name"])}</button><button type="button" class="tbtn menu">{esc(L["menu"])}</button></div></div></header><main>')


def footer(shell):
    L = shell["labels"]
    trust = "".join(f'<a href="{t["href"]}">{esc(t["label"])}</a>' for t in shell["trust"])
    trust_label = next((g["label"] for g in shell["footer"] if any(l["href"].endswith("/about/") for l in g["links"])), L["trust_nav"])
    groups = "".join(f'<div><strong>{esc(g["label"])}</strong>' + "".join(f'<a href="{l["href"]}">{esc(l["label"])}</a>' for l in g["links"]) + "</div>"
                     for g in shell["footer"] if not any(l["href"].endswith("/about/") for l in g["links"]))
    return (f'</main><footer class="inst"><div class="inst-in"><div class="trust"><h3>{esc(trust_label)}</h3><nav aria-label="{esc(L["trust_nav"])}">{trust}</nav></div>'
            f'<div class="id">{logo(40)}<p>{esc(L["footer_strapline"])}</p></div><nav class="groups" aria-label="{esc(L["footer_nav"])}">{groups}</nav>'
            f'<div class="fine">© 2026 CauseWay · {esc(L["footer_rights"])} · {esc(shell["edition"])}</div></div></footer>')


def crumb(bc, shell):
    if not bc:
        return ""
    cur = bdi(bc["current"]) if bc["mode"] == "STABLE_OBJECT_ID" else esc(bc["current"])
    return f'<nav class="crumb" aria-label="{esc(shell["labels"]["breadcrumb"])}"><a href="{bc["parent_href"]}">{esc(bc["parent_label"])}</a> / <span aria-current="page">{cur}</span></nav>'


def source_card(s):
    L = s["labels"]
    ref = f'<span class="rref">{esc(s["reference_label"])} {bdi(s["id"])}</span>'
    head_ = f'<strong dir="auto">{esc(s["title"])}</strong><span class="kind" dir="auto">{esc(s["kind_line"])}</span>{ref}' if s["display_ready"] and s["title"] else f'<strong>{esc(s["untitled_label"])}</strong>{ref}'
    rights = f'<p class="rights">{esc(s["rights_note"])}</p>' if s["rights_note"] else ""
    return (f'<article class="src">{head_}<div class="acts"><a href="{s["data_href"]}">{esc(L["open_source_record"])}</a><a href="{esc(s["url"])}">{esc(L["open_original"])}</a><button type="button" class="tbtn">{esc(L["copy_reference"])}</button></div>{rights}</article>')


def compact(rec, L, open_label):
    """Clock-first compact evidence object: when → title → for whom → open."""
    ck = clock(L["period"], esc(rec["period"])) if rec.get("period") else clock(L["period"], "")
    return (f'<article class="compact">{ck}<div class="q"><a href="{rec["href"]}">{esc(rec["title"])}</a></div>'
            + (f'<div class="small">{esc(rec["universe"])}</div>' if rec.get("universe") else "")
            + f'<div class="open"><a href="{rec["href"]}">{esc(open_label)}</a></div></article>')


def spine(index, edges, foot=False):
    idx = "".join(f'<li><a href="#{a}"><span class="n">{i+1:02d}</span><span>{esc(t)}</span></a></li>' for i, (a, t) in enumerate(index))
    ed = "".join(f'<div class="edges"><h3>{esc(h)}</h3><ul>' + "".join(f"<li>{x}</li>" for x in items) + "</ul></div>" for h, items in edges if items)
    cls = "spine foot-spine" if foot else "spine"
    index_html = "" if foot else f'<nav class="index"><ul>{idx}</ul></nav>'
    return f'<aside class="{cls}">{index_html}{ed}</aside>'


def strip(index):
    return '<nav class="strip">' + "".join(f'<a href="#{a}"><span class="n">{i+1:02d}</span><span>{esc(t)}</span></a>' for i, (a, t) in enumerate(index)) + "</nav>"


SENT = re.compile(r"(?<=[.؟?!])\s+(?=[A-Z«؀-ۿ])")


def paced(text, resolution_prefix=("These are different measures", "هذه مقاييس مختلفة")):
    """A governed paragraph paced sentence by sentence (one <p>, block spans): the words and their order are intact."""
    sents = [x.strip() for x in SENT.split(text) if x.strip()]
    out = []
    for s in sents:
        cls = "sent res" if s.startswith(resolution_prefix) else "sent"
        out.append(f'<span class="{cls}">{esc(s)}</span>')
    return f'<p>{"".join(out)}</p>'


def figure(v, lang):
    d = rv001_data(v); f = rv001_frame_lines(v)
    row_labels = f'<div class="rows"><div class="rl">{esc(d["label_ar2024"])}</div><div></div><div class="rl">{esc(d["label_ar2025"])}</div><div></div></div>'
    return (f'<figure class="fig"><span class="rubric">{esc(v["labels"]["analytical_question"])}</span><h4>{esc(f["title"])}</h4><p class="cap">{esc(v["question"])}</p><p class="cap">{esc(f["scope"])}</p>'
            f'<div class="panels"><div class="panel p1"><h5>2024 · {esc(d["unit_usd"])}</h5><div class="rows"><div class="rl">{esc(d["label_ar2024"])}<br>{esc(d["label_ar2025"])}</div><div>{rv001_panel1_rows_svg(d, lang)}</div></div>'
            f'<div class="legend"><span class="k"><span class="sw c"></span>{esc(d["label_ar2024"])}</span><span class="k"><span class="sw s"></span>{esc(d["label_ar2025"])}</span></div><p class="cap" style="margin-top:8px"><b>{esc(f["same_year"])}</b></p></div>'
            f'<div class="between">{esc(f["not_comparable"])}</div>'
            f'<div class="panel p2"><h5>{esc(d["unit_index"])} · {esc(v["labels"]["derived"])}</h5><div class="lanes"><div class="lane"><h5>{esc(d["label_cby"])}</h5>{rv001_index_panel_svg(d["cby_index"], lang, w=280, h=200, mark="circle")}</div><div class="lane"><h5>{esc(d["label_imf"])}</h5>{rv001_index_panel_svg(d["imf_index"], lang, w=280, h=200, mark="square")}</div></div><p class="cap" style="margin-top:8px">{esc(f["note"])}</p></div></div>'
            f'<div class="foot"><p class="b"><b>{esc(f["boundary_label"])}</b> {esc(f["boundary"])}</p><p>{esc(f["credit"])}</p><p>{esc(f["full_record_label"])} <a href="{f["full_record"]}">{esc(f["full_record"])}</a></p></div>'
            f'<details class="alt"><summary>{esc(v["labels"]["text_alternative"])}</summary><p class="small" style="padding-top:8px">{esc(v["alt_text"])}</p><div class="table-wrap">{rv001_tables(d, v, lang)}</div></details>'
            f'<figcaption class="sr-only">{esc(v["alt_text"])}</figcaption></figure>')


# ------------------------------------------------------------------------------------------------ surfaces
def record(page, shell):
    L = page["labels"]
    index = [("q1", L["establishes"]), ("q2", L["measures"]), ("q3", L["applies"]), ("q4", L["currentness"]), ("q5", L["does_not_establish"]), ("q6", L["source"]), ("q7", L["more"])]
    summary = esc(page["summary"])
    head = (f'<div class="head">{crumb(page["breadcrumb"], shell)}{rubric(L["family"])}{clock(L["period"], esc(page["period"]))}'
            f'<div class="ref"><b>{esc(L["reference"])}</b> {bdi(page["id"])}</div><h1>{esc(page["title"])}</h1></div>' + strip(index))
    qa = [f'<div class="qa first" id="q1">{rubric(L["establishes"])}<div class="st"><p>{summary}</p></div></div>',
          f'<div class="qa" id="q2">{rubric(L["measures"])}<div class="body"><p>{esc(page["definition"])}</p></div></div>',
          f'<div class="qa" id="q3">{rubric(L["applies"])}<div class="body"><p>{esc(page["universe"])}</p></div></div>',
          f'<div class="qa" id="q4">{rubric(L["currentness"])}<div class="body"><p>{esc(page["currentness"])}</p></div></div>',
          f'<div class="bnd" id="q5">{rubric(L["does_not_establish"])}<p>{esc(page["does_not_establish"])}</p></div>']
    chips = "".join(f'<a class="chip" href="/{shell["lang"]}/data/?source={esc(sid)}#source-{esc(sid)}">{bdi(sid)}</a>' for sid in page["trace_ids"])
    qa.append(f'<div class="qa" id="q6">{rubric(L["source"])}<div><p class="small">{esc(L["source_intro"])}</p><div style="margin-top:10px">{"".join(source_card(s) for s in page["sources"])}</div>'
              f'<div style="margin-top:16px"><span class="small"><b>{esc(L["trace"])}</b> · {esc(L["trace_intro"])}</span><div class="chips"><span class="chip">{bdi(page["id"])}</span>{chips}</div></div></div></div>')
    more = "".join(f'<div class="qa">{rubric(L[k])}<div class="body"><p>{esc(page[k])}</p></div></div>' for k in ("method", "change_trigger", "verification") if page[k])
    more += f'<div class="qa">{rubric(L["reading_guidance"])}<div class="body">{paragraphs(page["reading_guidance"]["paragraphs"])}</div></div>'
    qa.append(f'<div class="qa" id="q7">{rubric(L["more"])}<details class="more"><summary>{esc(L["more_intro"])}</summary>{more}</details></div>')
    util = (f'<div class="util"><div class="ref"><b>{esc(L["reference"])}</b> {bdi(page["id"])}</div><div class="actions"><button type="button" class="tbtn">{esc(L["cite"])}</button><a href="{page["hrefs"]["rights"]}">{esc(L["reuse"])}</a><a href="{page["hrefs"]["corrections"]}">{esc(L["history"])}</a><a href="{page["hrefs"]["report"]}">{esc(L["report"])}</a></div><p class="small">{esc(L["reuse_note"])}</p></div>')
    edges = [(L["used_in"], [f'<a href="{x["href"]}">{esc(x["title"])}</a>' for x in page["used_in_readings"]]),
             (L["related"], [f'<a href="{x["href"]}">{esc(x["label"])}</a>' for x in page["routes_back"]] + [f'<a href="{page["hrefs"]["evidence"]}">{esc(L["evidence_hub"])}</a>', f'<a href="{page["hrefs"]["data"]}">{esc(L["data"])}</a>', f'<a href="{page["hrefs"]["methodology"]}">{esc(L["methodology"])}</a>'])]
    return header(shell) + f'<div class="page"><article class="obj page-obj">{head}{"".join(qa)}{util}</article>{spine(index, edges)}{spine(index, edges, foot=True)}</div>' + footer(shell)


def home(page, shell):
    L = page["labels"]; S = {s["order"]: s for s in page["sections"]}
    index = [("s3", S[3]["heading"]), ("s4", S[4]["heading"]), ("s1", L["product"]), ("s9", S[9]["heading"]), ("s5", S[5]["heading"]), ("s6", S[6]["heading"]), ("s7", S[7]["heading"]), ("s8", S[8]["heading"]), ("sf", L["featured"])]
    parts = [f'<div class="head">{rubric(L["product"])}<h1>{esc(page["title"])}</h1></div>' + strip(index)]
    parts.append(f'<div class="qa first" id="s3"><h2>{esc(S[3]["heading"])}</h2><div class="paced">{paced(S[3]["body"])}</div></div>')
    objs = "".join(compact(r, L, L["open_evidence_record"]) for r in page["records"])
    parts.append(f'<div class="qa">{rubric(L["records_heading"])}<div class="objs">{objs}</div></div>')
    parts.append(f'<div class="bnd" id="s4"><h2>{esc(S[4]["heading"])}</h2><div style="margin-top:8px">{paragraphs(S[4]["paragraphs"])}</div></div>')
    parts.append(f'<div class="qa" id="s1">{rubric(L["flow"])}<div><div class="st">{paragraphs(S[1]["paragraphs"])}</div><div class="actions"><a href="{page["hrefs"]["explore"]}">{esc(L["start"])}</a><a href="{page["hrefs"]["evidence"]}">{esc(L["verify"])}</a></div></div></div>')
    qs = "".join(f'<li><div><div class="q"><a href="{q["href"]}">{esc(q["question"])}</a></div><div class="gets small">{esc(q["gets"])}</div></div></li>' for q in page["starting_questions"])
    parts.append(f'<div class="qa" id="s9"><h2>{esc(S[9]["heading"])}</h2><div><p class="small">{esc(S[9]["body"])}</p><ol class="qlist">{qs}</ol><p class="small" style="margin-top:12px"><a href="{page["hrefs"]["explore"]}">{esc(L["view_all"])}</a></p></div></div>')
    parts.append(f'<div class="qa" id="s5"><h2>{esc(S[5]["heading"])}</h2><div class="body">{paragraphs(S[5]["paragraphs"])}</div></div>')
    v = page["system_visual"]
    parts.append(f'<div class="qa" id="s6"><h2 id="system">{esc(S[6]["heading"])}</h2><div><div class="body">{paragraphs(S[6]["paragraphs"])}</div>'
                 f'<div class="fig" style="margin-top:18px"><span class="rubric">{esc(L["visual_eyebrow"])}</span><h4>{esc(v["title"])}</h4><p class="cap">{esc(v["question"])}</p><div class="body"><p>{esc(v["alt_text"])}</p></div><p class="small" style="margin-top:8px"><a href="{v["canonical_href"]}">{esc(L["open_record"])}</a></p></div></div></div>')
    for o, i in ((7, "s7"), (8, "s8")):
        parts.append(f'<div class="qa" id="{i}"><h2>{esc(S[o]["heading"])}</h2><div class="body">{paragraphs(S[o]["paragraphs"])}</div></div>')
    f = page["featured"]
    parts.append(f'<div class="qa" id="sf">{rubric(L["featured"])}<div><article class="compact" style="border-top:0;padding-top:0">{clock(L["evidence_period"], esc(f["evidence_period"]))}<div class="q"><a href="{f["href"]}">{esc(f["title"])}</a></div><div class="st"><p>{esc(f["thesis"])}</p></div><div class="open"><a href="{f["href"]}">{esc(L["open_reading"])}</a> · <a href="{page["hrefs"]["readings"]}">{esc(L["all_readings"])}</a></div></article></div></div>')
    edges = [(L["records_heading"], [f'<a href="{r["href"]}">{esc(r["title"])}</a>' for r in page["records"]]),
             (L["flow"], [f'<a href="{h}">{esc(t)}</a><br><span class="small">{esc(d)}</span>' for h, t, d in ((page["hrefs"]["readings"], L["readings_nav"], L["cta_readings"]), (page["hrefs"]["measurement"], L["measurement_nav"], L["cta_measurement"]), (page["hrefs"]["data"], L["data_nav"], L["cta_data"]))])]
    return header(shell) + f'<div class="page"><article class="obj page-obj">{"".join(parts)}</article>{spine(index, edges)}{spine(index, edges, foot=True)}</div>' + footer(shell)


def reading(page, shell):
    L = page["labels"]; lang = shell["lang"]
    index = [(f's-{s["section_id"]}', s["heading"]) for s in page["sections"] if s["heading"]] + [("trace", L["trace"]), ("sources", L["sources"]), ("related", L["related"])]
    head = (f'<div class="head">{crumb(page["breadcrumb"], shell)}{rubric(L["eyebrow"])}<div class="q">{esc(page["question"])}</div><h1>{esc(page["title"])}</h1><div class="st"><p>{esc(page["thesis"])}</p></div>'
            f'<div style="display:flex;flex-wrap:wrap;gap:10px 32px;margin-top:6px">{clock(L["evidence_period"], esc(page["evidence_period"]))}{clock(L["last_reviewed"], esc(page["last_reviewed"]))}</div></div>' + strip(index))
    bnd = f'<div class="bnd">{rubric(L["do_not_infer"])}<p>{esc(page["prohibited_inference"])}</p></div>'
    essay = []
    for i, s in enumerate(page["sections"]):
        h = f'<h2 id="s-{esc(s["section_id"])}">{esc(s["heading"])}</h2>' if s["heading"] else ""
        essay.append(f'<section>{h}<div class="{"st" if i == 0 else "read"}">{reading_blocks(s["blocks"])}</div>{"".join(figure(v, lang) for v in page["visuals"]) if i == 0 else ""}</section>')
    steps = []
    for x in page["trace"]:
        srcs = " · ".join(f'<a href="{s["data_href"]}">{esc(s["title"] or s["id"])}</a>' for s in x["sources"])
        if x["no_locator_note"]:
            srcs += (" · " if srcs else "") + esc(x["no_locator_note"])
        flag = f' · {esc(x["state_flag"])}' if x["state_flag"] else ""
        steps.append(f'<article class="compact">{clock(L["evidence_period"], esc(x["period"]))}<div class="q"><a href="{x["href"]}">{esc(x["proposition"])}</a></div><div class="small">{esc(L["reference"])} {bdi(x["id"])}{flag}</div><div class="small">{srcs}</div></article>')
    trace = (f'<div class="qa" id="trace"><h2>{esc(L["trace"])}</h2><div><p class="small">{esc(L["trace_intro"])}</p><p class="small"><b>{esc(page["trace_status"])}</b></p><div class="objs">{"".join(steps)}</div>'
             f'<div class="actions"><a href="{page["compare_href"]}">{esc(L["compare"])}</a></div></div></div>')
    sources = f'<div class="qa" id="sources"><h2>{esc(L["sources"])}</h2><div>{"".join(source_card(s) for s in page["sources"])}</div></div>'
    rel = "".join(f'<article class="compact">{clock(L["evidence_period"], esc(x["evidence_period"]))}<div class="q"><a href="{x["href"]}">{esc(x["title"])}</a></div><div class="small">{esc(x["thesis"])}</div></article>' for x in page["related"])
    related = f'<div class="qa" id="related"><h2>{esc(L["related"])}</h2><div><div class="objs">{rel}</div><p class="small" style="margin-top:12px"><a href="{L["readings_index_href"]}">{esc(L["all"])}</a></p></div></div>'
    edges = [(L["trace"], [f'<a href="{x["href"]}">{esc(x["proposition"])}</a>' for x in page["trace"]]),
             (L["return"], [f'<a href="{b["href"]}">{esc(b["label"])}</a>' for b in page["return_to"]])]
    body = f'<article class="obj page-obj">{head}{bnd}<div class="essay">{"".join(essay)}</div>{trace}{sources}{related}</article>'
    return header(shell) + f'<div class="page">{body}{spine(index, edges)}{spine(index, edges, foot=True)}</div>' + footer(shell)


COMPOSE = {"home": home, "record": record, "reading": reading}
