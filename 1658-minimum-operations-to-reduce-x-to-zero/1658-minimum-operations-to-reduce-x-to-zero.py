class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        prefix = {0: 0}
        prev = 0
        
        result = float("inf")
        for i in range(len(nums)):
            prev += nums[i]
            prefix[prev] = i + 1
            if prev == x:
                result = i + 1
            
        prev = 0
        for i in range(len(nums) - 1, -1, -1):
            prev += nums[i]
            target = x - prev
            if target in prefix and prefix[target] <= i:
                result = min(result, len(nums) - i + prefix[target])
        
        return result if result != float("inf") else -1
    