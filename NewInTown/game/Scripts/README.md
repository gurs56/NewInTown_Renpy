# NewInTown — Script Guide

How the game's code is organized and how to add things without
breaking other things. Written for the whole team — no Ren'Py
experience assumed beyond the basics.

## Folder map

| Folder | What lives there |
|---|---|
| `System/` | Engine-y stuff: game loop (`GameState.rpy`), time system (`TimeTracker.rpy`), HUD + reusable buttons (`GameButtons.rpy`), Ren'Py defaults (`options.rpy`, `gui.rpy`, `screens.rpy`) |
| `StoryLine/` | Quest flags (`StoryFlags.rpy`) and the acts (`Act_1/A00.rpy` …) |
| `Characters/` | One file per character: their `Character()`, mood images, presence flags, and `talk_*` menu |
| `Locations/` | Location screens (`MidTownLocations.rpy`) and who stands where (`CharacterLocation.rpy`) |
| `Maps/` | World / mid-town map screens and the Map button's helper |
| `Backgrounds/` | All `image bg …` declarations |
| `Phone/` | The phone: home screen + app list (`PhoneApp.rpy`), texting UI (`PhoneTexting.rpy`) |
| `Posters/` | The `Poster()` helper for one-shot story paintings |

## Ground rules (these prevent whole categories of bugs)

1. **Never write a bare `"""string"""` inside a `label`** — in Ren'Py that
   is dialogue and shows on screen. Use `#` comments.
2. **Every flag gets a `default`** in `StoryFlags.rpy` (or the character's
   file if it's per-character). One name per quest step.
3. **Never let a label branch dead-end** — always finish with
   `jump`/`return`, or Ren'Py falls through into the next label.
4. **Story scenes start with `$ in_story_scene = True`** and end with the
   3-line pattern: `$ in_story_scene = False` → `show screen <location>` →
   `jump exploration_loop`.
5. **Sub-labels inside acts are LOCAL** (`label .merge:` / `jump .merge`) so
   act files can never collide with each other.
6. **Asset filenames**: no spaces, no typos — they're referenced as strings.

## How to add …

**…a location:** define its bg in `Backgrounds/Backgrounds.rpy`, copy any
small screen in `MidTownLocations.rpy` (keep `tag location` / `modal True` /
`zorder 100`), then add `use nav_button("To X", "x_screen", x, y)` lines
to/from its neighbours. `tag location` handles the hiding automatically.

**…a character:** copy a small file in `Characters/` (mood list + flags +
`talk_*` label), then one `use character_button(...)` line in
`CharacterLocation.rpy` for where they stand.

**…a quest scene:** write the label in the act file (start/end patterns
from rule 4), gate a menu option in the relevant `talk_*` label — or a
`use quest_button(...)` in a location screen — on your quest flag, and
chain the next act with `call setup_aXX_event`.

**…a phone app:** add one `("Name", Action)` line to `phone_apps` in
`Phone/PhoneApp.rpy`.

**…a poster (story painting):** use
`scene expression Poster("A0X - Name") with dissolve` and drop the art at
`images/Posters/A0X - Name.png` when it exists — a labeled placeholder
shows until then.

**…a character mood:** add one word to that character's mood list.

## Names that matter

- `mc_name` (Characters/MC.rpy) — the player-chosen name; the phone and
  all dialogue read it. Never hardcode the MC's name.
- Poster names are canonical: script string == art filename, forever.
- The father is **Aaron Vale** — story-critical, set in A00.
