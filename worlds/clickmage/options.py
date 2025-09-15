from typing import Any
from dataclasses import dataclass
from worlds.AutoWorld import PerGameCommonOptions
from Options import Choice, OptionGroup, Toggle, Range

def create_option_groups() -> list[OptionGroup]:
    option_group_list:list[OptionGroup] = []
    for name, options in click_mage_option_groups.items():
        option_group_list.append(OptionGroup(name=name, options=options))

    return option_group_list

@dataclass
class ClickMageOptions(PerGameCommonOptions):


click_mage_option_groups: dict[str, list[Any]] = {
    "General Options": [],
}
