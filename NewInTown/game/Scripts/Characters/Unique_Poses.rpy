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
    unique_poses = [
        "UP_Scratch",        # MC             - Scratching the back of his head
        "UP_BoobFaceLopez",  # MC / Ms. Lopez - Ms. Lopez hugs MC with her boobs in his face
        "UP_CelebrateMC",    # MC             - MC and Uncle both celebrate at the same time
        "UP_CelebrateUNC",   # Uncle          - MC and Uncle both celebrate at the same time
        "UP_EyesWild",       # MC             - MC's eyes widen and jaw drops while blushing
        "UP_BenDover",       # Amber          - Amber's bent over, seeing her butt in her underwear
        "UP_LookDown",       # Uncle          - Uncle looks down at his tools from his junk stand
        "UP_GrabHingeMC",    # MC / Uncle     - MC goes to grab hinges, Uncle grabs his hands to stop him
        "UP_HandsRing",      # MC / Uncle     - MC hands the ring over to Uncle
        "UP_BigGot",         # Tanya          - Tanya turns around showing her big monster ass
        "UP_Playboy_Find",   # MC             - MC opens the magazine, eyes widen, crotch bulges
        "UP_Playboy_Love",   # Ms. Lopez      - MC shows Ms. Lopez the Playboy magazines; she looks intently
        "UP_Playboy_Horny",  # Ms. Lopez      - Ms. Lopez gets horny looking at the magazines
        "UP_KnockDoor",      # MC             - MC knocks on the door
        "UP_FlashLight",     # MC             - MC holds the flashlight for Razor
        "UP_StepLadder",     # Razor          - Razor is on a stepladder working on the pipe
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
