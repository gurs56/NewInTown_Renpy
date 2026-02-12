# ==========================================================
# MID TOWN FLAGS + DIALOGUE
# ==========================================================
# Contains character flags, routing, and dialogue for Mid Town.
# Keep location screens in Mid_Town_Location.rpy
# ==========================================================

# ==========================================================
# CHARACTER FLAGS INITIALIZATION
# ==========================================================
default ms_lopez_in_lobby = True
default ms_lopez_has_event = False

default amber_in_apartment = True
default amber_in_hallway = False
default amber_has_event = False

default razor_in_apartment = True
default razor_has_event = False

default uncle_in_shop = True
default uncle_has_event = False

default tanya_in_cafe = False
default tanya_has_event = False

# Add more characters as needed...
# default character_name_location = True
# default character_name_has_event = False

# ==========================================================
# STORY/QUEST FLAGS
# ==========================================================
default quest_meet_ms_lopez_complete = False
default quest_fix_amber_door_started = False
default quest_fix_amber_door_complete = False
default quest_find_job_started = False
default quest_find_job_complete = False
default quest_hot_water_fixed = False
default has_apartment = False

# Story scene flag (hides characters during cutscenes)
default in_story_scene = True

# ==========================================================
# CHARACTER EVENT SETUP FUNCTIONS
# ==========================================================
# Call these functions when you want to trigger new events

label setup_a02_event:
    """Enable A02 - Fixing Amber's Door"""
    $ ms_lopez_has_event = True
    $ quest_fix_amber_door_started = True
    return

label setup_a03_event:
    """Enable A03 - Job Interview"""
    $ ms_lopez_has_event = True
    $ quest_find_job_started = True
    return

label setup_a04_event:
    """Enable A04 - Hot Water"""
    $ ms_lopez_has_event = True
    return

label setup_a05_event:
    """Enable A05 - Getting Apartment"""
    $ ms_lopez_has_event = True
    return

# ==========================================================
# MS. LOPEZ
# ==========================================================
# Interaction routing
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
        
        "Talk about tasks" if quest_meet_ms_lopez_complete and not quest_fix_amber_door_complete:
            $ ms_lopez_has_event = False
            jump A02_1_LOBBY_TASK
        
        "Never mind":
            show screen apartment_lobby_screen
            $ renpy.pause(hard=True)
            jump exploration_loop

# Dialogue options
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

# ==========================================================
# AMBER
# ==========================================================
# Interaction routing
label talk_amber:
    """Amber interaction handler"""
    hide screen amber_apartment_screen
    
    if amber_has_event and quest_fix_amber_door_started and not quest_fix_amber_door_complete:
        $ amber_has_event = False
        jump A02_2_AMBER_DOOR
    else:
        call generic_amber_chat
        show screen amber_apartment_screen
        $ renpy.pause(hard=True)
        jump exploration_loop

# Generic conversation
label generic_amber_chat:
    scene bg apartment_amber_apartment with fade
    # show Amber idle

    Amber "Hey there, pervy. Need something?"

    MC "Just checking in."
    Amber "Well, I'm fine. Door's working great, by the way."

    return

# ==========================================================
# RAZOR
# ==========================================================
# Interaction routing
label talk_razor:
    """Razor interaction handler"""
    hide screen razor_apartment_screen
    
    if razor_has_event:
        # Route to Razor's events
        pass
    else:
        call generic_razor_chat
        show screen razor_apartment_screen
        $ renpy.pause(hard=True)
        jump exploration_loop

# Generic conversation
label generic_razor_chat:
    scene bg apartment_razor_apartment with fade
    # show Razor grumpy

    Razor "What do you want, kid?"

    MC "Just saying hi."
    Razor "Hmph. I'm busy. Come back later."

    return
