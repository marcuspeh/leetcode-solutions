class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        limit = len(nums) // 2
        
        # Use to count how many of each elements
        cache = {}
        
        for n in nums:
            if n in cache:
                cache[n] += 1
            else:
                cache[n] = 1
                
            if cache[n] > limit:
                return n