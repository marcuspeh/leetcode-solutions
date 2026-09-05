class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0 
        end = len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] < nums[end]:
                end = mid
            else:
                start = mid + 1
    
        rotations = start
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            num = nums[(mid + rotations) % len(nums)]
            if num < target:
                start = mid + 1
            else:
                end = mid
        
        idx = (start + rotations) % len(nums)
        if nums[idx] == target:
            return idx

        return -1