import timeit
from typing import Dict, NamedTuple, Optional

from BaseClasses import Item, ItemClassification
from .data.research import *
from .data.research_items import *
from .Constants import Items

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
    'filler': RimWorldItemData(Items.Categories.FILLER, Items.Expansions.CORE, 2001, ItemClassification.filler, 999)
}

def addToItemTable(list: list[dict], category: str, expansion: str, classification = ItemClassification.useful):
    for item in list:
        label = item['label']
        id = label_to_item_id[label]
        item_table[label] = RimWorldItemData(category, expansion, id, classification)

addToItemTable(research_1, Items.Categories.RESEARCH, Items.Expansions.CORE)
addToItemTable(research_2, Items.Categories.RESEARCH, Items.Expansions.CORE)
addToItemTable(research_3, Items.Categories.RESEARCH, Items.Expansions.CORE)
addToItemTable(research_4, Items.Categories.RESEARCH, Items.Expansions.CORE)
addToItemTable(research_5, Items.Categories.RESEARCH, Items.Expansions.CORE)
addToItemTable(research_biotech_mech, Items.Categories.RESEARCH, Items.Expansions.BIOTECH)
addToItemTable(research_biotech_misc, Items.Categories.RESEARCH, Items.Expansions.BIOTECH)
addToItemTable(research_ideology, Items.Categories.RESEARCH, Items.Expansions.IDEOLOGY)
addToItemTable(research_royalty_implants, Items.Categories.RESEARCH, Items.Expansions.ROYALTY)
addToItemTable(research_royalty_music, Items.Categories.RESEARCH, Items.Expansions.ROYALTY)
addToItemTable(research_royalty_apparel, Items.Categories.RESEARCH, Items.Expansions.ROYALTY)


def get_items_by_category(category: str) -> Dict[str, RimWorldItemData]:
    item_dict: Dict[str, RimWorldItemData] = {}
    for name, data in item_table.items():
        if data.category == category:
            item_dict.setdefault(name, data)

    return item_dict


