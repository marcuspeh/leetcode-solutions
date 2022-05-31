class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(floor(sqrt(c)) + 1):
            search = self.binarySearch(c - i * i)
            
            if search != -1:
                return True
            
        return False
            
    def binarySearch(self, a):
        start = 0
        end = floor(sqrt(a))
        
        while start < end:
            mid = (end - start) // 2 + start
            
            if mid * mid < a:
                start = mid + 1
            else:
                end = mid
        
        return start if start * start == a else -1