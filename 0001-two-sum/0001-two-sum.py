class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {}
        for i in range(len(nums)):
            num = nums[i]
            requiredPrev = target - num
            if requiredPrev in idx:
                return [idx[requiredPrev], i]
            
            idx[num] = i
