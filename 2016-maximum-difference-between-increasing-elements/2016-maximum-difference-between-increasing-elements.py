class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        smallest = nums[0]
        diff = float("-inf")
        for i in range(1, len(nums)):
            if smallest < nums[i]:
                diff = max(diff, nums[i] - smallest)
            smallest = min(smallest, nums[i])
        
        if diff == float("-inf"):
            return -1
        return diff

