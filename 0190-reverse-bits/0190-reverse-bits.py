class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0

        for i in range(32):
            result = (result << 1) | (n & 0x1)
            n = n >> 1
        
        return result