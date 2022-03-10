class Solution:
    def findMin(self, nums: List[int]) -> int:
        # smallest - biggest
        # biggest - smalleest
        
        if len(nums) == 1:
            return nums[0]
        
        start = 0
        end = len(nums) -1
        
        # If still in order
        if nums[start] < nums[end]:
            return nums[start]
        
        # [4,5,6,7,0,1,2]
        while start < end:
            mid = (end - start) // 2 + start
            
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            
            if nums[mid] <= nums[start]:
                end = mid + 1
            else:
                start = mid + 1
                
        return nums[start]