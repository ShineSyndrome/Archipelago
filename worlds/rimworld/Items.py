import timeit
from typing import Dict, NamedTuple, Optional

from BaseClasses import Item, ItemClassification
from .data.research import *
from .data.research_items import *


class RimWorldItem(Item):
    game: str = "RimWorld"


class RimWorldItemData(NamedTuple):
    category: str
    expansion: str
    code: Optional[int] = None
    classification: ItemClassification = ItemClassification.filler
    max_quantity: int = 1
    weight: int = 1

item_table: Dict[str, RimWorldItemData] = {
    # TODO remove meaningless 'filler'
    'filler': RimWorldItemData('Filler', 'core', 2001, ItemClassification.filler, 999)
}

def addToItemTable(list: list[dict], category: str, expansion: str, classification = ItemClassification.useful):
    for item in list:
        label = item['label']
        id = label_to_item_id[label]
        item_table[label] = RimWorldItemData(category, expansion, id, classification)

addToItemTable(research_1, 'research', 'core')
addToItemTable(research_2, 'research', 'core')
addToItemTable(research_3, 'research', 'core')
addToItemTable(research_4, 'research', 'core')
addToItemTable(research_5, 'research', 'core')
addToItemTable(research_biotech_mech, 'research', 'biotech')
addToItemTable(research_biotech_misc, 'research', 'biotech')
addToItemTable(research_ideology, 'research', 'ideology')
addToItemTable(research_royalty_implants, 'research', 'royalty')
addToItemTable(research_royalty_music, 'research', 'royalty')
addToItemTable(research_royalty_apparel, 'research', 'royalty')


def get_items_by_category(category: str) -> Dict[str, RimWorldItem]:
    item_dict: Dict[str, RimWorldItem] = {}
    for name, data in item_table.items():
        if data.category == category:
            item_dict.setdefault(name, data)

    return item_dict
