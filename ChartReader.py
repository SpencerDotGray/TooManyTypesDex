
import csv
from pprint import pprint

class ChartReader:

    chart = {}
    all_types = []

    reverse_check ={
        '2': '0.5',
        '0.5': '2',
        '4': '0.25',
        '0.25': '4',
        '0': '0',
        '1': '1'
    }

    def __init__(self):

        with open('typechart.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile)

            for (index, row) in enumerate(spamreader):

                if index == 1:
                    self.all_types = row[2:-1]
                elif index == 65:
                    pass
                else:

                    row = row[1:-1]

                    if row[0].strip() != '':
                        self.chart[row[0].upper()] = row[1:]
        
        for i in range(0, len(self.all_types)):
            self.all_types[i] = self.all_types[i].upper()
        
        
    def get_effectiveness(self, attacking, defending):

        attacking = attacking.upper()
        defending = defending.upper()

        index = self.all_types.index(defending)

        return self.chart[attacking][index]
    
    def get_super_effective_types(self, defending):

        defending = defending.upper()
        index = self.all_types.index(defending)

        weaknesses = []

        for key in self.chart.keys():

            stat = self.chart[key][index]
            if stat.strip() != '' and float(stat) > 1:
                weaknesses.append(key)
        
        return weaknesses
    

    def get_all_effectiveness_helper(self, type1: str, type2: str = None, type3: str = None):

        if type2 is None and type3 is None:
            return self.get_all_effectiveness_one(type1)
        elif type2 is not None and type3 is None:
            return self.get_all_effectiveness_two(type1, type2)
        else:
            return self.get_all_effectiveness_three(type1, type2, type3)
    

    def get_all_effectiveness(self, type_list: list):

        if type_list is None:
            return None

        if len(type_list) == 1:
            return self.get_all_effectiveness_helper(type_list[0])
        elif len(type_list) == 2:
            return self.get_all_effectiveness_helper(type_list[0], type_list[1])
        else:
            return self.get_all_effectiveness_helper(type_list[0], type_list[1], type_list[2])


    def get_all_effectiveness_one(self, type1):

        type1 = type1.strip()

        index = self.all_types.index(type1.upper())
        
        returnList = {}

        for key in self.chart.keys():

            returnList[key] = self.chart[key][index]
        
        return returnList
    

    def get_all_effectiveness_two(self, type1, type2):

        type1 = type1.strip()
        type2 = type2.strip()

        index = self.all_types.index(type1.upper())
        index2 = self.all_types.index(type2.upper())

        returnList = {}

        for key in self.chart.keys():

            if (type1.upper() == 'REVERSE' or type2.upper() == 'REVERSE'):
                returnList[key] = float(self.reverse_check[self.chart[key][index]]) * float(self.reverse_check[self.chart[key][index2]])
            else:
                returnList[key] = float(self.chart[key][index]) * float(self.chart[key][index2])
            
        
        return returnList
    

    def get_all_effectiveness_three(self, type1, type2, type3):

        type1 = type1.strip()
        type2 = type2.strip()
        type3 = type3.strip()

        index = self.all_types.index(type1.upper())
        index2 = self.all_types.index(type2.upper())
        index3 = self.all_types.index(type3.upper())

        returnList = {}

        for key in self.chart.keys():

            if (type1.upper() == 'REVERSE' or type2.upper() == 'REVERSE' or type3.upper() == 'REVERSE'):
                returnList[key] = float(self.reverse_check[self.chart[key][index]]) * float(self.reverse_check[self.chart[key][index2]]) * float(self.reverse_check[self.chart[key][index3]])
            else:
                returnList[key] = float(self.chart[key][index]) * float(self.chart[key][index2]) * float(self.chart[key][index3])
        
        return returnList