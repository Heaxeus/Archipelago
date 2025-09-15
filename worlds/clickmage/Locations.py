# Look at init or Items.py for more information on imports
from typing import TYPE_CHECKING
import logging

from .Types import LocData

if TYPE_CHECKING:
    from . import ClickMageWorld

# This is used by ap and in Items.py
# There's a multitude of reasons to need to grab how many locations there are
def get_total_locations(world: "ClickMageWorld") -> int:
    # This is the total that we'll keep updating as we count how many locations there are
    return sum(1 for _ in location_table)

def get_location_names() -> dict[str, int]:
    # This is just a fancy way of getting all the names and data in the location table and making a dictionary that's {name, code}
    # If you have dynamic locations then you want to add them to the dictionary as well
    names = {name: data.ap_code for name, data in location_table.items()}

    return names

# You might need more functions as well so be liberal with them

# Heres where you do the next fun part of listing out all those locations
# I'm doing it programatically, but they can also be added to location_table manually
# It's important to note that locations MUST be bigger than progressive item count and should be greater or equal to the total item count

blueprint_locations = {
    "PortalBlueprint"
    "WaterWellBlueprint"
    "SmelterBlueprint"
    "CharcoalBlueprint"
    "SawBlueprint"
    "StorageBlueprint"
    "ForgeBlueprint"
    "PhialBlueprint"
    "SteelProcessingBlueprint"
    "CopperProcessingBlueprint"
    "AlchemyTableBlueprint"
    "CatalystBlueprint"
}

upgrade_locations = {
    "ClickHardness1"
    "ClickHardness2"
    "ClickHardness3"
    "ClickHardness4"
    "ClickPower1"
    "ClickPower2"
    "ClickPower3"
    "ClickPower4"
    "ClickPower5"
    "ClickPower6"
    "ClickPower7"
    "ClickPower8"
    "ClickPower9"
    "HandSize1"
    "HandSize2"
    "HandSize3"
    "HandSize4"
    "HandSize5"
    "HandSize6"
    "HandSize7"
    "AutoClick1"
    "AutoClick2"
    "AutoClick3"
    "AutoClick4"
    "BuildingStorage1"
    "BuildingStorage2"
    "BuildingStorage3"
    "BuildingStorage4"
    "BuildingStorage5"
    "BuildingStorage6"
    "BuildingStorage7"
    "BuildingStorage8"
    "FuelStorage1"
    "FuelStorage2"
    "FuelStorage3"
    "FuelStorage4"
}



location_table = {

    

}

