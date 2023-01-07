import pprint
from typing import Dict, NamedTuple, Optional

from BaseClasses import Item, ItemClassification
from .data.research import *

class RimWorldItem(Item):
     game: str = "RimWorld"

class RWItemData(NamedTuple):
    category: str
    code: Optional[int] = None
    classification: ItemClassification = ItemClassification.filler
    max_quantity: int = 1
    weight: int = 1


def get_items_by_category(category: str) -> Dict[str, RWItemData]:
    item_dict: Dict[str, RWItemData] = {}
    for name, data in item_table.items():
        if data.category == category:
            item_dict.setdefault(name, data)

    return item_dict


item_table: Dict[str, RWItemData] = {}


id_iterator = 1
def addToItemTable(research_list: list[dict]):
    global id_iterator
    for research in research_list:
        item_table[research['label']] = RWItemData('research', id_iterator, ItemClassification.useful)
        id_iterator+=1

addToItemTable(research_1)
addToItemTable(research_2)
addToItemTable(research_3)
addToItemTable(research_4)
addToItemTable(research_5)
addToItemTable(research_biotech_mech)
addToItemTable(research_biotech_misc)
addToItemTable(research_ideology)
addToItemTable(research_royalty_implants)
addToItemTable(research_royalty_music)
addToItemTable(research_royalty_apparel)

pprint.pp(item_table)
