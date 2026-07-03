
define MC = Character("[mc_name]", color="#54c0f2", image="MC")

# ==========================================================
# MC NAME - single source of truth (player-changeable)
# ==========================================================
# In the script/team the MC is "mc", but in-game the player will
# get to choose their name. `mc_name` is a `default`, so it's part
# of each save and can change mid-playthrough. The Character above
# uses "[mc_name]", which re-reads this every time the MC speaks,
# so changing it updates ALL dialogue, narration ([mc_name]) and
# the phone instantly. Starts as "Aaron" until the player picks.
default mc_name = "EgeMan"

# Drop-in name entry. When the name-entry screen is built, either
# `call set_player_name` from it, or just set `mc_name` directly
# from your screen (e.g. action SetVariable). Nothing else to change.
label set_player_name:
    python:
        _n = renpy.input("What should we call you?", default=mc_name, length=20).strip()
        mc_name = _n if _n else "Aaron"
    return

# ==========================================================
# EXPRESSIONS (placeholder)
# ==========================================================
# The CANONICAL POSES below are the official pose list for the
# artist. LEGACY MOODS are older words the scripts still use; they
# stay working until the scripts are migrated to a canonical pose.
init python:
    # ------------------------------------------------------
    # CANONICAL POSES - the official pose list (what the
    # artist will draw). This is the source of truth; add or
    # remove poses here as art is planned.
    # ------------------------------------------------------
    MC_poses = [
        "idle", "happy", "innocent", "laughing", "excited", "confident",
        "sad", "thinking", "worried", "scared", "surprised", "blush",
        "smug", "disgusted", "explaining", "bargaining",
    ]

    # ------------------------------------------------------
    # LEGACY MOODS - older words still used by story scripts
    # that AREN'T canonical poses yet. Kept working (they show
    # the placeholder) so nothing crashes. To retire one:
    # change the script to a canonical pose above, then
    # delete the word here.
    # ------------------------------------------------------
    MC_legacy_moods = [
        "apologetic", "blushing", "celebrating", "confused", "curious", "determined",
        "disbelief", "enthusiastic", "flustered", "hesitant", "intrigued", "mischievous",
        "neutral", "panicking", "polite", "proud", "shy", "tired",
    ]

    # Every pose shares one placeholder sprite for now. When real
    # art exists, replace this loop with proper per-pose images.
    for _m in MC_poses + MC_legacy_moods:
        renpy.image("MC " + _m, im.Scale("images/Test_Characters/body1_3.png", 600, 900))
    del _m
