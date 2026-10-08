# ==========================================================
# SPRITE FRAMING - one shared camera for every character
# ==========================================================
# The source art does NOT arrive at one size. Ms. Lopez is
# 1067x1945 (ratio 0.55); Uncle and Razor are 1405x1807
# (ratio 0.78). The old code pushed every sprite through
# im.Scale(600, 900), forcing all of them into one box - so each
# was stretched by a DIFFERENT amount (Lopez widened, the men
# squashed) and they ended up looking like different sizes.
#
# Instead each character is measured once, in SOURCE PIXELS:
#
#   canvas - the png's own size, so the crop maths is exact.
#   head   - y of the top of the head.
#   knee   - y of the knee line. This sets the SCALE: everyone is
#            zoomed so head->knee is the same number of screen
#            pixels, which is what makes them read as standing at
#            the same distance from the camera. It is also the
#            bottom of the finished image, so `yanchor 1.0` puts
#            every character's knees on the same line.
#   cut    - y where the art is actually sliced, for art that has
#            something awkward crossing the knee line. It is
#            padded back out to `knee`, so cutting higher does not
#            shrink a character or drop their head.
#            CURRENTLY EVERY CHARACTER USES cut == knee. Uncle was
#            briefly cut above his knee (his crossed-forward shoe
#            straddles the line), but padding the difference left
#            49px of empty space under him: his legs stopped short
#            of the bottom edge and he read as "cut off" floating
#            above it. Slicing straight through at the knee looks
#            far better - the trouser simply runs off the screen
#            edge. Only raise `cut` above `knee` if the resulting
#            gap is genuinely less ugly than the slice.
#   cx     - x of the body's centre line, measured from the part
#            of the silhouette common to ALL of that character's
#            poses. Anchoring on the body rather than the bounding
#            box stops a character sliding sideways when an arm
#            swings out - Razor's cigarette arm and Uncle's
#            pointing arm both travel a long way between poses.
#   scale  - per-character height trim. 1.0 means "same head-to-
#            knee as everyone else". Lower it to make a character
#            read as shorter, raise it for taller. This is the
#            only value here that is art direction rather than
#            measurement, so it is the one to tweak by eye.
#   flip   - True mirrors the sprite horizontally, for art drawn
#            facing the wrong way for where the character stands.
#            The mirror happens AFTER the body is centred, so a
#            flipped character does not shift sideways.
#
# Every pose of a character is registered to the same canvas
# (feet land within 0-18px across poses), so one row covers all
# of that character's expressions.
#
# Characters whose art has not arrived yet are not listed here -
# they keep the flat placeholder sprite.
# ==========================================================

init -10 python:

    # On-screen pixels from top of head to knee. This is the one
    # dial for "how close is the camera" - raise it to push the
    # cast further forward, lower it to pull back. Changing it here
    # resizes the whole cast at once and keeps their relative
    # heights (the per-character `scale` column) intact.
    SPRITE_KNEE_H = 792

    CHAR_FRAME = {
        #             canvas         head  knee  cut   cx   scale  flip
        "MsLopez": ((1067, 1945),     35, 1315, 1315,  539, 0.90, True),
        "Uncle":   ((1405, 1807),     80, 1232, 1232,  857, 0.90, False),
        "Razor":   ((1405, 1807),     15, 1230, 1230,  753, 0.90, True),
        "MC":      ((2109, 3019),      0, 2058, 2058,  969, 1.00, False),
        "Amber":   (( 944, 2607),     32, 1815, 1815,  441, 0.90, False),

        # Sketch sheets. The artist draws roughs on a square 2048
        # canvas at a different zoom from the finished sprites, so
        # they need their own row - reusing "MsLopez" here would
        # show her about 40% too large. Measured off the cleaned
        # sheets in images/Characters/<name>/SK/.
        "MsLopez_SK": ((2048, 2048),  160, 1971, 1971, 1024, 0.90, True),
        "Amber_SK":   ((2048, 2048),  160, 1712, 1712, 1024, 0.90, False),
        "MC_SK":      ((2048, 2048),  113, 1994, 1994, 1010, 1.00, False),
    }

    # ------------------------------------------------------
    # BAKED SPRITES - tools/bake_sprites.py
    # Building the crop -> composite -> flip -> scale chain at
    # runtime is what made the whole cast flicker. Ren'Py caches
    # EVERY link of an im.* chain separately (each load() calls
    # cache.get() on its child), so one MC sketch pose held the
    # 2048x2048 source, the crop, the composite AND the sprite at
    # once: 12.6 million pixels to draw 0.7 million. The cache is
    # about 105M px (config.image_cache_size_mb = 400), so scene
    # A01 wanted 69% of it for eight sprites - and past the limit
    # Ren'Py evicts images that are still on screen and re-decodes
    # them the next frame, which reads as blinking.
    #
    # A baked file is the finished sprite, so it costs only what it
    # draws and nothing is decoded or rescaled mid-scene. Re-run
    # the tool whenever art or the numbers above change; if a bake
    # is missing the live chain below still runs, so a fresh
    # checkout works without it.
    # ------------------------------------------------------
    BAKED_DIR = "images/Characters/_framed"

    def baked_sprite(char, path, tag=""):
        """Path of the pre-rendered sprite, or None if it isn't baked."""
        stem = path.rsplit("/", 1)[-1].rsplit(".", 1)[0]
        rv = "%s/%s__%s%s.png" % (BAKED_DIR, char, stem, tag)
        return rv if renpy.loadable(rv) else None

    def framed_sprite(char, path):
        """Crop one raw sprite to knees-up and fit it to the shared camera.

        Returns a displayable whose bottom edge is the character's knee
        line and whose horizontal centre is the character's body centre.
        That lets the stage_* transforms below place anyone with a plain
        xanchor 0.5 / yanchor 1.0.
        """
        rv = baked_sprite(char, path)
        if rv:
            return rv

        (cw, chh), head, knee, cut, cx, scale, flip = CHAR_FRAME[char]

        zoom = (SPRITE_KNEE_H * scale) / float(knee - head)
        croph = cut - head     # how much art we actually keep
        fullh = knee - head    # ...padded out to the knee line

        # Vertical crop only - full width is kept so an outstretched
        # arm is never clipped.
        img = im.Crop(path, (0, head, cw, croph))

        # Pad symmetrically about cx (body centre -> image centre) and
        # down to the knee line (so `cut` above `knee` costs no height).
        half = int(max(cx, cw - cx))
        img = im.Composite((half * 2, fullh), (int(half - cx), 0), img)

        # Mirrored after centring, so the body stays on its mark.
        if flip:
            img = im.Flip(img, horizontal=True)

        return im.FactorScale(img, zoom)


    # Height of a character button's sprite, in screen pixels.
    BUTTON_H = 400

    def button_sprite(char, path, height=None):
        """The same framing, sized down for a location's character button.

        Buttons used to run the raw art through im.Scale(200, 400), which
        forced every sprite into one box and squashed each by a different
        amount - the same bug the stage sprites had. Reusing the framing
        keeps a button's figure matching how that character looks on stage.
        """
        if height is None:
            height = BUTTON_H
        if height == BUTTON_H:
            rv = baked_sprite(char, path, "_btn")
            if rv:
                return rv

        (cw, chh), head, knee, cut, cx, scale, flip = CHAR_FRAME[char]
        croph, fullh = cut - head, knee - head
        img = im.Crop(path, (0, head, cw, croph))
        half = int(max(cx, cw - cx))
        img = im.Composite((half * 2, fullh), (int(half - cx), 0), img)
        if flip:
            img = im.Flip(img, horizontal=True)
        return im.FactorScale(img, height / float(fullh))


    # ------------------------------------------------------
    # PLACEHOLDER - characters whose art has not arrived.
    # The stand-in bodies in images/Test_Characters are all
    # 256x288 (ratio 0.889). They used to go through
    # im.Scale(600, 900), which is ratio 0.667 - so the
    # placeholder was squashed ~25% narrower, AND ended up 900
    # tall next to real characters at 990. A scene mixing the two
    # looked wrong in both size and proportion.
    #
    # This keeps the stand-in's own aspect and matches the height
    # of a framed character, so a placeholder sits correctly
    # beside finished art and the stage_* transforms line them up.
    # ------------------------------------------------------
    PLACEHOLDER_SIZE = (256, 288)   # every Test_Characters body

    def placeholder_sprite(path, height=None):
        if height is None:
            height = SPRITE_KNEE_H
        pw, ph = PLACEHOLDER_SIZE
        return im.Scale(path, int(height * pw / float(ph)), int(height))


# ==========================================================
# STAGE POSITIONS
# ==========================================================
# ypos/yanchor 1.0 drops the knee line onto the bottom screen edge.
# xanchor 0.5 lands the BODY centre on xpos, because framed_sprite()
# already centred the body inside the image.
# Evenly spaced: quarter / half / three-quarters, so the gaps
# between marks and the margins to each screen edge all match.
transform stage_left:
    xpos 0.25 xanchor 0.5 ypos 1.0 yanchor 1.0

transform stage_center:
    xpos 0.50 xanchor 0.5 ypos 1.0 yanchor 1.0

transform stage_right:
    xpos 0.75 xanchor 0.5 ypos 1.0 yanchor 1.0
