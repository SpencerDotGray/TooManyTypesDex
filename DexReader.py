
import csv
from pprint import pprint

class DexReader:

    pokemon = {}

    def __init__(self):

        with open('dex.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile)

            for (index, row) in enumerate(spamreader):
                
                if index > 0:
                    type1 = row[2]
                    type2 = None if row[3] == '' else row[3]
                    type3 = None if row[4] == '' else row[4]
                    self.pokemon[row[1]] = [type1, type2, type3]

    def get_pokemon_types(self, name):

        name = name.lower().capitalize()

        if name not in self.pokemon.keys():
            return None

        return self.pokemon[name]


    def get_all_pokemon(self):
        return self.pokemon.keys()
