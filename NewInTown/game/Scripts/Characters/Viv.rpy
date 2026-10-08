# Viv Character Definition
define Viv = Character("Viv", color="#e05fa8", image="Viv")

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
    # Mirrors the pose sheet: # / pose (aliases) / art status.
    # ------------------------------------------------------
    Viv_poses = [
        "idle",         # 1 Idle                                -
        "smiling",      # 2 Smiling                             -
        "blush",        # 3 Blush                               -
        "horny_smirk",  # 4 Horny Smirk                         -
    ]

    # Every pose shares one placeholder sprite for now. When real
    # art exists, replace this loop with proper per-pose images.
    for _m in Viv_poses:
        renpy.image("Viv " + _m, placeholder_sprite("images/Test_Characters/body1_2.png"))
    del _m

# ==========================================================
# FLAGS (presence + event)
# ==========================================================
# Viv isn't placed in a location or wired into any scene yet.
# When she is: add a presence flag (e.g. viv_in_college) and a
# character_button for her in Locations/CharacterLocation.rpy.
# Her one unique pose (UP_ScanID, scene B01_01) lives in
# Characters/Unique_Poses.rpy.
default viv_has_event = False
