'''
IDE friendly way to handle those string references easily and correctly :)
'''


class Locations:
    class Categories:
        RESEARCH = "Research"
        CRAFTING = "Craft"
        PURCHASE = "Purchase"


class Items:
    class Categories:
        RESEARCH = "research"
        FILLER = "filler"

    class Expansions:
        CORE = "core"
        IDEOLOGY = "ideology"
        ROYALTY = "royalty"
        BIOTECH = "biotech"


class Options:
    ROYALTY = "royalty"
    IDEOLOGY = "ideology"
    BIOTECH = "biotech"
    RESEARCH_LOCATIONS_QUANTITY = "research_locations"
    CRAFT_LOCATIONS_QUANTITY = "craft_locations"
    PURCHASE_LOCATIONS_QUANTITY = "purchase_locations"
    MAX_RESEARCH_COST = "research_max"
    MIN_RESEARCH_COST = "research_min"
