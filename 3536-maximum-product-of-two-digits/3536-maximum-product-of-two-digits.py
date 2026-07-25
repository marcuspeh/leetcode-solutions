class Solution:
    def maxProduct(self, n: int) -> int:
        n1 = n2 = 0
        while n > 0:
            currNum = n % 10
            n //= 10

            if currNum > n1:
                n2 = n1
                n1 = currNum
                continue
            if currNum > n2:
                n2 = currNum
        
        return n1 * n2