# Uzi Character Definition
define Uzi = Character("Uzi", color="#9b59b6", image="Uzi")

# ==========================================================
# EXPRESSIONS (placeholder)
# ==========================================================
# The CANONICAL POSES below are the official pose list for the
# artist. These are the current pose names used by the scripts.
init python:
    # ------------------------------------------------------
    # CANONICAL POSES - the official pose list (what the
    # artist will draw). This is the source of truth; add or
    # remove poses here as art is planned.
    # ------------------------------------------------------
    Uzi_poses = [
        "blank", "idle", "perverted_smile", "shocked", "bad_mood", "annoyed",
    ]

    # Every pose shares one placeholder sprite for now. When real
    # art exists, replace this loop with proper per-pose images.
    for _m in Uzi_poses:
        renpy.image("Uzi " + _m, im.Scale("images/Test_Characters/body1_4.png", 600, 900))
    del _m

# ==========================================================
# FLAGS (presence + event)
# ==========================================================
# Uzi isn't placed in a location or wired into any scene yet.
# When he is: add a presence flag (e.g. uzi_in_cafe) and a
# character_button for him in Locations/CharacterLocation.rpy.
default uzi_has_event = False
