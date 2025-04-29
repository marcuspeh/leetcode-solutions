class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        result = 0
        target = max(nums)
        freq = 0
        start = 0
        for end in range(len(nums)):
            if nums[end] == target:
                freq += 1
            while freq == k:
                if nums[start] == target:
                    freq -= 1
                start += 1
            result += start
        return result
