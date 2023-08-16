class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]
        
        for i in nums:
            result.append(result[-1] * i)
        
        curr = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= curr
            curr *= nums[i]
        
        result.pop()
        return result