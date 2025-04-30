import heapq

class solution:
    # sorting (nlogn)
    def knearest(self, points:list[list[int]], k:int)->list[list[int]]:
        points.sort(key=lambda p: p[0]**2 + p[1]**2)
        return points[:k]
    
    # minheap
    def minheapknearest(self, points:list[list[int]], k:int)-> list[list[int]]:
        return heapq.nsmallest(k, points, key = lambda p: p[0]**2 + p[1]**2)
    
    # minheap without built in function
    def ksnearest_minheap(self, points:list[list[int]], k:int)-> list[list[int]]:
        minHeap = []
        
        for x, y in points:
            dist = x**2 + y**2
            minHeap.append([dist, x, y])
        
        heapq.heapify(minHeap)
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1
        return res
