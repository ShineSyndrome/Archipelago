from . import RimWorldTestBase


class CrashLandedTest(RimWorldTestBase):
    options = {
        "starting_scenario": 0
    }


class LostTribeTest(RimWorldTestBase):
    options = {
        "starting_scenario": 1
    }


class LostTribeEarlyPowerTest(RimWorldTestBase):
    options = {
        "starting_scenario": 2
    }


class RichExplorerTest(RimWorldTestBase):
    options = {
        "starting_scenario": 3
    }


class NakedBrutalityTest(RimWorldTestBase):
    options = {
        "starting_scenario": 4
    }


class MechanitorTest(RimWorldTestBase):
    options = {
        "starting_scenario": 5
    }


class SanguophageTest(RimWorldTestBase):
    options = {
        "starting_scenario": 6
    }
