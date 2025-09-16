from BaseClasses import Item, Tutorial
from worlds.AutoWorld import World, WebWorld
from .locations import get_location_names, get_total_locations
from .items import create_item, create_itempool, item_table 
from .options import ClickMageOptions
from .regions import create_regions
from .rules import set_rules

class ClickMageWebWorld(WebWorld):
    theme = "partyTime"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Click Mage for Archipelago. "
        "This guide covers single-player, multiworld, and related software.",
        "English",
        "setup_en.md",
        "setup/en",
        ["ExpandedReality"]
    )]

class ClickMageWorld(World):
    """
    Click Mage is a clicker/resource game. No automation, just you and your island.\nMake a portal to escape!
    The Archipelago implementation adds the option to have some helpful automations!
    """
    game = "Click Mage"
    item_name_to_id = {name: data.ap_code for name, data in item_table.items()}
    location_name_to_id = get_location_names() 
    options_dataclass = ClickMageOptions
    options: ClickMageOptions
    web = ClickMageWebWorld()

    def generate_early(self):
        return

    def create_regions(self):
        create_regions(self)

    def set_rules(self):
        set_rules(self)

    def create_items(self):
        self.multiworld.itempool += create_itempool(self)

    def create_item(self, name: str) -> Item:
        return create_item(self, name)
    
    def fill_slot_data(self) -> dict[str, object]:
        slot_data: dict[str, object] = {
            "options": {
                  "EnableBlueprintLocations": self.options.EnableBlueprintLocations.value,
                  "EnablePortalLocations": self.options.EnablePortalLocations.value,
                  "EnableUpgradeLocations": self.options.EnableUpgradeLocations.value,
                  "ImprovedStorage": self.options.ImprovedStorage.value
            },
            "Seed": self.multiworld.seed_name,
            "Slot": self.player_name,
            "TotalLocations": get_total_locations(self)
        }

        return slot_data
