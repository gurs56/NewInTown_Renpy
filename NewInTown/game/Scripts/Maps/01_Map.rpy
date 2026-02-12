
init:
    pass

# ==========================================================
# MAP IMAGES
# ==========================================================

image bg world_map = im.Scale("images/Test_Map/World_Map.png", 1920, 1080)
image bg mid_town_map = im.Scale("images/Test_Map/Mid_Town_Map.png", 1920, 1080)


# ==========================================================
# MAP INTERFACE BUTTON 
# ==========================================================
screen map_button_v2():
    # Using imagebutton with custom image
    imagebutton:
        idle "gui/blacksqaure_Button_Map.jpg"
        hover "gui/blacksqaure_Button_Map.jpg"
        xysize (100, 100)
        xpos 40
        ypos 30
        action Show("world_map_screen")

# ==========================================================
# WORLD MAP SCREEN
# ==========================================================
screen world_map_screen():
    modal True
    zorder 100
    
    # The map image
    add "bg world_map"
    
    # Exit button - TOP LEFT
    button:
        xysize (100, 100)
        xpos 50
        ypos 50
        action Quit(confirm=False)
        add "gui/blacksqaure_Button_Map.jpg" fit "contain"
    
    # Mid Town Map button - MIDDLE
    button:
        xysize (100, 100)
        xpos 910
        ypos 490
        action [Hide("world_map_screen"), Show("mid_town_map_screen")]
        add "gui/blacksqaure_Button_Map.jpg" fit "contain"

# ==========================================================
# MID TOWN MAP SCREEN
# ==========================================================
screen mid_town_map_screen():
    modal True
    zorder 100
    
    # The mid town map image
    add "bg mid_town_map"
    
    # Back to world map button
    button:
        xysize (100, 100)
        xpos 50
        ypos 50
        action [Hide("mid_town_map_screen"), Show("world_map_screen")]
        add "gui/blacksqaure_Button_Map.jpg" fit "contain"
    
    # Apartment Building button
    button:
        xysize (100, 100)
        xpos 910
        ypos 490
        action [Hide("mid_town_map_screen"), Show("apartment_building_screen")]
        add "gui/blacksqaure_Button_Map.jpg" fit "contain"


