import heapq
class Solution:
    def __init__(self, k:int, nums:list[int]):
        self.Minheap, self.k = nums, k
        heapq.heapify(self.Minheap)
        while len(self.Minheap) > self.k: heapq.heappop(self.Minheap)
    
    def add(self, val: int) -> int:
        heapq.heappush(self.Minheap, val)
        if len(self.Minheap) > self.k: heapq.heappop(self.Minheap)
        return self.Minheap[0]