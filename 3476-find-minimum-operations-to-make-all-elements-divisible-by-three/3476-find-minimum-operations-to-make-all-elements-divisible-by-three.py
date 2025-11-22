class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            mod = num % 3
            result += min(mod, 3 - mod)
        
        return result