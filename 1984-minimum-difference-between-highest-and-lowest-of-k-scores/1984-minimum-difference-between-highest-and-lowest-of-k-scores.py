class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        result = nums[-1] - nums[0]
        for i in range(len(nums) - k + 1):
            result = min(result, nums[i + k - 1] - nums[i])
        return result