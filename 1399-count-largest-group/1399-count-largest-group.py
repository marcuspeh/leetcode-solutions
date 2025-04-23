class Solution:
    def countLargestGroup(self, n: int) -> int:
        seen = {}
        largest = 0
        count = 0
        for i in range(1, n + 1):
            total = self.sum(i)
            if total not in seen:
                seen[total] = 0
            seen[total] += 1
            
            if largest == seen[total]:
                count += 1
            elif seen[total] > largest:
                count = 1
                largest = seen[total]
        
        return count

    def sum(self, n):
        result = 0
        while n > 0:
            result += n % 10
            n //= 10
        return result