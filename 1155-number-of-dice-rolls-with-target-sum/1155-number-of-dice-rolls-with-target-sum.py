class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10 ** 9 + 7
        
        table = [[0 for _ in range(target + 1)] for _ in range(n + 1)]
        table[0][0] = 1
        
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                for n in range(1, k + 1):
                    if j - n < 0:
                        break
                    table[i][j] += table[i - 1][j - n]
                    table[i][j] %= MOD
                    
        return table[-1][-1]
                