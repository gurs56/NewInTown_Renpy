
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
default mc_name = "Aaron"

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
# Every mood currently shares one placeholder sprite. To add a
# new mood, just drop its name in this list - it will never crash
# for a missing image and needs no extra lines.
init python:
    for _m in [
        "neutral", "confident", "confused", "nervous", "thinking",
        "surprised", "determined", "shy", "curious", "panicking",
        "polite", "happy", "apologetic", "bargaining", "blush",
        "blushing", "celebrating", "disbelief", "disgusted",
        "enthusiastic", "excited", "explaining", "flustered",
        "hesitant", "idle", "innocent", "intrigued", "laughing",
        "mischievous", "proud", "sad", "scared", "tired", "worried",
    ]:
        renpy.image("MC " + _m, im.Scale("images/Test_Characters/body1 3.png", 600, 900))
    del _m
