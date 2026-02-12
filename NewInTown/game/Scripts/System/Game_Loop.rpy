# ==========================================================
# GAME LOOP - Main game flow control
# ==========================================================

# The main start label - entry point of the game
label start:
    # QUICK START - Skip to apartment building (for testing)
    call initialize_game
    $ in_story_scene = False  # Enable free roam
    $ quest_meet_ms_lopez_complete = True  # Skip intro quest
    call setup_a02_event  # Enable A02 event
    show screen apartment_building_screen
    jump exploration_loop
    
    # NORMAL START - Uncomment these lines to play full intro
    # call initialize_game
    # call story_intro
    # jump free_roam_mode

# ==========================================================
# INITIALIZATION
# ==========================================================
label initialize_game:
    # Set starting time
    $ time_of_day.set_time("Morning")
    
    # Note: Character flags are now in Scripts/System/Characters.rpy
    # They use 'default' so they're automatically initialized
    
    return

# ==========================================================
# STORY INTRO SEQUENCE
# ==========================================================
label story_intro:
    # Play Act 1, Scene 00 - Bus Terminal Intro
    call A00_INTRO_BUS_TERMINAL
    
    # Play Act 1, Scene 01 - Meeting Ms. Lopez
    call A01_meeting_lopez
    
    # Mark A01 as complete and enable free roam
    $ quest_meet_ms_lopez_complete = True
    $ in_story_scene = False
    
    # Enable first event (A02)
    call setup_a02_event
    
    # Story intro complete
    "And now, your adventure in this new town begins..."
    
    return

# ==========================================================
# FREE ROAM MODE - Exploration
# ==========================================================
label free_roam_mode:
    # Show persistent UI elements
    show screen time_display
    
    # Show the world map as starting point
    show screen world_map_screen
    
    # Enter the main exploration loop
    jump exploration_loop

# ==========================================================
# EXPLORATION LOOP - Keeps game running
# ==========================================================
label exploration_loop:
    # Check for any events that should trigger
    # call check_events
    
    # Wait for player interaction
    # hard=True prevents auto-advance on clicks
    $ renpy.pause(hard=True)
    
    # Loop back to continue exploration
    jump exploration_loop

# ==========================================================
# EVENT CHECKER (Future expansion)
# ==========================================================
# label check_events:
#     # Check time-based events
#     if time_of_day.current == "Evening" and not story_flag_x:
#         call some_evening_event
#     
#     # Check location-based events
#     # Check relationship-based events
#     
#     return
