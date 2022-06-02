class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        
        result = 0
        total = 1
        left = 0
        right = 0
        
        while right < len(nums):
            total *= nums[right]
            
            while total >= k:
                total /= nums[left]
                left += 1
                
            result += right - left + 1
            right += 1
        
        return result