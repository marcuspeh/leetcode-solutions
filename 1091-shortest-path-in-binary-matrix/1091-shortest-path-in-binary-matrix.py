class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] or grid[-1][-1]:
            return -1
        
        if len(grid) == 1:
            return 1;
        
        moves = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1)
        ]
        
        frontier = [(0, 0)]
        steps = 1
        
        while frontier:
            newFrontier = []
            
            for row, col in frontier:
                if grid[row][col]:
                    continue
                
                grid[row][col] = 1
                
                for i, j in moves:
                    newRow = row + i
                    newCol = col + j
                    
                    if newRow < 0 or newRow >= len(grid):
                        continue
                        
                    if newCol < 0 or newCol >= len(grid):
                        continue
                        
                    if newRow == len(grid) - 1 and newCol == len(grid) - 1:
                        return steps + 1
                    
                    if grid[newRow][newCol]:
                        continue
                    
                    newFrontier.append((newRow, newCol))
                    
            frontier = newFrontier
            steps += 1
        return -1