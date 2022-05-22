class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        isIncreasing = None
        
        for i in range(1, len(nums)):
            if isIncreasing == None:
                if nums[i - 1] < nums[i]:
                    isIncreasing = False
                elif nums[i - 1] > nums[i]:
                    isIncreasing = True
            else:
                if isIncreasing:
                    if nums[i - 1] < nums[i]:
                        return False
                else:
                    if nums[i - 1] > nums[i]:
                        return False
        return True