class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        prevDiff = nums[1] - nums[0]
        result = 1 if prevDiff == 0 else 2
        
        for i in range(2, len(nums)):
            newDiff = nums[i] - nums[i - 1]
            if prevDiff <= 0 and newDiff > 0:
                result += 1
                prevDiff = newDiff
            elif prevDiff >= 0 and newDiff < 0:
                result += 1
                prevDiff = newDiff
                
        return result
            