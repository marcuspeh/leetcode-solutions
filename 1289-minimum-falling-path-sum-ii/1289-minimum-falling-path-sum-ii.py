class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        min1, min2 = self.getSmallest2Pair(grid[0])
        for i in range(1, len(grid)):
            min1, min2 = self.getSmallest2Pair(grid[i], min1, min2)
            
        return min1[0]
                
            
    def getSmallest2Pair(self, row, prev1=(0, -1), prev2=(0, -1)):
        min1 = None
        min2 = None
        
        for col in range(len(row)):
            if col == prev1[1]:
                val = row[col] + prev2[0]
            else:
                val = row[col] + prev1[0]
            
            if min1 is None or val <= min1[0]:
                min2 = min1
                min1 = (val, col)
            elif min2 is None or val <= min2[0]:
                min2 = (val,  col)
        return min1, min2