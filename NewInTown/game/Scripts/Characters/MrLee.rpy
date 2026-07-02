# Mr. Lee Character Definition
define MrLee = Character("Mr. Lee", color="#7ab547", image="MrLee")

# ==========================================================
# EXPRESSIONS (placeholder)
# ==========================================================
# All moods share one placeholder sprite. Add a new mood by
# dropping its name in this list - no missing-image crashes.
init python:
    for _m in ["neutral", "apologetic", "mad", "strict"]:
        renpy.image("MrLee " + _m, im.Scale("images/Test_Characters/body1 1.png", 600, 900))
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
    """Mr. Lee interaction handler"""
    hide screen grocery_store_interior_screen

    menu:
        "What would you like to say?"

        "Chat with Mr. Lee":
            call generic_mr_lee_chat
            show screen grocery_store_interior_screen
            $ renpy.pause(hard=True)
            jump exploration_loop

        "Ask about door hinges" if quest_get_hinges and not quest_check_uncle_shop:
            jump A02_3_MR_LEE_STORE

        "Never mind":
            show screen grocery_store_interior_screen
            $ renpy.pause(hard=True)
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
