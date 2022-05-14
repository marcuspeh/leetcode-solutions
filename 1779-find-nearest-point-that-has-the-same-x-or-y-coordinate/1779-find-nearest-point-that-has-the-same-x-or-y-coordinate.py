import heapq

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        sameX = []
        sameY = []
        
        for index in range(len(points)):
            i, j = points[index]
            if i == x and j == y:
                return index
            
            if i == x:
                heapq.heappush(sameX, (abs(j - y), index))
                
            if j == y:
                heapq.heappush(sameY, (abs(i - x), index))
                
        if sameX:
            minSameX = heapq.heappop(sameX)
        else:
            minSameX = (1 << 32, -1)
            
        if sameY:
            minSameY = heapq.heappop(sameY)
        else:
            minSameY = (1 << 32, -1)
        
        if minSameX[0] < minSameY[0]:
            return minSameX[1]
        elif minSameX[0] > minSameY[0]:
            return minSameY[1]
        else:
            return min(minSameX[1], minSameY[1])