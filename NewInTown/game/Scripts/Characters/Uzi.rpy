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
    # Mirrors the pose sheet: # / pose (aliases) / art status.
    # NOTE: the whole Uzi set is on HOLD on the pose sheet.
    # ------------------------------------------------------
    Uzi_poses = [
        "blank",            # 1 Blank, cold expression          HOLD
        "idle",             # 2 Idle                            HOLD
        "perverted_smile",  # 3 Perverted smile                 HOLD
        "shocked",          # 4 Shocked                         HOLD
        "bad_mood",         # 5 Bad mood                        HOLD
        "annoyed",          # 6 Annoyed, fist on the table      HOLD
    ]

    # Every pose shares one placeholder sprite for now. When real
    # art exists, replace this loop with proper per-pose images.
    for _m in Uzi_poses:
        renpy.image("Uzi " + _m, placeholder_sprite("images/Test_Characters/body1_4.png"))
    del _m

# ==========================================================
# FLAGS (presence + event)
# ==========================================================
# Uzi isn't placed in a location or wired into any scene yet.
# When he is: add a presence flag (e.g. uzi_in_cafe) and a
# character_button for him in Locations/CharacterLocation.rpy.
default uzi_has_event = False
