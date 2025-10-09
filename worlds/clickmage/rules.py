from worlds.generic.Rules import add_rule 
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import ClickMageWorld

def set_rules(world: "ClickMageWorld"):
    player = world.player
    world.multiworld.completion_condition[player] = lambda state: state.has("Victory", player, 1)

    iron_ingot = {"Progressive Click Hardness": 2,"Water Well Blueprint": 1, "Smelter Blueprint": 1}
    

    #BLUEPRINTS
    add_rule(world.multiworld.get_entrance("Island -> Portal Blueprint", player), lambda state: state.has("Progressive Click Hardness", player))
    add_rule(world.multiworld.get_entrance("Island -> Water Well Blueprint", player), lambda state: state.has("Progressive Click Hardness", player))
    add_rule(world.multiworld.get_entrance("Island -> Smelter Blueprint", player), lambda state: state.has_all(["Progressive Click Hardness", "Progressive Building Storage"], player))
    add_rule(world.multiworld.get_entrance("Island -> Charcoal Blueprint", player), lambda state: state.has("Progressive Click Hardness", player, 2))
    add_rule(world.multiworld.get_entrance("Island -> Saw Blueprint", player), lambda state: state.has_all_counts({"Progressive Click Hardness": 2,"Water Well Blueprint": 1, "Smelter Blueprint": 1, "Progressive Building Storage":2}, player))
    add_rule(world.multiworld.get_entrance("Island -> Storage Blueprint", player), lambda state: state.has_all_counts({"Progressive Click Hardness": 2,"Water Well Blueprint": 1, "Smelter Blueprint": 1}, player))
    add_rule(world.multiworld.get_entrance("Island -> Forge Blueprint", player), lambda state: state.has_all_counts({"Progressive Click Hardness":2, "Water Well Blueprint":1, "Smelter Blueprint":1, "Saw Blueprint":1, "Progressive Building Storage":3}, player))
    add_rule(world.multiworld.get_entrance("Island -> Phial Blueprint", player), lambda state: state.has_all_counts({"Forge Blueprint":1,"Progressive Click Hardness":2, "Water Well Blueprint":1, "Smelter Blueprint":1}, player))
    add_rule(world.multiworld.get_entrance("Island -> Steel Blueprint", player), lambda state: state.has_all_counts({"Phial Blueprint":1, "Saw Blueprint":1, "Charcoal Blueprint":1}, player))
    #add_rule(world.multiworld.get_entrance("Island -> Copper Blueprint", player), lambda state: state.has("Progressive Click Hardness", player))
    #add_rule(world.multiworld.get_entrance("Island -> Alchemy Blueprint", player), lambda state: state.has("Progressive Click Hardness", player))
    #add_rule(world.multiworld.get_entrance("Island -> Catalyst Blueprint", player), lambda state: state.has("Progressive Click Hardness", player))


    #CLICK HARDNESS
    add_rule(world.multiworld.get_entrance("Click Hardness 1 -> Click Hardness 2", player), lambda state: state.has_all(["Progressive Click Hardness","Water Well Blueprint", "Smelter Blueprint"], player))
    #add_rule(world.multiworld.get_entrance("Click Hardness 2 -> Click Hardness 3", player), lambda state: state.has("Progressive Click Hardness", player))
    #add_rule(world.multiworld.get_entrance("Click Hardness 3 -> Click Hardness 4", player), lambda state: state.has("Progressive Click Hardness", player))

    #CLICK POWER
    add_rule(world.multiworld.get_entrance("Click Power 1 -> Click Power 2", player), lambda state: state.has("Smelter Blueprint", player))
    #add_rule(world.multiworld.get_entrance("Click Power 2 -> Click Power 3", player), lambda state: state.has("Progressive Click Hardness", player))
    #add_rule(world.multiworld.get_entrance("Click Power 3 -> Click Power 4", player), lambda state: state.has("Progressive Click Hardness", player))
    #add_rule(world.multiworld.get_entrance("Click Power 4 -> Click Power 5", player), lambda state: state.has("Progressive Click Hardness", player))
    #add_rule(world.multiworld.get_entrance("Click Power 5 -> Click Power 6", player), lambda state: state.has("Progressive Click Hardness", player))
    #add_rule(world.multiworld.get_entrance("Click Power 6 -> Click Power 7", player), lambda state: state.has("Progressive Click Hardness", player))
    #add_rule(world.multiworld.get_entrance("Click Power 7 -> Click Power 8", player), lambda state: state.has("Progressive Click Hardness", player))
    #add_rule(world.multiworld.get_entrance("Click Power 8 -> Click Power 9", player), lambda state: state.has("Progressive Click Hardness", player))

    #HAND SIZE
    add_rule(world.multiworld.get_entrance("Hand Size 1 -> Hand Size 2", player), lambda state: state.has("Progressive Click Hardness", player))
    add_rule(world.multiworld.get_entrance("Hand Size 2 -> Hand Size 3", player), lambda state: state.has_all(["Progressive Click Hardness", "Water Well Blueprint", "Smelter Blueprint"], player))
    add_rule(world.multiworld.get_entrance("Hand Size 3 -> Hand Size 4", player), lambda state: state.has_all_counts({"Progressive Click Hardness": 2,"Water Well Blueprint": 1, "Smelter Blueprint": 1}, player))
    #add_rule(world.multiworld.get_entrance("Hand Size 4 -> Hand Size 5", player), lambda state: state.has("Progressive Click Hardness", player))
    #add_rule(world.multiworld.get_entrance("Hand Size 5 -> Hand Size 6", player), lambda state: state.has("Progressive Click Hardness", player))

    #AUTO CLICK
    add_rule(world.multiworld.get_entrance("Island -> Auto Click 1", player), lambda state: state.has_all(["Water Well Blueprint", "Smelter Blueprint"], player))
    #add_rule(world.multiworld.get_entrance("Auto Click 1 -> Auto Click 2", player), lambda state: state.has("Progressive Click Hardness", player))
    #add_rule(world.multiworld.get_entrance("Auto Click 2 -> Auto Click 3", player), lambda state: state.has("Progressive Click Hardness", player))
    #add_rule(world.multiworld.get_entrance("Auto Click 3 -> Auto Click 4", player), lambda state: state.has("Progressive Click Hardness", player))

    #BUILDING STORAGE
    add_rule(world.multiworld.get_entrance("Island -> Building Storage 1", player), lambda state: state.has("Progressive Click Hardness", player))
    add_rule(world.multiworld.get_entrance("Building Storage 1 -> Building Storage 2", player), lambda state: state.has("Water Well Blueprint", player))
    add_rule(world.multiworld.get_entrance("Building Storage 2 -> Building Storage 3", player), lambda state: state.has("Smelter Blueprint", player))
    add_rule(world.multiworld.get_entrance("Building Storage 3 -> Building Storage 4", player), lambda state: state.has_all_count({"Progressive Click Hardness": 2,"Water Well Blueprint": 1, "Smelter Blueprint": 1, "Saw Blueprint":1}, player))
    #add_rule(world.multiworld.get_entrance("Building Storage 4 -> Building Storage 5", player), lambda state: state.has("Progressive Click Hardness", player))
    #add_rule(world.multiworld.get_entrance("Building Storage 5 -> Building Storage 6", player), lambda state: state.has("Progressive Click Hardness", player))
    #add_rule(world.multiworld.get_entrance("Building Storage 6 -> Building Storage 7", player), lambda state: state.has("Progressive Click Hardness", player))
    #add_rule(world.multiworld.get_entrance("Building Storage 7 -> Building Storage 8", player), lambda state: state.has("Progressive Click Hardness", player))

    #FUEL STORAGE
    add_rule(world.multiworld.get_entrance("Island -> Fuel Storage 1", player), lambda state: state.has("Progressive Click Hardness", player))
    add_rule(world.multiworld.get_entrance("Fuel Storage 1 -> Fuel Storage 2", player), lambda state: state.has("Smelter Blueprint", player))
    add_rule(world.multiworld.get_entrance("Fuel Storage 2 -> Fuel Storage 3", player), lambda state: state.has_all_counts({"Progressive Click Hardness": 2,"Water Well Blueprint": 1, "Smelter Blueprint": 1}, player))
    #add_rule(world.multiworld.get_entrance("Fuel Storage 3 -> Fuel Storage 4", player), lambda state: state.has("Progressive Click Hardness", player))
    #add_rule(world.multiworld.get_entrance("Fuel Storage 4 -> Fuel Storage 5", player), lambda state: state.has("Progressive Click Hardness", player))
    
    #MOVE FAST
    add_rule(world.multiworld.get_entrance("Island -> Move Fast", player), lambda state: state.has_all_counts({"Progressive Click Hardness": 2,"Water Well Blueprint": 1, "Smelter Blueprint": 1}, player))

    #BEACH UPGRADE
    add_rule(world.multiworld.get_entrance("Island -> Beach Upgrade 1", player), lambda state: state.has("Water Well Blueprint", player))
    add_rule(world.multiworld.get_entrance("Beach Upgrade 1 -> Beach Upgrade 2", player), lambda state: state.has_all_counts({"Progressive Click Hardness": 2,"Water Well Blueprint": 1, "Smelter Blueprint": 1, "Saw Blueprint":1, "Charcoal Blueprint":1}, player))



    #PORTAL BUILD
    add_rule(world.multiworld.get_entrance("Island -> Portal Stage 1", player), lambda state: state.has_all(["Water Well Blueprint","Saw Blueprint"], player))
    add_rule(world.multiworld.get_entrance("Portal Stage 1 -> Portal Stage 2", player), lambda state: state.has_all_counts({"Water Well Blueprint":1,"Saw Blueprint":1, "Forge Blueprint":1, "Steel Blueprint":1}, player))
    #add_rule(world.multiworld.get_entrance("Portal Stage 2 -> Portal Stage 3", player), lambda state: state.has("Progressive Click Hardness", player))
    #add_rule(world.multiworld.get_entrance("Portal Stage 3 -> Portal Stage 4", player), lambda state: state.has("Progressive Click Hardness", player))
    #add_rule(world.multiworld.get_entrance("Portal Stage 4 -> Portal Stage 5", player), lambda state: state.has("Progressive Click Hardness", player))
    #add_rule(world.multiworld.get_entrance("Portal Stage 5 -> Portal Stage 6", player), lambda state: state.has("Progressive Click Hardness", player))
    #add_rule(world.multiworld.get_entrance("Portal Stage 6 -> Portal Stage 7", player), lambda state: state.has("Progressive Click Hardness", player))
    #add_rule(world.multiworld.get_entrance("Portal Stage 7 -> Portal Stage 8", player), lambda state: state.has("Progressive Click Hardness", player))
    #add_rule(world.multiworld.get_entrance("Portal Stage 8 -> Portal Stage 9", player), lambda state: state.has("Progressive Click Hardness", player))
    #add_rule(world.multiworld.get_entrance("Portal Stage 9 -> Portal Stage 10", player), lambda state: state.has("Progressive Click Hardness", player))
    #add_rule(world.multiworld.get_entrance("Portal Stage 10 -> Portal Stage 11", player), lambda state: state.has("Progressive Click Hardness", player))
    #add_rule(world.multiworld.get_entrance("Portal Stage 11 -> Portal Stage 12", player), lambda state: state.has("Progressive Click Hardness", player))
    #add_rule(world.multiworld.get_entrance("Portal Stage 12 -> Portal Stage 13", player), lambda state: state.has("Progressive Click Hardness", player))