# ==========================================================
# UNIQUE POSES - one-off story poses / mini-CGs
# ==========================================================
# These are special poses used in ONE specific moment (unlike the
# reusable mood poses in the other Characters/*.rpy files). Each id
# below becomes an image, so a script can simply do:
#
#     show UP_KnockDoor
#     scene UP_BoobFaceLopez with dissolve
#
# The art isn't drawn yet, so each one shows a labeled placeholder
# card (its id) until real art is dropped at
# images/Poses/<UP_id>.png - then it swaps in automatically.
#
# TO ADD A UNIQUE POSE: add its id to the list below.
# ==========================================================

init python:
    # ------------------------------------------------------
    # # / scene(s) / character(s) / description / art status
    # UP_Scratch is reused across several scenes - it is listed
    # once here with every scene that calls for it.
    # ------------------------------------------------------
    unique_poses = [
        # NOTE: "Scratch (back of head)" used to live here as
        # UP_Scratch. PoseList v02 moves it into MC's GENERAL poses
        # as mc_g_scratch (#18), which is what it always needed to be
        # - it is spoken through mid-conversation, and a full-screen
        # card would have wiped the scene behind it. Use `MC scratch`.
        # The same reasoning applies to lopez_u_tears, which lives in
        # MsLopez_poses as `tears`.

        # 1  A01      MC / Ms. Lopez  Ms. Lopez hugs MC, his face in her chest - she is glad
        "UP_BoobFaceLopez_Happy",
        # 2  A01      MC / Ms. Lopez  ...the same hug, but she has just heard the news   HOLD
        "UP_BoobFaceLopez_Sad",
        # 3  A01      MC              MC and Uncle both celebrate at the same time
        "UP_CelebrateMC",
        # 4  A01      Uncle           MC and Uncle both celebrate at the same time
        "UP_CelebrateUNC",
        # 5  A02_02   MC              MC's eyes widen and jaw drops while blushing
        "UP_EyesWild",
        # 6  A02_02   Amber           Amber's bent over, seeing her butt in her underwear
        "UP_BenDover",
        # 7  A02_04   Uncle           Uncle looks down at his tools from his junk stand
        "UP_LookDown",
        # 8  A02_04   MC / Uncle      MC goes to grab hinges, Uncle grabs his hands to stop him
        "UP_GrabHingeMC",
        # 9  A02_04   MC / Uncle      MC hands the ring over to Uncle
        "UP_HandsRing",
        # 10 A03_04   Tanya           Tanya turns around showing her big monster ass
        "UP_BigGot",
        # 11 A04_02   MC              MC opens the magazine, eyes widen, crotch bulges
        "UP_Playboy_Find",
        # 12 A04_03   Ms. Lopez       MC shows her the Playboy magazines; she looks intently
        "UP_Playboy_Love",
        # 13 A04_03   Ms. Lopez       Ms. Lopez gets horny looking at the magazines
        "UP_Playboy_Horny",
        # 14 A04_04   MC              MC knocks on the door
        "UP_KnockDoor",
        # 15 A04_05   MC              MC holds the flashlight for Razor
        "UP_FlashLight",
        # 16 A04_05   Razor           Razor is on a stepladder working on the pipe
        "UP_StepLadder",
        # 17 B01_01   Viv             Viv walks into the college and scans her ID
        "UP_ScanID",

        # ---- Tanya side quest (S01) ----
        # 1  S01_01   MC              MC is cleaning tables
        "UPS_Cleaning",
        # 2/3 S01_01  MC / Tanya      Tanya gives MC a kiss on the cheek
        "UPS_KissCheek",
        #    S01_02   Ms. Lopez       Sour face, sets the cup down after a single sip
        "UP_BadSip",
        #    S01_02   Tanya           Explaining how to tamp down an espresso
        "UP_TeachTramping",
        #    S01_02   MC / Tanya      Tanya's hands over MC's on the tamper, chin near
        #                             his shoulder; MC has gone completely still
        "UP_WatchTramping",
        #    S01_02   Tanya           Same tamper pose, but she is laughing
        "UP_LaughTramping",
        #    S01_02   MC / Tanya      Tanya kisses MC on the lips, hand on his chest
        "UP_TanFirstKiss",

        # ---- SP: recurring special poses ----
        # 1  MC                       MC is blushing with a boner
        "SP_Boner",
        # 2  MC                       MC is trying to hide his boner
        "SP_BonerHide",
    ]

    # Register each pose as an image. Real art wins if it exists;
    # otherwise a labeled placeholder card (the id) stands in.
    for _id in unique_poses:
        _path = "images/Poses/" + _id + ".png"
        if renpy.loadable(_path):
            renpy.image(_id, _path)
        else:
            renpy.image(_id, Fixed(
                Solid("#1f1524"),
                Text(_id, size=64, align=(0.5, 0.5), text_align=0.5),
                xysize=(config.screen_width, config.screen_height),
            ))
    del _id, _path
