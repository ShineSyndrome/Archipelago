from typing import Dict

from BaseClasses import Tutorial
from .items import all_items_name_to_id, electricity_research_item
from .locations import all_locations_name_to_id
from .options import RimWorldOptions, StartingScenario
from .regions import create_regions
from ..AutoWorld import WebWorld, World

class RimWorldWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Rimworld for Archipelago. "
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

        if self.options.starting_scenario.value == StartingScenario.option_lost_tribe_early_power:
            self.multiworld.local_early_items[self.player][electricity_research_item.identifier()] = 1

        self._validate_options()

    def create_regions(self) -> None:
        create_regions(self.multiworld, self.player, self.options)

    def create_items(self) -> None:
        """
        Method for creating and submitting items to the itempool. Items and Regions must *not* be created and submitted
        to the MultiWorld after this step. If items need to be placed during pre_fill use `get_prefill_items`.
        """
        pass

    def set_rules(self) -> None:
        """Method for setting the rules on the World's regions and locations."""
        pass

    def fill_slot_data(self) -> Dict[str, Any]:  # json of WebHostLib.models.Slot
        """Fill in the `slot_data` field in the `Connected` network package.
        This is a way the generator can give custom data to the client.
        The client will receive this as JSON in the `Connected` response.

        The generation does not wait for `generate_output` to complete before calling this.
        `threading.Event` can be used if you need to wait for something from `generate_output`."""
        return {}

    def _validate_options(self):
        
        biotech_starting_scenario = self.options.starting_scenario.value in [StartingScenario.option_mechanitor, StartingScenario.option_sanguophage]

        if not self.options.biotech_expansion and biotech_starting_scenario:
            raise Exception(f"{self.multiworld.get_player_name(self.player)}'s RimWorld settings aren't supported."
                f" The chosen starting scenario requires enabling Biotech DLC.")