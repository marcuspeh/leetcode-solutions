class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        result = float(-inf)
        for i in range(len(nums)):
            result = max(result, abs(nums[i] - nums[(i + 1) % len(nums)]))

        return result