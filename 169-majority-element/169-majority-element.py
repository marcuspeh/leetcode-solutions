class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Use count
        cache = {}
        highest = nums[0]
        
        for n in nums:
            if n in cache:
                cache[n] += 1
            else:
                cache[n] = 1
                
            if cache[n] > cache[highest]:
                highest = n
        
        return highest
        
        