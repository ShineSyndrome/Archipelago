from typing import List, Dict

from BaseClasses import Entrance, Region, Tutorial, MultiWorld
from . import Constants
from .Items import item_table, RimWorldItem, get_items_by_category
from .Locations import build_location_table, RimWorldLocation, RimWorldLocationData
from .Options import rimworld_options
from .data import research_items
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
    # not all of these items will be present in every game but there needs to be a fixed name:id mapping here
    item_name_to_id = {name: data.archipelago_id for name, data in item_table.items()}
    # not all of these locations will be present in every game but there needs to be a fixed name:id mapping here
    location_name_to_id = {name: data.archipelago_id for name, data in build_location_table(300, 300, 300).items()}

    topology_present = False  # show path to required location checks in spoiler

    # data_version is used to signal that items, locations or their names
    # changed. Set this to 0 during development so other games' clients do not
    # cache any texts, then increase by 1 for each release that makes changes.
    data_version = 0

    def __init__(self, world: MultiWorld, player: int):
        super().__init__(world, player)
        self.locations_data = build_location_table(
            self.get_setting(Constants.Options.RESEARCH_LOCATIONS_QUANTITY),
            self.get_setting(Constants.Options.CRAFT_LOCATIONS_QUANTITY),
            self.get_setting(Constants.Options.PURCHASE_LOCATIONS_QUANTITY),
        )
        self.locations: List[RimWorldLocation] = []

    def get_setting(self, name: str):
        return getattr(self.multiworld, name)[self.player].value

    def create_regions(self):
        # some basic regions are needed for any game to work in archipelago
        player = self.player
        menu = Region("Menu", player, self.multiworld)
        game_start = Entrance(player, "Start Game", menu)
        menu.exits.append(game_start)
        planet = Region("RimWorld", player, self.multiworld)
        game_start.connect(planet)
        self.multiworld.regions += [menu, planet]

        # add locations
        self.locations: List[RimWorldLocation] = [RimWorldLocation(player, name, loc.archipelago_id, planet)
                                                  for name, loc in self.locations_data.items()]
        planet.locations.extend(self.locations)

    def generate_basic(self):
        item_pool: List[RimWorldItem] = []
        total_locations = len(self.multiworld.get_unfilled_locations(self.player))
        for name, item in item_table.items():

            if item.category == Constants.Items.Categories.FILLER:
                continue
            if not self.get_setting(Constants.Options.ROYALTY) and item.expansion == Constants.Items.Expansions.ROYALTY:
                continue
            if not self.get_setting(
                    Constants.Options.IDEOLOGY) and item.expansion == Constants.Items.Expansions.IDEOLOGY:
                continue
            if not self.get_setting(Constants.Options.BIOTECH) and item.expansion == Constants.Items.Expansions.BIOTECH:
                continue
            quantity = item.max_quantity
            item_pool += [self.create_item(name) for _ in range(0, quantity)]

        # Fill any empty locations with filler items.
        while len(item_pool) < total_locations:
            item_pool.append(self.create_item(self.get_filler_item_name()))

        self.multiworld.itempool += item_pool

    def get_filler_item_name(self) -> str:
        # TODO
        fillers = get_items_by_category(Constants.Items.Categories.FILLER)
        weights = [item.weight for item in fillers.values()]
        return self.multiworld.random.choices([filler for filler in fillers.keys()], weights, k=1)[0]

    def create_item(self, name: str) -> RimWorldItem:
        item = item_table[name]
        return RimWorldItem(name, item.classification, item.archipelago_id, self.player)

    def fill_slot_data(self) -> Dict[str, object]:
        slot_data: Dict[str, object] = {}

        research_locations = [value for key, value in self.locations_data.items()
                              if value.category == Constants.Locations.Categories.RESEARCH]
        tech_tree = Locations.build_research_tech_tree(
            research_locations,
            self.get_setting(Constants.Options.MIN_RESEARCH_COST),
            self.get_setting(Constants.Options.MAX_RESEARCH_COST)
        )
        slot_data['techTree'] = tech_tree  # json.dumps(tech_tree, separators=(',', ':'))

        slot_data['item_id_to_rimworld_def'] = self._item_id_to_rimworld_def()

        return slot_data

    def have_expansion(self, expansion) -> bool:
        return (expansion == Constants.Items.Expansions.CORE
                or (expansion == Constants.Items.Expansions.ROYALTY and self.get_setting(Constants.Options.ROYALTY))
                or (expansion == Constants.Items.Expansions.BIOTECH and self.get_setting(Constants.Options.BIOTECH))
                or (expansion == Constants.Items.Expansions.IDEOLOGY and self.get_setting(Constants.Options.IDEOLOGY)))

    def _item_id_to_rimworld_def(self) -> Dict[int, tuple[str, str]]:
        expansions = []
        if self.get_setting(Constants.Options.ROYALTY):
            expansions.append(Constants.Items.Expansions.ROYALTY)
        if self.get_setting(Constants.Options.BIOTECH):
            expansions.append(Constants.Items.Expansions.BIOTECH)
        if self.get_setting(Constants.Options.IDEOLOGY):
            expansions.append(Constants.Items.Expansions.IDEOLOGY)

        return {
            value.archipelago_id: {
                'defName': value.defName,
                'defType': value.defType,
            } for value in
            Items.get_items_by_category(Constants.Items.Categories.RESEARCH, expansions).values()
        }
