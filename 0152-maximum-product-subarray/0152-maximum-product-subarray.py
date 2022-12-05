class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = float('-inf')
        negative = float('inf')
        positive = float('-inf')
        
        for n in nums:
            if n < 0:
                negative, positive = min(n, positive * n), max(n, negative * n)
            else:
                negative = min(n, negative * n)
                positive = max(n, positive * n)                
            result = max(result, positive)
        return result