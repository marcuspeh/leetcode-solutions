class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        min_increments = 0
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                continue
            increment = nums[i - 1] + 1 - nums[i]
            min_increments += increment
            nums[i] = nums[i - 1] + 1

        return min_increments