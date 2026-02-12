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
    
    # Fade in
    scene bg apartment_lobby with fade
    
    # Show Ms. Lopez at counter
    # show MsLopez curious
    
    "MC meets Ms. Lopez at the main lobby to discuss their arrangement. Since it will take a while before MC gets his paycheck, MC needs to do more chores for Ms. Lopez."
    
    MsLopez curious "You're finally back. How's your job hunt?"
    
    MC proud "I got hired at a local cafe!"
    
    MsLopez impressed "That was quick! Which means you can finally pay the rent."
    
    MC bargaining "But I just got hired, so it will take a while before I can receive my first paycheck."
    
    MsLopez sad "I figured…"
    
    MsLopez stressed "First, it was the old man, then it was you who could not pay the rent. And now, the other tenants are threatening not to pay as well!"
    
    MC curious "Why? What happened?"
    
    MsLopez explaining "Several tenants on the upper floors have been without hot water for some time now."
    
    MsLopez "They're threatening to withhold rent."
    
    MsLopez stressed "And since no one has paid their rent yet, I can not afford to pay for a plumber."
    
    MC confident "I can go take a look."
    
    MsLopez stern "You are sweet, and I am glad you're here helping."
    
    MsLopez "But, plumbing? It's a no-no."
    
    MC bargaining "I handled the last task perfectly; I'm sure I can do it again. I promise."
    
    MsLopez explaining "Honey, this isn't just tightening a bolt—those old pipes are leaking and the boiler's pressure is too high."
    
    MsLopez "One wrong move and you could wreck it all."
    
    MC thinking "I'm sure there is no skill that I cannot learn. Perhaps there's someone I can ask for help."
    
    MsLopez thinking "Hmmmm… Maybe you can ask Razor."
    
    MsLopez stern "He's a retired handyman, but I will warn you. He's not very helpful to people he doesn't know."
    
    MC confident "Well, I haven't met someone who doesn't like me. I'm Sure I can convince him."
    
    MsLopez doubtful "I wouldn't hold my breath."
    
    MsLopez "You should probably go look at the Leak first, before you go to Razor."
    
    # Set quest flag
    $ quest_fix_hot_water = True
    $ quest_check_leak = True
    
    # Fade out
    scene black with fade
    
    return

# ==========================================================
# SCENE A04_02 - Investigating the Leak
# ==========================================================
label A04_02_CHECK_LEAK:
    
    # Fade in
    scene bg apartment_basement with fade
    
    "MC is going to look at the leak in the basement. There is a bucket under the leak to catch the water."
    
    MC disgusted "The leak is horrible… And the smell is unbearable as well… Maybe I should empty the water bucket first."
    
    "The player goes to grab the water bucket to empty it into the sink nearby."
    
    "After emptying the bucket, the player notices something under the sink peeking out."
    
    MC curious "Hmmm…"
    
    MC intrigued "I wonder what that is…"
    
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
    
    return

# ==========================================================
# SCENE A04_03 - Showing Ms. Lopez the Magazines
# ==========================================================
label A04_03_MAGAZINES_LOPEZ:
    
    # Fade in
    scene bg apartment_lobby with fade
    
    # Show Ms. Lopez
    # show MsLopez idle
    
    "MC brings the Magazines to Ms. Lopez."
    
    MC hesitant "Ahmm… Ms. Lopez, I think I found something downstairs."
    
    MsLopez curious "What did you find?"
    
    MC hesitant "Well…"
    
    MC "Ummm..."
    
    # Unique pose: MC shows magazines, Ms. Lopez blushes
    
    MsLopez "Oh my God."
    
    MsLopez "Umm… Wow."
    
    MsLopez "I just don't understand how they can wear such small underwear."
    
    # Unique pose: Ms. Lopez looks at her butt, MC stares
    
    MsLopez "I'm too old now, but when I was younger, I could never fit my big butt into something like that."
    
    MC flustered "Oh…"
    
    MC "I—I think you're not old. I'm sure you would look great in those."
    
    MsLopez smirk "Oh, that's sweet of you, but you will not be seeing me in anything like that~"
    
    MC panicking "Oh.. No-no…"
    
    MC "Oh, I wasn't trying to say I wanted to…"
    
    MC "Umm, I mean… I was just…"
    
    MsLopez laughing "Hahaha."
    
    MsLopez smirk "You know who could pull off something like this?"
    
    MC curious "Umm… Who?"
    
    MsLopez excited "Your mom!"
    
    MsLopez "She could definitely pull this off when she was younger. Could you imagine?"
    
    MC disgusted "EEEWWWWWW"
    
    MC "No, thank you."
    
    MsLopez laughing "Hahahahaha. I guess you did not know her like I did."
    
    MsLopez thinking "Going back to the topic, I think those might be Razor's old magazines."
    
    MsLopez explaining "I mean, if I remember it correctly. He was the last one down there. But I'm not sure if those magazines will make him help you."
    
    MC confident "Well… Gonna trust my luck then."
    
    MC "I'll go talk to him."
    
    # Set quest flags
    $ quest_ask_lopez_magazines = False
    $ quest_ask_razor_help = True
    
    # Fade out
    scene black with fade
    
    return

# ==========================================================
# SCENE A04_04 - Convincing Razor
# ==========================================================
label A04_04_RAZOR_BLACKMAIL:
    
    # Fade in - exterior of Razor's door
    scene bg apartment_razor_apartment with fade
    
    "MC knocks on Razor's Door."
    
    MC "Razor? Are you there?"
    
    # Show Razor at door
    # show Razor grumpy
    
    "Razor comes to open the door."
    
    Razor grumpy "Yeah, what do you want, kid?"
    
    MC polite "Ms. Lopez said there's a leaky pipe downstairs. She was hoping you could help fix it."
    
    Razor stern "Not my problem, kid. I'm retired for a reason. Tell her to call a plumber."
    
    MC bargaining "I see… Maybe you could teach me how to do it instead?"
    
    MC enthusiastic ""
    
    Razor irritated "What makes you think that I'll teach you, ey?"
    
    MC mischievous "Well… I figured you would. Coz I found something that maybe belongs to you."
    
    Razor suspicious "…"
    
    Razor "What are you talking about, you little rat?"
    
    MC bargaining "Let's just say, a certain box of… vintage gentlemen's reading material ended up in my hands."
    
    MC "Great stuff, BTW."
    
    Razor shocked "…You found my old Playboy stash!?"
    
    MC mischievous "So it was truly yours…"
    
    MC "It would be a shame if the whole building knows about Razor's, uh… \"collector's edition\" magazines."
    
    Razor irritated "…You little brat…"
    
    Razor "*Sighs*"
    
    Razor "Fine. I'll fix the damn pipe. Just… keep your mouth shut."
    
    Razor stern "You'll be my assistant, so you can do it yourself next time."
    
    MC happy "Deal."
    
    # Set quest flags
    $ quest_ask_razor_help = False
    $ quest_fix_with_razor = True
    
    # Fade out
    scene black with fade
    
    return

# ==========================================================
# SCENE A04_05 - Fixing the Leak with Razor
# ==========================================================
label A04_05_FIX_LEAK:
    
    # Fade in
    scene bg apartment_basement with fade
    
    # Show Razor
    # show Razor thinking
    
    "MC must take this opportunity to gain some clues while holding some small talk with Razor as they fix the leaking pipe."
    
    # Unique pose: Razor examining pipes, MC watching
    
    Razor "Hmmm… It seems like a little adjustment to the tubes and some plaster can do the trick…"
    
    MC excited "Great! How can I help?"
    
    Razor irritated "Just hold on to the flashlight and let me do my job."
    
    # Unique pose: MC holds flashlight, Razor works
    
    "After a few seconds of dead silence, MC finally talks to Razor while they work."
    
    MC curious "Soooo…"
    
    MC "How long have you been here?"
    
    Razor serious "Too long…"
    
    MC curious "How long is that?"
    
    Razor serious "Long enough to see everything around here."
    
    Razor "There's a reason why I'm retired now, Kiddo."
    
    MC thinking "(Everything around here?)"
    
    MC "(If that's the case, Razor probably knows something about my father…)"
    
    MC "(But I'd better play this one carefully…)"
    
    # Player choice menu
    menu:
        "Pry for more answers":
            jump option1_pry
        
        "Play it safe":
            jump option2_safe

# Option 1: Pry for answers
label option1_pry:
    
    MC confused "What do you mean by that?"
    
    Razor stern "Look, kid. You are new to this town."
    
    Razor "Just don't stick your nose where it doesn't belong if you don't want to get in trouble."
    
    jump both_razor_options_continue

# Option 2: Play it safe
label option2_safe:
    
    MC curious "I see… Got any advice for the newcomer in town?"
    
    Razor stern "Just don't stick your nose where it doesn't belong, and you'll be fine."
    
    Razor "After all, curiosity kills the cat."
    
    jump both_razor_options_continue

# Both options continue here
label both_razor_options_continue:
    
    MC thinking "(I knew it… Something is going around here.)"
    
    MC "(I should earn Razor's trust if I want more info around the town…)"
    
    # Unique pose: Razor wipes forehead, MC turns off flashlight
    
    Razor serious "Alright, that should do it."
    
    Razor "I keep our deal, so you better shut your mouth."
    
    MC polite "Certainly! Thank you for your help!"
    
    # hide Razor
    
    "Razor leaves the place."
    
    MC proud "Another task completed…"
    
    MC "Better report this to Ms. Lopez immediately."
    
    "MC leaves the place."
    
    # Set quest flags
    $ quest_fix_with_razor = False
    $ quest_hot_water_fixed = True
    $ quest_report_lopez_water = True
    $ razor_relationship += 1
    
    # Fade out
    scene black with fade
    
    return

# ==========================================================
# END OF A04 SCENES
# ==========================================================

