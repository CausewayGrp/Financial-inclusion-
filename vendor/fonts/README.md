# Vendored fonts — IBM Plex Sans and IBM Plex Sans Arabic

The product's required typefaces, carried in the repository so that Design and Code need no network access for them.
Nothing in the reference build (`dist/`) loads these files; the Design reference implementation and the production
runtime self-host them from here.

| Folder | Source package | Files | Licence |
|---|---|---|---|
| `ibm-plex-sans/` | npm `@ibm/plex-sans@1.1.0` — `fonts/complete/woff2/` (16 files) and `LICENSE.txt` | Thin … Bold, with italics, and Text | SIL Open Font License 1.1, Reserved Font Name "Plex" |
| `ibm-plex-sans-arabic/` | npm `@ibm/plex-sans-arabic@1.1.0` — `fonts/complete/woff2/` (8 files) and `LICENSE.txt` | Thin … Bold, and Text | SIL Open Font License 1.1, Reserved Font Name "Plex" |

Provenance (26 September 2026): npm `dist.integrity`
`sha512-WPgvO6Yfj2w5YbhyAr1tv95RUz4LRJlqN+CmYvBglabXteufP1D1E9BABMde+ZIKdRbFJDoKF5eQzfhpnbgZcQ==` (`@ibm/plex-sans@1.1.0`) and
`sha512-u8wIS6szLAOFvlBjCFZmtpKIqbhuIuniG2N0J+sio8vV6INH58hP0t0QNYrSl9SZtCv2Fwb4oQGuZJY3kJ4+QA==` (`@ibm/plex-sans-arabic@1.1.0`).
The files are copied unchanged from those packages; their hashes are in `SHA256SUMS.txt`.

Rules:

- Ship `LICENSE.txt` with the fonts wherever they are served or packaged.
- Use the files as shipped. Making your own subset modifies a font whose licence reserves the name "Plex"; IBM publishes
  its own pre-split Latin subsets of IBM Plex Sans in the same npm package (`fonts/split/woff2/`), not vendored here;
  the steward adds them on request, unchanged and with provenance, like the files above. A self-made subset is an owner
  decision, not a design or engineering default.
- No font CDN; no other typeface (the rule is in `handoff/CLAUDE_DESIGN_MASTER_PROMPT.md` §8).
