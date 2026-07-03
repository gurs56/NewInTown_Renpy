# Tanya Character Definition
define Tanya = Character("Tanya", color="#ff9933", image="Tanya")

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
    Tanya_poses = [
        "idle", "happy", "greeting", "seductive", "annoyed", "angry",
        "explaining", "calling_out", "laughing", "blush", "intrigued",
    ]

    # ------------------------------------------------------
    # LEGACY MOODS - older words still used by story scripts
    # that AREN'T canonical poses yet. Kept working (they show
    # the placeholder) so nothing crashes. To retire one:
    # change the script to a canonical pose above, then
    # delete the word here.
    # ------------------------------------------------------
    Tanya_legacy_moods = [
        "blushing", "composed", "irritated", "welcoming",
    ]

    # Every pose shares one placeholder sprite for now. When real
    # art exists, replace this loop with proper per-pose images.
    for _m in Tanya_poses + Tanya_legacy_moods:
        renpy.image("Tanya " + _m, im.Scale("images/Test_Characters/body1_2.png", 600, 900))
    del _m

# ==========================================================
# FLAGS (presence + event)
# ==========================================================
default tanya_in_cafe = False
default tanya_has_event = False
