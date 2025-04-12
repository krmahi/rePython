# unique elements in list
class solution:
    def subsequence(self, words:list) -> list:
        n = len(words)
        if not words or n == 1: return []
        words.sort(key = len)
        substrings = []
        for i in range(n - 1):
            for j in range(i + 1, n - 1):
                if words[i] in words[j]: 
                    substrings.append(words[i])
                    break
        return substrings