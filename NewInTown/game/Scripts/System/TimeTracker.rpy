
init python:
    # Time tracking system
    class TimeOfDay:
        def __init__(self):
            self.periods = ["Early Morning", "Morning", "Afternoon", "Evening", "Night"]
            self.current_index = 0
            
        @property
        def current(self):
            """Get the current time of day"""
            return self.periods[self.current_index]
        
        def advance(self):
            """Move to the next time period"""
            self.current_index = (self.current_index + 1) % len(self.periods)
            # Trigger screen update
            renpy.restart_interaction()
        
        def set_time(self, time_name):
            """Set time to a specific period"""
            if time_name in self.periods:
                self.current_index = self.periods.index(time_name)
                return True
            return False
        
        def is_morning(self):
            """Check if it's any morning period"""
            return self.current in ["Early Morning", "Morning"]
        
        def is_night(self):
            """Check if it's night"""
            return self.current == "Night"

# Initialize the time system
default time_of_day = TimeOfDay()

# Label to advance time (call this when you want time to progress)
label advance_time:
    $ new_day = time_of_day.advance()
    
    if new_day:
        "A new day begins..."
    else:
        "Time passes... It's now [time_of_day.current]."
    
    return

