# Vendored fonts — IBM Plex Sans, IBM Plex Sans Arabic and the two display faces

The product's required typefaces, carried in the repository so that Design and Code need no network access for them.
Since EAD-01 the production build self-hosts them from here: `scripts/build.py` copies the faces the stylesheet
declares — Regular, Medium and SemiBold of each body family, and since OD-1018 one display face per edition — with each
family's licence, into `dist/assets/fonts/`, and each page preloads Regular, SemiBold and the display face of its own
language. The other files stay vendored and unshipped rather than served and never requested.

| Folder | Source package | Files | Licence |
|---|---|---|---|
| `ibm-plex-sans/` | npm `@ibm/plex-sans@1.1.0` — `fonts/complete/woff2/` (16 files) and `LICENSE.txt` | Thin … Bold, with italics, and Text | SIL Open Font License 1.1, Reserved Font Name "Plex" |
| `ibm-plex-sans-arabic/` | npm `@ibm/plex-sans-arabic@1.1.0` — `fonts/complete/woff2/` (8 files) and `LICENSE.txt` | Thin … Bold, and Text | SIL Open Font License 1.1, Reserved Font Name "Plex" |
| `ibm-plex-serif/` | npm `@ibm/plex-serif@2.0.0` (2 February 2026) — `fonts/split/woff2/IBMPlexSerif-SemiBold-Latin1.woff2` (IBM's own Latin-1 split, unchanged) and `LICENSE.txt` | SemiBold 600, Latin-1 | SIL Open Font License 1.1, Reserved Font Name "Plex" |
| `noto-naskh-arabic/` | notofonts/arabic release `NotoNaskhArabic-v2.021` (16 January 2026) — `NotoNaskhArabic/unhinted/ttf/NotoNaskhArabic-SemiBold.ttf`, subset by `scripts/font_subset.py`, and the release's `OFL.txt` | SemiBold 600, Arabic subset | SIL Open Font License 1.1, no Reserved Font Name |

Provenance (26 September 2026): npm `dist.integrity`
`sha512-WPgvO6Yfj2w5YbhyAr1tv95RUz4LRJlqN+CmYvBglabXteufP1D1E9BABMde+ZIKdRbFJDoKF5eQzfhpnbgZcQ==` (`@ibm/plex-sans@1.1.0`) and
`sha512-u8wIS6szLAOFvlBjCFZmtpKIqbhuIuniG2N0J+sio8vV6INH58hP0t0QNYrSl9SZtCv2Fwb4oQGuZJY3kJ4+QA==` (`@ibm/plex-sans-arabic@1.1.0`).
The files are copied unchanged from those packages; their hashes are in `SHA256SUMS.txt`.

## The display faces (owner decision OD-1018 D2, 18 October 2026)

Titles and section headings take one display face per edition, loaded only by that edition: Noto Naskh Arabic 600 in
Arabic, IBM Plex Serif 600 in English. Body, controls and figures stay in IBM Plex Sans and IBM Plex Sans Arabic
(figures in Western tabular digits from a face the page already loads); at most four font files per page.

- IBM Plex Serif (18 October 2026): npm `@ibm/plex-serif@2.0.0`, `dist.integrity`
  `sha512-xVu9JsC18tBoQF2M6fofpsWrHj5a94saxlOZbYmXoC0E3UfjgS1JlibgrnaUJjnkLlEyCpMgI2PdhkDxijw0gA==`; the Latin-1 split
  is copied unchanged (24,016 bytes, SHA-256 `c1487f9484cc8f04c656f7f074724154a04fdefd2ce7ffeab653f517bb4d366d`).
- Noto Naskh Arabic (18 October 2026): `NotoNaskhArabic-v2.021.zip` from the notofonts/arabic release of that name,
  SHA-256 `6c050ab9bd087d69b733c505a7576e60c528c2f33cd7b91005a5bd7da4514032`. The subset keeps the Arabic letters
  (U+0621–063A, U+0641–064A), the marks (U+064B–0655, U+0670), Arabic punctuation and digits (U+060C, U+061B, U+061C,
  U+061F, U+0660–066D, U+06D4), U+0640, U+0671, the bidi joiners and marks (U+200C–200F) and the space, no-break space,
  exclamation mark, comma, full stop, colon and guillemets the release covers — no Latin letter and no Western digit, so
  a source name, a year or a figure inside an Arabic title falls back to IBM Plex Sans Arabic 600, the body face already
  on the page. Every layout feature of the kept glyphs is kept; the head table keeps the release's timestamp.
  Result: 12,616 bytes, SHA-256 `e0f9f65db3447041cd631fc46e4f807d2fc263685317727be4af381a198e45dd`.
- The recipe is `scripts/font_subset.py` on fontTools 4.67.0 and brotli 1.2.0 (it refuses other versions):
  `python3 scripts/font_subset.py --naskh-zip NotoNaskhArabic-v2.021.zip` rebuilds the subset byte for byte, and
  `--check [--naskh-zip …]` confirms the record and, with the zip, the rebuild. The record
  `display_coverage.json` holds both display files' hashes and the code points their cmaps cover; the standard-library
  gate `scripts/tests/test_display_font_coverage.py` checks every generated heading of both editions against it.
- Reconciliation with draft PR #63 (the Folio proof, superseded by OD-1018): its `design/exploration/v3/README.md` described
  a Noto Naskh Arabic 700 subset that kept Latin (U+0020–007E, U+00A0–00FF; 23 KB) and IBM Plex Serif from
  `@ibm/plex-serif@1.1.0`. The file that proof actually used was the SemiBold 600 subset without Latin (13,124 bytes);
  this folder rebuilds that design from the current upstream release (v2.021, the same version) with the recipe above,
  and takes Plex Serif from the current release, 2.0.0. The README of #63 is left as its branch's lineage.

Rules:

- Ship each family's licence with the fonts wherever they are served or packaged.
- Use the Plex files as shipped. Making your own subset modifies a font whose licence reserves the name "Plex"; IBM
  publishes its own pre-split subsets in the same npm packages (`fonts/split/woff2/`), and the steward adds them on
  request, unchanged and with provenance, like the files above. A self-made subset is an owner decision, not a design or
  engineering default: the Noto Naskh Arabic subset is one (OD-1018 D2), allowed by its licence, which reserves no name.
- No font CDN; no other typeface than the four families above (the rule is in `handoff/CLAUDE_DESIGN_MASTER_PROMPT.md`
  §8, extended by OD-1018).
