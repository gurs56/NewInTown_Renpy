# Coach DeShawn Character Definition
define CoachDeShawn = Character("Coach DeShawn", color="#2d5016", image="CoachDeShawn")

# ==========================================================
# EXPRESSIONS (placeholder)
# ==========================================================
# All moods share one placeholder sprite. Add a new mood by
# dropping its name in this list - no missing-image crashes.
init python:
    for _m in [
        "neutral", "apologetic", "confident", "idle", "surprised",
        "welcoming",
    ]:
        renpy.image("CoachDeShawn " + _m, im.Scale("images/Test_Characters/body1 3.png", 600, 900))
    del _m
