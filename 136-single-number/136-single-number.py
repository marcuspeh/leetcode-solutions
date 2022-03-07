class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in nums:
            result ^= i
        return result
     
    # 01 xor 11 xor 01 = 10 xor 01 = 11