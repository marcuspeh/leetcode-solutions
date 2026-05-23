class Solution:
    def check(self, nums: List[int]) -> bool:
        i = 0
        n = len(nums)
        while i + 1 < n and nums[i] <= nums[i + 1]:
            i = i + 1
        if i == n - 1:
            return True
        j = i + 1
        while j + 1 < n and nums[j] <= nums[j + 1]:
            j = j + 1
        if j == n - 1 and nums[j] <= nums[0]:
            return True
        else:
            return False