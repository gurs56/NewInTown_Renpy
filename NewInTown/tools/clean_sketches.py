# -*- coding: utf-8 -*-
"""Prepare a folder of sketch scans for use as in-game stand-in sprites.

The artist's roughs arrive in two shapes, and both need work before Ren'Py
can draw them next to finished art:

  --key-white     The scan is flattened onto an opaque white page (MC's
                  batch). Drawn as-is it would put a white box on the
                  stage. The page is keyed out to transparency by flood
                  filling white inwards from the canvas border, so white
                  ENCLOSED by the drawing - an unfilled hand, teeth - is
                  kept. On by default when the file has no transparency.

  --strip-labels  The pose name is handwritten beside the head (Ms. Lopez
                  and Amber's batches). It never touches the drawing, so
                  it survives as its own ink component: anything that is
                  not the figure and finishes above --label-zone is
                  handwriting. Off by default - MC's batch has no labels,
                  and running this on it would eat the motion marks over
                  his head in Laughing.

  --align         The scans are not drawn on a consistent mark. Across
                  Amber's nine the hip centre wanders 375px, which would
                  make her jump sideways every time the pose changed.
                  `x` (default) puts the hip centre on the canvas centre
                  line; `xy` also puts the top of the head on --head-y;
                  `none` leaves the art where it was drawn.
                  Use plain `x` when a pose legitimately changes the
                  silhouette's height - MC's hair stands up in Worried,
                  and aligning head-tops would shove that whole drawing
                  35px down.

After this, one CHAR_FRAME row in SpriteFraming.rpy describes every pose of
that character.

  python tools/clean_sketches.py game/images/Characters/MC 1881
  python tools/clean_sketches.py game/images/Characters/Amber 1552 --strip-labels --align xy

The second argument is head-top to knee in source pixels - the same number
that goes in the character's CHAR_FRAME row. Cleaned copies are written to
<char-folder>/SK/; the scans themselves are never touched.
"""
import argparse, glob, os
import numpy as np
from scipy import ndimage
from PIL import Image

ap = argparse.ArgumentParser()
ap.add_argument('folder')
ap.add_argument('knee_span', type=int, help='head-top to knee, in source px')
ap.add_argument('--key-white', dest='key', action='store_true', default=None)
ap.add_argument('--no-key-white', dest='key', action='store_false')
ap.add_argument('--strip-labels', action='store_true')
ap.add_argument('--label-zone', type=int, default=430)
ap.add_argument('--align', choices=('x', 'xy', 'none'), default='x')
ap.add_argument('--head-y', type=int, default=160)
a = ap.parse_args()

dst = os.path.join(a.folder, 'SK')
if not os.path.isdir(dst):
    os.makedirs(dst)


def key_white(arr, thr=246):
    """True where the pixel is page, not drawing."""
    white = (arr[:, :, 0] >= thr) & (arr[:, :, 1] >= thr) & (arr[:, :, 2] >= thr)
    lab, _ = ndimage.label(white)
    edge = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]])))
    edge.discard(0)
    return np.isin(lab, list(edge))


for f in sorted(glob.glob(os.path.join(a.folder, 'NAT_*.png'))):
    arr = np.array(Image.open(f).convert('RGBA'))
    H, W = arr.shape[:2]
    notes = []

    if a.key or (a.key is None and arr[:, :, 3].min() == 255):
        bg = key_white(arr)
        arr[bg] = (0, 0, 0, 0)
        notes.append('keyed %.0f%% page' % (100.0 * bg.sum() / bg.size))

    if a.strip_labels:
        ink = arr[:, :, 3] > 30
        lab, n = ndimage.label(ink, structure=np.ones((3, 3), np.uint8))
        sizes = ndimage.sum(ink, lab, range(1, n + 1))
        biggest = int(np.argmax(sizes)) + 1
        sl = ndimage.find_objects(lab)
        # Open line art can leave the figure in several pieces, so "is it the
        # biggest blob" is not enough on its own. What separates the two is
        # reach: every piece of the drawing extends down into the body, while
        # a letter is finished before the shoulders. Size is not a safe test -
        # one capital stroke is bigger than 5% of the figure.
        drop = [i for i in range(1, n + 1)
                if i != biggest and sl[i - 1][0].stop < a.label_zone]
        if drop:
            mask = np.isin(lab, drop)
            keep_ink = ink & ~mask
            mask = ndimage.binary_dilation(mask, iterations=3)  # take the halo
            mask &= ~keep_ink                                   # never bite the drawing
            arr[mask] = (0, 0, 0, 0)
            notes.append('erased %d label blob(s)' % len(drop))

    if a.align != 'none':
        ink = arr[:, :, 3] > 30
        head = int(np.nonzero(ink.any(axis=1))[0].min())
        # hip band: low enough to clear the arms, high enough to clear the legs
        y0, y1 = head + int(a.knee_span * 0.55), head + int(a.knee_span * 0.68)
        cols = np.nonzero(ink[y0:y1].any(axis=0))[0]
        cx = int((cols.min() + cols.max()) // 2)
        dx = W // 2 - cx
        dy = (a.head_y - head) if a.align == 'xy' else 0
        arr = np.roll(np.roll(arr, dy, axis=0), dx, axis=1)
        notes.append('shift (%+d,%+d)' % (dx, dy))

    Image.fromarray(arr).save(os.path.join(dst, os.path.basename(f)))
    print('%-40s %s' % (os.path.basename(f), '; '.join(notes) or 'copied'))
