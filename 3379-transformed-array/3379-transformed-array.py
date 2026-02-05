class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            num = nums[i]
            idx = (i + num) % len(nums)
            result.append(nums[idx])
        
        return result