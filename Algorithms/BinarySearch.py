class solution:
    def search(self, nums: list, target: int) -> int:
        if not nums: return -1
        nums.sort()
        def BinarySearch(low, high):
            if low > high: return -1
            mid = (low + high) // 2
            if nums[mid] == target: return mid
            elif target > nums[mid]: return BinarySearch(mid + 1, high)
            else: return BinarySearch(low, mid - 1)
        
        return BinarySearch(0, len(nums) - 1)
    
my_search = solution()
nums = [123,1,5,1,62167,8,4,8,525,980,54,523,12]
target = 62167
print(my_search.search(nums, target))