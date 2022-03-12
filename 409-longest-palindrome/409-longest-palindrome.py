class Solution:
    def longestPalindrome(self, strs: str) -> int:
        # Number of pairs
        cache = set()
        pairs = 0
        
        for s in strs:
            if s in cache:
                cache.remove(s)
                pairs += 1
            else:
                cache.add(s)
                
        return pairs * 2 + (1 if cache else 0)