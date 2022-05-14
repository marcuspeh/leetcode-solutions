class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        smallestDistance = 1 << 32
        index = -1
        
        for ind in range(len(points)):
            i, j = points[ind]
            if i == x and j == y:
                return ind
            
            if i == x:
                distance = abs(j - y)
                if distance < smallestDistance:
                    smallestDistance = distance
                    index = ind
                
            if j == y:
                distance = abs(i - x)
                
                if distance < smallestDistance:
                    smallestDistance = distance
                    index = ind
                
        return index