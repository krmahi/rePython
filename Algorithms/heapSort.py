class solution:
    def sortArray(self, nums: list) -> list:
        if not nums: return nums
        self.heapsort(nums)
        return nums

    def heapify(self, arr, n, i):
        l = i * 2 + 1 #* left child for arr with 0 indexing
        r = i * 2 + 2 #* right child for arr with 0 indexing
        largest = i
        if l < n and arr[l] > arr[largest]: largest = l
        if r < n and arr[r] > arr[largest]: largest = r
        if largest != i:
            arr[largest], arr[i] = arr[i], arr[largest]
            self.heapify(arr, n, largest)

    #! MAX HEAP    
    def heapsort(self, arr):
        n = len(arr)
        #* this will find the max element of the list
        for i in range(n // 2 - 1, -1, -1): #* n // 2 for parent and n // 2 - 1 bcz in list index start from 0 and we dont have any 0 element in heap already
            self.heapify(arr, n, i)

        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self.heapify(arr, i, 0)

my_sort = solution()
# nums = [21,0,0,0,14,5,34,234,63,2]
nums = []
print(my_sort.sortArray(nums))
