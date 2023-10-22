class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        result = nums[k]
        
        left = k
        right = k
        currMin = nums[k]
        
        while left > 0 and right < len(nums) - 1:
            if nums[left - 1] < nums[right + 1]:
                right += 1
                currMin = min(currMin, nums[right])
            else:
                left -= 1
                currMin = min(currMin, nums[left])
            result = max(result, currMin * (right - left + 1))
            
        while left > 0:
            left -=  1
            currMin = min(currMin, nums[left])
            result = max(result, currMin * (right - left + 1))
            
        while right < len(nums) - 1:
            right += 1
            currMin = min(currMin, nums[right])
            result = max(result, currMin * (right - left + 1))
        
        return result