class Solution:
    def squareSum(self, n):
        result = 0
        while n:
            result += (n % 10) ** 2
            n //= 10
            
        return result
        
    def isHappy(self, n: int) -> bool:
        visited = set()
        
        while n > 1:
            visited.add(n)
            
            n = self.squareSum(n)
            
            if n in visited:
                return False
    
        return n == 1
        