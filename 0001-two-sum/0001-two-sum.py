class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        
        for i in range(len(nums)):
            n = nums[i]
            if target - n in cache:
                return (cache[target - n], i)
            cache[n] = i