class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cache = {}
        result = 0
        prevIndex = 0
        
        for i in range(len(s)):
            letter = s[i]
            if letter in cache:
                prevIndex = max(cache[letter] + 1, prevIndex)
            
            result = max(i - prevIndex + 1, result)
            cache[letter] = i
        
        return result