from . import RimWorldTestBase
from ..options import StartingScenario
from ..items import micro_electronics_research_item, multi_analyzer_research_item, electricity_research_item
from ..locations import hitech_research_locations, multi_analyzer_research_locations


class DefaultAccessTest(RimWorldTestBase):

    def test_hitech_research(self) -> None:
        """Test hitech research requires research bench, part of microelectronics tech"""
        location_data = {**hitech_research_locations, **multi_analyzer_research_locations}
        locations = [location.identifier() for location in location_data.values()]
        items = [[micro_electronics_research_item.identifier()]]
        self.assertAccessDependency(locations, items)

    def test_multi_analyzer_research(self) -> None:
        """Test hitech research requires research bench, part of microelectronics tech"""
        locations = [location.identifier() for location in multi_analyzer_research_locations.values()]
        items = [[multi_analyzer_research_item.identifier()]]
        self.assertAccessDependency(locations, items)


class TribalAccessTest(RimWorldTestBase):
    options = {
        "starting_scenario": StartingScenario.option_lost_tribe
    }

    def test_tribal_hitech_research(self) -> None:
        """Test hitech research requires research bench, part of microelectronics tech"""
        location_data = {**hitech_research_locations, **multi_analyzer_research_locations}
        locations = [location.identifier() for location in location_data.values()]
        items = [[micro_electronics_research_item.identifier(), electricity_research_item.identifier()]]
        self.assertAccessDependency(locations, items)
