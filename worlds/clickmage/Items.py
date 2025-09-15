from BaseClasses import Item, ItemClassification
from .types import ItemData, ClickMageItem
from . import options
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import ClickMageWorld

def create_itempool(world: "ClickMageWorld") -> list[Item]:
    itempool: list[Item] = []
    return itempool

def create_item(world: "ClickMageWorld", name: str) -> Item:
    data = item_table[name]
    return ClickMageItem(name, data.classification, data.ap_code, world.player)

def create_multiple_items(world: "ClickMageWorld", name: str, count: int,
                          item_type: ItemClassification = ItemClassification.progression) -> list[Item]:
    
    return [ClickMageItem(name, item_type, item_table[name].ap_code, world.player) for _ in range(count)]

item_table = {}
