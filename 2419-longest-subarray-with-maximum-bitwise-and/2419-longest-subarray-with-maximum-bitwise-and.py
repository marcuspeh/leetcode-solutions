class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        highestNum = max(nums)
        result = 0
        curr = 0
        for num in nums:
            if num == highestNum:
                curr += 1
            else:
                curr = 0
            
            result = max(result, curr)
        return result