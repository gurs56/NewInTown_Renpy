# Amber Character Definition
define Amber = Character("Amber", color="#ff6b9d", image="Amber")

# ==========================================================
# EXPRESSIONS (placeholder)
# ==========================================================
# All moods share one placeholder sprite. Add a new mood by
# dropping its name in this list - no missing-image crashes.
init python:
    for _m in [
        "neutral", "embarrassed", "playful", "teasing", "grateful",
        "sassy", "irritated", "smirk", "concerned", "idle",
        "laughing", "seductive", "underwear", "work_uniform",
    ]:
        renpy.image("Amber " + _m, im.Scale("images/Test_Characters/body1_2.png", 600, 900))
    del _m

# ==========================================================
# FLAGS (presence + event)
# ==========================================================
default amber_in_apartment = True
default amber_has_event = False

# ==========================================================
# INTERACTION ROUTING
# ==========================================================
label talk_amber:
    # Amber interaction handler (must be a # comment - a bare
    # string inside a label would display as dialogue!)
    hide screen apartment_amber_apartment_screen

    if amber_has_event and quest_fix_amber_door_started and not quest_fix_amber_door_complete:
        $ amber_has_event = False
        jump A02_2_AMBER_DOOR
    elif has_hinges and not quest_fix_amber_door_complete:
        jump A02_5_FIX_DOOR
    else:
        call generic_amber_chat
        show screen apartment_amber_apartment_screen
        jump exploration_loop

# ==========================================================
# DIALOGUE
# ==========================================================
label generic_amber_chat:
    scene bg apartment_amber_apartment with fade
    # show Amber idle

    Amber "Hey there, pervy. Need something?"

    MC "Just checking in."
    if quest_fix_amber_door_complete:
        Amber "Well, I'm fine. Door's working great, by the way."
    else:
        Amber "Well, I'm fine. Busy, but fine. Now shoo."

    return
