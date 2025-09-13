from BaseClasses import Region
from .Types import ClickMageLocation
from .Locations import location_table
from typing import TYPE_CHECKING
from . import Options

if TYPE_CHECKING:
    from . import ClickMageWorld

# This is where you will create your imaginary game world
# IE: connect rooms and areas together
# This is NOT where you'll add requirements for how to get to certain locations thats in Rules.py
def create_regions(world: "ClickMageWorld"):
    # The functions that are being used here will be located at the bottom to view
    # The important part is that if its not a dead end and connects to another place then make it a variable
    # Otherwise you can just create the connection. Not that making it a variable is bad, it would just be unused

    # You can technically name your connections whatever you want as well
    # You'll use those connection names in Rules.py
    menu = create_region(world, "Menu")
    
   

def create_region(world: "ClickMageWorld", name: str) -> Region:
    reg = Region(name, world.player, world.multiworld)

    # When we create the region we go through all the locations we made and check if they are in that region
    # If they are and are valid, we attach it to the region
    for (key, data) in location_table.items():
        if data.region == name:
            location = ClickMageLocation(world.player, key, data.ap_code, reg)
            reg.locations.append(location)
    
    world.multiworld.regions.append(reg)
    return reg

# This runs the create region function while also connecting to another region
# Just simplifies process since you will be connecting a lot of regions
def create_region_and_connect(world: "ClickMageWorld",
                               name: str, entrancename: str, connected_region: Region) -> Region:
    reg: Region = create_region(world, name)
    connected_region.connect(reg, entrancename)
    return reg
