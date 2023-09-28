class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        start = 0
        end = len(nums) - 1
        
        while start < end:
            if nums[start] & 1 == 0:
                start += 1
            else:
                nums[start], nums[end] = nums[end], nums[start]
                end -= 1
        
        return nums
        