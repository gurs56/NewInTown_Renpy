
define MC = Character("[mc_name]", color="#54c0f2", image="MC")

# ==========================================================
# MC NAME - single source of truth (player-changeable)
# ==========================================================
# In the script/team the MC is "mc", but in-game the player will
# get to choose their name. `mc_name` is a `default`, so it's part
# of each save and can change mid-playthrough. The Character above
# uses "[mc_name]", which re-reads this every time the MC speaks,
# so changing it updates ALL dialogue, narration ([mc_name]) and
# the phone instantly. Starts as "Barry" until the player picks.
default mc_name = "Barry"

# Drop-in name entry. When the name-entry screen is built, either
# `call set_player_name` from it, or just set `mc_name` directly
# from your screen (e.g. action SetVariable). Nothing else to change.
label set_player_name:
    python:
        _n = renpy.input("What should we call you?", default=mc_name, length=20).strip()
        mc_name = _n if _n else "Barry"
    return

# ==========================================================
# EXPRESSIONS (placeholder)
# ==========================================================
# The CANONICAL POSES below are the official pose list for the
# artist. LEGACY MOODS are older words the scripts still use; they
# stay working until the scripts are migrated to a canonical pose.
init python:
    # ------------------------------------------------------
    # CANONICAL POSES - the official pose list (what the
    # artist will draw). This is the source of truth; add or
    # remove poses here as art is planned.
    # Mirrors the pose sheet: # / pose (aliases) / art status.
    # ------------------------------------------------------
    MC_poses = [
        "idle",         #  1 Idle (Neutral/Polite)              Finished
        "happy",        #  2 Happy (Sincere)                    Sketch
        "innocent",     #  3 Innocent                           Sketch
        "laughing",     #  4 Laughing                           Sketch
        "excited",      #  5 Excited (Celebrating)              HOLD
        "confident",    #  6 Confident (Proud/Determined)       Sketch
        "sad",          #  7 Sad (Apologetic)                   Sketch
        "thinking",     #  8 Thinking (Confused/Curious)        Sketch
        "worried",      #  9 Worried (Nervous/Sweating/Lying)   Sketch
        "scared",       # 10 Scared (Panicking)                 Sketch
        "surprised",    # 11 Surprised (Shock)                  -
        "blush",        # 12 Blush (Flustered/Shy)              Sketch
        "smug",         # 13 Smug (Mischievous/Grinning)        Sketch
        "disgusted",    # 14 Disgusted                          Sketch
        "explaining",   # 15 Explaining                         -
        "bargaining",   # 16 Bargaining (Pleading)              Sketch
        "horny",        # 17 Horny                              -
        "scratch",      # 18 Scratch (back of head)             Sketch
        "tears",        # 19 Looking down, tears in his eyes    -
    ]

    # ------------------------------------------------------
    # LEGACY MOODS - older words still used by story scripts
    # that AREN'T canonical poses yet. Kept working (they show
    # the placeholder) so nothing crashes. To retire one:
    # change the script to a canonical pose above, then
    # delete the word here.
    # ------------------------------------------------------
    MC_legacy_moods = [
        "apologetic", "blushing", "celebrating", "confused", "curious", "determined",
        "disbelief", "enthusiastic", "flustered", "hesitant", "intrigued", "mischievous",
        "neutral", "panicking", "polite", "proud", "shy", "tired",
    ]

    # ------------------------------------------------------
    # ART. The clothed idle is the only FINISHED sprite, and it is
    # what any pose without its own art falls back to - so MC
    # always looks right, he just may not change expression on
    # that line.
    #
    # Ten of his expressions exist as pencil roughs and are wired
    # as stand-ins, which is most of his screen time: 70 of his
    # 114 lines now change expression instead of showing the same
    # finished sprite throughout. To go back to "finished sprite
    # everywhere", empty MC_sketch_art below - nothing else needs
    # touching. As each rough is inked, move it up into
    # MC_pose_art and it takes over automatically.
    #
    # The wired copies are the prepared ones in SK/. The scans
    # are flattened onto an opaque white page, which would draw a
    # white box on stage, so the page is keyed out to
    # transparency first (tools/clean_sketches.py). They sit on a
    # square 2048 canvas at their own zoom, hence the separate
    # "MC_SK" camera row.
    #
    # Still needing art, with no rough drawn yet:
    #   sad (11 lines), bargaining (11), excited (2),
    #   surprised (2), explaining (1), horny (0)
    #
    # The nude / nude_erect finals sit beside this file in
    # images/Characters/MC/ but are not wired to a mood - no scene
    # asks for them yet.
    # ------------------------------------------------------
    MC_default_art = "images/Characters/MC/nit_mc_full_clothed.png"

    # Finished, inked art. A pose listed here beats its sketch.
    MC_pose_art = {
        # "happy": "images/Characters/MC/...",   <- per-expression art
    }

    MC_sketch_art = {
        "happy":     "images/Characters/MC/SK/NAT_CH_MC_Happy_SK_v01.png",
        "innocent":  "images/Characters/MC/SK/NAT_CH_MC_Innocent_SK_v01.png",
        "laughing":  "images/Characters/MC/SK/NAT_CH_MC_Laughing_SK_v01.png",
        "confident": "images/Characters/MC/SK/NAT_CH_MC_Confident_SK_v01.png",
        "thinking":  "images/Characters/MC/SK/NAT_CH_MC_Thinking_SK_v01.png",
        "worried":   "images/Characters/MC/SK/NAT_CH_MC_Worried_SK_v01.png",
        "scared":    "images/Characters/MC/SK/NAT_CH_MC_Scared_SK_v01.png",
        "blush":     "images/Characters/MC/SK/NAT_CH_MC_Blush_SK_v01.png",
        "smug":      "images/Characters/MC/SK/NAT_CH_MC_Smug_SK_v01.png",
        "disgusted": "images/Characters/MC/SK/NAT_CH_MC_Disgusted_SK_v01.png",
    }

    # Legacy words that are just another name for a pose with art.
    MC_legacy_art_alias = {
        "blushing":    "blush",
        "flustered":   "blush",
        "shy":         "blush",
        "confused":    "thinking",
        "curious":     "thinking",
        "intrigued":   "thinking",
        "determined":  "confident",
        "proud":       "confident",
        "mischievous": "smug",
        "panicking":   "scared",
        "hesitant":    "worried",
    }

    # NB: do not name a temporary here `_p` - that is Ren'Py's own
    # gettext helper, and deleting it breaks gui.about.
    for _m in MC_poses + MC_legacy_moods:
        _pose = MC_legacy_art_alias.get(_m, _m)
        if _pose in MC_pose_art:
            _img = framed_sprite("MC", MC_pose_art[_pose])
        elif _pose in MC_sketch_art:
            _img = framed_sprite("MC_SK", MC_sketch_art[_pose])
        else:
            _img = framed_sprite("MC", MC_default_art)
        renpy.image("MC " + _m, _img)
    del _m, _pose, _img
