# Luca Character Definition
define Luca = Character("Luca", color="#4a90e2", image="Luca")

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
    # Mirrors the pose sheet: # / pose (aliases) / art status.
    # ------------------------------------------------------
    Luca_poses = [
        "idle",         # 1 Idle (Playing Switch)               Finished
        "boastful",     # 2 Boastful                            Sketch
        "serious",      # 3 Serious                             Sketch
        "unbothered",   # 4 Unbothered (doesn't care)           Sketch
    ]

    # Every pose shares one placeholder sprite for now. When real
    # art exists, replace this loop with proper per-pose images.
    for _m in Luca_poses:
        renpy.image("Luca " + _m, placeholder_sprite("images/Test_Characters/body1_4.png"))
    del _m
