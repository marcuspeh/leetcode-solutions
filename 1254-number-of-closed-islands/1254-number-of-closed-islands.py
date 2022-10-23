class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        result = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != 0:
                    continue

                isClosed = self.checkIsClosed(grid, i, j)
                if isClosed:
                    result += 1
        return result
        
    def checkIsClosed(self, grid, r, c):
        frontier = [(r, c)]
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        isSurrounded = True

        while frontier:
            row, col = frontier.pop()
            if grid[row][col] != 0:
                continue
            grid[row][col] = 2

            for i, j in moves:
                newRow = row + i
                newCol = col + j

                if newRow < 0 or newRow >= len(grid):
                    isSurrounded = False
                    continue

                if newCol < 0 or newCol >= len(grid[newRow]):
                    isSurrounded = False
                    continue
                frontier.append((newRow, newCol))

        return isSurrounded
                




