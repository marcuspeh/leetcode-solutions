class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def helper(lst, perm):
            nonlocal result
            if not lst:
                result.append(perm)
                
            for i in range(len(lst)):
                helper(lst[:i] + lst[i + 1:], perm + [lst[i]])
                
        helper(nums, [])
        
        return result