from typing import Dict, NamedTuple
from BaseClasses import Item, ItemClassification, MultiWorld
from .options import RimWorldOptions
from .constants import *


class RimWorldItem(Item):
    game: str = "RimWorld"


class RimWorldItemData(NamedTuple):
    defName: str
    label: str
    category: str
    expansion: str
    classification: ItemClassification = ItemClassification.filler

    def identifier(self) -> str:
        return f"{self.category}: {self.defName}"


def create_items(multiworld: MultiWorld, player: int, options: RimWorldOptions):
    research_item_data = core_research_items
    if options.biotech_expansion:
        research_item_data.update(biotech_research_items)
    if options.royalty_expansion:
        research_item_data.update(royalty_research_items)
    if options.ideology_expansion:
        research_item_data.update(ideology_research_items)

    research_items = [RimWorldItem(item.identifier(), item.classification, key, player) for key, item in
                      research_item_data.items()]
    research_items = [item for item in research_items if item not in starting_tech_dict[options.starting_scenario]]

    for item in research_items:
        multiworld.itempool.append(item)


def create_item(item_name: str, player: int) -> RimWorldItem:
    item_id = all_items_name_to_id[item_name]
    item_data = all_items[item_id]

    return RimWorldItem(item_data.identifier(), item_data.classification, item_id, player)


# Potential progressive items
electricity_research_item = RimWorldItemData(Researches.ELECTRICITY, 'research: electricity', Items.Categories.RESEARCH,
                                             Expansions.CORE, ItemClassification.progression)
micro_electronics_research_item = RimWorldItemData(Researches.MICROELECTRONICSBASICS, 'research: microelectronics',
                                                   Items.Categories.RESEARCH, Expansions.CORE,
                                                   ItemClassification.progression)
multi_analyzer_research_item = RimWorldItemData(Researches.MULTIANALYZER, 'research: multi-analyzer',
                                                Items.Categories.RESEARCH, Expansions.CORE,
                                                ItemClassification.progression)
ship_basics_research_item = RimWorldItemData(Researches.SHIPBASICS, 'research: starflight basics',
                                             Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.progression)
ship_crypto_sleep_research_item = RimWorldItemData(Researches.SHIPCRYPTOSLEEP, 'research: vacuum cryptosleep casket',
                                                   Items.Categories.RESEARCH, Expansions.CORE,
                                                   ItemClassification.progression)
ship_reactor_research_item = RimWorldItemData(Researches.SHIPREACTOR, 'research: starship reactor',
                                              Items.Categories.RESEARCH, Expansions.CORE,
                                              ItemClassification.progression)
ship_engine_research_item = RimWorldItemData(Researches.SHIPENGINE, 'research: Johnson-Tanaka drive',
                                             Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.progression)
ship_computer_core_research_item = RimWorldItemData(Researches.SHIPCOMPUTERCORE, 'research: machine persuasion',
                                                    Items.Categories.RESEARCH, Expansions.CORE,
                                                    ItemClassification.progression)
ship_sensor_research_item = RimWorldItemData(Researches.SHIPSENSORCLUSTER, 'research: starflight sensors',
                                             Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.progression)

core_research_items: Dict[int, RimWorldItemData] = {
    1001: RimWorldItemData(Researches.PSYCHOIDBREWING, 'research: psychoid brewing', Items.Categories.RESEARCH,
                           Expansions.CORE, ItemClassification.useful),
    1002: RimWorldItemData(Researches.TREESOWING, 'research: tree sowing', Items.Categories.RESEARCH, Expansions.CORE,
                           ItemClassification.useful),
    1003: RimWorldItemData(Researches.BREWING, 'research: brewing', Items.Categories.RESEARCH, Expansions.CORE,
                           ItemClassification.useful),
    1004: RimWorldItemData(Researches.COMPLEXFURNITURE, 'research: complex furniture', Items.Categories.RESEARCH,
                           Expansions.CORE, ItemClassification.useful),
    1005: RimWorldItemData(Researches.PASSIVECOOLER, 'research: passive cooler', Items.Categories.RESEARCH,
                           Expansions.CORE, ItemClassification.useful),
    1006: RimWorldItemData(Researches.STONECUTTING, 'research: stonecutting', Items.Categories.RESEARCH,
                           Expansions.CORE, ItemClassification.useful),
    1007: RimWorldItemData(Researches.COMPLEXCLOTHING, 'research: complex clothing', Items.Categories.RESEARCH,
                           Expansions.CORE, ItemClassification.useful),
    1008: RimWorldItemData(Researches.DRUGPRODUCTION, 'research: drug production', Items.Categories.RESEARCH,
                           Expansions.CORE, ItemClassification.useful),
    1009: RimWorldItemData(Researches.COCOA, 'research: cocoa', Items.Categories.RESEARCH, Expansions.CORE,
                           ItemClassification.useful),
    1010: RimWorldItemData(Researches.DEVILSTRAND, 'research: devil strand', Items.Categories.RESEARCH, Expansions.CORE,
                           ItemClassification.useful),
    1011: RimWorldItemData(Researches.CARPETMAKING, 'research: carpet making', Items.Categories.RESEARCH,
                           Expansions.CORE, ItemClassification.filler),
    1012: RimWorldItemData(Researches.PEMMICAN, 'research: pemmican', Items.Categories.RESEARCH, Expansions.CORE,
                           ItemClassification.useful),
    1013: RimWorldItemData(Researches.SMITHING, 'research: smithing', Items.Categories.RESEARCH, Expansions.CORE,
                           ItemClassification.useful),
    1014: RimWorldItemData(Researches.RECURVEBOW, 'research: recurve bow', Items.Categories.RESEARCH, Expansions.CORE,
                           ItemClassification.useful),
    1015: RimWorldItemData(Researches.PSYCHITEREFINING, 'research: psychite brewing', Items.Categories.RESEARCH,
                           Expansions.CORE, ItemClassification.useful),
    1016: RimWorldItemData(Researches.WAKEUPPRODUCTION, 'research: wake-up production', Items.Categories.RESEARCH,
                           Expansions.CORE, ItemClassification.useful),
    1017: RimWorldItemData(Researches.GOJUICEPRODUCTION, 'research: go-juice production', Items.Categories.RESEARCH,
                           Expansions.CORE, ItemClassification.useful),
    1018: RimWorldItemData(Researches.PENOXYCYLINEPRODUCTION, 'research: penoxycyline production',
                           Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1019: RimWorldItemData(Researches.LONGBLADES, 'research: long blades', Items.Categories.RESEARCH, Expansions.CORE,
                           ItemClassification.useful),
    1020: RimWorldItemData(Researches.PLATEARMOR, 'research: plate armor', Items.Categories.RESEARCH, Expansions.CORE,
                           ItemClassification.useful),
    1021: RimWorldItemData(Researches.GREATBOW, 'research: greatbow', Items.Categories.RESEARCH, Expansions.CORE,
                           ItemClassification.useful),
    1022: electricity_research_item,
    1023: RimWorldItemData(Researches.BATTERIES, 'research: battery', Items.Categories.RESEARCH, Expansions.CORE,
                           ItemClassification.useful),
    1024: RimWorldItemData(Researches.BIOFUELREFINING, 'research: biofuel refining', Items.Categories.RESEARCH,
                           Expansions.CORE, ItemClassification.useful),
    1025: RimWorldItemData(Researches.WATERMILLGENERATOR, 'research: watermill generator', Items.Categories.RESEARCH,
                           Expansions.CORE, ItemClassification.useful),
    1026: RimWorldItemData(Researches.NUTRIENTPASTE, 'research: nutrient paste', Items.Categories.RESEARCH,
                           Expansions.CORE, ItemClassification.useful),
    1027: RimWorldItemData(Researches.SOLARPANELS, 'research: solar panels', Items.Categories.RESEARCH, Expansions.CORE,
                           ItemClassification.useful),
    1028: RimWorldItemData(Researches.AIRCONDITIONING, 'research: air conditioning', Items.Categories.RESEARCH,
                           Expansions.CORE, ItemClassification.useful),
    1029: RimWorldItemData(Researches.AUTODOORS, 'research: autodoor', Items.Categories.RESEARCH, Expansions.CORE,
                           ItemClassification.filler),
    1030: RimWorldItemData(Researches.HYDROPONICS, 'research: hydroponics', Items.Categories.RESEARCH, Expansions.CORE,
                           ItemClassification.useful),
    1031: RimWorldItemData(Researches.TUBETELEVISION, 'research: tube televison', Items.Categories.RESEARCH,
                           Expansions.CORE, ItemClassification.filler),
    1032: RimWorldItemData(Researches.PACKAGEDSURVIVALMEAL, 'research: packaged survival meal',
                           Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1033: RimWorldItemData(Researches.FIREFOAM, 'research: firefoam', Items.Categories.RESEARCH, Expansions.CORE,
                           ItemClassification.useful),
    1034: RimWorldItemData(Researches.IEDS, 'research: IEDs', Items.Categories.RESEARCH, Expansions.CORE,
                           ItemClassification.useful),
    1035: RimWorldItemData(Researches.GEOTHERMALPOWER, 'research: geothermal power', Items.Categories.RESEARCH,
                           Expansions.CORE, ItemClassification.useful),
    1036: RimWorldItemData(Researches.STERILEMATERIALS, 'research: sterile materials', Items.Categories.RESEARCH,
                           Expansions.CORE, ItemClassification.useful),
    1037: RimWorldItemData(Researches.COLOREDLIGHTS, 'research: advanced lights', Items.Categories.RESEARCH,
                           Expansions.CORE, ItemClassification.useful),
    1038: RimWorldItemData(Researches.MACHINING, 'research: machining', Items.Categories.RESEARCH, Expansions.CORE,
                           ItemClassification.useful),
    1039: RimWorldItemData(Researches.SMOKEPOPBELT, 'research: smokepop packs', Items.Categories.RESEARCH,
                           Expansions.CORE, ItemClassification.useful),
    1040: RimWorldItemData(Researches.PROSTHETICS, 'research: prosthetics', Items.Categories.RESEARCH, Expansions.CORE,
                           ItemClassification.useful),
    1041: RimWorldItemData(Researches.GUNSMITHING, 'research: gunsmithing', Items.Categories.RESEARCH, Expansions.CORE,
                           ItemClassification.useful),
    1042: RimWorldItemData(Researches.FLAKARMOR, 'research: flak armor', Items.Categories.RESEARCH, Expansions.CORE,
                           ItemClassification.useful),
    1043: RimWorldItemData(Researches.MORTARS, 'research: mortars', Items.Categories.RESEARCH, Expansions.CORE,
                           ItemClassification.useful),
    1044: RimWorldItemData(Researches.BLOWBACKOPERATION, 'research: blowback operation', Items.Categories.RESEARCH,
                           Expansions.CORE, ItemClassification.useful),
    1045: RimWorldItemData(Researches.GASOPERATION, 'research: gas operation', Items.Categories.RESEARCH,
                           Expansions.CORE, ItemClassification.useful),
    1046: RimWorldItemData(Researches.GUNTURRETS, 'research: gun turrets', Items.Categories.RESEARCH, Expansions.CORE,
                           ItemClassification.useful),
    1047: RimWorldItemData(Researches.FOAMTURRET, 'research: foam turret', Items.Categories.RESEARCH, Expansions.CORE,
                           ItemClassification.filler),
    1048: micro_electronics_research_item,
    1049: RimWorldItemData(Researches.FLATSCREENTELEVISION, 'research: flatscreen television',
                           Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.filler),
    1050: RimWorldItemData(Researches.MOISTUREPUMP, 'research: moisture pump', Items.Categories.RESEARCH,
                           Expansions.CORE, ItemClassification.filler),
    1051: RimWorldItemData(Researches.HOSPITALBED, 'research: hospital bed', Items.Categories.RESEARCH, Expansions.CORE,
                           ItemClassification.useful),
    1052: RimWorldItemData(Researches.DEEPDRILLING, 'research: deep drilling', Items.Categories.RESEARCH,
                           Expansions.CORE, ItemClassification.useful),
    1053: RimWorldItemData(Researches.GROUNDPENETRATINGSCANNER, 'research: ground-penetrating scanner',
                           Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1054: RimWorldItemData(Researches.TRANSPORTPOD, 'research: transport pod', Items.Categories.RESEARCH,
                           Expansions.CORE, ItemClassification.useful),
    1055: RimWorldItemData(Researches.MEDICINEPRODUCTION, 'research: medicine production', Items.Categories.RESEARCH,
                           Expansions.CORE, ItemClassification.useful),
    1056: RimWorldItemData(Researches.LONGRANGEMINERALSCANNER, 'research: long-range mineral scanner',
                           Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1057: RimWorldItemData(Researches.SHIELDBELT, 'research: shields', Items.Categories.RESEARCH, Expansions.CORE,
                           ItemClassification.useful),
    1058: RimWorldItemData(Researches.PRECISIONRIFLING, 'research: precision rifling', Items.Categories.RESEARCH,
                           Expansions.CORE, ItemClassification.useful),
    1059: RimWorldItemData(Researches.HEAVYTURRETS, 'research: autocannon turret', Items.Categories.RESEARCH,
                           Expansions.CORE, ItemClassification.useful),
    1060: RimWorldItemData(Researches.MULTIBARRELWEAPONS, 'research: multibarrel weapons', Items.Categories.RESEARCH,
                           Expansions.CORE, ItemClassification.useful),
    1061: multi_analyzer_research_item,
    1062: RimWorldItemData(Researches.VITALSMONITOR, 'research: vitals monitor', Items.Categories.RESEARCH,
                           Expansions.CORE, ItemClassification.useful),
    1063: RimWorldItemData(Researches.FABRICATION, 'research: fabrication', Items.Categories.RESEARCH, Expansions.CORE,
                           ItemClassification.useful),
    1064: RimWorldItemData(Researches.ADVANCEDFABRICATION, 'research: advanced fabrication', Items.Categories.RESEARCH,
                           Expansions.CORE, ItemClassification.useful),
    1065: RimWorldItemData(Researches.CRYPTOSLEEP, 'research: cryptosleep casket', Items.Categories.RESEARCH,
                           Expansions.CORE, ItemClassification.useful),
    1066: RimWorldItemData(Researches.RECONARMOR, 'research: recon armor', Items.Categories.RESEARCH, Expansions.CORE,
                           ItemClassification.useful),
    1067: RimWorldItemData(Researches.POWEREDARMOR, 'research: marine armor', Items.Categories.RESEARCH,
                           Expansions.CORE, ItemClassification.useful),
    1068: RimWorldItemData(Researches.CHARGEDSHOT, 'research: pulse-charged munitions', Items.Categories.RESEARCH,
                           Expansions.CORE, ItemClassification.useful),
    1069: RimWorldItemData(Researches.BIONICS, 'research: bionics', Items.Categories.RESEARCH, Expansions.CORE,
                           ItemClassification.useful),
    1070: RimWorldItemData(Researches.SNIPERTURRET, 'research: uranium slug turret', Items.Categories.RESEARCH,
                           Expansions.CORE, ItemClassification.useful),
    1071: RimWorldItemData(Researches.ROCKETSWARMLAUNCHER, 'research: rocketswarm launcher', Items.Categories.RESEARCH,
                           Expansions.CORE, ItemClassification.useful),
    1072: ship_basics_research_item,
    1073: ship_crypto_sleep_research_item,
    1074: ship_reactor_research_item,
    1075: ship_engine_research_item,
    1076: ship_computer_core_research_item,
    1077: ship_sensor_research_item,
}

biotech_research_items: Dict[int, RimWorldItemData] = {
    1078: RimWorldItemData(Researches.BASICMECHTECH, 'research: basic mechtech', Items.Categories.RESEARCH,
                           Expansions.BIOTECH, ItemClassification.useful),
    1079: RimWorldItemData(Researches.STANDARDMECHTECH, 'research: standard mechtech', Items.Categories.RESEARCH,
                           Expansions.BIOTECH, ItemClassification.useful),
    1080: RimWorldItemData(Researches.HIGHMECHTECH, 'research: high mechtech', Items.Categories.RESEARCH,
                           Expansions.BIOTECH, ItemClassification.useful),
    1081: RimWorldItemData(Researches.ULTRAMECHTECH, 'research: ultra mechtech', Items.Categories.RESEARCH,
                           Expansions.BIOTECH, ItemClassification.useful),
    1082: RimWorldItemData(Researches.WASTEPACKATOMIZER, 'research: wastepack atomizer', Items.Categories.RESEARCH,
                           Expansions.BIOTECH, ItemClassification.useful),
    1083: RimWorldItemData(Researches.TOXIFIERGENERATOR, 'research: toxifier generator', Items.Categories.RESEARCH,
                           Expansions.BIOTECH, ItemClassification.useful),
    1084: RimWorldItemData(Researches.XENOGERMINATION, 'research: xenogenetics', Items.Categories.RESEARCH,
                           Expansions.BIOTECH, ItemClassification.useful),
    1085: RimWorldItemData(Researches.GENEPROCESSOR, 'research: gene processor', Items.Categories.RESEARCH,
                           Expansions.BIOTECH, ItemClassification.useful),
    1086: RimWorldItemData(Researches.ARCHOGENETICS, 'research: archogenetics', Items.Categories.RESEARCH,
                           Expansions.BIOTECH, ItemClassification.useful),
    1087: RimWorldItemData(Researches.DEATHREST, 'research: deathrest', Items.Categories.RESEARCH, Expansions.BIOTECH,
                           ItemClassification.useful),
    1088: RimWorldItemData(Researches.FERTILITYPROCEDURES, 'research: fertility procedures', Items.Categories.RESEARCH,
                           Expansions.BIOTECH, ItemClassification.useful),
    1089: RimWorldItemData(Researches.TOXGAS, 'research: tox gas', Items.Categories.RESEARCH, Expansions.BIOTECH,
                           ItemClassification.useful),
    1090: RimWorldItemData(Researches.TOXFILTRATION, 'research: toxin filtration', Items.Categories.RESEARCH,
                           Expansions.BIOTECH, ItemClassification.useful),
    1091: RimWorldItemData(Researches.GROWTHVATS, 'research: growth vats', Items.Categories.RESEARCH,
                           Expansions.BIOTECH, ItemClassification.useful),
}

ideology_research_items: Dict[int, RimWorldItemData] = {
    1092: RimWorldItemData(Researches.BIOSCULPTING, 'research: biosculpting', Items.Categories.RESEARCH,
                           Expansions.IDEOLOGY, ItemClassification.useful),
    1093: RimWorldItemData(Researches.BIOREGENERATION, 'research: bioregeneration', Items.Categories.RESEARCH,
                           Expansions.IDEOLOGY, ItemClassification.useful),
    1094: RimWorldItemData(Researches.NEURALSUPERCHARGER, 'research: neural supercharger', Items.Categories.RESEARCH,
                           Expansions.IDEOLOGY, ItemClassification.useful),
}

royalty_research_items: Dict[int, RimWorldItemData] = {
    1095: RimWorldItemData(Researches.NOBLEAPPAREL, 'research: noble apparel', Items.Categories.RESEARCH,
                           Expansions.ROYALTY, ItemClassification.filler),
    1096: RimWorldItemData(Researches.ROYALAPPAREL, 'research: royal apparel', Items.Categories.RESEARCH,
                           Expansions.ROYALTY, ItemClassification.filler),
    1097: RimWorldItemData(Researches.CATAPHRACTARMOR, 'research: cataphract armor', Items.Categories.RESEARCH,
                           Expansions.ROYALTY, ItemClassification.useful),
    1098: RimWorldItemData(Researches.JUMPPACK, 'research: jump packs', Items.Categories.RESEARCH, Expansions.ROYALTY,
                           ItemClassification.useful),
    1099: RimWorldItemData(Researches.GUNLINK, 'research: gun link', Items.Categories.RESEARCH, Expansions.ROYALTY,
                           ItemClassification.useful),
    1100: RimWorldItemData(Researches.BRAINWIRING, 'research: brain wiring', Items.Categories.RESEARCH,
                           Expansions.ROYALTY, ItemClassification.useful),
    1101: RimWorldItemData(Researches.SPECIALIZEDLIMBS, 'research: specialized limbs', Items.Categories.RESEARCH,
                           Expansions.ROYALTY, ItemClassification.useful),
    1102: RimWorldItemData(Researches.COMPACTWEAPONRY, 'research: compact weaponry', Items.Categories.RESEARCH,
                           Expansions.ROYALTY, ItemClassification.useful),
    1103: RimWorldItemData(Researches.VENOMSYNTHESIS, 'research: poison synthesis', Items.Categories.RESEARCH,
                           Expansions.ROYALTY, ItemClassification.useful),
    1104: RimWorldItemData(Researches.ARTIFICIALMETABOLISM, 'research: artificial metabolism',
                           Items.Categories.RESEARCH, Expansions.ROYALTY, ItemClassification.useful),
    1105: RimWorldItemData(Researches.NEURALCOMPUTATION, 'research: neural computation', Items.Categories.RESEARCH,
                           Expansions.ROYALTY, ItemClassification.useful),
    1106: RimWorldItemData(Researches.SKINHARDENING, 'research: skin hardening', Items.Categories.RESEARCH,
                           Expansions.ROYALTY, ItemClassification.useful),
    1107: RimWorldItemData(Researches.HEALINGFACTORS, 'research: healing factors', Items.Categories.RESEARCH,
                           Expansions.ROYALTY, ItemClassification.useful),
    1108: RimWorldItemData(Researches.FLESHSHAPING, 'research: flesh shaping', Items.Categories.RESEARCH,
                           Expansions.ROYALTY, ItemClassification.useful),
    1109: RimWorldItemData(Researches.MOLECULARANALYSIS, 'research: molecular analysis', Items.Categories.RESEARCH,
                           Expansions.ROYALTY, ItemClassification.useful),
    1110: RimWorldItemData(Researches.CIRCADIANINFLUENCE, 'research: circadian influence', Items.Categories.RESEARCH,
                           Expansions.ROYALTY, ItemClassification.useful),
    1111: RimWorldItemData(Researches.HARP, 'research: harp', Items.Categories.RESEARCH, Expansions.ROYALTY,
                           ItemClassification.filler),
    1112: RimWorldItemData(Researches.HARPSICHORD, 'research: harpsichord', Items.Categories.RESEARCH,
                           Expansions.ROYALTY, ItemClassification.filler),
    1113: RimWorldItemData(Researches.PIANO, 'research: neural computation', Items.Categories.RESEARCH,
                           Expansions.ROYALTY, ItemClassification.filler),
}

all_items: Dict[int, RimWorldItemData] = {**core_research_items, **biotech_research_items, **ideology_research_items,
                                          **royalty_research_items}

all_items_name_to_id = {value.identifier(): key for key, value in all_items.items()}
