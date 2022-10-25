class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        moves = [(1,0), (-1, 0), (0, 1), (0, -1)]
        
        q = deque([(i,j) for i in range(m) for j in range(n) if grid[i][j] == 1])    
        
        if len(q) == m * n or len(q) == 0: 
            return -1
        
        level = 0
        
        while q:
            size = len(q)
            for _ in range(size):
                row, col = q.popleft()
                for x, y in moves:
                    newRow = row + x 
                    newCol = col + y
                    if newRow < 0 or newRow >= m:
                        continue
                    if newCol < 0 or newCol >= n:
                        continue
                    if grid[newRow][newCol] != 0:
                        continue
                        
                    q.append((newRow, newCol))
                    grid[newRow][newCol] = 1
            level += 1
        return level-1