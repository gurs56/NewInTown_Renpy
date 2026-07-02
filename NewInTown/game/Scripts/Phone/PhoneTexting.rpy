# ==========================================================
# PHONE TEXTING - draws text-message conversations on the phone
# ==========================================================
# This file makes dialogue show up as text-message bubbles instead
# of the normal bottom-of-screen textbox. It works by turning on
# Ren'Py's built-in "NVL mode" (a mode meant for full-screen text)
# and replacing its look with our own phone-shaped screen below.
# ==========================================================

# Tells Ren'Py: "whenever NVL mode is used, show the screen called
# PhoneDialogue" (defined further down) instead of the default look.
define nvl_mode = "phone"

# The phone right-aligns the player's own texts by matching the
# speaker name to mc_name (the single source of truth in Characters/MC.rpy).


# ----------------------------------------------------------
# SETUP - runs once when the game starts (init -1 = run early,
# before most other init code, so these are ready when needed)
# ----------------------------------------------------------
init -1 python:
    # Where the phone sits on screen when only ONE message is
    # showing (see phone_appear below). 0.3 = slightly left of
    # center, 0.5 = vertically centered.
    phone_position_x = 0.3
    phone_position_y = 0.5

    def Phone_ReceiveSound(event, interact=True, **kwargs):
        # Plays a "text received" sound effect. Ren'Py calls this
        # automatically at certain points while a screen is shown;
        # we only care about the "show_done" event (the screen has
        # finished appearing), so every other event is ignored.
        if event == "show_done":
            renpy.sound.play("audio/ReceiveText.ogg")

    def Phone_SendSound(event, interact=True, **kwargs):
        # Same idea, but for a "text sent" sound effect.
        if event == "show_done":
            renpy.sound.play("audio/SendText.ogg")

    def print_bonjour():
        # Leftover test/debug function - not used by the phone
        # itself. Safe to delete once you confirm nothing calls it.
        print("bonjour")


# ----------------------------------------------------------
# TRANSFORMS - reusable animations/positions for phone elements
# ----------------------------------------------------------

# Keeps the phone frame centered at a given x/y position.
# (pXalign/pYalign let the caller override where it sits.)
transform phone_transform(pXalign=0.5, pYalign=0.5):
    xcenter pXalign
    yalign pYalign

# Slide-up entrance animation for the phone frame.
# Only played when the conversation has just ONE message on
# screen (i.e. the very first message of a new chat) - see the
# "if len(dialogue) == 1" check in PhoneDialogue below.
transform phone_appear(pXalign=0.5, pYalign=0.5):
    xcenter pXalign
    yalign pYalign

    on show:
        yoffset 1080          # start fully off-screen, below the frame
        easein_back 1.0 yoffset 0   # slide up into place over 1 second

# Makes a single message bubble slide in from the side and fade in.
# pDirection: 1 = slide in from the right (player's own texts),
#            -1 = slide in from the left (the other person's texts).
transform message_appear(pDirection):
    alpha 0.0
    xoffset 50 * pDirection
    parallel:
        ease 0.5 alpha 1.0          # fade in over half a second
    parallel:
        easein_back 0.5 xoffset 0  # slide into place over half a second

# Makes the little sender-icon (the round avatar next to a bubble)
# pop in with a quick zoom, instead of just appearing instantly.
transform message_appear_icon():
    zoom 0.0
    easein_back 0.5 zoom 1.0

# Fade-and-drop-in animation used for narrator lines (lines with no
# speaker, e.g. "MC glances at his phone.").
transform message_narrator:
    alpha 0.0
    yoffset -50
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        easein_back 0.5 yoffset 0


# ==========================================================
# THE PHONE SCREEN - what NVL mode actually displays
# ==========================================================
# Ren'Py calls this screen automatically (because of
# `define nvl_mode = "phone"` above) every time a text-message
# scene plays. `dialogue` is the full list of messages said so
# far in this conversation; Ren'Py hands it to us automatically.
screen PhoneDialogue(dialogue, items=None):

    # Every widget inside this screen looks up its style in
    # styles named "phoneFrame_..." (defined near the bottom of
    # this file) instead of Ren'Py's defaults.
    style_prefix "phoneFrame"

    frame at phone_transform(phone_position_x, phone_position_y):
        # Only play the slide-up "phone appears" animation on the
        # very first message - once the chat has more messages,
        # the phone should just stay in place while new bubbles
        # animate in on their own (see message_appear above).
        if len(dialogue) == 1:
            at phone_appear(phone_position_x, phone_position_y)

        viewport:
            # Lets the player click-drag or scroll the conversation
            # if it's taller than the phone screen.
            draggable True
            mousewheel True
            yinitial 1.0   # start scrolled all the way down (newest message visible)
            vbox:
                null height 20     # small gap above the first message
                use nvl_phonetext(dialogue)   # draw all the message bubbles (below)
                null height 100    # gap below the last message (room to scroll to)


# ----------------------------------------------------------
# MESSAGE BUBBLES - draws every line of the conversation
# ----------------------------------------------------------
# This is the part that turns each line of dialogue into either
# a plain narrator line or a chat bubble with an avatar icon.
screen nvl_phonetext(dialogue):
    # Don't inherit "phoneFrame" styles here - these widgets use
    # Ren'Py's plain defaults so we can style bubbles manually.
    style_prefix None

    # Tracks who spoke the PREVIOUS line, so we know when a NEW
    # speaker starts talking (that's when we show their name/icon).
    $ previous_d_who = None

    # Loop over every line said so far in this conversation.
    # `d` is one line of dialogue; `d.who` is the speaker's name
    # (or None for narrator lines), and `d.what` is the text.
    for id_d, d in enumerate(dialogue):

        if d.who == None:
            # --- NARRATOR LINE (no speaker) ---
            text d.what:
                    xpos -335
                    ypos 0.0
                    xsize 350
                    text_align 0.5
                    italic True
                    size 28
                    slow_cps False
                    id d.what_id
                    # Only animate the newest line, not old ones
                    # that are just being redrawn as the chat scrolls.
                    if d.current:
                        at message_narrator
        else:
            # --- CHAT BUBBLE (someone is speaking) ---

            # Pick which bubble-background image to use: a
            # different shape/color for the player's own texts
            # vs. the other person's texts.
            if d.who == mc_name:
                $ message_frame = "phone_send_frame.png"
            else:
                $ message_frame = "phone_received_frame.png"

            hbox:
                spacing 10
                # The player's own messages sit on the RIGHT side of
                # the phone; box_reverse flips the icon+bubble order
                # so the bubble is on the left, icon on the right.
                if d.who == mc_name:
                    box_reverse True

                # Only show the little avatar icon the FIRST time a
                # new speaker starts talking (not on every line) -
                # this is what makes consecutive messages from the
                # same person look grouped together, like a real
                # texting app.
                if previous_d_who != d.who:
                    if d.who == mc_name:
                        $ message_icon = "phone_send_icon.png"
                    else:
                        $ message_icon = "phone_received_icon.png"

                    add message_icon:
                        # Only animate the icon in if this message is
                        # brand new (not being redrawn from scrolling).
                        if d.current:
                            at message_appear_icon()

                else:
                    # Same speaker as last time - leave empty space
                    # where the icon would go, so the bubble still
                    # lines up neatly under the previous one.
                    null width 107

                vbox:
                    yalign 1.0
                    # Show the speaker's name only above their FIRST
                    # bubble in a row, and never for the player's own
                    # texts (a real phone doesn't label "you").
                    if d.who != mc_name and previous_d_who != d.who:
                        text d.who

                    frame:
                        padding (20,20)

                        # The bubble's background image/shape, picked above.
                        background Frame(message_frame, 23,23,23,23)
                        xsize 350

                        # Slide the newest bubble in from the correct
                        # side; older bubbles just appear instantly
                        # (no animation replay) when the list redraws.
                        if d.current:
                            if d.who == mc_name:
                                at message_appear(1)
                            else:
                                at message_appear(-1)

                        text d.what:
                            pos (0,0)
                            xsize 350
                            slow_cps False

                            if d.who == mc_name :
                                # Player's own texts: white text,
                                # right-aligned, nudged left so the
                                # bubble reads correctly on that side.
                                color "#FFF"
                                text_align 1.0
                                xpos -580
                            else:
                                # The other person's texts: plain
                                # black text, left-aligned (default).
                                color "#000"

                            id d.what_id
        # Remember who just spoke, so the NEXT loop can tell
        # whether the speaker changed.
        $ previous_d_who = d.who


# ==========================================================
# STYLES - the look of the phone frame and its contents
# ==========================================================
# "is default" means: start from Ren'Py's built-in look, then
# only override the specific parts listed below.
style phoneFrame is default

# The phone's outer frame: the background/foreground artwork
# (the phone "case" image) and its on-screen size.
style phoneFrame_frame:
    background Transform("images/Phone/phone_background.png", xcenter=0.5,yalign=0.5)
    foreground Transform("images/Phone/phone_foreground.png", xcenter=0.5,yalign=0.5)

    # Same size as the home-screen phone (PHONE_SIZE is defined
    # once in Phone/PhoneApp.rpy so both screens always match).
    xsize PHONE_SIZE[0]
    ysize PHONE_SIZE[1]

# The scrollable area that holds all the message bubbles.
style phoneFrame_viewport:
    yfill True
    xfill True
    yoffset -20   # nudge up slightly so bubbles sit inside the phone's screen art

# The vertical list of message bubbles inside the viewport.
style phoneFrame_vbox:
    spacing 10   # gap between each message bubble
    xfill True
