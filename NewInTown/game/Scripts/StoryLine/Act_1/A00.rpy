# ==========================================================
# DEFINITIONS
# ==========================================================

# The Main Character
define MC = Character("MC", color="#54c0f2", image="MC")

# The Narrator (Internal Monologue)
# We set this to italics ({i}) to show he is thinking to himself.
define vo = Character(None, what_prefix="{i}", what_suffix="{/i}", what_color="#cccccc")

# ==========================================================
# THE SCENE START
# ==========================================================

label A00_INTRO_BUS_TERMINAL:

    # --- SCENE A: BUS INTRO ---
    
    # [NOTE] Place your "Bus Exterior - Rainy" background here later
    # scene bg bus_rainy with dissolve
    
    # [NOTE] Place your MC sprite here (Sitting by window)
    # show mc sitting_sad at center

    vo "Ever feel like nothing really goes in your favor? The odds are seemingly always against you, making you wonder if things can get worse than this…"

    vo "Yeah… That’s basically my life right from the beginning…"

    # --- SCENE B: KITCHEN FLASHBACK ---

    # [NOTE] Transition effect for flashback
    scene black with fade
    
    # [NOTE] Place "Kitchen (Old House)" background here
    # scene bg kitchen_old
    
    # [NOTE] Place Mom sprite here (Stressed/On Phone)
    # show mom stressed at center

    vo "My mother did her best to raise me alone, trying to juggle everything all at once despite being ill for years… She pushed herself to the absolute limit…"

    vo "But because of that, her illness eventually caught up to her."

    # --- SCENE C: HOSPITAL FLASHBACK ---

    scene black with fade

    # [NOTE] Place "Hospital Room" background here OR a CG of holding hands
    # scene cg holding_mom_hand with dissolve

    vo "To be honest… We never really had a choice. We lived paycheck after paycheck, not knowing when our next meals would be. And frankly speaking, our efforts just delayed the inevitable…"

    vo "Until her body finally gave up…"

    # --- SCENE D: BUS INTERIOR (PRESENT DAY) ---

    scene black with fade

    # [NOTE] Place "Bus Interior" background here
    # scene bg bus_interior

    # [NOTE] Place "Old Photo" item image here
    # show item old_photo at truecenter

    vo "All she left me is a faded photo, a wedding band, and a name—Aaron Vale—my father."

    vo "I know nothing about him, but I can’t move on without answers. Where was he when we needed him? Does he even know what happened to her? Did he ever care at all?"

    vo "All these questions felt like a repeating noise to my brain… I need answers to finally close this chapter."

    # [NOTE] Hide the photo
    # hide item old_photo

    # --- SCENE E: ARRIVAL IN CITY ---

    # [NOTE] Place "City Skyline / Street" background here
    # scene bg city_street_morning with dissolve

    vo "This is where I will find my answers. Crescent City. A city like no other."

    # --- SCENE F: APARTMENT EXTERIOR ---

    # [NOTE] Place "Apartment Building Exterior" background here
    # scene bg apartment_exterior

    # [NOTE] Place MC sprite standing/looking up here
    # show mc standing_determined at center

    vo "First stop: find Ms. López. That would be the first piece of this puzzle—A place to stay and a step closer to the truth."

    # End of A00 - return to game loop
    return