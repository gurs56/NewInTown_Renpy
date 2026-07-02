
init python:
    # ------------------------------------------------------
    # NAVIGATION
    # ------------------------------------------------------
    # Every location / map screen shares `tag location` (declared
    # in each screen). Ren'Py only keeps ONE screen per tag on
    # screen at a time, so showing a new location automatically
    # hides the previous one. There is NO master list to keep in
    # sync: to add a new location, just write a screen with
    # `tag location` - nothing here needs editing.

    def go_to_world_map():
        """Open the world map. The `location` tag hides whatever
        location screen is currently showing."""
        renpy.show_screen("world_map_screen")
        renpy.restart_interaction()

# ==========================================================
# MAP IMAGES
# ==========================================================

image bg world_map = im.Scale("images/Test_Map/World_Map.png", 1920, 1080)
image bg mid_town_map = im.Scale("images/Test_Map/Mid_Town_Map.png", 1920, 1080)

# ==========================================================
# WORLD MAP SCREEN
# ==========================================================
screen world_map_screen():
    tag location
    modal True
    zorder 100

    add "bg world_map"

    use nav_button("Mid Town", "mid_town_map_screen", 910, 490, 100, 20)

# ==========================================================
# MID TOWN MAP SCREEN
# ==========================================================
screen mid_town_map_screen():
    tag location
    modal True
    zorder 100

    add "bg mid_town_map"

    use nav_button("World Map", "world_map_screen", 50, 50, 100, 20)
    use nav_button("Apartment", "apartment_building_screen", 910, 490, 100, 20)
    use nav_button("Cafe", "cafe_building_screen", 600, 490, 100, 20)
    use nav_button("Corner Store", "grocery_store_screen", 1200, 490, 100, 20)
