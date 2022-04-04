class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    result = max(result, self.dfs(grid, i, j))
                    
        return result
        
    def dfs(self, grid, row, col):
        if row < 0 or row >= len(grid):
            return 0
        if col < 0 or col >= len(grid[0]):
            return 0
        
        if grid[row][col] == 0:
            return 0
        
        grid[row][col] = 0
        
        result = 1
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for r, c in moves:
            result += self.dfs(grid, row + r, col + c)
            
        return result