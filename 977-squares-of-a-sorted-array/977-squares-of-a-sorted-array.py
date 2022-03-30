class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        start = 0
        end = len(nums) - 1
        
        # binary search for first positive number
        while start < end:
            mid = (end - start) // 2 + start
            
            if nums[mid] >= 0:
                end = mid
            else:
                start = mid + 1
        
        # start == end -> starting location of first postive number
        
        start -= 1
        
        result = []
        while start >= 0 and end < len(nums):
            if -nums[start] < nums[end]:
                result.append(nums[start] ** 2)
                start -= 1
            else:
                result.append(nums[end] ** 2)
                end += 1
        
        for i in range(start, -1, -1):
            result.append(nums[i] ** 2)
            
        for i in range(end, len(nums)):
            result.append(nums[i] ** 2)
                
        return result