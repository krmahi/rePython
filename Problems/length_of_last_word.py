class solution:
    def length_of_word(self, s:str)->int:
        n = len(s)
        count = 0
        for i in range(n - 1, -1, -1):
            if count == 0 and s[i] == " ": continue
            if count >= 1 and s[i] == " ": break
            count += 1
        return count