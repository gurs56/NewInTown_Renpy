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
                idle im.Scale("images/Test_Characters/body1 2.png", 200, 400)
                hover im.Scale("images/Test_Characters/body1 2.png", 220, 440)
                action [Hide("apartment_lobby_screen"), Jump("talk_ms_lopez")]
                xpos 400
                ypos 200

            # Character name label (aligned with button)
            text "Ms. Lopez" xpos 400 ypos 170 size 22 color "#ffffff"

            # Quest indicator (exclamation mark if she has an event)
            if ms_lopez_has_event:
                text "!" xpos 430 ypos 195 size 40 color "#ffff00" bold True

# ==========================================================
# AMBER'S APARTMENT CHARACTER BUTTONS
# ==========================================================
screen character_buttons_amber_apartment():
    # Only show when NOT in a story scene
    if not in_story_scene:
        if amber_in_apartment:
            imagebutton:
                idle im.Scale("images/Test_Characters/body1 2.png", 200, 400)
                hover im.Scale("images/Test_Characters/body1 2.png", 220, 440)
                action [Hide("apartment_amber_apartment_screen"), Jump("talk_amber")]
                xpos 400
                ypos 200
            text "Amber" xpos 400 ypos 170 size 22 color "#ffffff"
            if amber_has_event:
                text "!" xpos 430 ypos 195 size 40 color "#ffff00" bold True
# ==========================================================
# GROCERY STORE CHARACTER BUTTONS
# ==========================================================
screen character_buttons_grocery():
    # Only show when NOT in a story scene
    if not in_story_scene:
        # Mr. Lee - always in his store
        if mr_lee_in_store:
            imagebutton:
                idle im.Scale("images/Test_Characters/body1 2.png", 200, 400)
                hover im.Scale("images/Test_Characters/body1 2.png", 220, 440)
                action [Hide("grocery_store_interior_screen"), Jump("talk_mr_lee")]
                xpos 400
                ypos 200

            # Character name label
            text "Mr. Lee" xpos 400 ypos 170 size 22 color "#ffffff"

            # Quest indicator (exclamation mark if he has an event)
            if mr_lee_has_event:
                text "!" xpos 430 ypos 195 size 40 color "#ffff00" bold True

# ==========================================================
# ALLEY CHARACTER BUTTONS
# ==========================================================
screen character_buttons_alley():
    # Only show when NOT in a story scene
    if not in_story_scene:
        # Uncle - always in the alley (for now)
        if uncle_in_alley:
            imagebutton:
                idle im.Scale("images/Test_Characters/body1 2.png", 200, 400)
                hover im.Scale("images/Test_Characters/body1 2.png", 220, 440)
                action [Hide("apartment_alley_screen"), Jump("talk_uncle")]
                xpos 400
                ypos 200

            # Character name label
            text "Uncle" xpos 400 ypos 170 size 22 color "#ffffff"

            # Quest indicator (exclamation mark if he has an event)
            if uncle_has_event:
                text "!" xpos 430 ypos 195 size 40 color "#ffff00" bold True

# ==========================================================