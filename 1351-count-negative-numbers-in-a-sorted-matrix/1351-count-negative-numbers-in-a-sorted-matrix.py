class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        i = len(grid) - 1
        j = 0
        result = 0
        
        while i >= 0 and j < len(grid[0]):
            if grid[i][j] < 0:
                result += len(grid[0]) - j
                i -= 1
            else:
                j += 1
        
        return result