import heapq

class Solution:
    def numSquares(self, n: int) -> int:
        frontier = [(0, n)]
        
        while frontier:
            node = heapq.heappop(frontier)
            
            for i in range(1, floor(sqrt(node[1])) + 1):
                newN = node[1] - i * i
                
                if newN == 0:
                    return node[0] + 1
                else:
                    heapq.heappush(frontier, (node[0] + 1, newN))
        
        