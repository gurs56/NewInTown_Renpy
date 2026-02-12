# ==========================================================
# ACT 1 - SCENE A02: Fixing Amber's Door
# ==========================================================
# Location: Apartment Lobby, Amber's Apartment, Mr. Lee's Store, Uncle's Pawn Shop
# Cast: MC, Ms. Lopez, Amber, Mr. Lee, Uncle
# Objective: Fix Amber's door by obtaining hinges
# ==========================================================

# ==========================================================
# SCENE A02_1 - Meeting Ms. Lopez at the Lobby
# ==========================================================
label A02_1_LOBBY_TASK:
    
    # Fade in
    scene bg apartment_lobby with fade
    
    # Show Ms. Lopez at counter (add character when available)
    # show MsLopez idle
    
    "MC meets Ms. Lopez at the front counter of the lobby and asks for the details of his first task."
    
    MsLopez stressed "Here's the deal."
    
    MsLopez "Amber's door has been broken for 2 weeks. The regular repair is charging me $400 to fix some simple hinges."
    
    MsLopez "It's a stiff price for a door hinge repair, you know."
    
    MsLopez "Do you think you could go up to Amber's room and have a look?"
    
    # Player choice menu
    menu:
        "Promise to handle the situation":
            jump option1_promise
        
        "Ask who Amber is":
            jump option2_ask_amber

# Option 1: Promise to handle it
label option1_promise:
    
    MC confident "That's a regular situation at my place. I'll fix it in no time."
    
    MsLopez idle "Great. Just head to Amber's place and you'll see the door that never closes."
    
    jump both_options_continue

# Option 2: Ask who Amber is
label option2_ask_amber:
    
    MC confused "Sure! But… Umm, who is Amber?"
    
    MsLopez idle "Amber is one of the tenants here. She's really a hard-working mother, just like Jessia."
    
    jump both_options_continue

# Both options continue here
label both_options_continue:
    
    MsLopez stressed "I feel so bad for not being able to fix her door for quite some time now."
    
    MsLopez "To compromise, I told her to hold off on rent for the month, but she wouldn't take no for an answer."
    
    MC determined "That's unfortunate. Don't worry, I'll handle this one. How hard could it be?"
    
    MsLopez stern "I love the spirit, but if this is proving to be too difficult, the responsible thing would be to own up to it."
    
    MC confused "I'll keep that in mind… Umm, where is Amber's room, again?"
    
    MsLopez stressed "Third floor, to the left."
    
    MC shy "Hahaha."
    
    MC "Got it."
    
    # Set quest flag
    $ quest_fix_amber_door_started = True
    $ amber_in_hallway = True
    $ amber_has_event = True
    
    # Fade out
    scene black with fade
    
    $ in_story_scene = False
    show screen apartment_lobby_screen
    jump exploration_loop

# ==========================================================
# SCENE A02_2 - Amber's Apartment
# ==========================================================
label A02_2_AMBER_DOOR:
    
    # Fade in
    scene bg apartment_amber_apartment with fade
    
    # Show Amber in underwear/bra (use appropriate pose when available)
    # show Amber underwear
    
    MC curious "Hello? I'm here about the door."
    
    # MC sees Amber, eyes widen, blushes
    
    Amber sassy "Great… As if my life wasn't messy enough—now I have to deal with perverts."
    
    MC panicking "A—ahhh… I—it's not what it looks like. Ms. López sent me. I swear, I'm here to fix hinges!"
    
    Amber sassy "Really? She sent a little pervy to fix my door."
    
    Amber "What do you even know about fixing doors?"
    
    MC polite "My mom taught me to fix what breaks—if it breaks again, then fix and fix it again."
    
    MC "It's kinda what we do, relying only on ourselves… I just hope I'm up to it."
    
    # Amber softens
    
    Amber irritated "Fine…"
    
    Amber "I guess beggars can't be choosers, but if you mess it up worse, you'll owe more than rent."
    
    MC happy "I—I promise not to let you down!"
    
    # MC stares and blushes, Amber notices
    
    Amber smirk "Chop-chop hinges first, staring later. Time to man up with your words."
    
    MC "Right—hinges. I'll head to Mr. Lee's Convenience."
    
    # Set quest flag
    $ quest_get_hinges = True
    
    # Fade out
    scene black with fade
    
    return

# ==========================================================
# SCENE A02_3 - Mr. Lee's Convenience Store
# ==========================================================
label A02_3_MR_LEE_STORE:
    
    # Fade in
    scene bg mr_lee_store with fade
    
    # Show Mr. Lee (add character when available)
    # show MrLee strict
    
    MC curious "Good afternoon, how much for this door hinge?"
    
    MrLee strict "15 dollars."
    
    MC shy "Well, about that… I actually don't have money?"
    
    MrLee mad "Out of my store. No free here."
    
    MC bargaining "Yes, I understand, but maybe we can…"
    
    MrLee mad "NO FREE. OUT!"
    
    MC scared "OK. OK."
    
    MC "I'm sorry."
    
    MC thinking "Maybe some other place has hinges…"
    
    MC "I should check around."
    
    # Set quest flag
    $ quest_check_uncle_shop = True
    
    # Fade out
    scene black with fade
    
    return

# ==========================================================
# SCENE A02_4 - Uncle's Pawn Shop
# ==========================================================
label A02_4_UNCLE_PAWN_SHOP:
    
    # Fade in
    scene bg uncle_pawn_shop with fade
    
    # Show Uncle (add character when available)
    # show Uncle happy
    
    MC happy "Hey, Uncle."
    
    Uncle happy "Oh, MC. Looks like the old hag is already putting you to work. What can I do for you, Sonny?"
    
    MC explaining "Hahaha, she does."
    
    MC "I actually have been running around, looking for some door hinges. But sadly, I can't afford one."
    
    Uncle idle "Well, I have a pair here."
    
    MC happy "That's exactly what I need! You are a lifesaver."
    
    # MC reaches for hinges, Uncle stops him
    
    Uncle stern "Slow down, kid. This is a Pawn shop, not a get-free shop."
    
    MC bargaining "But Uncle, I don't have anything to give…"
    
    MC "The only thing I have is this picture of my dad and my mom's wedding band."
    
    Uncle wise "Well… you could pawn the ring?"
    
    MC hesitant "…"
    
    MC sad "How could I? This is the only thing I have left of my mom…"
    
    Uncle explaining "Don't worry, kid. It's not like it's going away. I will hold on to it for you until you can get it back."
    
    MC worried "But what if someone buys it before I can get it back?"
    
    Uncle wise "Well, that's just life, kid. You either take the risk or play it safe."
    
    # Player choice menu
    menu:
        "Pawn the ring":
            jump option1_pawn_ring
        
        "Do not pawn the ring":
            jump option2_no_pawn

# Option 1: Pawn the ring
label option1_pawn_ring:
    
    MC bargaining "Ok…"
    
    MC sad "Can you please hold on to it until I can buy it back?"
    
    Uncle explaining "Well, I can try, but you'd better be quick. I can't hold this forever; it's a business after all."
    
    MC sad "Sigh…"
    
    MC "I guess I don't have a choice…"
    
    # Set flags
    $ pawned_ring = True
    $ has_hinges = True
    $ quest_get_ring_back = True
    
    "MC gives the ring to Uncle."
    
    # Fade out
    scene black with fade
    
    # Continue to fixing the door
    jump A02_5_FIX_DOOR

# Option 2: Don't pawn the ring (forces player to reconsider)
label option2_no_pawn:
    
    MC thinking "(...)"
    
    MC thinking "(What should I do?)"
    
    MC thinking "(I cannot just let go of my mother's ring.)"
    
    MC sad "I'll think about it first…"
    
    "MC leaves Uncle's Pawnshop."
    
    # Set flag for limited access
    $ refused_pawn = True
    
    # Fade out
    scene black with fade
    
    return

# ==========================================================
# CALLBACK SCENES - Player must return to pawn shop
# ==========================================================

# Attempt to visit Mr. Lee again
label A02_CALLBACK_MR_LEE:
    
    scene bg mr_lee_store_exterior with fade
    
    MC "Going back in there without money is probably not a good idea…"
    
    "MC leaves the area."
    
    scene black with fade
    
    return

# Attempt to ask Ms. Lopez for help
label A02_CALLBACK_MS_LOPEZ:
    
    scene bg apartment_lobby with fade
    
    # show MsLopez idle
    
    MC polite "Hi, Ms. Lopez. Are there any spare door hinges that I can use?"
    
    MC "Amber's door needs a new one."
    
    MsLopez irritated "If there's any, I would fix the door myself."
    
    MC thinking "Yeah, I figured…"
    
    MC "Welp, I guess I should take Uncle's offer…"
    
    "MC leaves the lobby."
    
    scene black with fade
    
    # Player should return to pawn shop
    return

# ==========================================================
# SCENE A02_5 - Fixing Amber's Door
# ==========================================================
label A02_5_FIX_DOOR:
    
    # Fade in
    scene bg apartment_amber_apartment with fade
    
    "MC gets back to Amber's place. He immediately replaces the door hinges, fixing the door in a few minutes."
    
    MC proud "That should do it…"
    
    MC "Ms. Amber! You can try it now—it should swing smoothly as new."
    
    # Show Amber in work uniform
    # show Amber work_uniform
    
    "Amber comes out in her work uniform, then tries to move the door."
    
    Amber seductive "Impressive… Thank you so much."
    
    Amber "Unfortunately for you, I'm not in my underwear anymore. There would be no staring service, but maybe I can thank you in other ways~"
    
    MC blushing "Ahh, there's no need…"
    
    MC "Umm, to thank…"
    
    Amber laughing "Hahahaha…"
    
    Amber "I'm just messing with you."
    
    Amber "Your mom would be proud. Thank you again for your help."
    
    MC happy "Glad that I can help."
    
    # Baby voice offscreen
    "Baby" "Mommy!"
    
    Amber concerned "Coming, Baby!"
    
    Amber idle "Sorry, I gotta go. See you around then."
    
    MC polite "Sure, sure… Ah… let me know if you need any more help. I would be around the building."
    
    Amber seductive "Sure thing, perv~"
    
    # Set quest flags
    $ quest_fix_amber_door = False
    $ quest_amber_door_complete = True
    $ quest_report_ms_lopez = True
    
    # Fade out
    scene black with fade
    
    return

# ==========================================================
# END OF A02 SCENES
# ==========================================================

