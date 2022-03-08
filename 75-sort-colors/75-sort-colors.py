class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 3 pointer for each color
        red = -1
        unsorted = 0
        blue = len(nums)
        
        while unsorted < blue:
            print(nums)
            if nums[unsorted] == 0:
                nums[red + 1], nums[unsorted] = nums[unsorted], nums[red + 1]
                red += 1
                unsorted += 1
            elif nums[unsorted] == 1:
                unsorted += 1
            else:
                nums[blue - 1], nums[unsorted] = nums[unsorted], nums[blue - 1]
                blue -= 1
                