class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        prefix = 0
        for i in range(len(nums)):
            if i == 0:
                prefix += nums[i]
                continue
            if nums[i - 1] + 1 == nums[i]:
                prefix += nums[i]
                continue
            
            break
        
        cache = set(nums)
        while prefix in cache:
            prefix += 1
        
        return prefix