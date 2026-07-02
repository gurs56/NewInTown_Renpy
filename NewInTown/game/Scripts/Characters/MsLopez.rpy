
define MsLopez = Character("Ms. Lopez", color="#a64d79", image="MsLopez")

# ==========================================================
# EXPRESSIONS (placeholder)
# ==========================================================
# All moods share one placeholder sprite. Add a new mood by
# dropping its name in this list - no missing-image crashes.
init python:
    for _m in [
        "neutral", "stressed", "idle", "stern", "warm", "curious",
        "amused", "doubtful", "excited", "explaining", "happy",
        "impressed", "irritated", "laughing", "sad", "shocked",
        "smirk", "thinking", "angry", "convinced", "strict", "worried",
    ]:
        renpy.image("MsLopez " + _m, im.Scale("images/Test_Characters/body1 1.png", 600, 900))
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
    """Ms. Lopez interaction handler"""
    hide screen apartment_lobby_screen

    menu:
        "What would you like to say?"

        "Option 1 (Placeholder)":
            call dialogue_ms_lopez_option1
            show screen apartment_lobby_screen
            $ renpy.pause(hard=True)
            jump exploration_loop

        "Option 2 (Placeholder)":
            call dialogue_ms_lopez_option2
            show screen apartment_lobby_screen
            $ renpy.pause(hard=True)
            jump exploration_loop

        "Talk about tasks" if quest_meet_ms_lopez_complete and not quest_fix_amber_door_started:
            $ ms_lopez_has_event = False
            jump A02_1_LOBBY_TASK

        "About Amber's door..." if quest_fix_amber_door_started and not quest_fix_amber_door_complete:
            MsLopez "Have you checked on Amber's door yet? She's on the third floor, to the left."
            MsLopez "Just head up to her apartment and talk to her."
            show screen apartment_lobby_screen
            $ renpy.pause(hard=True)
            jump exploration_loop

        "Never mind":
            show screen apartment_lobby_screen
            $ renpy.pause(hard=True)
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
