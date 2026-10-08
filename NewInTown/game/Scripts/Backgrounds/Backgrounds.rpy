

# ==========================================================
# BACKGROUND IMAGE DECLARATIONS
# ==========================================================

# --- APARTMENT BUILDING - COMMON AREAS ---
image bg apartment_building = im.Scale("images/Test_Backgrounds/Apartment_Building_BG.png", 1920, 1080)
image bg apartment_lobby = im.Scale("images/BackGrounds/Midtown/Apartment_Building/Lobby_Apartment/NAT_BG_01MID_APARTMENT_LOBBY_DAY_RN_v01.png", 1920, 1080)
image bg apartment_elevator = im.Scale("images/Test_Backgrounds/Apartment_Elevator_BG.png", 1920, 1080)
image bg apartment_hallway = im.Scale("images/Test_Backgrounds/Apartment_Hallway_BG.png", 1920, 1080)
image bg apartment_basement = im.Scale("images/BackGrounds/Midtown/Apartment_Building/Basement_Apartment/NAT_BG_01MID_APARTMENT_BASEMENT_LN_v01.png", 1920, 1080)
image bg apartment_boiler_room = im.Scale("images/BackGrounds/Midtown/Apartment_Building/Basement_Apartment/NAT_BG_01MID_APARTMENT_BOILERROOM_LN_v01.png", 1920, 1080)
image bg apartment_landlord_office = im.Scale("images/BackGrounds/Midtown/Apartment_Building/Lobby_Apartment/NAT_BG_01MID_APARTMENT_OFFICE_DAY_LN_v01.png", 1920, 1080)

# --- MC'S APARTMENT ---
image bg apartment_mc_apartment = im.Scale("images/BackGrounds/Midtown/Apartment_Building/MC_Apartment/NAT_BG_01MID_APARTMENT_MCLIVINGROOM_DAY_RN_v01.png", 1920, 1080)
image bg apartment_mc_bedroom = im.Scale("images/BackGrounds/Midtown/Apartment_Building/MC_Apartment/NAT_BG_01MID_APARTMENT_MCBEDROOM_DAY_RN_v01.png", 1920, 1080)
image bg apartment_mc_kitchen = im.Scale("images/BackGrounds/Midtown/Apartment_Building/MC_Apartment/NAT_BG_01MID_APARTMENT_MCKITCHEN_DAY_FIN_v01.png", 1920, 1080)
image bg apartment_mc_bathroom = im.Scale("images/BackGrounds/Midtown/Apartment_Building/MC_Apartment/NAT_BG_01MID_APARTMENT_MCBATHROOM_DAY_FIN_v01.png", 1920, 1080)

# --- AMBER'S APARTMENT ---
# living room art is still sketch-stage (SK) - swap when a lineart/final pass lands
image bg apartment_amber_apartment = im.Scale("images/BackGrounds/Midtown/Apartment_Building/Amber_Apartment/NAT_BG_01MID_APARTMENT_AMBERLIVINGROOM_DAY_SK_v01.jpg", 1920, 1080)
image bg apartment_amber_bedroom = im.Scale("images/BackGrounds/Midtown/Apartment_Building/Amber_Apartment/NAT_BG_01MID_APARTMENT_AMBERBEDROOM_DAY_LN_v01.png", 1920, 1080)
image bg apartment_amber_kitchen = im.Scale("images/BackGrounds/Midtown/Apartment_Building/Amber_Apartment/NAT_BG_01MID_APARTMENT_AMBERKITCHEN_DAY_LN_v01.png", 1920, 1080)
image bg apartment_amber_bathroom = im.Scale("images/BackGrounds/Midtown/Apartment_Building/Amber_Apartment/NAT_BG_01MID_APARTMENT_AMBERBATHROOM_DAY_FIN_v01.png", 1920, 1080)

# --- RAZOR'S APARTMENT ---
image bg apartment_razor_apartment = im.Scale("images/Test_Backgrounds/Apartment_Razor_Apartment_BG.png", 1920, 1080)

# --- ALLEYWAY BEHIND APARTMENT ---
image bg apartment_alley = im.Scale("images/Test_Backgrounds/alley.png", 1920, 1080)

# --- Mr.Lee's Grocery Store  ---
image bg grocery_store = im.Scale("images/Test_Backgrounds/exterior.png", 1920, 1080)
image bg grocery_store_interior = im.Scale("images/Test_Backgrounds/Interior2.png", 1920, 1080)

# --- CAFE ---
image bg cafe_building = im.Scale("images/BackGrounds/Midtown/Corner_Cafe/NAT_BG_03WEST_CAFE_EXTERIOR_DAY_LN_v01.png", 1920, 1080)
image bg cafe_interior = im.Scale("images/BackGrounds/Midtown/Corner_Cafe/NAT_BG_03WEST_CAFE_INTERIOR_DAY_LN_v01.png", 1920, 1080)
image bg cafe_kitchen = im.Scale("images/Test_Backgrounds/Kitchen.png", 1920, 1080)
image bg cafe_storage = im.Scale("images/BackGrounds/Midtown/Corner_Cafe/NAT_BG_03WEST_CAFE_BACKROOM_LN_v01.png", 1920, 1080)

# --- BOXING GYM (no art yet) ---
# Uses the Poster placeholder card until art exists. Drop the real
# art at images/Posters/BG - Boxing_Gym.png (it swaps in automatically),
# or replace this line with an im.Scale(...) like the ones above.
image bg boxing_gym = Poster("BG - Boxing_Gym")