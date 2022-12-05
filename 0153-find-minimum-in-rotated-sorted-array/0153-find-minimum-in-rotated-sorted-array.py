class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        if  nums[0] < nums[-1]:
            return nums[0]
        
        # left lower = go left
        # left higher = return curr
        # right lower = go right
        # right higher = go left
        
        # start < mid = 
        
        start = 0
        end = len(nums) - 1
        
        while start < end:
            mid = start + (end - start) // 2
            
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            
            if nums[mid] > nums[start]:
                start = mid + 1
            else:
                end = mid
                
        return start