class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        curr = 0
        blue = len(nums) - 1
        red = 0
        while curr <= blue:
            if nums[curr] == 0:
                tmp = nums[curr]
                nums[curr] = nums[red]
                nums[red] = tmp
                curr += 1
                red += 1
            elif nums[curr] == 1:
                curr += 1
            else:
                tmp = nums[curr]
                nums[curr] = nums[blue]
                nums[blue] = tmp
                blue -= 1
        