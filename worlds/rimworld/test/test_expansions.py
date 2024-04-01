from . import RimWorldTestBase


class NoExpansionTest(RimWorldTestBase):
    options = {
        "royalty_expansion": False,
        "ideology_expansion": False,
        "biotech_expansion": False
    }


class RoyaltyOnlyTest(RimWorldTestBase):
    options = {
        "royalty_expansion": True,
        "ideology_expansion": False,
        "biotech_expansion": False
    }


class IdeologyOnlyTest(RimWorldTestBase):
    options = {
        "royalty_expansion": False,
        "ideology_expansion": True,
        "biotech_expansion": False
    }


class BiotechOnlyTest(RimWorldTestBase):
    options = {
        "royalty_expansion": False,
        "ideology_expansion": False,
        "biotech_expansion": True
    }
