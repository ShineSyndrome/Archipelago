from typing import List, Dict

from BaseClasses import Entrance, Region, RegionType, Tutorial
from .Items import item_table, RimWorldItem, get_items_by_category
from .Locations import build_location_table, RimWorldLocation, RimWorldLocationData
from .Options import rimworld_options
from ..AutoWorld import WebWorld, World


class RimWorldWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Rimworld for Archipelago. "
        "This guide covers single-player, multiworld, and related software.",
        "English",
        "rimworld_en.md",
        "rimworld/en",
        ["Stephen Lujan"]
    )]


class RimWorldWorld(World):
    """
    RimWorld is a sci-fi colony sim driven by an intelligent AI storyteller.
    Inspired by Dwarf Fortress, Firefly, and Dune. You begin with three
    survivors of a shipwreck on a distant world. Manage colonists' moods,
    needs, wounds, illnesses and addictions. Build in the forest, desert,
    jungle, tundra, and more.
    """
    game = "RimWorld"
    web = RimWorldWeb()
    option_definitions = rimworld_options
    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_table: Dict[str, RimWorldLocationData] = build_location_table(50, 50, 20)
    location_name_to_id = {name: data.code for name, data in location_table.items()}

    topology_present: bool = False  # show path to required location checks in spoiler

    # data_version is used to signal that items, locations or their names
    # changed. Set this to 0 during development so other games' clients do not
    # cache any texts, then increase by 1 for each release that makes changes.
    data_version = 0

    def get_setting(self, name: str):
        return getattr(self.multiworld, name)[self.player]

    def fill_slot_data(self) -> dict:
        return {option_name: self.get_setting(option_name).value for option_name in rimworld_options}

    def generate_basic(self):
        item_pool: List[RimWorldItem] = []
        total_locations = len(self.multiworld.get_unfilled_locations(self.player))
        for name, data in item_table.items():
            quantity = data.max_quantity

            if data.category == "Filler":
                continue
            if not self.get_setting('royalty_expansion') and data.expansion == 'royalty':
                continue
            if not self.get_setting('ideology_expansion') and data.expansion == 'ideology':
                continue
            if not self.get_setting('biotech_expansion') and data.expansion == 'biotech':
                continue
            quantity = data.max_quantity
            item_pool += [self.create_item(name) for _ in range(0, quantity)]

        # Fill any empty locations with filler items.
        while len(item_pool) < total_locations:
            item_pool.append(self.create_item(self.get_filler_item_name()))

        self.multiworld.itempool += item_pool

    def get_filler_item_name(self) -> str:
        # TODO
        fillers = get_items_by_category("Filler")
        weights = [data.weight for data in fillers.values()]
        return self.multiworld.random.choices([filler for filler in fillers.keys()], weights, k=1)[0]

    def create_item(self, name: str) -> RimWorldItem:
        data = item_table[name]
        return RimWorldItem(name, data.classification, data.code, self.player)

    def create_regions(self):
        player = self.player
        menu = Region("Menu", RegionType.Generic, "Menu", player, self.multiworld)
        crash = Entrance(player, "Crash Land", menu)
        menu.exits.append(crash)
        planet = Region("RimWorld", RegionType.Generic, "RimWorld", player, self.multiworld)
        self.locations: List[RimWorldLocation] = [RimWorldLocation(player, name, loc.code, planet)
                                                  for name, loc in RimWorldWorld.location_table.items()]
        planet.locations.extend(self.locations)

        crash.connect(planet)
        self.multiworld.regions += [menu, planet]
