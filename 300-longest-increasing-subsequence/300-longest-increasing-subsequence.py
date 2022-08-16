class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            left = 0
            right = size
            while left < right:
                mid = left + (right - left) // 2
                if tails[mid] < x:
                    left = mid + 1
                else:
                    right = mid
            tails[left] = x
            size = max(left + 1, size)
        return size

