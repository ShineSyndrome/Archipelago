from typing import Any, Dict

from BaseClasses import Tutorial
from worlds.rimworld.rules import set_rules
from .items import RimWorldItem, all_items_name_to_id, create_item, create_items, electricity_research_item
from .locations import all_locations_name_to_id
from .options import RimWorldOptions, StartingScenario
from .regions import create_regions
from ..AutoWorld import WebWorld, World


class RimWorldWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up RimWorld for Archipelago. "
        "This guide covers single-player, multiworld, and related software.",
        "English",
        "rimworld_en.md",
        "rimworld/en",
        ["Rob Gardner"]
    )]


class RimWorldWorld(World):
    """
    RimWorld is a sci-fi colony sim driven by an intelligent AI storyteller.
    Inspired by Dwarf Fortress, Firefly, and Dune. 
    You begin with survivors of a shipwreck on a distant world. Manage colonists' moods,
    needs, wounds, illnesses and addictions. Build in the forest, desert,
    jungle, tundra, and more.
    """
    game = "RimWorld"
    web = RimWorldWeb()
    options_dataclass = RimWorldOptions
    options: RimWorldOptions

    item_name_to_id = all_items_name_to_id
    location_name_to_id = all_locations_name_to_id

    def generate_early(self) -> None:

        self._validate_options()

        if self.options.starting_scenario.value == StartingScenario.option_lost_tribe_early_power:
            self.multiworld.local_early_items[self.player][electricity_research_item.identifier()] = 1

    def create_regions(self) -> None:
        create_regions(self.multiworld, self.player, self.options)

    def create_items(self) -> None:
        create_items(self.multiworld, self.player, self.options)

    def create_item(self, item: str) -> RimWorldItem:
        return create_item(item, self.player)

    def set_rules(self) -> None:
        set_rules(self.multiworld, self.player, self.options)

    def fill_slot_data(self) -> Dict[str, Any]:
        slot_data: Dict[str, Any] = {
            "scenario": self.options.starting_scenario.value,
            "biotech": self.options.biotech_expansion.value,
            "royalty": self.options.royalty_expansion.value,
            "ideology": self.options.ideology_expansion.value,
        }

        return slot_data

    def _validate_options(self):

        biotech_starting_scenario = self.options.starting_scenario.value in [StartingScenario.option_mechanitor,
                                                                             StartingScenario.option_sanguophage]

        if not self.options.biotech_expansion and biotech_starting_scenario:
            raise Exception(f"{self.multiworld.get_player_name(self.player)}'s RimWorld settings aren't supported."
                            f" The chosen starting scenario requires enabling Biotech DLC.")
