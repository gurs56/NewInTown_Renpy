# ==========================================================
# SCENE: A01 - Meeting Ms. Lopez
# LOCATION: Apartment Lobby
# ==========================================================

label A01_meeting_lopez:

    # --- SCENE START ---
    
    # Start with black to clear previous scenes
    scene black with fade

    scene bg apartment_lobby
    
    with dissolve
    # scene bg apartment_lobby_morning with dissolve

    # [ART PLACEHOLDER] Show characters. 
    # Since you are using "neutral" for testing, we just show them once here.
    show MsLopez neutral at right
    show Uncle neutral at left
    # MC will enter later from the right; keep it hidden at scene start
    hide MC

    # --- ARGUMENT SEQUENCE ---

    # Script says: Ms. Lopez (Pose: Angry)
    # When you have the art, uncomment the next line:
    # show MsLopez angry
    MsLopez "How many times did I tell you to pay rent on time?"

    # Script says: Uncle (Pose: Sad)
    # show Uncle sad
    Uncle "It's been hard these past few months, you know that."

    # Script says: Ms. Lopez (Pose: Angry)
    MsLopez "I don't care what you have to say! I'm running a business here, not a charity, Lenny. I already let you set up that junk shop outside for free. What more do you need?"

    # Script says: Uncle (Pose: Explaining)
    # show Uncle explaining
    Uncle "Hey, it's a Pawn Shop, and we're not selling junk. You must know that one man's trash is another man's treasure."

    # MC Enters
    # [ART PLACEHOLDER] Show MC (entering from the right)
    show MC neutral at center with moveinright

    # Script says: MC (Pose: Idle)
    MC "My mom used to say, 'Why throw something away when you can keep it?'"

    # Script says: Uncle (Pose: Wise)
    # show Uncle wise
    Uncle "See, buddy gets it."

    # Internal thought (in parentheses in your script usually means thought)
    # Script says: Uncle (Pose: Confused)
    # show Uncle confused
    Uncle "(Umm, who is Buddy anyway?)"

    # ==========================================================
    # MENU 1: INTRODUCTIONS
    # ==========================================================
    
    menu:
        "How will you respond?"

        "Introduce yourself politely":
            # --- OPTION 1 ---
            # Script says: MC (Pose: Polite)
            # show MC polite
            MC "Hi, I'm [mcname]. Nice to meet you."

            # Script says: Uncle (Pose: Wise)
            # show Uncle wise
            Uncle "Oh, you must be new in town. I'm Lenny, but everyone just calls me Uncle."

        "Apologies for intruding":
            # --- OPTION 2 ---
            # Script says: MC (Pose: Apologetic)
            # show MC apologetic
            MC "Sorry for meddling. I'm [mcname]."

            # Script says: Uncle (Calm)
            # show Uncle calm
            Uncle "Oh, a shy kid. I'm Lenny, but everyone just calls me Uncle. Nice to meet you."

    # ==========================================================
    # MERGE (Main Story Continues)
    # ==========================================================

    # Script says: Uncle (Pose: Curious)
    # show Uncle curious
    Uncle "You wouldn't happen to be looking for a slightly used microwave?"

    # Script says: MC (Pose: Laughing)
    # show MC laughing
    MC "Hahaha, sadly no. I am actually looking for a place to stay."

    # Script says: Uncle (Pose: Happy)
    # show Uncle happy
    Uncle "WELL, YOU'VE COME TO THE RIGHT PLACE!"
    Uncle "You can stay with me for the low, low price of $200 a month."

    # Script says: Ms. Lopez (Pose: Angry)
    # show MsLopez angry
    MsLopez "LENNY!"
    MsLopez "This is your last warning! Stop trying to use your back alley scams on handsome, young, naive boys."

    # Script says: Uncle (Pose: Guilty-looking)
    # show Uncle guilty
    Uncle "Oh, I would never. How can you say that?"

    # Script says: Ms. Lopez (Pose: Idle)
    # show MsLopez neutral
    MsLopez "Don't listen to that old man. I'm the landlady of this place. You can stay here if you pay rent."

    # ==========================================================
    # MENU 2: MONEY SITUATION
    # ==========================================================

    menu:
        "Tell her you don't have money":
            # --- OPTION 1 ---
            # Script says: MC (Pose: Scratching head/shy)
            # show MC shy
            MC "Well… the thing is, I don't have any money."

            # Script says: Ms. Lopez (Pose: Strict, Talking to self)
            # show MsLopez strict
            MsLopez "(Welp, you'd better get some if you want to stay here.)"
            MsLopez "(No rent, No Stay.)"

        "Tell her you came from Willow Creek":
            # --- OPTION 2 ---
            # Script says: Mc (Pose: Scratching head/shy)
            # show MC shy
            MC "Well… I just used my last savings to get here, all the way from Willow Creek."

            # Script says: Ms. Lopez (Pose: Curious -> Strict)
            # show MsLopez curious
            MsLopez "(Willow Creek? Right! I used to have a friend in Willow.)"
            
            # show MsLopez strict
            MsLopez "Doesn't matter, No rent, No Stay."

    # ==========================================================
    # MERGE: THE REVEAL
    # ==========================================================

    # Script says: MC (Pose: innocent)
    # show MC innocent
    MC "I understand. Maybe you could help me with something else then? My mom sent me here, and I was hoping you would know someone named Ms. Lopez?"

    # Script says: Ms. Lopez (Pose: Shocked)
    # show MsLopez shocked
    MsLopez "Wait… Who was your mother?"

    # Script says: MC (Pose: innocent)
    MC "Jessia."

    # Script says: Ms. Lopez (Pose: Shocked)
    MsLopez "Wait, that would mean you're.."

    # --- SPECIAL EVENT: THE HUG ---
    # [ART PLACEHOLDER] This is a "CG" scene. Usually we hide the sprites here.
    # hide MC
    # hide Uncle
    # hide MsLopez
    # scene cg_lopez_hug with dissolve

    MsLopez "Oh, you poor baby…"
    MsLopez "I'm so sorry. I wanted to come, but it had been so long. I didn't know what I would say."

    # Script says: Uncle (Pose: Confused)
    # Note: Since the CG is on screen, Uncle might just be a voice.
    Uncle "I feel like I'm missing some information here."

    MC "My mother passed not too long ago."

    # --- END SPECIAL EVENT ---
    # [ART PLACEHOLDER] Restore the lobby background and sprites
    # scene bg apartment_lobby_morning
    # show MC neutral at center
    # show MsLopez neutral at right
    # show Uncle neutral at left

    # Script says: Uncle (Pose: Shocked/Sad)
    # show Uncle sad
    Uncle "Shit, kid, I'm sorry to hear that. Even though I never had a mom, I know losing one can be the hardest thing sometimes… If you need something, I'll be here in my pawnshop."

    # Narrator line
    "Ms. Lopez lets [mcname] go."

    # Script says: Ms. Lopez (Pose: Sad)
    # show MsLopez sad
    MsLopez "Your mother was a good friend of mine when I first came to this country. As much as I wanted to return the favor… I still cannot just give out free rent."
    MsLopez "I'm barely making ends meet as is."

    # ==========================================================
    # MENU 3: NEGOTIATION
    # ==========================================================

    menu:
        "Offer help in exchange":
            # --- OPTION 1 ---
            # Script says: MC (Pose: Bargaining)
            # show MC bargaining
            MC "My mom taught me that nothing comes for free in life. Perhaps I can help you with something in exchange."

            # Script says: Ms. Lopez (Pose: Sad)
            # show MsLopez sad
            MsLopez "Oh, baby. I want to help you, but how can you help here?"

            # Script says: Uncle (Pose: Wise)
            # show Uncle wise
            Uncle "Maybe he can fix things around here, like Amber's broken door? He could be a handyman or an errand boy, you know."

        "Don't push further":
            # --- OPTION 2 ---
            # Script says: MC (Pose: Sad)
            # show MC sad
            MC "I understand… I guess I really had to figure things out on my own now…"

            # Script says: Uncle (Pose: Wise)
            # show Uncle wise
            Uncle "Oh, c'mon now. Have some mercy on this poor little boy. He can be a handyman or an errand boy, you know? Help fix Amber's broken door or something."

    # ==========================================================
    # MERGE: AGREEMENT
    # ==========================================================

    # Script says: Ms. Lopez (Pose: Irritated)
    # show MsLopez irritated
    MsLopez "You know, I can't hire someone to fix those until you pay your rent."

    # Script says: MC (Pose: Bargaining)
    # show MC bargaining
    MC "I can fix those things for free. Well, not actually free, but in exchange for a place to stay."

    # Script says: Ms. Lopez (Pose: Worried)
    # show MsLopez worried
    MsLopez "Baby, repairing stuff is no small task. You could further ruin something that needs to be fixed. I learned that from experience."

    # Script says: MC (Pose: Determined -> Proud -> Sad)
    # show MC determined
    MC "Back then, mom could never afford to hire a repairman whenever something broke at our place."
    MC "That's why we did things on our own, and I think I've gotten good at fixing broken things."
    
    # show MC proud
    # (No dialogue change here, just pose change in theory)
    
    # show MC sad
    MC "I know I'm asking for a lot, but all I want is a chance."

    # Script says: Uncle (Pose: Mocking)
    # show Uncle mocking
    Uncle "Come on, the kid just wants to help. What's the worst he can do, break it more? HAHAHA"

    # Script says: Ms. Lopez (Pose: Sad -> Convinced)
    # show MsLopez sad
    MsLopez "You know what… your mom was the first person to help me when I first came here. I could never forgive myself if I didn't do the same. Maybe that's the reason why she sent you to me."

    # show MsLopez convinced
    MsLopez "Ok, if you can help me with some things around here, you can have a room."

    # Script says: MC & Uncle "YEY!!" (Simultaneously)
    # show MC celebrating
    # show Uncle celebrating
    MC "YEY!!"
    Uncle "YEY!!"

    # Script says: Ms. Lopez (Pose: Stern)
    # show MsLopez stern
    MsLopez "Don't celebrate just yet."
    MsLopez "Just know that you still have to find a job and pay rent soon, just like everyone else. Don't think you're special just because you're cute."

    # Script says: MC (Pose: Blush)
    # show MC blush
    MC "Ah… Thank you! I won't let you down. I promise."

    # --- LOG UPDATE ---
    # This updates the variables for your quest log system.
    $ quest_fix_door = True
    $ quest_get_job = True

    "New Task Added: Fix Amber's Door"
    "New Task Added: Get a Job"

    # --- SCENE END ---
    scene black with fade
    
    return