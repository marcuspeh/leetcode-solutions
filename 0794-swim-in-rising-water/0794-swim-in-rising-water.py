class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        time = 0
        pq = [(grid[0][0], 0, 0)]
        visited = {(0, 0)}
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while pq:
            time = pq[0][0]
            while time >= pq[0][0]:
                _, i, j = heapq.heappop(pq)
                if i == len(grid) - 1 and j == len(grid[0]) - 1:
                    return time

                for x, y in moves:
                    newX = i + x
                    newY = j + y
                    
                    if newX < 0 or newX >= len(grid):
                        continue
                    if newY < 0 or newY >= len(grid[0]):
                        continue
                    if (newX, newY) in visited:
                        continue
                    
                    visited.add((newX, newY))
                    heapq.heappush(pq, (grid[newX][newY], newX, newY))
                
        return -1