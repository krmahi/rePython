class solution:
    def subsequence(self, s:str, t:str) -> bool:
        if not s: return True
        if len(s) > len(t): return False
        j = 0
        for i in t:
            if i == s[j]: 
                j += 1
                if j == len(s): return True
        return False

my_sol = solution()
t = "a"
s = "aa"
print(my_sol.subsequence(s, t))
