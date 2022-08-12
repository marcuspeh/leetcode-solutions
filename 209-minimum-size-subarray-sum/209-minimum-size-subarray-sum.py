class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        count = 1000000
        start = 0
        for i in range(len(nums)):
            total += nums[i]
            if total >= target:
                while start < i and total - nums[start] >= target:
                    total -= nums[start]
                    start += 1
                    
                count = min(count, i - start + 1)
                total -= nums[start]
                start += 1
        return count if count != 1000000 else 0