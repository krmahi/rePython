# brute force O(n^3)
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        res = set()
        nums.sort()
        
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        tmp = [nums[i], nums[j], nums[k]]
                        res.add(tuple(tmp))

        return [list(i) for i in res]
