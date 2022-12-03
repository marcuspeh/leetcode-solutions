class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        indexWithZero = []
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] != 0:
                    continue
                indexWithZero.append((i, j))
                
        for i, j in indexWithZero:
            # Fill horizontal
            for y in range(len(matrix[i])):
                matrix[i][y] = 0
            for x in range(len(matrix)):
                matrix[x][j] = 0