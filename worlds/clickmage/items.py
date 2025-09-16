from BaseClasses import Item, ItemClassification
from .types import ItemData, ClickMageItem
from .locations import get_total_locations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import ClickMageWorld

def create_itempool(world: "ClickMageWorld") -> list[Item]:
    itempool: list[Item] = []
    victory = create_item(world, "Victory")
    world.multiworld.get_location("Portal Stage 13", world.player).place_locked_item(victory)
    itempool += create_junk_items(world, get_total_locations(world) - len(itempool) - 1)
    return itempool

def create_item(world: "ClickMageWorld", name: str) -> Item:
    data = item_table[name]
    return ClickMageItem(name, data.classification, data.ap_code, world.player)

def create_multiple_items(world: "ClickMageWorld", name: str, count: int,
                          item_type: ItemClassification = ItemClassification.progression) -> list[Item]:
    
    return [ClickMageItem(name, item_type, item_table[name].ap_code, world.player) for _ in range(count)]


def create_junk_items(world: "ClickMageWorld", count: int) -> list[Item]:
    junk_pool: list[Item] = []
    junk_list: dict[str, int] = {}

    for name in item_table.keys():
        ic = item_table[name].classification
        if ic == ItemClassification.filler:
            junk_list[name] = junk_weights.get(name)

    for i in range(count):
        junk_pool.append(world.create_item(
            world.random.choices(list(junk_list.keys()), weights=list(junk_list.values()), k=1)[0]))

    return junk_pool

victory_item = {
    "Victory": ItemData(1000, ItemClassification.progression)
}

blueprint_items = {
    "Portal Blueprint": ItemData(101, ItemClassification.progression),
    "Water Well Blueprint": ItemData(102, ItemClassification.progression),
    "Smelter Blueprint": ItemData(103, ItemClassification.progression),
    "Charcoal Blueprint": ItemData(104, ItemClassification.progression),
    "Saw Blueprint": ItemData(105, ItemClassification.progression),
    "Storage Blueprint": ItemData(106, ItemClassification.progression),
    "Forge Blueprint": ItemData(107, ItemClassification.progression),
    "Phial Blueprint": ItemData(108, ItemClassification.progression),
    "Steel Processing Blueprint": ItemData(109, ItemClassification.progression),
    "Copper Processing Blueprint": ItemData(110, ItemClassification.progression),
    "Alchemy Table Blueprint": ItemData(111, ItemClassification.progression),
    "Catalyst Blueprint": ItemData(112, ItemClassification.progression)
}

upgrade_items = {
    "Progressive Click Hardness": ItemData(201, ItemClassification.progression),
    "Progressive Click Hardness": ItemData(202, ItemClassification.progression),
    "Progressive Click Hardness": ItemData(203, ItemClassification.progression),
    "Progressive Click Hardness": ItemData(204, ItemClassification.progression),
    "Progressive Click Power": ItemData(205, ItemClassification.useful),
    "Progressive Click Power": ItemData(206, ItemClassification.useful),
    "Progressive Click Power": ItemData(207, ItemClassification.useful),
    "Progressive Click Power": ItemData(208, ItemClassification.useful),
    "Progressive Click Power": ItemData(209, ItemClassification.useful),
    "Progressive Click Power": ItemData(210, ItemClassification.useful),
    "Progressive Click Power": ItemData(211, ItemClassification.useful),
    "Progressive Click Power": ItemData(212, ItemClassification.useful),
    "Progressive Click Power": ItemData(213, ItemClassification.useful),
    "Progressive Hand Size": ItemData(214, ItemClassification.useful),
    "Progressive Hand Size": ItemData(215, ItemClassification.useful),
    "Progressive Hand Size": ItemData(216, ItemClassification.useful),
    "Progressive Hand Size": ItemData(217, ItemClassification.useful),
    "Progressive Hand Size": ItemData(218, ItemClassification.useful),
    "Progressive Hand Size": ItemData(219, ItemClassification.useful),
    "Progressive Hand Size": ItemData(220, ItemClassification.useful),
    "Progressive Auto Click": ItemData(221, ItemClassification.useful),
    "Progressive Auto Click": ItemData(222, ItemClassification.useful),
    "Progressive Auto Click": ItemData(223, ItemClassification.useful),
    "Progressive Auto Click": ItemData(224, ItemClassification.useful),
    "Progressive Building Storage": ItemData(225, ItemClassification.progression),
    "Progressive Building Storage": ItemData(226, ItemClassification.progression),
    "Progressive Building Storage": ItemData(227, ItemClassification.progression),
    "Progressive Building Storage": ItemData(228, ItemClassification.progression),
    "Progressive Building Storage": ItemData(229, ItemClassification.progression),
    "Progressive Building Storage": ItemData(230, ItemClassification.progression),
    "Progressive Building Storage": ItemData(231, ItemClassification.progression),
    "Progressive Building Storage": ItemData(232, ItemClassification.progression),
    "Progressive Fuel Storage": ItemData(233, ItemClassification.useful),
    "Progressive Fuel Storage": ItemData(234, ItemClassification.useful),
    "Progressive Fuel Storage": ItemData(235, ItemClassification.useful),
    "Progressive Fuel Storage": ItemData(236, ItemClassification.useful),
    "Progressive Fuel Storage": ItemData(237, ItemClassification.useful),
    "Move Fast": ItemData(238, ItemClassification.useful),
    "Progressive Beach Upgrade": ItemData(239, ItemClassification.useful),
    "Progressive Beach Upgrade": ItemData(240, ItemClassification.useful)
}

junk_items = {
    "Literally Nothing": ItemData(301, ItemClassification.filler)
}

junk_weights = {
    "Literally Nothing": 40
}


item_table = {
    **victory_item,
    **blueprint_items,
    **upgrade_items,
    **junk_items
}
