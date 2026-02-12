# ==========================================================
# ACT 1 - SCENE A03: Job Interview
# ==========================================================
# Location: Apartment Lobby, Mr. Lee's Store, Boxing Gym, Bean Spill Cafe
# Cast: MC, Ms. Lopez, Mr. Lee, Coach DeShawn, Tanya, Luca
# Objective: Find and secure a job
# ==========================================================

# ==========================================================
# SCENE A03_01 - Reporting to Ms. Lopez
# ==========================================================
label A03_01_REPORT_TO_LOPEZ:
    
    # Fade in
    scene bg apartment_lobby with fade
    
    # Show Ms. Lopez at counter
    # show MsLopez curious
    
    "MC gets back to the main lobby of the apartment building, reporting to Ms. Lopez."
    
    MsLopez curious "Ah, there you are, MC. So, how's the door fixing going?"
    
    MC proud "Completed successfully! Ms. Amber was happy with my work."
    
    MsLopez stern "But you know, fixing the door won't be enough to keep you here."
    
    MsLopez "Remember, no job, no roof. You want to stay? You've got to earn it."
    
    MC polite "I understand…"
    
    MC "Umm, but do you know anywhere that's hiring?"
    
    MC shy "The truth is… I never really had a proper job in my life. Aside from fixing stuff, I had no real work experience."
    
    MsLopez shocked "Wait, not even an after-school gig?"
    
    MsLopez "How will you find a job with no experience at all?"
    
    MC determined "Well… How does anyone get a job?"
    
    MC "Hard work and determination!"
    
    MC "And maybe a recommendation will surely help."
    
    MsLopez impressed "At least you have a good attitude about it…"
    
    MsLopez idle "Alright… I know a few places that might take you in, but you will have to go look around."
    
    MsLopez "There are a lot of work opportunities around the town. And since you have some spare time, go and look for any job out there while I talk to some people I know."
    
    MC determined "Thank you, I won't let you down."
    
    # Set quest flag
    $ quest_find_job = True
    
    # Fade out
    scene black with fade
    
    return

# ==========================================================
# SCENE A03_04.1 - Mr. Lee's Store (Rejected)
# ==========================================================
label A03_04_1_MR_LEE_JOB:
    
    # Fade in
    scene bg mr_lee_store with fade
    
    # Show Mr. Lee
    # show MrLee strict
    
    "MC goes to Mr. Lee's convenience store to ask for a job."
    
    MrLee strict "You again. What you want?"
    
    MC polite "Good afternoon, sir. I'm just wondering if you need a store clerk here."
    
    MrLee mad "No, no. I don't need help. If not buying something, get out."
    
    MC idle "(Yeah… I figured)"
    
    MC "(I don't want to work here anyway…)"
    
    "MC leaves the area."
    
    # Fade out
    scene black with fade
    
    return

# ==========================================================
# SCENE A03_04.2 - Boxing Gym (No Opening)
# ==========================================================
label A03_04_2_BOXING_GYM_JOB:
    
    # Fade in
    scene bg boxing_gym with fade
    
    # Show Coach DeShawn
    # show CoachDeShawn welcoming
    
    "MC was welcomed by Coach DeShawn upon entering the gym."
    
    CoachDeShawn welcoming "What do we have here… A new blood in the gym!"
    
    CoachDeShawn confident "Ready to get some gains, youngblood?"
    
    MC polite "I'm actually looking for a job… Maybe you need a cleaner here or something?"
    
    CoachDeShawn surprised "Oh, really?"
    
    CoachDeShawn idle "Too bad for you. We just hired a janitor last week. Come back again when there's an opening."
    
    MC sad "Bumper…"
    
    MC polite "Well, let me know if there will be any staff hiring here, thanks!"
    
    "MC leaves the area."
    
    # Fade out
    scene black with fade
    
    return

# ==========================================================
# SCENE A03_04.3 - Bean Spill Cafe (SUCCESS)
# ==========================================================
label A03_04_3_BEAN_SPILL_CAFE:
    
    # Exterior of cafe
    scene bg bean_spill_exterior with fade
    
    "MC sees the 'Hiring' sign in the establishment's window. He enters Bean Cafe, hoping to secure a job there despite having no prior experience."
    
    # Interior of cafe
    scene bg bean_spill_cafe with fade
    
    # Show Tanya at counter
    # show Tanya welcoming
    
    "MC approaches Tanya at the counter."
    
    Tanya welcoming "Good Morning, Welcome to the Bean Spill!"
    
    Tanya blushing "Wha—what can I brew for you today?"
    
    MC polite "Hi. I saw the sign on the window, and I was hoping to apply for a job."
    
    Tanya intrigued "Oh? You want to work here, huh…? Do you have any coffee experience? Any serving experience would be recommended."
    
    MC bargaining "Umm, no, not really…"
    
    MC "But how can someone get experience without getting a job?"
    
    Tanya laughing "Hahahahaha, very true."
    
    Tanya "You should probably talk to Luca. He's the owner's son."
    
    Tanya idle "Lucaaaa"
    
    Tanya "Hey, Luca."
    
    Tanya angry "LUCA!!!"
    
    # Luca offscreen
    luca "WHAT!!!"
    
    # Show Luca entering
    # show luca boastful
    
    "Luca comes out of the office, playing video games."
    
    Tanya composed "This gentleman wants to work here."
    
    luca boastful "Of course he does. Everyone wants to work here. We're the best cafe around here!"
    
    Tanya irritated "Sure…"
    
    Tanya seductive "Maybe you should interview him."
    
    Tanya "He looks promising…"
    
    luca serious "Do you know how to make coffee?"
    
    MC confident "Yes, that's easy. I drink coffee every day."
    
    luca serious "What about working at a cash register?"
    
    MC thinking "No, never before. But I'm willing to learn."
    
    MC "How hard could it be?"
    
    luca unbothered "Not very hard…"
    
    luca "You're hired."
    
    MC surprised "Wait, what? Really?"
    
    luca unbothered "Yeah, sure. Start right away if you want."
    
    luca "If my dad calls, tell him I'm busy working."
    
    # hide luca
    
    "Luca then leaves the premises, heading back to his office."
    
    MC disbelief "That seemed easy…"
    
    Tanya annoyed "Luca's dad put him in charge of this place, but he doesn't care too much."
    
    MC curious "So… who's gonna train me?"
    
    Tanya seductive "I guess… I will~"
    
    MC apologetic "Oh… I'm so sorry, didn't mean to give you extra work today."
    
    Tanya laughing "Hahaha. No worries. I actually don't mind~"
    
    Tanya "I'm used to doing all the work around here."
    
    Tanya seductive "Buuut… I think things will be interesting this time, especially with you~"
    
    MC blushing "I—I hope so, too."
    
    # Unique pose: Tanya turns around, MC stares
    
    Tanya "So, let's get you inside~"
    
    Tanya "I mean… to the kitchen~"
    
    # Transition to kitchen
    scene bg bean_spill_kitchen with fade
    
    "The scene transitions after Tanya showed MC around."
    
    Tanya composed "So, that's pretty much it."
    
    Tanya explaining "I guess your task will be cleaning duties here at first. But don't worry, I'll show you how we create coffee here during our free time."
    
    Tanya "Got any questions?"
    
    MC thinking "(...)"
    
    MC "(I understood zero of what she just said. I was busy staring somewhere else…)"
    
    Tanya composed "Ah, MC. Is everything clear?"
    
    MC flustered "Ah, yes! Everything is clear. Hehe…"
    
    Tanya happy "Great! I'll schedule you for an afternoon shift tomorrow. You can go home for now."
    
    Tanya "And remember, don't be late!"
    
    MC happy "Yes, Ma'am!"
    
    # Set quest flags
    $ quest_find_job = False
    $ job_bean_spill = True
    $ quest_secure_apartment = True
    
    # Fade out
    scene black with fade
    
    return

# ==========================================================
# END OF A03 SCENES
# ==========================================================

