# Mr. Lee Character Definition
define MrLee = Character("Mr. Lee", color="#7ab547", image="MrLee")

# ==========================================================
# EXPRESSIONS (placeholder)
# ==========================================================
# The CANONICAL POSES below are the official pose list for the
# artist. These are the current pose names used by the scripts
init python:
    # ------------------------------------------------------
    # CANONICAL POSES - the official pose list (what the
    # artist will draw). This is the source of truth; add or
    # remove poses here as art is planned.
    # ------------------------------------------------------
    MrLee_poses = [
        "idle", "mad",
    ]

    # ------------------------------------------------------
    # LEGACY MOODS - older words still used by story scripts
    # that AREN'T canonical poses yet. Kept working (they show
    # the placeholder) so nothing crashes. To retire one:
    # change the script to a canonical pose above, then
    # delete the word here.
    # ------------------------------------------------------
    MrLee_legacy_moods = [
        "neutral", "strict",
    ]

    # Every pose shares one placeholder sprite for now. When real
    # art exists, replace this loop with proper per-pose images.
    for _m in MrLee_poses + MrLee_legacy_moods:
        renpy.image("MrLee " + _m, im.Scale("images/Test_Characters/body1_1.png", 600, 900))
    del _m

# ==========================================================
# FLAGS (presence + event)
# ==========================================================
default mr_lee_in_store = True
default mr_lee_has_event = False

# ==========================================================
# INTERACTION ROUTING
# ==========================================================
label talk_mr_lee:
    # Mr. Lee interaction handler
    hide screen grocery_store_interior_screen

    menu:
        "What would you like to say?"

        "Chat with Mr. Lee":
            call generic_mr_lee_chat
            show screen grocery_store_interior_screen
            jump exploration_loop

        "Ask about door hinges" if quest_get_hinges and not quest_check_uncle_shop:
            jump A02_3_MR_LEE_STORE

        # --- A03: job hunting (he says no) ---
        "Ask about a job" if quest_find_job and not job_bean_spill:
            jump A03_04_1_MR_LEE_JOB

        "Never mind":
            show screen grocery_store_interior_screen
            jump exploration_loop

# ==========================================================
# DIALOGUE
# ==========================================================
label generic_mr_lee_chat:
    scene bg grocery_store_interior with fade
    # show MrLee neutral

    MrLee "What do you want? You buying something or not?"

    MC "Just browsing, Mr. Lee."
    MrLee "Browsing doesn't pay the bills. Buy something or get out."

    return
