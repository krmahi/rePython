from collections import Counter
from collections import deque
import heapq

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        count = Counter(tasks) # map of counts {task : occ}
        maxHeap = [cnt for cnt in count.values()]
        heapq._heapify_max(maxHeap) # log26 A -> Z
        t = 0
        queue = deque() # -> pair [cnt - 1, t + n]
        while maxHeap or queue:
            cnt = 0
            if maxHeap: 
                cnt = heapq.heappop(maxHeap)
                heapq._heapify_max(maxHeap)
                cnt -= 1
            t += 1
            if cnt: queue.append([cnt, t + n])
            if queue and queue[0][1] <= t:
                tmp, time = queue.popleft()
                heapq.heappush(maxHeap, tmp)
                heapq._heapify_max(maxHeap)
        return t
    
class solution_2:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        count = Counter(tasks) # map of counts {task : occ}
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap) # log26 A -> Z
        t = 0
        q = deque() # -> pair [cnt - 1, t + n]
        while maxHeap or q:
            if not maxHeap: t = q[0][1] 
            else: 
                t += 1
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt: q.append([cnt, t + n])
            if q and q[0][1] <= t:
                heapq.heappush(maxHeap, q.popleft()[0])
        return t

my_sol = solution_2()
print(my_sol.leastInterval(["A","C","A","B","D","B"], 1))