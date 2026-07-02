# Razor Character Definition
define Razor = Character("Razor", color="#8b4513", image="Razor")

# ==========================================================
# EXPRESSIONS (placeholder)
# ==========================================================
# All moods share one placeholder sprite. Add a new mood by
# dropping its name in this list - no missing-image crashes.
init python:
    for _m in [
        "neutral", "gruff", "defensive", "embarrassed", "serious",
        "grumpy", "irritated", "shocked", "stern", "suspicious",
        "thinking",
    ]:
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
