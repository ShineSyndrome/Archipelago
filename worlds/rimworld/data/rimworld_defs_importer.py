'''
This is a standalone tool to import data from a RimWorld installation
Assuming the output data is already present, archipelago need not run this.
'''

from typing import Dict, NamedTuple, Optional
import xml.etree.ElementTree as ET
import xmltodict
import pprint

RimWorldPath = 'F:\SteamLibrary\steamapps\common\RimWorld'
CorePath = RimWorldPath + '\Data\Core\Defs\ResearchProjectDefs'
BiotechPath = RimWorldPath + '\Data\Biotech\Defs\ResearchProjectDefs'
IdeologyPath = RimWorldPath + '\Data\Ideology\Defs\ResearchProjectDefs'
RoyaltyPath = RimWorldPath + '\Data\Royalty\Defs\ResearchProjectDefs'


def readXml(path: str) -> dict:
    tree = ET.parse(path)
    xml_data = tree.getroot()
    xml_str = ET.tostring(xml_data, encoding='utf-8', method='xml')
    return dict(xmltodict.parse(xml_str))


def readResearchXml(path: str) -> list:
    return readXml(path)['Defs']['ResearchProjectDef']


researches = {
    'research_1': readResearchXml(CorePath + '\ResearchProjects_1.xml'),
    'research_2': readResearchXml(CorePath + '\ResearchProjects_2_Electricity.xml'),
    'research_3': readResearchXml(CorePath + '\ResearchProjects_3_Microelectronics.xml'),
    'research_4': readResearchXml(CorePath + '\ResearchProjects_4_MultiAnalyzer.xml'),
    'research_5': readResearchXml(CorePath + '\ResearchProjects_5_Ship.xml'),
    'research_biotech_mech': readResearchXml(BiotechPath + '\ResearchProjects_Mechanitor.xml'),
    'research_biotech_misc': readResearchXml(BiotechPath + '\ResearchProjects_Misc.xml'),
    'research_ideology': readResearchXml(IdeologyPath + '\ResearchProjects_Misc.xml'),
    'research_royalty_apparel': readResearchXml(RoyaltyPath + '\ResearchProjects_Apparel.xml'),
    'research_royalty_implants': readResearchXml(RoyaltyPath + '\ResearchProjects_Implants.xml'),
    'research_royalty_music': readResearchXml(RoyaltyPath + '\ResearchProjects_MusicalInstruments.xml'),
}
pp = pprint.PrettyPrinter(width=79, compact=False, sort_dicts=False)

def processParents(list: list[dict]):
    abstracts = {}
    # find abstracts
    for el in list:
        if '@Abstract' in el and el['@Abstract'] == 'True':
            abstracts[el['@Name']]= el

    # remove abstracts from original list
    list[:] = [x for x in list if '@Abstract' in el and el['@Abstract'] == 'True']

    # apply parents to abstracts to deal with nesting
    # (at least for a hierarchy 3 tall unless we repeat this)
    for k, v in abstracts.items():
        if '@ParentName' in v:
            parent = abstracts[v['@ParentName']]
            v.update({k:v for (k,v) in parent.items() if k[0] != '@'})

    # apply parents to non-abstract elements
    for el in list:
        if '@ParentName' in el:
            parent = abstracts[el['@ParentName']]
            el.update({k:v for (k,v) in parent.items() if k[0] != '@'})






output_file_name = 'research.py'


with open(output_file_name, 'w') as f:

    for key, value in researches.items():
        processParents(value)
        f.write('\n' + '#' * 79 + '\n# ' + str.upper(key) + '\n' + '#' * 79 + '\n')
        f.write(key + ' = {}'.format(pp.pformat(value)))
        f.write('\n\n')

