class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        frontier = []
        cost = [[-1] * len(row) for row in grid]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if not grid[i][j]:
                    continue
                frontier.append((i, j))
                cost[i][j] = 0
        
        distance = 1
        change = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while frontier:
            newFrontier = []
            for i, j in frontier:
                for changeI, changeJ in change:
                    newI = i + changeI
                    newJ = j + changeJ
                    if newI < 0 or newI >= len(grid):
                        continue
                    if newJ < 0 or newJ >= len(grid[0]):
                        continue
                    if cost[newI][newJ] != -1:
                        continue
                    
                    cost[newI][newJ] = distance
                    newFrontier.append((newI, newJ))
                
            distance += 1
            frontier = newFrontier
        
        frontier = [(-cost[0][0], 0, 0)]
        while frontier:
            currCost, i, j = heapq.heappop(frontier)
            if cost[i][j] == -1:
                continue

            currCost = -currCost
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return currCost
            
            cost[i][j] = -1
            for changeI, changeJ in change:
                newI = i + changeI
                newJ = j + changeJ

                if newI < 0 or newI >= len(grid):
                    continue
                if newJ < 0 or newJ >= len(grid[0]):
                    continue
                if cost[newI][newJ] == -1:
                    continue
                
                newCost = min(currCost, cost[newI][newJ]) 
                heapq.heappush(frontier, (-newCost, newI, newJ))
            
        return -1 
