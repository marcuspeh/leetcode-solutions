class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rowCount = [0] * len(mat)
        colCount = [0] * len(mat[0])
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                rowCount[i] += mat[i][j]
                colCount[j] += mat[i][j]
        
        result = 0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if rowCount[i] != 1 or colCount[j] != 1:
                    continue
                if mat[i][j] != 1:
                    continue
                
                result += 1
        
        return result