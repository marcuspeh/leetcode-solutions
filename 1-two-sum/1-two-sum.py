class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        
        for i in range(len(nums)):
            n = nums[i]
            other = target - n
            
            if other in cache:
                return [i, cache[other]]
                
            cache[n] = i
            
        