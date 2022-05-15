class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        curr = 0
        
        for n in nums:
            if n:
                nums[curr] = n
                curr += 1
            
        while curr < len(nums):
            nums[curr] = 0
            curr += 1
        