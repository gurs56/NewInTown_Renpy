# Razor Character Definition
define Razor = Character("Razor", color="#8b4513", image="Razor")

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
    Razor_poses = [
        "idle", "suspicious", "shocked", "irritated", "thinking",
    ]

    # ------------------------------------------------------
    # LEGACY MOODS - older words still used by story scripts
    # that AREN'T canonical poses yet. Kept working (they show
    # the placeholder) so nothing crashes. To retire one:
    # change the script to a canonical pose above, then
    # delete the word here.
    # ------------------------------------------------------
    Razor_legacy_moods = [
        "grumpy", "serious", "stern",
    ]

    # Every pose shares one placeholder sprite for now. When real
    # art exists, replace this loop with proper per-pose images.
    for _m in Razor_poses + Razor_legacy_moods:
        renpy.image("Razor " + _m, im.Scale("images/Test_Characters/body1_3.png", 600, 900))
    del _m

# ==========================================================
# FLAGS (presence + event)
# ==========================================================
default razor_in_apartment = True
default razor_has_event = False

# ==========================================================
# INTERACTION ROUTING
# ==========================================================
label talk_razor:
    # Razor interaction handler
    hide screen apartment_razor_apartment_screen

    # --- A04: MC needs Razor's help with the leaky pipe ---
    if quest_ask_razor_help:
        $ razor_has_event = False
        jump A04_04_RAZOR_BLACKMAIL

    if razor_has_event:
        # No other Razor events are written yet. Clear the flag and
        # fall back to the normal chat below. (Never leave a branch
        # that just ends - Ren'Py would fall through into the next
        # label and its `return` would end the game.)
        $ razor_has_event = False

    call generic_razor_chat
    show screen apartment_razor_apartment_screen
    jump exploration_loop

# ==========================================================
# DIALOGUE
# ==========================================================
label generic_razor_chat:
    scene bg apartment_razor_apartment with fade
    # show Razor grumpy

    Razor "What do you want, kid?"

    MC "Just saying hi."
    Razor "Hmph. I'm busy. Come back later."

    return
