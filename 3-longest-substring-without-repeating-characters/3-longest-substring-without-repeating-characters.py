class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: 
        cache = {} 
        result = 0 
        start = 0
        
        for i in range(len(s)): 
            character = s[i] 
            
            if character in cache:
                start = max(start, cache[character] + 1)
            
            cache[character] = i
            
            result = max(result, i - start + 1)
            
        return result