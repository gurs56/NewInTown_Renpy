# ==========================================================
# POSTERS - one-shot story paintings (CG)
# ==========================================================
# A "poster" is a single-use, full-screen painting tied to a FIXED
# canonical NAME, e.g. "A00 - Intercity_Bus". That name never
# changes - it is both the on-screen label while the art is
# unfinished AND the filename the finished painting must use.
#
#   Finished art goes in:  images/Posters/<NAME>.png
#   e.g.                   images/Posters/A00 - Intercity_Bus.png
#
# Use it in a script just like a scene statement:
#
#   scene expression Poster("A00 - Intercity_Bus") with dissolve
#
# While the .png is missing, a labelled placeholder card stands in
# so the scene plays fully. Drop the correctly-named png into
# images/Posters/ and it shows automatically - nothing else to edit.
#
# WHY NO `define` PER POSTER:
# Each poster is shown exactly once, so there's nothing to reuse.
# Defining a global image for every one-shot CG would bloat the
# shared image namespace. Here the NAME at the call site IS the
# definition, and it's guaranteed to match the final art file.
# ==========================================================

define POSTER_DIR = "images/Posters/"

init python:
    def Poster(name):
        """Return the finished poster image if it exists in
        images/Posters/, otherwise a placeholder card showing the
        poster's canonical name so the scene stays playable."""
        path = POSTER_DIR + name + ".png"
        if renpy.loadable(path):
            return path

        # --- Placeholder: dark card + the poster's name + a note ---
        return Fixed(
            Solid("#15151f"),
            Text(
                "{size=72}" + name + "{/size}\n\n"
                "{size=30}{color=#8a8aa0}(poster art in progress){/color}{/size}",
                align=(0.5, 0.5),
                text_align=0.5,
            ),
            xysize=(config.screen_width, config.screen_height),
        )
