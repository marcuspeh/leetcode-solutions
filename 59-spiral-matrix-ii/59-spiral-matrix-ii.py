class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]
        
        matrix = [[0 for i in range(n)] for j in range(n)]
        
        
        counter = 1
        
        for offset in range(n // 2):
            # Fill row
            for i in range(offset, n - offset):
                matrix[offset][i] = counter
                counter += 1

            # Fill right
            for i in range(offset + 1, n - offset):
                matrix[i][n - 1 - offset] = counter
                counter += 1

            # Fill bottom
            for i in range(offset + 1, n - offset):
                matrix[n - 1 - offset][n - i - 1] = counter
                counter += 1

            # Fill left
            for i in range(offset + 1, n - offset - 1):
                matrix[n - i - 1][offset] = counter
                counter += 1
            
        if matrix[offset + 1][offset + 1] == 0:
            matrix[offset + 1][offset + 1] = counter
            
        return matrix