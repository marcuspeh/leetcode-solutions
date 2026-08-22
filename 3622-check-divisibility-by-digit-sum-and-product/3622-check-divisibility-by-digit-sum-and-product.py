class Solution:
    def checkDivisibility(self, n: int) -> bool:
        total = 0
        product = 1
        curr = n
        while curr:
            num = curr % 10
            curr = curr // 10
            total += num
            product *= num
        
        return (n % (total + product)) == 0