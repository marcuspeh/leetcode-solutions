class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        start = 0
        currCost = 0
        result = 0
        for i in range(len(s)):
            currCost += abs(ord(s[i]) - ord(t[i]))
            
            while currCost > maxCost:
                currCost -= abs(ord(s[start]) - ord(t[start]))
                start += 1
                
            result = max(result, i - start + 1)
            
        return result
            
            