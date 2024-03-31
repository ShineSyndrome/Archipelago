from worlds.generic.Rules import set_rule
from .regions import ExitNames
from .items import *


def set_rules(multiworld: MultiWorld, player: int, options: RimWorldOptions) -> None:
    if options.starting_scenario.value in \
            (options.starting_scenario.option_lost_tribe, options.starting_scenario.option_lost_tribe_early_power):

        set_rule(multiworld.get_entrance(ExitNames.CAN_HITECH_RESEARCH, player),
                 lambda state: state.has_all(
                     [electricity_research_item.identifier(), micro_electronics_research_item.identifier()], player))
    else:
        set_rule(multiworld.get_entrance(ExitNames.CAN_HITECH_RESEARCH, player),
                 lambda state: state.has(micro_electronics_research_item.identifier(), player))

    set_rule(multiworld.get_entrance(ExitNames.CAN_MA_RESEARCH, player),
             lambda state: state.has(multi_analyzer_research_item.identifier(), player))

    multiworld.completion_condition[player] = lambda state: state.has_all([
        ship_basics_research_item.identifier(),
        ship_computer_core_research_item.identifier(),
        ship_crypto_sleep_research_item.identifier(),
        ship_engine_research_item.identifier(),
        ship_reactor_research_item.identifier(),
        ship_sensor_research_item.identifier()], player)
