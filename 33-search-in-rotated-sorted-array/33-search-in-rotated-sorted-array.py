class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        
        while start < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid
        
        return self.binarySearch(nums, target, start)
    
    def binarySearch(self, nums, target, rotation):        
        
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = (start + end) // 2
            realMid = (mid + rotation) % len(nums)
            
            if (nums[realMid] == target):
                return realMid
            
            if nums[realMid] < target:
                start = mid + 1
            else:
                end = mid - 1
        
        return -1