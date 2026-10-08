# ==========================================================
# ACT 1 - SCENE A04: Fix Hot Water
# ==========================================================
# Location: Apartment Lobby, Basement, Razor's Apartment
# Cast: MC, Ms. Lopez, Razor
# Objective: Fix the hot water leak in the basement
# ==========================================================

# ==========================================================
# SCENE A04_01 - Hot Water Problem
# ==========================================================
label A04_01_HOT_WATER_PROBLEM:
    # Protect the cutscene - hides the HUD and character buttons
    $ in_story_scene = True
    
    # Fade in
    scene bg apartment_lobby with fade
    
    # Show Ms. Lopez at counter
    # show MsLopez curious
    
    "MC meets Ms. Lopez at the main lobby to discuss their arrangement. Since it will take a while before MC gets his paycheck, MC needs to do more chores for Ms. Lopez."
    
    MsLopez thinking "You're finally back. How's your job hunt?"
    
    MC confident "I got hired at a local cafe!"
    
    MsLopez smirk "Good job. I'm so proud of you. I'm going to be stopping by for some coffee then."
    
    MC bargaining "It might take me a while before I can receive my first paycheck."
    
    MsLopez joyful "That's ok, It's one step at a time."
    
    MsLopez sad "But it's hard."
    
    MsLopez worried "First, it was the old man, then it was you who could not pay the rent. And now, the other tenants are threatening not to pay as well!"
    
    MC thinking "Why? What happened?"
    
    MsLopez explaining "Several tenants on the upper floors have been without hot water for some time now."
    
    MsLopez "They're threatening to withhold rent."
    
    MsLopez worried "And since no one has paid their rent yet, I can not afford to pay for a plumber."
    
    MC confident "I can go take a look."
    
    MsLopez strict "You are sweet, and I am glad you're here helping."
    
    MsLopez "But, plumbing? That's not easy."
    
    MC bargaining "I handled the last task perfectly; I'm sure I can do it again. I promise."
    
    MsLopez explaining "Honey, this isn't just tightening a bolt — those old pipes are leaking, and the boiler's pressure is too high."
    
    MsLopez "What would happen if something went wrong?"
    
    MC thinking "I'm sure there is no skill that I cannot learn. Perhaps there's someone I can ask for help."
    
    MsLopez thinking "Hmmmm… Maybe you can ask Razor."
    
    MsLopez strict "He's a retired handyman, but I will warn you. He's not very helpful to people he doesn't know."
    
    MC confident "Well, I haven't met someone who doesn't like me. I'm Sure I can convince him."
    
    MsLopez thinking "I wouldn't hold my breath."
    
    MsLopez "You should probably look at the Leak first, before you go to Razor."
    
    # Set quest flag
    $ quest_fix_hot_water = True
    $ quest_check_leak = True
    
    # Fade out
    scene black with fade
    
    # Back to free roam
    $ in_story_scene = False
    show screen apartment_lobby_screen
    jump exploration_loop

# ==========================================================
# SCENE A04_02 - Investigating the Leak
# ==========================================================
label A04_02_CHECK_LEAK:
    # Protect the cutscene - hides the HUD and character buttons
    $ in_story_scene = True
    
    # Fade in
    scene bg apartment_basement with fade
    
    "MC is going to look at the leak in the basement. There is a bucket under the leak to catch the water."
    
    MC disgusted "The leak is horrible… And the smell is unbearable as well… Maybe I should empty the water bucket first."
    
    "The player goes to grab the water bucket to empty it into the sink nearby."
    
    "After emptying the bucket, the player notices something under the sink peeking out."
    
    MC thinking "Hmmm…"
    
    MC thinking "I wonder what that is…"
    
    # Unique pose: MC finds magazines
    
    MC "Woah… I guess full bush was still in back then."
    
    MC idle "I wonder whose these belong to? Maybe Ms Lopez knows?"
    
    MC "I'll just bring these magazines out. I'm done checking the leak here anyway."
    
    # Set quest flags
    $ found_magazines = True
    $ quest_check_leak = False
    $ quest_ask_lopez_magazines = True
    
    # Fade out
    scene black with fade
    
    # Back to free roam
    $ in_story_scene = False
    show screen apartment_basement_screen
    jump exploration_loop

# ==========================================================
# SCENE A04_03 - Showing Ms. Lopez the Magazines
# ==========================================================
label A04_03_MAGAZINES_LOPEZ:
    # Protect the cutscene - hides the HUD and character buttons
    $ in_story_scene = True
    
    # Fade in
    scene bg apartment_lobby with fade
    
    # Show Ms. Lopez
    # show MsLopez idle
    
    "MC brings the Magazines to Ms. Lopez."
    
    MC worried "Ahmm… Ms. Lopez, I think I found something downstairs."
    
    MsLopez thinking "What did you find?"
    
    MC worried "Well…"
    
    MC "Ummm..."
    
    # Unique pose: MC shows magazines, Ms. Lopez blushes
    
    MsLopez "Oh my God."
    
    MsLopez "Umm… Wow."
    
    MsLopez "I just don't understand how they can wear such small underwear."
    
    # Unique pose: Ms. Lopez looks at her butt, MC stares
    
    MsLopez "I'm too old now, but when I was younger, I could never fit my big butt into something like that."
    
    MC blush "Oh…"
    
    MC "I—I think you're not old. I'm sure you would look great in those."
    
    MsLopez smirk "Oh, that's sweet of you, but you will not be seeing me in anything like that~"
    
    MC scared "Oh.. No-no…"
    
    MC "Oh, I wasn't trying to say I wanted to…"
    
    MC "Umm, I mean… I was just…"
    
    MsLopez joyful "Hahaha."
    
    MsLopez smirk "You know who could pull off something like this?"
    
    MC thinking "Umm… Who?"
    
    MsLopez excited "Your mom!"
    
    MsLopez "She could definitely pull this off when she was younger. Could you imagine?"
    
    MC disgusted "EEEWWWWWW"
    
    MC "No, thank you."
    
    MsLopez joyful "Hahahahaha. I guess you did not know her like I did."
    
    # Ms. Lopez, Pose 11: Sad - to MC
    show MsLopez sad
    
    # MC, Pose 7: Sad - to Ms. Lopez
    MC sad "Hey, I miss her too."
    
    # Ms. Lopez, Pose 11: Sad - to MC
    MsLopez sad "You know… these look like something Razor would have. He was the handyman for years, he would be the only one with access to the boiler room."
    
    MC confident "Well, let's see if he can help?"
    
    MC "I'll go talk to him."
    
    # Set quest flags
    $ quest_ask_lopez_magazines = False
    $ quest_ask_razor_help = True
    
    # Fade out
    scene black with fade
    
    # Back to free roam
    $ in_story_scene = False
    show screen apartment_lobby_screen
    jump exploration_loop

# ==========================================================
# SCENE A04_04 - Convincing Razor
# ==========================================================
label A04_04_RAZOR_BLACKMAIL:
    # Protect the cutscene - hides the HUD and character buttons
    $ in_story_scene = True
    
    # Fade in - exterior of Razor's door
    scene bg apartment_razor_apartment with fade
    
    "MC knocks on Razor's Door."
    
    MC "Razor? Are you there?"
    
    # Show Razor at door
    show Razor idle at stage_center
    
    "Razor comes to open the door."
    
    Razor idle "Yeah, what do you want, kid?"
    
    MC idle "Ms. Lopez said there's a leaky pipe downstairs. She was hoping you could help fix it."
    
    Razor irritated "Not my problem, kid. I'm retired for a reason. Tell her to call a plumber."
    
    MC bargaining "I see… Maybe you could teach me how to do it instead?"
    
    # (pose change only - an empty say line would show a blank textbox)
    # show MC enthusiastic

    Razor irritated "What makes you think that I'll teach you, ey?"
    
    MC smug "Well… I figured you would. Coz I found something that maybe belongs to you."
    
    Razor suspicious "…"
    
    Razor "What are you talking about, you little rat?"
    
    MC bargaining "Let's just say, a certain box of… vintage gentlemen's reading material ended up in my hands."
    
    MC "Great stuff, BTW."
    
    Razor shocked "…You found my old Playboy stash!?"
    
    MC smug "So it was yours…"
    
    MC "It would be a shame if the whole building knows about Razor's, uh… \"collector's edition\" magazines."
    
    Razor irritated "…You little brat…"
    
    Razor "*Sighs*"
    
    Razor "Fine. I'll fix the damn pipe. Just… keep your mouth shut."
    
    Razor irritated "Fine. I'll fix the damn pipe. Just… keep your mouth shut."
    
    Razor "Meet me in the boiler room."
    
    MC happy "Deal."
    
    # Set quest flags
    $ quest_ask_razor_help = False
    $ quest_fix_with_razor = True
    
    # Fade out
    scene black with fade
    
    # Back to free roam
    $ in_story_scene = False
    show screen apartment_razor_apartment_screen
    jump exploration_loop

# ==========================================================
# SCENE A04_05 - Fixing the Leak with Razor
# ==========================================================
label A04_05_FIX_LEAK:
    # Protect the cutscene - hides the HUD and character buttons
    $ in_story_scene = True
    
    # Fade in
    scene bg apartment_basement with fade
    
    # Show Razor
    show Razor thinking at stage_center
    
    "MC must take this opportunity to gain some clues while holding some small talk with Razor as they fix the leaking pipe."
    
    # Unique pose: Razor examining pipes, MC watching
    
    Razor "Hmmm… It seems like a little adjustment to the tubes and some plaster can do the trick…"
    
    MC excited "Great! How can I help?"
    
    Razor irritated "Just hold on to the flashlight and let me do my job."
    
    # Unique pose: MC holds flashlight, Razor works
    
    "After a few seconds of dead silence, MC finally talks to Razor while they work."
    
    MC thinking "Soooo…"
    
    MC "How long have you been here?"
    
    Razor thinking "Too long…"
    
    MC thinking "How long is that?"
    
    Razor thinking "Long enough to see everything around here."
    
    Razor "There's a reason why I'm retired now, Kiddo."
    
    MC thinking "(Everything around here?)"
    
    MC "(If that's the case, Razor probably knows something about my father…)"
    
    MC "(But I'd better play this one carefully…)"
    
    # Player choice menu
    menu:
        "Pry for more answers":
            jump .pry
        
        "Play it safe":
            jump .safe

# Option 1: Pry for answers
label .pry:
    
    MC thinking "What do you mean by that?"
    
    Razor irritated "Look, kid. You are new to this town."
    
    Razor "Just don't stick your nose where it doesn't belong if you don't want to get in trouble."
    
    jump .merge

# Option 2: Play it safe
label .safe:
    
    MC thinking "I see… Got any advice for the newcomer in town?"
    
    Razor irritated "Just don't stick your nose where it doesn't belong, and you'll be fine."
    
    Razor "After all, curiosity kills the cat."
    
    jump .merge

# Both options continue here
label .merge:
    
    MC thinking "(I knew it… Something is going around here.)"
    
    MC "(I should earn Razor's trust if I want more info around the town…)"
    
    # Unique pose: Razor wipes forehead, MC turns off flashlight
    
    Razor thinking "Alright, that should do it."
    
    Razor "I keep our deal, so you better shut your mouth."
    
    MC idle "Certainly! Thank you for your help!"
    
    # hide Razor
    
    "Razor leaves the place."
    
    MC confident "Another task completed…"
    
    MC "Better report this to Ms. Lopez immediately."
    
    "MC leaves the place."
    
    # Set quest flags
    $ quest_fix_with_razor = False
    $ quest_hot_water_fixed = True
    $ quest_report_lopez_water = True
    $ razor_relationship += 1
    
    # Fade out
    scene black with fade
    
    # Unlock the next event (A05: getting the apartment)
    call setup_a05_event
    # Back to free roam
    $ in_story_scene = False
    show screen apartment_basement_screen
    jump exploration_loop

# ==========================================================
# END OF A04 SCENES
# ==========================================================

