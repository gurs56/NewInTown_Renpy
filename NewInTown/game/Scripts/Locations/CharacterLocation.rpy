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
        use character_button("Ms. Lopez", "talk_ms_lopez", ms_lopez_has_event, sprite="images/Test_Characters/body1_1.png")

# --- AMBER'S APARTMENT ---
screen character_buttons_amber_apartment():
    if amber_in_apartment:
        use character_button("Amber", "talk_amber", amber_has_event, sprite="images/Test_Characters/body1_2.png")

# --- GROCERY STORE ---
screen character_buttons_grocery():
    if mr_lee_in_store:
        use character_button("Mr. Lee", "talk_mr_lee", mr_lee_has_event, sprite="images/Test_Characters/body1_1.png")

# --- RAZOR'S APARTMENT ---
screen character_buttons_razor():
    if razor_in_apartment:
        use character_button("Razor", "talk_razor", (razor_has_event or quest_ask_razor_help), sprite="images/Test_Characters/body1_3.png")

# --- ALLEY (Uncle's pawn shop) ---
screen character_buttons_alley():
    if uncle_in_alley:
        use character_button("Uncle", "talk_uncle", uncle_has_event, sprite="images/Test_Characters/body1_4.png")
