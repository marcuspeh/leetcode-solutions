class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        
        left = 0
        right = position[-1]
        
        while left < right:
            mid = left + (right - left) // 2
            
            if self.isValid(position, m, mid):
                left = mid + 1
            else:   
                right = mid
                
        return left - 1
        
    def isValid(self, position, m, k):
        prev = position[0]
        m -= 1
        
        for i in position:
            if i >= prev + k:
                prev = i
                m -= 1
        
        return m <= 0
            