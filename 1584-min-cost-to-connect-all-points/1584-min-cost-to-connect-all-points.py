class Node:
    def __init__(self, curr):
        self.curr = {curr}
    
    def insert(self, other):
        self.curr.update(other.curr)

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        points = list(tuple(point) for point in points)
        cache = {point: Node(point) for point in points}
        
        heap = []
        for i in range(len(points)):
            for j in range(1, len(points)):
                distance = self.calcDistance(points[i], points[j])
                heapq.heappush(heap, (distance, points[i], points[j]))
                
        result = 0
        while heap:
            cost, point1, point2 = heapq.heappop(heap)
            if cache[point1] == cache[point2]:
                continue
                
            node1 = cache[point1]
            node2 = cache[point2]
            if len(node1.curr) < len(node2.curr):
                node1, node2 = node2, node1
            
            node1.insert(node2)
            result += cost
            for node in node2.curr:
                cache[node] = node1
        
        return result
        
    def calcDistance(self, point1, point2):
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
        