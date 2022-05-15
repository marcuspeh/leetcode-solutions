class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        curr = 0
        pointer = 0
        
        while pointer < len(nums):
            while pointer < len(nums) and nums[pointer] == 0:
                pointer += 1
            
            if pointer >= len(nums):
                break
            
            nums[curr] = nums[pointer]
            curr += 1
            pointer += 1
            
        while curr < len(nums):
            nums[curr] = 0
            curr += 1