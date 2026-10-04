#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The currentness re-run, as one command (Part B B14 e).

  python3 scripts/currentness_rerun.py            # read every watch point and print the dated result
  python3 scripts/currentness_rerun.py --append   # also append the result to audit/FINAL_CURRENTNESS_CUTOFF.md
  python3 scripts/currentness_rerun.py --strict   # exit 1 if any watch point shows something newer than the Master

Reads the watch points of `audit/FINAL_CURRENTNESS_CUTOFF.md` in their originals and compares each with what the
Production Master holds (through its projections under `site-src/content/`):

- CBY-Aden monthly POS releases (Arabic payments page): the latest month listed against the latest month held.
- CBY-Aden Governor's decisions (news listing): the highest decision number of the current year against the highest
  held.
- CBY-Aden licensing and regulation page: every file it links, against the locators the source library holds. This
  covers the licensed-bank list, the exchange and remittance roster, decisions and circulars.
- World Bank FMIIP (P180708): the latest Implementation Status and Results Report against the latest held.
- Global Findex, Yemen: the latest year with an account-ownership value against the wave held.
- Hosts that refuse automated requests or were down at the last check (IMF, Remittance Prices Worldwide, CBY Sana'a):
  each is requested and reported. A refusal is "check by hand", never "nothing newer".

Nothing is changed: a newer item becomes a Master transaction after it is read (`CONTRIBUTING.md`). A "no newer item"
result covers only the pages named. Run it at the release date (docs/RELEASE_RUNBOOK.md) and whenever an edition is
re-dated.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import date
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
C = ROOT / "site-src" / "content"
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
MONTHS_AR = {"يناير": 1, "فبراير": 2, "مارس": 3, "أبريل": 4, "ابريل": 4, "مايو": 5, "يونيو": 6, "يوليو": 7, "أغسطس": 8,
             "اغسطس": 8, "سبتمبر": 9, "أكتوبر": 10, "اكتوبر": 10, "نوفمبر": 11, "ديسمبر": 12}


def fetch(url: str, timeout: int = 60) -> tuple[int, str]:
    r = subprocess.run(["curl", "-sS", "-L", "--max-time", str(timeout), "-A", UA, "-w", "\n%{http_code}", url],
                       capture_output=True, text=True)
    body, _, code = r.stdout.rpartition("\n")
    return (int(code) if code.isdigit() else 0), body


def links(html: str) -> list[tuple[str, str]]:
    return [(h, unescape(re.sub(r"<[^>]+>", "", t)).strip()) for h, t in re.findall(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', html, re.S)]


def held_locators() -> set[str]:
    out = set()
    for s in json.loads((C / "sources" / "source_library.json").read_text(encoding="utf-8")):
        out.add(str(s.get("primary_url") or ""))
        extra = s.get("additional_urls")
        if extra:
            try:
                out.update(json.loads(extra))
            except (ValueError, TypeError):
                out.update(x.strip() for x in str(extra).split(";"))
    return {u for u in out if u}


def source_ids() -> list[str]:
    return [s["source_id"] for s in json.loads((C / "sources" / "source_library.json").read_text(encoding="utf-8"))]


def row(point, url, held, found, result, note=""):
    return {"point": point, "url": url, "held": held, "found": found, "result": result, "note": note}


def pos(year: int) -> dict:
    url = "https://cby-ye.com/pages/33"
    code, html = fetch(url)
    held = max((s[len("SRC-CBY-POS-"):] for s in source_ids() if re.fullmatch(r"SRC-CBY-POS-\d{4}-\d{2}", s)), default="none")
    if code != 200:
        return row("CBY-Aden monthly POS releases", url, held, f"HTTP {code}", "CHECK BY HAND")
    months = []
    for _, t in links(html):
        m = re.search(r"نقاط البيع الشهرية\s*\((\S+)\s+(\d{4})\)", t)
        if m and m.group(1) in MONTHS_AR:
            months.append(f"{m.group(2)}-{MONTHS_AR[m.group(1)]:02d}")
    found = max(months, default="none")
    return row("CBY-Aden monthly POS releases", url, held, found, "NEWER — read and transact" if found > held else "SAME")


def decisions(year: int) -> dict:
    url = "https://cby-ye.com/news"
    code, html = fetch(url)
    held = max((int(m.group(1)) for s in source_ids() for m in [re.fullmatch(rf"SRC-CBY-ENF-(\d+)-{year}", s)] if m), default=0)
    if code != 200:
        return row(f"CBY-Aden Governor's decisions ({year})", url, held, f"HTTP {code}", "CHECK BY HAND")
    nums = [int(m.group(1)) for _, t in links(html) for m in [re.search(r"قرار رقم\s*\(?(\d+)\)?", t)] if m and "إيقاف" in t]
    found = max(nums, default=0)
    return row(f"CBY-Aden Governor's enforcement decisions ({year})", url, f"No. {held}", f"No. {found} (latest listed)",
               "NEWER — read and transact" if found > held else "SAME",
               "Only the first page of the news listing is read; it covers the latest ten items.")


def licensing() -> dict:
    url = "https://cby-ye.com/pages/14"
    code, html = fetch(url)
    if code != 200:
        return row("CBY-Aden licensing and regulation page", url, "", f"HTTP {code}", "CHECK BY HAND")
    held = held_locators()
    files = [(h, t) for h, t in links(html) if "/files/" in h]
    missing = [(h, t) for h, t in files if not any(h.rsplit("/", 1)[-1] in u for u in held)]
    found = f"{len(files)} files linked; {len(missing)} not held"
    note = "; ".join(f"«{t}» ({h.rsplit('/', 1)[-1]})" for h, t in missing)
    return row("CBY-Aden licensing and regulation page (bank list, roster, decisions, circulars)", url,
               f"{len(files) - len(missing)} of them held", found, "NOT HELD — decide" if missing else "SAME", note)


def fmiip() -> dict:
    url = "https://search.worldbank.org/api/v3/wds?format=json&proid=P180708&fl=docdt,docty,display_title&rows=50"
    code, body = fetch(url)
    held = "ISR seq. 2, 2026-04-08 (SRC-WB-FMIIP-ISR2-2026-001)"
    if code != 200:
        return row("World Bank FMIIP (P180708) status reports", url, held, f"HTTP {code}", "CHECK BY HAND")
    docs = json.loads(body).get("documents", {})
    isr = sorted((v.get("docdt", "")[:10] for k, v in docs.items() if k != "facets" and "Implementation Status" in str(v.get("docty"))), reverse=True)
    found = f"{len(isr)} reports; latest {isr[0] if isr else 'none'}"
    return row("World Bank FMIIP (P180708) status reports", url, held, found,
               "NEWER — read and transact" if isr and isr[0] > "2026-04-08" else "SAME")


def findex() -> dict:
    url = "https://api.worldbank.org/v2/country/YEM/indicator/FX.OWN.TOTL.ZS?format=json&per_page=60"
    code, body = fetch(url)
    held = "2021 wave, data year 2022 (fieldwork 2022-11-07 to 2023-01-09)"
    if code != 200:
        return row("Global Findex — Yemen account ownership", url, held, f"HTTP {code}", "CHECK BY HAND")
    vals = [x["date"] for x in (json.loads(body)[1] or []) if x.get("value") is not None]
    latest = max(vals, default="none")
    return row("Global Findex — Yemen account ownership", url, held, f"latest year with a value: {latest}",
               "NEWER — read and transact" if latest != "none" and latest > "2022" else "SAME")


def refused() -> list[dict]:
    out = []
    for point, url, held in [
        ("IMF Staff-Monitored Program (Yemen)", "https://www.imf.org/en/news/articles/2026/07/16/pr26249-yemen-imf-reaches-sla-on-new-staff-monitored-program",
         "staff-level agreement, 16 July 2026; no approval notice held"),
        ("Remittance Prices Worldwide — Saudi Arabia to Yemen", "https://remittanceprices.worldbank.org/corridor/Saudi%20Arabia/Yemen", "2025 Q3"),
        ("CBY Sana'a annual report 2015 host", "http://centralbank.gov.ye/App_Upload/Ann_rep2015AR.pdf", "locator held; 503 on 3 October 2026"),
    ]:
        code, _ = fetch(url, 45)
        out.append(row(point, url, held, f"HTTP {code}", "SAME (reachable)" if code == 200 and "Sana" in point else "CHECK BY HAND",
                       "" if code == 200 else "The host refuses automated requests or is unavailable; a person checks it with a browser."))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--append", action="store_true")
    ap.add_argument("--strict", action="store_true")
    args = ap.parse_args()
    today = date.today()
    rows = [pos(today.year), decisions(today.year), licensing(), fmiip(), findex()] + refused()
    lines = [f"## Currentness re-run — {today.isoformat()} (`scripts/currentness_rerun.py`; appended)", "",
             "| Watch point | Held in the Master | Found | Result |", "|---|---|---|---|"]
    for r in rows:
        lines.append(f"| {r['point']} ([page]({r['url']})) | {r['held']} | {r['found']} | {r['result']} |")
    notes = [f"- {r['point']}: {r['note']}" for r in rows if r["note"]]
    if notes:
        lines += ["", *notes]
    lines += ["", "A result covers only the page named; \"CHECK BY HAND\" is not \"nothing newer\". A newer item enters the Master",
              "only through a transaction after it is read in its original."]
    text = "\n".join(lines)
    print(text)
    if args.append:
        p = ROOT / "audit" / "FINAL_CURRENTNESS_CUTOFF.md"
        p.write_text(p.read_text(encoding="utf-8").rstrip("\n") + "\n\n" + text + "\n", encoding="utf-8")
    newer = [r for r in rows if r["result"].startswith("NEWER")]
    return 1 if (args.strict and newer) else 0


if __name__ == "__main__":
    raise SystemExit(main())
