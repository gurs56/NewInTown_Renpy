# ==========================================================
# CHARACTER LOCATIONS (Mid Town)
# ==========================================================
# Contains only character image buttons for location screens.
# Used by Mid_Town_Location.rpy via `use`.
# ==========================================================

# ==========================================================
# LOBBY CHARACTER BUTTONS
# ==========================================================
screen character_buttons_lobby():
    # Only show when NOT in a story scene
    if not in_story_scene:
        # Ms. Lopez - always in lobby
        if ms_lopez_in_lobby:
            imagebutton:
                idle "images/Test_Characters/body1 2.png"
                hover "images/Test_Characters/body1 2.png"
                action Jump("talk_ms_lopez")
                xpos 700
                ypos 400
                focus_mask True

            # Character name label
            text "Ms. Lopez" xpos 700 ypos 370 size 22 color "#ffffff"

            # Quest indicator (exclamation mark if she has an event)
            if ms_lopez_has_event:
                text "!" xpos 730 ypos 395 size 40 color "#ffff00" bold True

# ==========================================================
# HALLWAY CHARACTER BUTTONS
# ==========================================================
screen character_buttons_hallway():
    # Only show when NOT in a story scene
    if not in_story_scene:
        if amber_in_hallway:
            button:
                xpos 720
                ypos 320
                xysize (300, 600)
                action Jump("talk_amber")
                add "images/Test_Characters/body1 2.png" fit "contain"
            text "Amber" xpos 720 ypos 290 size 22 color "#ffffff"
            if amber_has_event:
                text "!" xpos 750 ypos 315 size 40 color "#ffff00" bold True
# ==========================================================
# CHARACTER LOCATIONS (Mid Town)
# ==========================================================
# Contains only character image buttons for location screens.
# Used by Mid_Town_Location.rpy via `use`.
# ==========================================================

# ==========================================================
# LOBBY CHARACTER BUTTONS
# ==========================================================
screen character_buttons_lobby():
    # Only show when NOT in a story scene
    if not in_story_scene:
        # Ms. Lopez - always in lobby
        if ms_lopez_in_lobby:
            imagebutton:
                idle "images/Test_Characters/body1 2.png"
                hover "images/Test_Characters/body1 2.png"
                action Jump("talk_ms_lopez")
                xpos 700
                ypos 400
                focus_mask True

            # Character name label
            text "Ms. Lopez" xpos 700 ypos 370 size 22 color "#ffffff"

            # Quest indicator (exclamation mark if she has an event)
            if ms_lopez_has_event:
                text "!" xpos 730 ypos 395 size 40 color "#ffff00" bold True

# ==========================================================
# HALLWAY CHARACTER BUTTONS
# ==========================================================
screen character_buttons_hallway():
    # Only show when NOT in a story scene
    if not in_story_scene:
        if amber_in_hallway:
            button:
                xpos 720
                ypos 320
                xysize (300, 600)
                action Jump("talk_amber")
                add "images/Test_Characters/body1 2.png" fit "contain"
            text "Amber" xpos 720 ypos 290 size 22 color "#ffffff"
            if amber_has_event:
                text "!" xpos 750 ypos 315 size 40 color "#ffff00" bold True
