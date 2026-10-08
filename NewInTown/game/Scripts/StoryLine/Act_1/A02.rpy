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
    # Protect the cutscene - hides the HUD and character buttons
    $ in_story_scene = True
    
    # Fade in
    scene bg apartment_lobby with fade
    
    # Ms. Lopez, Pose 10: Worried (Stressed) - to MC
    show MsLopez worried at stage_center
    
    "MC meets Ms. Lopez at the front counter of the lobby and asks for the details of his first task."
    
    MsLopez worried "Here's the deal."
    
    MsLopez "Amber's door has been broken for 2 weeks. The regular repair is charging me $400 to fix some simple hinges."
    
    MsLopez "It's a stiff price for a door hinge repair, you know."
    
    MsLopez "Do you think you could go up to Amber's room and have a look?"
    
    # Player choice menu
    menu:
        "Promise to handle the situation":
            jump .promise
        
        "Ask who Amber is":
            jump .ask_amber

# Option 1: Promise to handle it
label .promise:
    
    MC confident "That’s a regular situation back at my old place. I'll fix it in no time."
    
    MsLopez idle "Great. Just head to Amber's place, and you'll see the door that never closes."
    
    jump .merge

# Option 2: Ask who Amber is
label .ask_amber:
    
    MC thinking "Sure! But… Umm, who is Amber?"
    
    MsLopez idle "Amber is one of the tenants here. She's really a hard-working mother, just like Jessica."
    
    jump .merge

# Both options continue here
label .merge:
    
    MsLopez worried "I feel so bad for not being able to fix her door for quite some time now."
    
    MsLopez "To compromise, I told her to hold off on rent for the month, but she wouldn't take no for an answer."
    
    MC confident "That's unfortunate. Don't worry, I'll handle this one. How hard could it be?"
    
    MsLopez strict "I love the spirit, but if this is proving to be too difficult, the responsible thing would be to own up to it."
    
    MC thinking "I'll keep that in mind… Umm, where is Amber's room, again?"
    
    MsLopez worried "Third floor, to the left."
    
    # MC, Pose 18: Scratch - back of the head
    MC scratch "Hahaha. Got it."
    
    # Set quest flag
    $ quest_fix_amber_door_started = True
    $ amber_in_apartment = True
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
    # Protect the cutscene - hides the HUD and character buttons
    $ in_story_scene = True
    
    # Fade in
    scene bg apartment_amber_apartment with fade
    
    # Amber is in her underwear here - no outfit art yet.
    show Amber arms_crossed at stage_right
    
    MC thinking "Hello? I'm here about the door."
    
    # UP_EyesWild / UP_BenDover: MC's eyes widen and jaw drops while
    # blushing; Amber is bent over. Not shown - the stand-ins are
    # full-screen cards and would wipe the room mid-scene.
    
    Amber arms_crossed "Great… As if my life wasn't messy enough, now I have to deal with perverts."
    
    MC scared "A—ahhh… I—it's not what it looks like. Ms. López sent me. I swear, I'm here to fix hinges!"
    
    Amber arms_crossed "Really? She sent a little perv to fix my door."
    
    Amber "What do you even know about fixing doors?"
    
    MC idle "My mom taught me to fix what breaks — if it breaks again, then fix and fix it again."
    
    MC "It's kinda what we do, relying only on ourselves… I just hope I'm up to it."
    
    # Amber softens
    
    Amber irritated "Fine…"
    
    Amber "I guess beggars can't be choosers, but if you mess it up worse, you'll owe more than rent."
    
    MC happy "I—I promise I will not let you down!"
    
    # MC stares and blushes, Amber notices
    
    Amber arms_crossed "Chop-chop. Hinges first, staring later. Time to man up with your words."
    
    MC thinking "Right, hinges. I'll head to a convenience store."
    
    # Set quest flag
    $ quest_get_hinges = True
    
    # Fade out
    scene black with fade
    
    $ in_story_scene = False
    show screen apartment_amber_apartment_screen
    jump exploration_loop

# ==========================================================
# SCENE A02_3 - Mr. Lee's Convenience Store
# ==========================================================
label A02_3_MR_LEE_STORE:
    # Protect the cutscene - hides the HUD and character buttons
    $ in_story_scene = True
    
    # Fade in
    scene bg grocery_store_interior with fade
    
    # Mr. Lee, Pose 1: Idle (Strict) - to MC
    show MrLee idle at stage_center
    
    MC thinking "Good afternoon, how much for this door hinge?"
    
    MrLee idle "15 dollars."
    
    # MC, Pose 18: Scratch - back of the head
    MC scratch "Well, about that… I actually don't have money?"
    
    MrLee mad "Out of my store. No free here."
    
    MC bargaining "Yes, I understand, but maybe we can…"
    
    MrLee mad "NO FREE. OUT."
    
    MC scared "OK. OK. I'm sorry."
    
    MC thinking "Maybe some other place has hinges… I should check around."
    
    # Set quest flag
    $ quest_check_uncle_shop = True
    
    # Fade out
    scene black with fade
    
    $ in_story_scene = False
    show screen grocery_store_interior_screen
    jump exploration_loop

# ==========================================================
# SCENE A02_4 - Uncle's Pawn Shop
# ==========================================================
label A02_4_UNCLE_PAWN_SHOP:
    # Protect the cutscene - hides the HUD and character buttons
    $ in_story_scene = True
    
    # Fade in
    scene bg apartment_alley with fade
    
    # Uncle, Pose 6: Happy - to MC
    show Uncle happy at stage_right
    
    MC happy "Hey, Uncle."
    
    Uncle happy "Oh, [mc_name]. Looks like the madam is already putting you to work. What can I do for you, Sonny?"
    
    MC explaining "Hahaha, she does."
    
    MC "I actually have been running around, looking for some door hinges. But sadly, I can't afford one."
    
    # UP_LookDown: Uncle looks down at his tools
    Uncle idle "Well, I have a pair here."
    
    MC excited "That's exactly what I need! You are a lifesaver."
    
    # UP_GrabHingeMC: MC goes to grab the hinges, Uncle stops his hands
    
    Uncle idle "Slow down, kid. This is a Pawn shop, not a get-free shop."
    
    MC bargaining "But Uncle, I don't have anything to give…"
    
    MC "The only thing I have is this picture of my dad and my mom's wedding band."
    
    Uncle wise "Well… you could pawn the ring?"
    
    MC bargaining "…"
    
    MC bargaining "How could I? This is the only thing I have left of my mom…"
    
    # MC, Pose 7: Sad
    show MC sad
    
    Uncle explaining "Don't worry, kid. It's not like it's going away. I will hold on to it for you until you can get it back."
    
    MC worried "But what if someone buys it before I can get it back?"
    
    Uncle wise "Well, I'm sorry. That's just life, kid. You either take the risk or play it safe."
    
    # Player choice menu
    menu:
        "Pawn the ring":
            jump .pawn_ring
        
        "Do not pawn the ring":
            jump .no_pawn

# Option 1: Pawn the ring
label .pawn_ring:
    
    MC bargaining "Ok…"
    
    MC bargaining "Can you please hold on to it until I can buy it back?"
    
    # MC, Pose 7: Sad
    show MC sad
    
    Uncle explaining "Well, I can try, but you'd better be quick. I can't hold this forever; it's a business after all."
    
    MC sad "Sigh…"
    
    MC "I guess I don't have a choice…"
    
    # Set flags
    $ pawned_ring = True
    $ has_hinges = True
    $ quest_get_ring_back = True
    
    # UP_HandsRing: MC hands the ring over to Uncle
    "MC gives the ring to Uncle."
    
    # Fade out
    scene black with fade
    
    $ in_story_scene = False
    show screen apartment_alley_screen
    jump exploration_loop

# Option 2: Don't pawn the ring (forces player to reconsider)
label .no_pawn:
    
    MC thinking "(...)"
    
    MC thinking "(What should I do?)"
    
    MC thinking "(I cannot just let go of my mother's ring.)"
    
    MC sad "I'll think about it first…"
    
    "MC leaves Uncle's Pawnshop."
    
    # Set flag for limited access
    $ refused_pawn = True
    
    # Fade out
    scene black with fade
    
    $ in_story_scene = False
    show screen apartment_alley_screen
    jump exploration_loop

# ==========================================================
# CALLBACK SCENES - Player must return to pawn shop
# ==========================================================

# Attempt to visit Mr. Lee again
label A02_CALLBACK_MR_LEE:
    
    scene bg grocery_store with fade
    
    MC "Going back in there without money is probably not a good idea…"
    
    "MC leaves the area."
    
    scene black with fade
    
    return

# Attempt to ask Ms. Lopez for help
label A02_CALLBACK_MS_LOPEZ:
    
    scene bg apartment_lobby with fade
    
    # show MsLopez idle
    
    MC idle "Hi, Ms. Lopez. Are there any spare door hinges that I can use?"
    
    MC "Amber's door needs a new one."
    
    MsLopez irritated "If there's any, I would fix the door myself."
    
    MC thinking "Yeah, I figured…"
    
    MC "Welp, I guess I should take Uncle's offer…"
    
    "MC leaves the lobby."
    
    scene black with fade
    
    # Player should return to pawn shop
    return

# Attempt to ask Uncle again (screenplay: IF THE PLAYER ASKS UNCLE AGAIN)
label A02_CALLBACK_UNCLE:
    
    scene bg apartment_alley with fade
    
    # Uncle, Pose 2: Explaining - to MC
    show Uncle explaining at stage_right
    
    Uncle "Did you find a way to trade for the hinges?"
    
    scene black with fade
    
    # END OF CALLBACK - loops back and connects to Option 1.
    return

# ==========================================================
# SCENE A02_5 - Fixing Amber's Door
# ==========================================================
label A02_5_FIX_DOOR:
    # Protect the cutscene - hides the HUD and character buttons
    $ in_story_scene = True
    
    # Fade in
    scene bg apartment_amber_apartment with fade
    
    # Poster: A02 - Ambers_Door_Fix
    "MC gets back to Amber's place. He immediately replaces the door hinges, fixing the door in a few minutes."
    
    MC confident "That should do it…"
    
    MC "Ms. Amber! You can try it now — it should swing smoothly as new."
    
    # Amber changes into her work uniform - no outfit art yet.
    
    "Amber comes out in her work uniform, then tries to move the door."
    
    Amber seductive "Impressive… Thank you so much."
    
    Amber "Unfortunately for you, I'm not in my underwear anymore. There would be no free service."
    
    MC blush "Umm, I didn’t see anything."
    
    Amber laughing "Hahahaha…"
    
    Amber "I'm just messing with you."
    
    Amber "Thank you again for your help."
    
    MC happy "Glad that I can help."
    
    # Baby voice offscreen
    "Baby" "Mommy!"
    
    Amber concerned "Coming, Baby!"
    
    Amber arms_crossed "Sorry, I gotta go. See you around town, [mc_name]."
    
    MC idle "Sure, sure… Ah… let me know if you need any more help. I would be around the building."
    
    Amber seductive "Sure thing, perv~"
    
    # Quest complete - unlock the next event (A03: finding a job)
    $ quest_fix_amber_door_complete = True
    call setup_a03_event
    
    # Fade out
    scene black with fade
    
    $ in_story_scene = False
    show screen apartment_amber_apartment_screen
    jump exploration_loop

# ==========================================================
# END OF A02 SCENES
# ==========================================================

