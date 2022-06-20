class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        result = 0
        curr = 0
        for i in range(len(nums) - 2):
            if nums[i + 1] - nums[i] == nums[i + 2] - nums[i + 1]:
                curr += 1
                result += curr
            else:
                curr = 0
        return result