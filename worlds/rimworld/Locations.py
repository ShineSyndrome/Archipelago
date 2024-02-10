import random
from typing import Dict, NamedTuple, List, Optional

from BaseClasses import Location
from .Constants import Locations


class RimWorldLocation(Location):
    game: str = "RimWorld"


class RimWorldLocationData(NamedTuple):
    category: str
    archipelago_id: int


def build_location_table(research: int, craft: int, buy: int) -> Dict[str, RimWorldLocationData]:
    return {
        **{f"Research {i + 1}": RimWorldLocationData(Locations.Categories.RESEARCH, 11_000 + i) for i in
           range(0, research)},
        **{f"Craft {i + 1}": RimWorldLocationData(Locations.Categories.CRAFTING, 12_000 + i) for i in range(0, craft)},
        **{f"Purchase {i + 1}": RimWorldLocationData(Locations.Categories.PURCHASE, 13_000 + i) for i in range(0, buy)},
    }


class ResearchLocationData(NamedTuple):
    '''
    important research metadata used by RimWorld like
    research costs, prerequisites, and their rendered position in the tech tree
    '''
    x: int
    y: int
    cost: int
    prerequisites: List[int]


def build_research_tech_tree(researches: List[RimWorldLocationData], min_cost, max_cost) \
        -> Dict[int, Dict]:
    # -> Dict[int, ResearchLocationData]:
    '''
    outputs all the ResearchLocationData Rimworld needs to set up the research tree
    each piece of metadata is keyed by their corresponding location's Archipelago code

    :param researches: a list of RimWorldLocationData for research locations in this game instance
    :param min_cost: the cheapest research cost that will be created
    :param max_cost: the final and most expensive research cost that will be created
    :return: location code to ResearchLocationData dictionary
    '''
    ROWS = 5
    EMPTY_CHANCE_PERCENT = 10
    TWO_PREREQUISITES_CHANCE = 20
    NO_PREREQUISITES_CHANCE = 0
    # TODO make options of the above?
    output = {}

    # temporary grid building iteration
    table: List[List[Optional[int]]] = []
    x = 0
    y = 0
    column_has_empty = False
    current_column: List[Optional[int]] = [None] * ROWS
    cost_increment = (max_cost - min_cost) / len(researches)
    current_cost = min_cost

    # create grid of research
    for research in researches:
        # chance for empty, skip one space
        if not column_has_empty and random.randint(0, 100) < EMPTY_CHANCE_PERCENT:
            column_has_empty = True
            y += 1
        # start new column
        if y > ROWS - 1:
            y -= ROWS
            x += 1
            column_has_empty = False
            table.append(current_column)
            current_column = [None] * ROWS

        # place research in table
        current_column[y] = research.archipelago_id

        # make prerequisites
        prerequisites: list[int] = []
        if x > 0 and random.randint(0, 100) >= NO_PREREQUISITES_CHANCE:
            valid_prerequisites = []
            prereq = table[x - 1][y]
            if prereq is not None:
                valid_prerequisites.append(prereq)
            if y < ROWS - 1:
                prereq = table[x - 1][y + 1]
                if prereq is not None:
                    valid_prerequisites.append(prereq)
            if y > 0:
                prereq = table[x - 1][y - 1]
                if prereq is not None:
                    valid_prerequisites.append(prereq)
            k = 1
            if random.randint(0, 100) < TWO_PREREQUISITES_CHANCE:
                k = min(len(valid_prerequisites), 2)
            prerequisites: list[int] = random.sample(valid_prerequisites, k=k)

        # build output data
        output[research.archipelago_id] = ResearchLocationData(x, y, current_cost, prerequisites)._asdict()
        # using _asdict() for now because named tuple serializes pretty weird

        # prepare next iteration
        y += 1
        current_cost += cost_increment

    return output
