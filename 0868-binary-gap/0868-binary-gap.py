class Solution:
    def binaryGap(self, n: int) -> int:
        result = 0
        count = 0
        has1 = False
        for i in range(32):
            if n == 0:
                continue
            
            bit = n & 0x1
            n = n >> 1

            if bit == 0:
                if has1:
                    count += 1
                continue
            
            if has1:
                result = max(result, count + 1)
            
            has1 = True
            count = 0
        
        return result