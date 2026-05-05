class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(mat)
        for i in range(n//2):
            for j in range(i, n-i-1):
                mat[i][j],     mat[j][n-1-i], mat[n-1-i][n-1-j], mat[n-1-j][i] = \
                mat[n-1-j][i], mat[i][j],     mat[j][n-1-i],     mat[n-1-i][n-1-j]
        