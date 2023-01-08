import typing

from Options import Toggle, Option


class RoyaltyExpansion(Toggle):
    display_name = "Include Royalty Expansion"


class IdeologyExpansion(Toggle):
    display_name = "Include Ideology Expansion"


class BiotechExpansion(Toggle):
    display_name = "Include Biotech Expansion"


# By convention, we call the options dict variable `<world>_options`.
rimworld_options: typing.Dict[str, type(Option)] = {
    "royalty_expansion": RoyaltyExpansion,
    "ideology_expansion": IdeologyExpansion,
    "biotech_expansion": BiotechExpansion,
}
