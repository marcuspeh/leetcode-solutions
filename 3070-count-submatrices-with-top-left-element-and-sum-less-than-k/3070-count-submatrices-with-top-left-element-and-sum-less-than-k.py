class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        rowCount = [0 for _ in range(len(grid[0]))]
        result = 0

        for i in range(len(grid)):
            row = grid[i]
            newRowCount = []
            presum = [0]
            for j in range(len(rowCount)):
                count = rowCount[j] + row[j] + presum[-1]                
                if count > k:
                    break

                presum.append(presum[-1] + row[j])
                newRowCount.append(count)
            
            rowCount = newRowCount
            result += len(rowCount)
        
        return result
                