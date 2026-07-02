# ==========================================================
# PHONE APP - The pocket phone the player can open anytime
# ==========================================================
# A little phone button (next to the Map button) "bigs up" into
# the full phone shell. For now the shell is empty - apps and a
# home screen get layered on top of this later.

# Grow-in / shrink-out animation for the enlarged phone.
transform phone_bigup:
    on show:
        zoom 0.15 alpha 0.0
        easein_back 0.35 zoom 1.0 alpha 1.0
    on hide:
        easein 0.20 zoom 0.15 alpha 0.0


# ----------------------------------------------------------
# The enlarged phone shell.
# Shown via ToggleScreen from the phone button. Tapping outside
# the phone (the dim backdrop) or the Close button hides it.
# ----------------------------------------------------------
screen phone_home():
    zorder 950
    modal True

    # Dim backdrop - tap anywhere off the phone to close.
    button:
        xfill True
        yfill True
        background "#00000099"
        action Hide("phone_home")

    # The phone itself, centered and animated. The whole phone is a
    # click-capturing button (NullAction) so tapping anywhere on the
    # phone png keeps it open - only the backdrop behind closes it.
    button:
        xysize (495, 815)
        xalign 0.5
        yalign 0.5
        at phone_bigup
        action NullAction()
        background None

        frame:
            style_prefix "phoneApp"

            # --- App buttons, laid out 3 across / 2 down ---
            grid 3 2:
                xalign 0.5
                yalign 0.5
                xspacing 25
                yspacing 30

                for i in range(1, 7):
                    button:
                        xysize (110, 110)
                        background "#ffffff22"
                        hover_background "#ffffff44"
                        action NullAction()
                        text "[i]":
                            align (0.5, 0.5)
                            size 30


style phoneApp_frame:
    background Transform("images/Phone/phone_background.png")
    foreground Transform("images/Phone/phone_foreground.png")
    xsize 495
    ysize 815
    xalign 0.5
    yalign 0.5
    padding (45, 90, 45, 70)
