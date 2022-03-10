class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # Check if it is land and not visited
                if grid[i][j] == "1":
                    self.dfs(i, j, grid)
                    result += 1
        
        return result
    
    def dfs(self, row, col, grid):
        frontier = [(row, col)]
        
        possibleMoves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while frontier:
            i, j = frontier.pop(0)
            
            if grid[i][j] != "1":
                continue
            
            grid[i][j] = "2"
            
            for moves in possibleMoves:
                tempI = i + moves[0]
                tempJ = j + moves[1]
                
                if tempI < 0 or tempJ < 0 or tempI >= len(grid) or tempJ >= len(grid[0]):
                    continue
                    
                frontier.append((tempI, tempJ))
                
            