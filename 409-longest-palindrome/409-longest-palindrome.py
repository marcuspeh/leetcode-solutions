class Solution:
    def longestPalindrome(self, s: str) -> int:
        cache = {}
        pairs = 0
        for i  in s:
            if i not in cache:
                cache[i] = 1
            else:
                pairs += 1
                del cache[i]
        
        if cache:
            return pairs * 2 + 1
        else:
            return pairs * 2