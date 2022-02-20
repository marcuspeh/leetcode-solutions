class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = -1 << 31
        currCount = 0
        
        for n in nums:
            currCount = max(currCount + n, n)
            result = max(currCount, result)
        
        return result
        