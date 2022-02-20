class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        container = {}
        for i, j in enumerate(nums):
            if target - j in container:
                return [container[target - j], i]
            container[j] = i
        return [-1, -1]
                