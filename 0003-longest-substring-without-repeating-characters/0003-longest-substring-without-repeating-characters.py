class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cache = {}
        result = 0
        currStart = 0
        
        for i in range(len(s)):
            word = s[i]
            
            if word in cache:
                currStart = max(currStart, cache[word] + 1)
            
            cache[word] = i
            result = max(result, i - currStart + 1)
        return result