class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        
        start = 0
        end = len(nums) 
        
        while start < end:
            mid = (end - start) // 2 + start
            
            if nums[mid] > mid:
                start = mid + 1
            else:
                end = mid
           
        return -1 if start < len(nums) and start == nums[start] else start
    