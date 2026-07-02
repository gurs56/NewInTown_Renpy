

# ==========================================================
# TIME TRACKER + HUD (top-right corner)
# ==========================================================
# Combined display + advance control. Clicking the tracker
# advances time. At Night it's disabled — the player must go
# to bed to sleep instead.
screen time_display():
    zorder 1000

    # Hidden during story scenes so a stray click on Map/Phone/time
    # can't derail a cutscene. Acts set in_story_scene at their start.
    if not in_story_scene:

        # --- Map + Phone + Time tracker, grouped in the top-right corner ---
        hbox:
            xalign 0.98
            yalign 0.02
            spacing 10

            # --- Map button: jumps straight to the world map ---
            button:
                yalign 0.0
                padding (15, 10)
                action Function(go_to_world_map)
                text "Map" size 22 yalign 0.5

            # --- Phone button: a little phone that "bigs up" when tapped ---
            button:
                yalign 0.0
                padding (10, 5)
                action ToggleScreen("phone_home")
                add "images/Phone/phone_foreground.png" zoom 0.1 yalign 0.5

            # --- Day / Time tracker doubles as the Advance Time button ---
            button:
                padding (10, 10)

                # Clicking advances time; sensitive only when it's not Night.
                action Function(time_of_day.advance)
                sensitive (not time_of_day.is_night())

                vbox:
                    spacing 2
                    text "[time_of_day.day_name]" size 24 xalign 0.5 bold True
                    text "[time_of_day.current]" size 20 xalign 0.5
                    text "Week [time_of_day.week_number]" size 16 xalign 0.5 color "#aaaaaa"

                    # Hint line: tells the player what clicking does.
                    if time_of_day.is_night():
                        text "Go to bed to sleep" size 16 xalign 0.5 color "#ff9999"
                    else:
                        text "Click to advance time" size 16 xalign 0.5 color "#aaaaaa"


# ==========================================================
# REUSABLE BUTTONS - use these instead of copy-pasting buttons
# ==========================================================
# Every location screen shares `tag location`, so Show()-ing a new
# location automatically hides the current one. That's why these
# buttons never need to know which screen they live on.

# ----------------------------------------------------------
# NAV BUTTON - moves the player to another location screen.
#   use nav_button("To Lobby", "apartment_lobby_screen", 885, 465)
# ----------------------------------------------------------
screen nav_button(label_text, target, x, y, size=120, text_size=24):
    button:
        xysize (size, size)
        xpos x
        ypos y
        action Show(target)
        add "gui/square_button.jpg" fit "contain"
        text label_text xalign 0.5 yalign 0.8 size text_size

# ----------------------------------------------------------
# QUEST BUTTON - starts a story scene (jumps to a label).
# Hides the current location screen first so the scene plays clean.
#   use quest_button("Check the leak", "A04_02_CHECK_LEAK", 700, 300)
# ----------------------------------------------------------
screen quest_button(label_text, target_label, x, y, size=150, text_size=24):
    button:
        xysize (size, size)
        xpos x
        ypos y
        action [Hide("location"), Jump(target_label)]
        add "gui/square_button.jpg" fit "contain"
        text label_text xalign 0.5 yalign 0.8 size text_size

# ----------------------------------------------------------
# CHARACTER BUTTON - a clickable character in a location.
# Shows name above, and a yellow "!" when they have an event.
#   use character_button("Amber", "talk_amber", amber_has_event)
# ----------------------------------------------------------
screen character_button(char_name, talk_label, has_event=False, x=400, y=200, sprite="images/Test_Characters/body1_2.png"):
    # Hidden during story scenes
    if not in_story_scene:
        imagebutton:
            idle im.Scale(sprite, 200, 400)
            hover im.Scale(sprite, 220, 440)
            action [Hide("location"), Jump(talk_label)]
            xpos x
            ypos y

        # Character name label above the sprite
        text char_name xpos x ypos (y - 30) size 22 color "#ffffff"

        # Quest indicator
        if has_event:
            text "!" xpos (x + 30) ypos (y - 5) size 40 color "#ffff00" bold True
