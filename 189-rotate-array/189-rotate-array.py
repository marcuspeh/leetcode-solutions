class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        first = nums[:-k]
        second = nums[-k:]
        nums.clear()
        nums.extend(second)
        nums.extend(first)
        