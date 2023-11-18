class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        total = k
        start = 0
        
        for i in range(len(nums)):
            total += nums[i]
            if total < nums[i] * (i - start + 1):
                total -= nums[start]
                start += 1
        
        return i - start + 1
        
