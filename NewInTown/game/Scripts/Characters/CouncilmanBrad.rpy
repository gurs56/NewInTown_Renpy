# Councilman Brad Character Definition
define Brad = Character("Councilman Brad", color="#5b7fb5", image="Brad")

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
    Brad_poses = [
        "idle",         # 1 Idle                                -
    ]

    # Every pose shares one placeholder sprite for now. When real
    # art exists, replace this loop with proper per-pose images.
    for _m in Brad_poses:
        renpy.image("Brad " + _m, placeholder_sprite("images/Test_Characters/body1_4.png"))
    del _m

# ==========================================================
# FLAGS (presence + event)
# ==========================================================
# Brad isn't placed in a location or wired into any scene yet.
# He is on the pose sheet as Luca's father - a City council
# member, referenced by Tanya in A03_04 but never shown.
# When he is used: add a presence flag (e.g. brad_in_city_hall)
# and a character_button for him in Locations/CharacterLocation.rpy.
default brad_has_event = False
