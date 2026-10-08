
define MsLopez = Character("Ms. Lopez", color="#a64d79", image="MsLopez")

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
    MsLopez_poses = [
        "idle",         #  1 Idle (Neutral)                     Finished
        "explaining",   #  2 Explaining                         -
        "strict",       #  3 Strict (Stern)                     Inked
        "irritated",    #  4 Irritated (Eyebrow Raised)         Finished
        "angry",        #  5 Angry                              Finished
        "thinking",     #  6 Thinking (Curious/Doubtful)        Inked
        "smirk",        #  7 Smirk (Impressed/Sassy)            -
        "happy",        #  8 Happy (Standard Smile)             Inked
        "joyful",       #  9 Joyful (Laughing)                  Finished
        "worried",      # 10 Worried (Stressed/Nervous)         NotStarted
        "sad",          # 11 Sad                                Finished
        "shocked",      # 12 Shocked                            Revision
        "horny",        # 13 Horny                              Inked
        "excited",      # 14 Excited                            -
        "guilty",       # 15 Guilty                             -
        "admiring",     # 16 Admiring                           -

        # Scene-specific on the pose sheet, but spoken through
        # mid-conversation, so it has to be a SPRITE - a full-screen
        # unique-pose card would wipe the lobby out from under the
        # dialogue. Artist id: lopez_u_tears.
        "tears",        #    A01: sad news about her friend     -
    ]

    # ------------------------------------------------------
    # LEGACY MOODS - older words still used by story scripts
    # that AREN'T canonical poses yet. Kept working (they show
    # the placeholder) so nothing crashes. To retire one:
    # change the script to a canonical pose above, then
    # delete the word here.
    # ------------------------------------------------------
    MsLopez_legacy_moods = [
        "convinced", "curious", "doubtful", "impressed", "laughing", "neutral",
        "stern", "stressed",
    ]

    # Poses with finished art (pose name -> art file).
    # Finished art. File names follow the artist's pose-sheet names.
    MsLopez_pose_art = {
        "idle": "images/Characters/Ms.Lopez/NIT_CH_LOPEZ_DEFAULT_idle.png",
        "irritated": "images/Characters/Ms.Lopez/NIT_CH_LOPEZ_DEFAULT_Irritated.png",
        "angry": "images/Characters/Ms.Lopez/NIT_CH_LOPEZ_DEFAULT_angry.png",
        "joyful": "images/Characters/Ms.Lopez/NIT_CH_LOPEZ_DEFAULT_joyful.png",
        "sad": "images/Characters/Ms.Lopez/NIT_CH_LOPEZ_DEFAULT_SAD.png",
        "shocked": "images/Characters/Ms.Lopez/NIT_CH_LOPEZ_DEFAULT_Shocked.png",
    }

    # Legacy words that are just aliases of a pose above with finished art.
    # Sketch stand-ins, for poses the artist has roughed out but not
    # finished. "happy" is filled by the Blush rough - the closest
    # warm expression drawn so far; swap it out when a real Happy
    # (pose 8, Standard Smile) is inked. Much better than the grey placeholder body, and they
    # read as "not final yet" on sight.
    # These are the CLEANED copies in SK/ - the raw scans have the
    # pose name handwritten beside her head, which would otherwise
    # show up on screen. They sit on a square 2048 canvas at a
    # different zoom, hence the separate "MsLopez_SK" camera row.
    MsLopez_sketch_art = {
        "strict":   "images/Characters/Ms.Lopez/SK/NAT_CH_MSLOPEZ_Sturn_SK_v01.png",
        "happy":    "images/Characters/Ms.Lopez/SK/NAT_CH_MSLOPEZ_Blush_SK_v01.png",
        "thinking": "images/Characters/Ms.Lopez/SK/NAT_CH_MSLOPEZ_Wonder_SK_v01.png",
        "worried":  "images/Characters/Ms.Lopez/SK/NAT_CH_MSLOPEZ_Stress_SK_v01.png",
        "horny":    "images/Characters/Ms.Lopez/SK/NAT_CH_MSLOPEZ_Horny_SK_v01.png",
    }

    # What a pose with no art of its own falls back to. Her finished
    # idle reads far better mid-scene than the grey placeholder body,
    # which used to appear for smirk, explaining, happy and excited.
    MsLopez_default_art = MsLopez_pose_art["idle"]

    # Legacy words that are just another name for a pose that has art.
    MsLopez_legacy_art_alias = {
        "neutral": "idle",
        "laughing": "joyful",
        "stressed": "worried",
        "stern": "strict",
        "curious": "thinking",
        "doubtful": "thinking",
    }

    def _mslopez_sprite(pose):
        """Best art available for a pose: finished, else sketch, else None."""
        pose = MsLopez_legacy_art_alias.get(pose, pose)
        if pose in MsLopez_pose_art:
            return framed_sprite("MsLopez", MsLopez_pose_art[pose])
        if pose in MsLopez_sketch_art:
            return framed_sprite("MsLopez_SK", MsLopez_sketch_art[pose])
        return None

    # Anything with neither finished nor sketch art draws her idle,
    # so no pose name can crash a scene or drop a grey body into one.
    for _m in MsLopez_poses + MsLopez_legacy_moods:
        _img = _mslopez_sprite(_m)
        if _img is None:
            _img = framed_sprite("MsLopez", MsLopez_default_art)
        renpy.image("MsLopez " + _m, _img)
    del _m, _img

# ==========================================================
# FLAGS (presence + event)
# ==========================================================
default ms_lopez_in_lobby = True
default ms_lopez_has_event = False

# ==========================================================
# INTERACTION ROUTING
# ==========================================================
label talk_ms_lopez:
    # Ms. Lopez interaction handler
    hide screen apartment_lobby_screen

    menu:
        "What would you like to say?"

        "Option 1 (Placeholder)":
            call dialogue_ms_lopez_option1
            show screen apartment_lobby_screen
            jump exploration_loop

        "Option 2 (Placeholder)":
            call dialogue_ms_lopez_option2
            show screen apartment_lobby_screen
            jump exploration_loop

        "Talk about tasks" if quest_meet_ms_lopez_complete and not quest_fix_amber_door_started:
            $ ms_lopez_has_event = False
            jump A02_1_LOBBY_TASK

        "About Amber's door..." if quest_fix_amber_door_started and not quest_fix_amber_door_complete:
            MsLopez "Have you checked on Amber's door yet? She's on the third floor, to the left."
            MsLopez "Just head up to her apartment and talk to her."
            show screen apartment_lobby_screen
            jump exploration_loop

        # --- A03: report the door, get sent job hunting ---
        "Report: Amber's door is fixed" if quest_find_job_started and not quest_find_job and not job_bean_spill:
            $ ms_lopez_has_event = False
            jump A03_01_REPORT_TO_LOPEZ

        # --- A04: report the new job, learn about the hot water ---
        "Tell her about your new job" if job_bean_spill and not quest_fix_hot_water and not quest_hot_water_fixed:
            $ ms_lopez_has_event = False
            jump A04_01_HOT_WATER_PROBLEM

        # --- A04: show her the magazines from the basement ---
        "Show her what you found downstairs" if quest_ask_lopez_magazines:
            jump A04_03_MAGAZINES_LOPEZ

        # --- A05: report the fixed pipe, get the surprise ---
        "Report: the hot water is fixed" if quest_report_lopez_water:
            $ ms_lopez_has_event = False
            jump A05_01_EAVESDROP_LOBBY

        "Never mind":
            show screen apartment_lobby_screen
            jump exploration_loop

# ==========================================================
# DIALOGUE
# ==========================================================
label dialogue_ms_lopez_option1:
    MC "Hey Ms. Lopez, how's everything going?"
    MsLopez "Oh, hello dear! Things are going well. Just keeping an eye on the building as always."
    MsLopez "Is there anything you need help with?"
    MC "Just checking in. Thanks!"
    return

label dialogue_ms_lopez_option2:
    MC "Do you know what time it is?"
    MsLopez "Let me check... It's currently Whatever fuck off."
    MsLopez "Is there somewhere you need to be?"
    MC "No, just curious. Thanks!"
    return

# Generic conversation
label generic_ms_lopez_chat:
    scene bg apartment_lobby with fade
    # show MsLopez idle

    MsLopez "Hello, MC. How are you settling in?"

    menu:
        "I'm doing well, thank you.":
            MC "Everything's good, Ms. Lopez. Thanks for asking."
            MsLopez "Good to hear. Let me know if you need anything."

        "Any work I can help with?":
            MC "Got any more jobs for me?"
            MsLopez "Not right now, but I'll let you know when something comes up."

    return
