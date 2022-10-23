class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "0":
                    continue

                result += 1
                self.dfs(grid, i, j)

        return result

    def dfs(self, grid, r, c):
        frontier = [(r, c)]
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while frontier:
            row, col = frontier.pop()
            
            if grid[row][col] == "0":
                continue

            grid[row][col] = "0"
            for i, j in moves:
                newRow = row + i
                newCol = col + j

                if newRow < 0 or newRow >= len(grid):
                    continue
                
                if newCol < 0 or newCol >= len(grid[row]):
                    continue

                if grid[newRow][newCol] == "0":
                    continue

                frontier.append((newRow, newCol))
        