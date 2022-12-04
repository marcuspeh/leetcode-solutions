class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "0":
                    continue
                
                self.dfs(grid, row, col)
                count += 1
        return count
        
    def dfs(self, grid, row, col):        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        frontier = [(row, col)]
        
        while frontier:
            row, col = frontier.pop()
            if grid[row][col] == "0":
                continue
            grid[row][col] = "0"
            for i, j in directions:
                newRow = row + i
                newCol = col + j
                
                if newRow < 0 or newRow >= len(grid):
                    continue
                if newCol < 0 or newCol >= len(grid[0]):
                    continue
                if grid[newRow][newCol] == "0":
                    continue
                
                frontier.append((newRow, newCol))