from dataclasses import dataclass
from Options import Choice, DefaultOnToggle, PerGameCommonOptions


class RoyaltyExpansion(DefaultOnToggle):
    """
    Include technology from the Royalty DLC.
    """
    display_name = "Include Royalty Expansion"
    default = 1


class IdeologyExpansion(DefaultOnToggle):
    """
    Include technology from the Ideology DLC.
    """
    display_name = "Include Ideology Expansion"
    default = 1


class BiotechExpansion(DefaultOnToggle):
    """
    Include technology from the Biotech DLC.
    """
    display_name = "Include Biotech Expansion"
    default = 1


class StartingScenario(Choice):
    """The starting scenario for your colony
    (Starting the game with a different scenario than selected here will cause unreachable checks).
    Crash Landed: Three pawns with some modern technology unlocked, including electricity.
    Lost Tribe: Five pawns with low technology.
    Lost Tribe & Early Electricity: As above, but guarantees electricity can be found early in your world.
    Rich Explorer: One rich pawn with modern technology, including technologies related to gun manufacture.
    Naked Brutality: One pawn, alone and unprepared. They have modern technology unlocked, including electricity.
    Mechanitor: Requires the Biotech DLC. One advanced pawn with some advanced technology unlocked.
    Sanguophage: Requiores the Biotech DLC. One vampire and one human with modern tech. Also has Deathrest unlocked.
    """
    display_name = "Starting Scenario"
    default = 0
    option_crash_landed = 0
    option_lost_tribe = 1
    option_lost_tribe_early_power = 2
    option_rich_explorer = 3
    option_naked_brutality = 4
    option_mechanitor = 5
    option_sanguophage = 6


# There's more to come! For now, it's important to signal to a user
# that this is the win condition that logic is formed around.
class WinCondition(Choice):
    """The win condition you want to pursue for your colony.
    Build a Ship: Find all the research required to build your own ship and escape the planet."""
    display_name = "Win Condition"
    default = 0
    option_build_ship = 0


@dataclass
class RimWorldOptions(PerGameCommonOptions):
    royalty_expansion: RoyaltyExpansion
    ideology_expansion: IdeologyExpansion
    biotech_expansion: BiotechExpansion
    starting_scenario: StartingScenario
    win_condition: WinCondition
