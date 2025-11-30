class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        toRemove = sum(nums) % p
        if toRemove == 0:
            return 0
            
        result = len(nums)
        cache = {0: -1} 
        curr = 0
        for idx in range(len(nums)):
            num = nums[idx]
            curr = (curr + num) % p

            valueToFind1 = (p + curr - toRemove) % p
            if valueToFind1 in cache:
                result = min(result, idx - cache[valueToFind1])

            cache[curr] = idx
        
        if result == len(nums):
            return -1

        return result