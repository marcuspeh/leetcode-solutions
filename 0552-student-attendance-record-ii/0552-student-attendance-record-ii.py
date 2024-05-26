class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        cache = [[[-1 for _ in range(2)] for _ in range(3)] for _ in range(n)]
        
        def helper(n, totalAbsent, consectiveLate):
            nonlocal cache            
            if totalAbsent >= 2 or consectiveLate >= 3:
                return 0
            
            if n == 0:
                return 1
            
            if cache[n - 1][consectiveLate][totalAbsent] != -1:
                return cache[n - 1][consectiveLate][totalAbsent]
            
            # Present
            result = helper(n - 1, totalAbsent, 0)
            
            # Absent
            result += helper(n - 1, totalAbsent + 1, 0) 
                
            # Late
            result += helper(n - 1, totalAbsent, consectiveLate + 1) 
            
            result %= MOD
            cache[n - 1][consectiveLate][totalAbsent] = result
            return result 
        
        return helper(n, 0, 0)
            