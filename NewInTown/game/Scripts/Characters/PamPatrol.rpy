# Pam Patrol Character Definition
define PamPatrol = Character("Pam Patrol", color="#3f8fb0", image="PamPatrol")

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
    PamPatrol_poses = [
        "idle",         # 1 Idle                                -
        "unimpressed",  # 2 Unimpressed                         -
        "happy",        # 3 Happy                               -
    ]

    # Every pose shares one placeholder sprite for now. When real
    # art exists, replace this loop with proper per-pose images.
    for _m in PamPatrol_poses:
        renpy.image("PamPatrol " + _m, placeholder_sprite("images/Test_Characters/body1_1.png"))
    del _m

# ==========================================================
# FLAGS (presence + event)
# ==========================================================
# Pam isn't placed in a location or wired into any scene yet.
# When she is: add a presence flag (e.g. pam_in_street) and a
# character_button for her in Locations/CharacterLocation.rpy.
default pam_has_event = False
