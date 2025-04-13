from collections import defaultdict
class solution:
    def wordpattern(self, pattern:str, s:str)-> bool:
        n = len(pattern)
        m = len(s)
        map = defaultdict(str)
        i = j = k = 0
        while i <= n - 1 and j <= m:
            if j == m or s[j] == " ":
                if pattern[i] not in map:
                    if s[k:j] not in map.values():
                        map[pattern[i]] = s[k:j]
                        k = j + 1
                        j += 1
                    else: return False
                else:
                    if map[pattern[i]] == s[k:j]:
                        k = j + 1
                        j += 1
                    else: return False
            else:
                j += 1
                continue
            i += 1
        if j < m or i < n: return False
        return True

my_sol = solution()
p = "aaaa"
s = "aa aa aa"
print(my_sol.wordpattern(p, s))