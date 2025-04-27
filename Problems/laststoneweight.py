import heapq
class solution:
    def laststoneweight(self, stones: list[int]) -> int:
        while len(stones) > 1:
            heapq._heapify_max(stones)
            y = heapq.heappop(stones)
            heapq._heapify_max(stones)
            x = heapq.heappop(stones)
            if x is not y: heapq.heappush(stones, y - x)
        return stones[0] if stones else 0