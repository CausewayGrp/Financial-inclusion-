# D1 canvas exploration — proposition composers

What this folder is: the sources that regenerate the D1 design propositions on the Claude Design canvas
"YFIE D1 Thesis Exploration" (https://claude.ai/artifact/XmHAYbp2cwfU9o9eLjNiVx). Each proposition module under
`boards/` (`t1.py` Register, `t2.py` Argument, `t3.py` Strata, `t4.py` Instrument) gives a stylesheet and three
compositions (Home, `/evidence/CLM-003/`, `/readings/same-year-different-number/`). `boards/common.py` supplies the
governed text — read from the neutral harness bundle, never retyped — plus the fonts, the unmodified logo and the canvas
file format. `proto_common.py` holds the shared RV-CWR-001 drawing helpers (each proposition draws the contract in its
own visual language, inside the contract); `proto_shell.py` the mechanics the browser suites need (skip link, search
dialog, utilities) and the responsive-rule doubler that lets a fixed-width artboard show the narrow form.

What it is not: not the reference implementation, not a design system, not an accepted decision. Everything here is a
proposition under test; the record of what is proven is `design/01_FOUNDATIONS.md`, and the decisions are in
`design/00_DESIGN_README.md` §9. Outputs are git-ignored (`out/`).

Regenerate:

```bash
python3 design/reference/build.py --renderer neutral        # writes design/reference/out/_bundle/<route>__<lang>.json
python3 design/exploration/d1_canvas/build_boards.py         # all propositions; or: build_boards.py t4
python3 design/exploration/d1_canvas/fold.py                 # first and second screens of every twin → out/fold/
python3 design/exploration/d1_canvas/crops.py                # screenshot-misuse crops → out/crops/
```

After the reference implementation is built and checked (`python3 design/reference/build.py && python3
design/reference/check_trio.py --shots`), `python3 design/exploration/d1_canvas/reference_boards.py` adds row R to the
canvas: every built page of the trio as an artboard beside the propositions, for the drift review. `inspect_widths.py
t4` renders a proposition at 320–1440 px in both languages; `tiles.py` cuts full-page renders into readable tiles;
`LENS_BRIEF.md` is the brief the nine critique lenses received; `review/` holds their reports, the independent final
review and the second independent pass as received (working material kept for the record; the adjudication is in
`design/01_FOUNDATIONS.md` §3 and §6).

`build_boards.py` writes, for every proposition × surface × language × size (1440 and 390 px): a plain HTML twin
(`out/local/`, rendered in Chromium to measure height and to screenshot into `out/shots/`), the canvas artboard
(`out/project/project/<name>.dc.html`) and the canvas index (`out/project/project/canvas.json`). The canvas is published
from `out/project/` (root) with `project/canvas.json` as the page and the artboards as files. Renders are proof for
critique; they are not authority.
