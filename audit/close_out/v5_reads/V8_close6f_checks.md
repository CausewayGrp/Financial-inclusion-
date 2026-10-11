# V8 CLOSE-6F checks (11 October 2026)

Checks run by the Team Lead for the Stage A final instruction v5, section 7. Read-only unless stated.

## 7a
- **CR-11** is already CLOSED on main (register: "CLOSE-2B, PR #30 at `f71a327d`: ReliefWeb locator"). Line dropped.
- **SRC-OECD-YEM-RESILIENCE-001**: the PDF is the read text (V6 §2; SHA-256 4ae2f699…). The DOI landing page and the chapter
  HTML return a Cloudflare challenge (HTTP 403), so the chapter HTML is added as the locator the 29_OECD_BENCHMARKS facts
  already cite, not as a page read here.
- **EXT-23 / SRC-CBY-POS-2026-01**: the instruction's note "values identical" is not true (V6 §1.3: four governorate cells
  differ). Recorded as a challenge; the original stays primary. https://cby-ye.com/pages/33 fetched 11 October 2026 (HTTP 200,
  35,398 bytes): the latest month listed is June 2026, so the July–September card stays open.

## 7b
The instruction names "nine" cards and lists eight (REF-REG-002, 004, 005, 007, 008, 009, 010, 011). Each maps by its URL to
a source card on /data/, and each carries why_it_matters and does_not_establish in English and Arabic, in the Master and
on the built page (dist/en/data and dist/ar/data):

| Rule | Source card | EN why / does not | AR why / does not | On the page EN / AR |
|---|---|---|---|---|
| REF-REG-002 | SRC-CBY-EKYC-2023 | yes / yes | yes / yes | yes / yes |
| REF-REG-004 | SRC-CBY-CIRC-01-2024 | yes / yes | yes / yes | yes / yes |
| REF-REG-005 | SRC-CBY-DEC-19-2024 | yes / yes | yes / yes | yes / yes |
| REF-REG-007 | SRC-CBY-CIRC-02-2025 | yes / yes | yes / yes | yes / yes |
| REF-REG-008 | SRC-CBY-CIRC-03-2025 | yes / yes | yes / yes | yes / yes |
| REF-REG-009 | SRC-CBY-CIRC-04-2025 | yes / yes | yes / yes | yes / yes |
| REF-REG-010 | SRC-CBY-DEC-07-2026 | yes / yes | yes / yes | yes / yes |
| REF-REG-011 | SRC-CBY-CIRC-01-2026 | yes / yes | yes / yes | yes / yes |

The SAR cross-rate settings: 31 August 2025 found as a decision to keep the announced rate (V3 §F, news/870: "the board kept",
not "set"); 13 February 2026 not found. No located primary for a setting: RESERVED with its trigger (W3f, PR-6). The
chronology rule is unchanged; no event is added.

## 7c
- **2013 Enterprise Survey collateral**: 281.5% is right; 284.3% is the Medium-size column (V4). No change.
- **"not published by any source"**: no such state is held for the OECD assertions (Master searched); nothing to correct.
- **master_principles.json** carried 605 and 1,114 (00_MASTER "Key evidence", rows 33–34). CLOSE-6F replaces both values
  with UNVERIFIED__DO_NOT_PROJECT there and in 12_VISUAL_PREVIEWS; the figures stay only in 29_OECD_BENCHMARKS
  (OECD-YEM-006/007), which no projection reads (gate CO-G02).
