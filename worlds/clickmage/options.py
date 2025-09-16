from typing import Dict,List,Any
from dataclasses import dataclass
from worlds.AutoWorld import PerGameCommonOptions
from Options import Choice, OptionGroup, Toggle, Range

def create_option_groups() -> list[OptionGroup]:
    option_group_list:list[OptionGroup] = []
    for name, options in click_mage_option_groups.items():
        option_group_list.append(OptionGroup(name=name, options=options))

    return option_group_list

class EnableBlueprintLocations(Toggle):
    """
    Blueprints from the Trader will be locations for checks, and blueprints will need to be sent to you.
    """
    display_name = "Enable Blueprint Locations"
    option_true = 1
    option_false = 2
    default = 1


class EnablePortalLocations(Toggle):
    """
    Portal build stages will be locations for checks, and Portal build stages will need to be sent to you.
    """
    display_name = "Enable Portal Locations"
    option_true = 1
    option_false = 2
    default = 1


class EnableUpgradeLocations(Toggle):
    """
    Upgrades will be locations for checks, and upgrades will need to be sent to you.
    """
    display_name = "Enable Upgrade Locations"
    option_true = 1
    option_false = 2
    default = 1

class ImprovedStorage(Toggle):
    """
    Items mined from resource nodes are now automatically sent to storage.
    Storage needs to have at least 1 item in them to set where items should be sent.
    """
    display_name = "Improved Storage"
    option_true = 1
    option_false = 2
    default = 2

@dataclass
class ClickMageOptions(PerGameCommonOptions):
    ImprovedStorage: ImprovedStorage
    EnableBlueprintLocations: EnableBlueprintLocations
    EnablePortalLocations: EnablePortalLocations
    EnableUpgradeLocations: EnableUpgradeLocations

click_mage_option_groups: Dict[str, List[Any]] = {
    "General Options": [EnableBlueprintLocations, EnablePortalLocations, EnableUpgradeLocations],
    "Game Modifications": [ImprovedStorage]
}
