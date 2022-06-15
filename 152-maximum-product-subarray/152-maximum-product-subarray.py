class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = -1 << 32
        curr = -1 << 32
        smaller = 1 << 32
        bigger = -1 << 32
        
        for n in nums:
            if n < 0:
                smaller, bigger = bigger, smaller
            
            smaller = min(smaller * n, n)
            bigger = max(bigger * n, n)
            result = max(result, bigger)
        
        return result
        
        