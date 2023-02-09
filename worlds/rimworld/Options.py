import typing

from Options import Toggle, Option, Range
from .Constants import Options


class RoyaltyExpansion(Toggle):
    """
    Include items, technology, and events from the Royalty DLC
    """
    display_name = "Include Royalty Expansion"
    default = 1


class IdeologyExpansion(Toggle):
    """
    Include items, technology, and events from the Ideology DLC
    """
    display_name = "Include Ideology Expansion"
    default = 1


class BiotechExpansion(Toggle):
    """
    Include items, technology, and events from the Biotech DLC
    """
    display_name = "Include Biotech Expansion"
    default = 1


class TechLocationsQuantity(Range):
    """
    How many Archipelago items are added to the Archipelago research tree.
    """
    display_name = "Researchable Items"
    default = 50
    range_start = 0
    range_end = 300


class CraftingLocationsQuantity(Range):
    """
    How many Archipelago items are added to the Archipelago work bench.
    """
    display_name = "Craftable Items"
    default = 50
    range_start = 0
    range_end = 300


class PurchasableLocationsQuantity(Range):
    """
    How many Archipelago items in total are available from Rimworld trades.
    """
    display_name = "Purchasable Items"
    default = 50
    range_start = 0
    range_end = 300


class MinimumResearchCost(Range):
    """
    How much work does it take to research the least expensive Archipelago item.
    """
    display_name = "Minimum Research Cost"
    default = 50
    range_start = 10
    range_end = 3000


class MaximumResearchCost(Range):
    """
    How much work does it take to research the most expensive Archipelago item.
    """
    display_name = "Maximum Research Cost"
    default = 1000
    range_start = 10
    range_end = 3000


# By convention, we call the options dict variable `<world>_options`.
rimworld_options: typing.Dict[str, type(Option)] = {
    Options.ROYALTY: RoyaltyExpansion,
    Options.IDEOLOGY: IdeologyExpansion,
    Options.BIOTECH: BiotechExpansion,
    Options.RESEARCH_LOCATIONS_QUANTITY: TechLocationsQuantity,
    Options.CRAFT_LOCATIONS_QUANTITY: CraftingLocationsQuantity,
    Options.PURCHASE_LOCATIONS_QUANTITY: PurchasableLocationsQuantity,
    Options.MAX_RESEARCH_COST: MaximumResearchCost,
    Options.MIN_RESEARCH_COST: MinimumResearchCost,
}
