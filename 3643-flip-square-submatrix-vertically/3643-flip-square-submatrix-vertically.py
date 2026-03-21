class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for j in range(y, y + k):
            for offset in range(k // 2):
                temp = grid[x + offset][j]
                grid[x + offset][j] = grid[x + k - offset - 1][j]
                grid[x + k - offset - 1][j] = temp
        return grid