class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        prev = 0
        curr = 0
        
        while curr < len(nums):
            if nums[curr] != 0:
                nums[prev] = nums[curr]
                prev += 1
            curr += 1
        
        while prev < len(nums):
            nums[prev] = 0
            prev += 1
        
        return nums