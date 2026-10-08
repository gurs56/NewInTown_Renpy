
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
    # Mirrors the pose sheet: # / pose (aliases) / art status.
    # ------------------------------------------------------
    Uncle_poses = [
        "idle",         #  1 Idle                               Finished
        "explaining",   #  2 Explaining (Talking/Lecturing)     Finished
        "laughing",     #  3 Laughing (Mocking)                 Finished
        "wise",         #  4 Wise                               Finished
        "celebrating",  #  5 Celebrating (Excited)              HOLD
        "happy",        #  6 Happy (Standard Smile)             Inked
        "confused",     #  7 Confused (Curious/Thinking)        Finished
        "guilty",       #  8 Guilty (Defensive/Apologetic)      Inked
        "sad",          #  9 Sad                                Finished
        "shocked",      # 10 Shocked (Surprised/Awkward)        -
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

    # Poses with finished art (pose name -> art file).
    Uncle_pose_art = {
        "idle": "images/Characters/Uncle/NIT_CH_UNCLE_CASUAL_STAND_IDLE_FIN_V01.png",
        "explaining": "images/Characters/Uncle/NIT_CH_UNCLE_CASUAL_STAND_EXPLAINING_FIN_V01.png",
        "laughing": "images/Characters/Uncle/NIT_CH_UNCLE_CASUAL_STAND_LAUGH_FIN_V01.png",
        "wise": "images/Characters/Uncle/NIT_CH_UNCLE_CASUAL_STAND_WISE_FIN_V01.png",
        "confused": "images/Characters/Uncle/NIT_CH_UNCLE_CASUAL_STAND_CONFUSED_FIN_V01.png",
        "sad": "images/Characters/Uncle/NIT_CH_UNCLE_CASUAL_STAND_SAD_FIN_V01.png",
    }

    # What a pose with no art of its own falls back to. His finished
    # idle reads far better mid-scene than the grey placeholder body -
    # A01 alone asks for happy, guilty and shocked, none of them drawn.
    Uncle_default_art = Uncle_pose_art["idle"]

    # Legacy words that are just aliases of a pose above with finished art.
    # (mocking/curious come straight from the pose sheet's own aliases.)
    Uncle_legacy_art_alias = {
        "neutral": "idle",
        "mocking": "laughing",
        "curious": "confused",
    }

    # Poses (and their legacy aliases) listed above use their own art;
    # everything else draws his idle until that pose is drawn.
    for _m in Uncle_poses + Uncle_legacy_moods:
        if _m in Uncle_pose_art:
            renpy.image("Uncle " + _m, framed_sprite("Uncle", Uncle_pose_art[_m]))
        elif _m in Uncle_legacy_art_alias:
            renpy.image("Uncle " + _m, framed_sprite("Uncle", Uncle_pose_art[Uncle_legacy_art_alias[_m]]))
        else:
            renpy.image("Uncle " + _m, framed_sprite("Uncle", Uncle_default_art))
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
