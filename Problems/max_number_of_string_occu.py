from collections import defaultdict

# 0 ms time 
class solution:
    def countstringoccu(self, text:str)-> int:
        if not text or len(text) < 7: return 0
        map = defaultdict(int)
        for i in text:
            if i in "balon": map[i] += 1
        
        balloon = {'b':1,'a':1,'l':2,'o':2,'n':1}
        return min(map[char] // balloon[char] for char in balloon)
    
# 3 ms time  but slight space optimisation 

class solution:
    def coutstringoccu(self, text:str) -> int:
        if not text or len(text) < 7:return 0
        map = defaultdict(int)
        for i in text: 
            if i in 'balon': map[i] += 1
        
        if len(map) < 5: return 0
        map['l'] //= 2
        map['o'] //= 2
        return min(map.values())
