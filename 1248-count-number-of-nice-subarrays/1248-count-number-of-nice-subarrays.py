class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        result = 0
        
        start = 0
        end = 0
        count = 0
        while end < len(nums):
            while end < len(nums) and count < k:
                if nums[end] % 2:
                    count += 1
                end += 1
            
            if count < k:
                break
            
            leftEven = 1
            while nums[start] % 2 == 0:
                start += 1
                leftEven += 1
        
            rightEven = 1
            while end < len(nums) and nums[end] % 2 == 0:
                end += 1
                rightEven += 1
                
        
            result += leftEven * rightEven
            start += 1
            count -= 1
        
        return result
            
            
        
        return result