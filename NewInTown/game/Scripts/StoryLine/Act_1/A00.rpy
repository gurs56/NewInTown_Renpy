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
# ==========================================================

# The Narrator (MC's internal monologue / voice-over).
# Character(None) = no name shown; italics mark it as a thought.
# NOTE: the MC Character itself lives in Characters/MC.rpy.
define vo = Character(None, what_prefix="{i}", what_suffix="{/i}", what_color="#cccccc")


label A00_INTRO_BUS_TERMINAL:

    # ----- Poster: A00 - Intercity_Bus -----
    # A lone intercity bus on an empty road; MC by the window,
    # raindrops on the glass, close-up on his sad expression.
    scene expression Poster("A00 - Intercity_Bus") with fade

    vo "Ever feel like nothing really goes in your favor? The odds are seemingly always against you, making you wonder if things can get worse than this…"
    vo "Yeah… That's basically my life right from the beginning…"

    # ----- Poster: A00 - Mothers_Hands -----
    # Young MC's POV holding his mother's IV-lined hand; she's weak
    # in the background, oxygen mask on, heart monitor beside her.
    scene expression Poster("A00 - Mothers_Hands") with dissolve

    vo "My mother did her best to raise me alone. She pushed herself to the absolute limit…"
    vo "But because of that, her illness eventually caught up to her."
    vo "To be honest… We never really had a choice. We lived paycheck after paycheck, not knowing when our next meals would be."
    vo "Until her body finally gave up…"

    # ----- Poster: A00 - Old_Photo -----
    # MC holds a worn old photo, empty seats behind him, gloomy
    # weather outside; grief lingering as he holds back emotion.
    scene expression Poster("A00 - Old_Photo") with dissolve

    vo "All she left me is a faded photo, a wedding band, and a name — Aaron Vale — my father."
    vo "I know nothing about him, but I can't move on without answers. Where was he when we needed him? Does he even know what happened to her? Did he ever care at all?"
    vo "All these questions felt like a repeating noise to my brain… I need answers to finally close this chapter."

    # ----- Poster: A00 - Bus_City -----
    # The bus winds through city streets past the grand library and
    # the glowing Tech Cafe; the bad weather fades to dim sunlight.
    scene expression Poster("A00 - Bus_City") with dissolve

    vo "This is where I will find my answers. Crescent City. A city like no other."

    # ----- Poster: A00 - Step_off -----
    # Semi-aerial: MC steps off the bus, photo in hand, looking up
    # at the apartments as sunlight breaks through the dark cloud.
    scene expression Poster("A00 - Step_off") with dissolve

    vo "First stop: find Ms. López. Mom said she'd help."
    vo "A place to stay, and maybe — if I'm lucky — someone who knew them both."

    # FADE OUT - end of A00
    scene black with fade
    return
