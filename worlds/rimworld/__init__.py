from BaseClasses import Entrance, Item, ItemClassification, Location, MultiWorld, Region, RegionType, Tutorial
from .Items import build_item_table
# from .Locations import location_table
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
    game = "RimWorld"
    web = RimWorldWeb()
    option_definitions = rimworld_options  # options the player can set
    item_table = build_item_table(rimworld_options['royalty_expansion'],
                                  rimworld_options['ideology_expansion'],
                                  rimworld_options['biotech_expansion'])
    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {}

    topology_present: bool = False  # show path to required location checks in spoiler

    # data_version is used to signal that items, locations or their names
    # changed. Set this to 0 during development so other games' clients do not
    # cache any texts, then increase by 1 for each release that makes changes.
    data_version = 0
