class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        cache = {}
        result = -1
        
        for i in range(len(s)):
            character = s[i]
            if character not in cache:
                cache[character] = i
                continue
            
            result = max(result, i - cache[character] - 1)
        
        return result