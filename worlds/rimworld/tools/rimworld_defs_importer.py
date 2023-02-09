'''
Please do not import this file in Archipelago code!

This is a standalone tool to import data from a RimWorld installation and
export to a more usable form in the archipelago/worlds/rimworld/data folder.
This script requires that all supported expansions and mods are installed.
'''

import pprint
import xml.etree.ElementTree as ET
from typing import Set

import xmltodict

# from worlds.rimworld import data

# change this to your rimworld installation path, the other relative paths should unchanged.
RimWorldPath = 'F:\\SteamLibrary\\steamapps\\common\\RimWorld'
CorePath = RimWorldPath + '\\Data\\Core\\Defs\\ResearchProjectDefs'
BiotechPath = RimWorldPath + '\\Data\\Biotech\\Defs\\ResearchProjectDefs'
IdeologyPath = RimWorldPath + '\\Data\\Ideology\\Defs\\ResearchProjectDefs'
RoyaltyPath = RimWorldPath + '\\Data\\Royalty\\Defs\\ResearchProjectDefs'


def read_xml(path: str) -> dict:
    tree = ET.parse(path)
    xml_data = tree.getroot()
    xml_str = ET.tostring(xml_data, encoding='utf-8', method='xml')
    return dict(xmltodict.parse(xml_str))


def read_research_xml(path: str) -> list:
    return read_xml(path)['Defs']['ResearchProjectDef']


def process_parents(list: list[dict]):
    abstracts = {}
    # find abstracts
    for el in list:
        if '@Abstract' in el and el['@Abstract'] == 'True':
            abstracts[el['@Name']] = el

    # get list without abstracts
    list = [x for x in list if '@Abstract' not in x or x['@Abstract'] != 'True']

    # apply parents to abstracts to deal with nesting
    # (at least for a hierarchy 3 tall unless we repeat this)
    for k, v in abstracts.items():
        if '@ParentName' in v:
            parent = abstracts[v['@ParentName']]
            v.update({k: v for (k, v) in parent.items() if k[0] != '@'})

    # apply parents to non-abstract elements
    for el in list:
        if '@ParentName' in el:
            parent = abstracts[el['@ParentName']]
            el.update({k: v for (k, v) in parent.items() if k[0] != '@'})

    return list


item_id: int = 1000

item_id_to_defName: dict[int, str] = {}

item_id_to_label: dict[int, str] = {}

label_to_item_id: dict[str, int] = {}

pp = pprint.PrettyPrinter(width=79, compact=False, sort_dicts=False)


def add_numeric_ids(list: list[dict]):
    global item_id
    for research in list:
        try:
            item_id += 1
            item_id_to_defName[item_id] = research['defName']
            item_id_to_label[item_id] = research['label']
            label_to_item_id[research['label']] = item_id
        except BaseException:
            pp.pprint(research)
            raise


def main():
    researches: dict[str:list] = {
        'research_1': read_research_xml(CorePath + '\\ResearchProjects_1.xml'),
        'research_2': read_research_xml(CorePath + '\\ResearchProjects_2_Electricity.xml'),
        'research_3': read_research_xml(CorePath + '\\ResearchProjects_3_Microelectronics.xml'),
        'research_4': read_research_xml(CorePath + '\\ResearchProjects_4_MultiAnalyzer.xml'),
        'research_5': read_research_xml(CorePath + '\\ResearchProjects_5_Ship.xml'),
        'research_biotech_mech': read_research_xml(BiotechPath + '\\ResearchProjects_Mechanitor.xml'),
        'research_biotech_misc': read_research_xml(BiotechPath + '\\ResearchProjects_Misc.xml'),
        'research_ideology': read_research_xml(IdeologyPath + '\\ResearchProjects_Misc.xml'),
        'research_royalty_apparel': read_research_xml(RoyaltyPath + '\\ResearchProjects_Apparel.xml'),
        'research_royalty_implants': read_research_xml(RoyaltyPath + '\\ResearchProjects_Implants.xml'),
        'research_royalty_music': read_research_xml(RoyaltyPath + '\\ResearchProjects_MusicalInstruments.xml'),
    }

    def header(string: str) -> str:
        '''create a more visible text header use in a python file'''
        return '\n' + '#' * 79 + '\n# ' + str.upper(string) + '\n' + '#' * 79 + '\n'

    with open('../data/research.py', 'w') as f:
        f.write("\n'''\n")
        f.write('This file contains raw data from the rimworld xml defs, '
                'rewritten as \n python dictionaries for easier and faster use '
                'by archipelago')
        f.write("\n'''\n")
        for key, value in researches.items():
            value = process_parents(value)
            f.write(header(key))
            f.write(key + ' = {}'.format(pp.pformat(value)))
            f.write('\n\n')
            add_numeric_ids(value)

    with open('../data/research_items.py', 'w') as f:
        f.write("\n'''\n")
        f.write('This file contains generated unique ids for RimWorld techs and items.\n'
                'This can be useful to both client and server,\n'
                'as RimWorld relies on defNames while Archipelago uses numeric ids')
        f.write("\n'''\n")
        f.write(header('id to defname'))
        f.write('item_id_to_defName = {}'.format(pp.pformat(item_id_to_defName)))
        f.write(header('id to label'))
        f.write('item_id_to_label = {}'.format(pp.pformat(item_id_to_label)))
        f.write(header('label to id'))
        f.write('label_to_item_id = {}'.format(pp.pformat(label_to_item_id)))

    def analyze_positions():
        values = [research for sublist in researches.values() for research in sublist]
        max_x = 0
        max_y = 0
        x_set: Set[float] = set()
        y_set: Set[float] = set()
        for research in values:
            try:
                x: float = float(research['researchViewX'])
                y: float = float(research['researchViewY'])
                max_x = max(max_x, x)
                max_y = max(max_y, y)
                x_set.add(x)
                y_set.add(y)
            except:
                raise
        print(f"max x {max_x}")
        print(f"max y {max_y}")
        print(f"x set {x_set}")
        print(f"y_set {y_set}")
    # analyze_positions()


if __name__ == "__main__":
    main()
