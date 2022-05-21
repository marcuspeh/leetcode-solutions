class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        
        while start < end:
            mid = (end - start) // 2 + start
            
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid
        return start if nums[start] == target else -1