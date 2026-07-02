
define Uncle = Character("Uncle", color="#c47f2b", image="Uncle")

# ==========================================================
# EXPRESSIONS (placeholder)
# ==========================================================
# All moods share one placeholder sprite. Add a new mood by
# dropping its name in this list - no missing-image crashes.
init python:
    for _m in [
        "neutral", "gruff", "amused", "explaining", "happy", "idle",
        "stern", "wise", "calm", "celebrating", "confused", "curious",
        "guilty", "mocking", "sad",
    ]:
        renpy.image("Uncle " + _m, im.Scale("images/Test_Characters/body1 4.png", 600, 900))
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
    """Uncle interaction handler"""
    hide screen apartment_alley_screen

    menu:
        "What would you like to say?"

        "Chat with Uncle":
            call generic_uncle_chat
            show screen apartment_alley_screen
            $ renpy.pause(hard=True)
            jump exploration_loop

        "Ask about door hinges" if quest_check_uncle_shop and not has_hinges:
            jump A02_4_UNCLE_PAWN_SHOP

        "Never mind":
            show screen apartment_alley_screen
            $ renpy.pause(hard=True)
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
