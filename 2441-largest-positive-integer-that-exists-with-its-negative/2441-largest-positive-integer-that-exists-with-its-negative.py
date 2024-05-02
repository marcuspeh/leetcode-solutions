class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        seen = set()
        result = -1
        for num in nums:
            if -num in seen:
                result = max(result, abs(num))
            seen.add(num)
        return result