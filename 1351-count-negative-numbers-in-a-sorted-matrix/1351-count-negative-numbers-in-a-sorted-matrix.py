class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        i = len(grid) - 1
        j = 0
        result = 0
        lengthRow = len(grid[0])
        
        while i >= 0 and j < lengthRow:
            if grid[i][j] < 0:
                result += lengthRow - j
                i -= 1
            else:
                j += 1
        
        return result