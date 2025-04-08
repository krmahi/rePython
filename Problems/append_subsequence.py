class solution:
    def make_subsequence(self, s: str, t: str) -> int:
        n = len(t)
        if not s: return n
        if not t: return 0
        j = 0
        for i in range(len(s)):
            if j < n: 
                if s[i] == t[j]: j += 1
        return 0 if j >= n else len(t[j:])