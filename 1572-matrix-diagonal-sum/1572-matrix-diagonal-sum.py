class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        result = 0
        
        for i in range(len(mat)):
            if i == len(mat[i]) - i - 1:
                result += mat[i][i]
            else:
                result += mat[i][i]
                result += mat[i][len(mat[i]) - i - 1]
        return result