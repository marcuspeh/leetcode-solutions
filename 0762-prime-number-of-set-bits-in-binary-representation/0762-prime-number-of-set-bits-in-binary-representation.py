class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        result = 0
        for num in range(left, right + 1):
            result += self.isPrimeBit(num)
        return result
    
    def isPrimeBit(self, n):
        primes = {2, 3, 5, 7, 11, 13, 17, 19}

        count = 0
        for i in range(32):
            if n == 0:
                break
            count += n & 0x1
            n = n >> 1
        
        if count in primes:
            return 1
        return 0