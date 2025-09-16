from typing import TYPE_CHECKING

from .types import LocData

if TYPE_CHECKING:
    from . import ClickMageWorld

def get_total_locations(world: "ClickMageWorld") -> int:
    return sum(1 for _ in location_table)

def get_location_names() -> dict[str, int]:
    names = {name: data.ap_code for name, data in location_table.items()}

    return names

blueprint_locations = {
    "Portal Blueprint": LocData(101, "Trader"),
    "Water Well Blueprint": LocData(102, "Trader"),
    "Smelter Blueprint": LocData(103, "Trader"),
    "Charcoal Blueprint": LocData(104, "Trader"),
    "Saw Blueprint": LocData(105, "Trader"),
    "Storage Blueprint": LocData(106, "Trader"),
    "Forge Blueprint": LocData(107, "Trader"),
    "Phial Blueprint": LocData(108, "Trader"),
    "Steel Processing Blueprint": LocData(109, "Trader"),
    "Copper Processing Blueprint": LocData(110, "Trader"),
    "Alchemy Table Blueprint": LocData(111, "Trader"),
    "Catalyst Blueprint": LocData(112, "Trader")
}

upgrade_locations = {
    "Click Hardness 1": LocData(201, "Obelisk"),
    "Click Hardness 2": LocData(202, "Obelisk"),
    "Click Hardness 3": LocData(203, "Obelisk"),
    "Click Hardness 4": LocData(204, "Obelisk"),
    "Click Power 1": LocData(205, "Obelisk"),
    "Click Power 2": LocData(206, "Obelisk"),
    "Click Power 3": LocData(207, "Obelisk"),
    "Click Power 4": LocData(208, "Obelisk"),
    "Click Power 5": LocData(209, "Obelisk"),
    "Click Power 6": LocData(210, "Obelisk"),
    "Click Power 7": LocData(211, "Obelisk"),
    "Click Power 8": LocData(212, "Obelisk"),
    "Click Power 9": LocData(213, "Obelisk"),
    "Hand Size 1": LocData(214, "Obelisk"),
    "Hand Size 2": LocData(215, "Obelisk"),
    "Hand Size 3": LocData(216, "Obelisk"),
    "Hand Size 4": LocData(217, "Obelisk"),
    "Hand Size 5": LocData(218, "Obelisk"),
    "Hand Size 6": LocData(219, "Obelisk"),
    "Hand Size 7": LocData(220, "Obelisk"),
    "Auto Click 1": LocData(221, "Obelisk"),
    "Auto Click 2": LocData(222, "Obelisk"),
    "Auto Click 3": LocData(223, "Obelisk"),
    "Auto Click 4": LocData(224, "Obelisk"),
    "Building Storage 1": LocData(225, "Obelisk"),
    "Building Storage 2": LocData(226, "Obelisk"),
    "Building Storage 3": LocData(227, "Obelisk"),
    "Building Storage 4": LocData(228, "Obelisk"),
    "Building Storage 5": LocData(229, "Obelisk"),
    "Building Storage 6": LocData(230, "Obelisk"),
    "Building Storage 7": LocData(231, "Obelisk"),
    "Building Storage 8": LocData(232, "Obelisk"),
    "Fuel Storage 1": LocData(233, "Obelisk"),
    "Fuel Storage 2": LocData(234, "Obelisk"),
    "Fuel Storage 3": LocData(235, "Obelisk"),
    "Fuel Storage 4": LocData(236, "Obelisk"),
    "Fuel Storage 5": LocData(237, "Obelisk"),
    "Move Fast 1": LocData(238, "Obelisk"),
    "Beach Upgrade 1": LocData(239, "Obelisk"),
    "Beach Upgrade 2": LocData(240, "Obelisk")
}

portal_locations = {
    "Portal Stage 1": LocData(301, "Portal"),
    "Portal Stage 2": LocData(302, "Portal"),
    "Portal Stage 3": LocData(303, "Portal"),
    "Portal Stage 4": LocData(304, "Portal"),
    "Portal Stage 5": LocData(305, "Portal"),
    "Portal Stage 6": LocData(306, "Portal"),
    "Portal Stage 7": LocData(307, "Portal"),
    "Portal Stage 8": LocData(308, "Portal"),
    "Portal Stage 9": LocData(309, "Portal"),
    "Portal Stage 10": LocData(310, "Portal"),
    "Portal Stage 11": LocData(311, "Portal"),
    "Portal Stage 12": LocData(312, "Portal"),
    "Portal Stage 13": LocData(313, "Portal")
}

location_table = {
    **blueprint_locations,
    **upgrade_locations,
    **portal_locations
}

