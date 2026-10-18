# W4F performance before/after (charter P6): cold bytes on the wire at 390, both editions, t1 (main 8c78fa0e) → G2 (this build)

Measured by design/evidence/v2/g0_measure.py (cold_bytes, gzip as _headers declares). Fonts: 3 files per edition before and after; no font added, none removed (the Medium weight stays, see the design record 6). The only persistent bytes added are stylesheet rules; the JavaScript and the images are unchanged.

| Route | AR cold bytes t1 → G2 | EN cold bytes t1 → G2 | delta (AR) | font files | font bytes (AR) |
|---|---|---|---|---|---|
| / | 267 → 267 KB | 239 → 239 KB | +0.7 KB | 3 | 220 KB |
| /payments/ | 277 → 278 KB | 248 → 248 KB | +0.7 KB | 3 | 220 KB |
| /evidence/CLM-001/ | 267 → 268 KB | 239 → 239 KB | +0.7 KB | 3 | 220 KB |
| /data/ | 323 → 324 KB | 291 → 292 KB | +0.7 KB | 3 | 220 KB |
| /readings/how-money-reaches-households/ | 276 → 277 KB | 246 → 247 KB | +0.7 KB | 3 | 220 KB |
| /measurement/ | 286 → 287 KB | 253 → 254 KB | +0.7 KB | 3 | 220 KB |

Throttled profile (scripts/performance_budget.py: 150 ms RTT, 1.6 Mbit/s down, CPU ×4; perf_g2.json): first contentful paint 1.3–1.9 s on Home and Explore in both editions, the heaviest page (/data/ AR) 2.3 s; every family within the recorded release-candidate budget. Speed on Yemeni networks stays release-stage evidence (charter P6).
