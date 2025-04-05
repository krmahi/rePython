class solution:
    def score(self, s: str) -> int:
        if not s: return 0
        if len(s) == 1: return ord(s[0])
        score = 0
        for i in range(len(s) - 1):
            score += abs(ord(s[i]) - ord(s[i + 1]))
        return score 