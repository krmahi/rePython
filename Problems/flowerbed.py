# time ->> O(m) ,space: O(m)
class solution:
    def canplantflower(self, flowerbed:list, n:int)->bool:
        f = [0] + flowerbed + [0]
        for i in range(1, len(f) - 1):
            if f[i - 1] == 0 and f[i] == 0 and f[i + 1] == 0:
                f[i] = 0
                n -= 1
        return n <= 0
    
# optimised space solution: time -> O(m - 2) --> O(m), space -> O(1)

class solution:
    def canplant(self, f:list, n: int) -> bool:
        m = len(f)
        # if len of list -> 1
        if m == 1:
            if f[0] == 0:
                f[0] = 1
                n -= 1
            return n <= 0

        # for first empty slot handling 
        if f[0] == 0 and f[1] == 0:
            f[0] = 1
            n -= 1
        
        # excluding 1st and last
        for i in range(1, m - 1):
            if f[i - 1] == 0 and f[i] == 0 and f[i + 1] == 0:
                f[i] = 1
                n -= 1
        
        # last empty slot handling
        if f[m - 2] == 0 and f[m - 1] == 0: n -= 1
        return n <= 0