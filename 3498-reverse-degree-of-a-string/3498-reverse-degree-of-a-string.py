class Solution:
    def reverseDegree(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            reverseIdx = 26 - (ord(s[i]) - ord('a'))
            result += reverseIdx * (i + 1)
        return result