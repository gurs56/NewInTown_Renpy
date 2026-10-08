# ==========================================================
# ACT 1 - SCENE A00: Intro - Bus Terminal
# ==========================================================
# LOCATION: On the Road
# CAST: MC (Narrator / V.O.)
# OBJECTIVE: Arrive in Crescent City
#
# Told entirely over POSTERS (one-shot paintings). See
# Scripts/Posters/Posters.rpy - the names below are canonical and
# must match the final art filenames in images/Posters/.
#
# Follows NewInTown_V5_01_A. That draft cuts the hospital beat
# (poster "A00 - Mothers_Hands") and no longer names the father,
# so both are gone from this scene. The narration is now four
# posters instead of five, and much terser - it withholds what
# happened to his mother so A01's reveal lands cold.
# ==========================================================

# The Narrator (MC's internal monologue / voice-over).
# Character(None) = no name shown; italics mark it as a thought.
# NOTE: the MC Character itself lives in Characters/MC.rpy.
define vo = Character(None, what_prefix="{i}", what_suffix="{/i}", what_color="#cccccc")


label A00_INTRO_BUS_TERMINAL:

    # ----- Poster: A00 - Intercity_Bus -----
    # A lone intercity bus on an empty two-lane road. MC sits by the
    # window looking far off, raindrops on the pane. He is the only
    # passenger left.
    scene expression Poster("A00 - Intercity_Bus") with fade

    vo "Fourteen hours, two transfers, and only one peanut and jelly sandwich."
    vo "All to chase some man."

    # ----- Poster: A00 - Old_Photo -----
    # MC holds a worn old photo: a man and a woman holding each other
    # outside a country fair. His thumb covers the man's face.
    scene expression Poster("A00 - Old_Photo") with dissolve

    vo "I don't know this man. I have never met him. All I've got is a face, a name, and a ring."
    vo "Mom always said, \"What's in the past should stay in the past\"."
    vo "…"
    vo "But…"
    vo "…She isn't here to argue that anymore."

    # ----- Poster: A00 - Bus_City -----
    # The bus winds through the city streets, past the spilled bean,
    # pedestrians and students on the sidewalks. The bad weather
    # fades as a dim sunlight rises.
    scene expression Poster("A00 - Bus_City") with dissolve

    vo "The bus driver says this is the last stop."
    vo "This isn't just my last stop, but my last chance."
    vo "One last chance to find all my answers."

    # ----- Poster: A00 - Step_off -----
    # Semi-aerial: MC steps off the bus and looks up at the apartment
    # buildings in front of him. Sunlight breaks through the cloud.
    scene expression Poster("A00 - Step_off") with dissolve

    vo "I do not have much of a plan."
    vo "Ms. Lopez is the only plan I have."
    vo "Mom said she could help…"
    vo "A place to stay…"
    vo "Maybe answers too…"

    # FADE OUT - end of A00
    scene black with fade
    return
