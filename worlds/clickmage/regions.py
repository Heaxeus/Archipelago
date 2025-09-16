from BaseClasses import Region
from .types import ClickMageLocation
from .locations import location_table
from typing import TYPE_CHECKING
from .options import EnableBlueprintLocations, EnablePortalLocations, EnableUpgradeLocations

if TYPE_CHECKING:
    from . import ClickMageWorld

def create_regions(world: "ClickMageWorld"):
    menu = create_region(world, "Menu")

    if world.options.EnableBlueprintLocations == EnableBlueprintLocations.option_true:
        create_region_and_connect(world, "Portal Blueprint", "Island -> Portal Blueprint", menu)
        create_region_and_connect(world, "Water Well Blueprint", "Island -> Water Well Blueprint", menu)
        create_region_and_connect(world, "Smelter Blueprint", "Island -> Smelter Blueprint", menu)
        create_region_and_connect(world, "Charcoal Blueprint", "Island -> Charcoal Blueprint", menu)
        create_region_and_connect(world, "Saw Blueprint", "Island -> Saw Blueprint", menu)
        create_region_and_connect(world, "Storage Blueprint", "Island -> Storage Blueprint", menu)
        create_region_and_connect(world, "Forge Blueprint", "Island -> Forge Blueprint", menu)
        create_region_and_connect(world, "Phial Blueprint", "Island -> Phial Blueprint", menu)
        create_region_and_connect(world, "Steel Blueprint", "Island -> Steel Blueprint", menu)
        create_region_and_connect(world, "Copper Blueprint", "Island -> Copper Blueprint", menu)
        create_region_and_connect(world, "Alchemy Blueprint", "Island -> Alchemy Blueprint", menu)
        create_region_and_connect(world, "Catalyst Blueprint", "Island -> Catalyst Blueprint", menu)

    if world.options.EnableUpgradeLocations == EnableUpgradeLocations.option_true:
        click_hardness_1 = create_region_and_connect(world, "Click Hardness 1", "Island -> Click Hardness 1", menu)
        click_hardness_2 = create_region_and_connect(world, "Click Hardness 2", "Click Hardness 1 -> Click Hardness 2", click_hardness_1)
        click_hardness_3 = create_region_and_connect(world, "Click Hardness 3", "Click Hardness 2 -> Click Hardness 3", click_hardness_2)
        create_region_and_connect(world, "Click Hardness 4", "Click Hardness 3 -> Click Hardness 4", click_hardness_3)

        click_power_1 = create_region_and_connect(world, "Click Power 1", "Island -> Click Power 1", menu)
        click_power_2 = create_region_and_connect(world, "Click Power 2", "Click Power 1 -> Click Power 2", click_power_1)
        click_power_3 = create_region_and_connect(world, "Click Power 3", "Click Power 2 -> Click Power 3", click_power_2)
        click_power_4 = create_region_and_connect(world, "Click Power 4", "Click Power 3 -> Click Power 4", click_power_3)
        click_power_5 = create_region_and_connect(world, "Click Power 5", "Click Power 4 -> Click Power 5", click_power_4)
        click_power_6 = create_region_and_connect(world, "Click Power 6", "Click Power 5 -> Click Power 6", click_power_5)
        click_power_7 = create_region_and_connect(world, "Click Power 7", "Click Power 6 -> Click Power 7", click_power_6)
        click_power_8 = create_region_and_connect(world, "Click Power 8", "Click Power 7 -> Click Power 8", click_power_7)
        create_region_and_connect(world, "Click Power 9", "Click Power 8 -> Click Power 9", click_power_8)

        hand_size_1 = create_region_and_connect(world, "Hand Size 1", "Island -> Hand Size 1", menu)
        hand_size_2 = create_region_and_connect(world, "Hand Size 2", "Hand Size 1 -> Hand Size 2", hand_size_1)
        hand_size_3 = create_region_and_connect(world, "Hand Size 3", "Hand Size 2 -> Hand Size 3", hand_size_2)
        hand_size_4 = create_region_and_connect(world, "Hand Size 4", "Hand Size 3 -> Hand Size 4", hand_size_3)
        hand_size_5 = create_region_and_connect(world, "Hand Size 5", "Hand Size 4 -> Hand Size 5", hand_size_4)
        hand_size_6 = create_region_and_connect(world, "Hand Size 6", "Hand Size 5 -> Hand Size 6", hand_size_5)
        create_region_and_connect(world, "Hand Size 7", "Hand Size 6 -> Hand Size 7", hand_size_6)

        auto_click_1 = create_region_and_connect(world, "Auto Click 1", "Island -> Auto Click 1", menu)
        auto_click_2 = create_region_and_connect(world, "Auto Click 2", "Auto Click 1 -> Auto Click 2", auto_click_1)
        auto_click_3 = create_region_and_connect(world, "Auto Click 3", "Auto Click 2 -> Auto Click 3", auto_click_2)
        create_region_and_connect(world, "Auto Click 4", "Auto Click 3 -> Auto Click 4", auto_click_3)

        building_storage_1 = create_region_and_connect(world, "Building Storage 1", "Island -> Building Storage 1", menu)
        building_storage_2 = create_region_and_connect(world, "Building Storage 2", "Building Storage 1 -> Building Storage 2", building_storage_1)
        building_storage_3 = create_region_and_connect(world, "Building Storage 3", "Building Storage 2 -> Building Storage 3", building_storage_2)
        building_storage_4 = create_region_and_connect(world, "Building Storage 4", "Building Storage 3 -> Building Storage 4", building_storage_3)
        building_storage_5 = create_region_and_connect(world, "Building Storage 5", "Building Storage 4 -> Building Storage 5", building_storage_4)
        building_storage_6 = create_region_and_connect(world, "Building Storage 6", "Building Storage 5 -> Building Storage 6", building_storage_5)
        building_storage_7 = create_region_and_connect(world, "Building Storage 7", "Building Storage 6 -> Building Storage 7", building_storage_6)
        create_region_and_connect(world, "Building Storage 8", "Building Storage 7 -> Building Storage 8", building_storage_7)

        fuel_storage_1 = create_region_and_connect(world, "Fuel Storage 1", "Island -> Fuel Storage 1", menu)
        fuel_storage_2 = create_region_and_connect(world, "Fuel Storage 2", "Fuel Storage 1 -> Fuel Storage 2", fuel_storage_1)
        fuel_storage_3 = create_region_and_connect(world, "Fuel Storage 3", "Fuel Storage 2 -> Fuel Storage 3", fuel_storage_2)
        fuel_storage_4 = create_region_and_connect(world, "Fuel Storage 4", "Fuel Storage 3 -> Fuel Storage 4", fuel_storage_3)
        create_region_and_connect(world, "Fuel Storage 5", "Fuel Storage 4 -> Fuel Storage 5", fuel_storage_4)

        create_region_and_connect(world, "Move Fast", "Island -> Move Fast", menu)

        beach_upgrade_1 = create_region_and_connect(world, "Beach Upgrade 1", "Island -> Beach Upgrade 1", menu)
        create_region_and_connect(world, "Beach Upgrade 2", "Beach Upgrade 1 -> Beach Upgrade 2", beach_upgrade_1)
    
    if world.options.EnablePortalLocations == EnablePortalLocations.option_true:
        portal_scene_1 = create_region_and_connect(world, "Portal Stage 1", "Island -> Portal Stage 1", menu)
        portal_scene_2 = create_region_and_connect(world, "Portal Stage 2", "Portal Stage 1 -> Portal Stage 2", portal_scene_1)
        portal_scene_3 = create_region_and_connect(world, "Portal Stage 3", "Portal Stage 2 -> Portal Stage 3", portal_scene_2)
        portal_scene_4 = create_region_and_connect(world, "Portal Stage 4", "Portal Stage 3 -> Portal Stage 4", portal_scene_3)
        portal_scene_5 = create_region_and_connect(world, "Portal Stage 5", "Portal Stage 4 -> Portal Stage 5", portal_scene_4)
        portal_scene_6 = create_region_and_connect(world, "Portal Stage 6", "Portal Stage 5 -> Portal Stage 6", portal_scene_5)
        portal_scene_7 = create_region_and_connect(world, "Portal Stage 7", "Portal Stage 6 -> Portal Stage 7", portal_scene_6)
        portal_scene_8 = create_region_and_connect(world, "Portal Stage 8", "Portal Stage 7 -> Portal Stage 8", portal_scene_7)
        portal_scene_9 = create_region_and_connect(world, "Portal Stage 9", "Portal Stage 8 -> Portal Stage 9", portal_scene_8)
        portal_scene_10 = create_region_and_connect(world, "Portal Stage 10", "Portal Stage 9 -> Portal Stage 10", portal_scene_9)
        portal_scene_11 = create_region_and_connect(world, "Portal Stage 11", "Portal Stage 10 -> Portal Stage 11", portal_scene_10)
        portal_scene_12 = create_region_and_connect(world, "Portal Stage 12", "Portal Stage 11 -> Portal Stage 12", portal_scene_11)
        create_region_and_connect(world, "Portal Stage 13", "Portal Stage 12 -> Portal Stage 13", portal_scene_12)

def create_region(world: "ClickMageWorld", name: str) -> Region:
    reg = Region(name, world.player, world.multiworld)
    for (key, data) in location_table.items():
        if data.region == name:
            location = ClickMageLocation(world.player, key, data.ap_code, reg)
            reg.locations.append(location)
    
    world.multiworld.regions.append(reg)
    return reg

def create_region_and_connect(world: "ClickMageWorld",
                               name: str, entrancename: str, connected_region: Region) -> Region:
    reg: Region = create_region(world, name)
    connected_region.connect(reg, entrancename)
    return reg
