class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result += self.get4DivisorSum(num)

        return result

    def get4DivisorSum(self, num):
        total = 1 + num
        found = False
        start  = 2
        while start * start <= num:
            other = num // start
            if num % start:
                start += 1
                continue
            if found or other == start:
                return 0

            total += start + other
            found = True
            start += 1
        
        if found:
            return total
        
        return 0