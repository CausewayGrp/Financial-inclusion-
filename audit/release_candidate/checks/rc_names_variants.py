"""Exercise the RC-NAMES gate block on test strings and on the built site, without running the whole validator."""
import re, sys, json, html as _html
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]; DIST = ROOT / "dist"; C = ROOT / "site-src" / "content"
src = (ROOT / "scripts/validate.py").read_text(encoding="utf-8")
a = src.index("# RC-NAMES (owner note of 3 October 2026, 03:10"); b = src.index("# RC-B6 (Part B B6)")
block = src[a:b]
errors = []
g = {"re": re, "json": json, "_html": _html, "ROOT": ROOT, "DIST": DIST, "C": C, "errors": errors, "sys": sys}
exec(block, g)
print("patterns:", len(g["_rcn"]), "subjects:", len({x[0] for x in g["_rcn"]}))
print("site errors:", len(errors)); [print(" ", e) for e in errors[:40]]
tests = ["محفظة جيب", "وجوالي", "WeCash", "Al-Buraq", "We&nbsp;Cash", "We\nCash", "We <b>Cash</b>", "ويكاش", "بفلوسك", "ووي كاش",
         "Al Dawli Money", "Dawli Money", "Al Mutakamila", "Riyal Mobile", "Floosk", "Jawwali", "Electronic Riyal", "e-Riyal",
         "الريال الإلكتروني", "وي کاش", "We%20Cash", "We\\u0020Cash", "SabaCash", "YemenWallet", "البراق للصرافة", "قطنان",
         "منشأة الابرق للصرافة", "شركة احمد العامري", "Saddam Express", "صدام اكسبرس", "al-buraq exchange", "Al Buraq",
         "Al-Shamil Exchange branch", "Bin Amin Ghannam Exchange branch", "Al-Thawr Exchange branch", "بن دابي", "Ghannam",
         # must NOT match (ordinary vocabulary)
         "الخدمات المتكاملة", "الاتحاد الأوروبي", "التيار الكهربائي", "mobile money accounts", "cash transfers", "Saba Islamic Bank",
         "الشامل", "صندوق النقد", "money transfer", "the rial", "electronic money", "جيب المستخدم", "Yemen's wallets", "Abu Dhabi"]
for s in tests:
    n = g["_rcn_norm"](s); ne = g["_rcn_en_strip"](n)
    hits = sorted({i for i, x, l, nds in g["_rcn"] if any(d in (ne if l == "en" else n) for d in nds) and x.search(ne if l == "en" else n)})
    print(f"{s!r:40} -> {hits}")
