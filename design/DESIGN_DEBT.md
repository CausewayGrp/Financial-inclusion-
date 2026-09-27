# Design-debt register

Every deliberate temporary compromise. Entries are closed, never deleted. Fields: ID · temporary decision · why ·
surfaces · user impact · intended behaviour · Code action · priority · blocks D7 / blocks release / neither · status.

| ID | Temporary decision | Why | Surfaces | User impact | Intended behaviour | Code action | Priority | Blocks | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEBT-001 | D0 authority hashes (Master, Page Specs) verified only against `SHA256SUMS.txt` and inventory `generated_from`; §8 commands NOT RUN; manifest/checksums not regenerated | Design environment has no shell, cannot fetch the binary Master or the full Page Specs file | Process only | None public | Steward runs `checksums.py --check` and the full §8 suite on the landed D0 branch and records output here | None | High | Blocks D0 exit until run | CLOSED 2026-09-27 by the steward on `design/d0-orientation`: direct SHA-256 of the Master `17db032b…038690b` and of Page Specs `d4574804…824b69aa` match; checksums 761 current; projection check pass; build 288 HTML; literal closure 12,760 / 0 unresolved; validator pass; public tools 25/26 (1 not applicable: no Compare ID contains "+"); viewport 168/168; bilingual invariance 0 of 143; architecture diagrams, repository manifest and handoff inventory current |
| DEBT-002 | No reference implementation exists | D0 forbids design work | All routes | None yet | `design/reference/` from D1; 288 documents by D4 | Inherits `design/reference/` at D7 | High | Blocks D7 | OPEN |
