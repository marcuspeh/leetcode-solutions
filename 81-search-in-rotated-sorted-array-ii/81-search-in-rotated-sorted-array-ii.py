class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        
        if not n:
            return False
        
        start = 0
        end = n - 1
        
        while start <= end:
            mid = (end - start) // 2 + start
            
            if nums[mid] == target:
                return True
            
            if nums[start] == nums[mid]:
                start += 1
                continue
                
            pivotArray = nums[start] <= nums[mid]
            targetArray = nums[start] <= target
            
            if pivotArray ^ targetArray:
                if (pivotArray):
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                if (nums[mid] < target):
                    start = mid + 1
                else:
                    end = mid - 1
        return False