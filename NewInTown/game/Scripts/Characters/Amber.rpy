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
    # Mirrors the pose sheet: # / pose (aliases) / art status.
    # ------------------------------------------------------
    Amber_poses = [
        "arms_crossed",    # 1 Arms crossed, Sassy              -
        "irritated",       # 2 Irritated (one arm on hips)      Inked
        "seductive",       # 3 Seductive (smirk/teasing)        Inked
        "laughing",        # 4 Laughing                         Inked
        "concerned",       # 5 Concerned                        -
        "idle",            # 6 Idle (Sassy)                     NotStarted
        "seductive_wink",  # 7 Seductive Wink (teasing)         NotStarted
        "smiling",         # 8 Smiling                          Sketch
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

    # ------------------------------------------------------
    # ART. The clothed idle is the only FINISHED sprite, and it
    # is what any pose without its own art falls back to - so
    # Amber always looks right, she just may not change
    # expression on that line.
    #
    # The NAT_CH_AMBER_*_SK files are the artist's pencil roughs.
    # They are wired as stand-ins so her expression actually
    # changes with the writing; a rough that matches the line
    # reads better than a finished sprite that ignores it. To
    # go back to "finished sprite everywhere", empty
    # Amber_sketch_art below - nothing else needs touching.
    #
    # The raw scans have the pose name handwritten beside her
    # head, so the wired copies are the CLEANED ones in SK/
    # (see the sketch note in SpriteFraming.rpy). They are drawn
    # on a square 2048 canvas at their own zoom, hence the
    # separate "Amber_SK" camera row.
    #
    # Not wired, because no canonical pose matches them yet:
    #   Shy, Thinking
    # ------------------------------------------------------
    Amber_default_art = "images/Characters/Amber/NIT_CH_AMBER_CLOTHED_IDLE_v01.png"

    # Finished, inked art. Add a pose here and it beats the sketch.
    Amber_pose_art = {
        # "irritated": "images/Characters/Amber/...",   <- inked art
    }

    Amber_sketch_art = {
        "irritated":    "images/Characters/Amber/SK/NAT_CH_AMBER_Irritated_SK_v01.png",
        "laughing":     "images/Characters/Amber/SK/NAT_CH_AMBER_Laughing_SK_v01.png",
        "smiling":      "images/Characters/Amber/SK/NAT_CH_AMBER_Smiling_SK_v01.png",
        "seductive":    "images/Characters/Amber/SK/NAT_CH_AMBER_Horny_SK_v01.png",
        "arms_crossed": "images/Characters/Amber/SK/NAT_CH_AMBER_Umimpressed_SK_v01.png",
        "concerned":    "images/Characters/Amber/SK/NAT_CH_AMBER_Surprised_SK_v01.png",
        "sassy":        "images/Characters/Amber/SK/NAT_CH_AMBER_Eyeroll_SK_v01.png",
        "smirk":        "images/Characters/Amber/SK/NAT_CH_AMBER_Horny_SK_v01.png",
    }

    for _m in Amber_poses + Amber_legacy_moods:
        if _m in Amber_pose_art:
            _img = framed_sprite("Amber", Amber_pose_art[_m])
        elif _m in Amber_sketch_art:
            _img = framed_sprite("Amber_SK", Amber_sketch_art[_m])
        else:
            _img = framed_sprite("Amber", Amber_default_art)
        renpy.image("Amber " + _m, _img)
    del _m, _img

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
