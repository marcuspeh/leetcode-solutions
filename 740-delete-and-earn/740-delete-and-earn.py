class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        cache = {}
        maxPoints = 0
        
        for i in nums:
            if i not in cache: 
                cache[i] = 0
            cache[i] += i
            maxPoints = max(maxPoints, i)
        
        memo = {}
        def helper(n):
            nonlocal memo
            if n in memo:
                return memo[n]
            score = cache[n] if n in cache else 0
            if n == 0:
                return 0
            elif n == 1:
                return score
            else:
                updated = max(helper(n - 2) + score, helper(n - 1))
                memo[n] = updated
                return updated
        
        return helper(maxPoints)