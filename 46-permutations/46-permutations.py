class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def helper(lst, nums):
            nonlocal result
            
            if not nums:
                result.append(lst)
            
            for i in range(len(nums)):
                helper(lst + [nums[i]], nums[:i] + nums[i + 1:])
                
        helper([], nums)
        
        return result