class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        totalXor = 0
        for num in nums:
            totalXor ^= num
            
        needToFlip = totalXor ^ k
        result = 0
        for bit in bin(needToFlip)[2:]:
            if bit == '1':
                result += 1
        return result