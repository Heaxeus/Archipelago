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
    "Portal Blueprint": LocData(101, "Portal Blueprint"),
    "Water Well Blueprint": LocData(102, "Water Well Blueprint"),
    "Smelter Blueprint": LocData(103, "Smelter Blueprint"),
    "Charcoal Blueprint": LocData(104, "Charcoal Blueprint"),
    "Saw Blueprint": LocData(105, "Saw Blueprint"),
    "Storage Blueprint": LocData(106, "Storage Blueprint"),
    "Forge Blueprint": LocData(107, "Forge Blueprint"),
    "Phial Blueprint": LocData(108, "Phial Blueprint"),
    "Steel Processing Blueprint": LocData(109, "Steel Blueprint"),
    "Copper Processing Blueprint": LocData(110, "Copper Blueprint"),
    "Alchemy Table Blueprint": LocData(111, "Alchemy Blueprint"),
    "Catalyst Blueprint": LocData(112, "Catalyst Blueprint")
}

upgrade_locations = {
    "Click Hardness 1": LocData(201, "Click Hardness 1"),
    "Click Hardness 2": LocData(202, "Click Hardness 2"),
    "Click Hardness 3": LocData(203, "Click Hardness 3"),
    "Click Hardness 4": LocData(204, "Click Hardness 4"),
    "Click Power 1": LocData(205, "Click Power 1"),
    "Click Power 2": LocData(206, "Click Power 2"),
    "Click Power 3": LocData(207, "Click Power 3"),
    "Click Power 4": LocData(208, "Click Power 4"),
    "Click Power 5": LocData(209, "Click Power 5"),
    "Click Power 6": LocData(210, "Click Power 6"),
    "Click Power 7": LocData(211, "Click Power 7"),
    "Click Power 8": LocData(212, "Click Power 8"),
    "Click Power 9": LocData(213, "Click Power 9"),
    "Hand Size 1": LocData(214, "Hand Size 1"),
    "Hand Size 2": LocData(215, "Hand Size 2"),
    "Hand Size 3": LocData(216, "Hand Size 3"),
    "Hand Size 4": LocData(217, "Hand Size 4"),
    "Hand Size 5": LocData(218, "Hand Size 5"),
    "Hand Size 6": LocData(219, "Hand Size 6"),
    "Hand Size 7": LocData(220, "Hand Size 7"),
    "Auto Click 1": LocData(221, "Auto Click 1"),
    "Auto Click 2": LocData(222, "Auto Click 2"),
    "Auto Click 3": LocData(223, "Auto Click 3"),
    "Auto Click 4": LocData(224, "Auto Click 4"),
    "Building Storage 1": LocData(225, "Building Storage 1"),
    "Building Storage 2": LocData(226, "Building Storage 2"),
    "Building Storage 3": LocData(227, "Building Storage 3"),
    "Building Storage 4": LocData(228, "Building Storage 4"),
    "Building Storage 5": LocData(229, "Building Storage 5"),
    "Building Storage 6": LocData(230, "Building Storage 6"),
    "Building Storage 7": LocData(231, "Building Storage 7"),
    "Building Storage 8": LocData(232, "Building Storage 8"),
    "Fuel Storage 1": LocData(233, "Fuel Storage 1"),
    "Fuel Storage 2": LocData(234, "Fuel Storage 2"),
    "Fuel Storage 3": LocData(235, "Fuel Storage 3"),
    "Fuel Storage 4": LocData(236, "Fuel Storage 4"),
    "Fuel Storage 5": LocData(237, "Fuel Storage 5"),
    "Move Fast 1": LocData(238, "Move Fast"),
    "Beach Upgrade 1": LocData(239, "Beach Upgrade 1"),
    "Beach Upgrade 2": LocData(240, "Beach Upgrade 2")
}

portal_locations = {
    "Portal Stage 1": LocData(301, "Portal Stage 1"),
    "Portal Stage 2": LocData(302, "Portal Stage 2"),
    "Portal Stage 3": LocData(303, "Portal Stage 3"),
    "Portal Stage 4": LocData(304, "Portal Stage 4"),
    "Portal Stage 5": LocData(305, "Portal Stage 5"),
    "Portal Stage 6": LocData(306, "Portal Stage 6"),
    "Portal Stage 7": LocData(307, "Portal Stage 7"),
    "Portal Stage 8": LocData(308, "Portal Stage 8"),
    "Portal Stage 9": LocData(309, "Portal Stage 9"),
    "Portal Stage 10": LocData(310, "Portal Stage 10"),
    "Portal Stage 11": LocData(311, "Portal Stage 11"),
    "Portal Stage 12": LocData(312, "Portal Stage 12"),
    "Portal Stage 13": LocData(313, "Portal Stage 13")
}

location_table = {
    **blueprint_locations,
    **upgrade_locations,
    **portal_locations
}

