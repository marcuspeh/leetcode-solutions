class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        firstPosition = self.firstBinarySearch(nums, 0, len(nums) - 1, target)
        secondPosition = self.lastBinarySearch(nums, 0, len(nums) - 1, target)
        return [firstPosition, secondPosition]
        
    def firstBinarySearch(self, nums, start, end, target):
        if start > end:
            return -1
        
        mid = (end + start) // 2
        
        if nums[mid] == target and (mid == 0 or target != nums[mid - 1]):
            return mid
        elif nums[mid] < target:
            return self.firstBinarySearch(nums, mid + 1, end, target)
        else:
            return self.firstBinarySearch(nums, start, mid - 1, target)
            
        
    
    def lastBinarySearch(self, nums, start, end, target):
        if start > end:
            return -1
        
        mid = (end + start) // 2
        print(start, end, mid)
        
        if nums[mid] == target and (mid == (len(nums) - 1) or target != nums[mid + 1]):
            return mid
        elif nums[mid] > target:
            return self.lastBinarySearch(nums, start, mid - 1, target)
        else:
            return self.lastBinarySearch(nums, mid + 1, end, target)
            
        