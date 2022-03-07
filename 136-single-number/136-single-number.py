class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Option 1: cache
        # Option 2: use xor
        # a ^ a = 0
        result = 0
        for n in nums:
            result ^= n
        return result