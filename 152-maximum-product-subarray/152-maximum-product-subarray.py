class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        lowest = nums[0]
        highest = nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]
            
            if num < 0:
                lowest, highest = highest, lowest
                
            lowest = min(lowest * num, num)
            highest = max(highest * num, num)
            
            result = max(result, highest)
            
        return result