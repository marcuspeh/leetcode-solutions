class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rowStart = 0
        rowEnd = len(matrix) - 1
        colStart = 0
        colEnd = len(matrix[0]) - 1
        
        result = []
        i = 0
        j = 0
        
        while len(result) < len(matrix) * len(matrix[0]):
            # top
            for j in range(colStart, colEnd + 1): 
                result.append(matrix[i][j])
            
            # right
            for i in range(rowStart + 1, rowEnd + 1):
                result.append(matrix[i][j])
            
            if (rowStart < rowEnd and colStart < colEnd):
                # bottom
                for j in range(colEnd - 1, colStart -1, -1):
                    result.append(matrix[i][j])

                # left
                for i in range(rowEnd - 1, rowStart, -1):
                    result.append(matrix[i][j])
                
            rowStart += 1
            rowEnd -= 1
            colStart += 1
            colEnd -= 1
        
        return result