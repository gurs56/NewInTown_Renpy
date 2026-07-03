
define Uncle = Character("Uncle", color="#c47f2b", image="Uncle")

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
    Uncle_poses = [
        "idle", "explaining", "laughing", "wise", "celebrating", "happy",
        "confused", "guilty", "sad", "shocked",
    ]

    # ------------------------------------------------------
    # LEGACY MOODS - older words still used by story scripts
    # that AREN'T canonical poses yet. Kept working (they show
    # the placeholder) so nothing crashes. To retire one:
    # change the script to a canonical pose above, then
    # delete the word here.
    # ------------------------------------------------------
    Uncle_legacy_moods = [
        "calm", "curious", "mocking", "neutral", "stern",
    ]

    # Every pose shares one placeholder sprite for now. When real
    # art exists, replace this loop with proper per-pose images.
    for _m in Uncle_poses + Uncle_legacy_moods:
        renpy.image("Uncle " + _m, im.Scale("images/Test_Characters/body1_4.png", 600, 900))
    del _m

# ==========================================================
# FLAGS (presence + event)
# ==========================================================
default uncle_in_alley = True
default uncle_has_event = False

# ==========================================================
# INTERACTION ROUTING
# ==========================================================
label talk_uncle:
    # Uncle interaction handler
    hide screen apartment_alley_screen

    menu:
        "What would you like to say?"

        "Chat with Uncle":
            call generic_uncle_chat
            show screen apartment_alley_screen
            jump exploration_loop

        "Ask about door hinges" if quest_check_uncle_shop and not has_hinges:
            jump A02_4_UNCLE_PAWN_SHOP

        "Never mind":
            show screen apartment_alley_screen
            jump exploration_loop

# ==========================================================
# DIALOGUE
# ==========================================================
label generic_uncle_chat:
    scene bg apartment_alley with fade
    # show Uncle neutral

    Uncle "Well, well... if it isn't my favorite nephew."

    MC "Hey Uncle, how's business?"
    Uncle "Same as always. People pawn their junk, I sell it. Circle of life."

    return
