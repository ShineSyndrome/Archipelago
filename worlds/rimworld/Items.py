import pprint
from typing import Dict, NamedTuple, Optional

from BaseClasses import Item, ItemClassification
from .data.research import *
from .data.research_items import *

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
def addToItemTable(research_list: list[dict]):
    for research in research_list:
        label = research['label']
        id = label_to_item_id[label]
        item_table[label] = RWItemData('research', id, ItemClassification.useful)


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
