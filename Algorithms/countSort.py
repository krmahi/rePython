from collections import defaultdict

class solution:
    def countsort(self, nums: list[int]) -> list[int]:
        count  = defaultdict(int)
        minval, maxval = min(nums), max(nums)

        for num in nums:
            count[num] += 1
        
        index = 0
        for value in range(minval, maxval + 1):
            while count[value] > 0:
                count[value] -= 1
                nums[index] = value
                index += 1

my_sort = solution()
nums = [1,4,1,561,71,7,1,5,1,5,15778,1141,13]
my_sort.countsort(nums)
print(nums)