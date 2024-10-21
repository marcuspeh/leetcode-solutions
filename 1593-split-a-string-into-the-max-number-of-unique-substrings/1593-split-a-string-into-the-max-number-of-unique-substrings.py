class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def helper(idx, cache):
            if idx >= len(s):
                return 0
            
            result = 0
            for i in range(idx + 1, len(s) + 1):
                curr = s[idx: i]
                if curr not in cache:
                    cache.add(curr)
                    result = max(result, helper(i, cache) + 1)
                    cache.remove(curr)
            
            return result
            
        return helper(0, set())