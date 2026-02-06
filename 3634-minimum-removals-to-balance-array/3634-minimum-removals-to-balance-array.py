class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        right = 0
        result = len(nums)
        for left in range(len(nums)):
            while right < len(nums) and nums[right] <= nums[left] * k:
                right += 1
            
            result = min(result, left + len(nums) - right)
        
        return result