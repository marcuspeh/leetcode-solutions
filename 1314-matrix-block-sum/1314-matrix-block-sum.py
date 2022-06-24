class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        table = [[0 for i in range(len(mat[0]) + 1)] for j in range(len(mat) + 1)]
        
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                table[i + 1][j + 1] = table[i][j + 1] + table[i + 1][j] - table[i][j] + mat[i][j]
                
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                mat[i][j] = self.getSum(table, i - k, j - k, i + k, j + k)
            
        return mat
        
    def getSum(self, table, row1, col1, row2, col2):
        if row1 < 0:
            row1 = 0
        if col1 < 0:
            col1 = 0
            
        if row2 >= len(table) - 1:
            row2 = len(table) - 2
        
        if col2 >= len(table[0]) - 1:
            col2 = len(table[0]) - 2
        return table[row2 + 1][col2 + 1] - table[row1][col2 + 1] - table[row2 + 1][col1] + table[row1][col1]