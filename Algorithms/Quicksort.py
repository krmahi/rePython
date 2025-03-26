class solution:
    def quicksort(self, nums:list) -> list:
        if not nums: return nums
        pivot = nums[0]
        left = [x for x in nums[1:] if x <= pivot]
        right = [x for x in nums[1:] if x > pivot]
        return self.quicksort(left) + [pivot] + self.quicksort(right)
    
sort = solution()
nums = [2,4,1,8,9,12,2]
print(sort.quicksort(nums))