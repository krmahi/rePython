import math
class solution:
    def bananas(self, piles:list[int], h: int) -> int:
        # bruste force -> O(max_el * n)
        k = math.ceil(sum(piles) / h)
        while True:
            hours = 0
            for i in piles:
                hours += math.ceil(i / k)
            if hours <= h: return k
            k += 1
        
        # Optimised (Binary search's algo) -> O(log(max_el * n))
        l , r = math.ceil(sum(piles) / h), max(piles)
        res = r
        while l <= r:
            k = (l + r) // 2
            hours = 0
            for i in piles:
                hours += math.ceil(l / k)

            if hours <= h:
                res = min(res, k)
                r = k - 1
            else: l = k + 1
        return res 