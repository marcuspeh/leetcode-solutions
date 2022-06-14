class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = -1 << 32
        curr = -1 << 32
        
        for n in nums:
            curr = max(curr + n, n)
            result = max(result, curr)
            
        return result
        
        