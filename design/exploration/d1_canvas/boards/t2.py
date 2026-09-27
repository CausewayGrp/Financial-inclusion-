# -*- coding: utf-8 -*-
"""T2 · ARGUMENT — Design proposition (canvas). Reading-first: one measured column; ANSWER, SCOPE, BOUNDARY and VERIFY
as typographic registers of the same text; evidence discloses in place. The deliberately image-free control: warm
paper, ink, one counter-voice colour. No visual grounding beyond native Arabic composition and editorial voice."""
from __future__ import annotations

from common import esc, bdi, paragraphs, reading_blocks, nav_flat, logo, mobile_rules, rv001_data, rv001_panel1_svg, rv001_index_panel_svg, rv001_tables, rv001_frame_lines

CUR = ' aria-current="page"'
NAME = "T2 · Argument"

TOKENS = """
:root,.root{--paper:#F9F6EF;--ink:#1C1C21;--ink-2:#45454D;--mute:#6B6B74;--rule:#D8D1C2;--counter:#1E4B5B;--line:#9A7A34;
--fs-body:19px;--lh-body:1.6;--fs-lead:23px;--lh-lead:1.5;--fs-stand:26px;--lh-stand:1.4;--fs-h1:46px;--lh-h1:1.08;--fs-h2:28px;--lh-h2:1.28;--fs-h3:21px;--fs-small:15px;--lh-small:1.5;--fs-label:12px;--measure:68ch;--font:'IBM Plex Sans',sans-serif}
html[dir=rtl],[dir=rtl].root{--fs-body:20px;--lh-body:1.95;--fs-lead:23px;--lh-lead:1.8;--fs-stand:26px;--lh-stand:1.75;--fs-h1:42px;--lh-h1:1.35;--fs-h2:28px;--lh-h2:1.55;--fs-h3:22px;--fs-small:16px;--lh-small:1.8;--fs-label:13.5px;--measure:36em;--font:'IBM Plex Sans Arabic',sans-serif}
"""

CSS = TOKENS + """
html,.root{background:var(--paper);color:var(--ink);font-family:var(--font);font-size:var(--fs-body);line-height:var(--lh-body)}
body{margin:0}
a{color:inherit;text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:.18em;text-decoration-color:var(--line)}
h1,h2,h3{margin:0;font-weight:600}
h1{font-size:var(--fs-h1);line-height:var(--lh-h1)}[dir=ltr] h1{letter-spacing:-.015em}
h2{font-size:var(--fs-h2);line-height:var(--lh-h2)}
h3{font-size:var(--fs-h3);line-height:1.4}
p{margin:0 0 1em}p:last-child{margin-bottom:0}
.col{max-width:760px;margin:0 auto;padding:0 24px}
.label{display:block;font-size:var(--fs-label);font-weight:600;color:var(--mute);margin-bottom:10px}
[dir=ltr] .label{text-transform:uppercase;letter-spacing:.12em}
.lead{font-size:var(--fs-lead);line-height:var(--lh-lead);font-weight:300;max-width:var(--measure)}
.stand{font-size:var(--fs-stand);line-height:var(--lh-stand);font-weight:300;max-width:var(--measure)}
.stand b,.lead b{font-weight:500}
.body{max-width:var(--measure)}
.small{font-size:var(--fs-small);line-height:var(--lh-small);color:var(--ink-2)}
.tbtn{background:none;border:0;padding:0;font:inherit;color:inherit;text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:.18em;text-decoration-color:var(--line);cursor:pointer}
.topline{border-bottom:1px solid var(--rule)}
.topline .col{display:flex;justify-content:space-between;align-items:center;gap:16px;padding:8px 24px;font-size:var(--fs-small);color:var(--mute);max-width:1120px}
.topline nav{display:flex;flex-wrap:wrap;gap:4px 20px}
.topline a{text-decoration:none}
.utilities{display:flex;gap:18px;align-items:center;font-weight:500}
.utilities .tbtn,.utilities a{text-decoration:none}
.utilities .lang{border:1px solid var(--rule);padding:4px 9px}
.utilities .menu{display:none}
.mast{text-align:center;padding:34px 0 0}
.mast .brand{display:inline-flex;flex-direction:column;align-items:center;gap:10px;text-decoration:none}
.mast .brand img{width:56px;height:56px}
.mast .name{font-size:13px;font-weight:600;color:var(--ink)}
[dir=ltr] .mast .name{text-transform:uppercase;letter-spacing:.14em}
.pnav{display:flex;justify-content:center;flex-wrap:wrap;gap:6px 28px;padding:22px 0 0;font-size:16px;font-weight:500;border-bottom:1px solid var(--rule);margin-bottom:56px}
.pnav a{text-decoration:none;padding:0 0 14px;border-bottom:2px solid transparent;margin-bottom:-1px}
.pnav a[aria-current=page]{border-bottom-color:var(--ink)}
.pnav .group{display:inline-flex;gap:18px}
.pnav .glabel{color:var(--mute);font-size:13px;font-weight:600;padding-top:2px}
[dir=ltr] .pnav .glabel{text-transform:uppercase;letter-spacing:.08em}
.crumb{font-size:var(--fs-small);color:var(--mute);margin-bottom:28px}
.crumb a{text-decoration:none}
.passage{margin:0 0 56px}
.passage h2{margin-bottom:16px}
.passage h3{margin-bottom:8px}
.runin{display:flex;flex-direction:column;gap:22px}
.runin h3{font-size:var(--fs-small);line-height:var(--lh-small);font-weight:600;color:var(--mute);margin:0 0 4px}
.counter{color:var(--counter);border-inline-start:3px solid var(--counter);padding:4px 0 4px 22px;margin:0 0 56px;max-width:var(--measure)}
[dir=rtl] .counter{padding:4px 22px 4px 0}
.counter .label{color:var(--counter)}
.counter p{font-weight:500}
.counter h2{color:var(--counter)}
.actions{display:flex;flex-wrap:wrap;gap:10px 28px;margin-top:22px;font-weight:600}
.actions a{text-decoration-thickness:2px}
.qlist{list-style:none;margin:8px 0 0;padding:0;counter-reset:q}
.qlist li{display:grid;grid-template-columns:40px minmax(0,1fr);gap:12px;padding:16px 0;border-top:1px solid var(--rule)}
.qlist li::before{counter-increment:q;content:counter(q);font-size:var(--fs-small);font-weight:600;color:var(--mute);padding-top:6px}
.qlist .q{font-size:var(--fs-h3);line-height:1.4;font-weight:500}
.qlist .gets{margin-top:4px}
details.disc{border-top:1px solid var(--rule);border-bottom:1px solid var(--rule);margin:22px 0 0}
details.disc summary{cursor:pointer;padding:14px 0;font-weight:600;font-size:var(--fs-small);list-style:none}
details.disc summary::-webkit-details-marker{display:none}
details.disc summary::before{content:"+";display:inline-block;width:1.4em;font-weight:600}
details.disc[open] summary::before{content:"−"}
details.disc ul{list-style:none;margin:0;padding:0 0 12px}
details.disc li{padding:8px 0;border-top:1px solid var(--rule)}
.recs li .meta{display:block;font-size:var(--fs-small);color:var(--mute)}
.scope{display:flex;flex-direction:column;gap:6px;margin:22px 0 0;padding:16px 0;border-top:1px solid var(--rule);border-bottom:1px solid var(--rule);font-size:var(--fs-small);line-height:var(--lh-small)}
.scope div{display:grid;grid-template-columns:minmax(120px,.3fr) minmax(0,1fr);gap:12px}
.scope dt{font-weight:600;color:var(--mute);margin:0}.scope dd{margin:0;color:var(--ink-2)}
.notes{list-style:none;margin:0;padding:0;counter-reset:n}
.notes>li{display:grid;grid-template-columns:32px minmax(0,1fr);gap:12px;padding:16px 0;border-top:1px solid var(--rule);font-size:var(--fs-small);line-height:var(--lh-small)}
.notes>li::before{counter-increment:n;content:counter(n);font-weight:600;color:var(--mute)}
.notes strong{font-size:var(--fs-body);color:var(--ink);display:block;margin-bottom:2px}
.notes .kind,.notes .ref{color:var(--mute);display:block}
.notes .acts{display:flex;flex-wrap:wrap;gap:6px 18px;margin-top:8px;font-weight:500}
.notes .rights{color:var(--mute);margin-top:6px}
.plain{list-style:none;margin:0;padding:0}
.plain li{padding:8px 0;border-top:1px solid var(--rule)}
.plain li:first-child{border-top:0;padding-top:0}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:8px}
.chip{display:inline-block;border:1px solid var(--rule);padding:3px 8px;font-size:var(--fs-small);text-decoration:none}
.pull{margin:28px 0;padding:0 0 0 24px;border-inline-start:2px solid var(--line);font-size:var(--fs-stand);line-height:var(--lh-stand);font-weight:300}
[dir=rtl] .pull{padding:0 24px 0 0}
.rlist{padding-inline-start:1.2em}
.meta-line{display:flex;flex-wrap:wrap;gap:6px 24px;margin:20px 0 0;font-size:var(--fs-small);color:var(--mute)}
.meta-line b{color:var(--ink-2);font-weight:600}
.reading{display:grid;grid-template-columns:190px minmax(0,760px);gap:56px;justify-content:center;padding:0 24px}
.toc{position:sticky;top:24px;align-self:start;font-size:var(--fs-small);line-height:var(--lh-small)}
.toc ol{list-style:none;margin:0;padding:0;counter-reset:t}
.toc li{padding:7px 0;border-top:1px solid var(--rule)}
.toc li::before{counter-increment:t;content:counter(t) " ";color:var(--mute);font-weight:600}
.toc a{text-decoration:none}
.essay{max-width:760px}
.figure{margin:40px 0;padding:24px 0;border-top:1px solid var(--ink);border-bottom:1px solid var(--ink)}
.figure h3{font-size:var(--fs-h3);margin-bottom:4px}
.figure .cap{font-size:var(--fs-small);line-height:var(--lh-small);color:var(--ink-2);max-width:70ch;margin:0 0 6px}
.figure .panelrow{display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.5fr);gap:28px;align-items:start;margin:18px 0}
.figure .lanes{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.figure h4,.figure h5{margin:0 0 6px;font-size:var(--fs-small);font-weight:600;color:var(--ink-2)}
.figure .between{font-size:var(--fs-small);font-weight:600;color:var(--counter);margin:0 0 10px}
.legend{display:flex;flex-wrap:wrap;gap:8px 20px;font-size:var(--fs-small);color:var(--ink-2);margin-top:6px}
.legend .k{display:inline-flex;align-items:center;gap:7px}
.legend .sw{display:inline-block;width:11px;height:11px;background:var(--ink)}.legend .sw.c{border-radius:50%}.legend .sw.s{background:var(--paper);border:2px solid var(--ink)}
.figure .foot{display:flex;flex-direction:column;gap:6px;font-size:var(--fs-small);line-height:var(--lh-small);color:var(--ink-2);margin-top:12px}
.figure .foot .bnd{color:var(--counter);font-weight:500}
svg.rv1,svg.rv2{max-width:100%;height:auto;font-family:var(--font)}
.axis{stroke:var(--ink);stroke-width:1}.grid{stroke:var(--rule);stroke-width:1}.tick{stroke:var(--ink);stroke-width:1}
.lbl{font-size:11px;fill:var(--mute);font-weight:500}.lbl.origin{fill:var(--ink)}.unit{font-size:11px;fill:var(--ink-2);font-weight:600}
.val{font-size:12.5px;fill:var(--ink);font-weight:600}.val.small{font-size:11px}
.mark.a{fill:var(--ink)}.mark.b{fill:var(--paper);stroke:var(--ink);stroke-width:2}
.path{stroke:var(--ink);stroke-width:1.5}
.rvtab{border-collapse:collapse;width:100%;font-size:var(--fs-small);line-height:var(--lh-small);margin-top:10px}
.rvtab caption{text-align:start;font-weight:600;color:var(--ink-2);padding:8px 0}
.rvtab th,.rvtab td{text-align:start;padding:7px 10px;border-top:1px solid var(--rule);vertical-align:top}
.rvtab thead th{border-top:1px solid var(--ink);font-weight:600}
.rvtab .state{color:var(--mute)}.rvtab .marker{font-weight:600}
.props{list-style:none;margin:0;padding:0;counter-reset:p}
.props>li{display:grid;grid-template-columns:36px minmax(0,1fr);gap:12px;padding:18px 0;border-top:1px solid var(--rule)}
.props>li::before{counter-increment:p;content:counter(p);font-weight:600;color:var(--mute);padding-top:4px}
.props .prop{font-size:var(--fs-h3);line-height:1.4;font-weight:500}
.props .line{font-size:var(--fs-small);line-height:var(--lh-small);color:var(--ink-2);margin-top:6px}
.foot{border-top:1px solid var(--ink);margin-top:72px;padding:36px 0 24px}
.foot .col{max-width:1120px;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,2fr);gap:40px}
.foot img{width:48px;height:48px;margin-bottom:12px}
.foot p{font-size:var(--fs-small);color:var(--ink-2);max-width:36ch}
.foot nav{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px;font-size:var(--fs-small)}
.foot nav div{display:flex;flex-direction:column;gap:6px}
.foot nav strong{font-size:var(--fs-label);color:var(--mute)}
[dir=ltr] .foot nav strong{text-transform:uppercase;letter-spacing:.1em}
.foot nav a{text-decoration:none}
.foot .fine{max-width:1120px;margin:28px auto 0;padding:14px 24px 0;border-top:1px solid var(--rule);font-size:var(--fs-small);color:var(--mute)}
""" + mobile_rules("""
:root,.root{--fs-h1:34px;--fs-h2:24px;--fs-stand:22px;--fs-lead:20px;--fs-body:18px}
[dir=rtl].root{--fs-h1:32px;--fs-h2:24px;--fs-stand:22px;--fs-lead:20px;--fs-body:19px}
.col{padding:0 18px}
.topline .col{padding:8px 18px}
.topline nav{display:none}
.utilities{gap:12px;font-size:14px}
.utilities .menu{display:inline-block}
.utilities .cite,.utilities .report{display:none}
.mast{padding-top:22px}
.mast .brand img{width:44px;height:44px}
.pnav{display:none}
.passage{margin-bottom:40px}
.reading{display:block;padding:0 18px}
.toc{position:static;margin-bottom:28px}
.figure .panelrow{grid-template-columns:minmax(0,1fr)}
.figure .lanes{grid-template-columns:minmax(0,1fr)}
.scope div{grid-template-columns:1fr;gap:2px}
.foot .col{grid-template-columns:1fr;gap:24px}
.foot nav{grid-template-columns:1fr}
""")


def label(t):
    return f'<span class="label">{esc(t)}</span>'


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
    return (f'<div class="topline"><div class="col"><nav aria-label="{esc(L["trust_nav"])}">{trust}</nav><div class="utilities"><button type="button" class="tbtn">{esc(L["search"])}</button><button type="button" class="tbtn cite">{esc(L["cite"])}</button><a class="report" href="{shell["contact_href"]}">{esc(L["report"])}</a>'
            f'<button type="button" class="tbtn lang" lang="{other}" dir="{"ltr" if other == "en" else "rtl"}">{esc(L["lang_switch_name"])}</button><button type="button" class="tbtn menu">{esc(L["menu"])}</button></div></div></div>'
            f'<header class="mast"><a class="brand" href="{shell["home_href"]}">{logo(56)}<span class="name">{esc(shell["product"])}</span></a><nav class="pnav" aria-label="{esc(L["primary_nav"])}">{"".join(nav)}</nav></header><main>')


def footer(shell):
    L = shell["labels"]
    groups = "".join(f'<div><strong>{esc(g["label"])}</strong>' + "".join(f'<a href="{l["href"]}">{esc(l["label"])}</a>' for l in g["links"]) + "</div>" for g in shell["footer"])
    return (f'</main><footer class="foot"><div class="col"><div>{logo(48)}<p>{esc(L["footer_strapline"])}</p></div><nav aria-label="{esc(L["footer_nav"])}">{groups}</nav></div>'
            f'<div class="fine">© 2026 CauseWay · {esc(L["footer_rights"])} · {esc(shell["edition"])}</div></footer>')


def crumb(bc, shell):
    if not bc:
        return ""
    cur = bdi(bc["current"]) if bc["mode"] == "STABLE_OBJECT_ID" else esc(bc["current"])
    return f'<nav class="crumb" aria-label="{esc(shell["labels"]["breadcrumb"])}"><a href="{bc["parent_href"]}">{esc(bc["parent_label"])}</a> / <span aria-current="page">{cur}</span></nav>'


def note_item(s):
    L = s["labels"]
    ref = f'<span class="ref">{esc(s["reference_label"])} {bdi(s["id"])}</span>'
    head_ = f'<strong dir="auto">{esc(s["title"])}</strong><span class="kind" dir="auto">{esc(s["kind_line"])}</span>{ref}' if s["display_ready"] and s["title"] else f'<strong>{esc(s["untitled_label"])}</strong>{ref}'
    rights = f'<div class="rights">{esc(s["rights_note"])}</div>' if s["rights_note"] else ""
    return (f'<li><div>{head_}<div class="acts"><a href="{s["data_href"]}">{esc(L["open_source_record"])}</a><a href="{esc(s["url"])}">{esc(L["open_original"])}</a><button type="button" class="tbtn">{esc(L["copy_reference"])}</button></div>{rights}</div></li>')


def figure(v, lang):
    d = rv001_data(v); f = rv001_frame_lines(v)
    return (f'<figure class="figure"><h3>{esc(f["title"])}</h3><p class="cap">{esc(v["question"])}</p><p class="cap">{esc(f["scope"])}</p>'
            f'<div class="panelrow"><div><h4>2024 · {esc(d["unit_usd"])}</h4>{rv001_panel1_svg(d, lang, w=380, h=280)}<div class="legend"><span class="k"><span class="sw c"></span>{esc(d["label_ar2024"])}</span><span class="k"><span class="sw s"></span>{esc(d["label_ar2025"])}</span></div><p class="cap" style="margin-top:8px"><b>{esc(f["same_year"])}</b></p></div>'
            f'<div><p class="between">{esc(f["not_comparable"])}</p><h4>{esc(d["unit_index"])} · {esc(v["labels"]["derived"])}</h4><div class="lanes"><div><h5>{esc(d["label_cby"])}</h5>{rv001_index_panel_svg(d["cby_index"], lang, w=260, h=200, mark="circle")}</div><div><h5>{esc(d["label_imf"])}</h5>{rv001_index_panel_svg(d["imf_index"], lang, w=260, h=200, mark="square")}</div></div><p class="cap" style="margin-top:8px">{esc(f["note"])}</p></div></div>'
            f'<div class="foot"><p class="bnd"><b>{esc(f["boundary_label"])}</b> {esc(f["boundary"])}</p><p>{esc(f["credit"])}</p><p>{esc(f["full_record_label"])} <a href="{f["full_record"]}">{esc(f["full_record"])}</a></p></div>'
            f'<details class="disc"><summary>{esc(v["labels"]["text_alternative"])}</summary><p class="small" style="padding:8px 0 0">{esc(v["alt_text"])}</p><div class="table-wrap">{rv001_tables(d, v, lang)}</div></details><figcaption class="sr-only">{esc(v["alt_text"])}</figcaption></figure>')


def home(page, shell):
    L = page["labels"]; S = {s["order"]: s for s in page["sections"]}
    out = [header(shell), '<div class="col">']
    out.append(f'<div class="passage">{label(L["product"])}<h1>{esc(page["title"])}</h1><div class="lead" style="margin-top:26px">{paragraphs(S[1]["paragraphs"])}</div><div class="actions"><a href="{page["hrefs"]["explore"]}">{esc(L["start"])}</a><a href="{page["hrefs"]["evidence"]}">{esc(L["verify"])}</a></div></div>')
    qs = "".join(f'<li><div><div class="q"><a href="{q["href"]}">{esc(q["question"])}</a></div><div class="gets small">{esc(q["gets"])}</div></div></li>' for q in page["starting_questions"])
    out.append(f'<div class="passage"><h2>{esc(S[2]["heading"])}</h2><div class="body">{paragraphs(S[2]["paragraphs"])}</div><ol class="qlist">{qs}</ol><p class="small" style="margin-top:14px"><a href="{page["hrefs"]["explore"]}">{esc(L["view_all"])}</a></p></div>')
    recs = "".join(f'<li><a href="{r["href"]}">{esc(r["title"])}</a>' + (f'<span class="meta">{esc(r["period"])}</span>' if r["period"] else "") + "</li>" for r in page["records"])
    out.append(f'<div class="passage"><h2>{esc(S[3]["heading"])}</h2><div class="body">{paragraphs(S[3]["paragraphs"])}</div><details class="disc recs"><summary>{esc(L["records_heading"])}</summary><ul>{recs}</ul></details></div>')
    out.append(f'<div class="counter"><h2>{esc(S[4]["heading"])}</h2><div class="body" style="margin-top:12px">{paragraphs(S[4]["paragraphs"])}</div></div>')
    out.append(f'<div class="passage"><h2>{esc(S[5]["heading"])}</h2><div class="body">{paragraphs(S[5]["paragraphs"])}</div></div>')
    v = page["system_visual"]
    out.append(f'<div class="passage"><h2 id="system">{esc(S[6]["heading"])}</h2><div class="body">{paragraphs(S[6]["paragraphs"])}</div>'
               f'<div class="runin" style="margin-top:28px;padding-top:22px;border-top:1px solid var(--rule)">{label(L["visual_eyebrow"])}<div><h3>{esc(v["title"])}</h3><p class="small">{esc(v["question"])}</p><div class="body" style="margin-top:10px"><p>{esc(v["alt_text"])}</p></div><p class="small" style="margin-top:10px"><a href="{v["canonical_href"]}">{esc(L["open_record"])}</a></p></div></div></div>')
    for o in (7, 8):
        out.append(f'<div class="passage"><h2>{esc(S[o]["heading"])}</h2><div class="body">{paragraphs(S[o]["paragraphs"])}</div></div>')
    f = page["featured"]
    out.append(f'<div class="passage" style="padding-top:36px;border-top:1px solid var(--ink)">{label(L["featured"])}<h2><a href="{f["href"]}">{esc(f["title"])}</a></h2><p class="stand" style="margin-top:14px">{esc(f["thesis"])}</p><p class="small" style="margin-top:14px"><b>{esc(L["evidence_period"])}</b> · {esc(f["evidence_period"])}</p><div class="actions"><a href="{f["href"]}">{esc(L["open_reading"])}</a><a href="{page["hrefs"]["readings"]}">{esc(L["all_readings"])}</a></div></div>')
    ctas = "".join(f'<li><a href="{h}"><b>{esc(t)}</b></a> — {esc(d)}</li>' for h, t, d in ((page["hrefs"]["readings"], L["readings_nav"], L["cta_readings"]), (page["hrefs"]["measurement"], L["measurement_nav"], L["cta_measurement"]), (page["hrefs"]["data"], L["data_nav"], L["cta_data"])))
    out.append(f'<div class="passage"><ul class="plain small">{ctas}</ul></div></div>')
    out.append(footer(shell))
    return "".join(out)


def record(page, shell):
    L = page["labels"]
    summary = esc(page["summary"]).replace("8.55%", "<b>8.55%</b>").replace("+11%", "<b>+11%</b>").replace("1,473", "<b>1,473</b>").replace("1,357", "<b>1,357</b>").replace("561", "<b>561</b>")
    out = [header(shell), '<div class="col">', crumb(page["breadcrumb"], shell)]
    out.append(f'<div class="passage">{label(L["family"])}<h1>{esc(page["title"])}</h1><p class="stand" style="margin-top:22px">{summary}</p>'
               f'<dl class="scope"><div><dt>{esc(L["period"])}</dt><dd>{esc(page["period"])}</dd></div><div><dt>{esc(L["applies"])}</dt><dd>{esc(page["universe"])}</dd></div><div><dt>{esc(L["reference"])}</dt><dd>{bdi(page["id"])}</dd></div></dl></div>')
    out.append(f'<div class="passage runin"><div><h3>{esc(L["measures"])}</h3><div class="body"><p>{esc(page["definition"])}</p></div></div><div><h3>{esc(L["currentness"])}</h3><div class="body"><p>{esc(page["currentness"])}</p></div></div></div>')
    out.append(f'<div class="counter">{label(L["does_not_establish"])}<p>{esc(page["does_not_establish"])}</p></div>')
    chips = "".join(f'<a class="chip" href="/{shell["lang"]}/data/?source={esc(sid)}#source-{esc(sid)}">{bdi(sid)}</a>' for sid in page["trace_ids"])
    out.append(f'<div class="passage"><h2>{esc(L["source"])}</h2><p class="small">{esc(L["source_intro"])}</p><ol class="notes">{"".join(note_item(s) for s in page["sources"])}</ol>'
               f'<div style="margin-top:22px">{label(L["trace"])}<p class="small">{esc(L["trace_intro"])}</p><div class="chips"><span class="chip">{bdi(page["id"])}</span>{chips}</div></div></div>')
    used = "".join(f'<li><a href="{x["href"]}">{esc(x["title"])}</a></li>' for x in page["used_in_readings"])
    back = "".join(f'<li><a href="{x["href"]}">{esc(x["label"])}</a></li>' for x in page["routes_back"])
    out.append(f'<div class="passage runin"><div><h3>{esc(L["used_in"])}</h3><ul class="plain">{used}</ul></div><div><h3>{esc(L["related"])}</h3><p class="small">{esc(L["related_intro"])}</p><ul class="plain">{back}<li><a href="{page["hrefs"]["evidence"]}">{esc(L["evidence_hub"])}</a> · <a href="{page["hrefs"]["data"]}">{esc(L["data"])}</a> · <a href="{page["hrefs"]["methodology"]}">{esc(L["methodology"])}</a></li></ul></div></div>')
    more = "".join(f'<div><h3>{esc(L[k])}</h3><div class="body"><p>{esc(page[k])}</p></div></div>' for k in ("method", "change_trigger", "verification") if page[k])
    more += f'<div><h3>{esc(L["reading_guidance"])}</h3><div class="body">{paragraphs(page["reading_guidance"]["paragraphs"])}</div></div>'
    out.append(f'<details class="disc passage"><summary>{esc(L["more"])} — {esc(L["more_intro"])}</summary><div class="runin" style="padding:12px 0 8px">{more}</div></details>')
    out.append(f'<div class="passage small">{label(L["reference"])}<p><b>{bdi(page["id"])}</b></p><div class="actions" style="margin-top:12px"><button type="button" class="tbtn">{esc(L["cite"])}</button><a href="{page["hrefs"]["rights"]}">{esc(L["reuse"])}</a><a href="{page["hrefs"]["corrections"]}">{esc(L["history"])}</a><a href="{page["hrefs"]["report"]}">{esc(L["report"])}</a></div><p style="margin-top:14px">{esc(L["reuse_note"])}</p></div></div>')
    out.append(footer(shell))
    return "".join(out)


def reading(page, shell):
    L = page["labels"]; lang = shell["lang"]
    toc = "".join(f'<li><a href="#s-{esc(s["section_id"])}">{esc(s["heading"])}</a></li>' for s in page["sections"] if s["heading"])
    out = [header(shell), '<div class="col">', crumb(page["breadcrumb"], shell)]
    out.append(f'<div class="passage">{label(L["eyebrow"])}<h1>{esc(page["title"])}</h1><p class="stand" style="margin-top:22px">{esc(page["thesis"])}</p>'
               f'<div class="meta-line"><span><b>{esc(L["evidence_period"])}</b> · {esc(page["evidence_period"])}</span><span><b>{esc(L["last_reviewed"])}</b> · {esc(page["last_reviewed"])}</span></div></div>')
    out.append(f'<div class="counter">{label(L["do_not_infer"])}<p>{esc(page["prohibited_inference"])}</p></div></div>')
    out.append(f'<div class="reading"><nav class="toc" aria-label="{esc(page["title"])}"><ol>{toc}</ol></nav><article class="essay">')
    for i, s in enumerate(page["sections"]):
        head_ = f'<h2 id="s-{esc(s["section_id"])}">{esc(s["heading"])}</h2>' if s["heading"] else ""
        cls = "lead" if i == 0 else "body"
        out.append(f'<div class="passage">{head_}<div class="{cls}">{reading_blocks(s["blocks"])}</div></div>')
        if i == 0:
            out.append("".join(figure(v, lang) for v in page["visuals"]))
    props = []
    for st in page["trace"]:
        srcs = " · ".join(f'<a href="{s["data_href"]}">{esc(s["title"] or s["id"])}</a>' for s in st["sources"])
        if st["no_locator_note"]:
            srcs += (" · " if srcs else "") + esc(st["no_locator_note"])
        props.append(f'<li><div><div class="prop"><a href="{st["href"]}">{esc(st["proposition"])}</a></div><div class="line">{esc(L["reference"])} {bdi(st["id"])}{" · " + srcs if srcs else ""}</div></div></li>')
    back = "".join(f'<li><a href="{b["href"]}">{esc(b["label"])}</a></li>' for b in page["return_to"])
    out.append(f'<div class="passage" style="padding-top:36px;border-top:1px solid var(--ink)"><h2>{esc(L["trace"])}</h2><p class="small">{esc(L["trace_intro"])}</p><p class="small"><b>{esc(page["trace_status"])}</b></p><ol class="props">{"".join(props)}</ol>'
               f'<div class="actions"><a href="{page["compare_href"]}">{esc(L["compare"])}</a></div><div class="runin" style="margin-top:28px"><div><h3>{esc(L["return"])}</h3><ul class="plain">{back}</ul></div></div></div>')
    out.append(f'<div class="passage"><h2>{esc(L["sources"])}</h2><ol class="notes">{"".join(note_item(s) for s in page["sources"])}</ol></div>')
    rel = "".join(f'<li><div><div class="prop"><a href="{x["href"]}">{esc(x["title"])}</a></div><div class="line">{esc(x["thesis"])}</div></div></li>' for x in page["related"])
    out.append(f'<div class="passage"><h2>{esc(L["related"])}</h2><ol class="props">{rel}</ol><p class="small" style="margin-top:14px"><a href="{L["readings_index_href"]}">{esc(L["all"])}</a></p></div></article></div>')
    out.append(footer(shell))
    return "".join(out)


COMPOSE = {"home": home, "record": record, "reading": reading}
