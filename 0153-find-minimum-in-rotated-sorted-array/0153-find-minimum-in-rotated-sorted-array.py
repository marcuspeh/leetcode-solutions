class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        """
        1 2 3 4 5 6 7 8
        ^     |       ^

        7 8 1 2 3 4 5 6
        ^     |       ^

        5 6 7 8 1 2 3 4
        ^     |       ^


        right > mid = right = mid
        right >= mid = left = mid
        """

        while left < right:
            mid = left + (right - left) // 2
            if nums[right] > nums[mid]:
                right = mid
            else:
                left = mid + 1
        
        return nums[left]