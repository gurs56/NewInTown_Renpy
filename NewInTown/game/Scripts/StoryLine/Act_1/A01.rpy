# ==========================================================
# ACT 1 - SCENE A01: Meeting Ms. Lopez
# ==========================================================
# LOCATION: Central District - Midtown - Apartment Building - Lobby
# CAST: MC, Ms. Lopez, Uncle (Lenny Cho)
# OBJECTIVE: Talk to Ms. Lopez
# FLAG IN: Start Game
#
# Follows NewInTown_V5_01_A, poses per NAT_PoseList_v02. The pose
# number from the screenplay is kept in the comment so this file can
# be diffed against the script by eye.
#
# CHANGED IN V5: the old middle of this scene is gone. There used to
# be a "how will you explain having no money" menu and a separate
# "negotiate for the room" menu; V5 replaces the first with a
# straight run of beats and the second with the mom's-name / ring
# choice, which is now what triggers the reveal. Ms. Lopez, not MC,
# is the one who says the name Jessica.
# ==========================================================

label A01_meeting_lopez:

    # --- SCENE START ---

    # Start with black to clear previous scenes
    scene black with fade

    scene bg apartment_lobby

    with dissolve

    # Show characters. stage_left/right frame them knees-up at a
    # shared camera distance - see Characters/SpriteFraming.rpy.
    show MsLopez idle at stage_left
    show Uncle idle at stage_right
    # MC walks in on the argument; keep him off stage until he does.
    hide MC

    # --- ARGUMENT SEQUENCE ---

    # Ms. Lopez, Pose 5: Angry - to Uncle
    show MsLopez angry
    MsLopez "How many times, Lenny? How many times did I tell you to pay rent on time?"

    # Uncle, Pose 9: Sad - to Ms. Lopez
    show Uncle sad
    Uncle "It's been hard these past few months, you know that."

    # Ms. Lopez, Pose 4: Irritated - to Lenny Cho
    show MsLopez irritated
    MsLopez "I'm trying to run a building here, not a charity."
    MsLopez "I already let you set up that junk shop outside for free."

    # Uncle, Pose 2: Explaining - to Ms. Lopez
    show Uncle explaining
    Uncle "Hey, it's a Pawn Shop, and we're not selling junk."
    Uncle "You must know that one man's trash is another man's treasure."

    # MC enters the conversation
    # MC, Pose 1: Idle
    show MC idle at stage_center with moveinright
    MC "My mom used to say, 'Why throw something away when you can keep it?'"

    # Uncle, Pose 4: Wise - to Ms. Lopez
    show Uncle wise
    Uncle "See, Buddy gets it."

    # Uncle, Pose 7: Confused - to MC
    show Uncle confused
    Uncle "Umm, who is Buddy anyway?"

    # ==========================================================
    # PLAYER CHOICE: INTRODUCTIONS
    # ==========================================================

    menu:
        "How will you respond?"

        "Introduce yourself politely":
            # --- OPTION 1 ---
            # MC, Pose 2: Happy
            show MC happy
            MC "Hi, I'm [mc_name]. Nice to meet you."

            # Uncle, Pose 4: Wise - to MC
            show Uncle wise
            Uncle "Oh, you must be new in town? I'm Lenny, but everyone just calls me Uncle."

        "Apologize for intruding":
            # --- OPTION 2 ---
            # MC, Pose 7: Sad - to Uncle
            show MC sad
            MC "Sorry for interrupting. I'm [mc_name]."

            # Uncle, Pose 3: Laughing - to MC
            show Uncle laughing
            Uncle "Oh, a shy kid. I'm Lenny, but everyone just calls me Uncle. Nice to meet you."

            # Uncle, Pose 4: Wise
            show Uncle wise

    # ==========================================================
    # BOTH OPTIONS CONTINUE
    # ==========================================================

    # Uncle, Pose 7: Confused - to MC
    show Uncle confused
    Uncle "You wouldn't happen to be looking for a slightly used microwave?"

    # MC, Pose 4: Laughing - to Uncle
    show MC laughing
    MC "Hahaha, sadly no. I am actually looking for a place to stay."

    # Uncle, Pose 6: Happy - to MC
    show Uncle happy
    Uncle "WELL, YOU'VE COME TO THE RIGHT PLACE!"
    Uncle "You can stay with me for the low, low price of …"

    # Ms. Lopez, Pose 5: Angry - to Uncle
    show MsLopez angry
    MsLopez "LENNY!"
    MsLopez "This is your last warning! Stop trying to use your back alley scams on every naive boy who walks through the door."

    # Uncle, Pose 8: Guilty - to Ms. Lopez
    show Uncle guilty
    Uncle "Oh, I would never."
    Uncle "How can you say that?"

    # Ms. Lopez, Pose 1: Idle - to MC
    show MsLopez idle
    MsLopez "Don't listen to that old man. I'm the landlady here."
    MsLopez "You can stay here…"
    MsLopez "… if you pay rent."

    # --- THE MONEY PROBLEM ---

    # MC, Pose 18: Scratch - back of the head
    show MC scratch
    MC "Well… the thing is, I don't have any money."
    MC "But I can work for it. Anything that's broken, I can fix it."
    MC "I'm good with my hands."

    # Ms. Lopez, Pose 3: Strict - to herself
    show MsLopez strict
    MsLopez "Oh baby. I've heard that exact speech before."

    # Ms. Lopez, Pose 4: Irritated - looking at Uncle
    show MsLopez irritated
    MsLopez "Every month, it would seem."

    # Uncle, Pose 8: Guilty - to Ms. Lopez (avoids eye contact)
    show Uncle guilty

    # Ms. Lopez, Pose 10: Worried - to MC
    show MsLopez worried
    MsLopez "Take a look around. This place is falling apart."
    MsLopez "Half the tenants are struggling to pay rent."
    MsLopez "If you can't pay rent, then I can't give you a room."

    # MC looks defeated. He turns to walk away - then stops, one last try.
    show MC sad

    # ==========================================================
    # PLAYER CHOICE: ONE LAST TRY
    # ==========================================================

    menu:
        "One last try…"

        "Say your mom's name":
            # --- OPTION 1 ---
            # MC, Pose 7: Sad - to Ms. Lopez
            MC "Umm…"
            MC "My mom's name was Jessica. She's the reason I came here."

        "Show the ring":
            # --- OPTION 2 ---
            # MC, Pose 7: Sad - to Ms. Lopez
            MC "Umm…"
            MC "This was my mom's ring."

    # ==========================================================
    # BOTH OPTIONS CONTINUE: THE REVEAL
    # ==========================================================

    # Ms. Lopez, Pose 12: Shocked - to MC
    show MsLopez shocked
    MsLopez "…"
    MsLopez "Wait, that would mean you're…"
    MsLopez "Jessica's boy?"

    # MC, Pose 12: Blush - to Ms. Lopez (doesn't answer)
    show MC blush

    # Ms. Lopez, Pose 8: Happy - to MC
    show MsLopez happy
    MsLopez "Oh my God!!!"
    MsLopez "JESSICA IS HERE!?!?!?"
    MsLopez "MY BESTIE!!!"

    # MC, Pose 7: Sad - to Ms. Lopez (doesn't answer)
    show MC sad

    # Ms. Lopez, lopez_u_tears - to MC
    show MsLopez tears
    MsLopez "Where is she?"

    # MC, Pose 19: Tears - to Ms. Lopez (doesn't answer)
    show MC tears

    # --- Ms. Lopez hugs MC, his face in her chest ---
    scene UP_BoobFaceLopez_Sad with dissolve

    MsLopez "Oh, you poor baby…"
    MsLopez "I'm so sorry."

    # Uncle, Pose 7: Confused - to Ms. Lopez
    Uncle "… I feel like I'm missing something."

    # MC, Pose 7: Sad - to Lenny
    MC "My mother is no longer with us."

    # Uncle, Pose 10: Shocked
    Uncle "Ah, hell, kid."

    # Uncle, Pose 9: Sad
    Uncle "I never had a mother myself, so I can't say I know it. But I know losing one's about the hardest thing there is…"
    Uncle "If you need something…"
    Uncle "… I'm out front."

    # --- Ms. Lopez lets MC go: restore the lobby ---
    scene bg apartment_lobby with dissolve
    show MsLopez sad at stage_left
    show Uncle sad at stage_right
    show MC sad at stage_center

    # Ms. Lopez, Pose 11: Sad - to MC
    MsLopez "Baby, I loved your mom; she was my best friend."
    MsLopez "But I still can not give away a room, as much as I really want to."

    # MC, Pose 6: Confident - to Ms. Lopez
    show MC confident
    MC "Let me earn it. I know I can do it."
    MC "You got a building falling apart and nobody to fix it. I got no money and only free time. Let me help around here."

    # Ms. Lopez, Pose 16: Admiring - to MC
    show MsLopez admiring
    MsLopez "Hmmm…"
    MsLopez "You sound just like her."

    # Uncle, Pose 4: Wise - to Ms. Lopez
    show Uncle wise
    Uncle "Oh, c'mon now. Have some mercy on the poor boy."

    # Ms. Lopez, Pose 7: Smirk - to MC
    show MsLopez smirk
    MsLopez "Alright, you got yourself a deal."
    MsLopez "If you can help out around here, I will get you a room."

    # --- UP_CelebrateMC / UP_CelebrateUNC: both celebrate at once ---
    scene UP_CelebrateMC with dissolve
    MC "YEY!!"
    Uncle "YEY!!"

    # --- back to the lobby ---
    scene bg apartment_lobby with dissolve
    show MsLopez strict at stage_left
    show Uncle idle at stage_right
    show MC idle at stage_center

    # Ms. Lopez, Pose 3: Strict - to MC
    MsLopez "Don't celebrate just yet."
    MsLopez "Just know that you still have to find a job and pay rent, just like everyone else."
    MsLopez "Don't think you're special just because you're cute."

    # MC, Pose 12: Blush - to Ms. Lopez
    show MC blush
    MC "Ah… Thank you! I won't let you down. I promise."

    # (The door-quest flags are set by A02 when Ms. Lopez formally
    #  assigns the task - no extra flags are needed here.)

    # LOG UPDATE
    "New Task Added: Fix Amber's Door"
    "New Task Added: Get a Job"

    # --- SCENE END ---
    scene black with fade

    return
