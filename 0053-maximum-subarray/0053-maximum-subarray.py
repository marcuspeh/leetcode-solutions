class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = float("-inf")
        curr = float("-inf")
        
        for num in nums:
            curr = max(curr + num, num)
            result = max(result, curr)
        
        return result