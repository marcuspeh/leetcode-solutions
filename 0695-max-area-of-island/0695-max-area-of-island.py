class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    continue

                area = self.getArea(grid, i, j)
                result = max(result, area)
        
        return result

    def getArea(self, grid, r, c):
        frontier = [(r, c)]
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        result = 0

        while frontier:
            row, col = frontier.pop()

            if grid[row][col] == 0:
                continue
            grid[row][col] = 0
            result += 1
            for i, j in moves:
                newRow = row + i
                newCol = col + j

                if newRow < 0 or newRow >= len(grid):
                    continue

                if newCol < 0 or newCol >= len(grid[newRow]):
                    continue
                
                frontier.append((newRow, newCol))
        
        return result
