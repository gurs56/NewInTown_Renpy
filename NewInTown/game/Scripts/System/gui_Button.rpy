

# Screen to display current time
screen time_display():
    zorder 1000
    
    frame:
        xalign 0.98
        yalign 0.02
        padding (10, 10)
        
        text "[time_of_day.current]" size 24
    
    # Time advance button - top center
    button:
        xalign 0.5
        yalign 0.02
        padding (15, 10)
        action Function(time_of_day.advance)
        
        text "Advance Time" size 20
