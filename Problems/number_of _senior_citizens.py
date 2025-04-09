class solution:
    def seniorCitizens(self, details:list) ->int:
        if not details: return 0
        count = 0
        for i in details:
            if int(i[-4:-2] > 60): count += 1
        return count