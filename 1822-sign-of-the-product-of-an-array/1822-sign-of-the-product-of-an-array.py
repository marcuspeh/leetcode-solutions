class Solution:
    def arraySign(self, nums: List[int]) -> int:
        sign = 1
        
        for n in nums:
            if n < 0:
                sign *= -1
            elif n > 0:
                sign *= 1
            else:
                return 0
            
        return sign