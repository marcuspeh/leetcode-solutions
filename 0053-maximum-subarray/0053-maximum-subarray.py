class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr =  float('-inf')
        result = curr
        
        for num in nums:
            curr = max(curr + num, num)
            result = max(result, curr)
            
        return result