class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        freshOrange = set()
        rotton = []
        time = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    freshOrange.add((i, j))
                elif grid[i][j] == 2:
                    rotton.append((i, j))
        
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while freshOrange and rotton:
            time += 1
            
            newRotton = []
            
            for row, col in rotton:
                for i, j in moves:
                    newRow = row + i
                    newCol = col + j
                    
                    if newRow < 0 or newRow >= len(grid):
                        continue
                    if newCol < 0 or newCol >= len(grid[0]):
                        continue
                    if grid[newRow][newCol] !=1:
                        continue
                        
                    newRotton.append((newRow, newCol))
                    grid[newRow][newCol] = 2
                    freshOrange.remove((newRow, newCol))
                    
            rotton = newRotton
            
        return -1 if freshOrange else time