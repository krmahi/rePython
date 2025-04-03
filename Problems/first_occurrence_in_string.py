class solution:
    def occurrence(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack): return -1
        i, j = 0, len(needle)
        while j <= len(haystack):
            if needle in haystack[i:j]: return i
            else: 
                i += 1
                j += 1
        return -1

My_solution = solution()
haystack = "butsudsad"
needle = "sad"
print(My_solution.occurrence(haystack, needle))