from worlds.generic.Rules import add_rule
from . import Options
from typing import TYPE_CHECKING
from .Items import HEXCELLS_LEVEL_ITEMS

if TYPE_CHECKING:
    from . import ClickMageWorld

# This is where you add rules for items or locations
# These are omega simplified rules
# There are a ton of different ways you can add rules, from amoount of items you need, to optional items
# There's also difficulty options and a bunch of others that aren't in this implementation
# I'd suggest going through a bunch of different ap worlds and seeing how they do the rules
# Even better if its a game you know a lot about and can tell what you need to get to certain locations
def set_rules(world: "ClickMageWorld"):
    player = world.player
    