class Solution:
    def freqAlphabets(self, s: str) -> str:
        for i in range(26, 0, -1): 
            if i > 9:
                 s = s.replace(str(i) + '#', chr(96 + i))
            else:
                s = s.replace(str(i), chr(96 + i))
        return s