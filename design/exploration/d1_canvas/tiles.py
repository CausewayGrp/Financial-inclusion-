# -*- coding: utf-8 -*-
"""Cut every full-page render in out/shots/ into tiles a reviewer can read (out/tiles/<name>-<i>.png)."""
import os
from pathlib import Path
from PIL import Image
HERE = Path(__file__).resolve().parent
SHOTS, TILES = HERE / "out" / "shots", HERE / "out" / "tiles"
TILES.mkdir(parents=True, exist_ok=True)
STEP = 1400
n = 0
for png in sorted(SHOTS.glob("*.png")):
    im = Image.open(png); w, h = im.size
    for i, y in enumerate(range(0, h, STEP)):
        im.crop((0, y, w, min(y + STEP, h))).save(TILES / f"{png.stem}-{i+1}.png"); n += 1
print(f"{n} tiles in {TILES}")
