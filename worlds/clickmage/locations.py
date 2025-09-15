from typing import TYPE_CHECKING
from .types import LocData

if TYPE_CHECKING:
    from . import ClickMageWorld

def get_total_locations(world: "ClickMageWorld") -> int:
    return sum(1 for _ in location_table)

def get_location_names() -> dict[str, int]:
    names = {name: data.ap_code for name, data in location_table.items()}

    return names

location_table = {}

