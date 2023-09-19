
class StatOrganizer:

    def get_refined_list(stats, desiredVal):

        if stats is None:
            return []

        returnList = []

        for key in stats.keys():
            if stats[key] == desiredVal:
                returnList.append(key)
        
        return returnList