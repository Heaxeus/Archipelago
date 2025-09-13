from typing import List, Dict, Any
from dataclasses import dataclass
from worlds.AutoWorld import PerGameCommonOptions
from Options import Choice, OptionGroup, Toggle, Range

# If you've ever gone to an options page and seen how sometimes options are grouped
# This is that
def create_option_groups() -> List[OptionGroup]:
    option_group_list: List[OptionGroup] = []
    for name, options in click_mage_option_groups.items():
        option_group_list.append(OptionGroup(name=name, options=options))

    return option_group_list



@dataclass
class ClickMageOptions(PerGameCommonOptions):

    


# This is where you organize your options into groups
# It's entirely up to you how you want to organize it
click_mage_option_groups: dict[str, list[Any]] = {
    "General Options": [],
}
