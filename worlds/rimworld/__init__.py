
from BaseClasses import Entrance, Item, ItemClassification, Location, MultiWorld, Region, RegionType, Tutorial
from .Items import item_table
#from .Locations import location_table
#from .Options import spire_options
from ..AutoWorld import WebWorld, World


class RimWorldWorld(World):
    game = "RimWorld"
    item_name_to_id = {name: data.code for name, data in item_table.items()}