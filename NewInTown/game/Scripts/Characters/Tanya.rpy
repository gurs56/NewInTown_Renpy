# Tanya Character Definition
define Tanya = Character("Tanya", color="#ff9933", image="Tanya")

# ==========================================================
# EXPRESSIONS (placeholder)
# ==========================================================
# All moods share one placeholder sprite. Add a new mood by
# dropping its name in this list - no missing-image crashes.
init python:
    for _m in [
        "neutral", "friendly", "encouraging", "angry", "annoyed",
        "blushing", "composed", "explaining", "happy", "idle",
        "intrigued", "irritated", "laughing", "seductive", "welcoming",
    ]:
        renpy.image("Tanya " + _m, im.Scale("images/Test_Characters/body1_2.png", 600, 900))
    del _m

# ==========================================================
# FLAGS (presence + event)
# ==========================================================
default tanya_in_cafe = False
default tanya_has_event = False
