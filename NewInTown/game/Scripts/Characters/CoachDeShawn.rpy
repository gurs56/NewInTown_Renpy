# Coach DeShawn Character Definition
define CoachDeShawn = Character("Coach DeShawn Briggs", color="#2d5016", image="CoachDeShawn")

# ==========================================================
# EXPRESSIONS (placeholder)
# ==========================================================
# The CANONICAL POSES below are the official pose list for the
# artist. These are the current pose names used by the scripts
init python:
    # ------------------------------------------------------
    # CANONICAL POSES - the official pose list (what the
    # artist will draw). This is the source of truth; add or
    # remove poses here as art is planned.
    # ------------------------------------------------------
    CoachDeShawn_poses = [
        "welcoming", "idle",
    ]

    # ------------------------------------------------------
    # LEGACY MOODS - older words still used by story scripts
    # that AREN'T canonical poses yet. Kept working (they show
    # the placeholder) so nothing crashes. To retire one:
    # change the script to a canonical pose above, then
    # delete the word here.
    # ------------------------------------------------------
    CoachDeShawn_legacy_moods = [
        "confident", "surprised",
    ]

    # Every pose shares one placeholder sprite for now. When real
    # art exists, replace this loop with proper per-pose images.
    for _m in CoachDeShawn_poses + CoachDeShawn_legacy_moods:
        renpy.image("CoachDeShawn " + _m, im.Scale("images/Test_Characters/body1_3.png", 600, 900))
    del _m
