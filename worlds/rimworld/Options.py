import typing

from Options import Toggle, Option


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


# By convention, we call the options dict variable `<world>_options`.
rimworld_options: typing.Dict[str, type(Option)] = {
    "royalty_expansion": RoyaltyExpansion,
    "ideology_expansion": IdeologyExpansion,
    "biotech_expansion": BiotechExpansion,
}
