from BaseClasses import Region
from .types import ClickMageLocation
from .locations import location_table
from typing import TYPE_CHECKING
from . import options

if TYPE_CHECKING:
    from . import ClickMageWorld

def create_regions(world: "ClickMageWorld"):
    menu = create_region(world, "Menu")

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
