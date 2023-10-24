class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n + 1):
            result.append(self.count(i))
        
        return result
    
    @cache
    def count(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        if n % 2 == 0:
            return self.count(n // 2)
        
        return self.count(n // 2) + 1