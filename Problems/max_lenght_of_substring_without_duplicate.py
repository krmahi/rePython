class solution:
    def subarray(self, s:str)-> int:
        n = len(s)
        if n < 2: return n
        # seen = set()
        map = {}
        left = res = 0
        for r in range(n):
            # while s[r] in seen:
            #     seen.remove(s[left])
            #     left += 1
            # seen.add(s[r])
            if s[r] in map:
                left = max(map[s[r]] + 1, left)
            map[s[r]] = r
            res = max(res, r - left + 1)
        # j = res = i = 0
        # while i < n:
        #     if j < n and s[j] in s[i:j]:
        #         res = max(res, j - i)
        #         i += 1
        #         j = i
        #     else:
        #         j += 1
        return res