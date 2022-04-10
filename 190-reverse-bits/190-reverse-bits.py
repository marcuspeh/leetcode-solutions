class Solution:
    def reverseBits(self, n: int) -> int:
        value = 0
        for i in range(32):
            value = (value << 1 )| (n & 1)
            n = n >> 1
        return value