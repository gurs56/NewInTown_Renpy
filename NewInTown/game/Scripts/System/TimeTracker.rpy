
# ==========================================================
# TIME TRACKER SYSTEM
# ==========================================================
# Tracks both time of day and day of the week.
#
# TIME OF DAY (5 periods):
#   Early Morning → Morning → Afternoon → Evening → Night
#   - Player can advance through these by clicking "Advance Time"
#   - At Night, advancing is BLOCKED — player must SLEEP to continue
#
# DAY OF WEEK (7-day cycle):
#   Monday → Tuesday → Wednesday → Thursday → Friday → Saturday → Sunday
#   - Day advances automatically when the player sleeps
#   - Use is_weekend() / is_weekday() to control character schedules
#
# WEEK COUNTER:
#   Tracks how many weeks have passed (starts at week 1)
#
# HOW TO USE IN SCRIPTS:
#   time_of_day.current        → "Morning" (current time period)
#   time_of_day.day_name       → "Monday" (current day)
#   time_of_day.day_short      → "Mon" (short day name)
#   time_of_day.week_number    → 1 (current week)
#   time_of_day.is_morning()   → True/False
#   time_of_day.is_night()     → True/False (blocked from advancing)
#   time_of_day.is_weekend()   → True if Saturday or Sunday
#   time_of_day.is_weekday()   → True if Monday-Friday
#   time_of_day.is_day("Friday") → True if it's Friday
#   time_of_day.advance()      → Move to next time period (blocked at Night)
#   time_of_day.sleep()        → Sleep: advance to next day's Early Morning
#   time_of_day.set_time("Afternoon") → Jump to specific time
#   time_of_day.set_day("Saturday")   → Jump to specific day
#
# SLEEP MECHANIC:
#   - Player MUST go to MC's Bedroom and click "Sleep" at Night
#   - This calls the "go_to_sleep" label which plays a transition
#     and advances to the next day's Early Morning
#   - The "Advance Time" button is disabled at Night
# ==========================================================

init python:
    class TimeOfDay:
        def __init__(self):
            # --- Time periods in a single day ---
            self.periods = ["Early Morning", "Morning", "Afternoon", "Evening", "Night"]

            # --- Days of the week ---
            self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

            # --- Current state ---
            self.current_index = 0   # Index into self.periods (0 = Early Morning)
            self.day_index = 0       # Index into self.days (0 = Monday)
            self.week_number = 1     # Tracks how many weeks have passed

        # ------------------------------------------------------
        # PROPERTIES (read-only, use in screens with [ ] syntax)
        # ------------------------------------------------------

        @property
        def current(self):
            """Get the current time of day (e.g. 'Morning')"""
            return self.periods[self.current_index]

        @property
        def day_name(self):
            """Get the current day name (e.g. 'Monday')"""
            return self.days[self.day_index]

        @property
        def day_short(self):
            """Get short day name (e.g. 'Mon')"""
            return self.day_name[:3]

        # ------------------------------------------------------
        # TIME ADVANCEMENT
        # ------------------------------------------------------

        def advance(self):
            """
            Move to the next time period.
            BLOCKED at Night — player must use sleep() instead.
            Returns True if time was advanced, False if blocked.
            """
            # Can't advance past Night — must sleep!
            if self.current == "Night":
                return False

            self.current_index += 1

            # Trigger screen update so the display refreshes
            renpy.restart_interaction()
            return True

        def sleep(self):
            """
            Sleep: advance to the next day's Early Morning.
            Can only be called at Night.
            Returns True if sleep happened, False if not Night.
            """
            if self.current != "Night":
                return False

            # Reset time to Early Morning
            self.current_index = 0

            # Advance to next day
            self.day_index += 1

            # If we passed Sunday, wrap to Monday and increment week
            if self.day_index >= len(self.days):
                self.day_index = 0
                self.week_number += 1

            # Trigger screen update
            renpy.restart_interaction()
            return True

        # ------------------------------------------------------
        # SETTERS (for scripted events)
        # ------------------------------------------------------

        def set_time(self, time_name):
            """Set time to a specific period (e.g. 'Afternoon')"""
            if time_name in self.periods:
                self.current_index = self.periods.index(time_name)
                return True
            return False

        def set_day(self, day_name):
            """Set to a specific day (e.g. 'Saturday')"""
            if day_name in self.days:
                self.day_index = self.days.index(day_name)
                return True
            return False

        # ------------------------------------------------------
        # CHECKERS (use in if-statements and screen conditions)
        # ------------------------------------------------------

        def is_morning(self):
            """True if Early Morning or Morning"""
            return self.current in ["Early Morning", "Morning"]

        def is_night(self):
            """True if Night (advance is blocked, must sleep)"""
            return self.current == "Night"

        def is_weekend(self):
            """True if Saturday or Sunday"""
            return self.day_name in ["Saturday", "Sunday"]

        def is_weekday(self):
            """True if Monday through Friday"""
            return not self.is_weekend()

        def is_day(self, day_name):
            """True if it's a specific day (e.g. time_of_day.is_day('Friday'))"""
            return self.day_name == day_name

# ==========================================================
# INITIALIZE THE TIME SYSTEM
# ==========================================================
default time_of_day = TimeOfDay()

# ==========================================================
# SLEEP LABEL — Called when player clicks "Sleep" in bedroom
# ==========================================================
# This plays a transition and advances to the next day.
# The sleep button in MC's bedroom jumps to this label.
label go_to_sleep:
    # Hide the bedroom screen
    hide screen apartment_mc_bedroom_screen

    # Fade to black
    scene black with fade

    # Actually sleep — advance to next day
    $ time_of_day.sleep()

    # Show a message
    "You go to sleep..."
    "A new day begins. It's [time_of_day.day_name], [time_of_day.current]."

    # Return to bedroom
    show screen apartment_mc_bedroom_screen
    jump exploration_loop

