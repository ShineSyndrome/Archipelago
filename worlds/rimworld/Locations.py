from typing import Dict, NamedTuple, Optional

from BaseClasses import Location


class RimWorldLocation(Location):
    game: str = "Rogue Legacy"


class RimWorldLocationData(NamedTuple):
    category: str
    code: Optional[int] = None


def get_locations_by_category(category: str, location_table: Dict[str, RimWorldLocationData]) -> \
        Dict[str, RimWorldLocationData]:
    location_dict: Dict[str, RimWorldLocationData] = {}
    for name, data in location_table.items():
        if data.category == category:
            location_dict.setdefault(name, data)

    return location_dict


def build_location_table(research: int, craft: int, buy: int) -> Dict[str, RimWorldLocationData]:
    return {
        **{f"Research {i + 1}": RimWorldLocationData("Research", 11_000 + i) for i in range(0, research)},
        **{f"Craft {i + 1}": RimWorldLocationData("Craft", 12_000 + i) for i in range(0, craft)},
        **{f"Purchase {i + 1}": RimWorldLocationData("Purchase", 13_000 + i) for i in range(0, buy)},
    }
