class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxElement = max(nums)
        result = 0
        start = 0
        appearance = 0
        
        for end in range(len(nums)):
            num = nums[end]
            
            if num == maxElement:
                appearance += 1
            
            while appearance == k:
                if nums[start] == maxElement:
                    appearance -= 1
                start += 1
            
            result += start
        return result