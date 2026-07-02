# ==========================================================
# MID TOWN LOCATIONS
# ==========================================================
# All the location screens for Mid Town (apartments, shops, etc).
#
# HOW LOCATION SCREENS WORK
#   Every screen here starts with the same 3 lines:
#     tag location   -> only one location shows at a time; Show()-ing
#                       a new one auto-hides the current one
#     modal True     -> clicks can't fall through to whatever is below
#     zorder 100     -> draws above story sprites, below the HUD (1000)
#
# HOW TO ADD A NEW LOCATION
#   1. Define its background in Backgrounds/Backgrounds.rpy
#   2. Copy any small screen below, rename it, swap the bg
#   3. Add nav_button lines to/from its neighbours - done.
#
# The reusable buttons (nav_button, quest_button, character_button)
# live in System/GameButtons.rpy.
# ==========================================================

# ==========================================================
# APARTMENT BUILDING
# ==========================================================
screen apartment_building_screen():
    tag location
    modal True
    zorder 100
    add "bg apartment_building"
    use nav_button("To Mid Town Map", "mid_town_map_screen", 50, 50, 100)
    use nav_button("To Lobby", "apartment_lobby_screen", 885, 465, 150, 28)
    use nav_button("To Alley", "apartment_alley_screen", 1400, 500)
    text "Apartment Building" xalign 0.5 yalign 0.1 size 50

# ==========================================================
# APARTMENT LOBBY
# ==========================================================
screen apartment_lobby_screen():
    tag location
    modal True
    zorder 100
    add "bg apartment_lobby"
    use character_buttons_lobby
    use nav_button("To Building Entrance", "apartment_building_screen", 50, 50, 100)
    use nav_button("To Elevator", "apartment_elevator_screen", 800, 500, 120, 28)
    use nav_button("To Ms. Lopez Office", "apartment_landlord_office_screen", 1050, 500, 120, 28)
    text "Apartment Lobby" xalign 0.5 yalign 0.1 size 50

# ==========================================================
# APARTMENT ELEVATOR
# ==========================================================
screen apartment_elevator_screen():
    tag location
    modal True
    zorder 100
    add "bg apartment_elevator"
    use nav_button("To Basement", "apartment_basement_screen", 300, 500)
    use nav_button("To Hallway", "apartment_hallway_screen", 800, 500)
    use nav_button("To Lobby", "apartment_lobby_screen", 1300, 500)
    text "Apartment Elevator" xalign 0.5 yalign 0.1 size 50

# ==========================================================
# APARTMENT HALLWAY (3rd floor)
# ==========================================================
screen apartment_hallway_screen():
    tag location
    modal True
    zorder 100
    add "bg apartment_hallway"
    use nav_button("To Razor's Apartment", "apartment_razor_apartment_screen", 200, 500)
    use nav_button("To MC's Apartment", "apartment_mc_apartment_screen", 600, 500)
    use nav_button("To Amber's Apartment", "apartment_amber_apartment_screen", 1000, 500)
    use nav_button("To Elevator", "apartment_elevator_screen", 1400, 500)
    # A05 quest trigger: Ms. Lopez's surprise (the new apartment)
    if quest_follow_lopez_apartment:
        use quest_button("Meet Ms. Lopez", "A05_02_NEW_APARTMENT", 800, 300)
    text "Apartment Hallway" xalign 0.5 yalign 0.1 size 50

# ==========================================================
# APARTMENT BASEMENT
# ==========================================================
screen apartment_basement_screen():
    tag location
    modal True
    zorder 100
    add "bg apartment_basement"
    use nav_button("To Boiler Room", "apartment_boiler_room_screen", 300, 500)
    use nav_button("To Elevator", "apartment_elevator_screen", 1300, 500)
    # A04 quest triggers (they never overlap - the flags swap over)
    if quest_check_leak:
        use quest_button("Check the leak", "A04_02_CHECK_LEAK", 700, 300)
    if quest_fix_with_razor:
        use quest_button("Fix pipe with Razor", "A04_05_FIX_LEAK", 700, 300)
    text "Apartment Basement" xalign 0.5 yalign 0.1 size 50

# ==========================================================
# BOILER ROOM
# ==========================================================
screen apartment_boiler_room_screen():
    tag location
    modal True
    zorder 100
    add "bg apartment_boiler_room"
    use nav_button("To Basement", "apartment_basement_screen", 800, 500)
    text "Apartment Boiler Room" xalign 0.5 yalign 0.1 size 50

# ==========================================================
# LANDLORD OFFICE
# ==========================================================
screen apartment_landlord_office_screen():
    tag location
    modal True
    zorder 100
    add "bg apartment_landlord_office"
    use nav_button("To Lobby", "apartment_lobby_screen", 50, 50, 100)
    text "Landlord Office" xalign 0.5 yalign 0.1 size 50

# ==========================================================
# MC'S APARTMENT
# ==========================================================
screen apartment_mc_apartment_screen():
    tag location
    modal True
    zorder 100
    add "bg apartment_mc_apartment"
    use nav_button("To Hallway", "apartment_hallway_screen", 50, 50, 100)
    use nav_button("To Bedroom", "apartment_mc_bedroom_screen", 400, 500)
    use nav_button("To Bathroom", "apartment_mc_bathroom_screen", 800, 500)
    use nav_button("To Kitchen", "apartment_mc_kitchen_screen", 1200, 500)
    text "MC's Apartment" xalign 0.5 yalign 0.1 size 50

screen apartment_mc_bedroom_screen():
    tag location
    modal True
    zorder 100
    add "bg apartment_mc_bedroom"
    use nav_button("To MC's Apartment", "apartment_mc_apartment_screen", 50, 50, 100)
    # Sleep button - only shows at Night
    if time_of_day.is_night():
        button:
            xysize (200, 80)
            xalign 0.5
            ypos 500
            action [Hide("location"), Jump("go_to_sleep")]
            add "gui/square_button.jpg" fit "contain"
            text "Sleep" xalign 0.5 yalign 0.5 size 32
    text "MC's Bedroom" xalign 0.5 yalign 0.1 size 50

screen apartment_mc_kitchen_screen():
    tag location
    modal True
    zorder 100
    add "bg apartment_mc_kitchen"
    use nav_button("To MC's Apartment", "apartment_mc_apartment_screen", 50, 50, 100)
    text "MC's Kitchen" xalign 0.5 yalign 0.1 size 50

screen apartment_mc_bathroom_screen():
    tag location
    modal True
    zorder 100
    add "bg apartment_mc_bathroom"
    use nav_button("To MC's Apartment", "apartment_mc_apartment_screen", 50, 50, 100)
    text "MC's Bathroom" xalign 0.5 yalign 0.1 size 50

# ==========================================================
# AMBER'S APARTMENT
# ==========================================================
screen apartment_amber_apartment_screen():
    tag location
    modal True
    zorder 100
    add "bg apartment_amber_apartment"
    use character_buttons_amber_apartment
    use nav_button("To Hallway", "apartment_hallway_screen", 50, 50, 100)
    use nav_button("To Bedroom", "apartment_amber_bedroom_screen", 400, 500)
    use nav_button("To Bathroom", "apartment_amber_bathroom_screen", 800, 500)
    use nav_button("To Kitchen", "apartment_amber_kitchen_screen", 1200, 500)
    text "Amber's Apartment" xalign 0.5 yalign 0.1 size 50

screen apartment_amber_bedroom_screen():
    tag location
    modal True
    zorder 100
    add "bg apartment_amber_bedroom"
    use nav_button("To Amber's Apartment", "apartment_amber_apartment_screen", 50, 50, 100)
    text "Amber's Bedroom" xalign 0.5 yalign 0.1 size 50

screen apartment_amber_kitchen_screen():
    tag location
    modal True
    zorder 100
    add "bg apartment_amber_kitchen"
    use nav_button("To Amber's Apartment", "apartment_amber_apartment_screen", 50, 50, 100)
    text "Amber's Kitchen" xalign 0.5 yalign 0.1 size 50

screen apartment_amber_bathroom_screen():
    tag location
    modal True
    zorder 100
    add "bg apartment_amber_bathroom"
    use nav_button("To Amber's Apartment", "apartment_amber_apartment_screen", 50, 50, 100)
    text "Amber's Bathroom" xalign 0.5 yalign 0.1 size 50

# ==========================================================
# RAZOR'S APARTMENT
# ==========================================================
screen apartment_razor_apartment_screen():
    tag location
    modal True
    zorder 100
    add "bg apartment_razor_apartment"
    use character_buttons_razor
    use nav_button("To Hallway", "apartment_hallway_screen", 50, 50, 100)
    text "Razor's Apartment" xalign 0.5 yalign 0.1 size 50

# ==========================================================
# ALLEYWAY BEHIND APARTMENT
# ==========================================================
screen apartment_alley_screen():
    tag location
    modal True
    zorder 100
    add "bg apartment_alley"
    use character_buttons_alley
    use nav_button("To Building", "apartment_building_screen", 50, 50, 100)
    text "Alleyway" xalign 0.5 yalign 0.1 size 50

# ==========================================================
# CAFE
# ==========================================================
screen cafe_building_screen():
    tag location
    modal True
    zorder 100
    add "bg cafe_building"
    use nav_button("To Mid Town Map", "mid_town_map_screen", 50, 50, 100)
    use nav_button("Enter Cafe", "cafe_interior_screen", 800, 500)
    text "Cafe" xalign 0.5 yalign 0.1 size 50

screen cafe_interior_screen():
    tag location
    modal True
    zorder 100
    add "bg cafe_interior"
    use nav_button("To Cafe Entrance", "cafe_building_screen", 50, 50, 100)
    use nav_button("To Kitchen", "cafe_kitchen_screen", 800, 500)
    # A03 quest trigger: the 'Hiring' sign (only while job hunting)
    if quest_find_job and not job_bean_spill:
        use quest_button("'Hiring' sign", "A03_04_3_BEAN_SPILL_CAFE", 1200, 450)
    text "Cafe Interior" xalign 0.5 yalign 0.1 size 50

screen cafe_kitchen_screen():
    tag location
    modal True
    zorder 100
    add "bg cafe_kitchen"
    use nav_button("To Cafe Interior", "cafe_interior_screen", 50, 50, 100)
    use nav_button("To Storage", "cafe_storage_screen", 800, 500)
    text "Cafe Kitchen" xalign 0.5 yalign 0.1 size 50

screen cafe_storage_screen():
    tag location
    modal True
    zorder 100
    add "bg cafe_storage"
    use nav_button("To Kitchen", "cafe_kitchen_screen", 50, 50, 100)
    text "Cafe Storage" xalign 0.5 yalign 0.1 size 50

# ==========================================================
# GROCERY STORE (MR. LEE'S)
# ==========================================================
screen grocery_store_screen():
    tag location
    modal True
    zorder 100
    add "bg grocery_store"
    use nav_button("To Mid Town Map", "mid_town_map_screen", 50, 50, 100)
    use nav_button("Enter Store", "grocery_store_interior_screen", 800, 500)
    text "Mr. Lee's Grocery Store" xalign 0.5 yalign 0.1 size 50

screen grocery_store_interior_screen():
    tag location
    modal True
    zorder 100
    add "bg grocery_store_interior"
    use character_buttons_grocery
    use nav_button("Exit Store", "grocery_store_screen", 50, 50, 100)
    text "Mr. Lee's Store Interior" xalign 0.5 yalign 0.1 size 50
