from BaseClasses import Location, MultiWorld, Region
from constants import *
from .options import RimWorldOptions
from .locations import *

class RimWorldLocation(Location):
    game: str = "RimWorld"

    # override constructor to automatically mark event locations as such
    def __init__(self, player: int, name="", code=None, parent=None) -> None:
        super(RimWorldLocation, self).__init__(player, name, code, parent)
        self.event = code is None

class RegionNames:
    MENU_REGION = "Menu"

    SIMPLE_RESEARCH = "SIMPLE_RESEARCH"
    HITECH_RESEARCH = "HITECH_RESEARCH"
    MA_RESEARCH = "MA_RESEARCH"

def create_regions(multiworld: MultiWorld, player: int, options: RimWorldOptions):
    
    filtered_simple_research = filter_starting_tech(simple_research_locations, options.starting_scenario.value)
    filtered_simple_research = filter_locations_by_expansion(filtered_simple_research, options)
    filtered_hitech_research = filter_locations_by_expansion(hitech_research_locations, options)
    filtered_ma_research =  filter_locations_by_expansion(multi_analyzer_research_locations, options)

    menu_region = Region(RegionNames.MENU_REGION, player, multiworld)

    simple_research_region = create_region(multiworld, player, filtered_simple_research, RegionNames.SIMPLE_RESEARCH)
    hitech_research_region = create_region(multiworld, player, filtered_hitech_research, RegionNames.HITECH_RESEARCH)
    ma_research_region =  create_region(multiworld, player, filtered_ma_research, RegionNames.MA_RESEARCH)

    menu_region.connect(simple_research_region)
    simple_research_region.connect(hitech_research_region)
    hitech_research_region.connect(ma_research_region)

    multiworld.regions += menu_region
    multiworld.regions += simple_research_region
    multiworld.regions += hitech_research_region
    multiworld.regions += ma_research_region

def filter_starting_tech(research_locations: Dict[int, RimWorldLocationData], starting_scenario: str) -> Dict[int,RimWorldLocationData]:

    starting_tech = starting_tech_dict[starting_scenario]
    return {
	loc_id: research_location
	for loc_id, research_location in research_locations.items()
		if research_location not in starting_tech
    }

def filter_locations_by_expansion(locations: Dict[int, RimWorldLocationData], options: RimWorldOptions) -> Dict[int,RimWorldLocationData]:

    enabled_expansions = [Expansions.CORE]
    if options.biotech_expansion: enabled_expansions.append(Expansions.BIOTECH)
    if options.royalty_expansion: enabled_expansions.append(Expansions.ROYALTY)
    if options.ideology_expansion: enabled_expansions.append(Expansions.IDEOLOGY)

    return {
	loc_id: location
	for loc_id, location in locations.items()
		if location.expansion in enabled_expansions
    }

def create_region(world: MultiWorld, player: int, locations: Dict[int, RimWorldLocationData], name: str) -> Region:
    region = Region(name, player, world)

    for id, location_data in locations.items():
        location = RimWorldLocation(player, location_data.identifier(), id, region)
        region.locations.append(location)
    
    return region

