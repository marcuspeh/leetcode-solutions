MOD = 10 ** 9 + 7

class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        table = [[{} for _ in row] for row in grid]
        table[0][0][grid[0][0] % k] = 1

        for i in range(1, len(grid)):
            val = grid[i][0]
            prevMap = table[i - 1][0]
            currMap = table[i][0]
            self.processMap(prevMap, currMap, val, k)
        
        for j in range(1, len(grid[0])):
            val = grid[0][j]
            prevMap = table[0][j - 1]
            currMap = table[0][j]
            self.processMap(prevMap, currMap, val, k)
        
        for i in range(1, len(grid)):
            for j in range(1, len(grid[i])):
                val = grid[i][j]
                prevMapLeft = table[i - 1][j]
                currMap = table[i][j]
                self.processMap(prevMapLeft, currMap, val, k)

                prevMapTop = table[i][j - 1]
                self.processMap(prevMapTop, currMap, val, k)
        
        lastMap = table[-1][-1]
        if 0 not in lastMap:
            return 0
        return lastMap[0]
    
    def processMap(self, prevMap, currMap, val, k):
        for curr, count in prevMap.items():
            newVal = (val + curr) % k
            if newVal in currMap:
                count += currMap[newVal]
            currMap[newVal] = count % MOD

