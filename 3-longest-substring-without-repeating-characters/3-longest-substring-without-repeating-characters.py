class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cache = {}
        result = 0
        start = 0
        
        for i in range(len(s)):
            letter = s[i]
            
            if letter in cache:
                start = max(start, cache[letter] + 1)
            
            cache[letter] =  i
            
            result = max(result, i - start + 1)
            
        return result