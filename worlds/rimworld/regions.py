from typing import NamedTuple
from constants import *
from .options import RimWorldOptions
from .locations import *

class RimWorldRegion(NamedTuple):
    name: str
    type: str

SimpleResearch = RimWorldRegion('simple_research', Locations.Categories.RESEARCH)
AdvancedResearch = RimWorldRegion('advanced_research', Locations.Categories.RESEARCH)
MultiAnalyzerResearch = RimWorldRegion('multi_analyzer_research', Locations.Categories.RESEARCH)



def create_regions(options: RimWorldOptions):
    
def remove_starting_tech(options: RimWorldOptions):



def filter_locations_by_expansion(options: RimWorldOptions):

