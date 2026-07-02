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
# QUEST FLAGS used by Act scripts (A03/A04/A05) that were being
# assigned in-scene without a default. Undeclared flags crash if
# a screen/menu condition reads them before they're ever set, so
# every flag the scripts touch is declared here.
# NOTE: several of these overlap older flags above (e.g.
# quest_fix_amber_door vs quest_fix_amber_door_started). Worth
# consolidating to ONE name per quest later - see review notes.
# ----------------------------------------------------------
default quest_amber_door_complete = False
default quest_ask_lopez_magazines = False
default quest_ask_razor_help = False
default quest_check_leak = False
default quest_find_father_clues = False
default quest_find_job = False
default quest_fix_amber_door = False
default quest_fix_door = False
default quest_fix_hot_water = False
default quest_fix_with_razor = False
default quest_follow_lopez_apartment = False
default quest_get_job = False
default quest_go_to_work = False
default quest_report_lopez_water = False
default quest_report_ms_lopez = False
default quest_secure_apartment = False

# Story scene flag (hides characters during cutscenes)
default in_story_scene = True

# ==========================================================
# CHARACTER EVENT SETUP LABELS
# ==========================================================
# Call these to switch on the next act's event(s).

label setup_a02_event:
    """Enable A02 - Fixing Amber's Door"""
    $ ms_lopez_has_event = True
    return

label setup_a03_event:
    """Enable A03 - Job Interview"""
    $ ms_lopez_has_event = True
    $ quest_find_job_started = True
    return

label setup_a04_event:
    """Enable A04 - Hot Water"""
    $ ms_lopez_has_event = True
    return

label setup_a05_event:
    """Enable A05 - Getting Apartment"""
    $ ms_lopez_has_event = True
    return
