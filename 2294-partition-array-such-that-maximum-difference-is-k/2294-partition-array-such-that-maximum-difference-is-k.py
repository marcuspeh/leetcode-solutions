class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        result = 0
        idx = 0
        while idx < len(nums):
            first = nums[idx]
            idx += 1
            while idx < len(nums) and nums[idx] - first <= k:
                idx += 1
            
            result += 1
        
        return result
