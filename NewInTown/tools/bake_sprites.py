# -*- coding: utf-8 -*-
"""Pre-render every framed character sprite to disk.

WHY THIS EXISTS
---------------
framed_sprite() builds a sprite at runtime as a chain of image
manipulators: Crop -> Composite -> Flip -> FactorScale. Ren'Py caches
EVERY LINK of that chain separately (each one's load() calls
cache.get() on its child), so a single MC sketch pose occupies the
2048x2048 source, the crop, the composite AND the final sprite at once
- 12.6 million pixels to display 0.7 million. The default cache holds
about 105 million pixels (config.image_cache_size_mb = 400), so scene
A01 alone wanted 69% of it for eight sprites. Past the limit Ren'Py
evicts images that are still on screen and re-decodes them the next
frame, which shows up as the whole cast flickering.

Baking collapses each chain to one small PNG, so a pose costs only its
final size - roughly 20x less - and nothing has to be decoded or
rescaled while the game is running.

RUN IT WHENEVER ART OR FRAMING CHANGES
--------------------------------------
    python tools/bake_sprites.py

It reads CHAR_FRAME and SPRITE_KNEE_H straight out of
SpriteFraming.rpy and the art tables out of each character file, so
this stays in step with the game on its own. Output goes to
game/images/Characters/_framed/ and is safe to delete: framed_sprite()
falls back to building the chain live when a baked file is missing.
"""
import io, os, re, sys
from PIL import Image, ImageOps

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GAME = os.path.join(ROOT, 'game')
OUT = os.path.join(GAME, 'images', 'Characters', '_framed')

sf = io.open(os.path.join(GAME, 'Scripts/Characters/SpriteFraming.rpy'), encoding='utf-8').read()
KNEE_H = int(re.search(r'SPRITE_KNEE_H\s*=\s*(\d+)', sf).group(1))
BUTTON_H = int(re.search(r'BUTTON_H\s*=\s*(\d+)', sf).group(1))

FRAME = {}
for m in re.finditer(r'"(\w+)":\s*\(\(\s*(\d+),\s*(\d+)\),\s*(\d+),\s*(\d+),\s*(\d+),\s*(\d+),\s*([\d.]+),\s*(True|False)\)', sf):
    FRAME[m.group(1)] = ((int(m.group(2)), int(m.group(3))), int(m.group(4)), int(m.group(5)),
                         int(m.group(6)), int(m.group(7)), float(m.group(8)), m.group(9) == 'True')


def bake(char, rel, height=None):
    """Same maths as framed_sprite()/button_sprite(), done once."""
    (cw, chh), head, knee, cut, cx, scale, flip = FRAME[char]
    src = Image.open(os.path.join(GAME, rel)).convert('RGBA')
    if src.size != (cw, chh):
        return None, 'canvas is %dx%d, CHAR_FRAME says %dx%d' % (src.size + (cw, chh))
    fullh = knee - head
    img = src.crop((0, head, cw, head + (cut - head)))
    half = int(max(cx, cw - cx))
    pad = Image.new('RGBA', (half * 2, fullh), (0, 0, 0, 0))
    pad.alpha_composite(img, (int(half - cx), 0))
    if flip:
        pad = ImageOps.mirror(pad)
    zoom = (height / float(fullh)) if height else (KNEE_H * scale) / float(fullh)
    return pad.resize((int(pad.width * zoom), int(pad.height * zoom)), Image.LANCZOS), None


def table(text, name):
    m = re.search(r'%s\s*=\s*\{(.*?)\n    \}' % name, text, re.S)
    out = []
    if not m:
        return out
    for line in m.group(1).splitlines():
        line = line.strip()
        if line.startswith('#'):
            continue
        kv = re.match(r'"([a-z_]+)":\s*"([^"]+)"', line)
        if kv:
            out.append(kv.group(2))
    return out


# Collect (frame row, source path) pairs from every character file.
jobs = set()
for f in sorted(os.listdir(os.path.join(GAME, 'Scripts/Characters'))):
    if not f.endswith('.rpy'):
        continue
    t = io.open(os.path.join(GAME, 'Scripts/Characters', f), encoding='utf-8').read()
    base = f[:-4]
    for rel in table(t, base + '_pose_art'):
        jobs.add((base, rel))
    for rel in table(t, base + '_sketch_art'):
        jobs.add((base + '_SK', rel))
    m = re.search(r'%s_default_art\s*=\s*"([^"]+)"' % base, t)
    if m:
        jobs.add((base, m.group(1)))

if not os.path.isdir(OUT):
    os.makedirs(OUT)

made = skipped = 0
before = after = 0
for char, rel in sorted(jobs):
    if char not in FRAME:
        print('  SKIP %-12s no CHAR_FRAME row  (%s)' % (char, rel))
        skipped += 1
        continue
    stem = os.path.splitext(os.path.basename(rel))[0]
    stage = None
    for tag, height in (('', None), ('_btn', BUTTON_H)):
        im, err = bake(char, rel, height)
        if im is None:
            print('  SKIP %-12s %s: %s' % (char, stem, err))
            skipped += 1
            continue
        if not tag:
            stage = im.size
        dst = os.path.join(OUT, '%s__%s%s.png' % (char, stem, tag))
        im.save(dst, optimize=True)
        made += 1
    if stage is None:
        continue
    (cw, chh), head, knee, cut, cx, scale, flip = FRAME[char]
    half = max(cx, cw - cx)
    before += cw * chh + cw * (cut - head) + (2 * half) * (knee - head) * (2 if flip else 1)
    after += stage[0] * stage[1]
    print('  %-12s %-44s -> %dx%d stage' % (char, stem, stage[0], stage[1]))

print()
print('baked %d file(s), %d skipped, into %s' % (made, skipped, os.path.relpath(OUT, ROOT)))
if before:
    print('cache cost of these sprites: %.1fM px -> %.1fM px  (%.0fx smaller)'
          % (before / 1e6, after / 1e6, float(before) / after))
