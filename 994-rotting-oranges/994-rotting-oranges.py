class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
        
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        frontier = []
        time = 0
        fresh = 0
        
        # Fill up number of fresh and position of rotton
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    frontier.append((i, j))
                    
        while frontier and fresh > 0:
            newFrontier = []
            time += 1
            
            for row, col in frontier:
                for i, j in moves:
                    newRow = row + i
                    newCol = col + j
                    
                    if newRow < 0 or newRow >= len(grid):
                        continue
                        
                    if newCol < 0 or newCol >= len(grid[0]):
                        continue
                    
                    if grid[newRow][newCol] == 1:
                        grid[newRow][newCol] = 2
                        fresh -= 1
                        newFrontier.append((newRow, newCol))
                        
            frontier = newFrontier
            
        return time if fresh == 0 else -1