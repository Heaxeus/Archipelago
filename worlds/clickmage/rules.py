from worlds.generic.Rules import add_rule
from . import options
from typing import TYPE_CHECKING
from .items import CLICKMAGE_LEVEL_ITEMS

if TYPE_CHECKING:
    from . import ClickMageWorld

def set_rules(world: "ClickMageWorld"):
    player = world.player
    