# -*- coding: utf-8 -*-
"""T3 · STRATA — Design proposition (canvas). The evidence system made spatial: every page is a fixed sequence of
strata (answer → scope → boundary → source) on stacked surfaces, with a persistent, relevance-limited evidence trail.
Grounding: built form abstracted — dense ordered storeys, plaster bands over an earth-toned ground, lime-white
surfaces, openings that look from one layer into the system, quiet between dense layers. No arch, no motif."""
from __future__ import annotations

from common import esc, bdi, paragraphs, reading_blocks, nav_flat, logo, mobile_rules, rv001_data, rv001_panel1_svg, rv001_index_panel_svg, rv001_tables, rv001_frame_lines

CUR = ' aria-current="page"'
NAME = "T3 · Strata"

TOKENS = """
:root,.root{--ground:#ECE8E0;--surface:#FFFFFF;--lime:#F7F5F0;--ink:#1A2230;--ink-2:#414B58;--mute:#5E6874;--rule:#D5D0C7;--band:#B9B1A3;--trail:#1F5C58;--edge:#8C6B1F;
--fs-body:17px;--lh-body:1.6;--fs-h1:40px;--lh-h1:1.12;--fs-h2:24px;--lh-h2:1.3;--fs-h3:19px;--fs-statement:21px;--lh-statement:1.45;--fs-small:14px;--lh-small:1.5;--fs-label:12px;--measure:64ch;--font:'IBM Plex Sans',sans-serif}
html[dir=rtl],[dir=rtl].root{--fs-body:18px;--lh-body:1.9;--fs-h1:38px;--lh-h1:1.35;--fs-h2:25px;--lh-h2:1.5;--fs-h3:20px;--fs-statement:22px;--lh-statement:1.7;--fs-small:15px;--lh-small:1.75;--fs-label:13.5px;--measure:34em;--font:'IBM Plex Sans Arabic',sans-serif}
"""

CSS = TOKENS + """
html,.root{background:var(--ground);color:var(--ink);font-family:var(--font);font-size:var(--fs-body);line-height:var(--lh-body)}
body{margin:0}
a{color:inherit;text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:.16em;text-decoration-color:var(--band)}
h1,h2,h3,h4,h5{margin:0;font-weight:600}
h1{font-size:var(--fs-h1);line-height:var(--lh-h1);max-width:24ch}[dir=ltr] h1{letter-spacing:-.012em}
h2{font-size:var(--fs-h2);line-height:var(--lh-h2)}h3{font-size:var(--fs-h3);line-height:1.4}
p{margin:0 0 .9em}p:last-child{margin-bottom:0}
.label{display:flex;gap:12px;align-items:baseline;font-size:var(--fs-label);font-weight:600;color:var(--trail);margin-bottom:16px}
[dir=ltr] .label{text-transform:uppercase;letter-spacing:.12em}
.label .n{color:var(--mute);font-weight:600;min-width:1.6em}
.statement{font-size:var(--fs-statement);line-height:var(--lh-statement);font-weight:500;max-width:var(--measure)}
.statement b{font-weight:600}
.text{max-width:var(--measure)}.text p{color:var(--ink-2)}
.small{font-size:var(--fs-small);line-height:var(--lh-small);color:var(--ink-2)}
.tbtn{background:none;border:0;padding:0;font:inherit;color:inherit;text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:.16em;text-decoration-color:var(--band);cursor:pointer}
.wrap{max-width:1280px;margin:0 auto;padding:0 32px}
.trustline{font-size:var(--fs-small);color:var(--mute)}
.trustline nav{display:flex;flex-wrap:wrap;gap:4px 22px;padding:9px 0}
.trustline a{text-decoration:none}
.bar{background:var(--surface);border-top:1px solid var(--rule);border-bottom:3px solid var(--band)}
.bar-in{display:grid;grid-template-columns:auto minmax(0,1fr) auto;align-items:end;gap:36px}
.brand{display:flex;align-items:center;gap:12px;text-decoration:none;padding:14px 0}
.brand img{width:48px;height:48px}
.brand-name{font-weight:600;font-size:14px;line-height:1.2;max-width:14ch}
.tabs{display:flex;flex-wrap:wrap;gap:0 26px;font-size:15px;font-weight:500;align-items:end}
.tabs a{text-decoration:none;padding:24px 0 14px;border-bottom:3px solid transparent;margin-bottom:-3px}
.tabs a[aria-current=page]{border-bottom-color:var(--ink)}
.tabs .group{display:inline-flex;gap:16px;align-items:end}
.tabs .glabel{color:var(--mute);font-size:12px;font-weight:600;padding-bottom:16px}
[dir=ltr] .tabs .glabel{text-transform:uppercase;letter-spacing:.08em}
.utilities{display:flex;gap:16px;align-items:center;font-size:14px;font-weight:500;padding:14px 0}
.utilities .tbtn,.utilities a{text-decoration:none}
.utilities .lang{border:1px solid var(--band);padding:6px 10px}
.utilities .menu{display:none}
.grid{max-width:1280px;margin:0 auto;padding:28px 32px 48px;display:grid;grid-template-columns:minmax(0,1fr) 280px;column-gap:36px;row-gap:14px;align-items:start}
.grid>*{min-width:0}
.stratum{grid-column:1;background:var(--surface);padding:30px 36px 36px;position:relative;border-top:3px solid var(--band)}
.stratum.quiet{background:var(--lime)}
.stratum.boundary{border-top:8px double var(--band)}
.stratum.head{padding-top:36px}
.crumb{font-size:var(--fs-small);color:var(--mute);margin-bottom:22px}
.crumb a{text-decoration:none}
.trail{grid-column:2;position:sticky;top:20px;display:flex;flex-direction:column;gap:14px;font-size:var(--fs-small);line-height:var(--lh-small)}
.tblock{background:var(--surface);border-top:3px solid var(--band);padding:16px 20px}
.tblock h3{font-size:var(--fs-label);color:var(--trail);margin:0 0 8px;font-weight:600}
[dir=ltr] .tblock h3{text-transform:uppercase;letter-spacing:.12em}
.tindex{list-style:none;margin:0;padding:0}
.tindex li{border-top:1px solid var(--rule)}
.tindex a{display:flex;gap:10px;padding:8px 0;text-decoration:none;color:var(--ink)}
.tindex .n{color:var(--mute);font-weight:600;min-width:1.4em}
.edges{list-style:none;margin:0;padding:0}
.edges li{border-top:1px solid var(--rule);padding:8px 0}
.edges li:first-child{border-top:0;padding-top:0}
.edges .e{display:block;font-size:12px;color:var(--mute);margin-bottom:2px}
.actions{display:flex;flex-wrap:wrap;gap:10px 26px;margin-top:22px;font-weight:600}
.actions a{text-decoration-thickness:2px}
.openings{display:grid;grid-template-columns:1fr 1fr;gap:1px;background:var(--rule);border:1px solid var(--rule);margin-top:8px}
.opening{background:var(--lime);padding:22px 24px 24px;display:flex;flex-direction:column;gap:8px}
.opening .n{font-size:var(--fs-small);font-weight:600;color:var(--mute)}
.opening .q{font-size:var(--fs-statement);line-height:var(--lh-statement);font-weight:500}
.opening .q a{text-decoration-color:var(--edge)}
.openings.single{grid-template-columns:1fr}
.reclist{list-style:none;margin:16px 0 0;padding:0}
.reclist li{display:grid;grid-template-columns:minmax(0,1fr) minmax(200px,.6fr);gap:20px;padding:14px 0;border-top:1px solid var(--rule)}
.reclist .t{font-size:var(--fs-h3);line-height:1.4;font-weight:500}
.dl{margin:0;display:grid;grid-template-columns:minmax(200px,.35fr) minmax(0,1fr);gap:14px 28px}
.dl dt{font-size:var(--fs-small);font-weight:600;color:var(--mute);padding-top:3px}
.dl dd{margin:0;max-width:var(--measure);color:var(--ink-2)}
.src{display:grid;gap:8px;padding:16px 0;border-top:1px solid var(--rule)}
.src:first-child{border-top:0;padding-top:0}
.src-head{display:flex;flex-direction:column;gap:3px}
.src .kind,.src .ref{font-size:var(--fs-small);color:var(--mute);font-weight:500}
.src-actions{display:flex;flex-wrap:wrap;gap:8px 22px;font-size:15px;font-weight:500}
.src .rights{font-size:var(--fs-small);color:var(--mute);margin:0}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:8px}
.chip{display:inline-block;border:1px solid var(--band);padding:3px 8px;font-size:var(--fs-small);text-decoration:none;background:var(--surface)}
details.more summary{cursor:pointer;list-style:none;font-weight:600;font-size:var(--fs-small);color:var(--trail)}
details.more summary::-webkit-details-marker{display:none}
details.more summary::before{content:"+ ";}
details.more[open] summary::before{content:"− "}
details.more .dl{margin-top:18px}
.pull{margin:24px 0;padding:0 0 0 22px;border-inline-start:3px solid var(--band);font-size:var(--fs-statement);line-height:var(--lh-statement);font-weight:500}
[dir=rtl] .pull{padding:0 22px 0 0}
.rlist{padding-inline-start:1.2em}
.essay section{padding:8px 0 28px}
.essay section+section{border-top:1px solid var(--rule);padding-top:26px}
.inset{background:var(--lime);border-top:3px solid var(--band);padding:22px 26px 20px;margin:24px 0 8px}
.inset h4{font-size:var(--fs-h3);margin-bottom:4px}
.inset .cap{font-size:var(--fs-small);line-height:var(--lh-small);color:var(--ink-2);margin:0 0 6px;max-width:70ch}
.panels{display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.5fr);gap:26px;align-items:start;margin:16px 0;padding-top:14px;border-top:1px solid var(--rule)}
.panel h5{margin:0 0 6px;font-size:var(--fs-small);font-weight:600;color:var(--ink-2)}
.between{font-size:var(--fs-small);font-weight:600;color:var(--trail);margin:0 0 8px;padding-bottom:6px;border-bottom:3px double var(--band)}
.lanes{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.legend{display:flex;flex-wrap:wrap;gap:8px 20px;font-size:var(--fs-small);color:var(--ink-2);margin-top:6px}
.legend .k{display:inline-flex;align-items:center;gap:7px}
.legend .sw{display:inline-block;width:11px;height:11px;background:var(--ink)}.legend .sw.c{border-radius:50%}.legend .sw.s{background:var(--lime);border:2px solid var(--ink)}
.inset .foot{display:flex;flex-direction:column;gap:6px;font-size:var(--fs-small);line-height:var(--lh-small);color:var(--ink-2);margin-top:12px}
.inset .foot .bnd{color:var(--ink);font-weight:500}
svg.rv1,svg.rv2{max-width:100%;height:auto;font-family:var(--font)}
.axis{stroke:var(--ink);stroke-width:1}.grid{stroke:var(--rule);stroke-width:1}.tick{stroke:var(--ink);stroke-width:1}
.lbl{font-size:11px;fill:var(--mute);font-weight:500}.lbl.origin{fill:var(--ink)}.unit{font-size:11px;fill:var(--ink-2);font-weight:600}
.val{font-size:12.5px;fill:var(--ink);font-weight:600}.val.small{font-size:11px}
.mark.a{fill:var(--ink)}.mark.b{fill:var(--lime);stroke:var(--ink);stroke-width:2}
.path{stroke:var(--ink);stroke-width:1.5}
.rvtab{border-collapse:collapse;width:100%;font-size:var(--fs-small);line-height:var(--lh-small);margin-top:10px;background:var(--surface)}
.rvtab caption{text-align:start;font-weight:600;color:var(--ink-2);padding:8px 0}
.rvtab th,.rvtab td{text-align:start;padding:7px 10px;border-top:1px solid var(--rule);vertical-align:top}
.rvtab thead th{border-top:1px solid var(--ink);font-weight:600}
.rvtab .state{color:var(--mute)}.rvtab .marker{font-weight:600}
.steps{list-style:none;margin:0;padding:0;counter-reset:s}
.steps>li{display:grid;grid-template-columns:36px minmax(0,1fr);gap:14px;padding:16px 0;border-top:1px solid var(--rule)}
.steps>li:first-child{border-top:0;padding-top:0}
.steps>li::before{counter-increment:s;content:counter(s);font-weight:600;color:var(--mute);padding-top:4px}
.steps .prop{font-size:var(--fs-h3);line-height:1.4;font-weight:500}
.steps .line{font-size:var(--fs-small);line-height:var(--lh-small);color:var(--ink-2);margin-top:6px}
.foot{background:var(--surface);border-top:3px solid var(--band);margin-top:12px}
.foot-in{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,2fr);gap:40px;padding:36px 0}
.foot img{width:48px;height:48px;margin-bottom:12px}
.foot p{font-size:var(--fs-small);color:var(--ink-2);max-width:36ch}
.foot nav{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px;font-size:var(--fs-small)}
.foot nav div{display:flex;flex-direction:column;gap:6px}
.foot nav strong{font-size:var(--fs-label);color:var(--trail)}
[dir=ltr] .foot nav strong{text-transform:uppercase;letter-spacing:.1em}
.foot nav a{text-decoration:none}
.fine{border-top:1px solid var(--rule);padding:14px 32px;font-size:var(--fs-small);color:var(--mute)}
""" + mobile_rules("""
:root,.root{--fs-h1:31px;--fs-h2:22px;--fs-statement:19px}
[dir=rtl].root{--fs-h1:30px;--fs-h2:23px;--fs-statement:20px}
.wrap{padding:0 14px}
.trustline{display:none}
.bar-in{grid-template-columns:auto minmax(0,1fr);gap:10px;align-items:center}
.brand{padding:10px 0}.brand img{width:40px;height:40px}.brand-name{font-size:12px}
.tabs{display:none}
.utilities{justify-self:end;gap:10px;font-size:13px;padding:10px 0}
.utilities .menu{display:inline-block}
.utilities .cite,.utilities .report{display:none}
.grid{display:flex;flex-direction:column;align-items:stretch;padding:14px 14px 36px;gap:12px}
.stratum{padding:22px 18px 26px}
.stratum.head{order:0}.stratum{order:2}
.trail{order:1;position:static;grid-column:auto;grid-row:auto!important}
.trail .tblock.edges-block{display:none}
.tindex{display:flex;flex-wrap:wrap;gap:6px}
.tindex li{border:0}
.tindex a{border:1px solid var(--band);padding:6px 10px;background:var(--surface)}
.foot-trail{order:3;display:block}
.openings{grid-template-columns:1fr}
.reclist li{grid-template-columns:1fr;gap:6px}
.dl{grid-template-columns:1fr;gap:4px 0}
.dl dt{padding-top:12px}
.panels{grid-template-columns:minmax(0,1fr)}
.lanes{grid-template-columns:minmax(0,1fr)}
.foot-in{grid-template-columns:1fr;gap:24px;padding:28px 0}
.foot nav{grid-template-columns:1fr}
.fine{padding:14px}
h1{max-width:none}
""") + ".foot-trail{display:none}"


def label(t, n=None):
    return f'<div class="label">{f"<span class=n>{n:02d}</span>" if n is not None else ""}<span>{esc(t)}</span></div>'


def header(shell):
    L = shell["labels"]
    trust = "".join(f'<a href="{t["href"]}">{esc(t["label"])}</a>' for t in shell["trust"])
    nav = []
    for it in nav_flat(shell):
        if "group" in it:
            kids = "".join(f'<a href="{k["href"]}"{CUR if k["active"] else ""}>{esc(k["label"])}</a>' for k in it["children"])
            nav.append(f'<span class="group"><span class="glabel">{esc(it["group"])}</span>{kids}</span>')
        else:
            nav.append(f'<a href="{it["href"]}"{CUR if it["active"] else ""}>{esc(it["label"])}</a>')
    other = shell["other_lang"]
    return (f'<div class="trustline"><div class="wrap"><nav aria-label="{esc(L["trust_nav"])}">{trust}</nav></div></div>'
            f'<header class="bar"><div class="wrap bar-in"><a class="brand" href="{shell["home_href"]}">{logo(48)}<span class="brand-name">{esc(shell["product"])}</span></a><nav class="tabs" aria-label="{esc(L["primary_nav"])}">{"".join(nav)}</nav>'
            f'<div class="utilities"><button type="button" class="tbtn">{esc(L["search"])}</button><button type="button" class="tbtn cite">{esc(L["cite"])}</button><a class="report" href="{shell["contact_href"]}">{esc(L["report"])}</a>'
            f'<button type="button" class="tbtn lang" lang="{other}" dir="{"ltr" if other == "en" else "rtl"}">{esc(L["lang_switch_name"])}</button><button type="button" class="tbtn menu">{esc(L["menu"])}</button></div></div></header><main>')


def footer(shell):
    L = shell["labels"]
    groups = "".join(f'<div><strong>{esc(g["label"])}</strong>' + "".join(f'<a href="{l["href"]}">{esc(l["label"])}</a>' for l in g["links"]) + "</div>" for g in shell["footer"])
    return (f'</main><footer class="foot"><div class="wrap foot-in"><div>{logo(48)}<p>{esc(L["footer_strapline"])}</p></div><nav aria-label="{esc(L["footer_nav"])}">{groups}</nav></div>'
            f'<div class="fine">© 2026 CauseWay · {esc(L["footer_rights"])} · {esc(shell["edition"])}</div></footer>')


def crumb(bc, shell):
    if not bc:
        return ""
    cur = bdi(bc["current"]) if bc["mode"] == "STABLE_OBJECT_ID" else esc(bc["current"])
    return f'<nav class="crumb" aria-label="{esc(shell["labels"]["breadcrumb"])}"><a href="{bc["parent_href"]}">{esc(bc["parent_label"])}</a> / <span aria-current="page">{cur}</span></nav>'


def source_card(s):
    L = s["labels"]
    ref = f'<span class="ref">{esc(s["reference_label"])} {bdi(s["id"])}</span>'
    head_ = f'<strong dir="auto">{esc(s["title"])}</strong><span class="kind" dir="auto">{esc(s["kind_line"])}</span>{ref}' if s["display_ready"] and s["title"] else f'<strong>{esc(s["untitled_label"])}</strong>{ref}'
    rights = f'<p class="rights">{esc(s["rights_note"])}</p>' if s["rights_note"] else ""
    return (f'<article class="src"><div class="src-head">{head_}</div><div class="src-actions"><a href="{s["data_href"]}">{esc(L["open_source_record"])}</a><a href="{esc(s["url"])}">{esc(L["open_original"])}</a><button type="button" class="tbtn">{esc(L["copy_reference"])}</button></div>{rights}</article>')


def stratum(n, lab, inner, cls="", id_=""):
    i = f' id="{id_}"' if id_ else ""
    return f'<section class="stratum {cls}"{i}>{label(lab, n) if lab else ""}{inner}</section>'


def trail(index, edges, span=8):
    idx = "".join(f'<li><a href="#{a}"><span class="n">{i+1:02d}</span><span>{esc(t)}</span></a></li>' for i, (a, t) in enumerate(index))
    ed = "".join(f'<div class="tblock edges-block"><h3>{esc(h)}</h3><ul class="edges">' + "".join(f'<li>{x}</li>' for x in items) + "</ul></div>" for h, items in edges if items)
    return f'<aside class="trail" style="grid-row:1 / span {span}"><div class="tblock"><ul class="tindex">{idx}</ul></div>{ed}</aside>'


def foot_trail(edges):
    ed = "".join(f'<div class="tblock"><h3>{esc(h)}</h3><ul class="edges">' + "".join(f'<li>{x}</li>' for x in items) + "</ul></div>" for h, items in edges if items)
    return f'<div class="foot-trail">{ed}</div>'


def figure(v, lang):
    d = rv001_data(v); f = rv001_frame_lines(v)
    return (f'<figure class="inset"><h4>{esc(f["title"])}</h4><p class="cap">{esc(v["question"])}</p><p class="cap">{esc(f["scope"])}</p>'
            f'<div class="panels"><div class="panel"><h5>2024 · {esc(d["unit_usd"])}</h5>{rv001_panel1_svg(d, lang, w=380, h=280)}<div class="legend"><span class="k"><span class="sw c"></span>{esc(d["label_ar2024"])}</span><span class="k"><span class="sw s"></span>{esc(d["label_ar2025"])}</span></div><p class="cap" style="margin-top:8px"><b>{esc(f["same_year"])}</b></p></div>'
            f'<div class="panel"><p class="between">{esc(f["not_comparable"])}</p><h5>{esc(d["unit_index"])} · {esc(v["labels"]["derived"])}</h5><div class="lanes"><div><h5>{esc(d["label_cby"])}</h5>{rv001_index_panel_svg(d["cby_index"], lang, w=260, h=200, mark="circle")}</div><div><h5>{esc(d["label_imf"])}</h5>{rv001_index_panel_svg(d["imf_index"], lang, w=260, h=200, mark="square")}</div></div><p class="cap" style="margin-top:8px">{esc(f["note"])}</p></div></div>'
            f'<div class="foot"><p class="bnd"><b>{esc(f["boundary_label"])}</b> {esc(f["boundary"])}</p><p>{esc(f["credit"])}</p><p>{esc(f["full_record_label"])} <a href="{f["full_record"]}">{esc(f["full_record"])}</a></p></div>'
            f'<div class="table-wrap">{rv001_tables(d, v, lang)}</div><figcaption class="sr-only">{esc(v["alt_text"])}</figcaption></figure>')


def home(page, shell):
    L = page["labels"]; S = {s["order"]: s for s in page["sections"]}
    st = []
    st.append(stratum(None, "", f'{label(L["product"])}<h1>{esc(page["title"])}</h1><div class="statement" style="margin-top:22px">{paragraphs(S[1]["paragraphs"])}</div><div class="actions"><a href="{page["hrefs"]["explore"]}">{esc(L["start"])}</a><a href="{page["hrefs"]["evidence"]}">{esc(L["verify"])}</a></div>', "head", "s0"))
    ops = "".join(f'<div class="opening"><span class="n">{i+1:02d}</span><div class="q"><a href="{q["href"]}">{esc(q["question"])}</a></div><div class="small">{esc(q["gets"])}</div></div>' for i, q in enumerate(page["starting_questions"]))
    st.append(stratum(1, L["flow"], f'<h2>{esc(S[9]["heading"])}</h2><p class="small" style="margin-top:6px">{esc(S[9]["body"])}</p><div class="openings">{ops}</div><p class="small" style="margin-top:14px"><a href="{page["hrefs"]["explore"]}">{esc(L["view_all"])}</a></p>', "", "s1"))
    recs = "".join(f'<li><div><div class="t"><a href="{r["href"]}">{esc(r["title"])}</a></div><div class="small">{esc(r["universe"])}</div></div><div class="small">' + (f'<b>{esc(L["period"])}</b><br>{esc(r["period"])}' if r["period"] else "") + "</div></li>" for r in page["records"])
    st.append(stratum(2, S[3]["role"] or "", f'<h2>{esc(S[3]["heading"])}</h2><div class="statement" style="margin-top:14px">{paragraphs(S[3]["paragraphs"])}</div><p class="small" style="margin-top:22px"><b>{esc(L["records_heading"])}</b></p><ul class="reclist">{recs}</ul>', "", "s2"))
    st.append(stratum(3, S[4]["role"] or "", f'<h2>{esc(S[4]["heading"])}</h2><div class="statement" style="margin-top:12px">{paragraphs(S[4]["paragraphs"])}</div>', "boundary", "s3"))
    st.append(stratum(4, S[5]["role"] or "", f'<h2>{esc(S[5]["heading"])}</h2><div class="text" style="margin-top:12px">{paragraphs(S[5]["paragraphs"])}</div>', "", "s4"))
    v = page["system_visual"]
    st.append(stratum(5, S[6]["role"] or "", f'<h2 id="system">{esc(S[6]["heading"])}</h2><div class="text" style="margin-top:12px">{paragraphs(S[6]["paragraphs"])}</div>'
              f'<div class="inset"><p class="cap"><b>{esc(L["visual_eyebrow"])}</b></p><h4>{esc(v["title"])}</h4><p class="cap">{esc(v["question"])}</p><div class="text"><p>{esc(v["alt_text"])}</p></div><p class="small" style="margin-top:10px"><a href="{v["canonical_href"]}">{esc(L["open_record"])}</a></p></div>', "", "s5"))
    st.append(stratum(6, S[7]["role"] or "", f'<h2>{esc(S[7]["heading"])}</h2><div class="text" style="margin-top:12px">{paragraphs(S[7]["paragraphs"])}</div>', "quiet", "s6"))
    st.append(stratum(7, S[8]["role"] or "", f'<h2>{esc(S[8]["heading"])}</h2><div class="text" style="margin-top:12px">{paragraphs(S[8]["paragraphs"])}</div>', "", "s7"))
    f = page["featured"]
    st.append(stratum(8, L["featured"], f'<h2><a href="{f["href"]}">{esc(f["title"])}</a></h2><p class="statement" style="margin-top:12px">{esc(f["thesis"])}</p><p class="small" style="margin-top:12px"><b>{esc(L["evidence_period"])}</b> · {esc(f["evidence_period"])}</p><div class="actions"><a href="{f["href"]}">{esc(L["open_reading"])}</a><a href="{page["hrefs"]["readings"]}">{esc(L["all_readings"])}</a></div>', "", "s8"))
    index = [("s1", S[9]["heading"]), ("s2", S[3]["heading"]), ("s3", S[4]["heading"]), ("s4", S[5]["heading"]), ("s5", S[6]["heading"]), ("s6", S[7]["heading"]), ("s7", S[8]["heading"]), ("s8", L["featured"])]
    edges = [(L["records_heading"], [f'<a href="{r["href"]}">{esc(r["title"])}</a>' for r in page["records"]]),
             (L["flow"], [f'<span class="e">{esc(d)}</span><a href="{h}">{esc(t)}</a>' for h, t, d in ((page["hrefs"]["readings"], L["readings_nav"], L["cta_readings"]), (page["hrefs"]["measurement"], L["measurement_nav"], L["cta_measurement"]), (page["hrefs"]["data"], L["data_nav"], L["cta_data"]))])]
    return header(shell) + f'<div class="grid">{"".join(st)}{trail(index, edges, len(st))}{foot_trail(edges)}</div>' + footer(shell)


def record(page, shell):
    L = page["labels"]
    summary = esc(page["summary"]).replace("8.55%", "<b>8.55%</b>").replace("+11%", "<b>+11%</b>")
    st = []
    st.append(stratum(None, "", f'{crumb(page["breadcrumb"], shell)}{label(L["family"])}<h1>{esc(page["title"])}</h1><p class="small" style="margin-top:14px"><b>{esc(L["reference"])}</b> {bdi(page["id"])} · <b>{esc(L["period"])}</b> {esc(page["period"])}</p>', "head", "s0"))
    st.append(stratum(1, L["establishes"], f'<div class="statement"><p>{summary}</p></div>', "", "s1"))
    dl = "".join(f'<dt>{esc(L[lab])}</dt><dd>{esc(page[k])}</dd>' for k, lab in (("definition", "measures"), ("universe", "applies"), ("period", "period"), ("currentness", "currentness")))
    st.append(stratum(2, L["scope"] if "scope" in L else L["measures"], f'<dl class="dl">{dl}</dl>', "", "s2"))
    st.append(stratum(3, L["does_not_establish"], f'<div class="statement"><p>{esc(page["does_not_establish"])}</p></div>', "boundary", "s3"))
    chips = "".join(f'<a class="chip" href="/{shell["lang"]}/data/?source={esc(sid)}#source-{esc(sid)}">{bdi(sid)}</a>' for sid in page["trace_ids"])
    st.append(stratum(4, L["source"], f'<p class="small">{esc(L["source_intro"])}</p><div style="margin-top:14px">{"".join(source_card(s) for s in page["sources"])}</div><div style="margin-top:22px;padding-top:16px;border-top:1px solid var(--rule)"><p class="small"><b>{esc(L["trace"])}</b> · {esc(L["trace_intro"])}</p><div class="chips"><span class="chip">{bdi(page["id"])}</span>{chips}</div></div>', "", "s4"))
    more = "".join(f'<dt>{esc(L[k])}</dt><dd>{esc(page[k])}</dd>' for k in ("method", "change_trigger", "verification") if page[k])
    more += f'<dt>{esc(L["reading_guidance"])}</dt><dd>{paragraphs(page["reading_guidance"]["paragraphs"])}</dd>'
    st.append(stratum(5, L["more"], f'<details class="more"><summary>{esc(L["more_intro"])}</summary><dl class="dl">{more}</dl></details>', "quiet", "s5"))
    st.append(stratum(None, "", f'<p class="small"><b>{esc(L["reference"])}</b> {bdi(page["id"])}</p><div class="actions" style="margin-top:8px"><button type="button" class="tbtn">{esc(L["cite"])}</button><a href="{page["hrefs"]["rights"]}">{esc(L["reuse"])}</a><a href="{page["hrefs"]["corrections"]}">{esc(L["history"])}</a><a href="{page["hrefs"]["report"]}">{esc(L["report"])}</a></div><p class="small" style="margin-top:14px">{esc(L["reuse_note"])}</p>', "quiet", "s6"))
    index = [("s1", L["establishes"]), ("s2", L["scope"] if "scope" in L else L["measures"]), ("s3", L["does_not_establish"]), ("s4", L["source"]), ("s5", L["more"])]
    edges = [(L["used_in"], [f'<a href="{x["href"]}">{esc(x["title"])}</a>' for x in page["used_in_readings"]]),
             (L["related"], [f'<a href="{x["href"]}">{esc(x["label"])}</a>' for x in page["routes_back"]] + [f'<a href="{page["hrefs"]["evidence"]}">{esc(L["evidence_hub"])}</a>', f'<a href="{page["hrefs"]["data"]}">{esc(L["data"])}</a>', f'<a href="{page["hrefs"]["methodology"]}">{esc(L["methodology"])}</a>'])]
    return header(shell) + f'<div class="grid">{"".join(st)}{trail(index, edges, len(st))}{foot_trail(edges)}</div>' + footer(shell)


def reading(page, shell):
    L = page["labels"]; lang = shell["lang"]
    st = []
    st.append(stratum(None, "", f'{crumb(page["breadcrumb"], shell)}{label(L["eyebrow"])}<h1>{esc(page["title"])}</h1><div class="statement" style="margin-top:22px"><p>{esc(page["thesis"])}</p></div><p class="small" style="margin-top:16px"><b>{esc(L["evidence_period"])}</b> · {esc(page["evidence_period"])} · <b>{esc(L["last_reviewed"])}</b> · {esc(page["last_reviewed"])}</p>', "head", "s0"))
    st.append(stratum(1, L["do_not_infer"], f'<div class="statement"><p>{esc(page["prohibited_inference"])}</p></div>', "boundary", "s1"))
    essay = []
    for i, s in enumerate(page["sections"]):
        head_ = f'<h2 id="s-{esc(s["section_id"])}">{esc(s["heading"])}</h2>' if s["heading"] else ""
        essay.append(f'<section>{head_}<div class="{"statement" if i == 0 else "text"}" style="margin-top:12px">{reading_blocks(s["blocks"])}</div>{"".join(figure(v, lang) for v in page["visuals"]) if i == 0 else ""}</section>')
    st.append(stratum(2, page["labels"]["eyebrow"], f'<div class="essay">{"".join(essay)}</div>', "", "s2"))
    steps = []
    for x in page["trace"]:
        srcs = " · ".join(f'<a href="{s["data_href"]}">{esc(s["title"] or s["id"])}</a>' for s in x["sources"])
        if x["no_locator_note"]:
            srcs += (" · " if srcs else "") + esc(x["no_locator_note"])
        steps.append(f'<li><div><div class="prop"><a href="{x["href"]}">{esc(x["proposition"])}</a></div><div class="line">{esc(L["reference"])} {bdi(x["id"])}{" · " + srcs if srcs else ""}</div></div></li>')
    st.append(stratum(3, L["trace"], f'<p class="small">{esc(L["trace_intro"])}</p><p class="small"><b>{esc(page["trace_status"])}</b></p><ol class="steps" style="margin-top:16px">{"".join(steps)}</ol><div class="actions"><a href="{page["compare_href"]}">{esc(L["compare"])}</a></div>', "", "s3"))
    st.append(stratum(4, L["sources"], "".join(source_card(s) for s in page["sources"]), "", "s4"))
    rel = "".join(f'<li><div><div class="prop"><a href="{x["href"]}">{esc(x["title"])}</a></div><div class="line">{esc(x["thesis"])}</div></div></li>' for x in page["related"])
    st.append(stratum(5, L["related"], f'<ol class="steps">{rel}</ol><p class="small" style="margin-top:14px"><a href="{L["readings_index_href"]}">{esc(L["all"])}</a></p>', "quiet", "s5"))
    index = [(f's-{s["section_id"]}', s["heading"]) for s in page["sections"] if s["heading"]] + [("s3", L["trace"]), ("s4", L["sources"]), ("s5", L["related"])]
    edges = [(L["trace"], [f'<a href="{x["href"]}">{esc(x["proposition"])}</a>' for x in page["trace"]]),
             (L["return"], [f'<a href="{b["href"]}">{esc(b["label"])}</a>' for b in page["return_to"]])]
    return header(shell) + f'<div class="grid">{"".join(st)}{trail(index, edges, len(st))}{foot_trail(edges)}</div>' + footer(shell)


COMPOSE = {"home": home, "record": record, "reading": reading}
