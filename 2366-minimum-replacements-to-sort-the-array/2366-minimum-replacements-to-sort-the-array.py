class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        prev = nums.pop()
        result = 0
        
        while nums:
            nextNumber = nums.pop()
            prev, count = self.split(nextNumber, prev)
            result += count
                
        return result
            
    
    def split(self, n, prev):
        if prev >= n:
            return n, 0
    
        breakBy = (n + prev - 1) // prev
        return n // breakBy, breakBy - 1
        
        