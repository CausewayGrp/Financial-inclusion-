#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Content-parity check for the reference implementation against the baseline build (`dist/`).

  python3 design/reference/check_content.py [site_dir] [--text]   # --text also lists baseline sentences the reference lost

For every document the reference site renders, in both languages:
- every number the baseline prints in <main> must also be printed by the reference (a missing governed number fails),
  except the baseline's decorative two-digit section ordinals (01, 02 …), which are presentation, not content;
- every number the reference prints that the baseline does not must be a governed value: a row value, derived value
  or identifier of a visual contract in `site-src/content/visuals/visual_design_contracts.json` (the baseline draws no
  chart and prints no contract row by rule P3-G02; the reference draws them at their canonical routes), or a number
  inside the governed content the loader handed the renderer for that page (the harness bundle — a bound record's
  period, population or summary that the reference composes where the baseline printed only a title; D2); axis tick
  labels of a drawn chart (SVG `<text class="lbl">`) are scale presentation, not content, and are excluded. A number
  the renderer formats differently from its governed value (rounding, truncation) is therefore caught.
Number normalisation is that of audit/tranche_c/checks/bilingual_invariance.py, so the same rules apply. Exit 1 on any
failure. This protects the loader against silent drift from the projections; it is not a design check.
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "audit/tranche_c/checks"))
import bilingual_invariance as BI  # noqa: E402

DECORATIVE = re.compile(r"^0\d$")
AXIS_LABEL = re.compile(r'<text class="lbl[^"]*"[^>]*>[^<]*</text>')


def governed_visual_numbers() -> set[str]:
    """Numbers a reference page may print beyond the baseline: visual-contract values and derived values, and the
    numeric fragments of governed source identifiers (a reference printed as a labelled reference is not a figure)."""
    text = (ROOT / "site-src/content/visuals/visual_design_contracts.json").read_text(encoding="utf-8")
    out = set()
    for x in re.findall(r"\d[\d,]*(?:\.\d+)?", text):
        v = x.replace(",", "").rstrip(".")
        if v:
            out.add(v)
            if re.fullmatch(r"\d+\.0", v):
                out.add(v[:-2])
    ids = " ".join(str(r.get("source_id") or "") for r in json.loads((ROOT / "site-src/content/sources/source_reference_map.json").read_text(encoding="utf-8")))
    tmp = ROOT / "design/reference/out/_bundle/.ids.html"
    tmp.write_text(f"<main>{ids}</main>", encoding="utf-8")
    out |= set(BI.nums(str(tmp)))
    tmp.unlink()
    return out


SENT = re.compile(r"(?<=[.؟?!:;])\s+")
INLINE_TAG = re.compile(r"</?(?:bdi|a|b|i|em|strong|span|time|button)\b[^>]*>")   # inline elements add no word break in rendered text
TAG = re.compile(r"<[^>]+>")
FRAMING_EXCEPTION = "UI-EVID-OPEN-THE-SOURCE-RECORD-HERE"   # not printed on a framing record (no source to open): a recorded exception


def main_text(path: Path) -> str:
    """The text of <main> as rendered (inline tags removed, block tags stripped, entities decoded, whitespace collapsed)."""
    import html as _html
    raw = path.read_text(encoding="utf-8")
    m = re.search(r"<main[^>]*>(.*)</main>", raw, re.S)
    text = TAG.sub(" ", INLINE_TAG.sub("", m.group(1) if m else raw))
    return re.sub(r"\s+", " ", _html.unescape(text)).strip()


SKIP_KEYS = {"href", "url", "route", "id", "cite_payload", "citation", "meta_description", "canonical_href", "data_href", "compare_href",
             "last_reviewed_iso", "hrefs", "ui_json", "readings_index_href", "parent_href", "mode", "family", "lang", "dir", "closure_state",
             "trace_state", "state", "series", "derived", "kind", "section_id", "order", "active", "other_lang", "edition"}


NUMBER_KEYS = {"id", "citation"}   # the page's own governed identifier and citation: their numbers may be printed as often as the composition needs (D6: the print-only provenance block)


def governed_strings(obj, out: set, key: str = "", min_len: int = 12) -> set:
    """Every governed string the renderer receives (the harness bundle), long enough to be a text block (or, with
    min_len 1, every governed string and value — the page's governed number set)."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k not in SKIP_KEYS or (min_len <= 1 and k in NUMBER_KEYS):
                governed_strings(v, out, k, min_len)
    elif isinstance(obj, list):
        for v in obj:
            governed_strings(v, out, key, min_len)
    elif isinstance(obj, str) and len(obj.strip()) >= min_len and not obj.startswith(("/", "http", "UI-", "SRC-", "CLM-", "VIS-", "RV-")):
        out.add(re.sub(r"\s+", " ", obj).strip())
    elif isinstance(obj, (int, float)) and not isinstance(obj, bool) and min_len <= 1:
        out.add(str(obj))
    return out


def main() -> int:
    argv = [a for a in sys.argv[1:] if not a.startswith("--")]
    text_mode = "--text" in sys.argv
    site = Path(argv[0] if argv else ROOT / "design/reference/out")
    governed = governed_visual_numbers()
    bad = 0
    if not (site / "en" / "index.html").exists():   # an empty or unbuilt site is a failure, never a pass
        print(f"CONTENT PARITY: FAIL (site not built: {site})")
        return 1
    for lang in ("en", "ar"):
        for page in sorted((site / lang).rglob("index.html")):
            rel = page.relative_to(site)
            base = ROOT / "dist" / rel
            if not base.exists():
                print("no baseline for", rel)
                bad += 1
                continue
            stripped = page.parent / ".stripped.html"
            stripped.write_text(AXIS_LABEL.sub("", page.read_text(encoding="utf-8")), encoding="utf-8")
            a, b = BI.nums(str(base)), BI.nums(str(stripped))
            stripped.unlink()
            bundle = site / "_bundle" / ((str(rel.parent).replace("\\", "/").split("/", 1)[1] if "/" in str(rel.parent) else "home").replace("/", "_") + f"__{lang}.json")
            if not bundle.exists():
                bundle = site / "_bundle" / f"home__{lang}.json"
            page_data = json.loads(bundle.read_text(encoding="utf-8"))["page"]
            tmp = page.parent / ".bundle.html"
            tmp.write_text("<main>" + " ".join(sorted(governed_strings(page_data, set(), min_len=1))) + "</main>", encoding="utf-8")
            page_governed = set(BI.nums(str(tmp)))
            tmp.unlink()
            missing = Counter({k: v for k, v in (a - b).items() if not DECORATIVE.match(k)})
            extra = Counter({k: v for k, v in (b - a).items() if k not in governed and k not in page_governed})
            if missing or extra:
                bad += 1
                print(f"DIFF {rel}: missing from reference {dict(missing)} · ungoverned in reference {dict(extra)}")
            if text_mode:
                # every governed string the baseline renders in <main> must be rendered by the reference too (text-block parity)
                gov = governed_strings(page_data, set())
                base_text, ref_text = main_text(base), main_text(page)
                def present(x: str) -> bool:
                    if x in ref_text:
                        return True
                    # a paced paragraph (Home, DEBT-008): every sentence present, in order, with objects interleaved
                    parts = [y.strip() for y in SENT.split(x) if y.strip()]
                    if len(parts) > 1 and all(y in ref_text for y in parts):
                        pos = [ref_text.index(y) for y in parts]
                        return pos == sorted(pos)
                    return False
                framing = page_data.get("closure_state") == "FRAMING_NO_FACT"
                framing_text = json.loads((ROOT / "site-src/content/content/interface_copy.json").read_text(encoding="utf-8"))
                framing_text = next((r.get(f"label_{lang}") for r in framing_text if r.get("ui_id") == FRAMING_EXCEPTION), "")
                lost = sorted(x for x in gov if x in base_text and not present(x) and not (framing and x == framing_text))
                if lost:
                    bad += 1
                    print(f"TEXT {rel}: {len(lost)} baseline sentence(s) not in the reference:")
                    for x in lost:
                        print("   -", x[:160])
    print(f"CONTENT PARITY: {'PASS' if not bad else 'FAIL'} ({bad} differing documents)")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
