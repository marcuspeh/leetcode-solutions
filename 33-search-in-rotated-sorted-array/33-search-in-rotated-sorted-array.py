class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        
        while start < end:
            mid = (end - start) // 2 + start
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid
        
        rotated = start
        
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = (end - start) // 2 + start
            realMid = (mid + rotated) % len(nums)
            
            if nums[realMid] == target:
                return realMid
            elif nums[realMid] < target:
                start = mid + 1
            else:
                end = mid - 1
                
        return -1