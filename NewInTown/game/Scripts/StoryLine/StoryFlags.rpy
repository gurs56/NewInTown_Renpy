# ==========================================================
# STORY / QUEST FLAGS (shared across characters & acts)
# ==========================================================
# These flags track story progress and are read/written by
# MULTIPLE characters and acts, so they live here rather than
# under any single character. Per-character presence/event
# flags live in that character's file (e.g. Characters/Amber.rpy).
# ==========================================================

# ----------------------------------------------------------
# QUEST FLAGS
# ----------------------------------------------------------
default quest_meet_ms_lopez_complete = False
default quest_fix_amber_door_started = False
default quest_fix_amber_door_complete = False
default quest_get_hinges = False
default quest_check_uncle_shop = False
default pawned_ring = False
default has_hinges = False
default refused_pawn = False
default quest_get_ring_back = False
default quest_find_job_started = False
default quest_find_job_complete = False
default quest_hot_water_fixed = False
default has_apartment = False

# ----------------------------------------------------------
# QUEST FLAGS used by Act scripts A03-A05.
# Every flag the scripts touch is declared here - an undeclared
# flag crashes if a screen or menu condition reads it first.
# One name per quest step; old duplicate names were removed.
# ----------------------------------------------------------
default quest_ask_lopez_magazines = False
default quest_ask_razor_help = False
default quest_check_leak = False
default quest_find_father_clues = False
default quest_find_job = False
default quest_fix_hot_water = False
default quest_fix_with_razor = False
default quest_follow_lopez_apartment = False
default quest_go_to_work = False
default quest_report_lopez_water = False
default quest_secure_apartment = False

# Job / discovery flags set by A03-A04
default job_bean_spill = False
default found_magazines = False

# Relationship points (grow these as more characters get them)
default razor_relationship = 0

# Story scene flag (hides characters during cutscenes)
default in_story_scene = True

# ==========================================================
# CHARACTER EVENT SETUP LABELS
# ==========================================================
# Call these to switch on the next act's event(s).

# NOTE: these use # comments, not """docstrings""" - a bare string
# inside a label is a SAY statement in Ren'Py and would show on screen.

label setup_a02_event:
    # Enable A02 - Fixing Amber's Door
    $ ms_lopez_has_event = True
    return

label setup_a03_event:
    # Enable A03 - Job Interview
    $ ms_lopez_has_event = True
    $ quest_find_job_started = True
    return

label setup_a04_event:
    # Enable A04 - Hot Water
    $ ms_lopez_has_event = True
    return

label setup_a05_event:
    # Enable A05 - Getting Apartment
    $ ms_lopez_has_event = True
    return
