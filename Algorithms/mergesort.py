class solution:
    def sortArray(self, nums:list) -> list:
        self.mergesort(nums, 0, len(nums) - 1)
        return nums
    
    def mergesort(self, arr, l, r):
        if l == r: return
        m = (l + r) // 2
        self.mergesort(arr, l, m) #* -> left
        self.mergesort(arr, m + 1, r) #* -> right
        self.merge(arr, l, m, r)
        return
    
    def merge(self, arr, l, m, r):
        left, right = arr[l:m + 1], arr[m + 1:r + 1] #* -> left and right temp arrays
        i, j, k = l, 0, 0 #* i -> nums and arr, j -> left, k -> right

        while j < len(left) and k < len(right):
            if left[j] <= right[k]:
                arr[i] = left[j]
                j += 1
            else:
                arr[i] = right[k]
                k += 1
            i += 1

        while j < len(left):
            arr[i] = left[j]
            j += 1
            i += 1
        
        while j < len(right):
            arr[i] = right[k]
            k += 1
            i += 1

sort = solution()
nums = [123,14,6,213,6,1,7,2,7,3,7422,1]
print(sort.sortArray(nums))
