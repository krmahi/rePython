import heapq
from collections import Counter

# heapify O(nlogn)
class solution:
    def topkfrequent(self, nums: list[int], k: int)-> list[int]:
        count = Counter(nums)
        maxHeap = []

        for key, value in count.items():
            maxHeap.append([-value, key])
        
        heapq.heapify(maxHeap)
        res = []

        while k > 0:
            value, key = heapq.heappop(maxHeap)
            res.append(key) 
            k -= 1
        
        return res
    
#heapify with inbuilt function
class solution:
    def topkfrequent(self, nums: list[int], k: int)-> list[int]:
        count = Counter(nums)
        return [item for item, _ in heapq.nlargest(k, count.items(),key = lambda p: p[1])] # [item for item, freq in [[1,3], [2,2]]]
    