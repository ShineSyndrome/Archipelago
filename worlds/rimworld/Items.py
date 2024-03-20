from typing import Dict, NamedTuple, Optional, Callable

from BaseClasses import Item, ItemClassification
from .data.research import *
from .data.research_items import *
from .constants import Items, Researches, Expansions

class RimWorldItem(Item):
    game: str = "RimWorld"

class RimWorldItemData(NamedTuple):
    defName: str
    label: str
    category: str
    expansion: str
    classification: ItemClassification = ItemClassification.filler

core_research_items: Dict[int, RimWorldItemData] = {
    1001: RimWorldItem(Researches.PSYCHOIDBREWING, 'research: psychoid brewing', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1002: RimWorldItem(Researches.TREESOWING, 'research: tree sowing', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1003: RimWorldItem(Researches.BREWING, 'research: brewing', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1004: RimWorldItem(Researches.COMPLEXFURNITURE, 'research: complex furniture', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1005: RimWorldItem(Researches.PASSIVECOOLER, 'research: passive cooler', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1006: RimWorldItem(Researches.STONECUTTING, 'research: stonecutting', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1007: RimWorldItem(Researches.COMPLEXCLOTHING, 'research: complex clothing', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),    
    1008: RimWorldItem(Researches.DRUGPRODUCTION, 'research: drug production', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1009: RimWorldItem(Researches.COCOA, 'research: cocoa', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1010: RimWorldItem(Researches.DEVILSTRAND, 'research: devil strand', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1011: RimWorldItem(Researches.CARPETMAKING, 'research: carpet making', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.filler),
    1012: RimWorldItem(Researches.PEMMICAN, 'research: pemmican', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1013: RimWorldItem(Researches.SMITHING, 'research: smithing', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1014: RimWorldItem(Researches.RECURVEBOW, 'research: recurve bow', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1015: RimWorldItem(Researches.PSYCHITEREFINING, 'research: psychite brewing', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1016: RimWorldItem(Researches.WAKEUPPRODUCTION, 'research: wake-up production', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1017: RimWorldItem(Researches.GOJUICEPRODUCTION, 'research: go-juice production', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1018: RimWorldItem(Researches.PENOXYCYLINEPRODUCTION, 'research: penoxycyline production', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1019: RimWorldItem(Researches.LONGBLADES, 'research: long blades', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1020: RimWorldItem(Researches.PLATEARMOR, 'research: plate armor', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1021: RimWorldItem(Researches.GREATBOW, 'research: greatbow', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1022: RimWorldItem(Researches.ELECTRICITY, 'research: electricity', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.progression),
    1023: RimWorldItem(Researches.BATTERIES, 'research: battery', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1024: RimWorldItem(Researches.BIOFUELREFINING, 'research: biofuel refining', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1025: RimWorldItem(Researches.WATERMILLGENERATOR, 'research: watermill generator', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1026: RimWorldItem(Researches.NUTRIENTPASTE, 'research: nutrient paste', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1027: RimWorldItem(Researches.SOLARPANELS, 'research: solar panels', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1028: RimWorldItem(Researches.AIRCONDITIONING, 'research: air conditioning', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1029: RimWorldItem(Researches.AUTODOORS, 'research: autodoor', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.filler),
    1030: RimWorldItem(Researches.HYDROPONICS, 'research: hydroponics', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1031: RimWorldItem(Researches.TUBETELEVISION, 'research: tube televison', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.filler),
    1032: RimWorldItem(Researches.PACKAGEDSURVIVALMEAL, 'research: packaged survival meal', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1033: RimWorldItem(Researches.FIREFOAM, 'research: firefoam', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1034: RimWorldItem(Researches.IEDS, 'research: IEDs', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1035: RimWorldItem(Researches.GEOTHERMALPOWER, 'research: geothermal power', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1036: RimWorldItem(Researches.STERILEMATERIALS, 'research: sterile materials', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1037: RimWorldItem(Researches.COLOREDLIGHTS, 'research: advanced lights', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1038: RimWorldItem(Researches.MACHINING, 'research: machining', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1039: RimWorldItem(Researches.SMOKEPOPBELT, 'research: smokepop packs', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1040: RimWorldItem(Researches.PROSTHETICS, 'research: prosthetics', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1041: RimWorldItem(Researches.GUNSMITHING, 'research: gunsmithing', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1042: RimWorldItem(Researches.FLAKARMOR, 'research: flak armor', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1043: RimWorldItem(Researches.MORTARS, 'research: mortars', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1044: RimWorldItem(Researches.BLOWBACKOPERATION, 'research: blowback operation', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1045: RimWorldItem(Researches.GASOPERATION, 'research: gas operation', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1046: RimWorldItem(Researches.GUNTURRETS, 'research: gun turrets', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1047: RimWorldItem(Researches.FOAMTURRET, 'research: foam turret', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.filler),
    1048: RimWorldItem(Researches.MICROELECTRONICSBASICS, 'research: microelectronics', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.progression),
    1049: RimWorldItem(Researches.FLATSCREENTELEVISION, 'research: flatscreen television', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.filler),
    1050: RimWorldItem(Researches.MOISTUREPUMP, 'research: moisture pump', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.filler),
    1051: RimWorldItem(Researches.HOSPITALBED, 'research: hospital bed', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1052: RimWorldItem(Researches.DEEPDRILLING, 'research: deep drilling', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1053: RimWorldItem(Researches.GROUNDPENETRATINGSCANNER, 'research: ground-penetrating scanner', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1054: RimWorldItem(Researches.TRANSPORTPOD, 'research: transport pod', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1055: RimWorldItem(Researches.MEDICINEPRODUCTION, 'research: medicine production', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1056: RimWorldItem(Researches.LONGRANGEMINERALSCANNER, 'research: long-range mineral scanner', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1057: RimWorldItem(Researches.SHIELDBELT, 'research: shields', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1058: RimWorldItem(Researches.PRECISIONRIFLING, 'research: precision rifling', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1059: RimWorldItem(Researches.HEAVYTURRETS, 'research: autocannon turret', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1060: RimWorldItem(Researches.MULTIBARRELWEAPONS, 'research: multibarrel weapons', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1061: RimWorldItem(Researches.MULTIANALYZER, 'research: multi-analyzer', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.progression),
    1062: RimWorldItem(Researches.VITALSMONITOR, 'research: vitals monitor', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1063: RimWorldItem(Researches.FABRICATION, 'research: fabrication', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful), 
    1064: RimWorldItem(Researches.ADVANCEDFABRICATION, 'research: advanced fabrication', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1065: RimWorldItem(Researches.CRYPTOSLEEP, 'research: cryptosleep casket', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1066: RimWorldItem(Researches.RECONARMOR, 'research: recon armor', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1067: RimWorldItem(Researches.POWEREDARMOR, 'research: marine armor', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1068: RimWorldItem(Researches.CHARGEDSHOT, 'research: pulse-charged munitions', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1069: RimWorldItem(Researches.BIONICS, 'research: bionics', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1070: RimWorldItem(Researches.SNIPERTURRET, 'research: uranium slug turret', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1071: RimWorldItem(Researches.ROCKETSWARMLAUNCHER, 'research: rocketswarm launcher', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.useful),
    1072: RimWorldItem(Researches.SHIPBASICS, 'research: starflight basics', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.progression),
    1073: RimWorldItem(Researches.SHIPCRYPTOSLEEP, 'research: vacuum cryptosleep casket', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.progression),
    1074: RimWorldItem(Researches.SHIPREACTOR, 'research: starship reactor', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.progression),
    1075: RimWorldItem(Researches.SHIPENGINE, 'research: Johnson-Tanaka drive', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.progression),
    1076: RimWorldItem(Researches.SHIPCOMPUTERCORE, 'research: machine persuasion', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.progression),
    1077: RimWorldItem(Researches.SHIPSENSORCLUSTER, 'research: starflight sensors', Items.Categories.RESEARCH, Expansions.CORE, ItemClassification.progression),                        
}

biotech_research_items: Dict[int, RimWorldItemData] = {
    1078: RimWorldItem(Researches.BASICMECHTECH, 'research: basic mechtech', Items.Categories.RESEARCH, Expansions.BIOTECH, ItemClassification.useful),
    1079: RimWorldItem(Researches.STANDARDMECHTECH, 'research: standard mechtech', Items.Categories.RESEARCH, Expansions.BIOTECH, ItemClassification.useful),
    1080: RimWorldItem(Researches.HIGHMECHTECH, 'research: high mechtech', Items.Categories.RESEARCH, Expansions.BIOTECH, ItemClassification.useful),
    1081: RimWorldItem(Researches.ULTRAMECHTECH, 'research: ultra mechtech', Items.Categories.RESEARCH, Expansions.BIOTECH, ItemClassification.useful),
    1082: RimWorldItem(Researches.WASTEPACKATOMIZER, 'research: wastepack atomizer', Items.Categories.RESEARCH, Expansions.BIOTECH, ItemClassification.useful),
    1083: RimWorldItem(Researches.TOXIFIERGENERATOR, 'research: toxifier generator', Items.Categories.RESEARCH, Expansions.BIOTECH, ItemClassification.useful),
    1084: RimWorldItem(Researches.XENOGERMINATION, 'research: xenogenetics', Items.Categories.RESEARCH, Expansions.BIOTECH, ItemClassification.useful),
    1085: RimWorldItem(Researches.GENEPROCESSOR, 'research: gene processor', Items.Categories.RESEARCH, Expansions.BIOTECH, ItemClassification.useful),
    1086: RimWorldItem(Researches.ARCHOGENETICS, 'research: archogenetics', Items.Categories.RESEARCH, Expansions.BIOTECH, ItemClassification.useful),
    1087: RimWorldItem(Researches.DEATHREST, 'research: deathrest', Items.Categories.RESEARCH, Expansions.BIOTECH, ItemClassification.useful),
    1088: RimWorldItem(Researches.FERTILITYPROCEDURES, 'research: fertility procedures', Items.Categories.RESEARCH, Expansions.BIOTECH, ItemClassification.useful),
    1089: RimWorldItem(Researches.TOXGAS, 'research: tox gas', Items.Categories.RESEARCH, Expansions.BIOTECH, ItemClassification.useful),
    1090: RimWorldItem(Researches.TOXFILTRATION, 'research: toxin filtration', Items.Categories.RESEARCH, Expansions.BIOTECH, ItemClassification.useful),
    1091: RimWorldItem(Researches.GROWTHVATS, 'research: growth vats', Items.Categories.RESEARCH, Expansions.BIOTECH, ItemClassification.useful),                
}

ideology_research_items: Dict[int, RimWorldItemData] = {
    1092: RimWorldItem(Researches.BIOSCULPTING, 'research: biosculpting', Items.Categories.RESEARCH, Expansions.IDEOLOGY, ItemClassification.useful),
    1093: RimWorldItem(Researches.BIOREGENERATION, 'research: bioregeneration', Items.Categories.RESEARCH, Expansions.IDEOLOGY, ItemClassification.useful),
    1094: RimWorldItem(Researches.NEURALSUPERCHARGER, 'research: neural supercharger', Items.Categories.RESEARCH, Expansions.IDEOLOGY, ItemClassification.useful),
}

royalty_research_items: Dict[int, RimWorldItemData] = {
    1095: RimWorldItem(Researches.NOBLEAPPAREL, 'research: noble apparel', Items.Categories.RESEARCH, Expansions.ROYALTY, ItemClassification.filler),
    1096: RimWorldItem(Researches.ROYALAPPAREL, 'research: royal apparel', Items.Categories.RESEARCH, Expansions.ROYALTY, ItemClassification.filler),
    1097: RimWorldItem(Researches.CATAPHRACTARMOR, 'research: cataphract armor', Items.Categories.RESEARCH, Expansions.ROYALTY, ItemClassification.useful),
    1098: RimWorldItem(Researches.JUMPPACK, 'research: jump packs', Items.Categories.RESEARCH, Expansions.ROYALTY, ItemClassification.useful),
    1099: RimWorldItem(Researches.GUNLINK, 'research: gun link', Items.Categories.RESEARCH, Expansions.ROYALTY, ItemClassification.useful),
    1100: RimWorldItem(Researches.BRAINWIRING, 'research: brain wiring', Items.Categories.RESEARCH, Expansions.ROYALTY, ItemClassification.useful),
    1101: RimWorldItem(Researches.SPECIALIZEDLIMBS, 'research: specialized limbs', Items.Categories.RESEARCH, Expansions.ROYALTY, ItemClassification.useful),
    1102: RimWorldItem(Researches.COMPACTWEAPONRY, 'research: compact weaponry', Items.Categories.RESEARCH, Expansions.ROYALTY, ItemClassification.useful),
    1103: RimWorldItem(Researches.VENOMSYNTHESIS, 'research: poison synthesis', Items.Categories.RESEARCH, Expansions.ROYALTY, ItemClassification.useful),
    1104: RimWorldItem(Researches.ARTIFICIALMETABOLISM, 'research: artificial metabolism', Items.Categories.RESEARCH, Expansions.ROYALTY, ItemClassification.useful),
    1105: RimWorldItem(Researches.NEURALCOMPUTATION, 'research: neural computation', Items.Categories.RESEARCH, Expansions.ROYALTY, ItemClassification.useful),
    1106: RimWorldItem(Researches.SKINHARDENING, 'research: skin hardening', Items.Categories.RESEARCH, Expansions.ROYALTY, ItemClassification.useful),
    1107: RimWorldItem(Researches.HEALINGFACTORS, 'research: healing factors', Items.Categories.RESEARCH, Expansions.ROYALTY, ItemClassification.useful),
    1108: RimWorldItem(Researches.FLESHSHAPING, 'research: flesh shaping', Items.Categories.RESEARCH, Expansions.ROYALTY, ItemClassification.useful),
    1109: RimWorldItem(Researches.MOLECULARANALYSIS, 'research: molecular analysis', Items.Categories.RESEARCH, Expansions.ROYALTY, ItemClassification.useful),
    1110: RimWorldItem(Researches.CIRCADIANINFLUENCE, 'research: circadian influence', Items.Categories.RESEARCH, Expansions.ROYALTY, ItemClassification.useful),
    1111: RimWorldItem(Researches.HARP, 'research: harp', Items.Categories.RESEARCH, Expansions.ROYALTY, ItemClassification.filler),
    1112: RimWorldItem(Researches.HARPSICHORD, 'research: harpsichord', Items.Categories.RESEARCH, Expansions.ROYALTY, ItemClassification.filler),
    1113: RimWorldItem(Researches.PIANO, 'research: neural computation', Items.Categories.RESEARCH, Expansions.ROYALTY, ItemClassification.filler),
}
