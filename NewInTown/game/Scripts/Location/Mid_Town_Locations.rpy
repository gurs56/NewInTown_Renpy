# ==========================================================
# MID TOWN LOCATIONS
# ==========================================================
# This file contains all the location screens for Mid Town
# including apartments, shops, etc.

# ==========================================================
# APARTMENT BUILDING SCREEN
# ==========================================================
screen apartment_building_screen():
    modal True
    zorder 100
    add "bg apartment_building"
    # Back to mid town map button (Top Left)
    button:
        xysize (100, 100)
        xpos 50
        ypos 50
        action [Hide("apartment_building_screen"), Show("mid_town_map_screen")]
        add "gui/blacksqaure_Button_Map.jpg" fit "contain"
        text "To Mid Town Map" xalign 0.5 yalign 0.8 size 24
    # Enter Lobby button - CENTER
    button:
        xysize (150, 150)
        xpos 885
        ypos 465
        action [Hide("apartment_building_screen"), Show("apartment_lobby_screen")]
        add "gui/blacksqaure_Button_Map.jpg" fit "contain"
        text "To Lobby" xalign 0.5 yalign 0.8 size 28
    text "Apartment Building" xalign 0.5 yalign 0.1 size 50

# ==========================================================
# APARTMENT LOBBY SCREEN
# ==========================================================
screen apartment_lobby_screen():
    modal True
    zorder 100
    add "bg apartment_lobby"
    use character_buttons_lobby
    # Back to apartment building button (Top Left)
    button:
        xysize (100, 100)
        xpos 50
        ypos 50
        action [Hide("apartment_lobby_screen"), Show("apartment_building_screen")]
        add "gui/blacksqaure_Button_Map.jpg" fit "contain"
        text "To Building Entrance" xalign 0.5 yalign 0.8 size 24
    # Elevator button (Left Center)
    button:
        xysize (120, 120)
        xpos 800
        ypos 500
        action [Hide("apartment_lobby_screen"), Show("apartment_elevator_screen")]
        add "gui/blacksqaure_Button_Map.jpg" fit "contain"
        text "To Elevator" xalign 0.5 yalign 0.8 size 28
    # Landlord Office (Ms. Lopez) button (Right Center)
    button:
        xysize (120, 120)
        xpos 1050
        ypos 500
        action [Hide("apartment_lobby_screen"), Show("apartment_landlord_office_screen")]
        add "gui/blacksqaure_Button_Map.jpg" fit "contain"
        text "To Ms. Lopez Office" xalign 0.5 yalign 0.8 size 28
    text "Apartment Lobby" xalign 0.5 yalign 0.1 size 50

# ==========================================================
# APARTMENT ELEVATOR SCREEN
# ==========================================================
screen apartment_elevator_screen():
    modal True
    zorder 100
    add "bg apartment_elevator"
    # Button to basement (Left)
    button:
        xysize (120, 120)
        xpos 300
        ypos 500
        action [Hide("apartment_elevator_screen"), Show("apartment_basement_screen")]
        add "gui/blacksqaure_Button_Map.jpg" fit "contain"
        text "To Basement" xalign 0.5 yalign 0.8 size 24
    # Button to apartment hallway (Center)
    button:
        xysize (120, 120)
        xpos 800
        ypos 500
        action [Hide("apartment_elevator_screen"), Show("apartment_hallway_screen")]
        add "gui/blacksqaure_Button_Map.jpg" fit "contain"
        text "To Hallway" xalign 0.5 yalign 0.8 size 24
    # Button to lobby (Right)
    button:
        xysize (120, 120)
        xpos 1300
        ypos 500
        action [Hide("apartment_elevator_screen"), Show("apartment_lobby_screen")]
        add "gui/blacksqaure_Button_Map.jpg" fit "contain"
        text "To Lobby" xalign 0.5 yalign 0.8 size 24
    text "Apartment Elevator" xalign 0.5 yalign 0.1 size 50

# ==========================================================
# APARTMENT HALLWAY SCREEN
# ==========================================================
screen apartment_hallway_screen():
    modal True
    zorder 100
    add "bg apartment_hallway"
    # Button to Razor's Apartment (Far Left)
    button:
        xysize (120, 120)
        xpos 200
        ypos 500
        action [Hide("apartment_hallway_screen"), Show("apartment_razor_apartment_screen")]
        add "gui/blacksqaure_Button_Map.jpg" fit "contain"
        text "To Razor's Apartment" xalign 0.5 yalign 0.8 size 24
    # Button to MC's Apartment (Left Center)
    button:
        xysize (120, 120)
        xpos 600
        ypos 500
        action [Hide("apartment_hallway_screen"), Show("apartment_mc_apartment_screen")]
        add "gui/blacksqaure_Button_Map.jpg" fit "contain"
        text "To MC's Apartment" xalign 0.5 yalign 0.8 size 24
    # Button to Amber's Apartment (Right Center)
    button:
        xysize (120, 120)
        xpos 1000
        ypos 500
        action [Hide("apartment_hallway_screen"), Show("apartment_amber_apartment_screen")]
        add "gui/blacksqaure_Button_Map.jpg" fit "contain"
        text "To Amber's Apartment" xalign 0.5 yalign 0.8 size 24
    # Button back to elevator (Far Right)
    button:
        xysize (120, 120)
        xpos 1400
        ypos 500
        action [Hide("apartment_hallway_screen"), Show("apartment_elevator_screen")]
        add "gui/blacksqaure_Button_Map.jpg" fit "contain"
        text "To Elevator" xalign 0.5 yalign 0.8 size 24
    text "Apartment Hallway" xalign 0.5 yalign 0.1 size 50

# ==========================================================
# APARTMENT BASEMENT SCREEN
# ==========================================================
screen apartment_basement_screen():
    modal True
    zorder 100
    add "bg apartment_basement"
    # Button to boiler room (Left)
    button:
        xysize (120, 120)
        xpos 300
        ypos 500
        action [Hide("apartment_basement_screen"), Show("apartment_boiler_room_screen")]
        add "gui/blacksqaure_Button_Map.jpg" fit "contain"
        text "To Boiler Room" xalign 0.5 yalign 0.8 size 24
    # Button back to elevator (Right)
    button:
        xysize (120, 120)
        xpos 1300
        ypos 500
        action [Hide("apartment_basement_screen"), Show("apartment_elevator_screen")]
        add "gui/blacksqaure_Button_Map.jpg" fit "contain"
        text "To Elevator" xalign 0.5 yalign 0.8 size 24
    text "Apartment Basement" xalign 0.5 yalign 0.1 size 50

# ==========================================================
# APARTMENT BOILER ROOM SCREEN
# ==========================================================
screen apartment_boiler_room_screen():
    modal True
    zorder 100
    add "bg apartment_boiler_room"
    # Button back to basement (Center)
    button:
        xysize (120, 120)
        xpos 800
        ypos 500
        action [Hide("apartment_boiler_room_screen"), Show("apartment_basement_screen")]
        add "gui/blacksqaure_Button_Map.jpg" fit "contain"
        text "To Basement" xalign 0.5 yalign 0.8 size 24
    text "Apartment Boiler Room" xalign 0.5 yalign 0.1 size 50

# ==========================================================
# APARTMENT LANDLORD OFFICE SCREEN
# ==========================================================
screen apartment_landlord_office_screen():
    modal True
    zorder 100
    add "bg apartment_landlord_office"
    # Back to hallway button (Top Left)
    button:
        xysize (100, 100)
        xpos 50
        ypos 50
        action [Hide("apartment_landlord_office_screen"), Show("apartment_lobby_screen")]
        add "gui/blacksqaure_Button_Map.jpg" fit "contain"
        text "To Lobby" xalign 0.5 yalign 0.8 size 24
    text "Landlord Office" xalign 0.5 yalign 0.1 size 50

# ==========================================================
# MC'S APARTMENT SCREENS
# ==========================================================
screen apartment_mc_apartment_screen():
    modal True
    zorder 100
    add "bg apartment_mc_apartment"
    # Button to MC's Bedroom (Left)
    button:
        xysize (120, 120)
        xpos 400
        ypos 500
        action [Hide("apartment_mc_apartment_screen"), Show("apartment_mc_bedroom_screen")]
        add "gui/blacksqaure_Button_Map.jpg" fit "contain"
        text "To Bedroom" xalign 0.5 yalign 0.8 size 24
    # Button to MC's Bathroom (Center)
    button:
        xysize (120, 120)
        xpos 800
        ypos 500
        action [Hide("apartment_mc_apartment_screen"), Show("apartment_mc_bathroom_screen")]
        add "gui/blacksqaure_Button_Map.jpg" fit "contain"
        text "To Bathroom" xalign 0.5 yalign 0.8 size 24
    # Button to MC's Kitchen (Right)
    button:
        xysize (120, 120)
        xpos 1200
        ypos 500
        action [Hide("apartment_mc_apartment_screen"), Show("apartment_mc_kitchen_screen")]
        add "gui/blacksqaure_Button_Map.jpg" fit "contain"
        text "To Kitchen" xalign 0.5 yalign 0.8 size 24
    # Back to hallway button (Top Left)
    button:
        xysize (100, 100)
        xpos 50
        ypos 50
        action [Hide("apartment_mc_apartment_screen"), Show("apartment_hallway_screen")]
        add "gui/blacksqaure_Button_Map.jpg" fit "contain"
        text "To Hallway" xalign 0.5 yalign 0.8 size 24
    text "MC's Apartment" xalign 0.5 yalign 0.1 size 50

screen apartment_mc_bedroom_screen():
    modal True
    zorder 100
    add "bg apartment_mc_bedroom"
    # Back to MC's apartment button (Top Left)
    button:
        xysize (100, 100)
        xpos 50
        ypos 50
        action [Hide("apartment_mc_bedroom_screen"), Show("apartment_mc_apartment_screen")]
        add "gui/blacksqaure_Button_Map.jpg" fit "contain"
        text "To MC's Apartment" xalign 0.5 yalign 0.8 size 24
    text "MC's Bedroom" xalign 0.5 yalign 0.1 size 50

screen apartment_mc_kitchen_screen():
    modal True
    zorder 100
    add "bg apartment_mc_kitchen"
    # Back to MC's apartment button (Top Left)
    button:
        xysize (100, 100)
        xpos 50
        ypos 50
        action [Hide("apartment_mc_kitchen_screen"), Show("apartment_mc_apartment_screen")]
        add "gui/blacksqaure_Button_Map.jpg" fit "contain"
        text "To MC's Apartment" xalign 0.5 yalign 0.8 size 24
    text "MC's Kitchen" xalign 0.5 yalign 0.1 size 50

screen apartment_mc_bathroom_screen():
    modal True
    zorder 100
    add "bg apartment_mc_bathroom"
    # Back to MC's apartment button (Top Left)
    button:
        xysize (100, 100)
        xpos 50
        ypos 50
        action [Hide("apartment_mc_bathroom_screen"), Show("apartment_mc_apartment_screen")]
        add "gui/blacksqaure_Button_Map.jpg" fit "contain"
        text "To MC's Apartment" xalign 0.5 yalign 0.8 size 24
    text "MC's Bathroom" xalign 0.5 yalign 0.1 size 50

# ==========================================================
# AMBER'S APARTMENT SCREENS
# ==========================================================
screen apartment_amber_apartment_screen():
    modal True
    zorder 100
    add "bg apartment_amber_apartment"
    # Button to Amber's Bedroom (Left)
    button:
        xysize (120, 120)
        xpos 400
        ypos 500
        action [Hide("apartment_amber_apartment_screen"), Show("apartment_amber_bedroom_screen")]
        add "gui/blacksqaure_Button_Map.jpg" fit "contain"
        text "To Bedroom" xalign 0.5 yalign 0.8 size 24
    # Button to Amber's Bathroom (Center)
    button:
        xysize (120, 120)
        xpos 800
        ypos 500
        action [Hide("apartment_amber_apartment_screen"), Show("apartment_amber_bathroom_screen")]
        add "gui/blacksqaure_Button_Map.jpg" fit "contain"
        text "To Bathroom" xalign 0.5 yalign 0.8 size 24
    # Button to Amber's Kitchen (Right)
    button:
        xysize (120, 120)
        xpos 1200
        ypos 500
        action [Hide("apartment_amber_apartment_screen"), Show("apartment_amber_kitchen_screen")]
        add "gui/blacksqaure_Button_Map.jpg" fit "contain"
        text "To Kitchen" xalign 0.5 yalign 0.8 size 24
    # Back to hallway button (Top Left)
    button:
        xysize (100, 100)
        xpos 50
        ypos 50
        action [Hide("apartment_amber_apartment_screen"), Show("apartment_hallway_screen")]
        add "gui/blacksqaure_Button_Map.jpg" fit "contain"
        text "To Hallway" xalign 0.5 yalign 0.8 size 24
    text "Amber's Apartment" xalign 0.5 yalign 0.1 size 50

screen apartment_amber_bedroom_screen():
    modal True
    zorder 100
    add "bg apartment_amber_bedroom"
    # Back to Amber's apartment button (Top Left)
    button:
        xysize (100, 100)
        xpos 50
        ypos 50
        action [Hide("apartment_amber_bedroom_screen"), Show("apartment_amber_apartment_screen")]
        add "gui/blacksqaure_Button_Map.jpg" fit "contain"
        text "To Amber's Apartment" xalign 0.5 yalign 0.8 size 24
    text "Amber's Bedroom" xalign 0.5 yalign 0.1 size 50

screen apartment_amber_kitchen_screen():
    modal True
    zorder 100
    add "bg apartment_amber_kitchen"
    # Back to Amber's apartment button (Top Left)
    button:
        xysize (100, 100)
        xpos 50
        ypos 50
        action [Hide("apartment_amber_kitchen_screen"), Show("apartment_amber_apartment_screen")]
        add "gui/blacksqaure_Button_Map.jpg" fit "contain"
        text "To Amber's Apartment" xalign 0.5 yalign 0.8 size 24
    text "Amber's Kitchen" xalign 0.5 yalign 0.1 size 50

screen apartment_amber_bathroom_screen():
    modal True
    zorder 100
    add "bg apartment_amber_bathroom"
    # Back to Amber's apartment button (Top Left)
    button:
        xysize (100, 100)
        xpos 50
        ypos 50
        action [Hide("apartment_amber_bathroom_screen"), Show("apartment_amber_apartment_screen")]
        add "gui/blacksqaure_Button_Map.jpg" fit "contain"
        text "To Amber's Apartment" xalign 0.5 yalign 0.8 size 24
    text "Amber's Bathroom" xalign 0.5 yalign 0.1 size 50

# ==========================================================
# RAZOR'S APARTMENT SCREEN
# ==========================================================
screen apartment_razor_apartment_screen():
    modal True
    zorder 100
    add "bg apartment_razor_apartment"
    # Back to hallway button (Top Left)
    button:
        xysize (100, 100)
        xpos 50
        ypos 50
        action [Hide("apartment_razor_apartment_screen"), Show("apartment_hallway_screen")]
        add "gui/blacksqaure_Button_Map.jpg" fit "contain"
        text "To Hallway" xalign 0.5 yalign 0.8 size 24
    text "Razor's Apartment" xalign 0.5 yalign 0.1 size 50
