#!/usr/bin/env python3
"""Architecture diagrams under design/architecture/ — derived from current governed state (Pre-Tranche-C P4, V-D2).

The site map and the page-family map are drawn from the navigation contract (site-src/content/content/
navigation_interaction.json) and the public inventory (site-src/content/content/public_inventory.json); the full-stack
diagram takes its counts from the same inventory. The design-to-code flow carries no count or navigation and is not
regenerated. The diagrams are aids to understanding, never a parallel truth.

  python3 scripts/architecture_diagrams.py            # write the SVGs and their PNG previews
  python3 scripts/architecture_diagrams.py --check    # exit 1 if a committed SVG differs from the current state
"""
import json
import os
import re
import sys
from html import escape

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
C = os.path.join(ROOT, "site-src", "content")
OUT = os.path.join(ROOT, "design", "architecture")
FONT = "IBM Plex Sans, IBM Plex Sans Arabic, DejaVu Sans, Arial, sans-serif"
INK, TEAL, MUTED, LINE, PAPER, MINT, SAND, WHITE, NAVY = "#082D4F", "#0B6A63", "#64748B", "#CBD5E1", "#FCFBF7", "#E8F3EF", "#F7F2E8", "#FFFFFF", "#082D4F"


def load(rel):
    with open(os.path.join(C, rel), encoding="utf-8") as fh:
        return json.load(fh)


def state():
    nav = load("content/navigation_interaction.json")
    inv = {c["key"]: c["value"] for c in load("content/public_inventory.json")["counts"]}
    specs = load("page_specs.json")
    n_specs = len(specs["page_specs"] if isinstance(specs, dict) else specs)
    return nav, inv, n_specs


def t(x, y, s, size=12, weight=400, fill=INK, anchor="start", rtl=False):
    d = ' direction="rtl"' if rtl else ""
    return (f'<text x="{x:g}" y="{y:g}" font-family="{FONT}" font-size="{size}" font-weight="{weight}" fill="{fill}" '
            f'text-anchor="{anchor}"{d}>{escape(str(s), quote=False)}</text>')


def box(x, y, w, h, fill=WHITE):
    return f'<rect x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" rx="12" fill="{fill}" stroke="{LINE}" stroke-width="1.5"/>'


def header(width, title, subtitle):
    return (f'<rect width="{width}" height="100%" fill="{PAPER}"/><rect x="0" y="0" width="{width}" height="110" fill="{NAVY}"/>'
            + t(44, 48, title, 28, 700, WHITE) + t(44, 78, subtitle, 14, 400, "#DCE8F0"))


def row(items, y, h, fill, x0=44, width=1912, gap=12):
    """items: list of (title, lines, ar_title). Returns svg for equal-width boxes."""
    n = len(items)
    w = (width - gap * (n - 1)) / n
    out = []
    for i, (title, lines, ar) in enumerate(items):
        x = x0 + i * (w + gap)
        out.append(box(round(x, 2), y, round(w, 2), h, fill))
        out.append(t(round(x + 16, 2), y + 29, title, 16, 600))
        if ar:
            out.append(t(round(x + w - 16, 2), y + 51, ar, 13, 500, TEAL, "start", rtl=True))   # rtl: start = right edge
        for j, line in enumerate(lines):
            out.append(t(round(x + 16, 2), y + 51 + 18 * j, line, 11, 400, MUTED))
    return "".join(out)


FIREWALL = ("people ≠ accounts · access ≠ use · infrastructure ≠ outcome · target ≠ result · programme KPI ≠ national prevalence · "
            "licence/listing ≠ operation · observed ≠ estimated ≠ projected · missing ≠ zero")


def site_map(nav, inv, n):
    W, H = 2000, 1110
    s = [header(W, "Yemen Financial Inclusion Evidence — Public Site Map",
                f"Complete public route system · {n} controlled Page Specs · Arabic + English co-authoritative · derived from the navigation contract")]
    s.append(t(44, 145, "GLOBAL SHELL", 12, 700, TEAL))
    s.append(box(44, 160, 1912, 64) + t(60, 187, "Identity / Home via logo", 17, 600)
             + t(60, 209, "Global utilities: Search · Language · Cite this page · Report an issue", 13, 400, MUTED))
    s.append(t(44, 258, "PRIMARY NAVIGATION", 12, 700, TEAL))
    prim = []
    for it in nav["global_navigation"]:
        if it.get("children"):
            prim.append((it["label_en"], [f'{c["label_en"]} {c["route"]}' for c in it["children"]], it["label_ar"]))
        else:
            prim.append((it["label_en"], [it["route"]], it["label_ar"]))
    s.append(row(prim, 272, 88, MINT))
    s.append(t(44, 390, "TRUST LAYER (secondary, always reachable)", 12, 700, TEAL))
    s.append(row([(x["label_en"], [x["route"]], x["label_ar"]) for x in nav["trust_navigation"]], 404, 72, SAND))
    s.append(t(44, 510, "QUESTION-LED PUBLIC DOMAINS (contextual; reached from Home, Explore and search)", 12, 700, TEAL))
    with open(os.path.join(ROOT, "authority", "YFI_CURRENT_PROJECT_CONTEXT.json"), encoding="utf-8") as fh:
        order = json.load(fh).get("domain_routes") or []
    domains = sorted((r["route"] for r in nav["routes"] if r.get("page_family") == "Domain Answer"),
                     key=lambda rt: order.index(rt) if rt in order else len(order))
    s.append(row([(rt.strip("/").title(), [rt], None) for rt in domains], 524, 72, WHITE))
    s.append(t(44, 632, "VERIFY / ANALYSE / MEASURE", 12, 700, TEAL))
    s.append(row([
        ("Evidence hub", ["/evidence/", "Find and inspect public evidence"], None),
        ("Compare", ["/evidence/compare/", "Comparability verdict before values"], None),
        (f"Evidence Records ×{inv['evidence_records']}", ["/evidence/[id]/", "Scope · period · method · limitation · source"], None),
        (f"Evidence Readings ×{inv['readings']}", ["/readings/[slug]/", "Bounded cross-source analysis"], None),
        ("Measurement Agenda", ["/measurement/", f"{inv['measurement_priorities']} priorities: unknown → evidence needed"], None),
        ("Data & sources", ["/data/", f"{inv['public_locators']} public locators · {inv['curated_resources']} curated cards"], None),
    ], 646, 96, WHITE))
    s.append(t(44, 778, "UNSEEN BUT REQUIRED PUBLIC-SERVICE LAYERS", 12, 700, TEAL))
    s.append(row([
        ("Local bilingual search", [f"{inv['search_records']} public records only"], None),
        ("Source-reference closure", ["Claim → evidence → source → rights"], None),
        ("Publication firewall", ["No-locator sources never named"], None),
        ("Corrections & versions", ["Historical identity preserved"], None),
        ("Accessible fallbacks", ["Visual → ordered text / table"], None),
        ("Static route export", [f"{n} × 2 + root + 404 = {2 * n + 2} documents"], None),
    ], 792, 76, WHITE))
    s.append(box(44, 904, 1912, 170, WHITE))
    s.append(t(64, 944, "SEMANTIC FIREWALL — always visible in content behaviour, never collapsed by design", 14, 700, TEAL))
    s.append(t(64, 980, FIREWALL, 14, 500))
    s.append(t(64, 1016, "Public experience: UNDERSTAND → EXPLORE → VERIFY", 14, 600))
    s.append(t(64, 1048, "Counts and labels on this diagram are derived by scripts/architecture_diagrams.py; the navigation contract and the public inventory are authoritative.", 11, 400, MUTED))
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img">' + "".join(s) + "</svg>\n"


FAMILY_COLUMNS = [
    ("ORIENT", ["Orientation"]),
    ("EXPLORE / ANSWER", ["Question Entry", "Domain Answer"]),
    ("SYNTHESIZE / MEASURE", ["Reading Index", "Reading", "Measurement"]),
    ("VERIFY / TRUST", ["Evidence Directory", "Evidence Record", "Comparison", "Data & Source", "Reference / Trust"]),
]
PROMINENCE = {"GLOBAL_PRIMARY": "Primary navigation", "PRIMARY_CHILD": "Primary navigation (group child)",
              "SECONDARY_TRUST": "Trust layer", "CONTEXTUAL": "Contextual", "ADDRESSABLE_VERIFICATION": "Addressable (deep link)",
              "IDENTITY_ENTRY": "Identity (logo)", "MIXED_GLOBAL_AND_FOOTER": "Methodology in primary; others in trust layer"}


def family_map(nav, inv, n):
    W, H = 2200, 1400
    fams = {f["page_family"]: f for f in nav["page_families"]}
    listed = [x for _, col in FAMILY_COLUMNS for x in col]
    if sorted(listed) != sorted(fams):
        raise SystemExit(f"family map: page families changed ({sorted(set(fams) ^ set(listed))}); update FAMILY_COLUMNS")
    extra = {"Question Entry": f"{inv['entry_questions']} governed questions", "Reading": f"{inv['readings']} Evidence Readings",
             "Measurement": f"{inv['measurement_priorities']} priorities",
             "Data & Source": f"{inv['public_locators']} public locators + {inv['curated_resources']} curated cards",
             "Evidence Record": f"{inv['public_claims']} are public claims"}
    s = [header(W, "Yemen Financial Inclusion Evidence — Page Family & State Map",
                f"{n} controlled routes · {len(fams)} reusable page families · semantic authority remains in the Production Master")]
    colw, x0, gap = 500, 44, 28
    for ci, (title, members) in enumerate(FAMILY_COLUMNS):
        x = x0 + ci * (colw + gap)
        s.append(t(x + 18, 170, title, 12, 700, TEAL))
        for ri, name in enumerate(members):
            f = fams[name]
            y = 186 + ri * 124
            s.append(box(x, y, colw, 110, MINT if f["navigation_prominence"] in ("GLOBAL_PRIMARY", "PRIMARY_CHILD") else WHITE))
            s.append(t(x + 18, y + 30, name, 16, 600))
            lines = [f"{f['route_count']} route{'s' if f['route_count'] != 1 else ''} · {PROMINENCE.get(f['navigation_prominence'], f['navigation_prominence'])}",
                     "Job: " + f["unique_user_value_role"].replace("_", " ").lower()]
            if name in extra:
                lines.append(extra[name])
            for j, line in enumerate(lines):
                s.append(t(x + 18, y + 54 + 18 * j, line, 11, 400, MUTED))
    y0 = 830
    s.append(t(44, y0, "HARD STATES — design explicitly; never let presentation change semantic state", 12, 700, TEAL))
    s.append(row([
        ("Dense evidence", ["People · Finance · Remittances", "compress without hiding scope/limits"], None),
        ("Sparse / unknown", ["Access", "intentional absence; missing ≠ zero"], None),
        ("Conflict / revision", ["Evidence Records · Remittances", "show disagreement, vintage, contradiction"], None),
        ("Infrastructure vs use", ["Payments · Reforms", "state sequence without outcome inflation"], None),
        ("No public locator", ["withheld dependency", "never named on a public page"], None),
        ("Operational trust", ["Privacy · Rights · Corrections", "deployment facts vs stated principles"], None),
    ], y0 + 16, 100, WHITE, width=2112))
    y1 = 1000
    s.append(t(44, y1, "INTERACTION / RUNTIME LAYERS — same product, different execution responsibilities", 12, 700, TEAL))
    s.append(row([
        ("Layer 1 · Static public truth", ["Real deep-link-safe HTML", "Strongest answer + scope/period + material limitation",
                                           "Source/verification path + accessible visual fallback", "Meaningful without remote service"], None),
        ("Layer 2 · Local progressive enhancement", ["Bundled search + Compare", "Citation copy + disclosures + language context",
                                                      "URL-addressable state where reproducibility matters", "No semantic invention or remote truth"], None),
        ("Layer 3 · Optional adapters", ["Outbound publisher links", "Future analytics / issue submission / authorized APIs",
                                         "Failure must not erase controlled evidence", "No adapter may supersede the Master"], None),
    ], y1 + 16, 132, WHITE, width=2112))
    s.append(box(44, 1210, 2112, 120, WHITE))
    s.append(t(64, 1248, "SEMANTIC FIREWALL", 12, 700, TEAL))
    s.append(t(64, 1280, FIREWALL, 14, 600))
    s.append(t(64, 1310, "Derived by scripts/architecture_diagrams.py from the navigation contract (page families, route counts, prominence) and the public inventory.", 11, 400, MUTED))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">'
            f'<title id="title">Page family and state map</title><desc id="desc">Page families, route counts, navigation prominence, hard states and runtime layers.</desc>'
            + "".join(s) + "</svg>\n")


def full_stack(inv, n, current):
    rules = [(r"Page Specs ×\d+", f"Page Specs ×{n}"), (r"Visual contracts ×\d+", f"Visual contracts ×{inv['visual_contracts']}"),
             (r"\d+ localized pages", f"{2 * n} localized pages"), (r"(?<!Evidence )Readings / Measurement<", "Evidence Readings / Measurement<"),
             (r">Data / Sources<", ">Data &amp; sources<"),
             # F9: the Design package lives in the repository (design/), not in an external design file; no analytics ship
             (r">Design system / Figma<", ">Claude Design package (design/)<"),
             (r">Figma is visual artifact, repository spec remains implementation contract<", ">images illustrate; the repository package is the contract<"),
             (r">HOST / BASE_URL / analytics opt-in / reporting endpoint<", ">public origin · no analytics · static correction path<")]
    out = current
    for pat, rep in rules:
        if not re.search(pat, out) and not re.search(re.escape(rep), out):
            raise SystemExit(f"full-stack diagram: pattern {pat!r} not found")
        out = re.sub(pat, rep, out)
    return out


def render(check=False):
    nav, inv, n = state()
    cur_fs = open(os.path.join(OUT, "YFIE_FULL_STACK_SYSTEM_ARCHITECTURE.svg"), encoding="utf-8").read()
    want = {"YFIE_PUBLIC_SITE_MAP.svg": site_map(nav, inv, n), "YFIE_PAGE_FAMILY_STATE_MAP.svg": family_map(nav, inv, n),
            "YFIE_FULL_STACK_SYSTEM_ARCHITECTURE.svg": full_stack(inv, n, cur_fs)}
    diffs = []
    for name, svg in want.items():
        p = os.path.join(OUT, name)
        have = open(p, encoding="utf-8").read() if os.path.exists(p) else None
        if have != svg:
            diffs.append(name)
            if not check:
                with open(p, "w", encoding="utf-8", newline="\n") as fh:
                    fh.write(svg)
    return want, diffs


def png(names):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        for name in names:
            svg = open(os.path.join(OUT, name), encoding="utf-8").read()
            m = re.search(r'width="(\d+)" height="(\d+)"', svg)
            w, h = int(m.group(1)), int(m.group(2))
            pg = b.new_page(viewport={"width": w, "height": h})
            pg.set_content(f'<html><body style="margin:0">{svg}</body></html>')
            pg.screenshot(path=os.path.join(OUT, name.replace(".svg", ".png")), clip={"x": 0, "y": 0, "width": w, "height": h})
            pg.close()
        b.close()


if __name__ == "__main__":
    check = "--check" in sys.argv
    want, diffs = render(check)
    if check:
        if diffs:
            print("ARCHITECTURE DIAGRAMS STALE: " + ", ".join(diffs))
            sys.exit(1)
        print("ARCHITECTURE DIAGRAMS CURRENT")
    else:
        png(list(want))
        print("ARCHITECTURE DIAGRAMS WRITTEN: " + ", ".join(want))
