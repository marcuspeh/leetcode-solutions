class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        
        for i in range(len(nums)):
            toFind = target - nums[i]
            
            if toFind in cache:
                return [i, cache[toFind]]
            
            cache[nums[i]] = i