

# ==========================================================
# TIME DISPLAY + ADVANCE BUTTON
# ==========================================================
# Shows current day and time in the top-right corner.
# "Advance Time" button is disabled at Night — player must sleep.
screen time_display():
    zorder 1000

    # --- Day and Time display (top-right corner) ---
    frame:
        xalign 0.98
        yalign 0.02
        padding (10, 10)

        vbox:
            spacing 2
            text "[time_of_day.day_name]" size 24 xalign 0.5 bold True
            text "[time_of_day.current]" size 20 xalign 0.5
            text "Week [time_of_day.week_number]" size 16 xalign 0.5 color "#aaaaaa"

    # --- Advance Time button (top-center) ---
    if not time_of_day.is_night():
        # Normal: can advance time
        button:
            xalign 0.5
            yalign 0.02
            padding (15, 10)
            action Function(time_of_day.advance)
            text "Advance Time" size 20
    else:
        # Night: blocked — must sleep
        frame:
            xalign 0.5
            yalign 0.02
            padding (15, 10)
            text "Go to bed to sleep" size 20 color "#ff9999"
