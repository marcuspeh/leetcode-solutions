class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        curr = 1
        k -= 1
        while k > 0:
            step = self.count(n, curr, curr + 1)
            
            if step <= k:
                curr += 1
                k -= step
                continue
                
            curr *= 10
            k -= 1

        return curr
        
    def count(self, n, num1, num2):
        steps = 0
        while num1 <= n:
            steps += min(n + 1, num2) - num1
            num1 *= 10
            num2 *= 10
        return steps