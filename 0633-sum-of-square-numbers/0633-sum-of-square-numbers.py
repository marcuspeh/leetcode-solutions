class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c <= 2 or self.isSquare(c):
            return True
        
        for i in range(1, int(math.sqrt(c)) + 1):
            square = i * i
            
            if self.isSquare(c - square):
                return True
            
        return False
        
    def isSquare(self, num):
        return int(math.sqrt(num)) ** 2 == num