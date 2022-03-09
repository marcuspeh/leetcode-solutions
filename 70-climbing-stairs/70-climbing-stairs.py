class Solution:
    def climbStairs(self, n: int) -> int:
        # n = (n - 1) + (n - 2)
        a = 0
        b = 1
        
        for i in range(n):
            temp = a + b
            a = b
            b = temp
            
        return temp