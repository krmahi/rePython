class solution:
    def greatest_element(self, arr: list[int]) -> list[int]:
        n = len(arr)
        max_el = arr[n - 1]
        arr[n - 1] = -1
        for i in range(n - 2, -1, -1):
            tmp = arr[i]
            arr[i] = max_el
            if max_el < tmp: max_el = tmp
        return arr
    
    # 2nd solution

    def greatest_element(self, arr: list[int]) -> list[int]:
        n = len(arr)
        if n == 1:
            arr[0] = -1
            return arr
        max_el = max(list[1, n - 1])
        arr[0] = max_el
        for i in range(1, n - 1):
            if arr[i] == max_el: max_el = max(list[i + 1:n - 1])
            arr[i] = max_el
        arr[n - 1] = -1
        return arr