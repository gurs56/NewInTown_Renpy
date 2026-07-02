

# ==========================================================
# TIME TRACKER BUTTON
# ==========================================================
# Combined display + advance control in the top-right corner.
# Clicking the tracker advances time. At Night it's disabled —
# the player must go to bed to sleep instead.
screen time_display():
    zorder 1000

    # --- Map button + Time tracker, grouped in the top-right corner ---
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
