from .options import StartingScenario

class Expansions:
    CORE = "core"
    IDEOLOGY = "ideology"
    ROYALTY = "royalty"
    BIOTECH = "biotech"

#More categories coming soon
class Locations:
    class Categories:
        RESEARCH = "Research"

class Items:
    class Categories:
        RESEARCH = "Research"

class Researches:
    PSYCHOIDBREWING = "PsychoidBrewing"
    TREESOWING = "TreeSowing"
    BREWING = "Brewing"
    COMPLEXFURNITURE = "ComplexFurniture"
    PASSIVECOOLER = "PassiveCooler"
    STONECUTTING = "Stonecutting"
    COMPLEXCLOTHING = "ComplexClothing"
    DRUGPRODUCTION = "DrugProduction"
    COCOA = "Cocoa"
    DEVILSTRAND = "Devilstrand"
    CARPETMAKING = "CarpetMaking"
    PEMMICAN = "Pemmican"
    SMITHING = "Smithing"
    RECURVEBOW = "RecurveBow"
    PSYCHITEREFINING = "PsychiteRefining"
    WAKEUPPRODUCTION = "WakeUpProduction"
    GOJUICEPRODUCTION = "GoJuiceProduction"
    PENOXYCYLINEPRODUCTION = "PenoxycylineProduction"
    LONGBLADES = "LongBlades"
    PLATEARMOR = "PlateArmor"
    GREATBOW = "Greatbow"
    ELECTRICITY =  "Electricity"
    BATTERIES = "Batteries"
    BIOFUELREFINING = "BiofuelRefining"
    WATERMILLGENERATOR = "WatermillGenerator"
    NUTRIENTPASTE = "NutrientPaste"
    SOLARPANELS =  "SolarPanels"
    AIRCONDITIONING = "AirConditioning"
    AUTODOORS = "Autodoors"
    HYDROPONICS = "Hydroponics"
    TUBETELEVISION = "TubeTelevision" 
    PACKAGEDSURVIVALMEAL = "PackagedSurvivalMeal"
    FIREFOAM = "Firefoam"
    IEDS = "IEDs"
    GEOTHERMALPOWER = "GeothermalPower"
    STERILEMATERIALS = "SterileMaterials"
    COLOREDLIGHTS = "ColoredLights"
    MACHINING = "Machining"
    SMOKEPOPBELT = "SmokepopBelt"
    PROSTHETICS = "Prosthetics"
    GUNSMITHING = "Gunsmithing"
    FLAKARMOR = "FlakArmor"
    MORTARS = "Mortars"
    BLOWBACKOPERATION = "BlowbackOperation"
    GASOPERATION = "GasOperation"
    GUNTURRETS = "GunTurrets"
    FOAMTURRET = "FoamTurret"
    MICROELECTRONICSBASICS = "MicroelectronicsBasics"
    FLATSCREENTELEVISION = "FlatscreenTelevision"
    MOISTUREPUMP = "MoisturePump"
    HOSPITALBED = "HospitalBed"
    DEEPDRILLING = "DeepDrilling"
    GROUNDPENETRATINGSCANNER = "GroundPenetratingScanner"
    TRANSPORTPOD = "TransportPod"
    MEDICINEPRODUCTION = "MedicineProduction"
    LONGRANGEMINERALSCANNER = "LongRangeMineralScanner"
    SHIELDBELT = "ShieldBelt"
    PRECISIONRIFLING = "PrecisionRifling"
    HEAVYTURRETS = "HeavyTurrets"
    MULTIBARRELWEAPONS = "MultibarrelWeapons"
    MULTIANALYZER = "MultiAnalyzer"
    VITALSMONITOR = "VitalsMonitor"
    FABRICATION = "Fabrication"
    ADVANCEDFABRICATION = "AdvancedFabrication"
    CRYPTOSLEEP = "Cryptosleep"
    RECONARMOR = "ReconArmor"
    POWEREDARMOR = "PoweredArmor"
    CHARGEDSHOT = "ChargedShot"
    BIONICS = "Bionics"
    SNIPERTURRET = "SniperTurret"
    ROCKETSWARMLAUNCHER = "RocketswarmLauncher"
    SHIPBASICS = "ShipBasics"
    SHIPCRYPTOSLEEP = "ShipCryptosleep"
    SHIPREACTOR = "ShipReactor"
    SHIPENGINE = "ShipEngine"
    SHIPCOMPUTERCORE = "ShipComputerCore"
    SHIPSENSORCLUSTER = "ShipSensorCluster"
    BASICMECHTECH = "BasicMechtech"
    STANDARDMECHTECH = "StandardMechtech"
    HIGHMECHTECH = "HighMechtech"
    ULTRAMECHTECH = "UltraMechtech"
    WASTEPACKATOMIZER = "WastepackAtomizer"
    TOXIFIERGENERATOR = "ToxifierGenerator"
    XENOGERMINATION = "Xenogermination"
    GENEPROCESSOR = "GeneProcessor"
    ARCHOGENETICS = "Archogenetics"
    DEATHREST = "Deathrest"
    FERTILITYPROCEDURES = "FertilityProcedures"
    TOXGAS = "ToxGas"
    TOXFILTRATION = "ToxFiltration"
    GROWTHVATS = "GrowthVats"
    BIOSCULPTING = "Biosculpting"
    BIOREGENERATION = "Bioregeneration"
    NEURALSUPERCHARGER = "NeuralSupercharger"
    NOBLEAPPAREL = "NobleApparel"
    ROYALAPPAREL = "RoyalApparel"
    CATAPHRACTARMOR = "CataphractArmor"
    JUMPPACK = "JumpPack"
    GUNLINK = "Gunlink"
    BRAINWIRING = "BrainWiring"
    SPECIALIZEDLIMBS = "SpecializedLimbs"
    COMPACTWEAPONRY = "CompactWeaponry"
    VENOMSYNTHESIS = "VenomSynthesis"
    ARTIFICIALMETABOLISM = "ArtificialMetabolism"
    NEURALCOMPUTATION = "NeuralComputation"
    SKINHARDENING = "SkinHardening"
    HEALINGFACTORS = "HealingFactors"
    FLESHSHAPING = "FleshShaping"
    MOLECULARANALYSIS = "MolecularAnalysis"
    CIRCADIANINFLUENCE = "CircadianInfluence"
    HARP = "Harp"
    HARPSICHORD = "Harpsichord"
    PIANO = "Piano"

class ScenarioStartingTech:
    CRASHLANDED = [
        Researches.PASSIVECOOLER, 
        Researches.STONECUTTING,
        Researches.COMPLEXCLOTHING,
        Researches.COMPLEXFURNITURE,
        Researches.ELECTRICITY,
        Researches.AIRCONDITIONING,
        Researches.NUTRIENTPASTE]
    LOSTTRIBE = [
        Researches.TREESOWING,
        Researches.RECURVEBOW,
        Researches.PSYCHOIDBREWING,
        Researches.PASSIVECOOLER,
        Researches.PEMMICAN
    ]
    RICHEXPLORER = [
        Researches.PASSIVECOOLER,
        Researches.STONECUTTING,
        Researches.COMPLEXCLOTHING,
        Researches.SMITHING,
        Researches.COMPLEXFURNITURE,
        Researches.ELECTRICITY,
        Researches.AIRCONDITIONING,
        Researches.MACHINING,
        Researches.GUNSMITHING,
        Researches.NUTRIENTPASTE,
        Researches.BLOWBACKOPERATION,
        Researches.GUNTURRETS
    ]
    NAKEDBRUTALITY = [
        Researches.PASSIVECOOLER,
        Researches.STONECUTTING,
        Researches.COMPLEXCLOTHING,
        Researches.COMPLEXFURNITURE,
        Researches.ELECTRICITY,
        Researches.AIRCONDITIONING,
        Researches.NUTRIENTPASTE
    ]
    MECHANITOR = [
        Researches.PASSIVECOOLER, 
        Researches.STONECUTTING,
        Researches.COMPLEXCLOTHING,
        Researches.COMPLEXFURNITURE,
        Researches.ELECTRICITY,
        Researches.AIRCONDITIONING,
        Researches.NUTRIENTPASTE,
        Researches.MICROELECTRONICSBASICS,
        Researches.BASICMECHTECH,
        Researches.BATTERIES
    ]
    SANGUOPHAGE = [
        Researches.PASSIVECOOLER, 
        Researches.STONECUTTING,
        Researches.COMPLEXCLOTHING,
        Researches.COMPLEXFURNITURE,
        Researches.ELECTRICITY,
        Researches.AIRCONDITIONING,
        Researches.NUTRIENTPASTE,
        Researches.DEATHREST
    ]

starting_tech_dict = {
    StartingScenario.option_crash_landed: ScenarioStartingTech.CRASHLANDED,
    StartingScenario.option_lost_tribe: ScenarioStartingTech.LOSTTRIBE,
    StartingScenario.option_lost_tribe_early_power: ScenarioStartingTech.LOSTTRIBE,
    StartingScenario.option_mechanitor: ScenarioStartingTech.MECHANITOR,
    StartingScenario.option_naked_brutality: ScenarioStartingTech.NAKEDBRUTALITY,
    StartingScenario.option_rich_explorer: ScenarioStartingTech.RICHEXPLORER,
    StartingScenario.option_sanguophage: ScenarioStartingTech.SANGUOPHAGE
}