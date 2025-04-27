import heapq
# sorting
class solution:
    def Klargest(self, nums: list[int], k: int)-> int:
        nums.sort()
        return nums[len(nums) - k]

# heap (PQ)
class solution:
    def Klargest(self, nums: list[int], k: int)-> int:
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        # or 
        # return heapq.nlargest(k, nums)[-1]
        return nums[0]
    