class solution:
    def search(self, matrix:list[list[int]], target: int) -> bool:
        if not matrix: return False

        def BinarySearch(list:list[int], low: int, high: int)-> bool:
            if low > high: return False
            mid = high + low // 2
            if list[mid] > target: return BinarySearch(list, mid + 1, high)
            elif list[mid] == target: return True
            else: return BinarySearch(list, low, mid - 1)

        for i in matrix:
            m = len(i) - 1
            if len(i):
                res = BinarySearch(i, 0, m)
                if res: return True
        return False