class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def helper(nums, curr):
            nonlocal result
            
            if not nums:
                result.append(curr)
            
            for i in range(len(nums)):
                helper(nums[:i] + nums[i + 1:], curr + [nums[i]])
        
        helper(nums, [])
        return result