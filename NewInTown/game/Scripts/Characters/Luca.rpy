# Luca Character Definition
define Luca = Character("Luca", color="#4a90e2", image="Luca")

# ==========================================================
# EXPRESSIONS (placeholder)
# ==========================================================
# All moods share one placeholder sprite. Add a new mood by
# dropping its name in this list - no missing-image crashes.
init python:
    for _m in ["neutral", "serious", "pleased", "boastful", "unbothered"]:
        renpy.image("Luca " + _m, im.Scale("images/Test_Characters/body1_4.png", 600, 900))
    del _m
