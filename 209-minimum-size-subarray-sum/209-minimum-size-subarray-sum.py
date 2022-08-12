class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = 1000000
        start = 0
        end = 0
        total = 0
        
        while end < len(nums):
            total += nums[end]
            end +=  1
            
            if total >= target:
                while total - nums[start] >= target:
                    total -= nums[start]
                    start += 1
                result = min(end - start, result)
                total -= nums[start]
                start += 1
        
        return 0 if result == 1000000 else result