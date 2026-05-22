class Solution:
    def search(self, nums: List[int], target: int) -> int:
        high = len(nums) - 1
        low = 0
        while low <= high:
            x = low + (high - low) // 2
            if nums[x] == nums[high]:
                high = x - 1
                low = x
            elif nums[x] > nums[high]:
                low = x + 1
            elif nums[x] < nums[high]:
                high = x
        if target <= nums[-1]:
            high = len(nums)
        else:
            high = low
            low = 0
        if nums[low] == target:
            return low
        while low < high:
            x = low + (high - low) // 2
            if nums[x] == target:
                return x
            elif nums[x] > target:
                high = x
            else:
                low = x + 1
        return -1