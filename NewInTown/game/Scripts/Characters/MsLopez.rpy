
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
    # ------------------------------------------------------
    MsLopez_poses = [
        "idle", "explaining", "strict", "irritated", "angry", "thinking",
        "smirk", "happy", "joyful", "worried", "sad", "shocked",
        "horny", "excited",
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

    # Every pose shares one placeholder sprite for now. When real
    # art exists, replace this loop with proper per-pose images.
    for _m in MsLopez_poses + MsLopez_legacy_moods:
        renpy.image("MsLopez " + _m, im.Scale("images/Test_Characters/body1_1.png", 600, 900))
    del _m

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
