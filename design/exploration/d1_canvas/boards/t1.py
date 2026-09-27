# -*- coding: utf-8 -*-
"""T1 · REGISTER — Design proposition (canvas). The evidence record as the organising object; the apparatus visible.
Grounding: the manuscript page — text block (matn) and marginal commentary (ḥāshiya). Paper white, ink, hairlines,
rubricated labels in a dark ochre (labels only, never meaning). Every entry = margin · statement · apparatus."""
from __future__ import annotations

from common import esc, bdi, paragraphs, reading_blocks, nav_flat, logo, mobile_rules, rv001_data, rv001_panel1_svg, rv001_index_panel_svg, rv001_tables, rv001_frame_lines

CUR = ' aria-current="page"'
NAME = "T1 · Register"

TOKENS = """
:root,.root{--paper:#FFFFFF;--ink:#14202B;--ink-2:#3C4A56;--mute:#5F6B76;--rule:#D3DAE0;--rule-2:#A7B2BB;--ochre:#7E5C1C;--ochre-rule:#C9A24A;
--fs-body:17px;--lh-body:1.55;--fs-statement:22px;--lh-statement:1.4;--fs-h1:42px;--lh-h1:1.1;--fs-h2:25px;--lh-h2:1.25;--fs-h3:19px;--fs-margin:13.5px;--lh-margin:1.45;--fs-rubric:12px;--measure:66ch;--font:'IBM Plex Sans',sans-serif}
html[dir=rtl],[dir=rtl].root{--fs-body:18px;--lh-body:1.9;--fs-statement:23px;--lh-statement:1.65;--fs-h1:40px;--lh-h1:1.35;--fs-h2:26px;--lh-h2:1.5;--fs-h3:20px;--fs-margin:14.5px;--lh-margin:1.7;--fs-rubric:13.5px;--measure:36em;--font:'IBM Plex Sans Arabic',sans-serif}
"""

CSS = TOKENS + """
html,.root{background:var(--paper);color:var(--ink);font-family:var(--font);font-size:var(--fs-body);line-height:var(--lh-body);font-variant-numeric:tabular-nums}
body{margin:0}
a{color:inherit;text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:.16em;text-decoration-color:var(--rule-2)}
a:hover{text-decoration-color:var(--ink)}
.wrap{max-width:1280px;margin:0 auto;padding:0 32px}
h1,h2,h3,h4,h5{margin:0;font-weight:600;letter-spacing:0}
h1{font-size:var(--fs-h1);line-height:var(--lh-h1);max-width:22ch}
[dir=ltr] h1{letter-spacing:-.012em}
h2{font-size:var(--fs-h2);line-height:var(--lh-h2)}
h3{font-size:var(--fs-h3);line-height:1.35}
p{margin:0 0 .85em}p:last-child{margin-bottom:0}
.rubric{display:block;font-size:var(--fs-rubric);line-height:1.4;font-weight:600;color:var(--ochre);margin:0 0 6px}
[dir=ltr] .rubric{text-transform:uppercase;letter-spacing:.11em}
.mnote{font-size:var(--fs-margin);line-height:var(--lh-margin);color:var(--mute);font-weight:500;margin:0}
.mnote b{color:var(--ink-2);font-weight:600}
.mnote+.mnote{margin-top:10px}
.statement{font-size:var(--fs-statement);line-height:var(--lh-statement);font-weight:500;max-width:var(--measure)}
.statement b{font-weight:600}
.lead{font-size:19.5px;line-height:1.55;font-weight:400;max-width:var(--measure)}
[dir=rtl] .lead{font-size:20px;line-height:1.85}
.text{max-width:var(--measure)}.text p{color:var(--ink-2)}
.tbtn{background:none;border:0;padding:0;font:inherit;color:inherit;text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:.16em;text-decoration-color:var(--rule-2);cursor:pointer}
.trustline{border-bottom:1px solid var(--rule)}
.trustline nav{display:flex;flex-wrap:wrap;gap:4px 22px;padding:9px 0;font-size:var(--fs-margin);font-weight:500;color:var(--mute)}
.trustline a{text-decoration:none;padding:4px 0}
.mast{border-bottom:1px solid var(--ink)}
.mast-in{display:grid;grid-template-columns:auto minmax(0,1fr) auto;align-items:center;gap:32px;padding:18px 0}
.brand{display:flex;align-items:center;gap:14px;text-decoration:none}
.brand img{width:64px;height:64px}
.brand-name{font-weight:600;font-size:15px;line-height:1.2;max-width:14ch}
.pnav{display:flex;flex-wrap:wrap;align-items:baseline;gap:6px 26px;font-size:15.5px;font-weight:500}
.pnav a{text-decoration:none;padding:6px 0;border-bottom:2px solid transparent}
.pnav a[aria-current=page]{border-bottom-color:var(--ink)}
.pnav .group{display:inline-flex;gap:14px;align-items:baseline}
.pnav .glabel{color:var(--mute);font-size:13px;font-weight:600}
[dir=ltr] .pnav .glabel{text-transform:uppercase;letter-spacing:.08em}
.utilities{display:flex;gap:18px;align-items:center;font-size:14.5px;font-weight:500}
.utilities .tbtn,.utilities a{text-decoration:none}
.utilities .lang{border:1px solid var(--rule-2);padding:6px 10px}
.utilities .menu{display:none}
.crumb{font-size:var(--fs-margin);font-weight:500;color:var(--mute);padding:18px 0 0}
.crumb a{text-decoration:none}
.entry{display:grid;grid-template-columns:200px minmax(0,1fr) 220px;column-gap:44px;padding:36px 0;border-top:1px solid var(--rule)}
.entry.major{border-top:3px solid var(--ink);padding-top:40px}
.entry.boundary{border-top:3px double var(--ink)}
.entry.first{border-top:0}
.entry.tail{border-top:1px solid var(--ink);border-bottom:3px solid var(--ink);margin-bottom:64px}
.entry.compact{padding:22px 0}
.m{display:flex;flex-direction:column;gap:12px}
.a{display:flex;flex-direction:column;gap:14px;font-size:var(--fs-margin);line-height:var(--lh-margin);color:var(--ink-2)}
.a p{margin:0}
.sub{display:grid;grid-template-columns:200px minmax(0,1fr) 220px;column-gap:44px;padding:18px 0;border-top:1px solid var(--rule)}
.subs{margin-top:20px;border-top:1px solid var(--rule-2)}
.entry>.subs{grid-column:1 / -1;margin-top:24px}
.sub{grid-column:1 / -1}
.subs .sub:first-child{border-top:0}
.num{font-size:var(--fs-margin);font-weight:600;color:var(--mute);letter-spacing:.06em}
.q{font-size:var(--fs-statement);line-height:var(--lh-statement);font-weight:500}
.q a{text-decoration-color:var(--ochre-rule)}
.gets{font-size:var(--fs-margin);line-height:var(--lh-margin);color:var(--ink-2)}
.actions{display:flex;flex-wrap:wrap;gap:12px 28px;margin-top:22px;font-weight:600}
.actions a{text-decoration-color:var(--ochre-rule);text-decoration-thickness:2px}
.mlist{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:12px}
.mlist li{border-top:1px solid var(--rule);padding-top:12px}.mlist li:first-child{border-top:0;padding-top:0}
.apparatus{display:flex;flex-direction:column;gap:18px}
.fig{display:flex;flex-direction:column;gap:4px}
.fig .v{font-size:30px;line-height:1.1;font-weight:600;color:var(--ink)}
.fig .state{font-size:var(--fs-margin);color:var(--ink-2);font-weight:500}
.inline-list{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:8px 18px}
.chip{display:inline-block;border:1px solid var(--rule-2);padding:3px 8px;font-size:var(--fs-margin);font-weight:500;text-decoration:none}
.src{display:grid;gap:8px;padding:16px 0;border-top:1px solid var(--rule)}
.src:first-child{border-top:0;padding-top:0}
.src-head{display:flex;flex-direction:column;gap:3px}
.src .kind,.src .ref{font-size:var(--fs-margin);color:var(--mute);font-weight:500}
.src-actions{display:flex;flex-wrap:wrap;gap:8px 22px;font-size:15px;font-weight:500}
.src .rights{font-size:var(--fs-margin);color:var(--mute);margin:0}
details.more{border-top:1px solid var(--rule)}
details.more summary{cursor:pointer;padding:22px 0;list-style:none;display:grid;grid-template-columns:200px minmax(0,1fr);column-gap:44px}
details.more summary::-webkit-details-marker{display:none}
details.more summary .rubric{margin:0}
details.more summary .hint{font-size:var(--fs-margin);color:var(--mute)}
details.more summary .hint::before{content:"+ ";font-weight:600;color:var(--ink)}
.pull{margin:22px 0;padding:0 0 0 22px;border-inline-start:3px solid var(--ochre-rule);font-size:var(--fs-statement);line-height:var(--lh-statement);font-weight:500}
[dir=rtl] .pull{padding:0 22px 0 0}
.rlist{padding-inline-start:1.2em}
.frame{grid-column:2 / span 2;border:1px solid var(--ink);padding:24px 28px 20px;margin:0}
.frame-head{display:flex;flex-direction:column;gap:6px;margin-bottom:18px}
.frame-scope{font-size:var(--fs-margin);color:var(--ink-2);font-weight:500;max-width:70ch;margin:0}
.panels{display:grid;grid-template-columns:minmax(0,1fr) auto minmax(0,1.4fr);gap:24px;align-items:start;padding:12px 0;border-top:1px solid var(--rule);border-bottom:1px solid var(--rule)}
.panel h4{margin:0 0 8px;font-size:var(--fs-margin);font-weight:600;color:var(--ink-2)}
.between{align-self:center;font-size:var(--fs-margin);font-weight:600;color:var(--ink-2);max-width:10em;text-align:center;border-inline-start:1px solid var(--rule);border-inline-end:1px solid var(--rule);padding:0 14px}
.lanes{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.lane h5{margin:0 0 4px;font-size:var(--fs-margin);font-weight:600;color:var(--ink)}
.legend{display:flex;flex-wrap:wrap;gap:8px 20px;font-size:var(--fs-margin);color:var(--ink-2);font-weight:500;margin-top:8px}
.legend .k{display:inline-flex;align-items:center;gap:7px}
.legend .sw{display:inline-block;width:11px;height:11px;background:var(--ink)}.legend .sw.c{border-radius:50%}.legend .sw.s{background:#fff;border:2px solid var(--ink)}
.frame-foot{display:flex;flex-direction:column;gap:8px;margin-top:16px;font-size:var(--fs-margin);line-height:var(--lh-margin);color:var(--ink-2)}
.frame-foot .bnd b{color:var(--ink)}
svg.rv1,svg.rv2{max-width:100%;height:auto;font-family:var(--font)}
.axis{stroke:var(--ink);stroke-width:1}.grid{stroke:var(--rule);stroke-width:1}.tick{stroke:var(--ink);stroke-width:1}
.lbl{font-size:11px;fill:var(--mute);font-weight:500}.lbl.origin{fill:var(--ink)}.unit{font-size:11px;fill:var(--ink-2);font-weight:600}
.val{font-size:12.5px;fill:var(--ink);font-weight:600}.val.small{font-size:11px}
.mark.a{fill:var(--ink)}.mark.b{fill:#fff;stroke:var(--ink);stroke-width:2}
.path{stroke:var(--ink);stroke-width:1.5}
.table-wrap{margin-top:16px}
.rvtab{border-collapse:collapse;width:100%;font-size:var(--fs-margin);line-height:var(--lh-margin);margin-top:10px}
.rvtab caption{text-align:start;font-weight:600;color:var(--ink-2);padding:8px 0}
.rvtab th,.rvtab td{text-align:start;padding:7px 10px;border-top:1px solid var(--rule);vertical-align:top}
.rvtab thead th{border-top:1px solid var(--ink);border-bottom:1px solid var(--rule-2);font-weight:600}
.rvtab .state{color:var(--mute);font-weight:500}.rvtab .marker{color:var(--ink);font-weight:600}
.path-list{list-style:none;margin:0;padding:0;counter-reset:step}
.path-list>li{display:grid;grid-template-columns:36px minmax(0,1fr);gap:16px;padding:16px 0;border-top:1px solid var(--rule)}
.path-list>li:first-child{border-top:0;padding-top:0}
.path-list>li::before{counter-increment:step;content:counter(step,decimal-leading-zero);font-size:var(--fs-margin);font-weight:600;color:var(--mute);padding-top:4px}
.step-head{font-size:var(--fs-statement);line-height:var(--lh-statement);font-weight:500}
.step-meta{font-size:var(--fs-margin);color:var(--mute);font-weight:500;margin-top:4px}
.step-src{list-style:none;margin:8px 0 0;padding:0;font-size:var(--fs-margin);display:flex;flex-wrap:wrap;gap:6px 18px}
.foot{border-top:3px solid var(--ink);margin-top:24px}
.foot-in{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,2fr);gap:44px;padding:40px 0}
.foot-id img{width:56px;height:56px;margin-bottom:14px}
.foot-id p{max-width:34ch;color:var(--ink-2)}
.foot-nav{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px}
.foot-nav div{display:flex;flex-direction:column;gap:8px;font-size:15px}
.foot-nav strong{font-size:var(--fs-rubric);color:var(--ochre);font-weight:600}
[dir=ltr] .foot-nav strong{text-transform:uppercase;letter-spacing:.1em}
.foot-nav a{text-decoration:none}
.fine{border-top:1px solid var(--rule);padding:16px 32px;font-size:var(--fs-margin);color:var(--mute)}
""" + mobile_rules("""
:root,.root{--fs-h1:32px;--fs-statement:19px;--fs-h2:22px}
[dir=rtl].root{--fs-h1:31px;--fs-statement:20px;--fs-h2:23px}
.wrap{padding:0 16px}
.trustline{display:none}
.mast-in{grid-template-columns:auto minmax(0,1fr);gap:12px;padding:12px 0}
.brand img{width:44px;height:44px}
.brand-name{font-size:13px}
.pnav{display:none}
.utilities{justify-self:end;gap:12px;font-size:13px}
.utilities .menu{display:inline-block}
.utilities .cite,.utilities .report{display:none}
.entry,.sub{grid-template-columns:minmax(0,1fr);column-gap:0;row-gap:12px;padding:26px 0}
.entry.major{padding-top:28px}
.m{gap:6px}.a{margin-top:8px;padding-top:12px;border-top:1px dashed var(--rule)}
details.more summary{grid-template-columns:1fr;gap:6px}
.frame{grid-column:auto;padding:18px 16px}
.panels{grid-template-columns:minmax(0,1fr);gap:16px}
.between{border:0;border-top:1px solid var(--rule);border-bottom:1px solid var(--rule);padding:8px 0;max-width:none;text-align:start}
.lanes{grid-template-columns:minmax(0,1fr)}
.foot-in{grid-template-columns:1fr;gap:28px;padding:28px 0}
.foot-nav{grid-template-columns:1fr;gap:20px}
.fine{padding:16px}
h1{max-width:none}
""")


def rubric(t):
    return f'<span class="rubric">{esc(t)}</span>'


def mnote(label, value):
    return f'<p class="mnote"><b>{esc(label)}</b><br>{value}</p>'


def entry(m, s, a="", cls="", after=""):
    return f'<section class="entry {cls}"><div class="m">{m}</div><div class="s">{s}</div><div class="a">{a}</div>{after}</section>'


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
            f'<header class="mast"><div class="wrap mast-in"><a class="brand" href="{shell["home_href"]}">{logo(64)}<span class="brand-name">{esc(shell["product"])}</span></a>'
            f'<nav class="pnav" aria-label="{esc(L["primary_nav"])}">{"".join(nav)}</nav>'
            f'<div class="utilities"><button type="button" class="tbtn">{esc(L["search"])}</button><button type="button" class="tbtn cite">{esc(L["cite"])}</button><a class="report" href="{shell["contact_href"]}">{esc(L["report"])}</a>'
            f'<button type="button" class="tbtn lang" lang="{other}" dir="{"ltr" if other == "en" else "rtl"}">{esc(L["lang_switch_name"])}</button><button type="button" class="tbtn menu">{esc(L["menu"])}</button></div></div></header><main><div class="wrap">')


def footer(shell):
    L = shell["labels"]
    groups = "".join(f'<div><strong>{esc(g["label"])}</strong>' + "".join(f'<a href="{l["href"]}">{esc(l["label"])}</a>' for l in g["links"]) + "</div>" for g in shell["footer"])
    return (f'</div></main><footer class="foot"><div class="wrap foot-in"><div class="foot-id">{logo(56)}<p>{esc(L["footer_strapline"])}</p></div>'
            f'<nav class="foot-nav" aria-label="{esc(L["footer_nav"])}">{groups}</nav></div><div class="fine">© 2026 CauseWay · {esc(L["footer_rights"])} · {esc(shell["edition"])}</div></footer>')


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
    return (f'<article class="src"><div class="src-head">{head_}</div><div class="src-actions"><a href="{s["data_href"]}">{esc(L["open_source_record"])}</a>'
            f'<a href="{esc(s["url"])}">{esc(L["open_original"])}</a><button type="button" class="tbtn">{esc(L["copy_reference"])}</button></div>{rights}</article>')


def figure(v, lang):
    d = rv001_data(v); f = rv001_frame_lines(v)
    return (f'<figure class="frame"><div class="frame-head">{rubric(v["labels"]["analytical_question"])}<h3>{esc(f["title"])}</h3><p class="frame-scope">{esc(v["question"])}</p><p class="frame-scope">{esc(f["scope"])}</p></div>'
            f'<div class="panels"><div class="panel"><h4>2024 · {esc(d["unit_usd"])}</h4>{rv001_panel1_svg(d, lang)}<div class="legend"><span class="k"><span class="sw c"></span>{esc(d["label_ar2024"])}</span><span class="k"><span class="sw s"></span>{esc(d["label_ar2025"])}</span></div><p class="mnote" style="margin-top:8px"><b>{esc(f["same_year"])}</b></p></div>'
            f'<div class="between">{esc(f["not_comparable"])}</div>'
            f'<div class="panel"><h4>{esc(d["unit_index"])} · {esc(v["labels"]["derived"])}</h4><div class="lanes"><div class="lane"><h5>{esc(d["label_cby"])}</h5>{rv001_index_panel_svg(d["cby_index"], lang, mark="circle")}</div><div class="lane"><h5>{esc(d["label_imf"])}</h5>{rv001_index_panel_svg(d["imf_index"], lang, mark="square")}</div></div><p class="mnote" style="margin-top:8px">{esc(f["note"])}</p></div></div>'
            f'<div class="frame-foot"><p class="bnd"><b>{esc(f["boundary_label"])}</b> {esc(f["boundary"])}</p><p>{esc(f["credit"])}</p><p>{esc(f["full_record_label"])} <a href="{f["full_record"]}">{esc(f["full_record"])}</a></p></div>'
            f'<div class="table-wrap">{rv001_tables(d, v, lang)}</div><figcaption class="sr-only">{esc(v["alt_text"])}</figcaption></figure>')


def home(page, shell):
    L = page["labels"]; S = {s["order"]: s for s in page["sections"]}
    out = [header(shell)]
    out.append(entry(rubric(L["product"]) + f'<p class="mnote"><b>{esc(L["flow"])}</b></p>',
                     f'<h1>{esc(page["title"])}</h1><div class="lead" style="margin-top:22px">{paragraphs(S[1]["paragraphs"])}</div><div class="actions"><a href="{page["hrefs"]["explore"]}">{esc(L["start"])}</a><a href="{page["hrefs"]["evidence"]}">{esc(L["verify"])}</a></div>',
                     f'<p>{esc(L["side"])}</p>', "major first"))
    qs = "".join(f'<div class="sub"><div class="m"><span class="num">{i+1:02d}</span></div><div class="s q"><a href="{q["href"]}">{esc(q["question"])}</a></div><div class="a gets">{esc(q["gets"])}</div></div>' for i, q in enumerate(page["starting_questions"]))
    out.append(entry(rubric(L["questions_eyebrow"]) + f'<p class="mnote">{esc(S[9]["body"])}</p>', f'<h2>{esc(S[9]["heading"])}</h2>', f'<p><a href="{page["hrefs"]["explore"]}">{esc(L["view_all"])}</a></p>', after=f'<div class="subs">{qs}</div>'))
    recs = "".join(f'<div class="sub"><div class="m">{mnote(L["period"], esc(r["period"])) if r["period"] else ""}</div><div class="s q"><a href="{r["href"]}">{esc(r["title"])}</a></div><div class="a gets">{esc(r["universe"])}</div></div>' for r in page["records"])
    out.append(entry(rubric(S[3]["role"] or ""), f'<h2>{esc(S[3]["heading"])}</h2><div class="statement" style="margin-top:14px">{paragraphs(S[3]["paragraphs"])}</div>', "", after=f'<div class="subs"><div class="sub"><div class="m">{rubric(L["records_heading"])}</div></div>{recs}</div>'))
    for o in (4, 5):
        out.append(entry(rubric(S[o]["role"] or ""), f'<h2>{esc(S[o]["heading"])}</h2><div class="text" style="margin-top:12px">{paragraphs(S[o]["paragraphs"])}</div>', "", "boundary" if o == 4 else ""))
    v = page["system_visual"]
    out.append(entry(rubric(S[6]["role"] or ""), f'<h2 id="system">{esc(S[6]["heading"])}</h2><div class="text" style="margin-top:12px">{paragraphs(S[6]["paragraphs"])}</div>', "",
               after=f'<div class="subs"><div class="sub"><div class="m">{rubric(L["visual_eyebrow"])}</div><div class="s"><h3>{esc(v["title"])}</h3><p class="mnote" style="margin:6px 0 10px">{esc(v["question"])}</p><div class="text"><p>{esc(v["alt_text"])}</p></div></div><div class="a"><p><a href="{v["canonical_href"]}">{esc(L["open_record"])}</a></p></div></div></div>'))
    for o in (7, 8):
        out.append(entry(rubric(S[o]["role"] or ""), f'<h2>{esc(S[o]["heading"])}</h2><div class="text" style="margin-top:12px">{paragraphs(S[o]["paragraphs"])}</div>'))
    f = page["featured"]
    out.append(entry(rubric(L["featured"]) + mnote(L["evidence_period"], esc(f["evidence_period"])), f'<h2><a href="{f["href"]}">{esc(f["title"])}</a></h2><div class="statement" style="margin-top:12px"><p>{esc(f["thesis"])}</p></div>',
                     f'<p><a href="{f["href"]}">{esc(L["open_reading"])}</a></p><p><a href="{page["hrefs"]["readings"]}">{esc(L["all_readings"])}</a></p>', "major"))
    ctas = "".join(f'<div class="sub"><div class="m q"><a href="{h}">{esc(t)}</a></div><div class="s gets">{esc(d)}</div><div class="a"></div></div>'
                   for h, t, d in ((page["hrefs"]["readings"], L["readings_nav"], L["cta_readings"]), (page["hrefs"]["measurement"], L["measurement_nav"], L["cta_measurement"]), (page["hrefs"]["data"], L["data_nav"], L["cta_data"])))
    out.append(f'<section class="entry tail" style="display:block"><div class="subs" style="border-top:0">{ctas}</div></section>')
    out.append(footer(shell))
    return "".join(out)


def record(page, shell):
    L = page["labels"]
    out = [header(shell), crumb(page["breadcrumb"], shell)]
    apparatus = (f'<div class="apparatus"><div class="fig"><span class="v">{bdi("8.55%")}</span><span class="state">{esc(L["state_derived"])}</span></div>'
                 f'<div class="fig"><span class="v">{bdi("+11%")}</span><span class="state">{esc(L["disagreement"])}</span></div></div>')
    out.append(entry(rubric(L["family"]) + mnote(L["reference"], bdi(page["id"])) + mnote(L["period"], esc(page["period"])),
                     f'<h1>{esc(page["title"])}</h1><p class="rubric" style="margin-top:24px">{esc(L["establishes"])}</p><div class="statement"><p>{esc(page["summary"])}</p></div>', apparatus, "major"))
    for key, label in (("definition", "measures"), ("universe", "applies"), ("currentness", "currentness")):
        out.append(entry(rubric(L[label]), f'<div class="text"><p>{esc(page[key])}</p></div>', "", "compact"))
    out.append(entry(rubric(L["does_not_establish"]), f'<div class="statement"><p>{esc(page["does_not_establish"])}</p></div>', "", "boundary"))
    chips = "".join(f'<li><a class="chip" href="/{shell["lang"]}/data/?source={esc(sid)}#source-{esc(sid)}">{bdi(sid)}</a></li>' for sid in page["trace_ids"])
    trace = rubric(L["trace"]) + f'<p>{esc(L["trace_intro"])}</p><ul class="inline-list" style="margin-top:8px"><li><span class="chip">{bdi(page["id"])}</span></li>{chips}</ul>'
    out.append(f'<section class="entry"><div class="m"><h2 style="font-size:var(--fs-h3)">{esc(L["source"])}</h2><p class="mnote">{esc(L["source_intro"])}</p></div><div class="s">{"".join(source_card(s) for s in page["sources"])}</div><div class="a">{trace}</div></section>')
    used = "".join(f'<li><a href="{x["href"]}">{esc(x["title"])}</a></li>' for x in page["used_in_readings"])
    back = "".join(f'<li><a href="{x["href"]}">{esc(x["label"])}</a></li>' for x in page["routes_back"])
    hub = f'<p><a href="{page["hrefs"]["evidence"]}">{esc(L["evidence_hub"])}</a></p><p><a href="{page["hrefs"]["data"]}">{esc(L["data"])}</a></p><p><a href="{page["hrefs"]["methodology"]}">{esc(L["methodology"])}</a></p>'
    out.append(entry(rubric(L["used_in"]), f'<ul class="mlist q">{used}</ul>'))
    out.append(entry(rubric(L["related"]) + f'<p class="mnote">{esc(L["related_intro"])}</p>', f'<ul class="mlist q">{back}</ul>', hub))
    more = "".join(f'<div class="sub"><div class="m">{rubric(L[k])}</div><div class="s text"><p>{esc(page[k])}</p></div><div class="a"></div></div>' for k in ("method", "change_trigger", "verification") if page[k])
    more += f'<div class="sub"><div class="m">{rubric(L["reading_guidance"])}</div><div class="s text">{paragraphs(page["reading_guidance"]["paragraphs"])}</div><div class="a"></div></div>'
    out.append(f'<details class="more"><summary><span class="rubric">{esc(L["more"])}</span><span class="hint">{esc(L["more_intro"])}</span></summary><div class="subs" style="border-top:0">{more}</div></details>')
    out.append(f'<section class="entry tail"><div class="m">{rubric(L["reference"])}<p class="statement">{bdi(page["id"])}</p></div><div class="s"><div class="actions" style="margin-top:4px"><button type="button" class="tbtn">{esc(L["cite"])}</button><a href="{page["hrefs"]["rights"]}">{esc(L["reuse"])}</a><a href="{page["hrefs"]["corrections"]}">{esc(L["history"])}</a><a href="{page["hrefs"]["report"]}">{esc(L["report"])}</a></div></div><div class="a"><p>{esc(L["reuse_note"])}</p></div></section>')
    out.append(footer(shell))
    return "".join(out)


def reading(page, shell):
    L = page["labels"]; lang = shell["lang"]
    out = [header(shell), crumb(page["breadcrumb"], shell)]
    out.append(entry(rubric(L["eyebrow"]) + mnote(L["evidence_period"], esc(page["evidence_period"])) + mnote(L["last_reviewed"], esc(page["last_reviewed"])),
                     f'<h1>{esc(page["title"])}</h1><div class="statement" style="margin-top:22px"><p>{esc(page["thesis"])}</p></div>', f'<p>{esc(page["question"])}</p>', "major first"))
    out.append(entry(rubric(L["do_not_infer"]), f'<div class="statement"><p>{esc(page["prohibited_inference"])}</p></div>', "", "boundary"))
    for i, s in enumerate(page["sections"]):
        head_ = f'<h2 style="margin-bottom:14px">{esc(s["heading"])}</h2>' if s["heading"] else ""
        out.append(f'<section class="entry"><div class="m"><span class="num">{i+1:02d}</span></div><div class="s">{head_}<div class="{"statement" if i == 0 else "text"}">{reading_blocks(s["blocks"])}</div></div><div class="a"></div></section>')
        if i == 0:
            out.append('<section class="entry"><div class="m">' + rubric(page["visuals"][0]["labels"]["what_it_shows"]) + "</div>" + "".join(figure(v, lang) for v in page["visuals"]) + "</section>")
    steps = []
    for st in page["trace"]:
        srcs = "".join(f'<li><a href="{s["data_href"]}">{esc(s["title"] or s["id"])}</a></li>' for s in st["sources"])
        if st["no_locator_note"]:
            srcs += f'<li class="mnote">{esc(st["no_locator_note"])}</li>'
        steps.append(f'<li><div><div class="step-head"><a href="{st["href"]}">{esc(st["proposition"])}</a></div><div class="step-meta">{esc(L["reference"])} {bdi(st["id"])}</div><ul class="step-src">{srcs}</ul></div></li>')
    back = "".join(f'<li><a href="{b["href"]}">{esc(b["label"])}</a></li>' for b in page["return_to"])
    out.append(f'<section class="entry major"><div class="m"><h2 style="font-size:var(--fs-h3)">{esc(L["trace"])}</h2><p class="mnote">{esc(L["trace_intro"])}</p><p class="mnote">{esc(page["trace_status"])}</p></div>'
               f'<div class="s"><ol class="path-list">{"".join(steps)}</ol></div><div class="a"><p><a href="{page["compare_href"]}">{esc(L["compare"])}</a></p>{rubric(L["return"])}<ul class="mlist">{back}</ul></div></section>')
    out.append(f'<section class="entry"><div class="m">{rubric(L["sources"])}</div><div class="s">{"".join(source_card(s) for s in page["sources"])}</div><div class="a"></div></section>')
    rel = "".join(f'<div class="sub"><div class="m">{mnote(L["evidence_period"], esc(x["evidence_period"]))}</div><div class="s"><p class="q"><a href="{x["href"]}">{esc(x["title"])}</a></p><p class="gets">{esc(x["thesis"])}</p></div><div class="a"></div></div>' for x in page["related"])
    out.append(f'<section class="entry tail" style="display:block"><span class="rubric">{esc(L["related"])}</span><div class="subs">{rel}</div><p style="margin-top:18px"><a href="{L["readings_index_href"]}">{esc(L["all"])}</a></p></section>')
    out.append(footer(shell))
    return "".join(out)


COMPOSE = {"home": home, "record": record, "reading": reading}
