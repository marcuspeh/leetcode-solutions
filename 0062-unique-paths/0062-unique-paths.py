class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        table = [1 for _ in range(n)]
        
        for i in range(1, m):
            for j in range(1, n):
                table[j] += table[j - 1]
                
        return table[-1]