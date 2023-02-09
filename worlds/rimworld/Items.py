import timeit
from typing import Dict, NamedTuple, Optional, Callable

from BaseClasses import Item, ItemClassification
from .data.research import *
from .data.research_items import *
from .Constants import Items


class RimWorldItem(Item):
    game: str = "RimWorld"


class RimWorldItemData(NamedTuple):
    category: str
    expansion: str
    defName: str
    defType: str
    archipelago_id: Optional[int] = None
    classification: ItemClassification = ItemClassification.filler
    max_quantity: int = 1
    weight: int = 1


item_table: Dict[str, RimWorldItemData] = {
    # TODO remove meaningless 'filler'
    'filler': RimWorldItemData(Items.Categories.FILLER, Items.Expansions.CORE, "fakeDefName", "fakeType", 2001,
                               ItemClassification.filler, 999)
}


def add_to_item_table(items: list[dict], category: str, expansion: str, def_type: str = 'ResearchProjectDef',
                      classification=ItemClassification.useful):
    for item in items:
        label = item['label']
        item_table[label] = RimWorldItemData(
            category, expansion, item['defName'], def_type, label_to_item_id[label], classification)


add_to_item_table(research_1, Items.Categories.RESEARCH, Items.Expansions.CORE)
add_to_item_table(research_2, Items.Categories.RESEARCH, Items.Expansions.CORE)
add_to_item_table(research_3, Items.Categories.RESEARCH, Items.Expansions.CORE)
add_to_item_table(research_4, Items.Categories.RESEARCH, Items.Expansions.CORE)
add_to_item_table(research_5, Items.Categories.RESEARCH, Items.Expansions.CORE)
add_to_item_table(research_biotech_mech, Items.Categories.RESEARCH, Items.Expansions.BIOTECH)
add_to_item_table(research_biotech_misc, Items.Categories.RESEARCH, Items.Expansions.BIOTECH)
add_to_item_table(research_ideology, Items.Categories.RESEARCH, Items.Expansions.IDEOLOGY)
add_to_item_table(research_royalty_implants, Items.Categories.RESEARCH, Items.Expansions.ROYALTY)
add_to_item_table(research_royalty_music, Items.Categories.RESEARCH, Items.Expansions.ROYALTY)
add_to_item_table(research_royalty_apparel, Items.Categories.RESEARCH, Items.Expansions.ROYALTY)


def get_items_by_category(category: str, expansions: list[str] = None) -> Dict[str, RimWorldItemData]:
    if expansions is None:
        expansions = [Items.Expansions.BIOTECH, Items.Expansions.IDEOLOGY, Items.Expansions.ROYALTY]

    item_dict: Dict[str, RimWorldItemData] = {}
    for name, data in item_table.items():
        if data.category == category:
            if data.expansion == Items.Expansions.CORE or data.expansion in expansions:
                item_dict.setdefault(name, data)

    return item_dict
