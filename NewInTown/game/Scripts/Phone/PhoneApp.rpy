# ==========================================================
# PHONE APP - The pocket phone the player can open anytime
# ==========================================================
# A little phone button (next to the Map button) "bigs up" into
# the full phone shell with a home screen of app buttons.

# One place for the phone's on-screen size. PhoneTexting.rpy's
# frame uses this too, so the shell always matches everywhere.
define PHONE_SIZE = (495, 815)

# ----------------------------------------------------------
# THE APP LIST - to add an app to the phone, add ONE line here:
#     ("App name", <what clicking it does>),
# NullAction() means "does nothing yet". Real apps will use
# actions like Show("phone_messages") once their screens exist.
# The home grid is 3 wide x 2 tall, so up to 6 apps fit for now.
# ----------------------------------------------------------
define phone_apps = [
    ("App 1", NullAction()),
    ("App 2", NullAction()),
    ("App 3", NullAction()),
    ("App 4", NullAction()),
    ("App 5", NullAction()),
    ("App 6", NullAction()),
]

# Grow-in / shrink-out animation for the enlarged phone.
transform phone_bigup:
    on show:
        zoom 0.15 alpha 0.0
        easein_back 0.35 zoom 1.0 alpha 1.0
    on hide:
        easein 0.20 zoom 0.15 alpha 0.0


# ----------------------------------------------------------
# The enlarged phone.
# Shown via ToggleScreen from the phone button. Tapping the dim
# backdrop (off the phone) closes it; tapping the phone doesn't.
# ----------------------------------------------------------
screen phone_home():
    # Above the HUD (time_display is zorder 1000) so the open phone
    # covers the Map/time buttons and they can't be clicked through.
    zorder 1100
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
        xysize PHONE_SIZE
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

                for app_name, app_action in phone_apps:
                    button:
                        xysize (110, 110)
                        background "#ffffff22"
                        hover_background "#ffffff44"
                        action app_action
                        text "[app_name]":
                            align (0.5, 0.5)
                            size 20
                            text_align 0.5

                # Fill any leftover grid cells so 3x2 stays valid
                # even with fewer than 6 apps in the list.
                for _i in range(6 - len(phone_apps)):
                    null


style phoneApp_frame:
    background Transform("images/Phone/phone_background.png")
    foreground Transform("images/Phone/phone_foreground.png")
    xsize PHONE_SIZE[0]
    ysize PHONE_SIZE[1]
    xalign 0.5
    yalign 0.5
    padding (45, 90, 45, 70)
