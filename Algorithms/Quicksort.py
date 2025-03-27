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

# O(nlogn) -> time (Avg, and best case) == worst case (O(n^2)), o(1) -> space
class solution_2:
    def sortArray(self, nums: list) -> list:
        if len(nums) <= 1: return nums
        self.quicksort(nums, 0, len(nums) - 1)
        return nums
    
    def quicksort(self, arr, l, h):
        if l < h:
            partition = self.get_partition(arr, l, h)
            self.quicksort(arr, l, partition - 1)
            self.quicksort(arr, partition + 1, h)

    def get_partition(self, arr, l, h):
        pivot, i, j = arr[l], l, h
        while i < j:
            while arr[i] <= pivot and i < h: i += 1
            while arr[j] > pivot and j > l: j -= 1
            if i < j: arr[i], arr[j] = arr[j], arr[i]
        arr[l], arr[j] = arr[j], arr[l]
        return j

sort = solution_2()
nums = [2,4,1,8,9,12,2]
print(sort.sortArray(nums))
    