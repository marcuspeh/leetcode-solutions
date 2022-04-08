class Solution:
    def rob(self, nums: List[int]) -> int:
        a = 0
        b = 0
        
        for i in nums:
            temp = max(a + i, b)
            a = b
            b = temp
            
        return b
        