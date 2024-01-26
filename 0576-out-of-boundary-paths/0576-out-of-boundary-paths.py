class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MODULO =  10 ** 9 + 7
        table = [[0 for _ in range(n)] for _ in range(m)]
        result = 0
        table[startRow][startColumn] = 1
        
        for _ in range(maxMove):
            newTable = [[0 for _ in range(n)] for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if i == 0:
                        result += table[i][j]
                        result %= MODULO
                    if j == 0:
                        result += table[i][j]
                        result %= MODULO
                    if i == m - 1:
                        result += table[i][j]
                        result %= MODULO
                    if j == n - 1:
                        result += table[i][j]
                        result %= MODULO
                    
                    if i > 0:
                        newTable[i][j] += table[i - 1][j]
                        newTable[i][j] %= MODULO
                    if j > 0:
                        newTable[i][j] += table[i][j - 1]
                        newTable[i][j] %= MODULO
                    if i < m - 1:
                        newTable[i][j] += table[i + 1][j]
                        newTable[i][j] %= MODULO
                    if j < n - 1:
                        newTable[i][j] += table[i][j + 1]
                        newTable[i][j] %= MODULO
                        
            table = newTable
        return result