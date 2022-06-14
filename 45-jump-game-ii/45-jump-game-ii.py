class Solution:
    def jump(self, nums: List[int]) -> int:
        result = [10001 for _ in range(len(nums))]
        result[0] = 0
        
        for i in range(len(nums)):
            distance = nums[i]
            for j in range(i + 1, i + distance + 1):
                if j >= len(nums):
                    break
                result[j] = min(result[i] + 1, result[j])
        return result [-1]