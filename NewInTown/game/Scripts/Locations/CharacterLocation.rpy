# ==========================================================
# CHARACTER PLACEMENT (who stands where)
# ==========================================================
# Each location's screen `use`s one of these. Each entry is ONE
# line thanks to the shared character_button screen (defined in
# System/GameButtons.rpy):
#
#   use character_button(name, talk_label, has_event, x, y, sprite)
#
# To put a character somewhere: add a line inside that location's
# screen below (gated on their presence flag). To make them appear
# or leave, flip their *_in_* flag from a story script.
# ==========================================================

# --- APARTMENT LOBBY ---
screen character_buttons_lobby():
    if ms_lopez_in_lobby:
        use character_button("Ms. Lopez", "talk_ms_lopez", ms_lopez_has_event, char="MsLopez", sprite="images/Characters/Ms.Lopez/NIT_CH_LOPEZ_DEFAULT_idle.png")

# --- AMBER'S APARTMENT ---
screen character_buttons_amber_apartment():
    if amber_in_apartment:
        use character_button("Amber", "talk_amber", amber_has_event, char="Amber", sprite="images/Characters/Amber/NIT_CH_AMBER_CLOTHED_IDLE_v01.png")

# --- GROCERY STORE ---
# (Mr. Lee has no art yet, so no `char=`.)
screen character_buttons_grocery():
    if mr_lee_in_store:
        use character_button("Mr. Lee", "talk_mr_lee", mr_lee_has_event, sprite="images/Test_Characters/body1_1.png")

# --- RAZOR'S APARTMENT ---
screen character_buttons_razor():
    if razor_in_apartment:
        use character_button("Razor", "talk_razor", (razor_has_event or quest_ask_razor_help), char="Razor", sprite="images/Characters/Razor/NIT_CH_RAZOR_CASUAL_STAND_IDLE_FIN_V01.png")

# --- ALLEY (Uncle's pawn shop) ---
screen character_buttons_alley():
    if uncle_in_alley:
        use character_button("Uncle", "talk_uncle", uncle_has_event, char="Uncle", sprite="images/Characters/Uncle/NIT_CH_UNCLE_CASUAL_STAND_IDLE_FIN_V01.png")
