# ==========================================================
# ACT 1 - SCENE A05: Getting the Apartment
# ==========================================================
# Location: Apartment Lobby, MC's New Apartment (3rd Floor)
# Cast: MC, Ms. Lopez, Amber
# Objective: Receive apartment as reward for hard work
# ==========================================================

# ==========================================================
# SCENE A05_01 - Eavesdropping on Ms. Lopez and Amber
# ==========================================================
label A05_01_EAVESDROP_LOBBY:
    
    # Fade in
    scene bg apartment_lobby with fade
    
    # Show Ms. Lopez and Amber talking
    # show MsLopez explaining
    # show Amber sassy
    
    "MC went back to the front counter lobby to report progress. MC then finds Ms. Lopez and Amber talking about him. The player eavesdrops and will soon be spotted."
    
    Amber sassy "So, what's with this new handyman of yours?"
    
    MsLopez explaining "He's the son of an old friend."
    
    MsLopez "It's actually a long story, but the boy looks promising."
    
    Amber seductive "Yeah… I'm guessing it is indeed looong~"
    
    MsLopez happy "I don't usually let others stay for free. But MC has been fixing some problems around here."
    
    MsLopez smirk "Plus, that boy is kinda cute."
    
    Amber idle "He sure is~"
    
    Amber "And speaking of your cute pervy boy, he is again lurking around."
    
    # Unique pose: Both look at MC entering
    
    MC flustered "Oh, no-no."
    
    MC "I—I didn't mean to eavesdrop; I was just looking for Ms. Lopez."
    
    MC "Razor already fixed the pipes!"
    
    MsLopez happy "Yeah, Razor already told us when he passed by."
    
    MsLopez excited "And because of that, we have a surprise for you. Follow me on the third floor beside Amber's place!"
    
    # Set quest flag
    $ quest_report_lopez_water = False
    $ quest_follow_lopez_apartment = True
    
    # Fade out
    scene black with fade
    
    return

# ==========================================================
# SCENE A05_02 - Receiving the Apartment
# ==========================================================
label A05_02_NEW_APARTMENT:
    
    # Fade in
    scene bg apartment_mc_apartment with fade
    
    # Show Ms. Lopez and Amber
    # show MsLopez excited
    # show Amber sassy
    
    "MC's new room in the building. A proper apartment containing a bedroom, kitchen, and bathroom."
    
    MsLopez excited "Surprised!!"
    
    MsLopez "Here's a new room for you. Mostly empty. But at least the 1st month of rent is free!"
    
    # Unique pose: Ms. Lopez hugs MC
    
    # Player choice menu
    menu:
        "Appreciate the surprise":
            jump option1_appreciate
        
        "Question why":
            jump option2_question

# Option 1: Appreciate
label option1_appreciate:
    
    MC happy "Really!?"
    
    MC "Thank you so much!"
    
    MsLopez happy "Don't sweat it, kid."
    
    MsLopez "Consider it as a return of your mom's help before."
    
    jump both_apartment_options_continue

# Option 2: Question why
label option2_question:
    
    MC confused "Wait, what?"
    
    MC "Why?"
    
    MsLopez happy "Well, you seemed like a genuine kid."
    
    MsLopez "Consider it as a return of your mom's help before."
    
    jump both_apartment_options_continue

# Both options continue here
label both_apartment_options_continue:
    
    MsLopez explaining "And besides, I only covered half of it."
    
    MsLopez "Ms. Amber over here covered the other half~"
    
    Amber sassy "Don't get the wrong impression, pervy."
    
    Amber "You are placed here near me so you can help me when I need it."
    
    MC shy "I see… I'll keep that in mind, hehe…"
    
    MsLopez explaining "Also, don't forget. We are only covering the rent for this month."
    
    MsLopez "You are on your own after that."
    
    MC determined "I understand. I already landed a gig in the cafe nearby."
    
    MC "I'll make sure to pay on time."
    
    MsLopez happy "That's good to hear."
    
    MsLopez "We'll let you settle in for now."
    
    Amber seductive "See you around, but not when I'm changing clothes~"
    
    # hide MsLopez
    # hide Amber
    
    "Amber and Ms. Lopez left the room."
    
    MC "Finally… My efforts did not fail me."
    
    MC determined "I should settle in first."
    
    # Transition: unpacking scene
    scene black with fade
    
    "MC unpacked his stuff in his apartment. Clothes in the cabinet, notebooks and pens on the desk, a night lamp, etc."
    
    scene bg apartment_mc_apartment with fade
    
    MC tired "Wooooh…"
    
    MC "That was exhausting."
    
    MC proud "But at least I finally secured a place to sleep. Tomorrow is the start of a new beginning."
    
    # Set quest flags
    $ quest_follow_lopez_apartment = False
    $ has_apartment = True
    $ quest_go_to_work = True
    $ quest_find_father_clues = True
    
    # Fade out
    scene black with fade
    
    return

# ==========================================================
# END OF A05 SCENES - END OF ACT 1 ARC A
# ==========================================================

