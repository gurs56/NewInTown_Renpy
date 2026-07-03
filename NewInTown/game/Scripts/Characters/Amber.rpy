# Amber Character Definition
define Amber = Character("Amber", color="#ff6b9d", image="Amber")

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
    Amber_poses = [
        "arms_crossed", "irritated", "seductive", "laughing", "concerned", "idle",
        "seductive_wink",
    ]

    # ------------------------------------------------------
    # LEGACY MOODS - older words still used by story scripts
    # that AREN'T canonical poses yet. Kept working (they show
    # the placeholder) so nothing crashes. To retire one:
    # change the script to a canonical pose above, then
    # delete the word here.
    # ------------------------------------------------------
    Amber_legacy_moods = [
        "sassy", "smirk", "underwear", "work_uniform",
    ]

    # Every pose shares one placeholder sprite for now. When real
    # art exists, replace this loop with proper per-pose images.
    for _m in Amber_poses + Amber_legacy_moods:
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
