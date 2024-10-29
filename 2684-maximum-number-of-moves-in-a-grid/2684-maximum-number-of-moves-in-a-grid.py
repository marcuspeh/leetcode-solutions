class Solution:
    dirs = [-1, 0, 1]

    def DFS(self, row, col, grid, dp):
        M, N = len(grid), len(grid[0])
        if dp[row][col] != -1:
            return dp[row][col]

        max_moves = 0
        for dir in self.dirs:
            new_row, new_col = row + dir, col + 1
            if (
                0 <= new_row < M
                and 0 <= new_col < N
                and grid[row][col] < grid[new_row][new_col]
            ):
                max_moves = max(
                    max_moves, 1 + self.DFS(new_row, new_col, grid, dp)
                )

        dp[row][col] = max_moves
        return max_moves

    def maxMoves(self, grid):
        M, N = len(grid), len(grid[0])
        dp = [[-1] * N for _ in range(M)]

        max_moves = 0
        for i in range(M):
            moves_required = self.DFS(i, 0, grid, dp)
            max_moves = max(max_moves, moves_required)

        return max_moves