class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start = 1
        end = 1 << 32
        
        while start < end:
            mid = (end - start) // 2 + start
            sqMid = mid * mid
            
            if sqMid < num:
                start = mid + 1
            else:
                end = mid

        return start * start == num
            