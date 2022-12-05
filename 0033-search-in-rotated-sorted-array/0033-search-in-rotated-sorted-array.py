class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        
        while start < end:
            mid = start + (end - start) // 2
            
            if nums[mid] < nums[end]:
                end = mid
            else:
                start += 1
        
        rotation = start
        start = 0
        end = len(nums) - 1
        
        while start < end:
            mid = start + (end - start) // 2
            actualMid = (mid + rotation) % len(nums)
            
            if nums[actualMid] < target:
                start = mid + 1
            else:
                end = mid 
                
        index = (start + rotation) % len(nums)
        
        return index if nums[index] == target else -1