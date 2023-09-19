
from ChartReader import ChartReader
from DexReader import DexReader
from StatOrganizer import StatOrganizer 
from pprint import pprint
import json

cr = ChartReader()
dr = DexReader()

def get_pokemon(name):

    output = {}

    types = dr.get_pokemon_types(name)
    stats = cr.get_all_effectiveness(types)

    output['Name'] = name
    output['Types'] = types
    output['1x'] = StatOrganizer.get_refined_list(stats, 1)
    output['0.5x'] = StatOrganizer.get_refined_list(stats, 0.5)
    output['0.25x'] = StatOrganizer.get_refined_list(stats, 0.25)
    output['0.125x'] = StatOrganizer.get_refined_list(stats, 0.125)
    output['2x'] = StatOrganizer.get_refined_list(stats, 2)
    output['4x'] = StatOrganizer.get_refined_list(stats, 4)
    output['8x'] = StatOrganizer.get_refined_list(stats, 8)
    output['0x'] = StatOrganizer.get_refined_list(stats, 0)

    return output

output = []

for pokemon in dr.get_all_pokemon():

    output.append(get_pokemon(pokemon))

with open('Pokemon.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=4)