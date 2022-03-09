class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr = [[0 for i in range(m)] for i in range(n)]
        arr[0][0] = 1
        
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue
                
                if i == 0:
                    arr[i][j] = arr[i][j - 1]
                elif j == 0:
                    arr[i][j] = arr[i - 1][j]
                else:
                    arr[i][j] = arr[i - 1][j] + arr[i][j - 1]
        
        return arr[-1][-1]