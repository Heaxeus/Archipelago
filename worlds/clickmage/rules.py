from worlds.generic.Rules import add_rule 
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import ClickMageWorld

def set_rules(world: "ClickMageWorld"):
    player = world.player
    world.multiworld.completion_condition[player] = lambda state: state.has("Victory", player, 1)
    