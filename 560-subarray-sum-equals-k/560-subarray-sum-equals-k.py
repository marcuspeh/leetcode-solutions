class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        total = 0
        
        cache = {0: 1}
        
        for i in range(len(nums)):
            total += nums[i]
            if total - k in cache:
                count += cache[total - k]
            
            if total in cache:
                cache[total] += 1
            else:
                cache[total] = 1
        return count
        
        