class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        result = 0
        
        for ant in left:
            result = max(result, ant)
        
        for ant in right:
            result = max(result, n - ant)
            
        return result